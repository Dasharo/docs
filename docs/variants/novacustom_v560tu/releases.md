# NovaCustom V560TU Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
NovaCustom V560TU

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("d8319dd2-9108-48c5-86bf-318bb2ae94d2",
"Subscribe to NovaCustom V560TU 14th Gen Dasharo Release Newsletter") }}

## v1.0.0 - 2025-09-18

!!! warning
    Note: Due to [issue 1142](https://github.com/Dasharo/dasharo-issues/issues/1142),
    this update must be installed by following the process described in
    [Firmware Update - Manual Steps](https://docs.dasharo.com/unified/novacustom/firmware-update/#prerequisites)

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/NovaCustom/MTL_14th_Gen/V560TU/).

### Added

- [Quiet boot/Fast boot](https://docs.dasharo.com/dasharo-menu-docs/boot-maintenance-mgr/)
- [FTDI controller support](https://github.com/Dasharo/open-source-firmware-validation/blob/develop/docs/novacustom.md)
- [Dasharo TrustRoot (Intel Boot Guard) support](https://docs.dasharo.com/glossary/#dasharo-trustroot)
- [Sleep-and-charge ports](https://github.com/Dasharo/ec/pull/66)
- [Sleep type option](https://github.com/Dasharo/coreboot/pull/738/files)
- [PCR-0 reconstruction](https://github.com/Dasharo/coreboot/pull/740)
- [ACPI driver](https://docs.dasharo.com/unified/novacustom/features/#acpi-driver)
- [UEFI Capsule Update support](https://docs.dasharo.com/kb/capsule-updates-overview/)
- Fedora support

### Changed

- [coreboot rebased on 24.12](https://doc.coreboot.org/releases/coreboot-24.12-relnotes.html)
- EDK II rebased on edk2-stable202502
- UEFI DBX updated to 2025-06-13
- Owner GUID of Secure Boot DB and KEK to Microsoft recommended values

### Fixed

- [No HDMI output in FW on V540TU and V560TU](https://github.com/Dasharo/dasharo-issues/issues/930)
- [Laggy behaviour on Manjaro (KDE) with open drivers](https://github.com/Dasharo/dasharo-issues/issues/911)
- [Battery draining in sleep mode on Windows 11](https://github.com/Dasharo/dasharo-issues/issues/1375)
- [Small text in setup menu](https://github.com/Dasharo/dasharo-issues/issues/1237)
- [External boot file to USB flash drive not found after rebooting](https://github.com/dasharo/dasharo-issues/issues/990)
- [XFCE battery indicator keeps switching charge state when fully charged](https://github.com/dasharo/dasharo-issues/issues/1217)
- [Laptop starts after shutting down if WiFi is firmware-disabled](https://github.com/dasharo/dasharo-issues/issues/1157)
- [No HDMI output in firmware](https://github.com/dasharo/dasharo-issues/issues/533)
- [Integrated graphics driver does not load (Windows 11)](https://github.com/dasharo/dasharo-issues/issues/1236)
- [Windows 11 fails to resume from hibernation](https://github.com/dasharo/dasharo-issues/issues/529)
- [BIOS settings are randomly reset](https://github.com/dasharo/dasharo-issues/issues/1293)
- [Booting DTS v2.0.0 through iPXE has no internet](https://github.com/dasharo/dasharo-issues/issues/1142)
- [Wrong serial number printed in console](https://github.com/dasharo/dasharo-issues/issues/1255)
- [No external HDMI display (Firmware)](https://github.com/dasharo/dasharo-issues/issues/1098)

### Known issues

- [Previous power state restoration doesn't work](https://github.com/Dasharo/dasharo-issues/issues/931)
- [Artifacts in video playback in some players using HW acceleration](https://github.com/Dasharo/dasharo-issues/issues/948)
- [Only native resolution listed for internal panel](https://github.com/Dasharo/dasharo-issues/issues/949)
- [Early DMA protection cannot be applied to NovaCustom MTL](https://github.com/Dasharo/dasharo-issues/issues/985)
- [Spurious USB 3 disconnects with Sonnet Echo 11 Thunderbolt 4 dock](https://github.com/Dasharo/dasharo-issues/issues/1081)
- [Logo out of proportion](https://github.com/Dasharo/dasharo-issues/issues/1238)
- [GRUB installation fails sometimes](https://github.com/Dasharo/dasharo-issues/issues/1594)
- [Capsule Updates require ME to be manually disabled](https://github.com/Dasharo/dasharo-issues/issues/1302)
- [Capsule update signing is not enforced](https://github.com/Dasharo/dasharo-issues/issues/1075)
- [Microphone mute Fn key doesn't work in Windows](https://github.com/Dasharo/dasharo-issues/issues/1006)
- [48GB SODIMMs get hot during MemTest86+](https://github.com/Dasharo/dasharo-issues/issues/1125)

### Binaries

[novacustom_v56x_mtl_igpu_ec_v1.0.0.rom][novacustom_v56x_mtl_igpu_ec_v1.0.0.rom_file]{.md-button}
[sha256][novacustom_v56x_mtl_igpu_ec_v1.0.0.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_igpu_ec_v1.0.0.rom_sig]{.md-button}

[novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.cap][novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.cap_file]{.md-button}
[sha256][novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.cap_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.cap_sig]{.md-button}

[novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.rom][novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.rom_file]{.md-button}
[sha256][novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.03 revision 91420dbc](https://github.com/Dasharo/coreboot/tree/91420dbc)
- [Dasharo EDKII fork based on edk2-stable202502 revision 1c50dad8](https://github.com/Dasharo/edk2/tree/1c50dad8)
- [Dasharo iPXE fork based on 2025.03 revision 6c7068fc](https://github.com/Dasharo/ipxe/tree/6c7068fc)
    + [License](https://github.com/Dasharo/ipxe/blob/6c7068fc/COPYING.GPLv2)
- [vboot based on 3d37d2aafe revision f1f70f46](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/LICENSE)
- [Intel Management Engine version v18.0.10.2285](https://github.com/Dasharo/dasharo-blobs/blob/8dce7604/novacustom/v5x0tu/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package for Meteor Lake-H version 2024/04/30 v4122_12](https://github.com/Dasharo/dasharo-blobs/tree/8dce7604/novacustom/v5x0tu/MeteorLakeFspBinPkg)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/8dce7604/novacustom/v5x0tu/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel microcode version MTL C0 0x00000020 0x25 19/03/2025](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20250812/intel-ucode/06-aa-04)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20250812/license)

[novacustom_v56x_mtl_igpu_ec_v1.0.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_igpu/novacustom_v560tu_mtl/uefi/v1.0.0/novacustom_v56x_mtl_igpu_ec_v1.0.0.rom
[novacustom_v56x_mtl_igpu_ec_v1.0.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_igpu/novacustom_v560tu_mtl/uefi/v1.0.0/novacustom_v56x_mtl_igpu_ec_v1.0.0.rom.sha256
[novacustom_v56x_mtl_igpu_ec_v1.0.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_igpu/novacustom_v560tu_mtl/uefi/v1.0.0/novacustom_v56x_mtl_igpu_ec_v1.0.0.rom.sha256.sig
[novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.cap_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_igpu/novacustom_v560tu_mtl/uefi/v1.0.0/novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.cap
[novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_igpu/novacustom_v560tu_mtl/uefi/v1.0.0/novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.cap.sha256
[novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_igpu/novacustom_v560tu_mtl/uefi/v1.0.0/novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.cap.sha256.sig
[novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_igpu/novacustom_v560tu_mtl/uefi/v1.0.0/novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.rom
[novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_igpu/novacustom_v560tu_mtl/uefi/v1.0.0/novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.rom.sha256
[novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_igpu/novacustom_v560tu_mtl/uefi/v1.0.0/novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.rom.sha256.sig

## v0.9.0 - 2024-07-18

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/NovaCustom/MTL_14th_Gen/V560TU/v0.9.0-results.csv).

### Added

- Support for NovaCustom Meteor Lake platform (integrated graphics)
- [Vboot Verified Boot](https://docs.dasharo.com../../guides/vboot-signing/)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [Vboot recovery notification in UEFI Payload](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)
- [UEFI Shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
- [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [Firmware update mode](https://docs.dasharo.com../../guides/firmware-update/#firmware-update-mode)
- [BIOS boot medium write-protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [SMM BIOS write protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Early boot DMA protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Early Sign of Life display output](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/347-sign-of-life/)
- [Current limiting for USB-PD power supplies](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31H-usb-type-c/#utc020001-usb-type-c-pd-current-limiting-ubuntu-2204)
- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#user-password-management)
- [Wi-Fi / Bluetooth module disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Built-in webcam disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Network stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#networking-options)
- [Battery threshold options in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Intel ME disable option in setup menu](https://docs.dasharo.com/osf-trivia-list/me/)
- [Block boot when battery is too low](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/359-boot-blocking/#test-cases-common-documentation)
- [Power on AC option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Keyboard backlight level is restored after suspend or poweroff](https://github.com/Dasharo/dasharo-issues/issues/339)
- [Fan profiles in setup Menu](https://docs.dasharo.com/unified/novacustom/features/#fan-profiles)
- [Fn lock hotkey feature](https://docs.dasharo.com/unified/novacustom/fn-lock-hotkey/)
- [Throttling temperature adjustment in setup menu](https://docs.dasharo.com/unified/novacustom/features/#cpu-throttling-threshold)

### Known issues

- [No HDMI output in FW on V540TU and V560TU](https://github.com/Dasharo/dasharo-issues/issues/930)
- [Laggy behaviour on Manjaro (KDE) with open drivers](https://github.com/Dasharo/dasharo-issues/issues/911)
- [V540TU: Option Previous power state restoration doesn't work](https://github.com/Dasharo/dasharo-issues/issues/931)
- [Artifacts in video playback in some players using HW acceleration](https://github.com/Dasharo/dasharo-issues/issues/948)
- [Only native resolution listed for internal panel](https://github.com/Dasharo/dasharo-issues/issues/949)

### Binaries

[novacustom_v56x_mtl_ec_v0.9.0.rom][novacustom_v56x_mtl_ec_v0.9.0.rom_file]{.md-button}
[sha256][novacustom_v56x_mtl_ec_v0.9.0.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_ec_v0.9.0.rom_sig]{.md-button}

[novacustom_v56x_mtl_v0.9.0.rom][novacustom_v56x_mtl_v0.9.0.rom_file]{.md-button}
[sha256][novacustom_v56x_mtl_v0.9.0.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_v0.9.0.rom_sig]{.md-button}

[novacustom_v56x_mtl_v0.9.0_dev_signed.rom][novacustom_v56x_mtl_v0.9.0_dev_signed.rom_file]{.md-button}
[sha256][novacustom_v56x_mtl_v0.9.0_dev_signed.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_v0.9.0_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/dasharo-release-0.9.x-for-novacustom-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 24.02 revision 316f964c](https://github.com/Dasharo/coreboot/tree/316f964c)
- [Dasharo EDKII fork based on edk2-stable202402 revision cc2be228](https://github.com/Dasharo/edk2/tree/cc2be228)

[novacustom_v56x_mtl_ec_v0.9.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.0/novacustom_v56x_mtl_ec_v0.9.0.rom
[novacustom_v56x_mtl_ec_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.0/novacustom_v56x_mtl_ec_v0.9.0.rom.sha256
[novacustom_v56x_mtl_ec_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.0/novacustom_v56x_mtl_ec_v0.9.0.rom.sha256.sig
[novacustom_v56x_mtl_v0.9.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.0/novacustom_v56x_mtl_v0.9.0.rom
[novacustom_v56x_mtl_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.0/novacustom_v56x_mtl_v0.9.0.rom.sha256
[novacustom_v56x_mtl_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.0/novacustom_v56x_mtl_v0.9.0.rom.sha256.sig
[novacustom_v56x_mtl_v0.9.0_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.0/novacustom_v56x_mtl_v0.9.0_dev_signed.rom
[novacustom_v56x_mtl_v0.9.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.0/novacustom_v56x_mtl_v0.9.0_dev_signed.rom.sha256
[novacustom_v56x_mtl_v0.9.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.0/novacustom_v56x_mtl_v0.9.0_dev_signed.rom.sha256.sig
