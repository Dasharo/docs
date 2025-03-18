# Protectli V1000 series Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development
for Protectli V1000 series.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>
[Subscribe to Protectli Dasharo Release Newsletter]
[newsletter]{.md-button .md-button--primary .center}
</center>

## v0.9.3 - 2024-09-16

Test results for this release can be found here:

- [V1210](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/JSL_v1000/JSL_V1210/v0.9.3_results.csv)
- [V1410](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/JSL_v1000/JSL_V1410/v0.9.3_results.csv)
- [V1610](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/JSL_v1000/JSL_V1610/v0.9.3_results.csv)

### Added

- PC speaker beep on successful boot
- [Serial Console Redirection option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#serial-port-configuration)
- Memory speed is displayed in the firmware setup main page
- [Added support for taking screenshots in the firmware](https://docs.dasharo.com/dev-proc/screenshots/#taking-screenshots)
- Microsoft and Windows 2023 UEFI Secure Boot certificates
- [Option to customize the SMBIOS Serial Number and UUID](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/362-dcu/)
- UEFI 2.8 errata C compliance in EDKII fork
- Support for V1211 variant (same as V1210 but with 8GB RAM)
- SMBIOS fields and strings to reduce differences in SMBIOS between
  proprietary FW and Dasharo
- Intel-specific HDA verbs, for proper audio functionality

### Changed

- Disabled audio DSP
- Disabled SATA due to lack of HW support
- Rebased on official coreboot 4.21
- Updated coreboot-sdk version to 2024-02-18_732134932b
- Removed the i225/i226 EFI driver from the builds in favor of native iPXE
  driver
- Switched iPXE repository to Dasharo fork for the native iPXE driver for
  i225/i226
- [Updated ME to v13.50.27.1987; refer to SBOM section below](https://github.com/Dasharo/dasharo-blobs/tree/main/protectli/vault_jsl)
- Enroll default UEFI Secure Boot keys on the first boot
- [Improved UEFI Secure Boot menu user experience](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
- Scope of reset to default hotkey to global in firmware setup
- Disabled Intel HWP feature causing a decreased network bandwidth due to too
  aggressive CPU power savings, thus not reaching the required performance.

### Fixed

- Auto-boot timeout default value in setup not restored to proper value by F9 key
- Not all Secure Boot settings required a reset
- Errors related to WiFi L0 showing up in dmesg
- Not all Dasharo variables were measured at boot
- Windows default drivers not probing successfully due to SSID programming

#### Binaries

[protectli_v1210_v0.9.3.rom][protectli_v1210_v0.9.3.rom_file]{.md-button}
[sha256][protectli_v1210_v0.9.3.rom_hash]{.md-button}
[sha256.sig][protectli_v1210_v0.9.3.rom_sig]{.md-button}
[protectli_v1211_v0.9.3.rom][protectli_v1211_v0.9.3.rom_file]{.md-button}
[sha256][protectli_v1211_v0.9.3.rom_hash]{.md-button}
[sha256.sig][protectli_v1211_v0.9.3.rom_sig]{.md-button}
[protectli_v1410_v0.9.3.rom][protectli_v1410_v0.9.3.rom_file]{.md-button}
[sha256][protectli_v1410_v0.9.3.rom_hash]{.md-button}
[sha256.sig][protectli_v1410_v0.9.3.rom_sig]{.md-button}
[protectli_v1610_v0.9.3.rom][protectli_v1610_v0.9.3.rom_file]{.md-button}
[sha256][protectli_v1610_v0.9.3.rom_hash]{.md-button}
[sha256.sig][protectli_v1610_v0.9.3.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://github.com/3mdeb/3mdeb-secpack/raw/master/customer-keys/protectli/release-keys/dasharo-release-0.9.x-for-protectli-signing-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 4.21 revision ee437086](https://github.com/Dasharo/coreboot/tree/ee437086)
    + [License](https://github.com/Dasharo/coreboot/blob/ee437086/COPYING)
- [Dasharo EDKII fork based on f06673308f revision f0667330](https://github.com/Dasharo/edk2/tree/f0667330)
    + [License](https://github.com/Dasharo/edk2/blob/f0667330/License.txt)
- [Dasharo iPXE fork based on 838611b34e revision 838611b3](https://github.com/Dasharo/ipxe/tree/838611b3)
    + [License](https://github.com/Dasharo/ipxe/blob/838611b3/COPYING.GPLv2)
- [Intel Management Engine based on v13.50.27.1987 revision 9712e97a](https://github.com/Dasharo/dasharo-blobs/blob/9712e97a/protectli/vault_jsl/)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor based on v1.0 revision 9712e97a](https://github.com/Dasharo/dasharo-blobs/blob/9712e97a/protectli/vault_jsl)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package based on JSL 2021/08/23 v2115 revision 9712e97a](https://github.com/Dasharo/dasharo-blobs/blob/9712e97a/protectli/vault_jsl/JasperLakeFspBinPkg)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel microcode based on JSL A0 0x24000026 revision microcode-20240312](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240312/intel-ucode/06-9c-00)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240312/license)

[newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
[protectli_v1210_v0.9.3.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1210_v0.9.3.rom
[protectli_v1210_v0.9.3.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1210_v0.9.3.rom.sha256
[protectli_v1210_v0.9.3.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1210_v0.9.3.rom.sha256.sig
[protectli_v1211_v0.9.3.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl_v1211/v0.9.3/protectli_v1211_v0.9.3.rom
[protectli_v1211_v0.9.3.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl_v1211/v0.9.3/protectli_v1211_v0.9.3.rom.sha256
[protectli_v1211_v0.9.3.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl_v1211/v0.9.3/protectli_v1211_v0.9.3.rom.sha256.sig
[protectli_v1410_v0.9.3.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1410_v0.9.3.rom
[protectli_v1410_v0.9.3.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1410_v0.9.3.rom.sha256
[protectli_v1410_v0.9.3.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1410_v0.9.3.rom.sha256.sig
[protectli_v1610_v0.9.3.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1610_v0.9.3.rom
[protectli_v1610_v0.9.3.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1610_v0.9.3.rom.sha256
[protectli_v1610_v0.9.3.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1610_v0.9.3.rom.sha256.sig
