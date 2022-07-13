# Protectli VP46xx Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development for
Protectli VP46xx

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>
[Subscribe to Protectli VP46xx Dasharo Release Newsletter]
[newsletter]{.md-button .md-button--primary .center}
</center>

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit?usp=sharing).

## v1.0.16 - 2022-07-13

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/19YnBLxHw0mae-SQ2xl6BgPeims9hH_oVGwyF70pj9EY/edit#gid=1614315669).

### Added

- [Vboot Verified Boot](https://docs.dasharo.com/common-coreboot-docs/vboot_signing/)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [Vboot recovery notification in UEFI Payload](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)
- [UEFI Shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
- [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [Intel ME soft disable](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20F-me-neuter/)
- [BIOS flash protection for Vboot recovery region](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20J-bios-lock-support/)

### Changed

- [Changed supported CPUs to Comet Lake stepping 2](https://github.com/intel/FSP/tree/master/CometLakeFspBinPkg#comet-lake-binary-differences)

### Fixed

- [i225 network controller initialization takes too much time](https://github.com/Dasharo/dasharo-issues/issues/65)
- [CVE-2022-29264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-29264)

### Binaries

[protectli_vault_cml_v1.0.16.rom][v1.0.16_rom]{.md-button}
[sha256][v1.0.16_hash]{.md-button}
[sha256.sig][v1.0.16_sig]{.md-button}

See how to verify signatures on [this video](https://asciinema.org/a/388861)

### SBOM (Software Bill of Materials):

- [coreboot based on 4.16 revision dfaaf44d](https://github.com/Dasharo/coreboot/tree/dfaaf44d)
- [edk2 based on 7f90b9cd revision 5345a611](https://github.com/Dasharo/edk2/tree/5345a611)

## v1.0.13 - 2022-03-22

### Added

- UEFI boot support
- i225 network controller network boot support
- Customized boot menu keys
- Customized setup menu keys
- Configurable boot order
- Configurable boot options

### Changed

- ME version to 14.0.47.1558

### Known issues

- [i225 network controller initialization takes too much time](https://github.com/Dasharo/dasharo-issues/issues/65)

### Binaries

[protectli_vault_cml_v1.0.13.rom][v1.0.13_rom]{.md-button}
[sha256][v1.0.13_hash]{.md-button}
[sha256.sig][v1.0.13_sig]{.md-button}

See how to verify signatures on [asciinema](TBD)

### SBOM (Software Bill of Materials)

- [coreboot based on 4.16 revision 546e1c86](https://github.com/Dasharo/coreboot/tree/546e1c86)
- [edk2 based on 7f90b9cd revision 7f90b9cd](https://github.com/Dasharo/edk2/tree/7f90b9cd)

[newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
[v1.0.16_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.16.rom
[v1.0.16_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.16.rom.sha256
[v1.0.16_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.16.rom.sha256.sig
[v1.0.13_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.13.rom
[v1.0.13_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.13.rom.sha256
[v1.0.13_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.13.rom.sha256.sig
