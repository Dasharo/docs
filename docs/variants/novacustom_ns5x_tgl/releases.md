# NovaCustom NS5x/7x 11th Gen Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
NovaCustom NS5x/7x 11th Gen

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("8f2fb839-a6ce-40b8-a26d-8d1fa4de12f7",
"Subscribe to NovaCustom NS5x/7x 11th Gen Dasharo Release Newsletter") }}

## v1.5.2 - 2024-01-17

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit#gid=38447675).

### Added

- [Added Microsoft 2023 keys for UEFI Secure Boot and DBX from 2023.05.9](https://github.com/Dasharo/edk2/commit/b7274c98697e972e772236caf830c0780ec498bd)

### Changed

- [Changed throttling temperature to 80 degrees](https://github.com/Dasharo/dasharo-issues/issues/596)
- [Enabled HTTPS for Dasharo Tools Suite network boot option](https://github.com/Dasharo/dasharo-issues/issues/450)

### Fixed

- [Low performance when booting on battery power only](https://github.com/Dasharo/dasharo-issues/issues/555)
- [Regression charging via dell usb-c dock](https://github.com/Dasharo/dasharo-issues/issues/587)
- [Video on USB-C docks sometimes fails to initialize](https://github.com/Dasharo/dasharo-issues/issues/560)
- [USB-C chargers may be overloaded in certain scenarios](https://github.com/Dasharo/dasharo-issues/issues/619)
- [Hybrid Power Boost mode of battery charger is not functional](https://github.com/Dasharo/dasharo-issues/issues/620)
- [Laptop may shut down when disconnecting power supply](https://github.com/Dasharo/dasharo-issues/issues/621)
- [Input current limits are set too high](https://github.com/Dasharo/dasharo-issues/issues/622)
- [Keyboard backlight does not turn off immediately when going to sleep](https://github.com/Dasharo/dasharo-issues/issues/623)
- [Power LED blinks erratically in HPB mode](https://github.com/Dasharo/dasharo-issues/issues/624)
- [EC applying power limits may sometimes fail](https://github.com/Dasharo/dasharo-issues/issues/625)
- [Wrong power limits are applied on AC attach / detach](https://github.com/Dasharo/dasharo-issues/issues/626)
- [USB-PD controller may hang in glitched state on shutdown](https://github.com/Dasharo/dasharo-issues/issues/627)
- [Yellow bangs in device manager](https://docs.dasharo.com/unified/clevo/post-install/#unrecognized-usb-controller-device-in-device-manager)
- [Random freezes in Windows 11](https://github.com/Dasharo/dasharo-issues/issues/628)
- [Low level interfering crackling/popping of the speakers while playing no sound](https://github.com/Dasharo/dasharo-issues/issues/224)
- [ACPI error during boot (system76_acpi::kbd_backlight)](https://github.com/Dasharo/dasharo-issues/issues/559)
- [Thunderbolt may not work after wakeup from sleep](https://github.com/Dasharo/dasharo-issues/issues/629)
- [Unnecessary security warning after firmware update](https://github.com/Dasharo/dasharo-issues/issues/556)

### Known issues

- [Poor Package C-state residency at idle after first s2idle cycle](https://github.com/Dasharo/dasharo-issues/issues/631)
- [Some commands in dasharo_ectool fail](https://github.com/Dasharo/dasharo-issues/issues/648)
- [Incomplete serial console output](https://github.com/Dasharo/dasharo-issues/issues/614)
- [Some devices on dock are not detected after warmboot or reboot](https://github.com/Dasharo/dasharo-issues/issues/632)
- [Function Lock setting is not saved after cold boot](https://github.com/Dasharo/dasharo-issues/issues/458)
- [No ability to change active PCR banks with TPM PPI in FW](https://github.com/Dasharo/dasharo-issues/issues/521)
- [Turning wifi/bt off inside BIOS leads to an ACPI error message while system start on Gentoo Linux](https://github.com/Dasharo/dasharo-issues/issues/638)
- [The laptop does not automatically wake up from hibernation using rtcwake](https://github.com/Dasharo/dasharo-issues/issues/485)
- [Power state after power failure option does not work as intended](https://github.com/Dasharo/dasharo-issues/issues/524)
- [OS fails to resume from S3 on some board revisions](https://github.com/Dasharo/dasharo-issues/issues/523)
- [Windows 11 fails to resume from hibernation](https://github.com/Dasharo/dasharo-issues/issues/529)
- [No HDMI output in firmware](https://github.com/Dasharo/dasharo-issues/issues/533)
- [Connecting and immediately disconnecting the charger, sets the battery status in OS to "charging" for about 2 minutes](https://github.com/Dasharo/dasharo-issues/issues/350)
- [Platform fails to resume from S3 suspend](https://github.com/Dasharo/dasharo-issues/issues/554)
- [Early boot DMA protection setting in UEFI does not work correctly](https://github.com/Dasharo/dasharo-issues/issues/630)

### Binaries

[novacustom_ns5x_tgl_ec_v1.5.2.rom][novacustom_ns5x_tgl_ec_v1.5.2.rom_file]{.md-button}
[sha256][novacustom_ns5x_tgl_ec_v1.5.2.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_tgl_ec_v1.5.2.rom_sig]{.md-button}

[novacustom_ns5x_tgl_v1.5.2.rom][novacustom_ns5x_tgl_v1.5.2.rom_file]{.md-button}
[sha256][novacustom_ns5x_tgl_v1.5.2.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_tgl_v1.5.2.rom_sig]{.md-button}

[novacustom_ns5x_tgl_v1.5.2_dev_signed.rom][novacustom_ns5x_tgl_v1.5.2_dev_signed.rom_file]{.md-button}
[sha256][novacustom_ns5x_tgl_v1.5.2_dev_signed.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_tgl_v1.5.2_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 4.21 revision cb6ef1b9](https://github.com/Dasharo/coreboot/tree/cb6ef1b9)
- [Dasharo EDKII fork based on edk2-stable202002 revision b7274c98](https://github.com/Dasharo/edk2/tree/b7274c98)

[novacustom_ns5x_tgl_ec_v1.5.2.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.2/novacustom_ns5x_tgl_ec_v1.5.2.rom
[novacustom_ns5x_tgl_ec_v1.5.2.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.2/novacustom_ns5x_tgl_ec_v1.5.2.rom.sha256
[novacustom_ns5x_tgl_ec_v1.5.2.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.2/novacustom_ns5x_tgl_ec_v1.5.2.rom.sha256.sig
[novacustom_ns5x_tgl_v1.5.2.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.2/novacustom_ns5x_tgl_v1.5.2.rom
[novacustom_ns5x_tgl_v1.5.2.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.2/novacustom_ns5x_tgl_v1.5.2.rom.sha256
[novacustom_ns5x_tgl_v1.5.2.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.2/novacustom_ns5x_tgl_v1.5.2.rom.sha256.sig
[novacustom_ns5x_tgl_v1.5.2_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.2/novacustom_ns5x_tgl_v1.5.2_dev_signed.rom
[novacustom_ns5x_tgl_v1.5.2_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.2/novacustom_ns5x_tgl_v1.5.2_dev_signed.rom.sha256
[novacustom_ns5x_tgl_v1.5.2_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.2/novacustom_ns5x_tgl_v1.5.2_dev_signed.rom.sha256.sig

## v1.5.1 - 2023-11-06

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit#gid=38447675).

### Added

- [Firmware update mode](https://docs.dasharo.com../../guides/firmware-update/#firmware-update-mode)
- [BIOS boot medium write-protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [SMM BIOS write protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Early boot DMA protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Early Sign of Life display output](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/347-sign-of-life/)
- [Current limiting for USB-PD power supplies](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31H-usb-type-c/#utc020001-usb-type-c-pd-current-limiting-ubuntu-2204)
- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
- [Wi-Fi / Bluetooth module disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Built-in webcam disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Network stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#networking-options)
- [Battery threshold options in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Intel ME disable option in setup menu](https://docs.dasharo.com/osf-trivia-list/me/)
- [Block boot when battery is too low](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/359-boot-blocking/#test-cases-common-documentation)
- [Power on AC option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)

### Changed

- [Rebased on coreboot release 4.21](https://doc.coreboot.org/releases/coreboot-4.21-relnotes.html)
- [Removed software keyboard backlight controls for improved backlight reliability](https://github.com/Dasharo/dasharo-issues/issues/514)
- Disabled EC debug logging for improved security
- Set throttling temperature to 75 degrees C
- UEFI 2.8 specification compliance
- Improved battery charging logic
- Improved USB-C docking station compatibility

### Fixed

- [Low performance when booting on battery power only](https://github.com/Dasharo/dasharo-issues/issues/555)
- [Power delivery compatibility](https://github.com/Dasharo/dasharo-issues/issues/236)
- [Better support for USB-PD power supplies](https://github.com/Dasharo/dasharo-issues/issues/431)
- [After changing the Intel ME mode the Reset option in the setup menu turns off the device](https://github.com/Dasharo/dasharo-issues/issues/403)
- [Laptops randomly go into suspend mode from which they can not wake up.](https://github.com/Dasharo/dasharo-issues/issues/474)
- [Reset to defaults with F9 causes the wrong settings to be restored](https://github.com/Dasharo/dasharo-issues/issues/355)
- [Keyboard backlight not working after restart](https://github.com/Dasharo/dasharo-issues/issues/349)
- [Warning sign in device manager under the touchpad device](https://github.com/Dasharo/dasharo-issues/issues/194)
- [Popup with information about recovery mode is displayed after flashing with a valid binary](https://github.com/Dasharo/dasharo-issues/issues/269)
- [The power LED is not always blinking while in sleep mode on Windows 11](https://github.com/Dasharo/dasharo-issues/issues/182)
- [Internal keyboard stops working randomly in firmware](https://github.com/Dasharo/dasharo-issues/issues/295)
- [DTS on network boot fails to boot](https://github.com/Dasharo/dasharo-issues/issues/502)
- [Firmware Update Mode does not automatically boot into DTS](https://github.com/Dasharo/dasharo-issues/issues/506)
- [Permanent keyboard illumination after cold boot fails: keyboard light level is not saved correctly](https://github.com/Dasharo/dasharo-issues/issues/501)
- [Controlling keyboard illumination (brightess and on/off) does not work](https://github.com/Dasharo/dasharo-issues/issues/498)
- [Permanent keyboard illumination not working in Ubuntu 22.04](https://github.com/Dasharo/dasharo-issues/issues/517)
- [Controlling brightness and turning off RGB keyboard illumination does not work (Ubuntu 22.04)](https://github.com/Dasharo/dasharo-issues/issues/514)
- [Wi-Fi card is not recognized on Windows 11](https://github.com/Dasharo/dasharo-issues/issues/512)
- [No HDMI audio on Windows 11](https://github.com/Dasharo/dasharo-issues/issues/511)
- [No HDMI display output on Windows 11](https://github.com/Dasharo/dasharo-issues/issues/510)
- [No USB-C display output on Windows 11](https://github.com/Dasharo/dasharo-issues/issues/509)
- [Keyboard backlight is disabled after suspend (Windows 11)](https://github.com/Dasharo/dasharo-issues/issues/507)
- [Reset by F9 sets battery thresholds to 0](https://github.com/Dasharo/dasharo-issues/issues/499)
- [The docking station is not detected after cold-boot, warm-boot and reboot](https://github.com/Dasharo/dasharo-issues/issues/404)

### Known issues

- [Docking station may fail to be initialized if connected before booting and connected to multiple monitors](https://github.com/Dasharo/dasharo-issues/issues/560)
- [Connecting and immediately disconnecting the charger, sets the battery status in OS to 'charging' for about 2 minutes](https://github.com/Dasharo/dasharo-issues/issues/350)
- [Power state after power failure option does not work as intended](https://github.com/Dasharo/dasharo-issues/issues/524)
- [No ability to change active PCR banks with TPM PPI in FW](https://github.com/Dasharo/dasharo-issues/issues/521)
- [Windows 11 fails to resume from S3 on some board revisions](https://github.com/Dasharo/dasharo-issues/issues/523)
- [Windows 11 fails to resume from hibernation](https://github.com/Dasharo/dasharo-issues/issues/529)

### Binaries

[novacustom_ns5x_tgl_ec_v1.5.1.rom][novacustom_ns5x_tgl_ec_v1.5.1.rom_file]{.md-button}
[sha256][novacustom_ns5x_tgl_ec_v1.5.1.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_tgl_ec_v1.5.1.rom_sig]{.md-button}

[novacustom_ns5x_tgl_v1.5.1.rom][novacustom_ns5x_tgl_v1.5.1.rom_file]{.md-button}
[sha256][novacustom_ns5x_tgl_v1.5.1.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_tgl_v1.5.1.rom_sig]{.md-button}

[novacustom_ns5x_tgl_v1.5.1_dev_signed.rom][novacustom_ns5x_tgl_v1.5.1_dev_signed.rom_file]{.md-button}
[sha256][novacustom_ns5x_tgl_v1.5.1_dev_signed.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_tgl_v1.5.1_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 4.21 revision 36032e55](https://github.com/Dasharo/coreboot/tree/36032e55)
- [Dasharo EDKII fork based on edk2-stable202002 revision b68e46b0](https://github.com/Dasharo/edk2/tree/b68e46b0)

[novacustom_ns5x_tgl_ec_v1.5.1.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.1/novacustom_ns5x_tgl_ec_v1.5.1.rom
[novacustom_ns5x_tgl_ec_v1.5.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.1/novacustom_ns5x_tgl_ec_v1.5.1.rom.sha256
[novacustom_ns5x_tgl_ec_v1.5.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.1/novacustom_ns5x_tgl_ec_v1.5.1.rom.sha256.sig
[novacustom_ns5x_tgl_v1.5.1.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.1/novacustom_ns5x_tgl_v1.5.1.rom
[novacustom_ns5x_tgl_v1.5.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.1/novacustom_ns5x_tgl_v1.5.1.rom.sha256
[novacustom_ns5x_tgl_v1.5.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.1/novacustom_ns5x_tgl_v1.5.1.rom.sha256.sig
[novacustom_ns5x_tgl_v1.5.1_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.1/novacustom_ns5x_tgl_v1.5.1_dev_signed.rom
[novacustom_ns5x_tgl_v1.5.1_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.1/novacustom_ns5x_tgl_v1.5.1_dev_signed.rom.sha256
[novacustom_ns5x_tgl_v1.5.1_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.1/novacustom_ns5x_tgl_v1.5.1_dev_signed.rom.sha256.sig

## v1.5.0 - Non-public engineering release

## v1.4.0 - 2023-03-02

### Added

- [The same keyboard illumination setting is restored after suspend or poweroff](https://github.com/Dasharo/dasharo-issues/issues/339)
- [One of the two fan profiles can now be selected in Setup Menu](https://docs.dasharo.com/unified/novacustom/features/)
- [Fn lock hotkey feature](https://docs.dasharo.com/unified/novacustom/features/)

### Changed

- [Keys must be provisioned prior enabling Secure Boot](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
- [Trackpad no longer working after 1.3.0 upgrade from 1.1.0 (Dasharo issue #313)](https://github.com/Dasharo/dasharo-issues/issues/313)

### Known issues

- [Low level interfering crackling/popping of the speakers while playing no sound (Dasharo issue #224)](https://github.com/Dasharo/dasharo-issues/issues/224)
- [The power LED is not always blinking while in sleep mode on Windows 11 (Dasharo issue #182)](https://github.com/Dasharo/dasharo-issues/issues/182)
- [Keyboard backlight turns on after resuming from sleep mode  (Dasharo issue #332)](https://github.com/Dasharo/dasharo-issues/issues/332)
- [The screen brightness level gets stuck when key are held or pressed too fast (Dasharo issue #341)](https://github.com/Dasharo/dasharo-issues/issues/341)
- [Connecting and immediately disconnecting the charger, sets the battery status in OS to 'charging' for about 2 minutes (Dasharo issue #350)](https://github.com/Dasharo/dasharo-issues/issues/350)
- [Reset to defaults with F9 causes the wrong settings to be restored (Dasharo issue #355)](https://github.com/Dasharo/dasharo-issues/issues/355)
- [Connecting the RJ45 cable to the Gigabit Ethernet port on the docking station does not result in obtaining an Internet connection (Dasharo issue #356)](https://github.com/Dasharo/dasharo-issues/issues/356)
- [Unable to login to Windows 11 with the docking station connected (Dasharo issue #357)](https://github.com/Dasharo/dasharo-issues/issues/357)

### Binaries

[novacustom_ns5x_tgl_ec_v1.4.0.rom][novacustom_ns5x_tgl_ec_v1.4.0.rom_file]{.md-button}
[sha256][novacustom_ns5x_tgl_ec_v1.4.0.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_tgl_ec_v1.4.0.rom_sig]{.md-button}

[novacustom_ns5x_tgl_v1.4.0.rom][novacustom_ns5x_tgl_v1.4.0.rom_file]{.md-button}
[sha256][novacustom_ns5x_tgl_v1.4.0.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_tgl_v1.4.0.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 1a8eb6c02103727431ac1ea23f4f507e49f3cde7 revision 636f432a](https://github.com/Dasharo/coreboot/tree/636f432a)
- [EDK2 based on e0334c228ce4ba51f47ff79a118f214031d4650f revision 2c61576a](https://github.com/Dasharo/edk2/tree/2c61576a)
- Intel ME version 15.0.30.1776

[novacustom_ns5x_tgl_ec_v1.4.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.4.0/novacustom_ns5x_tgl_ec_v1.4.0.rom
[novacustom_ns5x_tgl_ec_v1.4.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.4.0/novacustom_ns5x_tgl_ec_v1.4.0.rom.sha256
[novacustom_ns5x_tgl_ec_v1.4.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.4.0/novacustom_ns5x_tgl_ec_v1.4.0.rom.sha256.sig
[novacustom_ns5x_tgl_v1.4.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.4.0/novacustom_ns5x_tgl_v1.4.0.rom
[novacustom_ns5x_tgl_v1.4.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.4.0/novacustom_ns5x_tgl_v1.4.0.rom.sha256
[novacustom_ns5x_tgl_v1.4.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.4.0/novacustom_ns5x_tgl_v1.4.0.rom.sha256.sig

## v1.3.0 - 2022-09-01

### EC firmware transition

Please note, that version 1.3.0 of `Dasharo BIOS firmware` works correctly
**only** with the `Dasharo EC firmware`. This is the first release when this
open-source EC firmware is used, so additional steps need to be taken when
upgrading.

Please refer to the [Firmware update](../../unified/novacustom/firmware-update.md)
section for more details on upgrading your firmware.

### Added

- [Enabled Vboot Verified Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)

- Vboot Recovery Popup

- Fullscreen setup menu

### Changed

- Rebased on upstream coreboot revision 1a8eb6c0

- [Support for Open EC
  Firmware](https://docs.dasharo.com/dasharo-tools-suite/documentation/features/#ec-transition)

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

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

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

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 4.16 revision b087dcbd](https://github.com/Dasharo/coreboot/tree/b087dcbd)
- [tianocore based on e0334c228ce4ba51f47ff79a118f214031d4650f revision 90364638](https://github.com/Dasharo/edk2/tree/90364638)

## v1.1.0 - 2022-04-22

### Added

- Support for NovaCustom NS7x
- [Support for RGB Keyboard](https://docs.dasharo.com/unified/novacustom/features/)
- [Persistent boot logo implementation](https://docs.dasharo.com../../guides/logo-customization)

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

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

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
