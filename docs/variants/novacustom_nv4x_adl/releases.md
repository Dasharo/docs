# NovaCustom NV4x ADL (12th Gen) Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
NovaCustom NV4x ADL (12th Gen)

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

[Subscribe to NovaCustom NV4x ADL (12th Gen) Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

</center>

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit#gid=1695997523).

## v1.6.0 - 2023-04-18

### Added

- [Intel Management Engine Disable](https://github.com/Dasharo/dasharo-issues/issues/111)
- [The same keyboard illumination setting is restored after suspend or poweroff](https://github.com/Dasharo/dasharo-issues/issues/339)
- [One of the two fan profiles can now be selected in Setup Menu](https://docs.dasharo.com/unified/novacustom/fan-profiles/)
- [Fn lock hotkey feature](https://docs.dasharo.com/unified/novacustom/fn-lock-hotkey/)
- [Setup menu option for switching between S0ix and S3 suspend mode](https://github.com/Dasharo/dasharo-issues/issues/300)

### Changed

- [Keys must be provisioned prior enabling Secure Boot](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
- The function keys responsible for entering the setup and boot menu in BIOS
  have been changed from ESC/F12 to F2/F7

### Fixed

- [The power LED is not always blinking while in sleep mode on Ubuntu 22.04 (Dasharo issue #260)](https://github.com/Dasharo/dasharo-issues/issues/260)
- [Suspend mode not working under Qubes OS 4.1 (Dasharo issue #266)](https://github.com/Dasharo/dasharo-issues/issues/266)
- [Docking station under Qubes OS (Dasharo issue #267)](https://github.com/Dasharo/dasharo-issues/issues/267)
- [The Auto Boot time-out value is not respected (Dasharo issue #292)](https://github.com/Dasharo/dasharo-issues/issues/292)
- [ACPI boot errors during booting Ubuntu 22.04 (Dasharo issue #293)](https://github.com/Dasharo/dasharo-issues/issues/293)
- [Windows update KB5012170 cannot be installed (Dasharo issue #294)](https://github.com/Dasharo/dasharo-issues/issues/294)
- [Internal keyboard sometimes does not work in firmware (Dasharo issue #295)](https://github.com/Dasharo/dasharo-issues/issues/295)
- [Laptop hangs up after 20 cycles of the suspend procedure (Dasharo issue #305)](https://github.com/Dasharo/dasharo-issues/issues/305)
- [Keyboard backlight not working after restart (Dasharo issue #349)](https://github.com/Dasharo/dasharo-issues/issues/349)
- [Function key display on/off does not completely blank the screen  (Dasharo issue #354)](https://github.com/Dasharo/dasharo-issues/issues/354)
- [Connecting the RJ45 cable to the Gigabit Ethernet port on the docking station does not result in obtaining an Internet connection (Dasharo issue #356)](https://github.com/Dasharo/dasharo-issues/issues/356)
- [Unable to wake up from suspend (Dasharo issue #362)](https://github.com/Dasharo/dasharo-issues/issues/362)

### Known issues

- [The power LED is not always blinking while in sleep mode on Windows 11 (Dasharo issue #182)](https://github.com/Dasharo/dasharo-issues/issues/182)
- [Popup with information about recovery mode is displayed after flashing with a valid binary (Dasharo issue #269)](https://github.com/Dasharo/dasharo-issues/issues/269)
- [Missing information about cache  (Dasharo issue #343)](https://github.com/Dasharo/dasharo-issues/issues/343)
- [Connecting and immediately disconnecting the charger, sets the battery status in OS to charging for about 2 minutes  (Dasharo issue #350)](https://github.com/Dasharo/dasharo-issues/issues/350)
- [Reset to defaults with F9 causes the wrong settings to be restored (Dasharo issue #355)](https://github.com/Dasharo/dasharo-issues/issues/355)
- [Unwanted reset of BIOS settings (Dasharo issue #365)](https://github.com/Dasharo/dasharo-issues/issues/365)
- [Laptop not suspending while connected to a USB-C docking station (Dasharo issue #368)](https://github.com/Dasharo/dasharo-issues/issues/368)
- [The docking station is not detected after cold-boot and warm-boot (dasharo issue #404)](https://github.com/Dasharo/dasharo-issues/issues/404)

### Binaries

[novacustom_nv4x_adl_ec_v1.6.0.rom][novacustom_nv4x_adl_ec_v1.6.0.rom_file]{.md-button}
[sha256][novacustom_nv4x_adl_ec_v1.6.0.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_ec_v1.6.0.rom_sig]{.md-button}

[novacustom_nv4x_adl_v1.6.0.rom][novacustom_nv4x_adl_v1.6.0.rom_file]{.md-button}
[sha256][novacustom_nv4x_adl_v1.6.0.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_v1.6.0.rom_sig]{.md-button}

See how to verify signatures on [this video](https://asciinema.org/a/518379)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 1a8eb6c02103727431ac1ea23f4f507e49f3cde7 revision a3056ac5](https://github.com/Dasharo/coreboot/tree/a3056ac5)
- [Dasharo EDKII fork based on e0334c228ce4ba51f47ff79a118f214031d4650f revision bd421b40](https://github.com/Dasharo/edk2/tree/bd421b40)

[newsletter]: https://newsletter.3mdeb.com/subscription/RJrTXDhWR
[novacustom_nv4x_adl_ec_v1.6.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.6.0/novacustom_nv4x_adl_ec_v1.6.0.rom
[novacustom_nv4x_adl_ec_v1.6.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.6.0/novacustom_nv4x_adl_ec_v1.6.0.rom.sha256
[novacustom_nv4x_adl_ec_v1.6.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.6.0/novacustom_nv4x_adl_ec_v1.6.0.rom.sha256.sig
[novacustom_nv4x_adl_v1.6.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.6.0/novacustom_nv4x_adl_v1.6.0.rom
[novacustom_nv4x_adl_v1.6.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.6.0/novacustom_nv4x_adl_v1.6.0.rom.sha256
[novacustom_nv4x_adl_v1.6.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.6.0/novacustom_nv4x_adl_v1.6.0.rom.sha256.sig

## v1.4.0 - 2022-12-13

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
