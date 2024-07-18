# NovaCustom V540TU Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
NovaCustom V540TU

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

## v0.9.0 - 2024-07-18

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/NovaCustom/MTL_14th_Gen/V540TU/v0.9.0-results.csv).

### Added

- Support for NovaCustom Meteor Lake platform (integrated graphics)
- [Vboot Verified Boot](https://docs.dasharo.com/common-coreboot-docs/vboot_signing/)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [Vboot recovery notification in UEFI Payload](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)
- [UEFI Shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
- [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [Automatic Embedded Controller update](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31G-ec-and-superio/#ecr031001-ec-firmware-sync-in-coreboot)
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
- [Keyboard backlight level is restored after suspend or poweroff](https://github.com/Dasharo/dasharo-issues/issues/339)
- [Fan profiles in setup Menu](https://docs.dasharo.com/unified/novacustom/fan-profiles/)
- [Fn lock hotkey feature](https://docs.dasharo.com/unified/novacustom/fn-lock-hotkey/)
- [Throttling temperature adjustment in setup menu](https://docs.dasharo.com/unified/novacustom/features/#cpu-throttling-threshold)

### Known issues

- [No HDMI output in FW on V540TU and V560TU](https://github.com/Dasharo/dasharo-issues/issues/930)
- [Laggy behaviour on Manjaro (KDE) with open drivers](https://github.com/Dasharo/dasharo-issues/issues/911)
- [V540TU: Option Previous power state restoration doesn't work](https://github.com/Dasharo/dasharo-issues/issues/931)
- [Artifacts in video playback in some players using HW acceleration](https://github.com/Dasharo/dasharo-issues/issues/948)
- [Only native resolution listed for internal panel](https://github.com/Dasharo/dasharo-issues/issues/949)

### Binaries

[novacustom_v54x_mtl_ec_v0.9.0.rom][novacustom_v54x_mtl_ec_v0.9.0.rom_file]{.md-button}
[sha256][novacustom_v54x_mtl_ec_v0.9.0.rom_hash]{.md-button}
[sha256.sig][novacustom_v54x_mtl_ec_v0.9.0.rom_sig]{.md-button}

[novacustom_v54x_mtl_v0.9.0.rom][novacustom_v54x_mtl_v0.9.0.rom_file]{.md-button}
[sha256][novacustom_v54x_mtl_v0.9.0.rom_hash]{.md-button}
[sha256.sig][novacustom_v54x_mtl_v0.9.0.rom_sig]{.md-button}

[novacustom_v54x_mtl_v0.9.0_dev_signed.rom][novacustom_v54x_mtl_v0.9.0_dev_signed.rom_file]{.md-button}
[sha256][novacustom_v54x_mtl_v0.9.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][novacustom_v54x_mtl_v0.9.0_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-0.x-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 24.02 revision 316f964c](https://github.com/Dasharo/coreboot/tree/316f964c)
- [Dasharo EDKII fork based on edk2-stable202402 revision cc2be228](https://github.com/Dasharo/edk2/tree/cc2be228)

[newsletter]: https://newsletter.3mdeb.com/subscription/4yriJD4GX
[novacustom_v54x_mtl_ec_v0.9.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v54x_mtl/v0.9.0/novacustom_v54x_mtl_ec_v0.9.0.rom
[novacustom_v54x_mtl_ec_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v54x_mtl/v0.9.0/novacustom_v54x_mtl_ec_v0.9.0.rom.sha256
[novacustom_v54x_mtl_ec_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v54x_mtl/v0.9.0/novacustom_v54x_mtl_ec_v0.9.0.rom.sha256.sig
[novacustom_v54x_mtl_v0.9.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v54x_mtl/v0.9.0/novacustom_v54x_mtl_v0.9.0.rom
[novacustom_v54x_mtl_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v54x_mtl/v0.9.0/novacustom_v54x_mtl_v0.9.0.rom.sha256
[novacustom_v54x_mtl_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v54x_mtl/v0.9.0/novacustom_v54x_mtl_v0.9.0.rom.sha256.sig
[novacustom_v54x_mtl_v0.9.0_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v54x_mtl/v0.9.0/novacustom_v54x_mtl_v0.9.0_dev_signed.rom
[novacustom_v54x_mtl_v0.9.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v54x_mtl/v0.9.0/novacustom_v54x_mtl_v0.9.0_dev_signed.rom.sha256
[novacustom_v54x_mtl_v0.9.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v54x_mtl/v0.9.0/novacustom_v54x_mtl_v0.9.0_dev_signed.rom.sha256.sig
