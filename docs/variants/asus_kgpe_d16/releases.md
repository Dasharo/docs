# ASUS KGPE-D16 Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development for
ASUS KGPE-D16.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

[Subscribe to ASUS KGPE-D16 Dasharo Release Newsletter](https://newsletter.3mdeb.com/subscription/ozes4Jxuo){ .md-button .md-button--primary .center }

## v0.1.0 - 2021-11-10

### Added
  
- C bootblock support
- postcar stage and no CAR global migration support
- separated chipset and mainboard code
- put non-mainboard specific romstage initialization to northirdge
- support for relocatable ramstage with caching in CBMEM

### Binaries

[asus_kgpe-d16_v0.1.0.rom](https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.1.0.rom){ .md-button }

### SBOM (Software Bill of Materials):

- [coreboot based on 03aef28 revision e6af2206](https://github.com/Dasharo/coreboot/tree/e6af2206)
