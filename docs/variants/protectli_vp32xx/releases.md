# Protectli VP32xx Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
Protectli VP32xx.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("49abc4a2-0807-4720-aef2-b150ef701b30",
"Subscribe to Protectli Dasharo Release Newsletter") }}

</center>

## v0.9.0 - 2025-07-14

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/VP32xx).

### Added

- Initial support for Protectli Alder Lake N devices VP32xx
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

- [M2T4SAT-AS1 M.2 Mini SAS SFF-8087 adapter increases FW boot time by aprox. 20 seconds](https://github.com/Dasharo/dasharo-issues/issues/1286)
- [ESXI TPM driver fails to load on VP3210](https://github.com/Dasharo/dasharo-issues/issues/1231)
- [Unexpected error in dmesg on VP3210](https://github.com/Dasharo/dasharo-issues/issues/1187)
- [STB002.001 encounters unlisted error](https://github.com/Dasharo/dasharo-issues/issues/1013)

### Binaries

[protectli_vp32xx_v0.9.0.rom][protectli_vp32xx_v0.9.0.rom_file]{.md-button}
[sha256][protectli_vp32xx_v0.9.0.rom_hash]{.md-button}
[sha256.sig][protectli_vp32xx_v0.9.0.rom_sig]{.md-button}

[protectli_vp32xx_v0.9.0_dev_signed.rom][protectli_vp32xx_v0.9.0_dev_signed.rom_file]{.md-button}
[sha256][protectli_vp32xx_v0.9.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][protectli_vp32xx_v0.9.0_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/dasharo-open-source-firmware-engineering-release-signing-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 24.02 revision 92c369e2](https://github.com/Dasharo/coreboot/tree/92c369e2)
    + [License](https://github.com/Dasharo/coreboot/blob/92c369e2/COPYING)
- [Dasharo EDKII fork based on edk2-stable202405 revision c2de870a](https://github.com/Dasharo/edk2/tree/c2de870a)
    + [License](https://github.com/Dasharo/edk2/blob/c2de870a/License.txt)
- [Dasharo iPXE fork based on 2024.07 revision 63ed3e35](https://github.com/Dasharo/ipxe/tree/63ed3e35)
    + [License](https://github.com/Dasharo/ipxe/blob/63ed3e35/COPYING.GPLv2)
- [Intel Management Engine version v16.50.12.1453](https://github.com/Dasharo/dasharo-blobs/blob/5eb84421/protectli/vault_adl_n/vp32xx/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/5eb84421/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/5eb84421/protectli/vault_adl_n/vp32xx/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/5eb84421/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version Iot ADL-N MR5 (5132_00)](https://github.com/intel/FSP/commits/86c91116/AlderLakeFspBinPkg/IoT/AlderLakeN)
    + [License](https://github.com/intel/FSP/blob/86c91116/FSP_License.pdf)
- [Intel microcode version ADL N0 0x15](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240312/intel-ucode/06-be-00)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240312/license)

[newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
[protectli_vp32xx_v0.9.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adln/v0.9.0/protectli_vp32xx_v0.9.0.rom
[protectli_vp32xx_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adln/v0.9.0/protectli_vp32xx_v0.9.0.rom.sha256
[protectli_vp32xx_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adln/v0.9.0/protectli_vp32xx_v0.9.0.rom.sha256.sig
[protectli_vp32xx_v0.9.0_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adln/v0.9.0/protectli_vp32xx_v0.9.0_dev_signed.rom
[protectli_vp32xx_v0.9.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adln/v0.9.0/protectli_vp32xx_v0.9.0_dev_signed.rom.sha256
[protectli_vp32xx_v0.9.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adln/v0.9.0/protectli_vp32xx_v0.9.0_dev_signed.rom.sha256.sig
