# Tuxedo IBS15 Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development for
Tuxedo IBS15

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/126oG3VLk51sTIz-uVIAOTVPxA0qpH9wQ4P-ue2fJLtI/edit?usp=sharing).

## v1.0.0 - 2022-03-15

### Added

- Support for Tuxedo InfinityBook S 15 Gen6
- Support for EC firmware 1.07.02
- Support for Intel ME version 15.0.30.1776
- UEFI Boot Support
- Configurable boot order
- Configurable boot options
- UEFI Secure Boot support
- Tuxedo boot logo

### Known issues

- [The touchpad ON/OFF switch Fn key is not functional](https://github.com/Dasharo/dasharo-issues/issues/38)

### Binaries

[tuxedo_ibs15_v1.0.0.rom](https://3mdeb.com/open-source-firmware/Dasharo/tuxedo_ibs15/tuxedo_ibs15_v1.0.0.rom
){ .md-button }
[sha256](https://3mdeb.com/open-source-firmware/Dasharo/tuxedo_ibs15/tuxedo_ibs15_v1.0.0.rom.sha256
){ .md-button }
[sha256.sig](https://3mdeb.com/open-source-firmware/Dasharo/tuxedo_ibs15/tuxedo_ibs15_v1.0.0.rom.sha256.sig
){ .md-button }

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/tuxedo/tuxedo-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 4.16 revision cf13d6c7](https://github.com/Dasharo/coreboot/commit/cf13d6c7)
- [tianocore based on 9522071f7497a1a0b1077d2b0d5fcc97a126cfd0 revision 7f90b9cd](https://github.com/Dasharo/edk2/commit/7f90b9cd)
