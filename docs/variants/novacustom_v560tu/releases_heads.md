# NovaCustom V560TU 14th Gen Dasharo (coreboot + heads) Release Notes

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our [shop](https://shop.3mdeb.com/product/dasharo-corebootuefi-pro-package-upgrade-to-corebootheads-for-laptop-users/).
As a subscriber, you will receive access to all firmware updates for the
duration of your subscription via the Dasharo Pro Package newsletter,
and gain entry to the Dasharo Premier Support invite-only live chat
on the Matrix network, enabling direct engagement with the Dasharo Team
and fellow subscribers for personalized, priority assistance.

This document contains the release notes for Heads firmware for NovaCustom
V560TU series of laptops.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("c82fe8ab-8332-460e-8251-401f0d7b89ee",
"Subscribe to NovaCustom V54x 14th Gen Dasharo Release Newsletter") }}

## v0.9.1 - 2026-05-11

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/tree/main/boards/NovaCustom/MTL_14th_Gen/V560TU/Heads/).

### Added

- [Added Dasharo EC module to Heads, enabling embedded controller firmware management from within the firmware](https://github.com/linuxboot/heads/pull/2062)
- [Added EC firmware version display in System Information menu and recovery shell](https://github.com/linuxboot/heads/pull/2063)
- [Added integrity gate for TPM reseal and factory reset paths; confirms /boot integrity before allowing secret-sealing or re-ownership](https://github.com/linuxboot/heads/pull/2068)
- [Added disk and TPM swap detection with guided user recovery flow](https://github.com/linuxboot/heads/pull/2068)
- [Added TOTP display before prompting for TPM Disk Unlock Key passphrase](https://github.com/linuxboot/heads/pull/2024)

### Changed

- Updated Intel microcode to microcode-20251111
- [Improved Nitrokey 3 (NK3) device-specific branding and PIN labels throughout the user interface](https://github.com/linuxboot/heads/pull/2088)
- [Improved CPU performance by lowering the Energy Performance Preference (EPP) value from 0xb3 to 0x73](https://github.com/Dasharo/dasharo-issues/issues/1711)

### Fixed

- [Some commands in dasharo_ectool failed due to outdated EC protocol](https://github.com/Dasharo/dasharo-issues/issues/648)
- [External audio devices not working on NovaCustom MTL-H](https://github.com/Dasharo/dasharo-issues/issues/1583)
- [When battery is low, USB-PD is constantly charging then discharging](https://github.com/Dasharo/dasharo-issues/issues/1660)
- [USB-PD charger overdraw](https://github.com/Dasharo/dasharo-issues/issues/1599)
- [TOTP display loop did not flush keyboard input before waiting for ESC key, causing stale input to skip the prompt](https://github.com/linuxboot/heads/pull/2059)
- [HOTP counter incorrectly reset to 0 during OEM factory reset and device re-ownership](https://github.com/linuxboot/heads/pull/2054)
- [Disk size incorrectly reported for drives larger than 2 TB](https://github.com/linuxboot/heads/pull/2035)
- [Archlinux and Tails distro signing keys contained expired subkeys, causing ISO verification failures in the field](https://github.com/linuxboot/heads/pull/2078)
- [Lesser performance in comparison with NVIDIA variants](https://github.com/Dasharo/dasharo-issues/issues/1216)

### Known issues

- [Some unexpected errors in dmesg](https://github.com/Dasharo/dasharo-issues/issues/1201)
- [Confusing UX when updating Heads firmware](https://github.com/Dasharo/dasharo-issues/issues/896)
- [Existing Qubes installation is not found as bootable after transition back to EDK2](https://github.com/Dasharo/dasharo-issues/issues/713)
- [DA lockout prevents unsealing HOTP secret (CI system)](https://github.com/Dasharo/dasharo-issues/issues/1396)
- [Booting is slow in Heads](https://github.com/Dasharo/dasharo-issues/issues/1336)
- [Early DMA protection cannot be applied to NovaCustom MTL models](https://github.com/Dasharo/dasharo-issues/issues/985)

### Binaries

[sha256][novacustom_v56x_mtl_igpu_ec_v0.9.1.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_igpu_ec_v0.9.1.rom_sig]{.md-button}
[sha256][novacustom_v56x_mtl_igpu_v0.9.1_heads.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_igpu_v0.9.1_heads.rom_sig]{.md-button}

This is a Dasharo Pro Package Release. To access the pre-built binaries,
you need to [subscribe to the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our
[shop](https://shop.3mdeb.com/product/dasharo-corebootuefi-pro-package-upgrade-to-corebootheads-for-laptop-users/).
As a subscriber, you will receive access to all firmware updates for the
duration of your subscription via the Dasharo Pro Package newsletter, and
gain entry to the Dasharo Premier Support invite-only live chat on the Matrix
network, enabling direct engagement with the Dasharo Team and fellow
subscribers for personalized, priority assistance.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://github.com/3mdeb/3mdeb-secpack/blob/master/customer-keys/novacustom/dasharo-release-0.9.x-for-novacustom-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo heads fork based on v0.2.1 revision 927a84ee](https://github.com/Dasharo/heads/tree/927a84ee)
    + [License](https://github.com/Dasharo/heads/blob/927a84ee/COPYING)
- [Dasharo fork of System76 EC based on d198b64 revision d198b641](https://github.com/Dasharo/ec/tree/d198b641/)
    + [License](https://github.com/Dasharo/ec/blob/d198b641/LICENSE)
- [Dasharo coreboot fork based on 24.12 revision 6de027d1](https://github.com/Dasharo/coreboot/tree/6de027d1/)
    + [License](https://github.com/Dasharo/coreboot/blob/6de027d1/LICENSES)
- [Intel Management Engine version v18.0.10.2285](https://github.com/Dasharo/dasharo-blobs/blob/8dce7604/novacustom/v5x0tu/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package for Meteor Lake-H version 2024/04/30 v4122_12](https://github.com/Dasharo/dasharo-blobs/tree/8dce7604/novacustom/v5x0tu/MeteorLakeFspBinPkg)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/8dce7604/novacustom/v5x0tu/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel microcode version MTL C0 0x00000025 0x25 19/03/2025](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20251111/intel-ucode/06-aa-04)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20251111/license)

[novacustom_v56x_mtl_igpu_ec_v0.9.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl_igpu/heads/v0.9.1/novacustom_v56x_mtl_igpu_ec_v0.9.1.rom.sha256
[novacustom_v56x_mtl_igpu_ec_v0.9.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl_igpu/heads/v0.9.1/novacustom_v56x_mtl_igpu_ec_v0.9.1.rom.sha256.sig
[novacustom_v56x_mtl_igpu_v0.9.1_heads.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl_igpu/heads/v0.9.1/novacustom_v56x_mtl_igpu_v0.9.1_heads.rom.sha256
[novacustom_v56x_mtl_igpu_v0.9.1_heads.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl_igpu/heads/v0.9.1/novacustom_v56x_mtl_igpu_v0.9.1_heads.rom.sha256.sig

## v0.9.0 - 2025-01-30

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/tree/main/boards/NovaCustom/MTL_14th_Gen/V560TU/Heads/v0.9.0-results.csv).

### Added

- Support for Novacustom V56 (v560tu)
- [Configured correct clock for GbE on Clevo/MTL-H](https://github.com/Dasharo/coreboot/commit/8554fcaac3e1b9790298ef658ec8ba03c5f9b497)
- [Fixed touchpad IRQ pin assignment on Clevo/MTL-H](https://github.com/Dasharo/coreboot/commit/5a28a0b82c13e41e147d082ab47ce287fa11ffda)
- [Adjusted ACPI configuration to fix missing CNVi pinmux](https://github.com/Dasharo/coreboot/commit/41de74e14e802aec65ea4e8538577a27b4269882)
- [Meteor Lake graphics operations integrated into SoC](https://github.com/Dasharo/coreboot/commit/ea0d2ab2daea6f17506c3da87aae4783db7df53d)
- [Clevo/MTL-H PCIe root port flags added](https://github.com/Dasharo/coreboot/commit/6757a4679e2d4a1ebffbcf8d404fb85b5cf2154d)
- [Windows BSOD caused by missing ACPI device names](https://github.com/Dasharo/coreboot/commit/160fa32c8493e88f67e5167abdc08b2870d366f2)
- [RTC failure workaround for MRC fastboot](https://github.com/Dasharo/coreboot/commit/d7eb079076fc5213d525468425e4def12bf6c204)
- [SPD size correctly set for Clevo/MTL-H](https://github.com/Dasharo/coreboot/commit/041ef28b686417204cd3850731ea4a9ab1c8a7a7)
- [Corrected temperature control offsets in Meteor Lake](https://github.com/Dasharo/coreboot/commit/c835072d2fa67be113631efb53ad85a68c24889d)
- [Fixed duplicate temperature symbol in Kconfig](https://github.com/Dasharo/coreboot/commit/c835072d2fa67be113631efb53ad85a68c24889d)
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
- [Fixed Secure App PIN handling during Nitrokey 3
re-ownership](https://github.com/Nitrokey/nitrokey-hotp-verification/pull/43)
- Corrected Diceware dictionary parsing and selection method for unbiased
passphrase generation
- Eliminated redundant USB Security dongle detection messages

### Known issues

- [Some unexpected errors in dmesg](https://github.com/Dasharo/dasharo-issues/issues/1201)
- [Performance increase for -TU Series (comparison with NVIDIA variants) - coreboot issue](https://github.com/Dasharo/dasharo-issues/issues/1216)

### Binaries

[sha256][novacustom_v56x_mtl_ec_v0.9.0.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_ec_v0.9.0.rom_sig]{.md-button}

[sha256][novacustom_v56x_mtl_v0.9.0_heads.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_v0.9.0_heads.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://github.com/3mdeb/3mdeb-secpack/blob/master/customer-keys/novacustom/dasharo-release-0.9.x-for-novacustom-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo heads fork based on v0.2.1 revision bbbca5d4](https://github.com/Dasharo/heads/tree/bbbca5d4)
    + [License](https://github.com/Dasharo/heads/blob/bbbca5d4/COPYING)
- [Dasharo fork of System76 EC based on 485f3900 revision 368e08e0](https://github.com/Dasharo/ec/tree/368e08e0/)
    + [License](https://github.com/Dasharo/ec/blob/368e08e0/LICENSE)
- [vboot based on 3d37d2aa revision 3d37d2aa](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/LICENSE)
- [Intel Management Engine version v18.0.5.2040](https://github.com/Dasharo/dasharo-blobs/blob/32cffee4/novacustom/v5x0tu/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/32cffee4/novacustom/v5x0tu/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel microcode version MTL C0 0x1c 03/01/2024](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240531/intel-ucode/06-aa-04)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240531/license)
- [Intel Firmware Support Package for Meteor Lake-H version 2024/04/30 v4122_12](https://github.com/Dasharo/dasharo-blobs/tree/32cffee4/novacustom/v5x0tu/MeteorLakeFspBinPkg)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)

[novacustom_v56x_mtl_ec_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/heads/v0.9.0/novacustom_v56x_mtl_ec_v0.9.0.rom.sha256
[novacustom_v56x_mtl_ec_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/heads/v0.9.0/novacustom_v56x_mtl_ec_v0.9.0.rom.sha256.sig
[novacustom_v56x_mtl_v0.9.0_heads.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/heads/v0.9.0/novacustom_v56x_mtl_v0.9.0_heads.rom.sha256
[novacustom_v56x_mtl_v0.9.0_heads.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/heads/v0.9.0/novacustom_v56x_mtl_v0.9.0_heads.rom.sha256.sig
