# Protectli VP4620 Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development for
Protectli VP4620

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>
[Subscribe to Protectli VP4620 Dasharo Release Newsletter]
[newsletter]{.md-button .md-button--primary .center}
</center>

Detailed test results for every release can be found
[here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit?usp=sharing).

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
[v1.0.13_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.13.rom
[v1.0.13_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.13.rom.sha256
[v1.0.13_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.13.rom.sha256.sig

### Test Results

|     Protectli VP4620     |  v1.0.13 |
|:------------------------:|:--------:|
|TESTED                    |32        |
|PASSED                    |32        |
|PASSED(%)                 |100,00%   |
|FAILED                    |0         |
