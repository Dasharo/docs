# Protectli VP6630/VP6650/VP6670 Dasharo Release Notes

Following Release Notes describe status of open-source firmware development
for Protectli VP6630/VP6650/VP6670

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

[Subscribe to Protectli Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

</center>

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

- [Display Port has trouble working with certain monitors](https://github.com/Dasharo/dasharo-issues/issues/1015)
- [STB002.001 encounters unlisted errors](https://github.com/Dasharo/dasharo-issues/issues/1013)

### Binaries

[protectli_vp66xx_v0.9.0.rom][protectli_vp66xx_v0.9.0.rom_file]{.md-button}
[sha256][protectli_vp66xx_v0.9.0.rom_hash]{.md-button}
[sha256.sig][protectli_vp66xx_v0.9.0.rom_sig]{.md-button}

[protectli_vp66xx_v0.9.0_dev_signed.rom][protectli_vp66xx_v0.9.0_dev_signed.rom_file]{.md-button}
[sha256][protectli_vp66xx_v0.9.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][protectli_vp66xx_v0.9.0_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
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

[newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
[protectli_vp66xx_v0.9.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.0/protectli_vp66xx_v0.9.0.rom
[protectli_vp66xx_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.0/protectli_vp66xx_v0.9.0.rom.sha256
[protectli_vp66xx_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.0/protectli_vp66xx_v0.9.0.rom.sha256.sig
[protectli_vp66xx_v0.9.0_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.0/protectli_vp66xx_v0.9.0_dev_signed.rom
[protectli_vp66xx_v0.9.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.0/protectli_vp66xx_v0.9.0_dev_signed.rom.sha256
[protectli_vp66xx_v0.9.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_adl/v0.9.0/protectli_vp66xx_v0.9.0_dev_signed.rom.sha256.sig
