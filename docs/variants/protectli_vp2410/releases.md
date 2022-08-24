# Release Notes

Following Release Notes describe status of Open Source Firmware development for
Protectli VP2410

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>
[Subscribe to Protectli VP2410 Dasharo Release Newsletter]
[newsletter]{.md-button .md-button--primary .center}
</center>

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit#gid=975611333).

## v1.0.15 - 2022-05-31

### Changed

- Customized Network boot menu and strings

### Fixed

- SMBIOS memory information showing 0 MB DRAM in setup

### Known issues

- [USB 2.0 sticks not detected on VP2410](https://github.com/Dasharo/dasharo-issues/issues/99)
- [S3 resume does not work in Geminilake FSP](https://github.com/Dasharo/dasharo-issues/issues/27)

### Binaries

<!--
[protectli_vault_glk_v1.0.15.rom][v1.0.15_rom]{.md-button}
[sha256][v1.0.15_hash]{.md-button}
[sha256.sig][v1.0.15_sig]{.md-button}

See how to verify signatures on [this video](https://asciinema.org/a/388861)
-->

The binaries will be published by Protectli on their webpage. As soon as they
show up, Dasharo will link to them as well.

### SBOM (Software Bill of Materials)

- [coreboot based on b77cf229 revision f59b1ec9](https://github.com/Dasharo/coreboot/tree/f59b1ec9)
- [edk2 based on 7f90b9cd revision 90364638](https://github.com/Dasharo/edk2/tree/90364638)

[newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
[v1.0.15_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.0.15/protectli_vault_glk_v1.0.15.rom
[v1.0.15_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.0.15/protectli_vault_glk_v1.0.15.rom.sha256
[v1.0.15_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.0.15/protectli_vault_glk_v1.0.15.rom.sha256.sig
