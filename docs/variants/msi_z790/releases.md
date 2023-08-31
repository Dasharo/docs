# MSI PRO Z790-P (WIFI) (DDR4) Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
MSI PRO Z790-P (WIFI) (DDR4)

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

[Subscribe to MSI PRO Z790-P (WIFI) (DDR4) Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

</center>

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

- [This is a Dasharo Entry Subscription release](https://docs.dasharo.com/dev-proc/versioning/#dasharo-entry-subscription-releases)
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

This is a Dasharo Entry Subscription Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Entry Subscription subscriber](../../ways-you-can-help-us.md#become-a-dasharo-entry-subscription-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Entry Subscription newsletter.

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
