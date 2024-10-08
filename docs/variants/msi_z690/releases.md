# MSI PRO Z690-A (WIFI) (DDR4) Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development for
MSI PRO Z690-A (WIFI) DDR4 and MSI PRO Z690-A (WIFI).

For detailed information on our validation setup, please refer to the
[Hardware Configuration Matrix](hardware-matrix.md). To gain a deeper
understanding of the nomenclature reasons behind the Z690/Z790 boards, we
recommend seeing our [FAQ](../../unified/msi/faq.md).

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>
[Subscribe to Dasharo compatible with MSI PRO Z690-A Newsletter]
[newsletter]{.md-button .md-button--primary .center}
</center>

## v1.1.3 - 2024-01-22

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/tree/main/boards/msi/ms7d25/results.csv).

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
- [Support for taking screenshots in the firmware](https://docs.dasharo.com/dev-proc/screenshots/#taking-screenshots)
- Microsoft and Windows 2023 UEFI Secure Boot certificates
- Disabling ME and unlocking descriptor with HMRFPO command on FUM flow

### Changed

- [This is a Dasharo Pro Package release](https://docs.dasharo.com/dev-proc/versioning/#dasharo-entry-subscription-releases)
- [Updated microcode to the newer version; refer to SBOM section below](https://github.com/coreboot/intel-microcode/commit/6788bb07eb5f9e9b83c31ea1364150fe898f450a)
- [Updated ME to the newer version; refer to SBOM section below](https://github.com/Dasharo/dasharo-blobs/tree/main/msi/ms7d25)
- [Switched to the Raptor Lake-S Client FSP; refer to SBOM section below](https://github.com/intel/FSP/tree/481ea7cf0bae0107c3e14aa746e52657647142f3/RaptorLakeFspBinPkg/Client/RaptorLakeS)
- Get SMBIOS serial number and UUID from ROMHOLE region instead of CBFS
  (ROMHOLE is preserved during FlashBIOS and updates via DTS)
- Rebased coreboot on 4.21 tag
- Reduced the amount of microcode blobs included in the build, due to
  redundancy (some blobs had the same shasum and supported the same CPUIDs)
- Enroll default UEFI Secure Boot keys on the first boot
- [Improved UEFI Secure Boot menu user experience](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
- Scope of reset to default hotkey to global in firmware setup
- Booting DTS over iPXE via HTTPS
- Removed the i225/i226 EFI driver from the builds in favor of native iPXE
  driver
- Switched iPXE repository to Dasharo fork for the native iPXE driver for
  i225/i226

### Fixed

- [No audio playback via headset](https://github.com/Dasharo/dasharo-issues/issues/483)
- [Auto Boot Time-out is reset to 0 when F9 is pressed](https://github.com/Dasharo/dasharo-issues/issues/513)
- [Some RPL-S CPUs ( 0xB06F2 (RPL-S C0) or 0xB06F5 (RPL-S H0)) have a problem with booting on v1.1.2](https://github.com/Dasharo/dasharo-issues/issues/496)
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

[sha256][msi_ms7d25_v1.1.3_ddr4.rom_hash]{.md-button}
[sha256.sig][msi_ms7d25_v1.1.3_ddr4.rom_sig]{.md-button}
(msi_ms7d25_v1.1.3_ddr4)

[sha256][msi_ms7d25_v1.1.3_ddr4_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7d25_v1.1.3_ddr4_dev_signed.rom_sig]{.md-button}
(msi_ms7d25_v1.1.3_ddr4_dev_signed)

[sha256][msi_ms7d25_v1.1.3_ddr5.rom_hash]{.md-button}
[sha256.sig][msi_ms7d25_v1.1.3_ddr5.rom_sig]{.md-button}
(msi_ms7d25_v1.1.3_ddr5)

[sha256][msi_ms7d25_v1.1.3_ddr5_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7d25_v1.1.3_ddr5_dev_signed.rom_sig]{.md-button}
(msi_ms7d25_v1.1.3_ddr5_dev_signed)

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-entry-subscription-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Pro Package newsletter.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-1.x-compatible-with-msi-ms-7d25-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 4.21 revision 2c5426c3](https://github.com/Dasharo/coreboot/tree/2c5426c3)
- [Dasharo EDKII fork based on edk2-stable202002 revision 11746340](https://github.com/Dasharo/edk2/tree/11746340)
- [iPXE based on 2023.12 revision 838611b3](https://github.com/Dasharo/ipxe/tree/838611b3)
- [vboot based on 0c11187c75 revision 0c11187c](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/0c11187c/)
- [Intel Management Engine based on v16.1.30.2307 revision 18aab76c](https://github.com/Dasharo/dasharo-blobs/blob/18aab76c/msi/ms7d25/me.bin)
- [Intel Flash Descriptor based on v1.0 revision 18aab76c](https://github.com/Dasharo/dasharo-blobs/blob/18aab76c/msi/ms7d25/descriptor.bin)
- [Intel Firmware Support Package based on RPL-S C.0.BD.40 revision 481ea7cf](https://github.com/intel/FSP/tree/481ea7cf/RaptorLakeFspBinPkg/Client/RaptorLakeS)
- [Intel microcode based on ADL/RPL C0/H0 0x0000002e revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-97-05)
- [Intel microcode based on RPL B0 0x00000119 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-b7-01)

## v1.1.2 - 2023-09-06

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/16wokQYhtS7XA1DQC3Om7FY-IImG6SZisGK7NnzyRGVY/edit?usp=sharing).

### Added

- [MSI FLASHBIOS recovery support](https://docs.dasharo.com/unified/msi/recovery/#using-msi-flashbios-button)
- [Raptor Lake-S CPU support](https://github.com/Dasharo/dasharo-issues/issues/130)
- [MSI ACPI device that triggers automatic driver and utility installation manager](https://www.youtube.com/watch?v=K-v-veV_jvI)
- [Support for logo customization](https://docs.dasharo.com/guides/logo-customization/)
- UEFI 2.8 errata C compliance in EDKII fork
- [Firmware Update Mode feature](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)

### Changed

- [This is a Dasharo Pro Package release](https://docs.dasharo.com/dev-proc/versioning/#dasharo-entry-subscription-releases)
- [Updated microcode to newer version, refer to SBOM](https://github.com/coreboot/intel-microcode/commit/390edfb411ba7de8559ad40597c7acb6c6a1ea96)
- [Updated ME to newer version, refer to SBOM](https://github.com/Dasharo/dasharo-blobs/tree/main/msi/ms7d25)

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

### Known issues

- [Windows 11 installer unable to detect i225 Ethernet NIC](https://github.com/Dasharo/dasharo-issues/issues/482)
- [No audio playback via headset](https://github.com/Dasharo/dasharo-issues/issues/483)
- [Cannot wake from suspend via RTC on QubesOS](https://github.com/Dasharo/dasharo-issues/issues/484)

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
- [Intel Management Engine based on v16.1.30.2255 revision 2a8875ec](https://github.com/Dasharo/dasharo-blobs/blob/2a8875ec/msi/ms7d25/me.bin)
- [Intel Flash Descriptor based on v1.0 revision 2a8875ec](https://github.com/Dasharo/dasharo-blobs/blob/2a8875ec/msi/ms7d25/descriptor.bin)
- [Intel Firmware Support Package based on ADL-S C.0.75.10 revision 2fea9a2f](https://github.com/intel/FSP/tree/2fea9a2f/AlderLakeFspBinPkg/Client/AlderLakeS)
- [Intel microcode based on ADL C0 0x0000002c revision microcode-20230613](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230613/intel-ucode/06-97-02)
- [Intel microcode based on ADL H0 0x0000002c revision microcode-20230613](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230613/intel-ucode/06-97-05)
- [Intel microcode based on RPL B0 0x00000113 revision microcode-20230613](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230613/intel-ucode/06-b7-01)

## v1.1.1 - 2023-02-23

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/16wokQYhtS7XA1DQC3Om7FY-IImG6SZisGK7NnzyRGVY/edit?usp=sharing).

To get more details about the changes one may read the
[Dasharo v1.1.1 release blog post](https://blog.3mdeb.com/2023/2023-03-02-msi_ms7d25_v1.1.1_release/)

### Added

- [Early boot DMA protection menu option](https://github.com/Dasharo/dasharo-issues/issues/275)
- ACPI PCI interrupt routing for CPU PCIe Root Ports
- OC Watchdog ACPI device as in MSI firmware

### Changed

- [Updated SMMSTORE driver to upstream version in UEFI Payload](https://github.com/Dasharo/dasharo-issues/issues/303)
- [Improved visual comfort in the boot manager](https://github.com/Dasharo/dasharo-issues/issues/286)

### Fixed

- [MSI PRO Z690-A WIFI DDR4 doesn't initialize IGP on certain Processors models](https://github.com/Dasharo/dasharo-issues/issues/274)
- [MSI PRO Z690-A WIFI DDR4 with two Video Cards (2x Radeon 5600XT) has issues related to MMIO resource allocation](https://github.com/Dasharo/dasharo-issues/issues/245)
- [Suspend doesn't work in Qubes OS with v1.1.0](https://github.com/Dasharo/dasharo-issues/issues/271)
- [Intel XTU on Windows reports "The platform does not support overclocking" on the MSI PRO Z690-A WIFI DDR4 with a K-series Processor](https://github.com/Dasharo/dasharo-issues/issues/159)
- [SATA ports malfunction or Hot-Plug function disabled](https://github.com/Dasharo/dasharo-issues/issues/315)
- Platform sometimes automatically powers on after power off
- GPIO controller ACPI device yellow bang in Windows device manager
- Resource conflicts with chipset internal P2SB PCI device being incorrectly
  defined and initialized in coreboot
- Reset button hanging the platform for up to 2 minutes due to watchdog bug

### Known issues

- [MSI FLASHBIOS feature is not working](https://github.com/Dasharo/dasharo-issues/issues/131)
- [Reset to defaults with F9 causes the wrong settings to be restored](https://github.com/Dasharo/dasharo-issues/issues/355)

### Binaries

[msi_ms7d25_v1.1.1_ddr4.rom][msi_ms7d25_v1.1.1_ddr4.rom_file]{.md-button}
[sha256][msi_ms7d25_v1.1.1_ddr4.rom_hash]{.md-button}
[sha256.sig][msi_ms7d25_v1.1.1_ddr4.rom_sig]{.md-button}

[msi_ms7d25_v1.1.1_ddr5.rom][msi_ms7d25_v1.1.1_ddr5.rom_file]{.md-button}
[sha256][msi_ms7d25_v1.1.1_ddr5.rom_hash]{.md-button}
[sha256.sig][msi_ms7d25_v1.1.1_ddr5.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-1.x-compatible-with-msi-ms-7d25-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 912a262b7bf revision aa4701cd](https://github.com/Dasharo/coreboot/tree/aa4701cd)
- [Dasharo EDKII fork based on dd7523b5b1 revision a913e338](https://github.com/Dasharo/edk2/tree/a913e338)

## v1.1.0 - 2022-11-22

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/16wokQYhtS7XA1DQC3Om7FY-IImG6SZisGK7NnzyRGVY/edit?usp=sharing).

### Added

- Vboot recovery popup informing that platform has booted in recovery mode
- TCG2 TPM Physical Presence Interface support
- [Support for DDR5 board variant](https://github.com/Dasharo/dasharo-issues/issues/226)
- PS/2 Controller enable/disable option
- [Chipset watchdog support during boot and watchdog configuration menu](https://www.github.com/dasharo/dasharo-issues/issues/221)
- [Early boot DMA protection](https://www.github.com/dasharo/dasharo-issues/issues/222)
- [Option to reset Secure Boot keys to defaults](https://www.github.com/dasharo/dasharo-issues/issues/119)
- [Intel ME disable support and menu options](https://www.github.com/dasharo/dasharo-issues/issues/111)
- [Dasharo setup password](https://www.github.com/dasharo/dasharo-issues/issues/120)
- [SED/OPAL disk password support](https://www.github.com/dasharo/dasharo-issues/issues/161)
- SATA disk password
- [Firmware performance reporting](https://github.com/Dasharo/dasharo-issues/issues/125)
- [USB stack and mass storage enable/disable option](https://github.com/Dasharo/dasharo-issues/issues/223)
- [Network Boot enable/disable option](https://github.com/Dasharo/dasharo-issues/issues/122)
- SMM BIOS Write Protection support and enable/disable option
- AcpiView command to UEFI Shell
- Platform will beep 12 times and blink HDD led on critical firmware errors,
  e.g. if memory training failed
- PCIe 5.0 firmware caching in flash which allows to disable ME without losing
  PCIe 5.0 port functionality
- cbmem logging from UEFI Payload is now supported and one can check complete
  firmware logs from OS using coreboot's cbmem utility
- Added Intel default settings for missing Alder Lake S CPUs

### Changed

- Added new ACPI Platform driver that installs coreboot exposed ACPI tables and
  all allows native EDK2 ACPI table protocol to install new tables, e.g.
  Firmware Performance Data Table, BGRT (Boot Logo) of VFCT (AMD GPU ACPI
  table)
- Secure Boot is now disabled by default with all keys erased
- iPXE is now built from source using coreboot-sdk and
  [included externally into UEFI Payload](https://github.com/Dasharo/dasharo-issues/issues/198)
- [Dasharo setup menu full screen mode support](https://github.com/Dasharo/dasharo-issues/issues/118)
- Disabled PCIe ASPM and Clock PM for better PCIe device compatibility
- Disabled GPIO programming by FSP, coreboot handles the GPIO completely. This
  additionally fixes a bug in FSP which did not enable SATA DEVSLP properly.
- Changed Super I/O pin for PECI mode to reflect vendor firmware setting
- Switched from IOT FSP to public ADL Client FSP
- Switched to include microcode from public Intel microcode repository
- Disabled PCIe hotplug
- Network boot disabled by default, now configurable via menu option

### Fixed

- Vboot recovery popup is displayed before logo, so that logo do not disappear
  after popup is displayed
- [Wrong Tau values from Turbo Boost](https://github.com/Dasharo/dasharo-issues/issues/256)
- PCI Express OptionROM loading causing certain dGPU cards to not work during
  POST
- PS/2 keyboard detection and inclusion to platform Console Input
  [causing long delays in Ventoy or lockups in USB enumeration](https://github.com/Dasharo/dasharo-issues/issues/160)
- Incorrect USB2 PHY tuning values for USB-C ports causing hard USB controller
  lockups during USB enumeration and resulting in firmware hangs as long as USB
  Type-C devices were plugged or devices being unable to detect and enumerate
  in OS
- [Broken PCI resource parsing above 4G](https://github.com/Dasharo/dasharo-issues/issues/128)
- Incorrect SMBIOS product name for non-WiFi variants
- [USB storage devices disappear after reboot/power failure](https://github.com/Dasharo/dasharo-issues/issues/70)

### Known issues

- [MSI FLASHBIOS feature is not working](https://github.com/Dasharo/dasharo-issues/issues/131)
- [MMIO resource allocation issues with two Video Cards](https://github.com/Dasharo/dasharo-issues/issues/245)
- [Slow video performance with Radeon 5600XT](https://github.com/Dasharo/dasharo-issues/issues/181)
- [Reset to defaults with F9 causes the wrong settings to be restored](https://github.com/Dasharo/dasharo-issues/issues/355)

### Binaries

[msi_ms7d25_v1.1.0_ddr4.rom][msi_ms7d25_v1.1.0_ddr4.rom_file]{.md-button}
[sha256][msi_ms7d25_v1.1.0_ddr4.rom_hash]{.md-button}
[sha256.sig][msi_ms7d25_v1.1.0_ddr4.rom_sig]{.md-button}

[msi_ms7d25_v1.1.0_ddr5.rom][msi_ms7d25_v1.1.0_ddr5.rom_file]{.md-button}
[sha256][msi_ms7d25_v1.1.0_ddr5.rom_hash]{.md-button}
[sha256.sig][msi_ms7d25_v1.1.0_ddr5.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-1.x-compatible-with-msi-ms-7d25-signing-key.asc)

Commands snippet:

```shell
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/3mdeb-dasharo-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-1.x-compatible-with-msi-ms-7d25-signing-key.asc
gpg --list-sigs "3mdeb Master Key" "3mdeb Dasharo Master Key" "Dasharo release 1.x compatible with MSI MS-7D25 signing key"
# DDR4
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.0/msi_ms7d25_v1.1.0_ddr4.rom
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.0/msi_ms7d25_v1.1.0_ddr4.rom.sha256
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.0/msi_ms7d25_v1.1.0_ddr4.rom.sha256.sig
sha256sum -c msi_ms7d25_v1.1.0_ddr4.rom.sha256
gpg --verify msi_ms7d25_v1.1.0_ddr4.rom.sha256.sig msi_ms7d25_v1.1.0_ddr4.rom.sha256
# DDR5
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.0/msi_ms7d25_v1.1.0_ddr5.rom
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.0/msi_ms7d25_v1.1.0_ddr5.rom.sha256
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.0/msi_ms7d25_v1.1.0_ddr5.rom.sha256.sig
sha256sum -c msi_ms7d25_v1.1.0_ddr5.rom.sha256
gpg --verify msi_ms7d25_v1.1.0_ddr5.rom.sha256.sig msi_ms7d25_v1.1.0_ddr5.rom.sha256
```

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 912a262b7bf revision b76a1467](https://github.com/Dasharo/coreboot/tree/b76a1467)
- [Dasharo EDKII fork based on dd7523b5b1 revision 5738f9e8](https://github.com/Dasharo/edk2/tree/5738f9e8)

## v1.0.0 - 2022-05-27

### Added

- Serial number and UUID in CBFS support
- TPM Physical Presence Interface support

### Changed

- [Updated i225 EFI driver to version 0.10.04 to reduce the POST time](https://github.com/Dasharo/dasharo-issues/issues/65)
- Vboot submodule revision to fix recovery mode loop

### Fixed

- [fTPM is not working](https://github.com/Dasharo/dasharo-issues/issues/76)

### Known issues

- [USB storage devices disappear after reboot/power failure](https://github.com/Dasharo/dasharo-issues/issues/70)

### Binaries

[MSI PRO Z690-A WIFI DDR4 v1.0.0][v1.0.0_rom]{.md-button}
[sha256][v1.0.0_hash]{.md-button}
[sha256.sig][v1.0.0_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-1.x-compatible-with-msi-ms-7d25-signing-key.asc)

Commands snippet:

```shell
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/3mdeb-dasharo-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-1.x-compatible-with-msi-ms-7d25-signing-key.asc
gpg --list-sigs "3mdeb Master Key" "3mdeb Dasharo Master Key" "Dasharo release 1.x compatible with MSI MS-7D25 signing key"
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.0.0/msi_ms7d25_v1.0.0.rom
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.0.0/msi_ms7d25_v1.0.0.rom.sha256
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.0.0/msi_ms7d25_v1.0.0.rom.sha256.sig
sha256sum -c msi_ms7d25_v1.0.0.rom.sha256
gpg --verify msi_ms7d25_v1.0.0.rom.sha256.sig msi_ms7d25_v1.0.0.rom.sha256
```

### SBOM (Software Bill of Materials)

- [coreboot based on a552cfc9 revision d22caaa0a](https://github.com/Dasharo/coreboot/tree/d22caaa0a)
- [edk2 based on 4d2846ba revision 0c94299b](https://github.com/Dasharo/edk2/tree/0c94299b)

## v0.4.0 - 2022-05-13

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/16wokQYhtS7XA1DQC3Om7FY-IImG6SZisGK7NnzyRGVY/edit?usp=sharing).

### Added

- [Verified boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)

### Fixed

- [Some PCIe ports are not working](https://github.com/Dasharo/dasharo-issues/issues/75)

### Known issues

- [USB storage devices disappear after reboot/power failure](https://github.com/Dasharo/dasharo-issues/issues/70)
- [fTPM is not working](https://github.com/Dasharo/dasharo-issues/issues/76)

### Binaries

[MSI PRO Z690-A WIFI DDR4 v0.4.0][v0.4.0_rom]{.md-button}
[sha256][v0.4.0_hash]{.md-button}
[sha256.sig][v0.4.0_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-0.x-compatible-with-msi-ms-7d25-signing-key.asc)

Commands snippet:

```shell
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/3mdeb-dasharo-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-0.x-compatible-with-msi-ms-7d25-signing-key.asc
gpg --list-sigs "3mdeb Master Key" "3mdeb Dasharo Master Key" "Dasharo release 0.x compatible with MSI MS-7D25 signing key"
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.4.0/msi_ms7d25_v0.4.0.rom
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.4.0/msi_ms7d25_v0.4.0.rom.sha256
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.4.0/msi_ms7d25_v0.4.0.rom.sha256.sig
sha256sum -c msi_ms7d25_v0.4.0.rom.sha256
gpg --verify msi_ms7d25_v0.4.0.rom.sha256.sig msi_ms7d25_v0.4.0.rom.sha256
```

### SBOM (Software Bill of Materials)

- [coreboot based on a552cfc9 revision 31c1da6b](https://github.com/Dasharo/coreboot/tree/31c1da6b)
- [edk2 based on 4d2846ba revision 5494c8e2](https://github.com/Dasharo/edk2/tree/5494c8e2)

## v0.3.0 - 2022-05-05

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/16wokQYhtS7XA1DQC3Om7FY-IImG6SZisGK7NnzyRGVY/edit?usp=sharing).

### Added

- Mainboard-specific SMBIOS data for slots and ports
- PCI Subsystem ID configuration
- CPU VR and PCH FIVR configuration
- [Memory HCL](https://docs.dasharo.com/unified/msi/hcl/)
- [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [TPM Support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/200-tpm-support/)
- [Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [Custom boot menu keys](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key/)

### Known issues

- [USB storage devices disappear after reboot/power failure](https://github.com/Dasharo/dasharo-issues/issues/70)
- [Some PCIe ports are not working](https://github.com/Dasharo/dasharo-issues/issues/75)
- [fTPM is not working](https://github.com/Dasharo/dasharo-issues/issues/76)

### Binaries

[MSI PRO Z690-A WIFI DDR4 v0.3.0][v0.3.0_rom]{.md-button}
[sha256][v0.3.0_hash]{.md-button}
[sha256.sig][v0.3.0_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-0.x-compatible-with-msi-ms-7d25-signing-key.asc)

Commands snippet:

```shell
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/3mdeb-dasharo-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-0.x-compatible-with-msi-ms-7d25-signing-key.asc
gpg --list-sigs "3mdeb Master Key" "3mdeb Dasharo Master Key" "Dasharo release 0.x compatible with MSI MS-7D25 signing key"
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.3.0/msi_ms7d25_v0.3.0.rom
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.3.0/msi_ms7d25_v0.3.0.rom.sha256
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.3.0/msi_ms7d25_v0.3.0.rom.sha256.sig
sha256sum -c msi_ms7d25_v0.3.0.rom.sha256
gpg --verify msi_ms7d25_v0.3.0.rom.sha256.sig msi_ms7d25_v0.3.0.rom.sha256
```

### SBOM (Software Bill of Materials)

- [coreboot based on a552cfc9 revision b45173e9](https://github.com/Dasharo/coreboot/tree/b45173e9)
- [edk2 based on 4d2846ba revision 5494c8e2](https://github.com/Dasharo/edk2/tree/5494c8e2)

## v0.2.0 - 2022-04-22

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/16wokQYhtS7XA1DQC3Om7FY-IImG6SZisGK7NnzyRGVY/edit?usp=sharing).

### Added

- Configurable boot order
- Configurable boot options
- [NVMe support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/312-nvme-support/)
- [Integrated WiFi and BT support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth/)
- PCIe support
- [Network boot with integrated Ethernet](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/315-network-boot/)
- [Audio support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31F-audio-subsystem/)

### Known issues

- [USB storage devices disappear after reboot/power failure](https://github.com/Dasharo/dasharo-issues/issues/70)
- [Some PCIe ports are not working](https://github.com/Dasharo/dasharo-issues/issues/75)

### Binaries

[MSI PRO Z690-A WIFI DDR4 v0.2.0][v0.2.0_rom]{.md-button}
[sha256][v0.2.0_hash]{.md-button}
[sha256.sig][v0.2.0_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-0.x-compatible-with-msi-ms-7d25-signing-key.asc)

Commands snippet:

```shell
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/3mdeb-dasharo-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-0.x-compatible-with-msi-ms-7d25-signing-key.asc
gpg --list-sigs "3mdeb Master Key" "3mdeb Dasharo Master Key" "Dasharo release 0.x compatible with MSI MS-7D25 signing key"
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.2.0/msi_ms7d25_v0.2.0.rom
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.2.0/msi_ms7d25_v0.2.0.rom.sha256
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.2.0/msi_ms7d25_v0.2.0.rom.sha256.sig
sha256sum -c msi_ms7d25_v0.2.0.rom.sha256
gpg --verify msi_ms7d25_v0.2.0.rom.sha256.sig msi_ms7d25_v0.2.0.rom.sha256
```

### SBOM (Software Bill of Materials)

- [coreboot based on a552cfc9 revision 83fbdcf1](https://github.com/Dasharo/coreboot/tree/83fbdcf1)
- [edk2 based on 4d2846ba revision 0a188758](https://github.com/Dasharo/edk2/tree/0a188758)

## v0.1.0 - 2022-04-13

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/16wokQYhtS7XA1DQC3Om7FY-IImG6SZisGK7NnzyRGVY/edit?usp=sharing).

### Added

- Initial support for the MSI PRO Z690-A WIFI DDR4 platform
- [Dasharo boot logo](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/304-custom-logo/)
- [Dasharo SMBIOS compatibility](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31L-smbios/)
- [UEFI compatibility](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface/)
- [UEFI shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
- One-time boot feature
- [External HDMI and Display Port rear panel display support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd/)
- [USB support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support/)

### Known issues

- [USB storage devices disappear after reboot/power failure](https://github.com/Dasharo/dasharo-issues/issues/70)

### Binaries

[MSI PRO Z690-A WIFI DDR4 v0.1.0][v0.1.0_rom]{.md-button}
[sha256][v0.1.0_hash]{.md-button}
[sha256.sig][v0.1.0_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-0.x-compatible-with-msi-ms-7d25-signing-key.asc)

Commands snippet:

```shell
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/3mdeb-dasharo-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-0.x-compatible-with-msi-ms-7d25-signing-key.asc
gpg --list-sigs "3mdeb Master Key" "3mdeb Dasharo Master Key" "Dasharo release 0.x compatible with MSI MS-7D25 signing key"
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/msi_ms7d25_v0.1.0.rom
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/msi_ms7d25_v0.1.0.rom.sha256
wget https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/msi_ms7d25_v0.1.0.rom.sha256.sig
sha256sum -c msi_ms7d25_v0.1.0.rom.sha256
gpg --verify msi_ms7d25_v0.1.0.rom.sha256.sig msi_ms7d25_v0.1.0.rom.sha256
```

### SBOM (Software Bill of Materials)

- [coreboot based on a552cfc9 revision 53948cd8](https://github.com/Dasharo/coreboot/commit/53948cd8)
- [edk2 based on 4d2846ba revision 4d2846ba](https://github.com/Dasharo/edk2/tree/4d2846ba)

[newsletter]: https://newsletter.3mdeb.com/subscription/aKgTJjYEA
[msi_ms7d25_v1.1.3_ddr4.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.3/msi_ms7d25_v1.1.3_ddr4.rom.sha256
[msi_ms7d25_v1.1.3_ddr4.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.3/msi_ms7d25_v1.1.3_ddr4.rom.sha256.sig
[msi_ms7d25_v1.1.3_ddr4_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.3/msi_ms7d25_v1.1.3_ddr4_dev_signed.rom.sha256
[msi_ms7d25_v1.1.3_ddr4_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.3/msi_ms7d25_v1.1.3_ddr4_dev_signed.rom.sha256.sig
[msi_ms7d25_v1.1.3_ddr5.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.3/msi_ms7d25_v1.1.3_ddr5.rom.sha256
[msi_ms7d25_v1.1.3_ddr5.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.3/msi_ms7d25_v1.1.3_ddr5.rom.sha256.sig
[msi_ms7d25_v1.1.3_ddr5_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.3/msi_ms7d25_v1.1.3_ddr5_dev_signed.rom.sha256
[msi_ms7d25_v1.1.3_ddr5_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.3/msi_ms7d25_v1.1.3_ddr5_dev_signed.rom.sha256.sig
[msi_ms7d25_v1.1.1_ddr4.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr4.rom
[msi_ms7d25_v1.1.1_ddr4.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr4.rom.sha256
[msi_ms7d25_v1.1.1_ddr4.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr4.rom.sha256.sig
[msi_ms7d25_v1.1.1_ddr5.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr5.rom
[msi_ms7d25_v1.1.1_ddr5.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr5.rom.sha256
[msi_ms7d25_v1.1.1_ddr5.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr5.rom.sha256.sig
[msi_ms7d25_v1.1.0_ddr4.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.0/msi_ms7d25_v1.1.0_ddr4.rom
[msi_ms7d25_v1.1.0_ddr4.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.0/msi_ms7d25_v1.1.0_ddr4.rom.sha256
[msi_ms7d25_v1.1.0_ddr4.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.0/msi_ms7d25_v1.1.0_ddr4.rom.sha256.sig
[msi_ms7d25_v1.1.0_ddr5.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.0/msi_ms7d25_v1.1.0_ddr5.rom
[msi_ms7d25_v1.1.0_ddr5.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.0/msi_ms7d25_v1.1.0_ddr5.rom.sha256
[msi_ms7d25_v1.1.0_ddr5.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.0/msi_ms7d25_v1.1.0_ddr5.rom.sha256.sig
[v1.0.0_rom]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.0.0/msi_ms7d25_v1.0.0.rom
[v1.0.0_hash]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.0.0/msi_ms7d25_v1.0.0.rom.sha256
[v1.0.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.0.0/msi_ms7d25_v1.0.0.rom.sha256.sig
[v0.4.0_rom]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.4.0/msi_ms7d25_v0.4.0.rom
[v0.4.0_hash]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.4.0/msi_ms7d25_v0.4.0.rom.sha256
[v0.4.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.4.0/msi_ms7d25_v0.4.0.rom.sha256.sig
[v0.3.0_rom]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.3.0/msi_ms7d25_v0.3.0.rom
[v0.3.0_hash]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.3.0/msi_ms7d25_v0.3.0.rom.sha256
[v0.3.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.3.0/msi_ms7d25_v0.3.0.rom.sha256.sig
[v0.2.0_rom]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.2.0/msi_ms7d25_v0.2.0.rom
[v0.2.0_hash]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.2.0/msi_ms7d25_v0.2.0.rom.sha256
[v0.2.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v0.2.0/msi_ms7d25_v0.2.0.rom.sha256.sig
[v0.1.0_rom]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/msi_ms7d25_v0.1.0.rom
[v0.1.0_hash]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/msi_ms7d25_v0.1.0.rom.sha256
[v0.1.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/msi_ms7d25_v0.1.0.rom.sha256.sig
