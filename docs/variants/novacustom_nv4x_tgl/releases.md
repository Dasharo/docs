# NovaCustom NV4x 11th Gen Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
NovaCustom NV4x 11th Gen

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

[Subscribe to NovaCustom NV4x 11th Gen Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

</center>

## v1.5.0 - 2023-10-30

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit#gid=536764189).

### Added

- [Firmware update mode](https://docs.dasharo.com/guides/firmware-update/#firmware-update-mode)
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

### Known issues

- [Connecting and immediately disconnecting the charger, sets the battery status in OS to 'charging' for about 2 minutes](https://github.com/Dasharo/dasharo-issues/issues/350)
- [Power state after power failure option does not work as intended](https://github.com/Dasharo/dasharo-issues/issues/524)
- [No ability to change active PCR banks with TPM PPI in FW](https://github.com/Dasharo/dasharo-issues/issues/521)
- [Windows 11 fails to resume from S3 on some board revisions](https://github.com/Dasharo/dasharo-issues/issues/523)
- [Windows 11 fails to resume from hibernation](https://github.com/Dasharo/dasharo-issues/issues/529)

### Binaries

[novacustom_nv4x_tgl_ec_v1.5.0.rom][novacustom_nv4x_tgl_ec_v1.5.0.rom_file]{.md-button}
[sha256][novacustom_nv4x_tgl_ec_v1.5.0.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_tgl_ec_v1.5.0.rom_sig]{.md-button}

[novacustom_nv4x_tgl_v1.5.0.rom][novacustom_nv4x_tgl_v1.5.0.rom_file]{.md-button}
[sha256][novacustom_nv4x_tgl_v1.5.0.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_tgl_v1.5.0.rom_sig]{.md-button}

[novacustom_nv4x_tgl_v1.5.0_dev_signed.rom][novacustom_nv4x_tgl_v1.5.0_dev_signed.rom_file]{.md-button}
[sha256][novacustom_nv4x_tgl_v1.5.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_tgl_v1.5.0_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 4.21 revision 36032e55](https://github.com/Dasharo/coreboot/tree/36032e55)
- [Dasharo EDKII fork based on edk2-stable202002 revision b68e46b0](https://github.com/Dasharo/edk2/tree/b68e46b0)

[novacustom_nv4x_tgl_ec_v1.5.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.5.0/novacustom_nv4x_tgl_ec_v1.5.0.rom
[novacustom_nv4x_tgl_ec_v1.5.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.5.0/novacustom_nv4x_tgl_ec_v1.5.0.rom.sha256
[novacustom_nv4x_tgl_ec_v1.5.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.5.0/novacustom_nv4x_tgl_ec_v1.5.0.rom.sha256.sig
[novacustom_nv4x_tgl_v1.5.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.5.0/novacustom_nv4x_tgl_v1.5.0.rom
[novacustom_nv4x_tgl_v1.5.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.5.0/novacustom_nv4x_tgl_v1.5.0.rom.sha256
[novacustom_nv4x_tgl_v1.5.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.5.0/novacustom_nv4x_tgl_v1.5.0.rom.sha256.sig
[novacustom_nv4x_tgl_v1.5.0_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.0/novacustom_nv4x_tgl_v1.5.0_dev_signed.rom
[novacustom_nv4x_tgl_v1.5.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.0/novacustom_nv4x_tgl_v1.5.0_dev_signed.rom.sha256
[novacustom_nv4x_tgl_v1.5.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.0/novacustom_nv4x_tgl_v1.5.0_dev_signed.rom.sha256.sig

## v1.4.0 - 2023-02-24

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit#gid=1695997523).

### Added

- [The same keyboard illumination setting is restored after suspend or poweroff](https://github.com/Dasharo/dasharo-issues/issues/339)
- [One of the two fan profiles can now be selected in Setup Menu](https://docs.dasharo.com/unified/novacustom/fan-profiles/)
- [Fn lock hotkey feature](https://docs.dasharo.com/unified/novacustom/fn-lock-hotkey/)

### Changed

- [Keys must be provisioned prior enabling Secure Boot](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)

### Fixed

- [ISO keyboard issue for non-US layouts (Dasharo issue #259)](https://github.com/Dasharo/dasharo-issues/issues/259)
- [The NVIDIA graphics power management isn't properly functional (Dasharo issue #145)](https://github.com/Dasharo/dasharo-issues/issues/145)

### Known issues

- [Low level interfering crackling/popping of the speakers while playing no sound (Dasharo issue #224)](https://github.com/Dasharo/dasharo-issues/issues/224)
- [Waking up from sleep on Ubuntu 22.04 is not 100% reliable (Dasharo issue #205)](https://github.com/Dasharo/dasharo-issues/issues/205)
- [The power LED is not always blinking while in sleep mode on Windows 11 (Dasharo issue #182)](https://github.com/Dasharo/dasharo-issues/issues/182)
- [No video output via USB-C after shutdown if PowerDelivery (PD) is active NV40MZ  (Dasharo issue #237)](https://github.com/Dasharo/dasharo-issues/issues/237)
- [Buggy touchpad when charging via USB-C (NV40MZ)  (Dasharo issue #265)](https://github.com/Dasharo/dasharo-issues/issues/265)
- [Keyboard backlight turns on after resuming from sleep mode  (Dasharo issue #332)](https://github.com/Dasharo/dasharo-issues/issues/332)
- [The screen brightness level gets stuck when key are held or pressed too fast (Dasharo issue #341)](https://github.com/Dasharo/dasharo-issues/issues/341)
- [Connecting and immediately disconnecting the charger, sets the battery status in OS to 'charging' for about 2 minutes (Dasharo issue #350)](https://github.com/Dasharo/dasharo-issues/issues/350)

### Binaries

[novacustom_nv4x_tgl_ec_v1.4.0.rom][novacustom_nv4x_tgl_ec_v1.4.0.rom_file]{.md-button}
[sha256][novacustom_nv4x_tgl_ec_v1.4.0.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_tgl_ec_v1.4.0.rom_sig]{.md-button}

[novacustom_nv4x_tgl_v1.4.0.rom][novacustom_nv4x_tgl_v1.4.0.rom_file]{.md-button}
[sha256][novacustom_nv4x_tgl_v1.4.0.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_tgl_v1.4.0.rom_sig]{.md-button}

[novacustom_nv4x_tgl_v1.5.0_dev_signed.rom][novacustom_nv4x_tgl_v1.5.0_dev_signed.rom_file]{.md-button}
[sha256][novacustom_nv4x_tgl_v1.5.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_tgl_v1.5.0_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 1a8eb6c02103727431ac1ea23f4f507e49f3cde7 revision 636f432a](https://github.com/Dasharo/coreboot/tree/636f432a)
- [Dasharo EDKII fork based on e0334c228ce4ba51f47ff79a118f214031d4650f revision 2c61576a](https://github.com/Dasharo/edk2/tree/2c61576a)
- Intel ME version 15.0.30.1776

[novacustom_nv4x_tgl_ec_v1.4.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.4.0/novacustom_nv4x_tgl_ec_v1.4.0.rom
[novacustom_nv4x_tgl_ec_v1.4.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.4.0/novacustom_nv4x_tgl_ec_v1.4.0.rom.sha256
[novacustom_nv4x_tgl_ec_v1.4.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.4.0/novacustom_nv4x_tgl_ec_v1.4.0.rom.sha256.sig
[novacustom_nv4x_tgl_v1.4.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.4.0/novacustom_nv4x_tgl_v1.4.0.rom
[novacustom_nv4x_tgl_v1.4.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.4.0/novacustom_nv4x_tgl_v1.4.0.rom.sha256
[novacustom_nv4x_tgl_v1.4.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.4.0/novacustom_nv4x_tgl_v1.4.0.rom.sha256.sig
[novacustom_nv4x_tgl_v1.5.0_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.5.0/novacustom_nv4x_tgl_v1.5.0_dev_signed.rom
[novacustom_nv4x_tgl_v1.5.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.5.0/novacustom_nv4x_tgl_v1.5.0_dev_signed.rom.sha256
[novacustom_nv4x_tgl_v1.5.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_tgl/v1.5.0/novacustom_nv4x_tgl_v1.5.0_dev_signed.rom.sha256.sig

## v1.3.0 - 2022-10-18

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit#gid=1695997523).

### EC firmware transition

Please note, that version 1.3.0 of `Dasharo BIOS firmware` works correctly
**only** with the `Dasharo EC firmware`. This is the first release when this
open-source EC firmware is used, so additional steps need to be taken when
upgrading.

Please refer to the [Firmware update](/unified/novacustom/firmware-update)
section for more details on upgrading your firmware.

### Added

- [Vboot recovery mode information popup](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)
- [Dasharo setup menu full screen mode support](https://github.com/Dasharo/dasharo-issues/issues/118)

### Changed

- [Rebased on upstream coreboot revision from 18 Aug 2022](https://github.com/Dasharo/coreboot/commits/1a8eb6c0)
- [Support for open-source EC firmware (transition procedure is required)](https://docs.dasharo.com/dasharo-tools-suite/documentation#ec-transition)
- [Disabled UEFI Secure Boot by default](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)

### Fixed

- [Custom fan curve is not applied after suspend (Dasharo issue #45)](https://github.com/Dasharo/dasharo-issues/issues/45)
- [The touchpad ON/OFF switch Fn key is not functional (Dasharo issue #38)](https://github.com/Dasharo/dasharo-issues/issues/38)
- [UCM-UCSI ACPI device displays an error in Windows Device Manager](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/19)
- [Laptop cannot output video via the Tunderbolt 4 USB Type-C port](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/7)

### Known issues

- [Low level interfering crackling/popping of the speakers while playing no sound (Dasharo issue #224)](https://github.com/Dasharo/dasharo-issues/issues/224)
- [Waking up from sleep on Ubuntu 22.04 is not 100% reliable (Dasharo issue #205)](https://github.com/Dasharo/dasharo-issues/issues/205)
- [After emergency shutdown, keyboard doesn't work before OS (Dasharo issue #199)](https://github.com/Dasharo/dasharo-issues/issues/199)
- [The power LED is not always blinking while in sleep mode on Windows 11 (Dasharo issue #182)](https://github.com/Dasharo/dasharo-issues/issues/182)
- [The NVIDIA graphics power management isn't properly functional (Dasharo issue #145)](https://github.com/Dasharo/dasharo-issues/issues/145)

### Binaries

[novacustom_nv4x_ec_v1.3.0.rom][novacustom_nv4x_ec_v1.3.0.rom_file]{.md-button}
[sha256][novacustom_nv4x_ec_v1.3.0.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_ec_v1.3.0.rom_sig]{.md-button}

[novacustom_nv4x_v1.3.0.rom][novacustom_nv4x_v1.3.0.rom_file]{.md-button}
[sha256][novacustom_nv4x_v1.3.0.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_v1.3.0.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on bcc2fb719aaf2d466f9fb429b892f2d268bed5a7 revision a087c3e2](https://github.com/Dasharo/coreboot/tree/a087c3e2)
- [Dasharo EDKII fork based on e0334c228ce4ba51f47ff79a118f214031d4650f revision abfdef40](https://github.com/Dasharo/edk2/tree/abfdef40)

[novacustom_nv4x_ec_v1.3.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x/v1.3.0/novacustom_nv4x_ec_v1.3.0.rom
[novacustom_nv4x_ec_v1.3.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x/v1.3.0/novacustom_nv4x_ec_v1.3.0.rom.sha256
[novacustom_nv4x_ec_v1.3.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x/v1.3.0/novacustom_nv4x_ec_v1.3.0.rom.sha256.sig
[novacustom_nv4x_v1.3.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x/v1.3.0/novacustom_nv4x_v1.3.0.rom
[novacustom_nv4x_v1.3.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x/v1.3.0/novacustom_nv4x_v1.3.0.rom.sha256
[novacustom_nv4x_v1.3.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x/v1.3.0/novacustom_nv4x_v1.3.0.rom.sha256.sig

## v1.2.1 - 2022-06-23

### Fixed

- cbfstool logo replacement not working on NV4x v1.2.0

### Known issues

- [Custom fan curve is not applied after suspend (Dasharo issue #45)](https://github.com/Dasharo/dasharo-issues/issues/45)
- [UCM-UCSI ACPI device displays an error in Windows Device Manager](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/19)
- [USB4 Root Device Router device displays an error in Windows 11 Device Manager](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/18)
- [Windows 10 SD card reader driver needs manual installation on NV41MB](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/16)
- [Low level interfering crackling/popping of the speakers while playing no sound](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/13)
- [Laptop cannot output video via the Tunderbolt 4 USB Type-C port](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/7)

### Binaries

[novacustom_nv4x_v1.2.1.rom][v1.2.1_rom]{ .md-button }
[sha256][v1.2.1_sha]{ .md-button }
[sha256.sig][v1.2.1_sig]{ .md-button }

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

[v1.2.1_rom]:https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x/v1.2.1/novacustom_nv4x_v1.2.1.rom
[v1.2.1_sha]:https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x/v1.2.1/novacustom_nv4x_v1.2.1.rom.sha256
[v1.2.1_sig]:https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x/v1.2.1/novacustom_nv4x_v1.2.1.rom.sha256.sig

### SBOM (Software Bill of Materials)

- [coreboot based on e3e965b1 revision baada726](https://github.com/Dasharo/coreboot/tree/baada726)
- [edk2 based on 2020.03.17 revision cad23725](https://github.com/Dasharo/edk2/tree/cad23725)

## v1.2.0 - 2022-06-10

### Added

- Renamed device to NovaCustom NV4x

### Fixed

- Wake from suspend doesn't work with certain SSDs
- CVE-2022-29264 SMM loader vulnerability
- Fix BIOS vendor name in SMBIOS

### Known issues

- [Custom fan curve is not applied after suspend (Dasharo issue #45)](https://github.com/Dasharo/dasharo-issues/issues/45)
- [UCM-UCSI ACPI device displays an error in Windows Device Manager](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/19)
- [USB4 Root Device Router device displays an error in Windows 11 Device Manager](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/18)
- [Windows 10 SD card reader driver needs manual installation on NV41MB](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/16)
- [Low level interfering crackling/popping of the speakers while playing no sound](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/13)
- [Laptop cannot output video via the Tunderbolt 4 USB Type-C port](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/7)

### Binaries

[novacustom_nv4x_v1.2.0.rom][v1.2.0_rom]{ .md-button }
[sha256][v1.2.0_sha]{ .md-button }
[sha256.sig][v1.2.0_sig]{ .md-button }

[v1.2.0_rom]:https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x/v1.2.0/novacustom_nv4x_v1.2.0.rom
[v1.2.0_sha]:https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x/v1.2.0/novacustom_nv4x_v1.2.0.rom.sha256
[v1.2.0_sig]:https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x/v1.2.0/novacustom_nv4x_v1.2.0.rom.sha256.sig

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on e3e965b1 revision baada726](https://github.com/Dasharo/coreboot/tree/baada726)
- [edk2 based on 2020.03.17 revision cad23725](https://github.com/Dasharo/edk2/tree/cad23725)

## v1.1.0 - 2022-03-23

### Added

- Add Dasharo Tools Suite network boot integration
- Add a persistent bootlogo implementation

### Known issues

- [UCM-UCSI ACPI device displays an error in Windows Device Manager](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/19)
- [USB4 Root Device Router device displays an error in Windows 11 Device Manager](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/18)
- [Windows 10 SD card reader driver needs manual installation on NV41MB](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/16)
- [Low level interfering crackling/popping of the speakers while playing no sound](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/13)
- [Laptop cannot output video via the Tunderbolt 4 USB Type-C port](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/7)

### Binaries

[clevo_nv41mz_v1.1.0.rom][v1.1.0_rom]{ .md-button }
[sha256][v1.1.0_sha]{ .md-button }
[sha256.sig][v1.1.0_sig]{ .md-button }

[v1.1.0_rom]:https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.1.0.rom
[v1.1.0_sha]:https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.1.0.rom.sha256
[v1.1.0_sig]:https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.1.0.rom.sha256.sig

### SBOM (Software Bill of Materials)

- [coreboot based on ae9a8447 revision 0722fdf0](https://github.com/Dasharo/coreboot/tree/0722fdf0)
- [edk2 based on 2020.03.17 revision ec6805c2](https://github.com/Dasharo/edk2/tree/ec6805c2)

## v1.0.1 - 2022-03-01

### Added

- Change DMI fields to match previous Insyde firmware
- Hide unknown ACPI devices
- Set correct Realtek HD Audio subsystem ID
- Set correct ACPI path for the TPM
- Set TPM IRQ in a manner understood by Windows

### Removed

- Removed proprietary blobs from built coreboot images

### Fixed

- Updating firmware using fwupd
- MIC-in phone jack not working
- This PC can't run Windows 11 error while installing Windows 11 from a USB pen drive

### Known issues

- [Custom fan curve is not functional after suspend](https://github.com/Dasharo/dasharo-issues/issues/45)
- [UCM-UCSI ACPI device displays an error in Windows Device Manager](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/19)
- [USB4 Root Device Router device displays an error in Windows 11 Device Manager](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/18)
- [Windows 10 SD card reader driver needs manual installation on NV41MB](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/16)
- [Low level interfering crackling/popping of the speakers while playing no sound](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/13)
- [Laptop cannot output video via the Tunderbolt 4 USB Type-C port](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/7)

### Binaries

[clevo_nv41mz_v1.0.1.rom][v1.0.1_rom]{ .md-button }
[sha256][v1.0.1_sha]{ .md-button }
[sha256.sig][v1.0.1_sig]{ .md-button }

[v1.0.1_rom]:https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.0.1.rom
[v1.0.1_sha]:https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.0.1.rom.sha256
[v1.0.1_sig]:https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.0.1.rom.sha256.sig

### SBOM (Software Bill of Materials)

- [coreboot based on ae9a8447 revision 3a3808f9](https://github.com/Dasharo/coreboot/tree/3a3808f9)
- [edk2 based on 2020.03.17 revision e0334c22](https://github.com/Dasharo/edk2/tree/e0334c22)

## v1.0.0 - 2022-01-19

### Added

- Documentation for touchpad hotkey enablement on Linux

### Removed

- Removed proprietary blobs from built coreboot images

### Fixed

- The touchpad ON/OFF switch Fn key is not functional
- Charging indicator displays wrong state if power adapter was unplugged while
  in sleep mode
- Bluetooth does not work under Windows

### Known issues

- [Unable to download the system by using iPXE](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/8)
- [Laptop cannot output video via the Tunderbolt 4 USB Type-C port](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/7)
- [Windows 10 SD card reader driver needs manual installation on NV41MB](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/16)

### Binaries

[clevo_nv41mz_v1.0.0.rom][v1.0.0_rom]{ .md-button }
[sha256][v1.0.0_sha]{ .md-button }
[sha256.sig][v1.0.0_sig]{ .md-button }

[v1.0.0_rom]:https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.0.0.rom
[v1.0.0_sha]:https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.0.0.rom.sha256
[v1.0.0_sig]:https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.0.0.rom.sha256.sig

### SBOM (Software Bill of Materials)

- [coreboot based on ae9a8447 revision e995fc1c](https://github.com/Dasharo/coreboot/commit/e995fc1c)
- [edk2 based on 2020.03.17 revision 59ae285f](https://github.com/Dasharo/edk2/tree/59ae285f)

## v0.5.0 - 2021-11-19

### Added

- vboot Verified Boot
- TPM Measured Boot
- Custom fan curve
- Microcode for Tiger Lake stepping 0x2
- Documentation for EC firmware update

### Changed

- Disabled unused DPTF device

### Fixed

- [Performance drop when the power adaptor is disconnected](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/5)
- [High Nvidia GPU energy draw at idle in Windows](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/6)

### Known issues

- [Unable to download the system by using iPXE](https://github.com/Dasharo/dasharo-issues/issues/40)
- [Laptop cannot output video via the Tunderbolt 4 USB Type-C port](https://github.com/Dasharo/dasharo-issues/issues/39)
- [The touchpad ON/OFF switch Fn key is not functional](https://github.com/Dasharo/dasharo-issues/issues/38)

### Binaries

[dasharo_clevo_nv41mz_v0.5.0.rom][v0.5.0_rom]{ .md-button }
[sha256][v0.5.0_sha]{ .md-button }
[sha256.sig][v0.5.0_sig]{ .md-button }

[v0.5.0_rom]:https://cloud.3mdeb.com/index.php/s/ywZtKFR3J3Y3sbG
[v0.5.0_sha]:https://cloud.3mdeb.com/index.php/s/6BeLRkSaawB42T6
[v0.5.0_sig]:https://cloud.3mdeb.com/index.php/s/xM8FcCsMc8kfmKB

### SBOM (Software Bill of Materials)

- [coreboot based on ae9a8447 revision 7d439573](https://gitlab.com/novacustom/coreboot/-/tree/7d439573)
- [EDK2 based on 2020.03.17 revision bfd3d1a2](https://github.com/Dasharo/edk2/tree/bfd3d1a2)

## v0.4.0 - 2021-10-26

### Added

- Added full support for sleep mode (s0ix / Modern Standby)
- Added support for NV41MB model
- Added support for nvidia discrete graphics (doesn't power off in Windows yet)

### Changed

- Fixed regression with non-funtional airplane mode hotkey on Windows
- Disabled legacy 8254 timer for lower power draw

### Fixed

- [Sleep mode is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/3)
- [The camera ON/OFF switch Fn key is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/2)

### Known issues

- [Unable to download the system by using iPXE](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/8)
- [Laptop cannot output video via the Tunderbolt 4 USB Type-C port](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/7)
- [High Nvidia GPU energy draw at idle in Windows](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/6)
- [Performance drop when the power adaptor is disconnected](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/5)
- [The touchpad ON/OFF switch Fn key is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/1)

### Binaries

[dasharo_clevo_nv41mz_v0.4.0.rom][v0.4.0_rom]{ .md-button }
[sha256][v0.4.0_sha]{ .md-button }
[sha256.sig][v0.4.0_sig]{ .md-button }

[v0.4.0_rom]:https://cloud.3mdeb.com/index.php/s/MZnCrbWqaKPc8st
[v0.4.0_sha]:https://cloud.3mdeb.com/index.php/s/2SkwmGFoyAf2e7d
[v0.4.0_sig]:https://cloud.3mdeb.com/index.php/s/HZxynzX3zDscTXr

### SBOM (Software Bill of Materials)

- [coreboot based on ae9a8447 revision 03972293](https://gitlab.com/novacustom/coreboot/-/tree/03972293)
- [EDK2 based on 2020.03.17 revision bfd3d1a2](https://github.com/Dasharo/edk2/tree/bfd3d1a2)

## v0.3.0 - 2021-10-11

### Added

- Support for discrete TPM
- USB Type-C ACPI support (UCSI)
- Improved runtime power management for SSD (reduces power usage while in sleep)
- Added partial sleep support (system saves power, but fans still spin)

### Changed

- Rebased on coreboot revision ae9a8447

### Known issues

- [Sleep mode is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/3)
- [The camera ON/OFF switch Fn key is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/2)
- [The touchpad ON/OFF switch Fn key is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/1)

### Binaries

[dasharo_clevo_nv41mz_v0.3.0.rom][v0.3.0_rom]{ .md-button }
[sha256][v0.3.0_sha]{ .md-button }
[sha256.sig][v0.3.0_sig]{ .md-button }

[v0.3.0_rom]:https://cloud.3mdeb.com/index.php/s/D7atioMH5Ega6JZ
[v0.3.0_sha]:https://cloud.3mdeb.com/index.php/s/j7RxnDWEzreD6w3
[v0.3.0_sig]:https://cloud.3mdeb.com/index.php/s/NLbgZiyiMFRyZt7

### SBOM (Software Bill of Materials)

- [coreboot based on ae9a8447 revision v0.3.0](https://gitlab.com/novacustom/coreboot/-/tree/v0.3.0)
- [EDK2 based on 2020.03.17 revision bfd3d1a2](https://github.com/Dasharo/edk2/tree/bfd3d1a2)

## v0.2.1 - 2021-9-29

### Added

- Integrated graphics backlight configuration for Windows

### Changed

- Updated the Video Bios Table

### Fixed

- [Screen brightness is stuck at 0% in the Windows Installer](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/4)

### Known issues

- [Sleep mode is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/3)
- [The camera ON/OFF switch Fn key is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/2)
- [The touchpad ON/OFF switch Fn key is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/1)

### Binaries

[dasharo_clevo_nv41mz_v0.2.1.rom][v0.2.1_rom]{ .md-button }
[sha256][v0.2.1_sha]{ .md-button }
[sha256.sig][v0.2.1_sig]{ .md-button }

[v0.2.1_rom]:https://cloud.3mdeb.com/index.php/s/9f9S9zNHZDYW8NM
[v0.2.1_sha]:https://cloud.3mdeb.com/index.php/s/q7aZz4LFA6B5byD
[v0.2.1_sig]:https://cloud.3mdeb.com/index.php/s/YnNXcyQyfKkabDG

### SBOM (Software Bill of Materials)

- [coreboot based on 4.14 revision 43c9604b](https://gitlab.com/novacustom/coreboot/-/tree/43c9604b)
- [EDK2 based on 2020.03.17 revision bfd3d1a2](https://github.com/Dasharo/edk2/tree/bfd3d1a2)

## v0.2.0 - 2021-9-24

### Added

- UEFI Secure Boot support
- UEFI Shell selectable in boot menu
- iPXE selectable in boot menu
- NovaCustom boot logo
- Customized boot menu keys
- Customized setup menu keys
- Support for backlight hotkey in Windows
- Preserve boot order settings after Dasharo update

### Changed

- Replaced CorebootPayloadPkg with Dasharo UEFIPayloadPkg
- Changed the behavior of airplane mode to match stock firmware (now it can be
  disabled in software)

### Known issues

- [Screen brightness is stuck at 0% in the Windows Installer](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/4)
- [Sleep mode is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/3)
- [The camera ON/OFF switch Fn key is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/2)
- [The touchpad ON/OFF switch Fn key is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/1)

### Binaries

[dasharo_clevo_nv41mz_v0.2.0.rom][v0.2.0_rom]{ .md-button }
[sha256][v0.2.0_sha]{ .md-button }
[sha256.sig][v0.2.0_sig]{ .md-button }

[v0.2.0_rom]:https://cloud.3mdeb.com/index.php/s/BnWwH7X8RYinm7x
[v0.2.0_sha]:https://cloud.3mdeb.com/index.php/s/xrwfNdC9PnfoMEL
[v0.2.0_sig]:https://cloud.3mdeb.com/index.php/s/yWitrxMRrCHYPE4

### SBOM (Software Bill of Materials)

- [coreboot based on 4.14 revision ff1c6572](https://gitlab.com/novacustom/coreboot/-/tree/ff1c6572)
- [EDK2 based on 2020.03.17 revision bfd3d1a2](https://github.com/Dasharo/edk2/tree/bfd3d1a2)

## v0.1.2 - 2021-08-31

### Added

- Clevo NV41MZ platform support
- Clevo IT5570 EC support
- UEFI boot support
- configurable boot order
- configurable boot options
- Integrated graphics initialization for internal LCD (eDP) and external HDMI
  port

### Binaries

[clevo_nv41mz_v0.1.2.rom][v0.1.2_rom]{ .md-button }
[sha256][v0.1.2_sha]{ .md-button }
[sha256.sig][v0.1.2_sig]{ .md-button }

[All in one zip][v0.1.2_aio]

[v0.1.2_rom]:https://cloud.3mdeb.com/index.php/s/zzWBdLkF78Ax6pP/download
[v0.1.2_sha]:https://cloud.3mdeb.com/index.php/s/mYzWRma6CYQpZg6/download
[v0.1.2_sig]:https://cloud.3mdeb.com/index.php/s/d6bsNzpnWyqLbqC/download
[v0.1.2_aio]:https://cloud.3mdeb.com/index.php/s/LXQizpTxg7C9g94/download

### SBOM (Software Bill of Materials)

- [coreboot 4.14 (with additional commits for Clevo NV41MZ board support)](https://gitlab.com/novacustom/coreboot/-/compare/4.14...v0.1.1?from_project_id=29249618)
- [EDK2](https://github.com/MrChromebox/edk2/commit/659ed4cb983a66ec241c05f42b69ad4d2e47b714)

[newsletter]: https://newsletter.3mdeb.com/subscription/S5ze5u_qN
