# Clevo NV41MZ Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development for
Clevo NV41MZ

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

[Subscribe to Clevo NV41MZ Dasharo Release Newsletter](https://newsletter.3mdeb.com/subscription/T61MyO2sP){ .md-button .md-button--primary .center }

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

[clevo_nv41mz_v1.0.1.rom](https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.0.1.rom){ .md-button }
[sha256](https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.0.1.rom.sha256){ .md-button }
[sha256.sig](https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.0.1.rom.sha256.sig){ .md-button }

### SBOM (Software Bill of Materials)

- [coreboot based on ae9a8447 revision 3a3808f9](https://github.com/Dasharo/coreboot/tree/3a3808f9)
- [edk2 based on 2020.03.17 revision e0334c22](https://github.com/Dasharo/edk2/tree/e0334c22)
- [Blobs based on v1.0 revision 39d95913](https://gitlab.com/novacustom/blobs/-/tree/39d95913)

## v1.0.0 - 2022-01-19

### Added

- Documentation for touchpad hotkey enablement on Linux

### Removed

- Removed proprietary blobs from built coreboot images

### Fixed

- The touchpad ON/OFF switch Fn key is not functional
- Charging indicator displays wrong state if power adapter was unplugged while in sleep mode
- Bluetooth does not work under Windows

### Known issues

- [Unable to download the system by using iPXE](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/8)
- [Laptop cannot output video via the Tunderbolt 4 USB Type-C port](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/7)
- [Windows 10 SD card reader driver needs manual installation on NV41MB](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/16)

### Binaries

[clevo_nv41mz_v1.0.0.rom](https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.0.0.rom){ .md-button }
[sha256](https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.0.0.rom.sha256){ .md-button }
[sha256.sig](https://3mdeb.com/open-source-firmware/Dasharo/clevo_nv41mz/clevo_nv41mz_v1.0.0.rom.sha256.sig){ .md-button }

### SBOM (Software Bill of Materials)

- [coreboot based on ae9a8447 revision e995fc1c](https://github.com/Dasharo/coreboot/commit/e995fc1c)
- [edk2 based on 2020.03.17 revision 59ae285f](https://github.com/Dasharo/edk2/tree/59ae285f)
- [Blobs based on v1.0 revision 39d95913](https://gitlab.com/novacustom/blobs/-/tree/39d95913)

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

[dasharo_clevo_nv41mz_0.5.0.SHA256](https://cloud.3mdeb.com/index.php/s/ywZtKFR3J3Y3sbG){ .md-button }
[dasharo_clevo_nv41mz_0.5.0.SHA256.sig](https://cloud.3mdeb.com/index.php/s/6BeLRkSaawB42T6){ .md-button }
[dasharo_clevo_nv41mz_0.5.0.rom](https://cloud.3mdeb.com/index.php/s/xM8FcCsMc8kfmKB){ .md-button }

### SBOM (Software Bill of Materials)

- [coreboot based on ae9a8447 revision 7d439573](https://gitlab.com/novacustom/coreboot/-/tree/7d439573)
- [EDK2 based on 2020.03.17 revision bfd3d1a2](https://github.com/Dasharo/edk2/tree/bfd3d1a2)
- [Blobs based on v1.0 revision 462f0c80](https://gitlab.com/novacustom/blobs/-/tree/462f0c80)

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

- [dasharo_clevo_nv41mz_0.4.0.rom](https://cloud.3mdeb.com/index.php/s/MZnCrbWqaKPc8st){ .md-button }
- [dasharo_clevo_nv41mz_0.4.0.SHA256](https://cloud.3mdeb.com/index.php/s/2SkwmGFoyAf2e7d){ .md-button }
- [dasharo_clevo_nv41mz_0.4.0.SHA256.sig](https://cloud.3mdeb.com/index.php/s/HZxynzX3zDscTXr){ .md-button }

### SBOM (Software Bill of Materials)

- [coreboot based on ae9a8447 revision 03972293](https://gitlab.com/novacustom/coreboot/-/tree/03972293)
- [EDK2 based on 2020.03.17 revision bfd3d1a2](https://github.com/Dasharo/edk2/tree/bfd3d1a2)
- [Blobs based on v1.0 revision 462f0c80](https://gitlab.com/novacustom/blobs/-/tree/462f0c80)

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

- [dasharo_clevo_nv41mz_0.3.0.rom](https://cloud.3mdeb.com/index.php/s/D7atioMH5Ega6JZ){ .md-button }
- [dasharo_clevo_nv41mz_0.3.0.SHA256](https://cloud.3mdeb.com/index.php/s/j7RxnDWEzreD6w3){ .md-button }
- [dasharo_clevo_nv41mz_0.3.0.SHA256.sig](https://cloud.3mdeb.com/index.php/s/NLbgZiyiMFRyZt7){ .md-button }

### SBOM (Software Bill of Materials)

- [coreboot based on ae9a8447 revision v0.3.0](https://gitlab.com/novacustom/coreboot/-/tree/v0.3.0)
- [EDK2 based on 2020.03.17 revision bfd3d1a2](https://github.com/Dasharo/edk2/tree/bfd3d1a2)
- [Blobs based on v1.0 revision 462f0c80](https://gitlab.com/novacustom/blobs/-/tree/462f0c80)

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

- [dasharo_clevo_nv41mz_0.2.1.rom](https://cloud.3mdeb.com/index.php/s/9f9S9zNHZDYW8NM){ .md-button }
- [dasharo_clevo_nv41mz_0.2.1.rom.SHA256](https://cloud.3mdeb.com/index.php/s/q7aZz4LFA6B5byD){ .md-button }
- [dasharo_clevo_nv41mz_0.2.1.rom.SHA256.sig](https://cloud.3mdeb.com/index.php/s/YnNXcyQyfKkabDG){ .md-button }

### SBOM (Software Bill of Materials)

- [coreboot based on 4.14 revision 43c9604b](https://gitlab.com/novacustom/coreboot/-/tree/43c9604b)
- [EDK2 based on 2020.03.17 revision bfd3d1a2](https://github.com/Dasharo/edk2/tree/bfd3d1a2)
- [Blobs based on v1.0 revision 462f0c80](https://gitlab.com/novacustom/blobs/-/tree/462f0c80)

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
- Changed the behavior of airplane mode to match stock firmware (now it can be disabled in software)

### Known issues

- [Screen brightness is stuck at 0% in the Windows Installer](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/4)
- [Sleep mode is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/3)
- [The camera ON/OFF switch Fn key is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/2)
- [The touchpad ON/OFF switch Fn key is not functional](https://gitlab.com/novacustom/dasharo-compatibility/-/issues/1)

### Binaries

- [dasharo_clevo_nv41mz_0.2.0.rom](https://cloud.3mdeb.com/index.php/s/BnWwH7X8RYinm7x){ .md-button }
- [dasharo_clevo_nv41mz_0.2.0.SHA256](https://cloud.3mdeb.com/index.php/s/xrwfNdC9PnfoMEL){ .md-button }
- [dasharo_clevo_nv41mz_0.2.0.SHA256.sig](https://cloud.3mdeb.com/index.php/s/yWitrxMRrCHYPE4){ .md-button }

### SBOM (Software Bill of Materials)

- [coreboot based on 4.14 revision ff1c6572](https://gitlab.com/novacustom/coreboot/-/tree/ff1c6572)
- [EDK2 based on 2020.03.17 revision bfd3d1a2](https://github.com/Dasharo/edk2/tree/bfd3d1a2)
- [Blobs based on v1.0 revision 462f0c80](https://gitlab.com/novacustom/blobs/-/tree/462f0c80)

## v0.1.2 - 2021-08-31

### Added

- Clevo NV41MZ platform support
- Clevo IT5570 EC support
- UEFI boot support
- configurable boot order
- configurable boot options
- Integreated graphics initialization for internal LCD (eDP) and external HDMI
  port

### Binaries

[Clevo NV41MZ Dasharo](https://cloud.3mdeb.com/index.php/s/zzWBdLkF78Ax6pP/download){ .md-button } [SHA256](https://cloud.3mdeb.com/index.php/s/mYzWRma6CYQpZg6/download){ .md-button } [SHA256.sig](https://cloud.3mdeb.com/index.php/s/d6bsNzpnWyqLbqC/download){ .md-button }

[All in one zip](https://cloud.3mdeb.com/index.php/s/LXQizpTxg7C9g94/download){ .md-button }

### SBOM (Software Bill of Materials)

- [coreboot 4.14 (with additional commits for Clevo NV41MZ board support)](https://gitlab.com/novacustom/coreboot/-/compare/4.14...v0.1.1?from_project_id=29249618)
- [EDK2](https://github.com/MrChromebox/edk2/commit/659ed4cb983a66ec241c05f42b69ad4d2e47b714)

#### Binary blobs

- [blobs extracted from the vendor firmware](https://gitlab.com/novacustom/blobs/-/tree/d56dacf5a06881c327e54b0632585402c4c3718d/mainboard/clevo/tgl-u/nv41mz)
