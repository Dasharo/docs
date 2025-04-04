# Release notes

Following Release Notes describe status of Open Source Firmware development for
Raptor Computing Systems Talos II

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("0f9f6d56-cc30-4caf-8087-bec92f1b9360",
"Subscribe to Release Newsletter") }}

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1KpmuPEkWOj3SieophUbgf7CF6mydliMsEDLtOFOrKn0/edit?usp=sharing).

## v0.7.0 - 2023-07-26

### Fixed

- [CPU appears to be stuck on initial frequency](https://github.com/Dasharo/dasharo-issues/issues/35)
- [No flashrom support](https://github.com/Dasharo/dasharo-issues/issues/190)
- [0.6 Release - Cannot boot if no TPM](https://github.com/Dasharo/dasharo-issues/issues/191)
- [OS-level access to CBMEM](https://github.com/Dasharo/dasharo-issues/issues/69)
- [TPM discovery and usage stability](https://github.com/Dasharo/dasharo-issues/issues/415)
- [Dual CPU setup - Second fan at full speed](https://github.com/Dasharo/dasharo-issues/issues/416)

### Known issues

- [Missing parts of Device Tree describing specific unit (VPD, serial numbers)](https://github.com/Dasharo/dasharo-issues/issues/32)
- [No DIMM temperatures reported](https://github.com/Dasharo/dasharo-issues/issues/446)

### Binaries

[raptor-cs_talos-2_bootblock_v0.7.0.signed.ecc][raptor-cs_talos-2_bootblock_v0.7.0.signed.ecc_file]{.md-button}
[sha256][raptor-cs_talos-2_bootblock_v0.7.0.signed.ecc_hash]{.md-button}
[sha256.sig][raptor-cs_talos-2_bootblock_v0.7.0.signed.ecc_sig]{.md-button}

[raptor-cs_talos-2_coreboot_v0.7.0.rom.signed.ecc][raptor-cs_talos-2_coreboot_v0.7.0.rom.signed.ecc_file]{.md-button}
[sha256][raptor-cs_talos-2_coreboot_v0.7.0.rom.signed.ecc_hash]{.md-button}
[sha256.sig][raptor-cs_talos-2_coreboot_v0.7.0.rom.signed.ecc_sig]{.md-button}

[raptor-cs_talos-2_zImage_v0.7.0.bundled][raptor-cs_talos-2_zImage_v0.7.0.bundled_file]{.md-button}
[sha256][raptor-cs_talos-2_zImage_v0.7.0.bundled_hash]{.md-button}
[sha256.sig][raptor-cs_talos-2_zImage_v0.7.0.bundled_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/insurgo/release-keys/insurgo-dasharo-trustworthy-computing-release-0.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 4ed0a830b14d6e1841eae0dd3c2e6539a8dcf0a8 revision fc47236e](https://github.com/Dasharo/coreboot/tree/fc47236e)
- [skiboot based on 9858186353f2203fe477f316964e03609d12fd1d revision 1b14dd0b](https://github.com/Dasharo/skiboot/tree/1b14dd0b)
- [heads based on edf200e7913c62975a424cfb9dbd579747d0665c revision edf200e7913c62975a424cfb9dbd579747d0665c](https://github.com/osresearch/heads/tree/edf200e7913c62975a424cfb9dbd579747d0665c)

[raptor-cs_talos-2_bootblock_v0.7.0.signed.ecc_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.7.0/raptor-cs_talos-2_bootblock_v0.7.0.signed.ecc
[raptor-cs_talos-2_bootblock_v0.7.0.signed.ecc_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.7.0/raptor-cs_talos-2_bootblock_v0.7.0.signed.ecc.sha256
[raptor-cs_talos-2_bootblock_v0.7.0.signed.ecc_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.7.0/raptor-cs_talos-2_bootblock_v0.7.0.signed.ecc.sha256.sig
[raptor-cs_talos-2_coreboot_v0.7.0.rom.signed.ecc_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.7.0/raptor-cs_talos-2_coreboot_v0.7.0.rom.signed.ecc
[raptor-cs_talos-2_coreboot_v0.7.0.rom.signed.ecc_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.7.0/raptor-cs_talos-2_coreboot_v0.7.0.rom.signed.ecc.sha256
[raptor-cs_talos-2_coreboot_v0.7.0.rom.signed.ecc_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.7.0/raptor-cs_talos-2_coreboot_v0.7.0.rom.signed.ecc.sha256.sig
[raptor-cs_talos-2_zImage_v0.7.0.bundled_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.7.0/raptor-cs_talos-2_zImage_v0.7.0.bundled
[raptor-cs_talos-2_zImage_v0.7.0.bundled_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.7.0/raptor-cs_talos-2_zImage_v0.7.0.bundled.sha256
[raptor-cs_talos-2_zImage_v0.7.0.bundled_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.7.0/raptor-cs_talos-2_zImage_v0.7.0.bundled.sha256.sig

## v0.6.0 - 2022-08-26

### Added

- Optional support for Infineon I2C TPM1 chips
- Initial support for measured boot

### Fixed

- [Heads console output only on BMC console, not VGA](https://github.com/Dasharo/dasharo-issues/issues/168)
- [Startup on a single CPU configuration](https://github.com/Dasharo/dasharo-issues/issues/80)
- Startup on a single CPU configuration and support for older CPUs
    (without WOF tables and with different frequencies)
- [CBMEM can no longer be accessed from OS](https://github.com/Dasharo/dasharo-issues/issues/69)

### Known issues

- [Missing parts of Device Tree describing specific unit (VPD, serial numbers)](https://github.com/Dasharo/dasharo-issues/issues/32)
- [CPU appears to be stuck on initial frequency](https://github.com/Dasharo/dasharo-issues/issues/35)

### Binaries

[raptor-cs_talos-2_zImage_v0.6.0.bundled][zImage_v0.6.0_file]{ .md-button }
[sha256][zImage_v0.6.0_hash]{ .md-button }
[sha256.sig][zImage_v0.6.0_sig]{ .md-button }

[raptor-cs_talos-2_coreboot_v0.6.0.rom.signed.ecc][cb_v0.6.0_file]{ .md-button }
[sha256][cb_v0.6.0_hash]{ .md-button }
[sha256.sig][cb_v0.6.0_sig]{ .md-button }

[raptor-cs_talos-2_bootblock_v0.6.0.signed.ecc][bb_v0.6.0_file]{ .md-button }
[sha256][bb_v0.6.0_hash]{ .md-button }
[sha256.sig][bb_v0.6.0_sig]{ .md-button }

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/insurgo/release-keys/insurgo-dasharo-trustworthy-computing-release-0.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 5621a1e revision 2207bbcc](https://github.com/Dasharo/coreboot/tree/2207bbcc)
- [skiboot based on 7f90b9cd revision fa060c2c](https://github.com/Dasharo/skiboot/tree/fa060c2c)
- [heads based on fdbd9b2 revision 66f0fce0870b729d](https://github.com/osresearch/heads/tree/66f0fce0870b729d)

[zImage_v0.6.0_file]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.6.0/raptor-cs_talos-2_zImage_v0.6.0.bundled
[zImage_v0.6.0_hash]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.6.0/raptor-cs_talos-2_zImage_v0.6.0.bundled.sha256
[zImage_v0.6.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.6.0/raptor-cs_talos-2_zImage_v0.6.0.bundled.sha256.sig
[cb_v0.6.0_file]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.6.0/raptor-cs_talos-2_coreboot_v0.6.0.rom.signed.ecc
[cb_v0.6.0_hash]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.6.0/raptor-cs_talos-2_coreboot_v0.6.0.rom.signed.ecc.sha256
[cb_v0.6.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.6.0/raptor-cs_talos-2_coreboot_v0.6.0.rom.signed.ecc.sha256.sig
[bb_v0.6.0_file]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.6.0/raptor-cs_talos-2_bootblock_v0.6.0.signed.ecc
[bb_v0.6.0_hash]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.6.0/raptor-cs_talos-2_bootblock_v0.6.0.signed.ecc.sha256
[bb_v0.6.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.6.0/raptor-cs_talos-2_bootblock_v0.6.0.signed.ecc.sha256.sig

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

[raptor-cs_talos-2_bootblock_v0.5.0.signed.ecc][v0.5.0_bb_rom]{ .md-button }
[sha256][v0.5.0_bb_sha]{ .md-button }
[sha256.sig][v0.5.0_bb_sig]{ .md-button }

[v0.5.0_bb_rom]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.5.0/raptor-cs_talos-2_bootblock_v0.5.0.signed.ecc
[v0.5.0_bb_sha]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.5.0/raptor-cs_talos-2_bootblock_v0.5.0.signed.ecc.sha256
[v0.5.0_bb_sig]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.5.0/raptor-cs_talos-2_bootblock_v0.5.0.signed.ecc.sha256.sig

[raptor-cs_talos-2_coreboot_v0.5.0.rom.signed.ecc][v0.5.0_rom]{ .md-button }
[sha256][v0.5.0_sha]{ .md-button }
[sha256.sig][v0.5.0_sig]{ .md-button }

[v0.5.0_rom]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.5.0/raptor-cs_talos-2_coreboot_v0.5.0.rom.signed.ecc
[v0.5.0_sha]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.5.0/raptor-cs_talos-2_coreboot_v0.5.0.rom.signed.ecc.sha256
[v0.5.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/raptor-cs_talos-2/v0.5.0/raptor-cs_talos-2_coreboot_v0.5.0.rom.signed.ecc.sha256.sig

Heads was not modified in this release, its binary from previous releases can be
used.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/insurgo/release-keys/insurgo-dasharo-trustworthy-computing-release-0.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 5621a1e revision c92383f9](https://github.com/Dasharo/coreboot/tree/c92383f9)
- [skiboot based on 04-16-2019 revision 98581863](https://git.raptorcs.com/git/talos-skiboot/tree/?id=9858186353f2203fe477f316964e03609d12fd1d)

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

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/insurgo/release-keys/insurgo-dasharo-trustworthy-computing-release-0.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 5621a1e revision 13b58058](https://github.com/Dasharo/coreboot/commit/13b58058)
- [skiboot based on 04-16-2019 revision 98581863](https://git.raptorcs.com/git/talos-skiboot/tree/?id=9858186353f2203fe477f316964e03609d12fd1d)
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

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/insurgo/release-keys/insurgo-dasharo-trustworthy-computing-release-0.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 5621a1e revision b535763b](https://github.com/Dasharo/coreboot/tree/raptor-cs_talos-2_v0.4.0)
- [skiboot based on 04-16-2019 revision 98581863](https://git.raptorcs.com/git/talos-skiboot/)
- [heads based on 21e50681 revision 34c77951](https://git.raptorcs.com/git/talos-skiboot/commit/?id=9858186353f2203fe477f316964e03609d12fd1d)
