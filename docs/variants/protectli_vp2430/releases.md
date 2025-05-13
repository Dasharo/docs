# Protectli VP2430 Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
Protectli VP2430.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

[Subscribe to Protectli VP2430 Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

</center>

## v0.9.0 - 2025-05-08

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/VP2430/v0.9.0-results.csv).

### Added

- Initial support for Protectli Alder Lake N devices (Vault Pro 2430)
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
- [Intel ME HAP disable](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20F-me-neuter/)
- [BIOS flash protection for Vboot recovery region](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20J-bios-lock-support/)
- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
- [SMM BIOS write protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Network stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#networking-options)

### Known issues

- [Unexpected error in dmesg](https://github.com/Dasharo/dasharo-issues/issues/1187)

### Binaries

[protectli_vp2430_v0.9.0.rom][protectli_vp2430_v0.9.0.rom_file]{.md-button}
[sha256][protectli_vp2430_v0.9.0.rom_hash]{.md-button}
[sha256.sig][protectli_vp2430_v0.9.0.rom_sig]{.md-button}

[protectli_vp2430_v0.9.0_dev_signed.rom][protectli_vp2430_v0.9.0_dev_signed.rom_file]{.md-button}
[sha256][protectli_vp2430_v0.9.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][protectli_vp2430_v0.9.0_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/dasharo-open-source-firmware-engineering-release-signing-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 24.02 revision feb2693f](https://github.com/Dasharo/coreboot/tree/feb2693f)
    + [License](https://github.com/Dasharo/coreboot/blob/feb2693f/COPYING)
- [Dasharo EDKII fork based on edk2-stable202405 revision c2de870a](https://github.com/Dasharo/edk2/tree/c2de870a)
    + [License](https://github.com/Dasharo/edk2/blob/c2de870a/License.txt)
- [Dasharo iPXE fork based on 2024.07 revision 63ed3e35](https://github.com/Dasharo/ipxe/tree/63ed3e35)
    + [License](https://github.com/Dasharo/ipxe/blob/63ed3e35/COPYING.GPLv2)
- [Intel Management Engine version v16.50.15.1515-v0.1](https://github.com/Dasharo/dasharo-blobs/blob/79be2c81/protectli/vault_adl_n/vp2430/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/79be2c81/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.2](https://github.com/Dasharo/dasharo-blobs/blob/79be2c81/protectli/vault_adl_n/vp2430/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/79be2c81/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version 0C.02.89.30-v0.1](https://github.com/intel/FSP/commits/86c91116/AlderLakeFspBinPkg/IoT/AlderLakeN)
    + [License](https://github.com/intel/FSP/blob/86c91116/FSP_License.pdf)
- [Intel microcode version ADL N0 0x15](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240312/intel-ucode/06-be-00)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240312/license)

[newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
[protectli_vp2430_v0.9.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vp2430/v0.9.0/protectli_vp2430_v0.9.0.rom
[protectli_vp2430_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vp2430/v0.9.0/protectli_vp2430_v0.9.0.rom.sha256
[protectli_vp2430_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vp2430/v0.9.0/protectli_vp2430_v0.9.0.rom.sha256.sig
[protectli_vp2430_v0.9.0_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vp2430/v0.9.0/protectli_vp2430_v0.9.0_dev_signed.rom
[protectli_vp2430_v0.9.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vp2430/v0.9.0/protectli_vp2430_v0.9.0_dev_signed.rom.sha256
[protectli_vp2430_v0.9.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vp2430/v0.9.0/protectli_vp2430_v0.9.0_dev_signed.rom.sha256.sig
