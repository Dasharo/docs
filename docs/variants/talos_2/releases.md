# Raptor Computing Systems Talos II Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development for
Raptor Computing Systems Talos II

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

[Subscribe to Release Newsletter][newsletter]
{ .md-button .md-button--primary .center }

[newsletter]: https://newsletter.3mdeb.com/subscription/w2Y2G4Rrj

</center>

## v0.5.0 - 2022-04-12

### Changed

- Add FSI initialization and functions for accessing devices behind FSI bus
- Cache MVPD between stages
- Initialize and train XBus links
- Change SCOM API to be able to access second CPU
- Initialize PCIe, MCS, OCC and TOD for second CPU
- Switch to ELF payload, clean up Device Tree generation
- Various boot time optimizations

### Fixed

- [Only one CPU is started](https://github.com/Dasharo/dasharo-issues/issues/30)
- [SPDs are not exposed in sysfs automatically](https://github.com/Dasharo/dasharo-issues/issues/31)

### Known issues

- [Missing parts of Device Tree describing specific unit (VPD, serial numbers)](https://github.com/Dasharo/dasharo-issues/issues/32)
- [CBMEM can no longer be accessed from OS](https://github.com/Dasharo/dasharo-issues/issues/69)

### Binaries

[raptor-cs_talos-2_bootblock_v0.5.0.signed.ecc](https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.5.0/raptor-cs_talos-2_bootblock_v0.5.0.signed.ecc){ .md-button }
[sha256](https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.5.0/raptor-cs_talos-2_bootblock_v0.5.0.signed.ecc.sha256){ .md-button }
[sha256.sig](https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.5.0/raptor-cs_talos-2_bootblock_v0.5.0.signed.ecc.sha256.sig){ .md-button }

[raptor-cs_talos-2_coreboot_v0.5.0.rom.signed.ecc](https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.5.0/raptor-cs_talos-2_coreboot_v0.5.0.rom.signed.ecc){ .md-button }
[sha256](https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.5.0/raptor-cs_talos-2_coreboot_v0.5.0.rom.signed.ecc.sha256){ .md-button }
[sha256.sig](https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.5.0/raptor-cs_talos-2_coreboot_v0.5.0.rom.signed.ecc.sha256.sig){ .md-button }

Heads was not modified in this release, its binary from previous releases can be
used.

### SBOM (Software Bill of Materials):

- [coreboot based on 5621a1e revision c92383f9](https://github.com/Dasharo/coreboot/tree/c92383f9)
- [skiboot based on 04-16-2019 revision 98581863](https://git.raptorcs.com/git/talos-skiboot/tree/?id=98581863)

## v0.4.1 - 2022-01-10

### Changed

- Simplify memlayout
- Replace PPC_SHIFT with PPC_PLACE macro
- Change SPR numbers definitions to decimal
- Print signing output to terminal

### Fixed

- Watchdog timing out
- Sporadic signing failure due to the tools not being built
- Building with cross compiler other than powerpc64-linux-gnu-

### Known issues

- [Only one CPU is started](https://github.com/Dasharo/dasharo-issues/issues/30)
- [SPDs are not exposed in sysfs automatically](https://github.com/Dasharo/dasharo-issues/issues/31)
- [Missing parts of Device Tree describing specific unit (VPD, serial numbers)](https://github.com/Dasharo/dasharo-issues/issues/32)

### Binaries

[dasharo_talos_2_bootblock_v0.4.1.signed.ecc][v0.4.1_bootblock_rom]{ .md-button }
[sha256][v0.4.1_bootblock_sha]{ .md-button }
[sha256.sig][v0.4.1_bootblock_sig]{ .md-button }

[v0.4.1_bootblock_rom]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/dasharo_talos_2_bootblock_v0.4.1.signed.ecc
[v0.4.1_bootblock_sha]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/dasharo_talos_2_bootblock_v0.4.1.signed.ecc.sha256
[v0.4.1_bootblock_sig]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/dasharo_talos_2_bootblock_v0.4.1.signed.ecc.sha256.sig

[dasharo_talos_2_coreboot_v0.4.1.rom.signed.ecc][v0.4.1_rom]{ .md-button }
[sha256][v0.4.1_sha]{ .md-button }
[sha256.sig][v0.4.1_sig]{ .md-button }

[v0.4.1_rom]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/dasharo_talos_2_coreboot_v0.4.1.rom.signed.ecc
[v0.4.1_sha]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/dasharo_talos_2_coreboot_v0.4.1.rom.signed.ecc.sha256
[v0.4.1_sig]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/dasharo_talos_2_coreboot_v0.4.1.rom.signed.ecc.sha256.sig

[dasharo_talos_2_zImage_v0.4.1.bundled][v0.4.1_bundled_rom]{ .md-button }
[sha256][v0.4.1_bundled_sha]{ .md-button }
[sha256.sig][v0.4.1_bundled_sig]{ .md-button }

[v0.4.1_bundled_rom]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/dasharo_talos_2_zImage_v0.4.1.bundled
[v0.4.1_bundled_sha]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/dasharo_talos_2_zImage_v0.4.1.bundled.sha256
[v0.4.1_bundled_sig]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/dasharo_talos_2_zImage_v0.4.1.bundled.sha256.sig

### SBOM (Software Bill of Materials)

- [coreboot based on 5621a1e revision 13b58058](https://github.com/Dasharo/coreboot/commit/13b58058)
- [skiboot based on 04-16-2019 revision 98581863](https://git.raptorcs.com/git/talos-skiboot/tree/98581863)
- [heads based on 21e50681 revision 34c77951](https://git.raptorcs.com/git/talos-skiboot/commit/?id=9858186353f2203fe477f316964e03609d12fd1d)

## v0.4.0 - 2021-10-29

### Added

- OCC support
- XIVE support
- PCIe initialization
- IPMI block transfer interface
- Non-constant nodes in Device Tree are generated programmatically

### Known issues

- [Only one CPU is started](https://github.com/Dasharo/dasharo-issues/issues/30)
- [SPDs are not exposed in sysfs automatically](https://github.com/Dasharo/dasharo-issues/issues/31)
- [Missing parts of Device Tree describing specific unit (VPD, serial numbers)](https://github.com/Dasharo/dasharo-issues/issues/32)
- [Watchdog times out](https://github.com/Dasharo/dasharo-issues/issues/29)

### Binaries

[dasharo_talos_2_bootblock_v0.4.0.signed.ecc][v0.4.0_bootblock_rom]{ .md-button }
[sha256][v0.4.0_bootblock_sha]{ .md-button }
[sha256.sig][v0.4.0_bootblock_sig]{ .md-button }

[v0.4.0_bootblock_rom]: https://cloud.3mdeb.com/index.php/s/54MDtRgBNEmyKo6
[v0.4.0_bootblock_sha]: https://cloud.3mdeb.com/index.php/s/DwpWdgfZyD9StBW
[v0.4.0_bootblock_sig]: https://cloud.3mdeb.com/index.php/s/5xawXEissBZN6rT

[dasharo_talos_2_coreboot.rom.signed.ecc][v0.4.0_coreboot_rom]{ .md-button }
[sha256][v0.4.0_coreboot_sha]{ .md-button }
[sha256.sig][v0.4.0_coreboot_sig]{ .md-button }

[v0.4.0_coreboot_rom]: https://cloud.3mdeb.com/index.php/s/5Pbw5EtmNimrdrj
[v0.4.0_coreboot_sha]: https://cloud.3mdeb.com/index.php/s/TNcLAz3CZo4QzeD
[v0.4.0_coreboot_sig]: https://cloud.3mdeb.com/index.php/s/9Fr6Kn57mP2bbwS

[zImage_v0.4.0.bundled][v0.4.0_bundled_rom]{ .md-button }
[sha256][v0.4.0_bundled_sha]{ .md-button }
[sha256.sig][v0.4.0_bundled_sig]{ .md-button }

[v0.4.0_bundled_rom]: https://cloud.3mdeb.com/index.php/s/o5RE7oj4r9kFXS2
[v0.4.0_bundled_sha]: https://cloud.3mdeb.com/index.php/s/FgeHfa4LzcZK6Pj
[v0.4.0_bundled_sig]: https://cloud.3mdeb.com/index.php/s/awNSefJrN4d2tAD

### SBOM (Software Bill of Materials)

- [coreboot based on 5621a1e revision b535763b](https://github.com/Dasharo/coreboot/tree/raptor-cs_talos-2_v0.4.0)
- [skiboot based on 04-16-2019 revision 98581863](https://git.raptorcs.com/git/talos-skiboot/)
- [heads based on 21e50681 revision 34c77951](https://git.raptorcs.com/git/talos-skiboot/commit/?id=9858186353f2203fe477f316964e03609d12fd1d)
