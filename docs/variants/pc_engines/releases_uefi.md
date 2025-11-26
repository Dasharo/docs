# Release Notes

This is a Dasharo Pro Package Release. o obtain access to the pre-built binaries,
you need to [subscribe to the Dasharo Pro Package subscriber](https://docs.dasharo.com/ways-you-can-help-us/#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our [shop](https://shop.3mdeb.com/shop/dasharo-pro-package/1year-desktop/).
As a subscriber, you will receive access to all firmware updates for the
duration of your subscription via the Dasharo Pro Package newsletter,
and gain entry to the Dasharo Premier Support invite-only live chat
on the Matrix network, enabling direct engagement with the Dasharo Team
and fellow subscribers for personalized, priority assistance.

Following Release Notes describe status of Dasharo (coreboot+UEFI) variant of
open-source firmware development for PC Engines apu2/3/4/6 platform.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("667a3af1-424e-439e-9144-57bfcf921ca4",
"Subscribe to Dasharo for PC Engines Release Notification Newsletter") }}

## v0.9.1 - 2025-11-26

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/tree/main/boards/PCEngines/).

### Changed

- [coreboot rebased on 24.12](https://doc.coreboot.org/releases/coreboot-24.12-relnotes.html)
- EDK II rebased on edk2-stable202408

### Known issues

- [Installer of OpenBSD 7.5 & 7.7 won't boot on Dasharo v0.9.0, PC Engines APU2](https://github.com/Dasharo/dasharo-issues/issues/1465)
- [APU2 - IO_PAGE_FAULTS on writes by ath10k_pci](https://github.com/Dasharo/dasharo-issues/issues/1134)
- [APU2 - "L1 TLB multimatch"](https://github.com/Dasharo/dasharo-issues/issues/994)
- [escape takes too long](https://github.com/Dasharo/dasharo-issues/issues/788)
- [Driver Health Manager blank screen](https://github.com/Dasharo/dasharo-issues/issues/787)
- [HDD Security Configuration blank screen](https://github.com/Dasharo/dasharo-issues/issues/786)
- [Dasharo v0.9.0, apu4, apu6 - Call Trace at boot time](https://github.com/Dasharo/dasharo-issues/issues/784)
- [TPMCMD007.002 CREATELOADED Function (Ubuntu 22.04) doesn't work](https://github.com/Dasharo/open-source-firmware-validation/issues/217)
- [Firmware boot time reported by systemd-analyze is too high](https://github.com/Dasharo/dasharo-issues/issues/761)
- [BIOS Lock does not work as expected](https://github.com/Dasharo/dasharo-issues/issues/754)
- [CBMEM buffer too small to fill full boot log](https://github.com/Dasharo/dasharo-issues/issues/753)

### Binaries

[sha256][pcengines_apu2_v0.9.1.rom_hash]{.md-button}
[sha256.sig][pcengines_apu2_v0.9.1.rom_sig]{.md-button}
(pcengines_apu2_v0.9.1.rom)

[sha256][pcengines_apu3_v0.9.1.rom_hash]{.md-button}
[sha256.sig][pcengines_apu3_v0.9.1.rom_sig]{.md-button}
(pcengines_apu3_v0.9.1.rom)

[sha256][pcengines_apu4_v0.9.1.rom_hash]{.md-button}
[sha256.sig][pcengines_apu4_v0.9.1.rom_sig]{.md-button}
(pcengines_apu4_v0.9.1.rom)

[sha256][pcengines_apu6_v0.9.1.rom_hash]{.md-button}
[sha256.sig][pcengines_apu6_v0.9.1.rom_sig]{.md-button}
(pcengines_apu6_v0.9.1.rom)

This is a Dasharo Pro Package Release. To access the pre-built binaries,
you need to [subscribe to the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our
[shop](https://shop.3mdeb.com/shop/dasharo-pro-package/1-year-dasharo-pro-package-for-network-appliance/).
As a subscriber, you will receive access to all firmware updates for the
duration of your subscription via the Dasharo Pro Package newsletter, and
gain entry to the Dasharo Premier Support invite-only live chat on the Matrix
network, enabling direct engagement with the Dasharo Team and fellow
subscribers for personalized, priority assistance.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/pcengines_apu2/dasharo-release-0.9.x-for-pc-engines-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 24.12 revision 217612e6](https://github.com/Dasharo/coreboot/tree/217612e6)
    + [License](https://github.com/Dasharo/coreboot/blob/217612e6/COPYING)
- [Dasharo EDKII fork based on edk2-stable202408 revision 42934b12](https://github.com/Dasharo/edk2/tree/42934b12)
    + [License](https://github.com/Dasharo/edk2/blob/42934b12/License.txt)
- [iPXE based on 6c7068fce4b revision 6c7068fc](https://github.com/Dasharo/ipxe/tree/6c7068fc)
    + [License](https://github.com/Dasharo/ipxe/blob/6c7068fc/COPYING.GPLv2)
- [vboot based on f1f70f46dc revision f1f70f46](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/LICENSE)
- [AMD AGESA Binary Platform Initialization version MullinsPI 1.0.0.A](https://github.com/coreboot/blobs/tree/14f8fcc1/pi/amd/00730F01/FT3b)
    + [License](https://github.com/coreboot/blobs/tree/14f8fcc1/pi/amd/00730F01/FT3b/license.txt)
- [AMD Platform Security Processor bootloader version D.1.1.4D](https://github.com/coreboot/blobs/tree/14f8fcc1/southbridge/amd/avalon/PSP/PspBootLoader.Bypass.sbin)
    + [License](https://github.com/coreboot/blobs/blob/14f8fcc1/southbridge/amd/avalon/PSP/license.txt)
- [AMD Platform Security Processor firmware public key version v1.0](https://github.com/coreboot/blobs/tree/14f8fcc1/southbridge/amd/avalon/PSP/AmdPubKey.bin)
    + [License](https://github.com/coreboot/blobs/blob/14f8fcc1/southbridge/amd/avalon/PSP/license.txt)
- [AMD System Management Unit firmware version 1433](https://github.com/coreboot/blobs/tree/14f8fcc1/southbridge/amd/avalon/PSP/SmuFirmware.sbin)
    + [License](https://github.com/coreboot/blobs/blob/14f8fcc1/southbridge/amd/avalon/PSP/license.txt)
- [AMD System Management Unit - Software Configuration Settings binary version 1433](https://github.com/coreboot/blobs/tree/14f8fcc1/southbridge/amd/avalon/PSP/SmuScs.bin)
    + [License](https://github.com/coreboot/blobs/blob/14f8fcc1/southbridge/amd/avalon/PSP/license.txt)
- [AMD Hudson xHCI firmware version 1.1.0.0068](https://github.com/coreboot/blobs/tree/14f8fcc1/southbridge/amd/avalon/xhci.bin)
    + [License](https://github.com/coreboot/blobs/blob/14f8fcc1/southbridge/amd/avalon/license.txt)

[pcengines_apu2_v0.9.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/uefi/v0.9.1/pcengines_apu2_v0.9.1.rom.sha256
[pcengines_apu2_v0.9.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/uefi/v0.9.1/pcengines_apu2_v0.9.1.rom.sha256.sig
[pcengines_apu3_v0.9.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/uefi/v0.9.1/pcengines_apu3_v0.9.1.rom.sha256
[pcengines_apu3_v0.9.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/uefi/v0.9.1/pcengines_apu3_v0.9.1.rom.sha256.sig
[pcengines_apu4_v0.9.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/uefi/v0.9.1/pcengines_apu4_v0.9.1.rom.sha256
[pcengines_apu4_v0.9.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/uefi/v0.9.1/pcengines_apu4_v0.9.1.rom.sha256.sig
[pcengines_apu6_v0.9.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/uefi/v0.9.1/pcengines_apu6_v0.9.1.rom.sha256
[pcengines_apu6_v0.9.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/uefi/v0.9.1/pcengines_apu6_v0.9.1.rom.sha256.sig

## v0.9.0 - 2024-04-02

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit#gid=1670191276).

### Added

- Initial release supporting UEFI
- Core Performance Boost option in UEFI Setup Menu
- Watchdog options in UEFI Setup Menu
- PCI Express Power Management option in UEFI Setup Menu
- TPM 2.0 Support
- TPM Measured Boot
- Vboot Verified Boot
- UEFI Secure Boot
- UEFI Setup Password
- UEFI Shell
- Configurable Boot Order
- iPXE Network Boot with Dasharo Tools Suite and Firmware Update Mode

### Known issues

- [TPMCMD007.002 CREATELOADED Function (Ubuntu 22.04) doesn't work](https://github.com/Dasharo/open-source-firmware-validation/issues/217)
- [Firmware boot time reported by systemd-analyze is too high](https://github.com/Dasharo/dasharo-issues/issues/761)
- [BIOS Lock does not work as expected](https://github.com/Dasharo/dasharo-issues/issues/754)
- [CBMEM buffer too small to fill full boot log](https://github.com/Dasharo/dasharo-issues/issues/753)

### Binaries

[sha256][pcengines_apu2_v0.9.0.rom_hash]{.md-button}
[sha256.sig][pcengines_apu2_v0.9.0.rom_sig]{.md-button}
(pcengines_apu2_v0.9.0.rom)

[sha256][pcengines_apu2_v0.9.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][pcengines_apu2_v0.9.0_dev_signed.rom_sig]{.md-button}
(pcengines_apu2_v0.9.0_dev_signed.rom)

[sha256][pcengines_apu3_v0.9.0.rom_hash]{.md-button}
[sha256.sig][pcengines_apu3_v0.9.0.rom_sig]{.md-button}
(pcengines_apu3_v0.9.0.rom)

[sha256][pcengines_apu3_v0.9.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][pcengines_apu3_v0.9.0_dev_signed.rom_sig]{.md-button}
(pcengines_apu3_v0.9.0_dev_signed.rom)

[sha256][pcengines_apu4_v0.9.0.rom_hash]{.md-button}
[sha256.sig][pcengines_apu4_v0.9.0.rom_sig]{.md-button}
(pcengines_apu4_v0.9.0.rom)

[sha256][pcengines_apu4_v0.9.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][pcengines_apu4_v0.9.0_dev_signed.rom_sig]{.md-button}
(pcengines_apu4_v0.9.0_dev_signed.rom)

[sha256][pcengines_apu6_v0.9.0.rom_hash]{.md-button}
[sha256.sig][pcengines_apu6_v0.9.0.rom_sig]{.md-button}
(pcengines_apu6_v0.9.0.rom)

[sha256][pcengines_apu6_v0.9.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][pcengines_apu6_v0.9.0_dev_signed.rom_sig]{.md-button}
(pcengines_apu6_v0.9.0_dev_signed.rom)

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/pcengines_apu2/dasharo-release-0.9.x-for-pc-engines-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 4.21 revision 4d12ba21](https://github.com/Dasharo/coreboot/tree/4d12ba21)
- [Dasharo EDKII fork based on edk2-stable202002 revision ae0ce3e2](https://github.com/Dasharo/edk2/tree/ae0ce3e2)
- [iPXE based on 2023.12 revision 838611b3](https://github.com/Dasharo/ipxe/tree/838611b3)
- [vboot based on 0c11187c75 revision 0c11187c](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/0c11187c/)
- [AMD AGESA Binary Platform Initialization based on MullinsPI 1.0.0.A revision a8db7dfe](https://github.com/coreboot/blobs/tree/a8db7dfe/pi/amd/00730F01/FT3b)
- [AMD Platform Security Processor bootloader based on D.1.1.4D revision a8db7dfe](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/PSP/PspBootLoader.Bypass.sbin)
- [AMD Platform Security Processor firmware public key based on v1.0 revision a8db7dfe](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/PSP/AmdPubKey.bin)
- [AMD System Management Unit firmware based on 1433 revision a8db7dfe](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/PSP/SmuFirmware.sbin)
- [AMD System Management Unit - Software Configuration Settings binary based on 1433 revision a8db7dfe](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/PSP/SmuScs.bin)
- [AMD Hudson xHCI firmware based on 1.1.0.0068 revision a8db7dfe](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/xhci.bin)

[pcengines_apu2_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu2_v0.9.0.rom.sha256
[pcengines_apu2_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu2_v0.9.0.rom.sha256.sig
[pcengines_apu2_v0.9.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu2_v0.9.0_dev_signed.rom.sha256
[pcengines_apu2_v0.9.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu2_v0.9.0_dev_signed.rom.sha256.sig
[pcengines_apu3_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu3_v0.9.0.rom.sha256
[pcengines_apu3_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu3_v0.9.0.rom.sha256.sig
[pcengines_apu3_v0.9.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu3_v0.9.0_dev_signed.rom.sha256
[pcengines_apu3_v0.9.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu3_v0.9.0_dev_signed.rom.sha256.sig
[pcengines_apu4_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu4_v0.9.0.rom.sha256
[pcengines_apu4_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu4_v0.9.0.rom.sha256.sig
[pcengines_apu4_v0.9.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu4_v0.9.0_dev_signed.rom.sha256
[pcengines_apu4_v0.9.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu4_v0.9.0_dev_signed.rom.sha256.sig
[pcengines_apu6_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu6_v0.9.0.rom.sha256
[pcengines_apu6_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu6_v0.9.0.rom.sha256.sig
[pcengines_apu6_v0.9.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu6_v0.9.0_dev_signed.rom.sha256
[pcengines_apu6_v0.9.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v0.9.0/pcengines_apu6_v0.9.0_dev_signed.rom.sha256.sig
