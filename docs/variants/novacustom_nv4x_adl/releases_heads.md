# NovaCustom NV4x 12th Gen Dasharo (coreboot + heads) Release Notes

This is a Dasharo Pro Package Release. To access the pre-built binaries,
you need to [subscribe to the Dasharo Pro Package subscriber](https://docs.dasharo.com/ways-you-can-help-us/#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our [shop](https://shop.3mdeb.com/shop/dasharo-pro-package/1-year-dasharo-entry-subscription-for-network-appliance/).

As a subscriber, you will receive access to all firmware updates for the
duration of your subscription via the Dasharo Pro Package newsletter,
and gain entry to the Dasharo Premier Support invite-only live chat on
the Matrix network, enabling direct engagement with the Dasharo Team and fellow
subscribers for personalized, priority assistance.

Following Release Notes describe status of development of Dasharo (coreboot +
Heads) firmware for NovaCustom NV4x 12th Gen.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("310eac18-d302-478f-a617-5f5d65e8e0ac",
"Subscribe to NovaCustom NV4x 12th Gen Dasharo Release Newsletter") }}

## v0.9.2 - 2025-06-03

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1yWZ--zFPIsQhXZByf7nJIrasQYuRSf1yCi60lY_RGsQ/edit#gid=2042954457).

### Added

- [Introduced Quiet Mode for reduced technical output in logs](https://github.com/linuxboot/heads/pull/1875)
- [Added TPM extend operations logging while maintaining quiet mode](https://github.com/linuxboot/heads/pull/1875)
- [Added support for GPG Admin/User PIN output grabbing for Nitrokey HOTP verification](https://github.com/Nitrokey/nitrokey-hotp-verification/issues/38)
- [Integrated EFF Diceware short wordlist v2 for easier passphrase generation](https://www.eff.org/dice)
- [Introduced automatic Secrets App reset logic for Nitrokey 3](https://github.com/Nitrokey/nitrokey-hotp-verification/pull/43)
- [Unified and enhanced passphrase generation logic in recovery shell](https://github.com/linuxboot/heads/pull/1875)
- Quiet Mode now logs all technical details to /tmp/debug.log instead of
  showing them in the console
- Improved TPM2 primary handle debugging and error handling
- Refactored the OEM Factory Reset process to clarify mode-based security implications
- Improved kexec boot configuration handling with enhanced security warnings
- [Transitioned from `ash` shell to `bash` for improved scripting consistency](https://github.com/linuxboot/heads/pull/1875)
- Suppressed unnecessary grep errors for missing `/etc/config.user`
- Resolved logging inconsistencies when performing TPM resets
- [Fixed Secure App PIN handling during Nitrokey 3 re-ownership](https://github.com/Nitrokey/nitrokey-hotp-verification/pull/43)
- Corrected Diceware dictionary parsing and selection method for unbiased
  passphrase generation
- Eliminated redundant USB Security dongle detection messages
- [Add missing TPM PIRQ route for NV41](https://github.com/Dasharo/coreboot/commit/6cd77aa95a7ab46771874b72c7dba6b3600d9b29)
- [Integrate downcoring and hyper-threading options in Alder Lake SoC](https://github.com/Dasharo/coreboot/commit/95f8459de5b432e69cceb3735d36bca9973e6321)

### Fixed

- [Power button doesn't work in Qubes](https://github.com/Dasharo/dasharo-issues/issues/710)
- [Reproducibility problems with libcrypto and libtss2](https://github.com/linuxboot/heads/issues/1616)

### Known issues

- [Hotkeys (e.g KEY_PLAYPAUSE) are not implemented in Qubes OS](https://github.com/QubesOS/qubes-issues/issues/9698)
- [Existing Qubes installation is not found as bootable after transition back to EDK2](https://github.com/Dasharo/dasharo-issues/issues/713)

### Binaries

[sha256][novacustom_nv4x_adl_v0.9.2_heads.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_v0.9.2_heads.rom_sig]{.md-button}

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Pro Package newsletter.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://github.com/3mdeb/3mdeb-secpack/blob/master/customer-keys/novacustom/dasharo-release-0.9.x-for-novacustom-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo heads fork based on v0.2.1 revision da9b8ed9](https://github.com/Dasharo/heads/tree/da9b8ed9)
    + [License](https://github.com/Dasharo/heads/blob/da9b8ed9/COPYING)
- [Intel Management Engine version v16.1.30.2307](https://github.com/Dasharo/dasharo-blobs/blob/32cffee4/novacustom/nv4x_adl/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/32cffee4/novacustom/nv4x_adl/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version ADL-P C.1.75.10](https://github.com/intel/FSP/tree/3819544e/AlderLakeFspBinPkg/Client/AlderLakeP)
    + [License](https://github.com/intel/FSP/blob/3819544e/FSP_License.pdf)
- [Intel microcode version ADL L0/R0 0x00000433](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240514/intel-ucode/06-9a-04)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240514/license)
- [Intel microcode version RPL J0/Q0 0x00004121](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240312/intel-ucode/06-ba-02)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240312/license)

[newsletter]: https://newsletter.3mdeb.com/subscription/RJrTXDhWR
[novacustom_nv4x_adl_v0.9.2_heads.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/heads/v0.9.2/novacustom_nv4x_adl_v0.9.2_heads.rom.sha256
[novacustom_nv4x_adl_v0.9.2_heads.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/heads/v0.9.2/novacustom_nv4x_adl_v0.9.2_heads.rom.sha256.sig

## v0.9.1 - 2024-06-27

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1yWZ--zFPIsQhXZByf7nJIrasQYuRSf1yCi60lY_RGsQ/edit#gid=2042954457).

### Fixed

- [NK3 not detected/discovered at OEM Factory Reset/Re-Ownership](https://github.com/Dasharo/dasharo-issues/issues/831)
- [NK3 v1.7.1 firmware update compatibility](https://www.nitrokey.com/blog/2024/heads-v25-and-nitrokey-3-firmware-v171-security-update)
- [Heads shuts down instead of rebooting](https://github.com/Dasharo/dasharo-issues/issues/711)
- [Laptop boots when plugging in the power adapter](https://github.com/Dasharo/dasharo-issues/issues/766)

### Known issues

- [Power button does not work in Qubes](https://github.com/Dasharo/dasharo-issues/issues/710)
- [Existing Qubes installation is not found as bootable after transition back to EDK2](https://github.com/Dasharo/dasharo-issues/issues/713)
- [Builds are not fully reproducible](https://github.com/linuxboot/heads/issues/1616)

### Binaries

[sha256][novacustom_nv4x_adl_v0.9.1_heads.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_v0.9.1_heads.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://github.com/3mdeb/3mdeb-secpack/blob/master/customer-keys/novacustom/dasharo-release-0.9.x-for-novacustom-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo heads fork based on v0.2.0 revision 0fb3886f](https://github.com/Dasharo/heads/tree/0fb3886f)
- [Dasharo coreboot fork based on 4.21 revision 3a9aa3a4](https://github.com/Dasharo/coreboot/tree/3a9aa3a4)
- [Intel Management Engine based on v16.1.30.2307 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/novacustom/nv4x_adl/me.bin)
- [Intel Flash Descriptor based on v1.0 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/novacustom/nv4x_adl/descriptor.bin)
- [Intel Firmware Support Package based on ADL-P C.1.75.10 revision 481ea7cf](https://github.com/intel/FSP/tree/481ea7cf/AlderLakeFspBinPkg/Client/AlderLakeP)
- [Intel microcode based on ADL L0/R0 0x0000042c revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-9a-04)
- [Intel microcode based on RPL J0/Q0 0x00004119 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-ba-02)

## v0.9.0 - 2024-02-29

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1yWZ--zFPIsQhXZByf7nJIrasQYuRSf1yCi60lY_RGsQ/edit#gid=2042954457).

### Added

- Support for NovaCustom NV4x 12th Gen
- [Open-source Embedded Controller Firmware](https://docs.dasharo.com/unified/novacustom/recovery/#ec-firmware-recovery)
- [The external headset connected to the jack slot works properly](https://github.com/Dasharo/dasharo-issues/issues/254)
- [ISO keyboard works with non-US layouts NV4xMx](https://github.com/Dasharo/dasharo-issues/issues/259)
- [Sleep working consistently](https://github.com/Dasharo/dasharo-issues/issues/261)
- [Functional touchpad ON/OFF switch Fn key](https://github.com/Dasharo/dasharo-issues/issues/38)
- [This is a Dasharo Pro Package release](https://docs.dasharo.com/dev-proc/versioning/#dasharo-pro-package-releases)
- Heads Linux is used as a payload

### Known issues

- [Power button does not work in Qubes](https://github.com/Dasharo/dasharo-issues/issues/710)
- [Heads shuts down instead of rebooting](https://github.com/Dasharo/dasharo-issues/issues/711)
- [Existing Qubes installation is not found as bootable after transition back to EDK2](https://github.com/Dasharo/dasharo-issues/issues/713)
- [Builds are not fully reproducible](https://github.com/linuxboot/heads/issues/1616)

### Binaries

[sha256][novacustom_nv4x_adl_v0.9.0_heads.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_v0.9.0_heads.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://github.com/3mdeb/3mdeb-secpack/blob/master/customer-keys/novacustom/dasharo-release-0.9.x-for-novacustom-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo heads fork based on v0.2.0 revision ccf49703](https://github.com/Dasharo/heads/tree/ccf49703)
- [Dasharo coreboot fork based on 4.21 revision 3a9aa3a4](https://github.com/Dasharo/coreboot/tree/3a9aa3a4)
- [Intel Management Engine based on v16.1.30.2307 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/novacustom/nv4x_adl/me.bin)
- [Intel Flash Descriptor based on v1.0 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/novacustom/nv4x_adl/descriptor.bin)
- [Intel Firmware Support Package based on ADL-P C.1.75.10 revision 481ea7cf](https://github.com/intel/FSP/tree/481ea7cf/AlderLakeFspBinPkg/Client/AlderLakeP)
- [Intel microcode based on ADL L0/R0 0x0000042c revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-9a-04)
- [Intel microcode based on RPL J0/Q0 0x00004119 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-ba-02)

[novacustom_nv4x_adl_v0.9.1_heads.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/heads/v0.9.1/novacustom_nv4x_adl_v0.9.1_heads.rom.sha256
[novacustom_nv4x_adl_v0.9.1_heads.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/heads/v0.9.1/novacustom_nv4x_adl_v0.9.1_heads.rom.sha256.sig
[novacustom_nv4x_adl_v0.9.0_heads.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/heads/v0.9.0/novacustom_nv4x_adl_v0.9.0_heads.rom.sha256
[novacustom_nv4x_adl_v0.9.0_heads.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/heads/v0.9.0/novacustom_nv4x_adl_v0.9.0_heads.rom.sha256.sig
