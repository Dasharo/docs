# Release Notes

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

## v1.0.18 - 2022-11-16

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit#gid=1613384145).

### Added

- Support for VP4650 and VP4670 platforms
- Platform will beep 12 times and blink HDD led on critical firmware errors

### Changed

- Disabled Intel PTT (fTPM)
- [Removed workaround for graphics power management as the issue no longer reproduces on newer revision of the hardware](https://github.com/Dasharo/dasharo-issues/issues/26)
- Binaries are built with coreboot-sdk 2021-09-23_b0d87f753c (was 0ad5fbd48d)
- Open-source graphics initialization with libgfxinit instead of proprietary and
  closed FSP GOP driver

### Binaries

[protectli_vp4630_vp4650_v1.0.18.rom][protectli_vp4630_vp4650_v1.0.18.rom_file]{.md-button}
[sha256][protectli_vp4630_vp4650_v1.0.18.rom_hash]{.md-button}
[sha256.sig][protectli_vp4630_vp4650_v1.0.18.rom_sig]{.md-button}

[protectli_vp4670_v1.0.18.rom][protectli_vp4670_v1.0.18.rom_file]{.md-button}
[sha256][protectli_vp4670_v1.0.18.rom_hash]{.md-button}
[sha256.sig][protectli_vp4670_v1.0.18.rom_sig]{.md-button}

See how to verify signatures on [this video](https://asciinema.org/a/388861)

### SBOM (Software Bill of Materials)

- [coreboot based on c6ee1509da revision ed9f6fe0](https://github.com/Dasharo/coreboot/tree/ed9f6fe0)
- [edk2 based on 7f90b9cd revision e31b7a71](https://github.com/Dasharo/edk2/tree/e31b7a71)

[protectli_vp4630_vp4650_v1.0.18.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.18/protectli_vp4630_vp4650_v1.0.18.rom
[protectli_vp4630_vp4650_v1.0.18.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.18/protectli_vp4630_vp4650_v1.0.18.rom.sha256
[protectli_vp4630_vp4650_v1.0.18.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.18/protectli_vp4630_vp4650_v1.0.18.rom.sha256.sig
[protectli_vp4670_v1.0.18.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.18/protectli_vp4670_v1.0.18.rom
[protectli_vp4670_v1.0.18.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.18/protectli_vp4670_v1.0.18.rom.sha256
[protectli_vp4670_v1.0.18.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.18/protectli_vp4670_v1.0.18.rom.sha256.sig

## v1.0.17 - 2022-08-17

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/19YnBLxHw0mae-SQ2xl6BgPeims9hH_oVGwyF70pj9EY/edit#gid=1614315669).

### Added

- [Tools for resigning Vboot images with one RW partition](https://docs.dasharo.com/common-coreboot-docs/vboot_signing/)

### Changed

- Set thermal throttling temperature to 80 degrees
- Disabled UEFI Secure Boot by default

### Fixed

- Platform rebooting every 56 minutes
- Incorrect menu labels displayed in network boot menu
- Built-in audio jack does not work

### Binaries

[protectli_vault_cml_v1.0.17.rom_file][protectli_vault_cml_v1.0.17.rom_file]{.md-button}
[protectli_vault_cml_v1.0.17.rom_hash][protectli_vault_cml_v1.0.17.rom_hash]{.md-button}
[protectli_vault_cml_v1.0.17.rom_sig][protectli_vault_cml_v1.0.17.rom_sig]{.md-button}

See how to verify signatures on [this video](https://asciinema.org/a/388861)

### SBOM (Software Bill of Materials)

- [coreboot based on 4.16 revision d662831d](https://github.com/Dasharo/coreboot/tree/d662831d)
- [edk2 based on 7f90b9cd revision 576aa6a4](https://github.com/Dasharo/edk2/tree/576aa6a4)

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

### SBOM (Software Bill of Materials)

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
[protectli_vault_cml_v1.0.17.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.17/protectli_vault_cml_v1.0.17.rom
[protectli_vault_cml_v1.0.17.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.17/protectli_vault_cml_v1.0.17.rom.sha256
[protectli_vault_cml_v1.0.17.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.17/protectli_vault_cml_v1.0.17.rom.sha256.sig
[v1.0.16_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.16/protectli_vault_cml_v1.0.16.rom
[v1.0.16_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.16/protectli_vault_cml_v1.0.16.rom.sha256
[v1.0.16_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.16/protectli_vault_cml_v1.0.16.rom.sha256.sig
[v1.0.13_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.13.rom
[v1.0.13_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.13.rom.sha256
[v1.0.13_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.13.rom.sha256.sig
