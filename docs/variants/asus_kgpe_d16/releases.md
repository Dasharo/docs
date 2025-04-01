# Release Notes

Following Release Notes describe status of Open Source Firmware development for
ASUS KGPE-D16.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

Feel free to contact us on our [Matrix Dasharo space](https://matrix.to/#/#dasharo:matrix.org).

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1rsJECHmYrpkPSByTyt7jmMuQnExE20zW7Zk6c8oMk6E/edit?usp=sharing).

## v0.4.0 - 2022-09-12

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1rsJECHmYrpkPSByTyt7jmMuQnExE20zW7Zk6c8oMk6E/edit#gid=0).

### Changed

- ACPI cleanup
- Added missing PCI bridge initialization

### Fixed

- [KGPE-D16 can not boot with a GPU connected](https://github.com/Dasharo/dasharo-issues/issues/48)
- [Configs for platforms without TPM](https://github.com/Dasharo/dasharo-issues/issues/62)
- [Bugs in DQS timing (kudos to Mike Rothfuss)](https://github.com/Dasharo/coreboot/pull/116)

### Known issues

- [Booting from recovery doesn't work](https://github.com/Dasharo/dasharo-issues/issues/66)
- [Fan controller gets stuck at 100%](https://github.com/Dasharo/dasharo-issues/issues/169)
- [FreeBSD serial output is broken](https://github.com/Dasharo/dasharo-issues/issues/170)
- [Linux kernel panic on booting USB media](https://github.com/Dasharo/dasharo-issues/issues/171)
- [Builds are not reproducible](https://github.com/Dasharo/dasharo-issues/issues/189)

### Binaries

[asus_kgpe-d16_v0.4.0_16M_vboot_notpm.rom][asus_kgpe-d16_v0.4.0_16M_vboot_notpm.rom_file]{.md-button}
[sha256][asus_kgpe-d16_v0.4.0_16M_vboot_notpm.rom_hash]{.md-button}
[sha256.sig][asus_kgpe-d16_v0.4.0_16M_vboot_notpm.rom_sig]{.md-button}

[asus_kgpe-d16_v0.4.0_16M_vboot_tpm12.rom][asus_kgpe-d16_v0.4.0_16M_vboot_tpm12.rom_file]{.md-button}
[sha256][asus_kgpe-d16_v0.4.0_16M_vboot_tpm12.rom_hash]{.md-button}
[sha256.sig][asus_kgpe-d16_v0.4.0_16M_vboot_tpm12.rom_sig]{.md-button}

[asus_kgpe-d16_v0.4.0_16M_vboot_tpm2.rom][asus_kgpe-d16_v0.4.0_16M_vboot_tpm2.rom_file]{.md-button}
[sha256][asus_kgpe-d16_v0.4.0_16M_vboot_tpm2.rom_hash]{.md-button}
[sha256.sig][asus_kgpe-d16_v0.4.0_16M_vboot_tpm2.rom_sig]{.md-button}

[asus_kgpe-d16_v0.4.0_8M_vboot_notpm.rom][asus_kgpe-d16_v0.4.0_8M_vboot_notpm.rom_file]{.md-button}
[sha256][asus_kgpe-d16_v0.4.0_8M_vboot_notpm.rom_hash]{.md-button}
[sha256.sig][asus_kgpe-d16_v0.4.0_8M_vboot_notpm.rom_sig]{.md-button}

[asus_kgpe-d16_v0.4.0_8M_vboot_tpm12.rom][asus_kgpe-d16_v0.4.0_8M_vboot_tpm12.rom_file]{.md-button}
[sha256][asus_kgpe-d16_v0.4.0_8M_vboot_tpm12.rom_hash]{.md-button}
[sha256.sig][asus_kgpe-d16_v0.4.0_8M_vboot_tpm12.rom_sig]{.md-button}

[asus_kgpe-d16_v0.4.0_8M_vboot_tpm2.rom][asus_kgpe-d16_v0.4.0_8M_vboot_tpm2.rom_file]{.md-button}
[sha256][asus_kgpe-d16_v0.4.0_8M_vboot_tpm2.rom_hash]{.md-button}
[sha256.sig][asus_kgpe-d16_v0.4.0_8M_vboot_tpm2.rom_sig]{.md-button}

[asus_kgpe-d16_v0.4.0_vboot_notpm.rom][asus_kgpe-d16_v0.4.0_vboot_notpm.rom_file]{.md-button}
[sha256][asus_kgpe-d16_v0.4.0_vboot_notpm.rom_hash]{.md-button}
[sha256.sig][asus_kgpe-d16_v0.4.0_vboot_notpm.rom_sig]{.md-button}

[asus_kgpe-d16_v0.4.0_vboot_tpm12.rom][asus_kgpe-d16_v0.4.0_vboot_tpm12.rom_file]{.md-button}
[sha256][asus_kgpe-d16_v0.4.0_vboot_tpm12.rom_hash]{.md-button}
[sha256.sig][asus_kgpe-d16_v0.4.0_vboot_tpm12.rom_sig]{.md-button}

[asus_kgpe-d16_v0.4.0_vboot_tpm2.rom][asus_kgpe-d16_v0.4.0_vboot_tpm2.rom_file]{.md-button}
[sha256][asus_kgpe-d16_v0.4.0_vboot_tpm2.rom_hash]{.md-button}
[sha256.sig][asus_kgpe-d16_v0.4.0_vboot_tpm2.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/asus_kgpe-d16/asus-kgpe-d16-dasharo-release-v0.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 03aef28f1613 revision cef95aaa](https://github.com/Dasharo/coreboot/tree/cef95aaa)
- [SeaBIOS based on rel-1.14.0 revision 155821a1](https://github.com/Dasharo/SeaBIOS/tree/155821a1)

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

[asus_kgpe-d16_v0.3.0_2M_vboot_TPM1.2.rom][v0.3.0_2m_tpm12_rom]{ .md-button }
[sha256][v0.3.0_2m_tpm12_sha]{ .md-button }
[sha256.sig][v0.3.0_2m_tpm12_sig]{ .md-button }

[v0.3.0_2m_tpm12_rom]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_2M_vboot_TPM1.2.rom
[v0.3.0_2m_tpm12_sha]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_2M_vboot_TPM1.2.rom.sha256
[v0.3.0_2m_tpm12_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_2M_vboot_TPM1.2.rom.sha256.sig

- 2MB vboot TPM 2.0

[asus_kgpe-d16_v0.3.0_2M_vboot_TPM2.0.rom][v0.3.0_2m_tpm20_rom]{ .md-button }
[sha256][v0.3.0_2m_tpm20_sha]{ .md-button }
[sha256.sig][v0.3.0_2m_tpm20_sig]{ .md-button }

[v0.3.0_2m_tpm20_rom]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_2M_vboot_TPM2.0.rom
[v0.3.0_2m_tpm20_sha]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_2M_vboot_TPM2.0.rom.sha256
[v0.3.0_2m_tpm20_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_2M_vboot_TPM2.0.rom.sha256.sig

- 8MB vboot TPM 1.2

[asus_kgpe-d16_v0.3.0_8M_vboot_TPM1.2.rom][v0.3.0_8m_tpm12_rom]{ .md-button }
[sha256][v0.3.0_8m_tpm12_sha]{ .md-button }
[sha256.sig][v0.3.0_8m_tpm12_sig]{ .md-button }

[v0.3.0_8m_tpm12_rom]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_8M_vboot_TPM1.2.rom
[v0.3.0_8m_tpm12_sha]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_8M_vboot_TPM1.2.rom.sha256
[v0.3.0_8m_tpm12_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_8M_vboot_TPM1.2.rom.sha256.sig

- 8MB vboot TPM 2.0

[asus_kgpe-d16_v0.3.0_8M_vboot_TPM2.0.rom][v0.3.0_8m_tpm20_rom]{ .md-button }
[sha256][v0.3.0_8m_tpm20_sha]{ .md-button }
[sha256.sig][v0.3.0_8m_tpm20_sig]{ .md-button }

[v0.3.0_8m_tpm20_rom]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_8M_vboot_TPM2.0.rom
[v0.3.0_8m_tpm20_sha]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_8M_vboot_TPM2.0.rom.sha256
[v0.3.0_8m_tpm20_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_8M_vboot_TPM2.0.rom.sha256.sig

- 16MB vboot TPM 1.2

[asus_kgpe-d16_v0.3.0_16M_vboot_TPM1.2.rom][v0.3.0_16m_tpm12_rom]{ .md-button }
[sha256][v0.3.0_16m_tpm12_sha]{ .md-button }
[sha256.sig][v0.3.0_16m_tpm12_sig]{ .md-button }

[v0.3.0_16m_tpm12_rom]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_16M_vboot_TPM1.2.rom
[v0.3.0_16m_tpm12_sha]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_16M_vboot_TPM1.2.rom.sha256
[v0.3.0_16m_tpm12_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_16M_vboot_TPM1.2.rom.sha256.sig

- 16MB vboot TPM 2.0

[asus_kgpe-d16_v0.3.0_16M_vboot_TPM2.0.rom][v0.3.0_16m_tpm20_rom]{ .md-button }
[sha256][v0.3.0_16m_tpm20_sha]{ .md-button }
[sha256.sig][v0.3.0_16m_tpm20_sig]{ .md-button }

[v0.3.0_16m_tpm20_rom]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_16M_vboot_TPM2.0.rom
[v0.3.0_16m_tpm20_sha]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_16M_vboot_TPM2.0.rom.sha256
[v0.3.0_16m_tpm20_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.3.0_16M_vboot_TPM2.0.rom.sha256.sig

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/asus_kgpe-d16/asus-kgpe-d16-dasharo-release-v0.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 4.14 revision 67190bf](https://github.com/Dasharo/coreboot/commit/67190bf)
- [SeaBIOS based on rel-1.14.0 revision 155821a1](https://github.com/coreboot/seabios/commit/155821a1)
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

[asus_kgpe-d16_v0.2.0_2M.rom][v0.2.0_2m_rom]{ .md-button }
[sha256][v0.2.0_2m_sha]{ .md-button }
[sha256.sig][v0.2.0_2m_sig]{ .md-button }

[v0.2.0_2m_rom]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_2M.rom
[v0.2.0_2m_sha]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_2M.rom.sha256
[v0.2.0_2m_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_2M.rom.sha256.sig

- 8MB target

[asus_kgpe-d16_v0.2.0_8M.rom][v0.2.0_8m_rom]{ .md-button }
[sha256][v0.2.0_8m_sha]{ .md-button }
[sha256.sig][v0.2.0_8m_sig]{ .md-button }

[v0.2.0_8m_rom]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_8M.rom
[v0.2.0_8m_sha]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_8M.rom.sha256
[v0.2.0_8m_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_8M.rom.sha256.sig

- 16MB target

[asus_kgpe-d16_v0.2.0_16M.rom][v0.2.0_16m_rom]{ .md-button }
[sha256][v0.2.0_16m_sha]{ .md-button }
[sha256.sig][v0.2.0_16m_sig]{ .md-button }

[v0.2.0_16m_rom]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_16M.rom
[v0.2.0_16m_sha]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_16M.rom.sha256
[v0.2.0_16m_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.2.0_16M.rom.sha256.sig

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/asus_kgpe-d16/asus-kgpe-d16-dasharo-release-v0.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 4.14 revision 63b7cbc1](https://github.com/Dasharo/coreboot/commit/63b7cbc1)
- [SeaBIOS based on rel-1.14.0 revision 155821a1](https://github.com/coreboot/seabios/commit/155821a1)
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

[asus_kgpe-d16_v0.1.0.rom][v0.1.0_rom]{ .md-button }

[asus_kgpe-d16_v0.1.0.rom.sha256][v0.1.0_sha]{ .md-button }

[asus_kgpe-d16_v0.1.0.rom.sha256.sig][v0.1.0_sig]{ .md-button }

[v0.1.0_rom]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.1.0.rom
[v0.1.0_sha]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.1.0.rom.sha256
[v0.1.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/asus_kgpe-d16_v0.1.0.rom.sha256.sig

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/asus_kgpe-d16/asus-kgpe-d16-dasharo-release-v0.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 03aef28 revision e6af2206](https://github.com/Dasharo/coreboot/tree/e6af2206)

[asus_kgpe-d16_v0.4.0_16M_vboot_notpm.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_16M_vboot_notpm.rom
[asus_kgpe-d16_v0.4.0_16M_vboot_notpm.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_16M_vboot_notpm.rom.sha256
[asus_kgpe-d16_v0.4.0_16M_vboot_notpm.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_16M_vboot_notpm.rom.sha256.sig
[asus_kgpe-d16_v0.4.0_16M_vboot_tpm12.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_16M_vboot_tpm12.rom
[asus_kgpe-d16_v0.4.0_16M_vboot_tpm12.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_16M_vboot_tpm12.rom.sha256
[asus_kgpe-d16_v0.4.0_16M_vboot_tpm12.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_16M_vboot_tpm12.rom.sha256.sig
[asus_kgpe-d16_v0.4.0_16M_vboot_tpm2.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_16M_vboot_tpm2.rom
[asus_kgpe-d16_v0.4.0_16M_vboot_tpm2.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_16M_vboot_tpm2.rom.sha256
[asus_kgpe-d16_v0.4.0_16M_vboot_tpm2.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_16M_vboot_tpm2.rom.sha256.sig
[asus_kgpe-d16_v0.4.0_8M_vboot_notpm.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_8M_vboot_notpm.rom
[asus_kgpe-d16_v0.4.0_8M_vboot_notpm.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_8M_vboot_notpm.rom.sha256
[asus_kgpe-d16_v0.4.0_8M_vboot_notpm.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_8M_vboot_notpm.rom.sha256.sig
[asus_kgpe-d16_v0.4.0_8M_vboot_tpm12.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_8M_vboot_tpm12.rom
[asus_kgpe-d16_v0.4.0_8M_vboot_tpm12.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_8M_vboot_tpm12.rom.sha256
[asus_kgpe-d16_v0.4.0_8M_vboot_tpm12.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_8M_vboot_tpm12.rom.sha256.sig
[asus_kgpe-d16_v0.4.0_8M_vboot_tpm2.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_8M_vboot_tpm2.rom
[asus_kgpe-d16_v0.4.0_8M_vboot_tpm2.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_8M_vboot_tpm2.rom.sha256
[asus_kgpe-d16_v0.4.0_8M_vboot_tpm2.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_8M_vboot_tpm2.rom.sha256.sig
[asus_kgpe-d16_v0.4.0_vboot_notpm.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_vboot_notpm.rom
[asus_kgpe-d16_v0.4.0_vboot_notpm.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_vboot_notpm.rom.sha256
[asus_kgpe-d16_v0.4.0_vboot_notpm.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_vboot_notpm.rom.sha256.sig
[asus_kgpe-d16_v0.4.0_vboot_tpm12.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_vboot_tpm12.rom
[asus_kgpe-d16_v0.4.0_vboot_tpm12.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_vboot_tpm12.rom.sha256
[asus_kgpe-d16_v0.4.0_vboot_tpm12.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_vboot_tpm12.rom.sha256.sig
[asus_kgpe-d16_v0.4.0_vboot_tpm2.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_vboot_tpm2.rom
[asus_kgpe-d16_v0.4.0_vboot_tpm2.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_vboot_tpm2.rom.sha256
[asus_kgpe-d16_v0.4.0_vboot_tpm2.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/asus_kgpe-d16/v0.4.0/asus_kgpe-d16_v0.4.0_vboot_tpm2.rom.sha256.sig
