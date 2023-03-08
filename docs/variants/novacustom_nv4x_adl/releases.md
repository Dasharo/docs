# NovaCustom NV4x ADL (12th Gen) Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
NovaCustom NV4x ADL (12th Gen)

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

[Subscribe to NovaCustom NV4x ADL (12th Gen) Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

</center>

## v1.4.0 - 2022-12-13

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit#gid=1695997523).

### Added

- Support for NovaCustom NV4x 12th Gen
- [UEFI Boot Support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface/)
- [Configurable boot order](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/325-custom-boot-order/)
- Configurable boot options
- [UEFI Secure Boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [NovaCustom boot logo](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/304-custom-logo/)
- [Vboot Verified Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)
- [Vboot Recovery Popup](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/#vbo009001-recovery-boot-popup-firmware)
- Fullscreen setup menu
- [Open-source Embedded Controller Firmware](../../../unified/novacustom/recovery/#ec-firmware-recovery)

### Fixed

- [The external headset connected to the jack slot doesn't work](https://github.com/Dasharo/dasharo-issues/issues/254)
- [ISO keyboard issue for non-US layouts NV4xMx](https://github.com/Dasharo/dasharo-issues/issues/259)
- [Sleep sometimes not working](https://github.com/Dasharo/dasharo-issues/issues/261)
- [The connected RJ45 cable to the Ethernet socket causes a hardware error on Windows 11](https://github.com/Dasharo/dasharo-issues/issues/264)
- [The touchpad ON/OFF switch Fn key is not functional](https://github.com/Dasharo/dasharo-issues/issues/38)

### Known issues

- [Popup with information about recovery mode is displayed after flashing with a valid binary](https://github.com/Dasharo/dasharo-issues/issues/269)
- [The power LED is not blinking during sleep mode when the docking station is connected on Windows 11](https://github.com/Dasharo/dasharo-issues/issues/268)

### Binaries

[novacustom_nv4x_adl_ec_v1.4.0.rom][novacustom_nv4x_adl_ec_v1.4.0.rom_file]{.md-button}
[sha256][novacustom_nv4x_adl_ec_v1.4.0.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_ec_v1.4.0.rom_sig]{.md-button}

[novacustom_nv4x_adl_v1.4.0.rom][novacustom_nv4x_adl_v1.4.0.rom_file]{.md-button}
[sha256][novacustom_nv4x_adl_v1.4.0.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_v1.4.0.rom_sig]{.md-button}

See how to verify signatures on [this video](https://asciinema.org/a/518379)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 1a8eb6c02103727431ac1ea23f4f507e49f3cde7 revision cd975d74](https://github.com/Dasharo/coreboot/tree/cd975d74)
- [Dasharo EDKII fork based on e0334c228ce4ba51f47ff79a118f214031d4650f revision abfdef40](https://github.com/Dasharo/edk2/tree/abfdef40)

[newsletter]: https://newsletter.3mdeb.com/subscription/ZkbNv4qdO
[novacustom_nv4x_adl_ec_v1.4.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.4.0/novacustom_nv4x_adl_ec_v1.4.0.rom
[novacustom_nv4x_adl_ec_v1.4.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.4.0/novacustom_nv4x_adl_ec_v1.4.0.rom.sha256
[novacustom_nv4x_adl_ec_v1.4.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.4.0/novacustom_nv4x_adl_ec_v1.4.0.rom.sha256.sig
[novacustom_nv4x_adl_v1.4.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.4.0/novacustom_nv4x_adl_v1.4.0.rom
[novacustom_nv4x_adl_v1.4.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.4.0/novacustom_nv4x_adl_v1.4.0.rom.sha256
[novacustom_nv4x_adl_v1.4.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.4.0/novacustom_nv4x_adl_v1.4.0.rom.sha256.sig
