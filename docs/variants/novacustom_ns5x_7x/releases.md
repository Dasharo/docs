# Release Notes

Following Release Notes describe status of Open Source Firmware development for
NovaCustom NS5x/7x

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

[Subscribe to NovaCustom NS5x/7x Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

[newsletter]: https://newsletter.3mdeb.com/subscription/T61MyO2sP

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit?usp=sharing).

## v1.2.0 - 2022-05-26

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit#gid=1695997523).

### Added

- Persistent RGB keyboard settings
- Increased power limits to CPU defaults (28W PL1 / 35W PL2)

### Fixed

- [CVE-2022-29264 SMM loader vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2022-29264)
- [Incorrect vendor name in SMBIOS](https://github.com/Dasharo/dasharo-issues/issues/74)

### Known issues

- [CPU not running on expected frequency and usage NS50MU](https://github.com/Dasharo/dasharo-issues/issues/64)
- [UCM-UCSI ACPI device displays an error in Windows Device Manager](https://github.com/Dasharo/dasharo-issues/issues/57)
- [Headsets connected to the docking station are not recognizable on NS70/50 v1.2.0](https://github.com/Dasharo/dasharo-issues/issues/89)
- [General problem with charging the DUT via the docking station using USB Type-C slot NS70/50 v1.2.0](https://github.com/Dasharo/dasharo-issues/issues/91)

### Binaries

[novacustom_ns5x_v1.2.0.rom][rom_v1.2.0]{ .md-button }
[sha256][sha_v1.2.0]{ .md-button }
[sha256.sig][sig_v1.2.0]{ .md-button }

[rom_v1.2.0]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/v1.2.0/novacustom_ns5x_v1.2.0.rom
[sha_v1.2.0]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/v1.2.0/novacustom_ns5x_v1.2.0.rom.sha256
[sig_v1.2.0]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/v1.2.0/novacustom_ns5x_v1.2.0.rom.sha256.sig

See how to verify signatures on [this video](https://asciinema.org/a/433461)

### SBOM (Software Bill of Materials)

- [coreboot based on 4.16 revision b087dcbd](https://github.com/Dasharo/coreboot/tree/b087dcbd)
- [tianocore based on e0334c228ce4ba51f47ff79a118f214031d4650f revision 90364638](https://github.com/Dasharo/edk2/tree/90364638)

## v1.1.0 - 2022-04-22

### Added

- Support for NovaCustom NS7x
- [Support for RGB Keyboard](https://docs.dasharo.com/variants/novacustom_ns5x/rgb_keyboard/)
- [Persistent boot logo implementation](https://docs.dasharo.com/common-coreboot-docs/custom_logo/)

### Changed

- [Temporarily disable vboot due to the risk of bricinkg certain units when flashing via internal programmer](https://github.com/Dasharo/dasharo-issues/issues/73)

### Known issues

- [CPU not running on expected frequency and usage NS50MU](https://github.com/Dasharo/dasharo-issues/issues/64)
- [UCM-UCSI ACPI device displays an error in Windows Device Manager](https://github.com/Dasharo/dasharo-issues/issues/57)
- [The touchpad ON/OFF switch Fn key is not functional](https://github.com/Dasharo/dasharo-issues/issues/38)
- [Incorrect vendor name in SMBIOS](https://github.com/Dasharo/dasharo-issues/issues/74)

### Binaries

[novacustom_ns5x_v1.1.0.rom][rom_v1.1.0]{ .md-button }
[sha256][sha_v1.1.0]{ .md-button }
[sha256.sig][sig_v1.1.0]{ .md-button }

[rom_v1.1.0]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/v1.1.0/novacustom_ns5x_v1.1.0.rom
[sha_v1.1.0]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/v1.1.0/novacustom_ns5x_v1.1.0.rom.sha256
[sig_v1.1.0]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/v1.1.0/novacustom_ns5x_v1.1.0.rom.sha256.sig

See how to verify signatures on [this video](https://asciinema.org/a/433461)

### SBOM (Software Bill of Materials)

- [coreboot based on 4.16 revision c2f031af](https://github.com/Dasharo/coreboot/tree/c2f031af)
- [tianocore based on e0334c228ce4ba51f47ff79a118f214031d4650f revision 4d2846ba](https://github.com/Dasharo/edk2/tree/4d2846ba)

## v1.0.0 - 2022-03-23

### Added

- Support for NovaCustom NS5x
- Support for EC firmware 1.07.07
- UEFI Boot Support
- Configurable boot order
- Configurable boot options
- UEFI Secure Boot support
- NovaCustom boot logo

### Known issues

- [The touchpad ON/OFF switch Fn key is not functional](https://github.com/Dasharo/dasharo-issues/issues/38)

### Binaries

[novacustom_ns5x_v1.0.0.rom][v1.0.0_rom]{ .md-button }
[sha256][v1.0.0_sha]{ .md-button }
[sha256.sig][v1.0.0_sig]{ .md-button }

[v1.0.0_rom]:https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/novacustom_ns5x_v1.0.0.rom
[v1.0.0_sha]:https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/novacustom_ns5x_v1.0.0.rom.sha256
[v1.0.0_sig]:https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/novacustom_ns5x_v1.0.0.rom.sha256.sig

### SBOM (Software Bill of Materials)

- [coreboot based on 4.16 revision ecf1e9b8](https://github.com/Dasharo/coreboot/tree/ecf1e9b8)
- [tianocore based on e0334c228ce4ba51f47ff79a118f214031d4650f revision ec6805c2](https://github.com/Dasharo/edk2/tree/ec6805c2)
