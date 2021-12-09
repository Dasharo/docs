# ASUS KGPE-D16 Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development for
ASUS KGPE-D16.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

[Subscribe to ASUS KGPE-D16 Dasharo Release Newsletter](https://newsletter.3mdeb.com/subscription/ozes4Jxuo){ .md-button .md-button--primary .center }

## v0.2.0 - 2021-12-9

### Added
  
- coreboot resource allocator v4 support
- Nuvoton W83795 HW monitor driver
- [automatic fan control with W83795](fan-control.md)
- platform and silicon ramstage support
- 2MB, 8MB and 16MB SPI flash targets
- SeaBIOS, iPXE and nvramcui payloads

### Binaries

* 2MB target

[asus_kgpe-d16_v0.2.0_2M.rom](https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_2M.rom){ .md-button }
[sha256](https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_2M.rom.sha256){ .md-button }
[sha256.sig](https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_2M.rom.sha256.sig){ .md-button }

* 8MB target

[asus_kgpe-d16_v0.2.0_8M.rom ](https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_8M.rom){ .md-button }
[sha256](https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_8M.rom.sha256){ .md-button }
[sha256.sig](https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_8M.rom.sha256.sig){ .md-button }

* 16MB target

[asus_kgpe-d16_v0.2.0_16M.rom](https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_16M.rom){ .md-button }
[sha256](https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_16M.rom.sha256){ .md-button }
[sha256.sig](https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_16M.rom.sha256.sig){ .md-button }

### SBOM (Software Bill of Materials):

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

[asus_kgpe-d16_v0.1.0.rom](https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.1.0.rom){ .md-button }

[asus_kgpe-d16_v0.1.0.rom.sha256](https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.1.0.rom.sha256){ .md-button }

[asus_kgpe-d16_v0.1.0.rom.sha256.sig](https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.1.0.rom.sha256.sig){ .md-button }

### SBOM (Software Bill of Materials):

- [coreboot based on 03aef28 revision e6af2206](https://github.com/Dasharo/coreboot/tree/e6af2206)
