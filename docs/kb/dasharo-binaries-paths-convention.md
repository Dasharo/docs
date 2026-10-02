# Dasharo Binaries Paths Convention

Dasharo firmware binaries are available to download on [dl.3mdeb.com][dl.3mdeb.com]
and [dlui.dasharo.com][dlui.dasharo.com]. These sources are being managed
- manually
- using semi-manual automation
- fully automated CI

The objective of this document is to describe a standard convention of the
directory tree and binary names used in Dasharo sources. It will make it easier
to navigate them and find the releases one is interested in, and it lets tools
build the path to a binary from a few variables instead of a lookup table.

The convention describes binaries, not products. It is independent of the
[Dasharo Product Naming Convention](../dasharo-naming-convention.md): package
names, editions and release tiers can change without moving a single file.

## Rules

1. Every field in a path or a file name describes a property that changes the
   binary contents: hardware vendor, device model, firmware framework and
   payload, version and build variant.
1. Properties that do not change the binary contents are not encoded. This
   covers the edition (Community, Pro, Enterprise), the release tier (Rapid,
   Assured, LTS) and the customer who ordered the build. Those are visible on
   the release page and in the storage a binary is published to.
1. One device model has exactly one directory, even when several models share
   an identical binary. The binary is then copied into every model directory
   it supports. Storage usage is not a concern of this convention.
1. All names are lower-case. Fields inside one path element are joined with
   `_`, path elements with `/`.

## Directories Convention

The standardised path to a release directory is as follows:

`/<vendor>/<model>/<framework>[_payload]/<version>/`

where:

- `<vendor>` - the brand the device is sold under, as used in the
  [supported hardware list](../variants/overview.md), like `novacustom`,
  `protectli`, `hardkernel`, `pcengines`, `msi`. A device built by an ODM for a
  brand uses the brand, so Clevo laptops sold by NovaCustom are `novacustom`.
  `3mdeb` appears here only for hardware designed by 3mdeb.
- `<model>` - the exact device model as the customer knows it, like `v540tu`,
  `vp6670`, `odroid-h4`, `apu4`, `v1211`. Names used in firmware source code,
  like `vault_jsl` or `v54x_mtl`, never appear here.
- `<framework>` - firmware framework, like `coreboot`, `slimbootloader`, `uefi`
- `[_payload]` - optional, firmware payload, like `_uefi`, `_heads`, `_seabios`,
  `_linuxboot`. A framework which boots the OS on its own, like EDK II used as
  a complete firmware, has no payload.
- `<version>` - Dasharo version, the same as in the release tag, like
  `v0.9.0`, `v1.7.2-rc1`, compliant with the
  [versioning scheme](../dev-proc/versioning.md).

Examples:

- Dasharo (coreboot+Heads) Community Package for Novacustom V540TNx 14th
  Gen laptops v1.0.0
    + (historically kept in one path due to compatibility):
    + `/novacustom/v540tnd/coreboot_heads/1.0.0/`
    + `/novacustom/v540tne/coreboot_heads/1.0.0/`
- Dasharo (coreboot+UEFI) Pro Package for Protectli V1000-series v0.9.3
    + (historically kept in two directories, a common `protectli_vault_jsl`
      path,
    and in more specific variants like `protectli_vault_jsl_v1210` due to
    temporal compatibility):
    + `/protectli/v1210/coreboot_uefi/v0.9.3/`
    + `/protectli/v1211/coreboot_uefi/v0.9.3/`
    + `/protectli/v1410/coreboot_uefi/v0.9.3/`
    + `/protectli/v1610/coreboot_uefi/v0.9.3/`
- Dasharo (coreboot+SeaBIOS) Community Package for PC Engines APU4 v24.08.00.01
    + (unique versioning scheme)
    + `/pcengines/apu4/coreboot_seabios/v24.08.00.01/`
- Dasharo (UEFI) Package, EDK II without a coreboot layer:
    + `/<vendor>/<model>/uefi/<version>/`

### Legacy directories

Releases published before this convention was adopted stay at their historical
locations, and so do the links pointing at them. Legacy directories are not
migrated and no legacy release is copied into the new tree.

### Motivation

#### <framework>[_payload]

Historically, the firmware framework and payload were generally not present in
the paths, which looked like `/<platform_family>/<version>/`.
When the support for new frameworks and payloads appeared, new directories
started to appear, like `/<platform_family>/heads/<version>/` or
`/<platform_family>/slimbootloader/<version>/` which made the paths
inconsistent with the older releases.

To fix this inconsistency issue the framework and (optional) payload will
always be there, even if a platform has only support for a single
framework/payload combination to reduce the ambiguity. The two fields form one
path element, so every binary sits at the same depth whether or not it has a
payload.

#### <vendor>/<model>

The idea to separate the `<platform_family>` into the vendor and specific models
has a couple reasons behind it:

1. the number of combinations of vendor, microarchitecture and model family
   resulted in too many directories on a single level
1. knowing just a model name it could be not that obvious which family
   it is supposed to belong to
1. the firmware binaries for all the models from a family could be, or not be
   compatible with the whole family, it could also change with releases and
   require changing the directory structure
1. it was not clear how to release the firmware for just one device from a
   family

By separating the `vendor` and `model` into independent fields all the issues
above are solved. An additional bonus is that the user searching for the
binaries doesn't need to know technical details like the microarchitecture
of their CPU, just the name of the producer and the model of the device.

[dl.3mdeb.com]: https://dl.3mdeb.com
[dlui.dasharo.com]: https://dlui.dasharo.com

## Binary Names Convention

To reduce the confusion and risk of mixing up binaries and allow for creating
multiple variants of a single binary without inconsistencies, the name of the
binary is also being standardised, and looks like:

`<vendor>_<model>_<framework>[_<payload>]_<version>[_extra].<extension>`

where:

- `<vendor>`, `<model>`, `<framework>`, `[_payload]`, `<version>` - the same
  values as in the directory path
- `[_extra]` - optional build variant, like `_dev_signed`, `_btg_provisioned`,
  `_btg_prod`, `_eom`
- `<extension>` - `rom` for normal binaries, `cap` for UEFI Capsules, `cab` for
  FWUPD cabinets etc.

Examples, all in `/novacustom/v540tu/coreboot_uefi/v1.0.1/`:

- `novacustom_v540tu_coreboot_uefi_v1.0.1.rom`
- `novacustom_v540tu_coreboot_uefi_v1.0.1_btg_prod.rom`
- `novacustom_v540tu_coreboot_uefi_v1.0.1_btg_prod.cap`
- `novacustom_v540tu_coreboot_uefi_v1.0.1.cab`

### Companion files

Files released together with a binary sit in the same `<version>` directory:

- checksum `<binary>.sha256` and signature `<binary>.sha256.sig`
- SBOM `<binary>.sbom.json`
- EC firmware `<vendor>_<model>_ec_<version>[_extra].rom`, with its own
  checksum and signature

### Motivation

This is especially important for the 3mdeb employees or users which flash their
devices often. Every binary should contain all the information required to
distinguish it from any other binary to reduce the risk of bricking the device
or other mishaps during flashing.
