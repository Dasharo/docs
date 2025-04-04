# Protectli VP2420 Dasharo Release Notes

Following Release Notes describe status of open-source firmware development
for Protectli VP2420.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("49abc4a2-0807-4720-aef2-b150ef701b30",
"Subscribe to Protectli Dasharo Release Newsletter") }}

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit#gid=270990532).

## v1.2.1 - 2025-03-12

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/VP2420/v1.2.1-results.csv).

### Added

- [Power State after AC loss feature](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Configurable CPU throttling temperature](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Human-readable certificate names in UEFI Secure Boot menu](https://github.com/Dasharo/dasharo-issues/issues/645)

### Changed

- Updated coreboot base to 24.02. Please refer to SBOM section for details
- Updated UEFI payload base to edk2-stable202402. Please refer to SBOM section
  for details
- Updated microcode blob. Please refer to SBOM section for details
- Updated FSP blob. Please refer to SBOM section for details
- [Removed UEFI Shell](https://github.com/Dasharo/dasharo-issues/issues/1218)
- Removed the autoboot timeout in the iPXE menu
- ME PCI device hidden to match the behavior of other Protectli devices with
  ME disabled
- Updated UEFI Secure Boot DBX to 2025-02-24
- [Simplified setup password policy](https://github.com/Dasharo/dasharo-issues/issues/646)

### Known issues

- [Certain PCIe WiFi cards may cause AER error](https://github.com/Dasharo/dasharo-issues/issues/1214)
- [STB002.001 encounters unlisted error](https://github.com/Dasharo/dasharo-issues/issues/1013)

### Binaries

[protectli_vp2420_v1.2.1.rom][protectli_vp2420_v1.2.1.rom_file]{.md-button}
[sha256][protectli_vp2420_v1.2.1.rom_hash]{.md-button}
[sha256.sig][protectli_vp2420_v1.2.1.rom_sig]{.md-button}

[protectli_vp2420_v1.2.1_dev_signed.rom][protectli_vp2420_v1.2.1_dev_signed.rom_file]{.md-button}
[sha256][protectli_vp2420_v1.2.1_dev_signed.rom_hash]{.md-button}
[sha256.sig][protectli_vp2420_v1.2.1_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/refs/heads/master/customer-keys/protectli/release-keys/dasharo-release-1.2.x-for-protectli-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 24.02 revision 832c6333](https://github.com/Dasharo/coreboot/tree/832c6333)
    + [License](https://github.com/Dasharo/coreboot/blob/832c6333/COPYING)
- [Dasharo EDKII fork based on edk2-stable202402 revision 8d06fe48](https://github.com/Dasharo/edk2/tree/8d06fe48)
    + [License](https://github.com/Dasharo/edk2/blob/8d06fe48/License.txt)
- [Dasharo iPXE fork based on 2024.05 revision 63ed3e35](https://github.com/Dasharo/ipxe/tree/63ed3e35)
    + [License](https://github.com/Dasharo/ipxe/blob/63ed3e35/COPYING.GPLv2)
- [vboot based on 3d37d2aafe revision 3d37d2aa](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/LICENSE)
- [Intel Management Engine version v15.40.32.2910](https://github.com/Dasharo/dasharo-blobs/blob/5e9a8713/protectli/vault_ehl/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/5e9a8713/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/5e9a8713/protectli/vault_ehl/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/5e9a8713/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version Elkhart Lake IPU2024.2](https://github.com/intel/FSP/tree/3819544e/ElkhartLakeFspBinPkg/)
    + [License](https://github.com/intel/FSP/blob/3819544e/FSP_License.pdf)
- [Intel microcode version EHL B1 0x1a 05/04/2024](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20250211/intel-ucode/06-96-01)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20250211/license)

[protectli_vp2420_v1.2.1.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.1/protectli_vp2420_v1.2.1.rom
[protectli_vp2420_v1.2.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.1/protectli_vp2420_v1.2.1.rom.sha256
[protectli_vp2420_v1.2.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.1/protectli_vp2420_v1.2.1.rom.sha256.sig
[protectli_vp2420_v1.2.1_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.1/protectli_vp2420_v1.2.1_dev_signed.rom
[protectli_vp2420_v1.2.1_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.1/protectli_vp2420_v1.2.1_dev_signed.rom.sha256
[protectli_vp2420_v1.2.1_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.1/protectli_vp2420_v1.2.1_dev_signed.rom.sha256.sig

## v1.2.0 - 2024-05-16

### Added

- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
- [Serial port console redirection option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#serial-port-configuration)
- [Customizable Serial Number and UUID via CBFS support](https://github.com/Dasharo/dcu)
- [Customizable boot logo support](https://github.com/Dasharo/dcu)
- [Support for taking screenshots in the firmware](https://docs.dasharo.com/dev-proc/screenshots/#taking-screenshots)
- [ESP partition scanning in look for grubx64.efi or shimx64.efi or Windows bootmgr](https://github.com/Dasharo/dasharo-issues/issues/94)
- Microsoft and Windows 2023 UEFI Secure Boot certificates
- UEFI 2.8 errata C compliance in EDKII fork

### Changed

- Rebased to coreboot 4.21
- Enroll default UEFI Secure Boot keys on the first boot
- [Improved UEFI Secure Boot menu user experience](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
- Scope of reset to defaults hotkey to global in firmware setup
- Updated microcode to the newer version; refer to SBOM section below
- Updated ME to the newer version; refer to SBOM section below

### Fixed

- [Auto Boot Time-out is reset to 0 when F9 is pressed](https://github.com/Dasharo/dasharo-issues/issues/513)
- [Reset to defaults with F9 causes the wrong settings to be restored](https://github.com/Dasharo/dasharo-issues/issues/355)
- [RTC time and date resetting to the coreboot build date on 29th February](https://review.coreboot.org/c/coreboot/+/80790)
- [Cannot set custom bootsplash in firmware via DCU nor cbfstool](https://github.com/Dasharo/dasharo-issues/issues/759)

### Binaries

[protectli_vp2420_v1.2.0.rom][protectli_vp2420_v1.2.0.rom_file]{.md-button}
[sha256][protectli_vp2420_v1.2.0.rom_hash]{.md-button}
[sha256.sig][protectli_vp2420_v1.2.0.rom_sig]{.md-button}

[protectli_vp2420_v1.2.0_dev_signed.rom][protectli_vp2420_v1.2.0_dev_signed.rom_file]{.md-button}
[sha256][protectli_vp2420_v1.2.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][protectli_vp2420_v1.2.0_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/dasharo-release-1.2.x-for-protectli-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 4.21 revision 7c2c79e8](https://github.com/Dasharo/coreboot/tree/7c2c79e8)
- [Dasharo EDKII fork based on edk2-stable202002 revision ae0ce3e2](https://github.com/Dasharo/edk2/tree/ae0ce3e2)
- [iPXE based on 2023.12 revision 838611b3](https://github.com/Dasharo/ipxe/tree/838611b3)
- [vboot based on 0c11187c75 revision 0c11187c](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/0c11187c/)
- [Intel Management Engine based on v15.40.32.2910 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/protectli/vault_ehl/me.bin)
- [Intel Flash Descriptor based on v1.0 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/protectli/vault_ehl/descriptor.bin)
- [Intel Firmware Support Package based on Elkhart Lake MR6 revision 481ea7cf](https://github.com/intel/FSP/tree/481ea7cf/ElkhartLakeFspBinPkg/)
- [Intel microcode based on EHL B1 0x00000016 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-96-01)

[protectli_vp2420_v1.2.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.0/protectli_vp2420_v1.2.0.rom
[protectli_vp2420_v1.2.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.0/protectli_vp2420_v1.2.0.rom.sha256
[protectli_vp2420_v1.2.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.0/protectli_vp2420_v1.2.0.rom.sha256.sig
[protectli_vp2420_v1.2.0_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.0/protectli_vp2420_v1.2.0_dev_signed.rom
[protectli_vp2420_v1.2.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.0/protectli_vp2420_v1.2.0_dev_signed.rom.sha256
[protectli_vp2420_v1.2.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.0/protectli_vp2420_v1.2.0_dev_signed.rom.sha256.sig

## v1.1.0 - 2023-04-20

### Added

- [USB stack and mass storage enable/disable option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [SMM BIOS write protection enable/disable option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)

### Changed

- [Updating from v1.0.x requires flashing the WP_RO recovery partition](../../unified/protectli/firmware-update.md#vp2420)
- [Firmware version v1.1.x are signed with a new key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/dasharo-release-1.1.x-for-protectli-signing-key.asc)
- [Keys must be provisioned prior enabling Secure Boot](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)

### Fixed

- [VP2420 memory issues and incorrectly reported memory capacity](https://github.com/Dasharo/dasharo-issues/issues/397)
- [Popup with information about recovery mode is still displayed after flashing with a valid binary](https://github.com/Dasharo/dasharo-issues/issues/320)

### Known issues

- [pfSense boot time](https://github.com/Dasharo/dasharo-issues/issues/318)
- [Double characters in pfSense initial boot phase](https://github.com/Dasharo/dasharo-issues/issues/319)

### Binaries

[protectli_vp2420_v1.1.0.rom][protectli_vp2420_v1.1.0.rom_file]{.md-button}
[sha256][protectli_vp2420_v1.1.0.rom_hash]{.md-button}
[sha256.sig][protectli_vp2420_v1.1.0.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/dasharo-release-1.1.x-for-protectli-signing-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on c86c926 revision e36a117d](https://github.com/Dasharo/coreboot/tree/e36a117d)
- [edk2 based on 7f90b9cd revision 19bf14b4](https://github.com/Dasharo/edk2/tree/19bf14b4)

[protectli_vp2420_v1.1.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.1.0/protectli_vp2420_v1.1.0.rom
[protectli_vp2420_v1.1.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.1.0/protectli_vp2420_v1.1.0.rom.sha256
[protectli_vp2420_v1.1.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.1.0/protectli_vp2420_v1.1.0.rom.sha256.sig

## v1.0.1 - 2023-02-02

### Added

- [TPM 2.0 support over SPI interface](https://docs.dasharo.com/unified-test-documentation/dasharo-security/200-tpm-support/#test-cases-common-documentation)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)

### Changed

- Downgrade edk2 Secure Boot driver to achieve consistent user experience as on
  the VP46XX v1.0.19 release

### Fixed

- [Dasharo BIOS lock menu is missing](https://github.com/Dasharo/dasharo-issues/issues/291)
- [iPXE entry doesn't occur in setup menu](https://github.com/Dasharo/dasharo-issues/issues/289)
- [Impossibility of pfSense/OPNsense console versions installation](https://github.com/Dasharo/dasharo-issues/issues/289)

### Known issues

- [Popup with information about recovery mode is still displayed after flashing with a valid binary](https://github.com/Dasharo/dasharo-issues/issues/320)
- [pfSense boot time](https://github.com/Dasharo/dasharo-issues/issues/318)
- [Double characters in pfSense initial boot phase](https://github.com/Dasharo/dasharo-issues/issues/319)

### Binaries

[protectli_vp2420_v1.0.1.rom][protectli_vp2420_v1.0.1.rom_file]{.md-button}
[sha256][protectli_vp2420_v1.0.1.rom_hash]{.md-button}
[sha256.sig][protectli_vp2420_v1.0.1.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/protectli-dasharo-firewall-release-1.0-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on c86c926 revision 54cbbc5b](https://github.com/Dasharo/coreboot/tree/54cbbc5b)
- [edk2 based on 7f90b9cd revision e31b7a71](https://github.com/Dasharo/edk2/tree/e31b7a71)

[protectli_vp2420_v1.0.1.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.1/protectli_vp2420_v1.0.1.rom
[protectli_vp2420_v1.0.1.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.1/protectli_vp2420_v1.0.1.rom.sha256
[protectli_vp2420_v1.0.1.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.1/protectli_vp2420_v1.0.1.rom.sha256.sig

## v1.0.0 - 2022-12-22

### Added

- Support for VP2420 platform
- [Vboot Verified Boot](https://docs.dasharo.com../../guides/vboot-signing/)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [Vboot recovery notification in UEFI Payload](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)
- [UEFI Shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
- [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [BIOS flash protection for Vboot recovery region](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20J-bios-lock-support/)
- UEFI boot support
- Intel i225 controller network boot support
- Customized boot menu keys
- Customized setup menu keys
- Configurable boot order
- Configurable boot options

### Binaries

[protectli_VP2420_v1.0.0.rom][v1.0.0_rom]{.md-button}
[sha256][v1.0.0_hash]{.md-button}
[sha256.sig][v1.0.0_sig]{.md-button}

How to verify signatures:

```bash
wget https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom
wget https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256
wget https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256.sig
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/3mdeb-dasharo-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/protectli-dasharo-firewall-release-1.0-key.asc
gpg --list-sigs "3mdeb Master Key" "3mdeb Dasharo Master Key" "Protectli Dasharo Firewall Release 1.0 Signing Key"
sha256sum -c protectli_vp2420_v1.0.0.rom.sha256
gpg -v --verify protectli_vp2420_v1.0.0.rom.sha256.sig protectli_vp2420_v1.0.0.rom.sha256
```

### SBOM (Software Bill of Materials)

- [coreboot based on c492b427 revision c86c9266](https://github.com/Dasharo/coreboot/tree/c86c9266)
- [edk2 based on e461f08 revision 7948a20](https://github.com/Dasharo/edk2/tree/7948a20)
- [iPXE for EFI revision 988d2](https://github.com/ipxe/ipxe/tree/988d2c13cdf0f0b4140685af35ced70ac5b3283c)

[v1.0.0_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom
[v1.0.0_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256
[v1.0.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256.sig
