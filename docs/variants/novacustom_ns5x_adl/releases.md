# NovaCustom NS5x/NS7x ADL (12th Gen) Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
NovaCustom NS5x/NS7x ADL (12th Gen)

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

[Subscribe to NovaCustom NS5x/NS7x ADL (12th Gen) Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

## v1.4.0 - 2022-11-06

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit#gid=1695997523).

### Added

- Support for NovaCustom NS5x/NS7x 12th Gen
- [UEFI Boot Support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface/)
- [Configurable boot order](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/325-custom-boot-order/)
- Configurable boot options
- [UEFI Secure Boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [NovaCustom boot logo](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/304-custom-logo/)
- [Vboot Verified Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)
- [Vboot recovery mode information popup](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/#vbo009001-recovery-boot-popup-firmware)
- [Dasharo setup menu full screen mode support](https://github.com/Dasharo/dasharo-issues/issues/118)
- [Support for RGB backlit keyboard](../../../unified/novacustom/rgb-keyboard/)
- [Support for open-source EC firmware](../../../dasharo-tools-suite/documentation#ec-transition)

### Known issues

- [The power LED is not always blinking while in sleep mode on Windows 11 (Dasharo issue #182)](https://github.com/Dasharo/dasharo-issues/issues/182)
- [Suspend does not work correctly while a SATA disk is installed (Dasharo issue #230)](https://github.com/Dasharo/dasharo-issues/issues/230)

### Binaries

[novacustom_ns5x_adl_ec_v1.4.0.rom][novacustom_ns5x_adl_ec_v1.4.0.rom_file]{.md-button}
[sha256][novacustom_ns5x_adl_ec_v1.4.0.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_adl_ec_v1.4.0.rom_sig]{.md-button}

[novacustom_ns5x_adl_v1.4.0.rom][novacustom_ns5x_adl_v1.4.0.rom_file]{.md-button}
[sha256][novacustom_ns5x_adl_v1.4.0.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_adl_v1.4.0.rom_sig]{.md-button}

See how to verify signatures on [this video](https://asciinema.org/a/433461)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 1a8eb6c02103 revision cf81af26](https://github.com/Dasharo/coreboot/tree/cf81af26)
- [Dasharo EDKII fork based on dd7523b5b123 revision abfdef40](https://github.com/Dasharo/edk2/tree/abfdef40)

[newsletter]: https://newsletter.3mdeb.com/subscription/RJrTXDhWR
[novacustom_ns5x_adl_ec_v1.4.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_adl/v1.4.0/novacustom_ns5x_adl_ec_v1.4.0.rom
[novacustom_ns5x_adl_ec_v1.4.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_adl/v1.4.0/novacustom_ns5x_adl_ec_v1.4.0.rom.sha256
[novacustom_ns5x_adl_ec_v1.4.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_adl/v1.4.0/novacustom_ns5x_adl_ec_v1.4.0.rom.sha256.sig
[novacustom_ns5x_adl_v1.4.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_adl/v1.4.0/novacustom_ns5x_adl_v1.4.0.rom
[novacustom_ns5x_adl_v1.4.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_adl/v1.4.0/novacustom_ns5x_adl_v1.4.0.rom.sha256
[novacustom_ns5x_adl_v1.4.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_adl/v1.4.0/novacustom_ns5x_adl_v1.4.0.rom.sha256.sig
