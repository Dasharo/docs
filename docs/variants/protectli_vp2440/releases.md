# Protectli VP2440 Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
Protectli VP2440.

{{ subscribe_form("49abc4a2-0807-4720-aef2-b150ef701b30",
"Subscribe to Protectli Dasharo Release Newsletter") }}

## v0.9.0 - 2025-08-27

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/VP2440/v0.9.0-results.csv).

### Added

- Initial support for Protectli Alder Lake N devices (Vault Pro 2440)
- [UEFI compatible interface](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface/)
- [Support for discrete TPM](https://docs.dasharo.com/unified-test-documentation/dasharo-security/200-tpm-support/)
- [UEFI Secure Boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [Boot logo customization support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/328-logo-customization-functionality/)
- [USB boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31N-usb-boot/)
- [NVMe boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/312-nvme-support/)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [Network boot](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/315b-netboot-utilities/)
- [Windows 11 booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31A-windows-booting/)
- [Ubuntu LTS booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support/)
- [Serial port console redirection](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31G-ec-and-superio/#sio004001-serial-port-in-firmware)
- [Vboot Verified Boot](https://docs.dasharo.com/guides/vboot-signing/)
- [BIOS flash protection for Vboot recovery region](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20J-bios-lock-support/)
- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
- [SMM BIOS write protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Network stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#networking-options)

### Known issues

- [Unexpected error in dmesg](https://github.com/Dasharo/dasharo-issues/issues/1187)
- [Protectli logo doesn't show on small displays](https://github.com/Dasharo/dasharo-issues/issues/1541/)
- [Time window for boot/setup menu too short when skipping recovery popup](https://github.com/Dasharo/dasharo-issues/issues/1539)
- [Wake on LAN disabled by default on enp2s0 on VP2440](https://github.com/Dasharo/dasharo-issues/issues/1503)
- [Long booting time on Protectli VP2440](https://github.com/Dasharo/dasharo-issues/issues/1502)
- [Wake from S3 does not work on VP2440](https://github.com/Dasharo/dasharo-issues/issues/1351)
- [No network connection in DTS when LTE module plugged](https://github.com/Dasharo/dasharo-issues/issues/1289)

### Binaries

[protectli_vp2440_v0.9.0.rom][protectli_vp2440_v0.9.0.rom_file]{.md-button}
[sha256][protectli_vp2440_v0.9.0.rom_hash]{.md-button}
[sha256.sig][protectli_vp2440_v0.9.0.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/dasharo-release-0.9.x-for-protectli-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.03 revision 6d163576](https://github.com/Dasharo/coreboot/tree/6d163576)
    + [License](https://github.com/Dasharo/coreboot/blob/6d163576/COPYING)
- [Dasharo EDKII fork based on edk2-stable202502 revision ac25544f](https://github.com/Dasharo/edk2/tree/ac25544f)
    + [License](https://github.com/Dasharo/edk2/blob/ac25544f/License.txt)
- [Dasharo iPXE fork based on 2025.03 revision 8b8a50a8](https://github.com/Dasharo/ipxe/tree/8b8a50a8)
    + [License](https://github.com/Dasharo/ipxe/blob/8b8a50a8/COPYING.GPLv2)
- [vboot based on f1f70f46dc revision f1f70f46](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/LICENSE)
- [Intel Management Engine version v16.50.15.1515](https://github.com/Dasharo/dasharo-blobs/blob/52647f9c/protectli/vault_adl_n/vp2440/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/52647f9c/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/52647f9c/protectli/vault_adl_n/vp2440/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/52647f9c/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version IoT ADL-N MR6 (6023_00)](https://github.com/intel/FSP/commits/86c91116/AlderLakeFspBinPkg/IoT/AlderLakeN)
    + [License](https://github.com/intel/FSP/blob/86c91116/FSP_License.pdf)
- [Intel microcode version ADL-N N0 0x1d 06/12/2024](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20250812/intel-ucode/06-be-00)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20250812/license)

[protectli_vp2440_v0.9.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adln_vp2440/uefi/v0.9.0/protectli_vp2440_v0.9.0.rom
[protectli_vp2440_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adln_vp2440/uefi/v0.9.0/protectli_vp2440_v0.9.0.rom.sha256
[protectli_vp2440_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adln_vp2440/uefi/v0.9.0/protectli_vp2440_v0.9.0.rom.sha256.sig
