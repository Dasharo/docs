# MSI PRO Z790-P (WIFI) (DDR4) Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
MSI PRO Z790-P (WIFI) (DDR4)

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

For detailed information on our validation setup, please refer to the
[Hardware Configuration Matrix](hardware-matrix.md). To gain a deeper
understanding of the nomenclature reasons behind the Z690/Z790 boards, we
recommend seeing our [FAQ](../../unified/msi/faq.md).

<center>

[Subscribe to MSI PRO Z790-P (WIFI) (DDR4) Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

</center>

## v0.9.1 - 2024-01-22

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/tree/main/boards/msi/ms7e06/results.csv).

### Added

- [Automatic fan control](https://github.com/Dasharo/dasharo-issues/issues/381)
- [RAM Disk support (EXPERIMENTAL)](https://github.com/Dasharo/dasharo-issues/issues/277)
- [Memory overclocking support with XMP profiles](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#memory-configuration)
- [Compatibility with Raptor Lake Refresh CPUs](https://github.com/Dasharo/dasharo-issues/issues/534)
- [Selective Option ROM loading](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#pcipcie-configuration)
- [Serial Console Redirection option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#serial-port-configuration)
- [Power state after power fail option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Option for Resizable BARs enabling](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#pcipcie-configuration)
- [ESP partition scanning in look for grubx64.efi or shimx64.efi or Windows bootmgr](https://github.com/Dasharo/dasharo-issues/issues/94)
- Memory speed is displayed in the firmware setup main page
- [Added support for taking screenshots in the firmware](https://docs.dasharo.com/dev-proc/screenshots/#taking-screenshots)
- Microsoft and Windows 2023 UEFI Secure Boot certificates
- Disabling ME and unlocking descriptor with HMRFPO command on FUM flow

### Changed

- [This is a Dasharo Pro Package release](https://docs.dasharo.com/dev-proc/versioning/#dasharo-entry-subscription-releases)
- [Updated microcode to the newer version; refer to SBOM section below](https://github.com/coreboot/intel-microcode/commit/6788bb07eb5f9e9b83c31ea1364150fe898f450a)
- [Updated ME to the newer version; refer to SBOM section below](https://github.com/Dasharo/dasharo-blobs/tree/main/msi/ms7e06)
- [Updated Flash Descriptor to unlock regions; refer to SBOM section below](https://github.com/Dasharo/dasharo-blobs/tree/main/msi/ms7e06)
- [Switched to the Raptor Lake-S Client FSP; refer to SBOM section below](https://github.com/intel/FSP/tree/481ea7cf0bae0107c3e14aa746e52657647142f3/RaptorLakeFspBinPkg/Client/RaptorLakeS)
- Get SMBIOS serial number and UUID from ROMHOLE region instead of CBFS
  (ROMHOLE is preserved during FlashBIOS and updates via DTS)
- Rebased coreboot on 4.21 tag
- Reduced the amount of microcode blobs included in the build, due to
  redundancy (some blobs had the same shasum and supported the same CPUIDs)
- Enroll default UEFI Secure Boot keys on the first boot
- [Improved UEFI Secure Boot menu user experience](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
- DDR4 variant SMBIOS product name to reflect MSI naming
- Scope of reset to default hotkey to global in firmware setup
- Booting DTS over iPXE via HTTPS
- Removed the i225/i226 EFI driver from the builds in favor of native iPXE
  driver
- Switched iPXE repository to Dasharo fork for the native iPXE driver for
  i225/i226

### Fixed

- [No audio playback via headset](https://github.com/Dasharo/dasharo-issues/issues/483)
- [Auto Boot Time-out is reset to 0 when F9 is pressed](https://github.com/Dasharo/dasharo-issues/issues/513)
- [Some RPL-S CPUs ( 0xB06F2 (RPL-S C0) or 0xB06F5 (RPL-S H0)) have a problem with booting on v0.9.0](https://github.com/Dasharo/dasharo-issues/issues/496)
- [Change boot order menu is confusing](https://github.com/Dasharo/dasharo-issues/issues/422)
- [The setup menu does not issue a reset, resulting in saved but unapplied settings](https://github.com/Dasharo/dasharo-issues/issues/398)
- [PCI Express Resizable BAR programming](https://github.com/Dasharo/dasharo-issues/issues/565)
- [PCI Express resource allocation for Intel ARC A750](https://github.com/Dasharo/dasharo-issues/issues/584)
- [CPU frequency not displayed on setup front page](https://github.com/Dasharo/dasharo-issues/issues/662)
- P2SB BAR not properly reserved in ACPI
- Power LED not blinking during S3 sleep
- PS/2 controller not enabled at first boot after flashing
- Incorrect C-states reported in ACPI unsupported by HW
- Incorrect first timestamp format in ACPI FPDT

### Known issues

- [XMP1 profile does not boot in combination with some DDR5 configurations](https://github.com/Dasharo/dasharo-issues/issues/683)
- [Windows 11 installer unable to detect i225 Ethernet NIC](https://github.com/Dasharo/dasharo-issues/issues/482)
- [Cannot wake from suspend via RTC on QubesOS](https://github.com/Dasharo/dasharo-issues/issues/484)
- [Windows 11 VBS (Virtualization-based Security) appears Not enabled on System Information](https://github.com/Dasharo/dasharo-issues/issues/539)
- [No ability to change active PCR banks with TPM PPI in FW](https://github.com/Dasharo/dasharo-issues/issues/521)

### Binaries

[sha256][msi_ms7e06_v0.9.1_ddr4.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.1_ddr4.rom_sig]{.md-button}
(msi_ms7e06_v0.9.1_ddr4)

[sha256][msi_ms7e06_v0.9.1_ddr4_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.1_ddr4_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.1_ddr4_dev_signed)

[sha256][msi_ms7e06_v0.9.1_ddr5.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.1_ddr5.rom_sig]{.md-button}
(msi_ms7e06_v0.9.1_ddr5)

[sha256][msi_ms7e06_v0.9.1_ddr5_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.1_ddr5_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.1_ddr5_dev_signed)

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-entry-subscription-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Pro Package newsletter.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7e06/dasharo-release-0.x-compatible-with-msi-ms-7e06-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 4.21 revision 2c5426c3](https://github.com/Dasharo/coreboot/tree/2c5426c3)
- [Dasharo EDKII fork based on edk2-stable202002 revision 11746340](https://github.com/Dasharo/edk2/tree/11746340)
- [iPXE based on 2023.12 revision 838611b3](https://github.com/Dasharo/ipxe/tree/838611b3)
- [vboot based on 0c11187c75 revision 0c11187c](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/0c11187c/)
- [Intel Management Engine based on v16.1.30.2307 revision 18aab76c](https://github.com/Dasharo/dasharo-blobs/blob/18aab76c/msi/ms7e06/me.bin)
- [Intel Flash Descriptor based on v1.1 revision 18aab76c](https://github.com/Dasharo/dasharo-blobs/blob/18aab76c/msi/ms7e06/descriptor.bin)
- [Intel Firmware Support Package based on RPL-S C.0.BD.40 revision 481ea7cf](https://github.com/intel/FSP/tree/481ea7cf/RaptorLakeFspBinPkg/Client/RaptorLakeS)
- [Intel microcode based on ADL/RPL C0/H0 0x0000002e revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-97-05)
- [Intel microcode based on RPL B0 0x00000119 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-b7-01)

## v0.9.0 - 2023-08-31

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/16wokQYhtS7XA1DQC3Om7FY-IImG6SZisGK7NnzyRGVY/edit?usp=sharing).

### Added

- [MSI FLASHBIOS recovery support](https://docs.dasharo.com/unified/msi/recovery/#using-msi-flashbios-button)
- [Raptor Lake-S CPU support](https://github.com/Dasharo/dasharo-issues/issues/130)
- MSI PRO Z790-P board support with the same feature set as PRO Z690-A
- [MSI ACPI device that triggers automatic driver and utility installation manager](https://www.youtube.com/watch?v=K-v-veV_jvI)
- [Support for logo customization](https://docs.dasharo.com/guides/logo-customization/)
- UEFI 2.8 errata C compliance in EDKII fork
- [Firmware Update Mode feature](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)

### Changed

- [This is a Dasharo Pro Package release](https://docs.dasharo.com/dev-proc/versioning/#dasharo-entry-subscription-releases)
- [Updated microcode to newer version, refer to SBOM](https://github.com/coreboot/intel-microcode/commit/390edfb411ba7de8559ad40597c7acb6c6a1ea96)
- [Updated ME to newer version, refer to SBOM](https://github.com/Dasharo/dasharo-blobs/tree/main/msi/ms7e06)

### Fixed

- [Nvidia RTX 3060 does not spawn HD Audio device in Device Manager](https://github.com/Dasharo/dasharo-issues/issues/364)
- [MSI FLASHBIOS feature is not working](https://github.com/Dasharo/dasharo-issues/issues/131)
- [Reset to defaults with F9 causes the wrong settings to be restored](https://github.com/Dasharo/dasharo-issues/issues/355)
- [Popup with information about recovery mode is displayed after flashing with a valid binary](https://github.com/Dasharo/dasharo-issues/issues/269)
- Too low watchdog timeout value causing reset loops on DDR5 boards with
  bigger amount of RAM
- [Chipset Watchdog timeout value does not change actual watchdog trigger time](https://github.com/Dasharo/dasharo-issues/issues/413)
- Missing ACPI objects errors in Linux dmesg
- Missing Setup Password option

### Binaries

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-entry-subscription-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Pro Package newsletter.

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 4.18 revision 197229de](https://github.com/Dasharo/coreboot/tree/197229de)
- [Dasharo EDKII fork based on edk2-stable202002 revision 94f562a7](https://github.com/Dasharo/edk2/tree/94f562a7)
- [iPXE based on 6ba671acd9 revision 6ba671ac](https://github.com/ipxe/ipxe/tree/6ba671ac)
- [vboot based on b76cd8c806 revision b76cd8c8](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/b76cd8c8/)
- [Intel Management Engine based on v16.1.30.2255 revision 2a8875ec](https://github.com/Dasharo/dasharo-blobs/blob/2a8875ec/msi/ms7e06/me.bin)
- [Intel Flash Descriptor based on v1.0 revision 2a8875ec](https://github.com/Dasharo/dasharo-blobs/blob/2a8875ec/msi/ms7e06/descriptor.bin)
- [Intel Firmware Support Package based on IoT RPL-S PV 3492_03 revision 2fea9a2f](https://github.com/intel/FSP/tree/2fea9a2f/RaptorLakeFspBinPkg/IoT/RaptorLakeS)
- [Intel microcode based on ADL C0 0x0000002c revision microcode-20230613](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230613/intel-ucode/06-97-02)
- [Intel microcode based on ADL H0 0x0000002c revision microcode-20230613](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230613/intel-ucode/06-97-05)
- [Intel microcode based on RPL B0 0x00000113 revision microcode-20230613](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230613/intel-ucode/06-b7-01)

[newsletter]: https://newsletter.3mdeb.com/subscription/KgJ7V_mmJ
[msi_ms7e06_v0.9.1_ddr4.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr4.rom.sha256
[msi_ms7e06_v0.9.1_ddr4.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr4.rom.sha256.sig
[msi_ms7e06_v0.9.1_ddr4_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr4_dev_signed.rom.sha256
[msi_ms7e06_v0.9.1_ddr4_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr4_dev_signed.rom.sha256.sig
[msi_ms7e06_v0.9.1_ddr5.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr5.rom.sha256
[msi_ms7e06_v0.9.1_ddr5.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr5.rom.sha256.sig
[msi_ms7e06_v0.9.1_ddr5_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr5_dev_signed.rom.sha256
[msi_ms7e06_v0.9.1_ddr5_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr5_dev_signed.rom.sha256.sig
