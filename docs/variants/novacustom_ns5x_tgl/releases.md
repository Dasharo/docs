# NovaCustom NS5x/NS7x TGL (11th Gen) Dasharo Release Notes

Following Release Notes describe the status of Open Source Firmware development
for NovaCustom NS5x/7x.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

[Subscribe to NovaCustom NS5x/7x Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

[newsletter]: https://newsletter.3mdeb.com/subscription/T61MyO2sP

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit?usp=sharing).

## v1.3.0 - 2022-09-01

### EC firmware transition

Please note, that version 1.3.0 of `Dasharo BIOS firmware` works correctly
**only** with the `Dasharo EC firmware`. This is the first release when this
open-source EC firmware is used, so additional steps need to be taken when
upgrading.

Please refer to the [Firmware update](/unified/novacustom/firmware-update)
section for more details on upgrading your firmware.

### Added

- [Enabled Vboot Verified Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)

- Vboot Recovery Popup

- Fullscreen setup menu

### Changed

- Rebased on upstream coreboot revision 1a8eb6c0

- [Support for Open EC Firmware](../../../common-coreboot-docs/dasharo_tools_suite/#dasharo-ec-transition)

- [Disabled UEFI Secure Boot by default](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)

### Fixed

- [The touchpad ON/OFF switch Fn key is not functional](https://github.com/Dasharo/dasharo-issues/issues/38)

### Binaries

[novacustom_ns5x_v1.3.0.rom][rom_v1.3.0]{ .md-button }
[sha256][sha_v1.3.0]{ .md-button }
[sha256.sig][sig_v1.3.0]{ .md-button }
[novacustom_ns5x_v1.3.0_ec.rom][rom_ec_v1.3.0]{ .md-button }
[sha256][sha_ec_v1.3.0]{ .md-button }
[sha256.sig][sig_ec_v1.3.0]{ .md-button }

[rom_v1.3.0]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/v1.3.0/novacustom_ns5x_v1.3.0.rom
[sha_v1.3.0]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/v1.3.0/novacustom_ns5x_v1.3.0.rom.sha256
[sig_v1.3.0]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/v1.3.0/novacustom_ns5x_v1.3.0.rom.sha256.sig
[rom_ec_v1.3.0]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/v1.3.0/novacustom_ns5x_v1.3.0_ec.rom
[sha_ec_v1.3.0]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/v1.3.0/novacustom_ns5x_v1.3.0_ec.rom.sha256
[sig_ec_v1.3.0]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x/v1.3.0/novacustom_ns5x_v1.3.0_ec.rom.sha256.sig

See how to verify signatures on [this video](https://asciinema.org/a/518379)

### SBOM (Software Bill of Materials)

- [coreboot based on 1a8eb6c02103727431ac1ea23f4f507e49f3cde7 revision 1153a18d](https://github.com/Dasharo/coreboot/tree/1153a18d)
- [EDK2 based on e0334c228ce4ba51f47ff79a118f214031d4650f revision abfdef40](https://github.com/Dasharo/edk2/tree/abfdef40)

## v1.2.0 - 2022-05-26

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
- [Support for RGB Keyboard](https://docs.dasharo.com/unified/novacustom/rgb-keyboard/)
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
