# NovaCustom NS5x/NS7x ADL (12th Gen) Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
NovaCustom NS5x/NS7x ADL (12th Gen)

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

[Subscribe to NovaCustom NS5x/NS7x ADL (12th Gen) Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

## v1.6.0 - 2023-04-07

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit#gid=1695997523).

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

- [Waking up from sleep on Ubuntu 22.04 is not 100% reliable (Dasharo issue #205)](https://github.com/Dasharo/dasharo-issues/issues/205)
- [The connected RJ45 cable to the Ethernet socket causes a hardware error on Windows 11 (Dasharo issue #264)](https://github.com/Dasharo/dasharo-issues/issues/264)
- [Laptop not starting after fully discharging (NS70PU) (Dasharo issue #287)](https://github.com/Dasharo/dasharo-issues/issues/287)
- [The Auto Boot time-out value is not respected (Dasharo issue #292)](https://github.com/Dasharo/dasharo-issues/issues/292)
- [ACPI boot errors during booting Ubuntu 22.04 (Dasharo issue #293)](https://github.com/Dasharo/dasharo-issues/issues/293)
- [Windows update KB5012170 cannot be installed (Dasharo issue #294)](https://github.com/Dasharo/dasharo-issues/issues/294)
- [Internal keyboard sometimes does not work in firmware (Dasharo issue #295)](https://github.com/Dasharo/dasharo-issues/issues/295)
- [SMMStore sometimes gets wiped out by UEFI payload on NovaCustom ADL laptops (Dasharo issue #298)](https://github.com/Dasharo/dasharo-issues/issues/298)

### Known issues

- [The power LED is not always blinking while in sleep mode on Windows 11 (Dasharo issue #182)](https://github.com/Dasharo/dasharo-issues/issues/182)
- [Suspend does not work correctly while a SATA disk is installed (Dasharo issue #230)](https://github.com/Dasharo/dasharo-issues/issues/230)
- [Touchpad isn't work on Debian 11.3 (Dasharo issue #240)](https://github.com/Dasharo/dasharo-issues/issues/240)
- [Sleep sometimes not working (Dasharo issue #261)](https://github.com/Dasharo/dasharo-issues/issues/261)
- [Popup with information about recovery mode is displayed after flashing with a valid binary (Dasharo issue #269)](https://github.com/Dasharo/dasharo-issues/issues/269)
- [Missing information about cache  (Dasharo issue #343)](https://github.com/Dasharo/dasharo-issues/issues/343)
- [Keyboard backlight not working after restart (Dasharo issue #349)](https://github.com/Dasharo/dasharo-issues/issues/349)
- [Connecting and immediately disconnecting the charger, sets the battery status in OS to charging for about 2 minutes  (Dasharo issue #350)](https://github.com/Dasharo/dasharo-issues/issues/350)
- [Reset to defaults with F9 causes the wrong settings to be restored (Dasharo issue #355)](https://github.com/Dasharo/dasharo-issues/issues/355)
- [Laptop not suspending while connected to a USB-C docking station (Dasharo issue #368)](https://github.com/Dasharo/dasharo-issues/issues/368)
- [Keyboard backlight brightness is not properly restored after cold boot (Dasharo issue #402)](https://github.com/Dasharo/dasharo-issues/issues/402)
- [After changing the Intel ME mode the Reset option in the setup menu turns off the device (Dasharo issue #403)](https://github.com/Dasharo/dasharo-issues/issues/403)
- [The docking station is not detected after cold boot and warm boot (Dasharo issue #404)](https://github.com/Dasharo/dasharo-issues/issues/404)

### Binaries

[novacustom_ns5x_adl_ec_v1.6.0.rom][novacustom_ns5x_adl_ec_v1.6.0.rom_file]{.md-button}
[sha256][novacustom_ns5x_adl_ec_v1.6.0.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_adl_ec_v1.6.0.rom_sig]{.md-button}

[novacustom_ns5x_adl_v1.6.0.rom][novacustom_ns5x_adl_v1.6.0.rom_file]{.md-button}
[sha256][novacustom_ns5x_adl_v1.6.0.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_adl_v1.6.0.rom_sig]{.md-button}

See how to verify signatures on [this video](https://asciinema.org/a/518379)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 1a8eb6c02103727431ac1ea23f4f507e49f3cde7 revision ae10b20f](https://github.com/Dasharo/coreboot/tree/ae10b20f)
- [Dasharo EDKII fork based on e0334c228ce4ba51f47ff79a118f214031d4650f revision bd421b40](https://github.com/Dasharo/edk2/tree/bd421b40)
- Intel ME version 16.1.25.1865

[newsletter]: https://newsletter.3mdeb.com/subscription/RJrTXDhWR
[novacustom_ns5x_adl_ec_v1.6.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_adl/v1.6.0/novacustom_ns5x_adl_ec_v1.6.0.rom
[novacustom_ns5x_adl_ec_v1.6.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_adl/v1.6.0/novacustom_ns5x_adl_ec_v1.6.0.rom.sha256
[novacustom_ns5x_adl_ec_v1.6.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_adl/v1.6.0/novacustom_ns5x_adl_ec_v1.6.0.rom.sha256.sig
[novacustom_ns5x_adl_v1.6.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_adl/v1.6.0/novacustom_ns5x_adl_v1.6.0.rom
[novacustom_ns5x_adl_v1.6.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_adl/v1.6.0/novacustom_ns5x_adl_v1.6.0.rom.sha256
[novacustom_ns5x_adl_v1.6.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_adl/v1.6.0/novacustom_ns5x_adl_v1.6.0.rom.sha256.sig

## v1.5.0 - Non-public engineering release

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
