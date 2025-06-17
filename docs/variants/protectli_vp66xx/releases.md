# Protectli VP6630/VP6650/VP6670 Dasharo Release Notes

Following Release Notes describe status of open-source firmware development
for Protectli VP6630/VP6650/VP6670

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("49abc4a2-0807-4720-aef2-b150ef701b30",
"Subscribe to Protectli Dasharo Release Newsletter") }}

## v0.9.2 - 2025-06-17

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/VP66xx/).

### Fixed

- [DisplayPort has trouble working with certain monitors](https://github.com/Dasharo/dasharo-issues/issues/1015)
- [ESXI installer fails to boot on VP66xx](https://github.com/Dasharo/dasharo-issues/issues/1232)

### Known issues

- [UEFI Shell sourced from Dasharo FW image in VP6650](https://github.com/Dasharo/dasharo-issues/issues/1362)
- [STB002.001 encounters unlisted errors](https://github.com/Dasharo/dasharo-issues/issues/1013)

### Binaries

[protectli_vp66xx_v0.9.2.rom][protectli_vp66xx_v0.9.2.rom_file]{.md-button}
[sha256][protectli_vp66xx_v0.9.2.rom_hash]{.md-button}
[sha256.sig][protectli_vp66xx_v0.9.2.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://github.com/3mdeb/3mdeb-secpack/blob/master/customer-keys/protectli/release-keys/dasharo-release-0.9.x-for-protectli-signing-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 24.02 revision 824b40cd](https://github.com/Dasharo/coreboot/tree/824b40cd)
    + [License](https://github.com/Dasharo/coreboot/blob/824b40cd/COPYING)
- [Dasharo EDKII fork based on edk2-stable202405 revision 787234d5](https://github.com/Dasharo/edk2/tree/787234d5)
    + [License](https://github.com/Dasharo/edk2/blob/787234d5/License.txt)
- [Dasharo iPXE fork based on 2023.12 revision 35d84756](https://github.com/Dasharo/ipxe/tree/35d84756)
    + [License](https://github.com/Dasharo/ipxe/blob/35d84756/COPYING.GPLv2)
- [vboot based on 3d37d2aafe revision 3d37d2aa](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/LICENSE)
- [Intel Management Engine version v16.1.25.1865-v0.1](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/protectli/vault_adl_p/)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.2](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/protectli/vault_adl_p/)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version IoT RPL-P MR1 (4445_03)](https://github.com/intel/FSP/commits/3819544e/RaptorLakeFspBinPkg/IoT/RaptorLakeP)
    + [License](https://github.com/intel/FSP/blob/3819544e/FSP_License.pdf)
- [Intel microcode version ADL R0 0x433 05/12/2023](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240531/intel-ucode/06-9a-04)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240531/license)
- [Intel microcode version RPL-H/P/PX 6+8 J0 0x4121 07/12/2023](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240531/intel-ucode/06-ba-02)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240531/license)

[protectli_vp66xx_v0.9.2.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/uefi/v0.9.2/protectli_vp66xx_v0.9.2.rom
[protectli_vp66xx_v0.9.2.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/uefi/v0.9.2/protectli_vp66xx_v0.9.2.rom.sha256
[protectli_vp66xx_v0.9.2.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/uefi/v0.9.2/protectli_vp66xx_v0.9.2.rom.sha256.sig

## v0.9.1 - 2025-01-23

Test results for this release can be found for [VP6650](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/VP66xx/VP6650_v0.9.1_results.csv)
and [VP6670](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/VP66xx/VP6670_v0.9.1_results.csv).

### Added

- [CPU throttling option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Power state after AC loss option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Fan control option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)

### Changed

- Rebased coreboot to 24.02
- Rebased edk2 to edk2-stable202405
- Updated Intel ME and Flash Descriptor (refer to SBOM section)

### Fixed

- [TPM Physical Presence interface not working in TPM2 setup menu](https://github.com/Dasharo/dasharo-issues/issues/521)
- Platform is power cycling instead of resetting during reboot or reset from
  setup menu

### Known issues

- [DisplayPort has trouble working with certain monitors](https://github.com/Dasharo/dasharo-issues/issues/1015)
- [STB002.201 encounters unlisted errors](https://github.com/Dasharo/dasharo-issues/issues/1013)

### Binaries

[protectli_vp66xx_v0.9.1.rom][protectli_vp66xx_v0.9.1.rom_file]{.md-button}
[sha256][protectli_vp66xx_v0.9.1.rom_hash]{.md-button}
[sha256.sig][protectli_vp66xx_v0.9.1.rom_sig]{.md-button}

[protectli_vp66xx_v0.9.1_dev_signed.rom][protectli_vp66xx_v0.9.1_dev_signed.rom_file]{.md-button}
[sha256][protectli_vp66xx_v0.9.1_dev_signed.rom_hash]{.md-button}
[sha256.sig][protectli_vp66xx_v0.9.1_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/dasharo-open-source-firmware-engineering-release-signing-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 24.02 revision 225d907a](https://github.com/Dasharo/coreboot/tree/225d907a)
    + [License](https://github.com/Dasharo/coreboot/blob/225d907a/COPYING)
- [Dasharo EDKII fork based on edk2-stable202405 revision 8a9fd05f](https://github.com/Dasharo/edk2/tree/8a9fd05f)
    + [License](https://github.com/Dasharo/edk2/blob/8a9fd05f/License.txt)
- [Dasharo iPXE fork based on 2023.12 revision 35d84756](https://github.com/Dasharo/ipxe/tree/35d84756)
    + [License](https://github.com/Dasharo/ipxe/blob/35d84756/COPYING.GPLv2)
- [vboot based on 3d37d2aafe revision 3d37d2aa](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/LICENSE)
- [Intel Management Engine version v16.1.25.1865-v0.1](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/protectli/vault_adl_p/)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.2](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/protectli/vault_adl_p/)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version IoT RPL-P MR1 (4445_03)](https://github.com/intel/FSP/commits/3819544e/RaptorLakeFspBinPkg/IoT/RaptorLakeP)
    + [License](https://github.com/intel/FSP/blob/3819544e/FSP_License.pdf)
- [Intel microcode version ADL R0 0x433 05/12/2023](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240531/intel-ucode/06-9a-04)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240531/license)
- [Intel microcode version RPL-H/P/PX 6+8 J0 0x4121 07/12/2023](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240531/intel-ucode/06-ba-02)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240531/license)

## v0.9.0 - 2024-09-11

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/VP66xx/v0.9.0-results.csv).

### Added

- Initial support for Protectli Alder Lake devices VP66XX
- [UEFI compatible interface](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface/)
- [Support for discrete TPM](https://docs.dasharo.com/unified-test-documentation/dasharo-security/200-tpm-support/)
- [UEFI Secure Boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [Boot logo customization support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/328-logo-customization-functionality/)
- [USB boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31N-usb-boot/)
- [NVMe boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/312-nvme-support/)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [UEFI Shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
- [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [Network boot](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/315b-netboot-utilities/)
- [Windows 11 booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31A-windows-booting/)
- [Ubuntu LTS booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support/)
- [Serial port console redirection](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31G-ec-and-superio/#sio004001-serial-port-in-firmware)
- [Vboot Verified Boot](https://docs.dasharo.com/guides/vboot-signing/)
- [Intel ME HAP disable](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20F-me-neuter/)
- [BIOS flash protection for Vboot recovery region](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20J-bios-lock-support/)
- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
- [SMM BIOS write protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Network stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#networking-options)

### Known issues

- [DisplayPort has trouble working with certain monitors](https://github.com/Dasharo/dasharo-issues/issues/1015)
- [STB002.201 encounters unlisted errors](https://github.com/Dasharo/dasharo-issues/issues/1013)

### Binaries

[protectli_vp66xx_v0.9.0.rom][protectli_vp66xx_v0.9.0.rom_file]{.md-button}
[sha256][protectli_vp66xx_v0.9.0.rom_hash]{.md-button}
[sha256.sig][protectli_vp66xx_v0.9.0.rom_sig]{.md-button}

[protectli_vp66xx_v0.9.0_dev_signed.rom][protectli_vp66xx_v0.9.0_dev_signed.rom_file]{.md-button}
[sha256][protectli_vp66xx_v0.9.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][protectli_vp66xx_v0.9.0_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/dasharo-open-source-firmware-engineering-release-signing-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 4.21 revision 50887bab](https://github.com/Dasharo/coreboot/tree/50887bab)
- [Dasharo EDKII fork based on f06673308f revision f0667330](https://github.com/Dasharo/edk2/tree/f0667330)
- [Dasharo iPXE fork based on 838611b34e revision 838611b3](https://github.com/Dasharo/ipxe/tree/838611b3)
- [Intel Management Engine based on v16.1.25.1865 revision 9712e97a](https://github.com/Dasharo/dasharo-blobs/blob/9712e97a/protectli/vault_adl_p/)
- [Intel Flash Descriptor based on v1.1 revision 9712e97a](https://github.com/Dasharo/dasharo-blobs/blob/9712e97a/protectli/vault_adl_p/)
- [Intel Firmware Support Package based on IoT RPL-P MR1 (4445_03) revision a6ee9636](https://github.com/intel/FSP/commits/a6ee9636/RaptorLakeFspBinPkg/IoT/RaptorLakeP)
- [Intel microcode based on ADL R0 0x432 revision microcode-20240312](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240312/intel-ucode/06-9a-04)
- [Intel microcode based on RPL-H/P/PX 6+8 J0 0x4121 revision microcode-20240312](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240312/intel-ucode/06-ba-02)

[protectli_vp66xx_v0.9.1.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.1/protectli_vp66xx_v0.9.1.rom
[protectli_vp66xx_v0.9.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.1/protectli_vp66xx_v0.9.1.rom.sha256
[protectli_vp66xx_v0.9.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.1/protectli_vp66xx_v0.9.1.rom.sha256.sig
[protectli_vp66xx_v0.9.1_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.1/protectli_vp66xx_v0.9.1_dev_signed.rom
[protectli_vp66xx_v0.9.1_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.1/protectli_vp66xx_v0.9.1_dev_signed.rom.sha256
[protectli_vp66xx_v0.9.1_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.1/protectli_vp66xx_v0.9.1_dev_signed.rom.sha256.sig
[protectli_vp66xx_v0.9.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.0/protectli_vp66xx_v0.9.0.rom
[protectli_vp66xx_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.0/protectli_vp66xx_v0.9.0.rom.sha256
[protectli_vp66xx_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.0/protectli_vp66xx_v0.9.0.rom.sha256.sig
[protectli_vp66xx_v0.9.0_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.0/protectli_vp66xx_v0.9.0_dev_signed.rom
[protectli_vp66xx_v0.9.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.0/protectli_vp66xx_v0.9.0_dev_signed.rom.sha256
[protectli_vp66xx_v0.9.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.0/protectli_vp66xx_v0.9.0_dev_signed.rom.sha256.sig
