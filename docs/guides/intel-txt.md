# Intel Trusted Execution Technology

## Introduction

Intel Trusted Execution Technology (TXT) establishes a Dynamic Root of Trust
for Measurement (DRTM). Unlike the static chain of trust, which starts at
power-on and measures every component from the reset vector onwards, a DRTM can
be started at any point while the platform is already running. The `GETSEC
[SENTER]` instruction resets the dynamic PCRs, loads an Intel-signed SINIT
Authenticated Code Module (ACM), and hands control to a Measured Launched
Environment (MLE) only after the ACM has measured it and verified it against a
Launch Control Policy (LCP).

The practical consequence is that the trustworthiness of the launched
environment does not depend on the whole firmware boot path. Everything that
ran before `SENTER` is excluded from the dynamic measurements, which makes the
resulting attestation quote much shorter and much easier to reason about than
one covering the entire static chain.

Dasharo uses [coreboot's Intel TXT support][coreboot-txt], which prepares the
TXT environment in romstage and ramstage, places the BIOS and SINIT ACMs in
memory, fills the TXT heap, and locks down the TXT configuration registers
before handing control to the payload.

!!! note

    Intel TXT only establishes the dynamic root of trust. It does not replace
    the static chain of trust (Intel Boot Guard, vboot, measured boot into PCRs
    0-7), and it does not protect the firmware itself. See
    [PCR measurements performed by Dasharo firmware](../kb/pcr-measurements.md)
    for the static measurements.

[coreboot-txt]: https://doc.coreboot.org/security/intel/txt.html

## Supported platforms

| Platform                                  | Availability
| ----------------------------------------- | ------------
| ASRock Rack SPC741D8-2L2T/BCM             | Always enabled

On the platforms listed above Intel TXT is compiled into the firmware and
active on every boot. **There is no setup menu option to turn it off.** The
firmware enables SMX and LT/SX unconditionally, loads the ACMs, and reserves
the TXT memory regions whether or not an MLE is ever launched.

!!! note "Other Dasharo platforms"

    Dell OptiPlex 7010/9010 can be built with Intel TXT support, but it is a
    separate build-time variant that requires ACM blobs which cannot be
    redistributed. See the
    [OptiPlex building manual](../variants/dell_optiplex/building-manual.md#intel-txt)
    for that case. It is not covered by this guide.

## Requirements

### Hardware and firmware

- A platform from the [supported platforms](#supported-platforms) table running
  a Dasharo release with TXT support.
- A discrete TPM 2.0 installed in the TPM header and
  [provisioned for TXT](#tpm-provisioning). On the SPC741D8 this is the ASROCK
  TPM-SPI module.

The BIOS ACM and the SINIT ACM are Intel-signed, non-redistributable binaries.
On platforms where TXT is always enabled, both are already built into the
firmware images published on the Releases page.

### TPM provisioning

Intel TXT requires two TPM 2.0 NV indices to exist before a measured launch can
succeed. They are created once per platform (more specifically, once per TPM)
and survive reboots:

| Index       | Name | Purpose
| ----------- | ---- | -------
| `0x01c10103` | PS   | Platform Supplier policy, written by the platform manufacturer
| `0x01c10102` | AUX  | Auxiliary index used by the ACM to store TXT state

A TPM that has never been provisioned, has neither index defined. A measured
launch on such a platform fails in the SINIT ACM with an LCP or TPM error (see
[Reading the TXT error code](#reading-the-txt-error-code)).

Provisioning is done from the running OS with `txt-prov` from the
[Converged Security Suite][css]. Build it:

```bash
$ git clone https://github.com/9elements/converged-security-suite.git
$ cd converged-security-suite
$ go build -o txt-prov cmd/core/txt-prov/*.go
```

Then describe the Launch Control Policy to write into the PS index. Save the
following as `lcp.json`. It matches the policy Intel's own provisioning tools
write on a reference platform, so it is a good default to start from:

```json
{
    "Version": "300",
    "HashAlg": "SHA256",
    "PolicyType": "Any",
    "SINITMinVersion": "0",
    "MaxSINITMinVersion": "0",
    "PolicyControl": "SinitCaps",
    "LCPHashAlgMask": "SHA256,SHA384",
    "LCPSignAlgMask": "RSA2048SHA256,ECDSAP256SHA256,ECDSAP384SHA384"
}
```

Every field is a string. The format rules are easy to get wrong:

| Field                | Format
| -------------------- | ------
| `Version`            | Hex, no `0x` prefix. `300` to `306` are valid
| `HashAlg`            | Exactly one of `SHA1`, `SHA256`, `SHA384`
| `PolicyType`         | `Any` (auto-promotion) or `List` (signed policy)
| `SINITMinVersion`    | Hex, no `0x` prefix. Defaults to `0` when empty
| `MaxSINITMinVersion` | Hex, no `0x` prefix. Defaults to `ff` when empty
| `PolicyControl`      | Comma-separated: `NPW`, `SinitCaps`, `OwnerEnforced`, `AuxDelete`. May be empty
| `LCPHashAlgMask`     | Comma-separated: `SHA1`, `SHA256`, `SHA384`
| `LCPSignAlgMask`     | Comma-separated: `RSA2048SHA1`, `RSA2048SHA256`, `RSA3072SHA256`, `RSA3072SHA384`, `ECDSAP256SHA256`, `ECDSAP384SHA384`

`PolicyType: Any` creates a permissive policy that allows any MLE to be
launched. This is the right starting point for bringing TXT up; tightening the
policy so that only a known-good MLE may launch is a separate exercise and
requires the MLE hash, which changes with every tboot update.

Provision both indices:

```bash
$ sudo ./txt-prov platform-prov lcp.json
INFO[0000] Now, please type in the password (mandatory):
```

The command prompts for a password, which is mandatory and not echoed. Its
SHA-256 hash becomes the authorization policy protecting the PS index, so
writing or deleting that index later - with `ps-update` or `ps-delete` -
requires the same password. Record it somewhere safe; there is no recovery
path, and even a TPM clear does not remove the indices.

Verify the result:

```bash
$ sudo ./txt-prov show
```

```text
INFO[0000] NV index overview
INFO[0000]
INFO[0000] PS NV index
INFO[0000]    Index: 0x1c10103
   Attributes: No Do + AuthRead + PlatformCreate + PolicyDelete + Writte + PolicyWrite
   Size: 70
   AuthPolicy: 0xc001c8000210d0faa4f4f4f8a78ef4f8264e6f8555340d2f04180f8cf110ffdd
INFO[0000] AUX NV index
INFO[0000]    Index: 0x1c10102
   Attributes: PolicyWrite + No Do + AuthRead + PlatformCreate + PolicyDelete + WriteSTClear + Writte
   Size: 104
   AuthPolicy: 0xef9a26fc22d1ae8cecff59e9481ac1ec533dbe228bec6d17930f4cb2cc5b9724
INFO[0000] PS index LCP Policy
INFO[0000]    Version: 0x300
   HashAlg: SHA256
   PolicyType: Any
   SINITMinVersion: 0
   DataRevocationCounters:
   PolicyControl: SinitCaps +
   MaxSINITMinVersion: 0
   LcpHashAlgMask: SHA256 + SHA385
   LcpSignAlgMask: RSA2048SHA256 + ECDSAP256SHA256 + ECDSAP384SHA384
   PolicyHash: [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31]
INFO[0000]
```

The PS index `AuthPolicy` above is an example: it is derived from the password
entered during provisioning and will differ on your platform. The AUX index
`AuthPolicy` is a fixed Intel-defined value and should match exactly.

[css]: https://github.com/9elements/converged-security-suite

## Verifying that the firmware brought TXT up

From the running OS, `txt-stat` (shipped with tboot) reads the TXT
configuration registers directly:

```bash
$ sudo txt-stat | head -40
```

```text
Intel(r) TXT Configuration Registers:
	STS: 0x...
	    senter_done: FALSE
	    sexit_done: FALSE
	    mem_config_lock: TRUE
	    private_open: FALSE
	...
	ERRORCODE: 0x00000000
	...
***********************************************************
	 TXT measured launch: FALSE
	 secrets flag set: FALSE
***********************************************************
```

Before a measured launch, `TXT measured launch: FALSE` is expected. What
matters at this stage is that `txt-stat` runs at all (it prints
`Intel(r) TXT is not supported` when the chipset does not expose TXT) and that
`ERRORCODE` is `0x00000000`.

## Using Intel TXT with tboot

[tboot][tboot] is the reference MLE. It is launched by the bootloader, performs
the `SENTER`, verifies the kernel and initrd against a Verified Launch policy,
and then boots them.

### Obtaining tboot

Availability varies by distribution:

| Distribution                     | Availability
| -------------------------------- | ------------
| Fedora, RHEL                     | Packaged as `tboot`
| Debian bookworm, trixie          | Packaged as `tboot`
| Ubuntu up to 25.10               | Packaged as `tboot`
| Ubuntu 26.04 and newer           | **Removed**, build from source
| Debian testing (forky) and newer | **Removed**, build from source

Where the package exists, install it the usual way:

```bash
$ sudo apt install tboot          # Debian, Ubuntu up to 25.10
$ sudo dnf install tboot          # Fedora, RHEL
```

tboot was dropped from Ubuntu 26.04 ([LP #2142596][lp-removal]) after being
removed from Debian testing. The reason is not the measured launch itself but
the GRUB generator scripts the package ships, which
[break `update-grub`](#the-grub-generator-scripts-are-broken). Nothing about
Intel TXT or tboot itself is affected, so building from source is a perfectly
sound option on those releases.

!!! warning

    Do not install the `.deb` from an older Ubuntu release. It carries the
    same broken generator scripts, and installing it will break
    `update-grub` system-wide for every kernel entry, not just the tboot ones.
    Build from source instead.

[lp-removal]: https://bugs.launchpad.net/ubuntu/+source/tboot/+bug/2142596

### Building tboot from source

tboot is developed in a Mercurial repository at
[hg.code.sf.net/p/tboot/code][tboot-hg], and releases are published as tarballs
on [SourceForge][tboot-files]. Use a release tarball - it is what the
distributions package:

```bash
$ curl -LO https://sourceforge.net/projects/tboot/files/tboot/tboot-1.12.0.tar.gz
$ tar xf tboot-1.12.0.tar.gz
$ cd tboot-1.12.0
```

!!! warning "Avoid the GitHub mirrors"

    Several unofficial GitHub mirrors of tboot exist and rank well in search
    results. The most prominent one last received a commit in 2018, at around
    version 1.9.6. Its `tboot/Makefile` links the MLE twice, feeding the
    already-linked executable back into `ld`, which current binutils refuses:

    ```text
    ld.bfd: cannot use executable file 'tboot/.tboot.0' as input to a link
    ```

    Current releases link in a single pass and build cleanly. That error means
    you are building an ancient tree, not that your toolchain is at fault.

Install the build dependencies and build:

```bash
$ sudo apt install build-essential libssl-dev zlib1g-dev
$ make
$ sudo make install
```

The OpenSSL and zlib headers are the only external dependencies. The
safestringlib used by the LCP tools is bundled in the tree and built along with
it, and TrouSerS is _not_ required - the tools that needed it are part of the
deprecated v1 LCP tooling, which is no longer built.

`make install` places:

- `/boot/tboot.gz` and `/boot/tboot-syms` - the MLE itself and its symbols
- `/usr/sbin/txt-stat`, `/usr/sbin/txt-parse_err`, `/usr/sbin/txt-acminfo` -
  the diagnostic tools
- `/usr/sbin/tb_polgen` and `/usr/sbin/lcp2_*` - the policy tools
- `/usr/share/man/man8/*` - manual pages for all of the above
- `/etc/grub.d/20_linux_tboot` and `/etc/grub.d/20_linux_xen_tboot` - the GRUB
  generator scripts

Pass `DESTDIR=<dir>` to stage the installation into a directory and inspect it
before touching the running system.

[tboot-hg]: http://hg.code.sf.net/p/tboot/code
[tboot-files]: https://sourceforge.net/projects/tboot/files/tboot/

#### The GRUB generator scripts are broken

`20_linux_tboot` and `20_linux_xen_tboot` call `version_find_latest`, a helper
from `/usr/share/grub/grub-mkconfig_lib` that has been deprecated in favour of
`version_sort` and removed from upstream GRUB. On distributions that have
dropped it, Ubuntu 26.04 among them, running `update-grub` or `grub-mkconfig`
with those scripts in place fails:

```text
/etc/grub.d/20_linux_tboot: line 193: version_find_latest: command not found
```

`grub-mkconfig` runs with `set -e`, so a generator script that exits non-zero
aborts the whole run and leaves the configuration incomplete. This breaks
ordinary kernel entries too, not just the tboot ones, which is why the bug was
considered serious enough to drop the package.

!!! note

    Distributions still carrying the helper are unaffected for now. Fedora's
    GRUB 2.12, for instance, defines `version_find_latest` but emits a
    deprecation warning. Removing the scripts is harmless there too, and keeps
    the setup identical across distributions.

Remove the scripts after installing:

```bash
$ sudo rm -f /etc/grub.d/20_linux_tboot /etc/grub.d/20_linux_xen_tboot
```

The tboot boot entry is then written by hand, as described below. This is the
approach this guide documents, and it works the same way on distributions that
still package tboot.

### Configuring GRUB

Add a tboot entry to `/etc/grub.d/40_custom`, which `grub-mkconfig` copies
into the generated configuration verbatim. Append it below the
`exec tail -n +3 $0` line that the file already contains.

Paths inside a `menuentry` are relative to GRUB's root, which is the
filesystem holding `/boot`, not the root filesystem. **This is the detail that
most often makes a hand-written entry fail**, so determine the prefix first:

```bash
$ mountpoint -q /boot && echo "separate /boot: use /tboot.gz" \
                      || echo "/boot on rootfs: use /boot/tboot.gz"
```

The generated entries in `/boot/grub/grub.cfg` show the same thing: whatever
prefix their `linux` lines use for `vmlinuz`, the `multiboot2` line needs for
`tboot.gz`. The entry below assumes `/boot` is part of the root filesystem,
which is the default on Ubuntu:

```text
menuentry 'Linux with Intel TXT' {
    insmod multiboot2
    search --no-floppy --fs-uuid --set=root <UUID>
    multiboot2 /boot/tboot.gz logging=serial,memory extpol=sha256
    module2 /boot/vmlinuz-<version> root=UUID=<root-UUID> ro intel_iommu=on
    module2 /boot/initrd.img-<version>
}
```

Three parts must match your system. Copy the `search --no-floppy --fs-uuid
--set=root` line verbatim from an existing entry in `/boot/grub/grub.cfg` -
it points GRUB at the filesystem holding `/boot`, and without it GRUB searches
whatever happens to be the default root. Replace `<version>` with the
installed kernel version, and copy `root=` and the remaining kernel arguments
from the same generated entry. `insmod multiboot2` is required because the
module is not loaded by default.

Only `intel_iommu=on` is there for TXT's sake. The rest are the distribution's
own arguments, carried over unchanged - `20_linux_tboot` builds its command
line the same way `10_linux` does. `ro` is one of them: the kernel already
defaults to mounting the root filesystem read-only, so passing it explicitly is
convention rather than necessity, and the initramfs remounts the filesystem
read-write later in boot.

No SINIT module is listed: the firmware already loaded one, and tboot picks it
up from `TXT.SINIT.BASE`.

Because the entry is static, it must be updated by hand whenever the kernel is
upgraded - that is the trade-off for not using the generator scripts.

!!! note "`error: file '/tboot.gz' not found`"

    GRUB reports this when the path is right but the prefix is wrong, which
    looks confusing because the file plainly exists. `/tboot.gz` resolves
    correctly only when `/boot` is a separate partition. When `/boot` lives on
    the root filesystem, the same file is `/boot/tboot.gz` as far as GRUB is
    concerned. The GRUB command line (press ++c++ at the menu) is the quickest
    way to confirm: `ls /` and `ls /boot/` show which one GRUB can see.

Regenerate the configuration:

```bash
$ sudo update-grub                                         # Debian, Ubuntu
$ sudo grub2-mkconfig -o /boot/efi/EFI/<distro>/grub.cfg   # Fedora, RHEL
```

On UEFI systems tboot is loaded through the multiboot2 protocol, which requires
the `multiboot2` and `relocator` GRUB modules to be present in the EFI
directory. If the entry fails with a "no multiboot2 support" style error, copy
them into place:

```bash
$ sudo mkdir -p /boot/efi/EFI/<distro>/x86_64-efi
$ sudo cp /usr/lib/grub/x86_64-efi/{multiboot2,relocator}.mod \
      /boot/efi/EFI/<distro>/x86_64-efi/
```

The options that matter:

| Option                      | Applies to | Purpose
| --------------------------- | ---------- | -------
| `logging=serial,vga,memory` | tboot      | Where tboot traces the launch. `memory` is what `txt-stat` reads back.
| `extpol=`                   | tboot      | TPM 2.0 PCR extension policy, see below.
| `pcr_map=da\|legacy`        | tboot      | PCR mapping, see [PCR usage](#pcr-usage). Default is `legacy`.
| `ignore_prev_err=false`     | tboot      | Boot the kernel directly instead of retrying a measured launch that previously failed. Prevents reboot loops.
| `intel_iommu=on`            | kernel     | Enables VT-d. The kernel forces this on a TXT launch anyway.

`extpol` selects how the dynamic PCRs are extended on a TPM 2.0:

- `agile` - the ACM computes the hashes and extends every active PCR bank. Most
  complete, slowest.
- `embedded` - the ACM uses only the algorithms tboot supports; banks using
  other algorithms are capped with `1`. Fastest, but leaves some banks
  unusable.
- A single algorithm (`sha1`, `sha256`, `sm3`, ...) - only that bank is
  extended.

`extpol=sha256` is a reasonable default. Bear in mind that a capped or
unextended bank cannot be used for sealing.

!!! note

    If you do pass a SINIT ACM as the last module on the GRUB line, tboot
    compares its date with the firmware-provided one and uses whichever is
    newer. The firmware-provided module is used when the bootloader supplies
    none.

[tboot]: https://sourceforge.net/projects/tboot/

### Verifying a measured launch

After booting the tboot entry, check that the launch actually happened:

```bash
$ sudo txt-stat | grep -A2 "TXT measured launch"
```

```text
	 TXT measured launch: TRUE
	 secrets flag set: TRUE
```

`TXT measured launch: TRUE` means `SENTER` completed. `secrets flag set: TRUE`
means the platform has secrets in memory and the firmware will scrub memory on
the next boot, which is the expected state while an MLE is running.

The full tboot log is available through the same tool when
`logging=memory` was used:

```bash
$ sudo txt-stat | less
```

The dynamic PCRs are the second confirmation. Before a measured launch they
read all-ones; after a successful one they are reset to zero and extended:

```bash
$ sudo tpm2_pcrread sha256:17,18,19
```

## PCR usage

PCRs 17-22 are the DRTM PCRs. They cannot be extended or reset by ordinary
software: `SENTER` resets them to zero and the ACM and MLE extend them from
locality 2 and above. At platform reset they are initialized to all-ones, so a
PCR 17 full of `ff` bytes is a reliable indication that no measured launch has
taken place.

tboot supports two mappings. `legacy` is the default; `pcr_map=da` selects the
Details / Authorities mapping, which separates measurements of components from
measurements of the authorities that signed them, so that a signed component
can be updated without changing the authorities PCR.

### Legacy mapping (default)

| PCR    | Extended by | Contents
| ------ | ----------- | --------
| PCR 17 | SINIT ACM   | DRTM configuration as defined by the Intel MLE Developer's Guide: BIOS ACM identity, MSEG/STM status, LCP policy control field, LCP policy hash and S-CRTM status
| PCR 17 | tboot       | Hash of the tboot policy control value (4 bytes) concatenated with the hash of the tboot policy. The policy hash is zeroed when `TB_POLCTL_EXTEND_PCR17` is clear
| PCR 18 | SINIT ACM   | The MLE hash, that is the measurement of tboot itself. `lcp2_mlehash` computes the same value offline, which is what an LCP MLE element is built from
| PCR 18 | tboot       | Hash of the first module on the GRUB line, that is the kernel or Xen
| PCR 19 | tboot       | Hashes of all remaining modules, in order, under the default Verified Launch policy

### Details / Authorities mapping (`pcr_map=da`)

| PCR    | Role        | Contents
| ------ | ----------- | --------
| PCR 17 | Details     | The values defined by the MLE Developer's Guide, the tboot policy control and policy hash, and the hash of the first module
| PCR 18 | Authorities | The values defined by the MLE Developer's Guide and the tboot policy control and policy hash
| PCR 17 | Details     | Hashes of all remaining modules, in order, under the default policy

Under this mapping PCR 19 is unused by default: module measurements go to
PCR 17 instead.

A Verified Launch policy built with `tb_polgen` may direct individual module
measurements to other PCRs. The tables above describe the default policy.

### What the DRTM chain does not cover

On 4th and 5th Generation Intel Xeon Scalable processors, the SINIT ACM does
not implement SMI Transfer Monitor support. No PCR in the DRTM chain reflects
which STM is present, or whether one is present at all. See
[No Intel TXT integration on Sapphire Rapids and Emerald Rapids](smi-transfer-monitor.md#no-intel-txt-integration-on-sapphire-rapids-and-emerald-rapids)
for the full consequences.

## Reading the TXT error code

When a measured launch fails, the processor or the ACM latches a code in the
`TXT.ERRORCODE` register at offset `0x30` of the TXT public configuration
space, which is memory-mapped at `0xfed30000`. Errors reported by the BIOS ACM
go to `TXT.BIOSACM.ERRORCODE` at offset `0x328` instead.

!!! warning

    `TXT.ERRORCODE` is sticky. A warm reset does **not** clear it - only a
    power cycle does. A code read after a reboot may therefore describe a
    failure from an earlier boot. When diagnosing, power-cycle first so that
    you know which launch the code belongs to.

### Decoding tools

`txt-parse_err`, part of the tboot package, decodes either the live register or
a value given on the command line:

```bash
$ sudo txt-parse_err             # read TXT.ERRORCODE from /dev/mem
$ txt-parse_err 0xc0007051       # decode a value noted earlier
```

```text
ERRORCODE: 0xc0007051
AC module error : acm_type=0x1, progress=0x05, error=0x1c
```

coreboot decodes the same register into the firmware log, where it appears as:

```text
SINIT: Error code valid
 Caused by: External
 Error Class: 5
 Error: 1c.0
```

The two tools use different names for the same bits, which is a frequent source
of confusion:

| Bits  | Intel / coreboot name | `txt-parse_err` name
| ----- | --------------------- | --------------------
| 9:4   | Class code            | `progress`
| 14:10 | Major error code      | `error`
| 23:16 | Progress code         | decoded only for the two special cases below

### Worked example

Take `0xc0007051`:

- Bit 31 is set, so the code is valid.
- Bit 30 is set, so it was reported by software rather than the processor.
- Bits 3:0 are `0x1`, so the SINIT ACM reported it.
- Bit 15 is clear, confirming an ACM as the source rather than the MLE.
- Bits 9:4 are `0x05` - the class code.
- Bits 14:10 are `0x1c` - the major error code.
- Bits 23:16 are `0x00` - no progress code.

The class and major codes are specific to the ACM and are listed in the Intel
TXT Software Development Guide.

### Special cases

Two combinations carry a decodable sub-field:

- **Class `0x0d` with major error `0x0a`** - the ACM hit a TPM error, and bits
  24:16 hold the TPM return code. This is the signature to look for when the
  TPM is not [provisioned](#tpm-provisioning) or is unresponsive.
- **Class `0x10`** - an LCP version 2 error. Bits 21:16 hold the minor error
  code and bits 24:22 the index of the policy list element that failed. Expect
  this when the PS index holds a policy the current MLE does not satisfy.

### Successful execution with a code set

A valid, non-zero `TXT.ERRORCODE` does not always mean failure. When the class
code and the major error code are both zero and the progress code is non-zero,
the ACM completed successfully and merely recorded how far it got. coreboot
reports this case explicitly:

```text
SINIT: Error code valid
 Caused by: External
 Execution successful
 Progress code 0xf
```

## Further reading

- [coreboot Intel TXT documentation][coreboot-txt]
- [coreboot ACM documentation](https://doc.coreboot.org/security/intel/acm.html)
- [PCR measurements performed by Dasharo firmware](../kb/pcr-measurements.md)
- [Preparing Ubuntu for SMI Transfer Monitor](smi-transfer-monitor.md)
- [Converged Security Suite][css], the source of `txt-prov` and `txt-suite`
