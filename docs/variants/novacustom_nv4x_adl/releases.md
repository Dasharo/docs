# NovaCustom NV4x 12th Gen Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
NovaCustom NV4x 12th Gen

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("310eac18-d302-478f-a617-5f5d65e8e0ac",
"Subscribe to NovaCustom NV4x 12th Gen Dasharo Release Newsletter") }}

## v1.7.2 - 2024-01-03

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit#gid=1371018314).

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
- [Noise caused by coil whine](https://github.com/Dasharo/dasharo-issues/issues/628)
- [Low level interfering crackling/popping of the speakers while playing no sound](https://github.com/Dasharo/dasharo-issues/issues/224)
- [ACPI error during boot (system76_acpi::kbd_backlight)](https://github.com/Dasharo/dasharo-issues/issues/559)
- [Thunderbolt may not work after wakeup from sleep](https://github.com/Dasharo/dasharo-issues/issues/629)
- [Unnecessary security warning after firmware update](https://github.com/Dasharo/dasharo-issues/issues/556)
- [Early boot DMA protection setting in UEFI does not work correctly](https://github.com/Dasharo/dasharo-issues/issues/630)

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

### Binaries

[novacustom_nv4x_adl_ec_v1.7.2.rom][novacustom_nv4x_adl_ec_v1.7.2.rom_file]{.md-button}
[sha256][novacustom_nv4x_adl_ec_v1.7.2.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_ec_v1.7.2.rom_sig]{.md-button}

[novacustom_nv4x_adl_v1.7.2.rom][novacustom_nv4x_adl_v1.7.2.rom_file]{.md-button}
[sha256][novacustom_nv4x_adl_v1.7.2.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_v1.7.2.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 4.21 revision cb6ef1b9](https://github.com/Dasharo/coreboot/tree/cb6ef1b9)
- [Dasharo EDKII fork based on edk2-stable202002 revision b7274c98](https://github.com/Dasharo/edk2/tree/b7274c98)

[newsletter]: https://3mdeb.com/subscribe/nc_nv4x_12th.html
[novacustom_nv4x_adl_ec_v1.7.2.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.2/novacustom_nv4x_adl_ec_v1.7.2.rom
[novacustom_nv4x_adl_ec_v1.7.2.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.2/novacustom_nv4x_adl_ec_v1.7.2.rom.sha256
[novacustom_nv4x_adl_ec_v1.7.2.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.2/novacustom_nv4x_adl_ec_v1.7.2.rom.sha256.sig
[novacustom_nv4x_adl_v1.7.2.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.2/novacustom_nv4x_adl_v1.7.2.rom
[novacustom_nv4x_adl_v1.7.2.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.2/novacustom_nv4x_adl_v1.7.2.rom.sha256
[novacustom_nv4x_adl_v1.7.2.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.2/novacustom_nv4x_adl_v1.7.2.rom.sha256.sig

## v1.7.1 - 2023-11-06

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1LOXY9HCu-fMitkYwX08iLsQdSNenzyU0LnMdVbZB5Do/edit#gid=1371018314).

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
- [Block boot when battery is too low](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/359-boot-blocking/#test-cases-common-documentation)
- [Power on AC option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- Firmware display on external monitor when lid is closed

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

### Binaries

[novacustom_nv4x_adl_ec_v1.7.1.rom][novacustom_nv4x_adl_ec_v1.7.1.rom_file]{.md-button}
[sha256][novacustom_nv4x_adl_ec_v1.7.1.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_ec_v1.7.1.rom_sig]{.md-button}

[novacustom_nv4x_adl_v1.7.1.rom][novacustom_nv4x_adl_v1.7.1.rom_file]{.md-button}
[sha256][novacustom_nv4x_adl_v1.7.1.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_v1.7.1.rom_sig]{.md-button}

[novacustom_nv4x_adl_v1.7.1_dev_signed.rom][novacustom_nv4x_adl_v1.7.1_dev_signed.rom_file]{.md-button}
[sha256][novacustom_nv4x_adl_v1.7.1_dev_signed.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_v1.7.1_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 4.21 revision 36032e55](https://github.com/Dasharo/coreboot/tree/36032e55)
- [Dasharo EDKII fork based on edk2-stable202002 revision b68e46b0](https://github.com/Dasharo/edk2/tree/b68e46b0)

[novacustom_nv4x_adl_ec_v1.7.1.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.1/novacustom_nv4x_adl_ec_v1.7.1.rom
[novacustom_nv4x_adl_ec_v1.7.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.1/novacustom_nv4x_adl_ec_v1.7.1.rom.sha256
[novacustom_nv4x_adl_ec_v1.7.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.1/novacustom_nv4x_adl_ec_v1.7.1.rom.sha256.sig
[novacustom_nv4x_adl_v1.7.1.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.1/novacustom_nv4x_adl_v1.7.1.rom
[novacustom_nv4x_adl_v1.7.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.1/novacustom_nv4x_adl_v1.7.1.rom.sha256
[novacustom_nv4x_adl_v1.7.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.1/novacustom_nv4x_adl_v1.7.1.rom.sha256.sig
[novacustom_nv4x_adl_v1.7.1_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.1/novacustom_nv4x_adl_v1.7.1_dev_signed.rom
[novacustom_nv4x_adl_v1.7.1_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.1/novacustom_nv4x_adl_v1.7.1_dev_signed.rom.sha256
[novacustom_nv4x_adl_v1.7.1_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.7.1/novacustom_nv4x_adl_v1.7.1_dev_signed.rom.sha256.sig

## v1.6.0 - 2023-04-19

### Added

- [Intel Management Engine Disable](https://github.com/Dasharo/dasharo-issues/issues/111)
- [The same keyboard illumination setting is restored after suspend or poweroff](https://github.com/Dasharo/dasharo-issues/issues/339)
- [One of the two fan profiles can now be selected in Setup Menu](https://docs.dasharo.com/unified/novacustom/features/)
- [Fn lock hotkey feature](https://docs.dasharo.com/unified/novacustom/features/)
- [Setup menu option for switching between S0ix and S3 suspend mode](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)

### Changed

- [Keys must be provisioned prior enabling Secure Boot](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
- The function keys responsible for entering the setup and boot menu in BIOS
  have been changed from ESC/F12 to F2/F7

### Fixed

- [The power LED is not always blinking while in sleep mode on Ubuntu 22.04 (#260)](https://github.com/Dasharo/dasharo-issues/issues/260)
- [Suspend mode not working under Qubes OS 4.1 (#266)](https://github.com/Dasharo/dasharo-issues/issues/266)
- [Docking station under Qubes OS (#267)](https://github.com/Dasharo/dasharo-issues/issues/267)
- [The Auto Boot time-out value is not respected (#292)](https://github.com/Dasharo/dasharo-issues/issues/292)
- [ACPI boot errors during booting Ubuntu 22.04 (#293)](https://github.com/Dasharo/dasharo-issues/issues/293)
- [Windows update KB5012170 cannot be installed (#294)](https://github.com/Dasharo/dasharo-issues/issues/294)
- [Internal keyboard sometimes does not work in firmware (#295)](https://github.com/Dasharo/dasharo-issues/issues/295)
- [Laptop hangs up after 20 cycles of the suspend procedure (#305)](https://github.com/Dasharo/dasharo-issues/issues/305)
- [Keyboard backlight not working after restart (#349)](https://github.com/Dasharo/dasharo-issues/issues/349)
- [Function key display on/off does not completely blank the screen (#354)](https://github.com/Dasharo/dasharo-issues/issues/354)
- [Connecting the RJ45 cable to the Gigabit Ethernet port on the docking station does not result in obtaining an Internet connection (#356)](https://github.com/Dasharo/dasharo-issues/issues/356)
- [Unable to wake up from suspend (#362)](https://github.com/Dasharo/dasharo-issues/issues/362)

### Known issues

- [The power LED is not always blinking while in sleep mode on Windows 11 (#182)](https://github.com/Dasharo/dasharo-issues/issues/182)
- [Popup with information about recovery mode is displayed after flashing with a valid binary (#269)](https://github.com/Dasharo/dasharo-issues/issues/269)
- [Missing information about cache (#343)](https://github.com/Dasharo/dasharo-issues/issues/343)
- [Connecting and immediately disconnecting the charger, sets the battery status in OS to charging for about 2 minutes (#350)](https://github.com/Dasharo/dasharo-issues/issues/350)
- [Reset to defaults with F9 causes the wrong settings to be restored (#355)](https://github.com/Dasharo/dasharo-issues/issues/355)
- [Unwanted reset of BIOS settings (#365)](https://github.com/Dasharo/dasharo-issues/issues/365)
- [Laptop not suspending while connected to a USB-C docking station (#368)](https://github.com/Dasharo/dasharo-issues/issues/368)
- [The docking station is not detected after cold-boot and warm-boot (#404)](https://github.com/Dasharo/dasharo-issues/issues/404)

### Binaries

[novacustom_nv4x_adl_ec_v1.6.0.rom][novacustom_nv4x_adl_ec_v1.6.0.rom_file]{.md-button}
[sha256][novacustom_nv4x_adl_ec_v1.6.0.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_ec_v1.6.0.rom_sig]{.md-button}

[novacustom_nv4x_adl_v1.6.0.rom][novacustom_nv4x_adl_v1.6.0.rom_file]{.md-button}
[sha256][novacustom_nv4x_adl_v1.6.0.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_v1.6.0.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 1a8eb6c02103727431ac1ea23f4f507e49f3cde7 revision a3056ac5](https://github.com/Dasharo/coreboot/tree/a3056ac5)
- [Dasharo EDKII fork based on e0334c228ce4ba51f47ff79a118f214031d4650f revision bd421b40](https://github.com/Dasharo/edk2/tree/bd421b40)
- Intel ME version 16.1.25.1865

[novacustom_nv4x_adl_ec_v1.6.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.6.0/novacustom_nv4x_adl_ec_v1.6.0.rom
[novacustom_nv4x_adl_ec_v1.6.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.6.0/novacustom_nv4x_adl_ec_v1.6.0.rom.sha256
[novacustom_nv4x_adl_ec_v1.6.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.6.0/novacustom_nv4x_adl_ec_v1.6.0.rom.sha256.sig
[novacustom_nv4x_adl_v1.6.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.6.0/novacustom_nv4x_adl_v1.6.0.rom
[novacustom_nv4x_adl_v1.6.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.6.0/novacustom_nv4x_adl_v1.6.0.rom.sha256
[novacustom_nv4x_adl_v1.6.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.6.0/novacustom_nv4x_adl_v1.6.0.rom.sha256.sig

## v1.5.0 - Non-public engineering release

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
- [Open-source Embedded Controller Firmware](https://docs.dasharo.com/unified/novacustom/recovery/#ec-firmware-recovery)

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

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 1a8eb6c02103727431ac1ea23f4f507e49f3cde7 revision cd975d74](https://github.com/Dasharo/coreboot/tree/cd975d74)
- [Dasharo EDKII fork based on e0334c228ce4ba51f47ff79a118f214031d4650f revision abfdef40](https://github.com/Dasharo/edk2/tree/abfdef40)

[novacustom_nv4x_adl_ec_v1.4.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.4.0/novacustom_nv4x_adl_ec_v1.4.0.rom
[novacustom_nv4x_adl_ec_v1.4.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.4.0/novacustom_nv4x_adl_ec_v1.4.0.rom.sha256
[novacustom_nv4x_adl_ec_v1.4.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.4.0/novacustom_nv4x_adl_ec_v1.4.0.rom.sha256.sig
[novacustom_nv4x_adl_v1.4.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.4.0/novacustom_nv4x_adl_v1.4.0.rom
[novacustom_nv4x_adl_v1.4.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.4.0/novacustom_nv4x_adl_v1.4.0.rom.sha256
[novacustom_nv4x_adl_v1.4.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/v1.4.0/novacustom_nv4x_adl_v1.4.0.rom.sha256.sig
