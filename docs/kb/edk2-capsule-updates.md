# Working with UEFI capsule updates in EDK2

## Introduction

The purpose of this document is to provide an overview of means for working with
UEFI update capsules that can be employed by an EDK2-based firmware.  This is,
however, not an exhaustive list of such tools and there are other ways of
managing capsules as is alluded to by the last section.

## Tools in EDK's source tree

[`BaseTools/BinWrappers/PosixLike/GenerateCapsule`][GenerateCapsule] (really
[`BaseTools/Source/Python/Capsule/GenerateCapsule.py`][GenerateCapsule.py]) can
be used to generate/unpack/dump capsules.

[`BaseTools/Source/Python/Pkcs7Sign`][Pkcs7Sign] can be used for signing
without `GenerateCapsule` but test keys there are more interesting.  The keys
come in a form suitable for integration into EDK thus making them a good fit for
initial testing.

`CapsuleApp.efi` ([`MdeModulePkg/Application/CapsuleApp`][CapsuleApp]) can be
used to test posting a capsule from a UEFI Shell (or even a bootloader) in
various modes (normal, mass storage, UX capsule out of a BMP-file) or dump
related information like ESRT (EFI System Resource Table), available
FMP (Firmware Management Protocol) instances or result of a failed update
attempt (it's stored in EFI variables).  To use this application:

- include corresponding INF-file into package's DSC
- do not add it to FDF-file, as it won't be used there
- find the file inside build directory like
  `DasharoPayloadPkgX64/RELEASE_COREBOOT/X64/CapsuleApp.efi` and transfer to
  the system where it needs to be used (likely along with a capsule file)

[GenerateCapsule]: https://github.com/Dasharo/edk2/blob/c30aa2f48b6ed3f60b21436b2eaed7a1bd4687d1/BaseTools/BinWrappers/PosixLike/GenerateCapsule
[GenerateCapsule.py]: https://github.com/Dasharo/edk2/blob/c30aa2f48b6ed3f60b21436b2eaed7a1bd4687d1/BaseTools/Source/Python/Capsule/GenerateCapsule.py
[Pkcs7Sign]: https://github.com/Dasharo/edk2/tree/c30aa2f48b6ed3f60b21436b2eaed7a1bd4687d1/BaseTools/Source/Python/Pkcs7Sign
[CapsuleApp]: https://github.com/Dasharo/edk2/tree/c30aa2f48b6ed3f60b21436b2eaed7a1bd4687d1/MdeModulePkg/Application/CapsuleApp

## `GenerateCapsule` files

The tool is written in Python and can be used standalone after copying a small
subtree of EDK2 sources:

```paths
BaseTools/
├── BinWrappers
│   └── PosixLike
│       └── GenerateCapsule
└── Source
    └── Python
        ├── Capsule/...
        └── Common/...
```

## Capsule information

Capsule is a bundle of:

- zero or more embedded drivers allowing for update code to come with a capsule
  instead of being part of current firmware
- one or more firmware update images (payloads)
- metadata describing each of the payloads

Creation of a capsule requires providing most of that information, the rest
have defaults suitable for most use cases without modifications.

### Required payload metadata

#### Basic information

- `Payload` — path to file containing payload data
- `Guid` — GUID that identifies firmware variant
- `FwVersion` — version of the firmware in the capsule
- `LowestSupportedVersion` — the lowest version that new firmware will allow
  to downgrade to

Versions are 32-bit unsigned integers, requiring a scheme to translate
something like v0.9.1 or v24.05.00.01 into an integer.  Different firmware
variants can employ different translation schemes.

#### Signing information

Signing takes three keys (root, its subkey and subkey's subkey for signing):

- `OpenSslTrustedPublicCertFile` — root key (CA) used for verification
- `OpenSslOtherPublicCertFile` — subkey for capsule updates (included along
  with signature)
- `OpenSslSignerPrivateCertFile` — certificate for signing of the capsules

This structure of signing keys is presupposed by `GenerateCapsule` and
`Pkcs7Sign` but it seems to be a design decision of the tooling rather than a
strict requirement on the length of a signing key chain by UEFI or cryptographic
implementation in EDK2.

### Optional payload metadata

There are a few optional fields used to support updating multiple instances of
the same device (`HardwareInstance`), firmware spread out across several
flash chips (`UpdateImageIndex`), firmware with dependencies (`Dependencies`)
as well as for strengthening security (`MonotonicCount`):

- `HardwareInstance` (defaults to `0`)
- `UpdateImageIndex` (defaults to `1`)
- `Dependencies` (defaults to no dependencies) which is a string in Depex format
- `MonotonicCount` (defaults to `0`) which is a 64-bit unsigned integer that is
  supposed to guard against replay attacks (its value is appended to the payload
  image before signing)

## Capsule creation

### Preparation

#### Picking a GUID

Every firmware variant should have its own GUID which appears in several places:

- ESRT entry describing the firmware
- FMP instance capable of updating the firmware
- capsule metadata

Switching between firmware variables is possible by adjusting GUID and version
fields of a capsule meant to perform the switch.

#### Preparing signing keys

`BaseTools/Source/Python/Pkcs7Sign` contains everything necessary for testing
purposes and that's what will be used below.

Real-world usage requires proper key management.  Key generation is covered by
the README of `Pkcs7Sign` as well as in [tianocore's wiki][wiki-keygen].
`Pkcs7Sign` additionally describes how to integrate generated keys into EDK2's
build system.

[wiki-keygen]: https://github.com/tianocore/tianocore.github.io/wiki/Capsule-Based-System-Firmware-Update-Generate-Keys

#### Preparing `GenerateCapsule`'s input

`GenerateCapsule` supports taking information via command-line keys or using a
JSON file.  Using JSON file for configuration is more flexible and future-proof
because options allow specifying only a single payload per capsule.  That said,
capsule flags are accepted only in form of options.

Example JSON file for a capsule that comes with an embedded FMP and uses test
keys (relative paths assume build of Dasharo coreboot):

```json
{
  "EmbeddedDrivers": [
    {
      "Driver": "../Build/DasharoPayloadPkgX64/RELEASE_COREBOOT/X64/FmpDxe.efi"
    }
  ],
  "Payloads": [
    {
      "Payload": "../../../../../build/coreboot.rom",
      "Guid": "00112233-4455-6677-8899-aabbccddeeff",
      "FwVersion": "0x01020000",
      "LowestSupportedVersion": "0x00080000",

      "OpenSslSignerPrivateCertFile": "BaseTools/Source/Python/Pkcs7Sign/TestCert.pem",
      "OpenSslOtherPublicCertFile": "BaseTools/Source/Python/Pkcs7Sign/TestSub.pub.pem",
      "OpenSslTrustedPublicCertFile": "BaseTools/Source/Python/Pkcs7Sign/TestRoot.pub.pem"
    }
  ]
}
```

Some notes on JSON:

- `GenerateCapsule` warns if `EmbeddedDrivers` isn't provided, having an empty
  array if one doesn't need to embed any drivers is enough to silence the
  warning
- all (even numerical) fields must be given as strings or there will be errors
- paths to files undergo expansion of environment variables
- relative paths are relative to current working directory

#### Building a capsule

The operation is called `--encode`.  JSON file is assumed to be in EDK2's
root directory.  Output files tend to use `.cap` extension.

Commands that can be run from inside Dasharo variant of coreboot's tree with
EDK2 payload:

```bash
cd payloads/external/edk2/workspace/Dasharo/
BaseTools/BinWrappers/PosixLike/GenerateCapsule --encode \
                                                --capflag PersistAcrossReset \
                                                --capflag InitiateReset \
                                                --json-file dasharo.json \
                                                --output dasharo.cap
```

Values from multiple `--capflag` options are combined together.

## Capsule introspection

### Viewing metadata

This dumps capsule information on the screen (doesn't perform signature
verification):

```bash
BaseTools/BinWrappers/PosixLike/GenerateCapsule --dump-info dasharo.cap
```

Example output:

```dump
========
EFI_CAPSULE_HEADER.CapsuleGuid      = 6DCBD5ED-E82D-4C44-BDA1-7194199AD92A
EFI_CAPSULE_HEADER.HeaderSize       = 00000020
EFI_CAPSULE_HEADER.Flags            = 00050000
  OEM Flags                         = 0000
  CAPSULE_FLAGS_PERSIST_ACROSS_RESET
  CAPSULE_FLAGS_INITIATE_RESET
EFI_CAPSULE_HEADER.CapsuleImageSize = 0081852D
sizeof (Payload)                    = 0081850D
--------
EFI_FIRMWARE_MANAGEMENT_CAPSULE_HEADER.Version             = 00000001
EFI_FIRMWARE_MANAGEMENT_CAPSULE_HEADER.EmbeddedDriverCount = 00000001
  sizeof (EmbeddedDriver)                                  = 000179C0
EFI_FIRMWARE_MANAGEMENT_CAPSULE_HEADER.PayloadItemCount    = 00000001
EFI_FIRMWARE_MANAGEMENT_CAPSULE_HEADER.ItemOffsetList      =
  0000000000000018
  00000000000179D8
EFI_FIRMWARE_MANAGEMENT_CAPSULE_IMAGE_HEADER.Version                = 00000003
EFI_FIRMWARE_MANAGEMENT_CAPSULE_IMAGE_HEADER.UpdateImageTypeId      = 00112233-4455-6677-8899-AABBCCDDEEFF
EFI_FIRMWARE_MANAGEMENT_CAPSULE_IMAGE_HEADER.UpdateImageIndex       = 00000001
EFI_FIRMWARE_MANAGEMENT_CAPSULE_IMAGE_HEADER.UpdateImageSize        = 00800B05
EFI_FIRMWARE_MANAGEMENT_CAPSULE_IMAGE_HEADER.UpdateVendorCodeSize   = 00000000
EFI_FIRMWARE_MANAGEMENT_CAPSULE_IMAGE_HEADER.UpdateHardwareInstance = 0000000000000000
EFI_FIRMWARE_MANAGEMENT_CAPSULE_IMAGE_HEADER.ImageCapsuleSupport    = 0000000000000001
sizeof (Payload)                                                    = 00800B05
sizeof (VendorCodeBytes)                                            = 00000000
--------
EFI_FIRMWARE_IMAGE_AUTHENTICATION.MonotonicCount                = 0000000000000000
EFI_FIRMWARE_IMAGE_AUTHENTICATION.AuthInfo.Hdr.dwLength         = 00000AED
EFI_FIRMWARE_IMAGE_AUTHENTICATION.AuthInfo.Hdr.wRevision        = 0200
EFI_FIRMWARE_IMAGE_AUTHENTICATION.AuthInfo.Hdr.wCertificateType = 0EF1
EFI_FIRMWARE_IMAGE_AUTHENTICATION.AuthInfo.CertType             = 4AAFD29D-68DF-49EE-8AA9-347D375665A7
sizeof (EFI_FIRMWARE_IMAGE_AUTHENTICATION.AuthInfo.CertData)    = 00000AD5
sizeof (Payload)                                                = 00800010
--------
No EFI_FIRMWARE_IMAGE_DEP
--------
FMP_PAYLOAD_HEADER.Signature              = 3153534D (MSS1)
FMP_PAYLOAD_HEADER.HeaderSize             = 00000010
FMP_PAYLOAD_HEADER.FwVersion              = 00020000
FMP_PAYLOAD_HEADER.LowestSupportedVersion = 00000000
sizeof (Payload)                          = 00800000
========
```

Don't confuse `EFI_CAPSULE_HEADER.CapsuleGuid` with firmware GUID.  The former
defines kind of the capsule which is always equal to FMP for `GenerateCapsule`.
Firmware GUID appears in the output as
`EFI_FIRMWARE_MANAGEMENT_CAPSULE_IMAGE_HEADER.UpdateImageTypeId`.

### Unpacking a capsule

The following creates a set of `decoded*` files and verifies signatures in the
process:

```bash
BaseTools/BinWrappers/PosixLike/GenerateCapsule \
    --decode dasharo.cap \
    --output decoded \
    --signer-private-cert BaseTools/Source/Python/Pkcs7Sign/TestCert.pem \
    --other-public-cert BaseTools/Source/Python/Pkcs7Sign/TestSub.pub.pem \
    --trusted-public-cert BaseTools/Source/Python/Pkcs7Sign/TestRoot.pub.pem
```

Created files:

- `decoded` — empty file (`GenerateCapsule` needs a fix for this because it will
   even truncate an existing file)
- `decoded.EmbeddedDriver.1.efi` — embedded driver whose name is lost
- `decoded.Payload.1.bin` — first payload, similarly without original name
- `decoded.json` — reconstructed JSON file, although not without troubles (more
   bugs of `GenerateCapsule`):
    + `EmbeddedDrivers` is missing
    + `Dependencies` is set to `None` which won't be parsed correctly

Certificates can be omitted for `--decode`.  In this case signatures won't be
verified but created files should be identical except for corresponding fields
of the output JSON file.

## Capsule authentication

The verification of capsules is performed via
[public-key cryptography][wiki-pkc] (the concepts most relevant here: key pairs
and subkeys).  This security mechanism uses a root key pair like this:

1. Public key is embedded into the firmware at build time (one key is enough,
   but using multiple keys is also supported).
2. Private key is used to (indirectly, via a subkey) sign capsules.
3. Signature embedded in the capsule is validated against the public key when
   an update is attempted to decide whether to perform the update.

Things to note:

- public root key is well-known
- private root key is stored in a safe place and nobody but the owner should
  know it, otherwise there is no security and whoever has access to the key can
  compromise the firmware (which might as well be considered insecure if the key
  is no longer private)
- root key pair can be changed only through a firmware update (not necessarily
  via an update capsule)
- signature of a capsule is a feature of the capsule, but not of a firmware
  image that it carries

The last two points are relevant when one wants to transition from one root key
pair to another.  This is possible to do via a capsule update as long as
there is an ability to sign a capsule with the root key embedded into current
firmware (the key itself or any key signed by it (subkey) should do if the
signature includes all certificates necessary to validate it).  This works
because while current firmware validates the capsule, contents of the capsule
is free of any restrictions: it can have a different root key pair, it can even
be a completely different firmware.  In other words, capsule authentication
applies only to a single firmware update process.  That said, successive updates
typically will share the same root key such that the whole series of firmware
versions will be compatible with one another (unless `LowestSupportedVersion`
interferes).

[wiki-pkc]: https://en.wikipedia.org/wiki/Public-key_cryptography

## `capsule.sh` script

### Building a capsule

As a convenience, there is a `capsule.sh` script which can be used to ease
capsule creation by automating some of the steps.  Once a firmware has been
built, an update capsule for it can be created by running the following from
coreboot's root directory:

```bash
./capsule.sh make -t keys/TestRoot.pub.pem \
                  -o keys/TestSub.pub.pem \
                  -s keys/TestCert.pem
```

(The command assumes that signing keys from `BaseTools/Source/Python/Pkcs7Sign/`
in EDK have been copied to `keys/`.)

JSON file will be automatically generated based on the contents of coreboot's
`.config` file which contains all the necessary information when the capsule
support is enabled (and the script aborts if it's not the case).

Output file name is generated based on coreboot options like
`CONFIG_MAINBOARD_DIR` and `CONFIG_LOCALVERSION`, for example:

- `emulation-qemu-q35-v0.2.0.cap`
- `msi-ms7d25-ddr4-v1.1.9.cap`

### Generating test signing keys

In order to test capsules signed with unsupported keys, one needs to generate a
suitable set of keys which can be done like this:

```bash
./capsule.sh keygen my-test-keys
```

At the end the script prints a command to use the keys:

```bash
./capsule.sh make -t my-test-keys/root.pub.pem \
                  -o my-test-keys/sub.pub.pem \
                  -s my-test-keys/sign.p12
```

!!! warning

    The generated keys are for testing only, field values are hard-coded and no
    additional encryption is employed to achieve a convenient non-interactive
    key creation.

## Alternatives

It's also possible to generate capsules via EDK's build system by configuring it
in FDF file like its done in edk2-platforms [here][platformcapsule.fdf].  That's
the EDK2-way of doing things via `SignedCapsulePkg` ([PDF][edk2-capsules]) but
it appears to be less flexible due to relying on the build system of EDK2 which
is quite rigid for a large firmware variance that can be found in Dasharo.

Because `GenerateCapsule` is in Python and at least part of the functionality
is abstracted in form of modules, it's also possible to build custom tools on
top of that.

[platformcapsule.fdf]: https://github.com/tianocore/edk2-platforms/blob/a164cd7c5d330d0e6aadb7f73f5bb4c0855bf0f9/Platform/AMD/VanGoghBoard/ChachaniBoardPkg/PlatformCapsule.fdf
[edk2-capsules]: https://raw.githubusercontent.com/tianocore-docs/Docs/master/White_Papers/A_Tour_Beyond_BIOS_Capsule_Update_and_Recovery_in_EDK_II.pdf
