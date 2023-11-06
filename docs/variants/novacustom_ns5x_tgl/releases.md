# NovaCustom NS5x/7x 11th Gen Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
NovaCustom NS5x/7x 11th Gen

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

[Subscribe to NovaCustom NS5x/7x 11th Gen Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

</center>

## v1.5.0 - 2023-10-30

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit#gid=38447675).

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

[novacustom_ns5x_tgl_ec_v1.5.0.rom][novacustom_ns5x_tgl_ec_v1.5.0.rom_file]{.md-button}
[sha256][novacustom_ns5x_tgl_ec_v1.5.0.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_tgl_ec_v1.5.0.rom_sig]{.md-button}

[novacustom_ns5x_tgl_v1.5.0.rom][novacustom_ns5x_tgl_v1.5.0.rom_file]{.md-button}
[sha256][novacustom_ns5x_tgl_v1.5.0.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_tgl_v1.5.0.rom_sig]{.md-button}

[novacustom_ns5x_tgl_v1.5.0_dev_signed.rom][novacustom_ns5x_tgl_v1.5.0_dev_signed.rom_file]{.md-button}
[sha256][novacustom_ns5x_tgl_v1.5.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][novacustom_ns5x_tgl_v1.5.0_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 4.21 revision 36032e55](https://github.com/Dasharo/coreboot/tree/36032e55)
- [Dasharo EDKII fork based on edk2-stable202002 revision b68e46b0](https://github.com/Dasharo/edk2/tree/b68e46b0)

[novacustom_ns5x_tgl_ec_v1.5.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.0/novacustom_ns5x_tgl_ec_v1.5.0.rom
[novacustom_ns5x_tgl_ec_v1.5.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.0/novacustom_ns5x_tgl_ec_v1.5.0.rom.sha256
[novacustom_ns5x_tgl_ec_v1.5.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.0/novacustom_ns5x_tgl_ec_v1.5.0.rom.sha256.sig
[novacustom_ns5x_tgl_v1.5.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.0/novacustom_ns5x_tgl_v1.5.0.rom
[novacustom_ns5x_tgl_v1.5.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.0/novacustom_ns5x_tgl_v1.5.0.rom.sha256
[novacustom_ns5x_tgl_v1.5.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.0/novacustom_ns5x_tgl_v1.5.0.rom.sha256.sig
[novacustom_ns5x_tgl_v1.5.0_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.0/novacustom_ns5x_tgl_v1.5.0_dev_signed.rom
[novacustom_ns5x_tgl_v1.5.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.0/novacustom_ns5x_tgl_v1.5.0_dev_signed.rom.sha256
[novacustom_ns5x_tgl_v1.5.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_ns5x_tgl/v1.5.0/novacustom_ns5x_tgl_v1.5.0_dev_signed.rom.sha256.sig

## v1.4.0 - 2023-03-02

### Added

- [The same keyboard illumination setting is restored after suspend or poweroff](https://github.com/Dasharo/dasharo-issues/issues/339)
- [One of the two fan profiles can now be selected in Setup Menu](https://docs.dasharo.com/unified/novacustom/fan-profiles/)
- [Fn lock hotkey feature](https://docs.dasharo.com/unified/novacustom/fn-lock-hotkey/)

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
instructions in [Dasharo release signature verification](/guides/signature-verification)
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

Please refer to the [Firmware update](/unified/novacustom/firmware-update)
section for more details on upgrading your firmware.

### Added

- [Enabled Vboot Verified Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)

- Vboot Recovery Popup

- Fullscreen setup menu

### Changed

- Rebased on upstream coreboot revision 1a8eb6c0

- [Support for Open EC Firmware](https://docs.dasharo.com/dasharo-tools-suite/documentation#ec-transition)

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
instructions in [Dasharo release signature verification](/guides/signature-verification)
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
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 4.16 revision b087dcbd](https://github.com/Dasharo/coreboot/tree/b087dcbd)
- [tianocore based on e0334c228ce4ba51f47ff79a118f214031d4650f revision 90364638](https://github.com/Dasharo/edk2/tree/90364638)

## v1.1.0 - 2022-04-22

### Added

- Support for NovaCustom NS7x
- [Support for RGB Keyboard](https://docs.dasharo.com/unified/novacustom/rgb-keyboard/)
- [Persistent boot logo implementation](https://docs.dasharo.com/guides/logo-customization)

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
instructions in [Dasharo release signature verification](/guides/signature-verification)
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

[newsletter]: https://newsletter.3mdeb.com/subscription/RJrTXDhWR
