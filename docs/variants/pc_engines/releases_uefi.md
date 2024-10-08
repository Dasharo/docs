# Release Notes

Following Release Notes describe status of Dasharo (coreboot+UEFI) variant of
open-source firmware development for PC Engines apu2/3/4/6 platform.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>
[Subscribe to Dasharo for PC Engines Release Notification Newsletter]
[newsletter]{.md-button .md-button--primary .center}
</center>

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit#gid=1670191276).

## v0.9.0 - 2024-04-02

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

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-entry-subscription-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Pro Package newsletter.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
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

[newsletter]: https://newsletter.3mdeb.com/subscription/ReBpt3IZY
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
