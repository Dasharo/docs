# Protectli V1000 series Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development
for Protectli V1000 series.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("49abc4a2-0807-4720-aef2-b150ef701b30",
"Subscribe to Protectli Dasharo Release Newsletter") }}

## v0.9.4 - 2025-12-18

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/JSL_v1000/).

### Added

- [Intel Management Engine Options menu (Disable Soft and Disable HAP)](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#intel-management-engine-options)
- [CPU Throttling Temperature Offset option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Power state after power or AC loss option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/)
- [Enable wake from USB devices on Jasper Lake](https://github.com/Dasharo/coreboot/commit/d2f6b3fa9c068c9a0177a2eb921a4b69a34b8447)
- [Intel Jasper Lake CrashLog support](https://github.com/Dasharo/coreboot/commit/07dd73c9214b766762a89ffe51f27c77799293be)

### Changed

- [Don't report LANs via SMBIOS Type 41](https://github.com/Dasharo/coreboot/pull/775/commits/082684648c22fc786deea7fc0c4c6ea27103f4ed)
- [Handle dynamic switching between NVMe and SATA for the M.2 slot on Protectli Vault JSL](https://github.com/Dasharo/coreboot/commit/0ce04fba800d56dd7b10a1a2a6068c1335e7d494)
- [Update flash descriptor binaries for Protectli Vault JSL variants (V1210 NVMe x2 and SATA, correct bifurcation, V1410 and V1610 updates)](https://github.com/Dasharo/dasharo-blobs/commit/0e5218dde63db6480d95f830be66dfcd37732352)
- [Add ACPI names for missing USB3 ports on Jasper Lake](https://github.com/Dasharo/coreboot/commit/a56fad6ca8f70169e020d0b76963b1adc32c52f8)
- [Expose SuperIO UART in ACPI DSDT](https://github.com/Dasharo/coreboot/commit/85a6b6cc96162a0d5cd7523fe8b22f48db78c091)
- [Predictable Linux NIC naming by exposing onboard NIC as eno](https://github.com/Dasharo/coreboot/commit/f3fed0fcf6e0e7f24f7b69c415ae0a7096bbdbe8)
- [Add PC speaker beep codes for boot errors](https://github.com/Dasharo/coreboot/commit/e082e953fd68fc8602d0e7b82f6715e5fca5bf2d)
- [Prevent wake events from the USB hub port on Protectli Vault JSL](https://github.com/Dasharo/coreboot/commit/6b14f4da3cbaa60b1ca71d0fb2c7b471967b94ca)
- [Remove iPXE menu timeout on Protectli platforms](https://github.com/Dasharo/coreboot/pull/613)

### Fixed

- [M.2 SATA devices not detected on Protectli V12xx](https://github.com/Dasharo/dasharo-issues/issues/1401)
- [Efibootmgr returns Bad address on FreeBSD on Protectli V1410](https://github.com/Dasharo/dasharo-issues/issues/1001)
- [SUSP DUT wakes up from S3 instantly](https://github.com/Dasharo/dasharo-issues/issues/1332)

### Known issues

- [Power LED constantly on in suspend on Protectli V1x10](https://github.com/Dasharo/dasharo-issues/issues/1636)
- [Atheros QCA6174 behind ASMedia ASM1806 switch isn't always detected](https://github.com/Dasharo/dasharo-issues/issues/961)
- [TCG2 Configuration missing when changing Intel ME mode Disabled (HAP) -> Enabled](https://github.com/Dasharo/dasharo-issues/issues/1106)

### Binaries

[protectli_v1210_v0.9.4.rom][protectli_v1210_v0.9.4.rom_file]{.md-button}
[sha256][protectli_v1210_v0.9.4.rom_hash]{.md-button}
[sha256.sig][protectli_v1210_v0.9.4.rom_sig]{.md-button}

[protectli_v1211_v0.9.4.rom][protectli_v1211_v0.9.4.rom_file]{.md-button}
[sha256][protectli_v1211_v0.9.4.rom_hash]{.md-button}
[sha256.sig][protectli_v1211_v0.9.4.rom_sig]{.md-button}

[protectli_v1410_v0.9.4.rom][protectli_v1410_v0.9.4.rom_file]{.md-button}
[sha256][protectli_v1410_v0.9.4.rom_hash]{.md-button}
[sha256.sig][protectli_v1410_v0.9.4.rom_sig]{.md-button}

[protectli_v1610_v0.9.4.rom][protectli_v1610_v0.9.4.rom_file]{.md-button}
[sha256][protectli_v1610_v0.9.4.rom_hash]{.md-button}
[sha256.sig][protectli_v1610_v0.9.4.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://github.com/3mdeb/3mdeb-secpack/raw/master/customer-keys/protectli/release-keys/dasharo-release-0.9.x-for-protectli-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 24.12 revision 270ea70b](https://github.com/Dasharo/coreboot/tree/270ea70b)
    + [License](https://github.com/Dasharo/coreboot/blob/270ea70b/COPYING)
- [Dasharo EDKII fork based on edk2-stable202502 revision 3bde471c](https://github.com/Dasharo/edk2/tree/3bde471c)
    + [License](https://github.com/Dasharo/edk2/blob/3bde471c/License.txt)
- [iPXE based on 2025.03 revision 6c7068fc](https://github.com/Dasharo/ipxe/tree/6c7068fc)
    + [License](https://github.com/Dasharo/ipxe/blob/6c7068fc/COPYING.GPLv2)
- [Intel Management Engine version v13.50.27.1987](https://github.com/Dasharo/dasharo-blobs/blob/0ca1dcac/protectli/vault_jsl/)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.1/v1.2(V1210)](https://github.com/Dasharo/dasharo-blobs/blob/0ca1dcac/protectli/vault_jsl)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version JSL 2021/08/23 v2115](https://github.com/Dasharo/dasharo-blobs/blob/0ca1dcac/protectli/vault_jsl/JasperLakeFspBinPkg)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel microcode version JSL A0](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20251111/intel-ucode/06-9c-00)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20251111/license)

[protectli_v1210_v0.9.4.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/uefi/v0.9.4/protectli_v1210_v0.9.4.rom
[protectli_v1210_v0.9.4.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/uefi/v0.9.4/protectli_v1210_v0.9.4.rom.sha256
[protectli_v1210_v0.9.4.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/uefi/v0.9.4/protectli_v1210_v0.9.4.rom.sha256.sig
[protectli_v1211_v0.9.4.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/uefi/v0.9.4/protectli_v1211_v0.9.4.rom
[protectli_v1211_v0.9.4.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/uefi/v0.9.4/protectli_v1211_v0.9.4.rom.sha256
[protectli_v1211_v0.9.4.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/uefi/v0.9.4/protectli_v1211_v0.9.4.rom.sha256.sig
[protectli_v1410_v0.9.4.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/uefi/v0.9.4/protectli_v1410_v0.9.4.rom
[protectli_v1410_v0.9.4.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/uefi/v0.9.4/protectli_v1410_v0.9.4.rom.sha256
[protectli_v1410_v0.9.4.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/uefi/v0.9.4/protectli_v1410_v0.9.4.rom.sha256.sig
[protectli_v1610_v0.9.4.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/uefi/v0.9.4/protectli_v1610_v0.9.4.rom
[protectli_v1610_v0.9.4.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/uefi/v0.9.4/protectli_v1610_v0.9.4.rom.sha256
[protectli_v1610_v0.9.4.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/uefi/v0.9.4/protectli_v1610_v0.9.4.rom.sha256.sig

## v0.9.3 - 2024-09-16

Test results for this release can be found here:

- [V1210](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/JSL_v1000/JSL_V1210/v0.9.3_results.csv)
- [V1211](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/JSL_v1000/JSL_V1210/v0.9.3_results.csv)
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
- Auto-boot timeout default value in setup gets restored to proper value by F9 key
- All Secure Boot settings require a reset
- No errors related to WiFi L0 showing up in dmesg
- All Dasharo variables get measured at boot
- Windows default drivers probe successfully

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

[protectli_v1210_v0.9.3.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1210_v0.9.3.rom
[protectli_v1210_v0.9.3.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1210_v0.9.3.rom.sha256
[protectli_v1210_v0.9.3.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1210_v0.9.3.rom.sha256.sig
[protectli_v1211_v0.9.3.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1211_v0.9.3.rom
[protectli_v1211_v0.9.3.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1211_v0.9.3.rom.sha256
[protectli_v1211_v0.9.3.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1211_v0.9.3.rom.sha256.sig
[protectli_v1410_v0.9.3.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1410_v0.9.3.rom
[protectli_v1410_v0.9.3.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1410_v0.9.3.rom.sha256
[protectli_v1410_v0.9.3.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1410_v0.9.3.rom.sha256.sig
[protectli_v1610_v0.9.3.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1610_v0.9.3.rom
[protectli_v1610_v0.9.3.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1610_v0.9.3.rom.sha256
[protectli_v1610_v0.9.3.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1610_v0.9.3.rom.sha256.sig

## v0.9.0 .. v0.9.2 - Non-public engineering releases
