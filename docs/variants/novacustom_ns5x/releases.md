# NovaCustom NS5x Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development for
NovaCustom NS5x

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

[Subscribe to NovaCustom NS5x Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

[newsletter]: https://newsletter.3mdeb.com/subscription/T61MyO2sP

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
