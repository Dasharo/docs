# ASUS KGPE-D16 Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development for
ASUS KGPE-D16.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

[Subscribe to Release Newsletter][1]
{ .md-button .md-button--primary .center }

</center>

Feel free to contact us on our [Matrix Dasharo space](https://matrix.to/#/#dasharo:matrix.org).

## v0.3.0 - 2021-12-16

### Added

- [TPM support](tpm-mboot.md)
- vboot support (see how to sign and protect the image [here](spi-wp.md#setting-flash-protection-for-vboot))
- build targets for vboot with measured boot using TPM 1.2 and TPM 2.0

### Fixed

- cmos.layout being incorrectly mapped from RW CBFS during coreboot tables generation
- CC6 storage area being incorrectly included in cbmem top calculations
- ACPI DSDT LPC device name which caused TPM to be undetected by OS
- SPI controller driver sometimes dropping bytes sent/received through SPI FIFO

### Binaries

- 2MB vboot TPM 1.2

[asus_kgpe-d16_v0.3.0_2M_vboot_TPM1.2.rom][14]{ .md-button }
[sha256][15]{ .md-button }
[sha256.sig][16]{ .md-button }

- 2MB vboot TPM 2.0

[asus_kgpe-d16_v0.3.0_2M_vboot_TPM2.0.rom][17]{ .md-button }
[sha256][18]{ .md-button }
[sha256.sig][19]{ .md-button }

- 8MB vboot TPM 1.2

[asus_kgpe-d16_v0.3.0_8M_vboot_TPM1.2.rom][20]{ .md-button }
[sha256][21]{ .md-button }
[sha256.sig][22]{ .md-button }

- 8MB vboot TPM 2.0

[asus_kgpe-d16_v0.3.0_8M_vboot_TPM2.0.rom][23]{ .md-button }
[sha256][24]{ .md-button }
[sha256.sig][25]{ .md-button }

- 16MB vboot TPM 1.2

[asus_kgpe-d16_v0.3.0_16M_vboot_TPM1.2.rom][26]{ .md-button }
[sha256][27]{ .md-button }
[sha256.sig][28]{ .md-button }

- 16MB vboot TPM 2.0

[asus_kgpe-d16_v0.3.0_16M_vboot_TPM2.0.rom][29]{ .md-button }
[sha256][30]{ .md-button }
[sha256.sig][31]{ .md-button }

### SBOM (Software Bill of Materials)

- [coreboot based on 4.14 revision 67190bf](https://github.com/Dasharo/coreboot/commit/67190bf)
- [SeaBIOS based on rel-1.14.0 revision 155821a1](https://review.coreboot.org/plugins/gitiles/seabios/+/155821a1)
- [iPXE based on 2019.3 revision ebf2eaf5](https://github.com/ipxe/ipxe/commit/ebf2eaf5)
- [nvramcui based on 4.14 revision f1d1309f](https://github.com/Dasharo/coreboot/blob/f1d1309f/payloads/nvramcui/nvramcui.c)

## v0.2.0 - 2021-12-9

### Added

- coreboot resource allocator v4 support
- Nuvoton W83795 HW monitor driver
- [automatic fan control with W83795](fan-control.md)
- platform and silicon ramstage support
- 2MB, 8MB and 16MB SPI flash targets
- SeaBIOS, iPXE and nvramcui payloads

### Binaries

- 2MB target

[asus_kgpe-d16_v0.2.0_2M.rom][11]{ .md-button }
[sha256][12]{ .md-button }
[sha256.sig][13]{ .md-button }

- 8MB target

[asus_kgpe-d16_v0.2.0_8M.rom][8]{ .md-button }
[sha256][9]{ .md-button }
[sha256.sig][10]{ .md-button }

- 16MB target

[asus_kgpe-d16_v0.2.0_16M.rom][5]{ .md-button }
[sha256][6]{ .md-button }
[sha256.sig][7]{ .md-button }

### SBOM (Software Bill of Materials)

- [coreboot based on 4.14 revision 63b7cbc1](https://github.com/Dasharo/coreboot/commit/63b7cbc1)
- [SeaBIOS based on rel-1.14.0 revision 155821a1](https://review.coreboot.org/plugins/gitiles/seabios/+/155821a1)
- [iPXE based on 2019.3 revision ebf2eaf5](https://github.com/ipxe/ipxe/commit/ebf2eaf5)
- [nvramcui based on 4.14 revision 63b7cbc1](https://github.com/Dasharo/coreboot/blob/63b7cbc1/payloads/nvramcui/nvramcui.c)

## v0.1.0 - 2021-11-10

### Added

- C bootblock support
- postcar stage and no CAR global migration support
- separated chipset and mainboard code
- put non-mainboard specific romstage initialization to northirdge
- support for relocatable ramstage with caching in CBMEM

### Binaries

[asus_kgpe-d16_v0.1.0.rom][2]{ .md-button }

[asus_kgpe-d16_v0.1.0.rom.sha256][3]{ .md-button }

[asus_kgpe-d16_v0.1.0.rom.sha256.sig][4]{ .md-button }

### SBOM (Software Bill of Materials)

- [coreboot based on 03aef28 revision e6af2206](https://github.com/Dasharo/coreboot/tree/e6af2206)

[1]: https://newsletter.3mdeb.com/subscription/ozes4Jxuo
[2]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.1.0.rom
[3]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.1.0.rom.sha256
[4]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.1.0.rom.sha256.sig
[5]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_16M.rom
[6]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_16M.rom.sha256
[7]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_16M.rom.sha256.sig
[8]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_8M.rom
[9]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_8M.rom.sha256
[10]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_8M.rom.sha256.sig
[11]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_2M.rom
[12]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_2M.rom.sha256
[13]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_2M.rom.sha256.sig
[14]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_2M_vboot_TPM1.2.rom
[15]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_2M_vboot_TPM1.2.rom.sha256
[16]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_2M_vboot_TPM1.2.rom.sha256.sig
[17]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_2M_vboot_TPM2.0.rom
[18]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_2M_vboot_TPM2.0.rom.sha256
[19]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_2M_vboot_TPM2.0.rom.sha256.sig
[20]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_8M_vboot_TPM1.2.rom
[21]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_8M_vboot_TPM1.2.rom.sha256
[22]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_8M_vboot_TPM1.2.rom.sha256.sig
[23]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_8M_vboot_TPM2.0.rom
[24]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_8M_vboot_TPM2.0.rom.sha256
[25]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_8M_vboot_TPM2.0.rom.sha256.sig
[26]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_16M_vboot_TPM1.2.rom
[27]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_16M_vboot_TPM1.2.rom.sha256
[28]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_16M_vboot_TPM1.2.rom.sha256.sig
[29]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_16M_vboot_TPM2.0.rom
[30]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_16M_vboot_TPM2.0.rom.sha256
[31]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_16M_vboot_TPM2.0.rom.sha256.sig
