# NovaCustom V56xTNx 14th Gen Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
NovaCustom V56xTNx 14th Gen

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("afc2dba2-664f-4b85-9fea-70df53400f1f",
"Subscribe to NovaCustom V56xTNx 14th Gen Dasharo Release Newsletter") }}

!!! note
    `btg_prod` binaries are signed with production Intel Boot Guard keys,
    and are safe to install on platforms with Boot Guard disabled as well as
    those that have Boot Guard enabled, and both on fused and unfused platforms.

    Flashing these binaries enables Boot Guard but does not perform platform
    fusing, which means that the Boot Guard key configuration is mutable as long
    as the platform is not fused. Check the [TrustRoot documentation](../../unified/novacustom/features.md#dasharo-trustroot)
    for more information.

## v1.0.0 - 2026-01-29

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/NovaCustom/MTL_14th_Gen/V560TNX/).

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
- [Intel Boot Guard OEM Signing Key check in capsule update](https://docs.dasharo.com/guides/capsule-update/#troubleshooting)

### Changed

- [coreboot rebased on 24.12](https://doc.coreboot.org/releases/coreboot-24.12-relnotes.html)
- EDK II rebased on edk2-stable202502
- UEFI DBX updated to 2025-10-16
- Intel Microcode updated to microcode-20251111
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
- [BIOS settings are randomly reset](https://github.com/dasharo/dasharo-issues/issues/1293)
- [Booting DTS v2.0.0 through iPXE has no internet](https://github.com/dasharo/dasharo-issues/issues/1142)
- [Wrong serial number printed in console](https://github.com/dasharo/dasharo-issues/issues/1255)
- [No external HDMI display (Firmware)](https://github.com/dasharo/dasharo-issues/issues/1098)
- [Logo out of proportion](https://github.com/Dasharo/dasharo-issues/issues/1238)
- [External audio devices don't work in Windows](https://github.com/Dasharo/dasharo-issues/issues/1583)
- [When battery is low, USB-PD is constantly charging then discharging](https://github.com/Dasharo/dasharo-issues/issues/1660)
- [Touchpad not working in Windows installer](https://github.com/Dasharo/dasharo-issues/issues/1657)
- [Low graphics performance](https://github.com/Dasharo/dasharo-issues/issues/1243)
- [Fusing process fails](https://github.com/Dasharo/dasharo-issues/issues/1622)
- [USB-PD charger overdraw](https://github.com/Dasharo/dasharo-issues/issues/1599)
- [SMMSTORE writes are unreliable if SMM_BWP is enabled](https://github.com/Dasharo/dasharo-issues/issues/1664)
- [DBX update via fwupd fails](https://github.com/Dasharo/dasharo-issues/issues/1641)
- [USB keyboard through docking station not working before OS boots](https://github.com/Dasharo/dasharo-issues/issues/1662)
- [Windows installer claims it doesn't meet the requirements](https://github.com/Dasharo/dasharo-issues/issues/1658)
- [Cannot enable memory integrity kern isolation in Windows Security](https://github.com/Dasharo/dasharo-issues/issues/1674)

### Known issues

- [Previous power state restoration doesn't work](https://github.com/Dasharo/dasharo-issues/issues/931)
- [Artifacts in video playback in some players using HW acceleration](https://github.com/Dasharo/dasharo-issues/issues/948)
- [Only native resolution listed for internal panel](https://github.com/Dasharo/dasharo-issues/issues/949)
- [Early DMA protection cannot be applied to NovaCustom MTL](https://github.com/Dasharo/dasharo-issues/issues/985)
- [Spurious USB 3 disconnects with Sonnet Echo 11 Thunderbolt 4 dock](https://github.com/Dasharo/dasharo-issues/issues/1081)
- [GRUB installation fails sometimes](https://github.com/Dasharo/dasharo-issues/issues/1594)
- [Capsule Updates require ME to be manually disabled](https://github.com/Dasharo/dasharo-issues/issues/1302)
- [Capsule update signing is not enforced](https://github.com/Dasharo/dasharo-issues/issues/1075)
- [Microphone mute Fn key doesn't work in Windows](https://github.com/Dasharo/dasharo-issues/issues/1006)
- [48GB SODIMMs get hot during MemTest86+](https://github.com/Dasharo/dasharo-issues/issues/1125)
- [Windows 11 fails to resume from hibernation](https://github.com/dasharo/dasharo-issues/issues/529)

### Binaries

[novacustom_v56x_mtl_dgpu_ec_v1.0.0.rom][novacustom_v56x_mtl_dgpu_ec_v1.0.0.rom_file]{.md-button}
[sha256][novacustom_v56x_mtl_dgpu_ec_v1.0.0.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_dgpu_ec_v1.0.0.rom_sig]{.md-button}

[novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cab][novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cab_file]{.md-button}
[sha256][novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cab_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cab_sig]{.md-button}

[novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cap][novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cap_file]{.md-button}
[sha256][novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cap_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cap_sig]{.md-button}

[novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.rom][novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.rom_file]{.md-button}
[sha256][novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.03 revision 6de027d1](https://github.com/Dasharo/coreboot/tree/6de027d1)
- [Dasharo EDKII fork based on edk2-stable202502 revision 917172ee](https://github.com/Dasharo/edk2/tree/917172ee)
- [Dasharo iPXE fork based on 2025.03 revision 6c7068fc](https://github.com/Dasharo/ipxe/tree/6c7068fc)
    + [License](https://github.com/Dasharo/ipxe/blob/6c7068fc/COPYING.GPLv2)
- [vboot based on 3d37d2aafe revision f1f70f46](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/LICENSE)
- [Intel Management Engine version v18.0.10.2285](https://github.com/Dasharo/dasharo-blobs/blob/8dce7604/novacustom/v5x0tnx/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package for Meteor Lake-H version 2024/04/30 v4122_12](https://github.com/Dasharo/dasharo-blobs/tree/8dce7604/novacustom/v5x0tnx/MeteorLakeFspBinPkg)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/8dce7604/novacustom/v5x0tnx/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel microcode version MTL C0 0x00000025 0x25 19/03/2025](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20251111/intel-ucode/06-aa-04)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20251111/license)

[novacustom_v56x_mtl_dgpu_ec_v1.0.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_dgpu/novacustom_v560tnx_mtl/uefi/v1.0.0/novacustom_v56x_mtl_dgpu_ec_v1.0.0.rom
[novacustom_v56x_mtl_dgpu_ec_v1.0.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_dgpu/novacustom_v560tnx_mtl/uefi/v1.0.0/novacustom_v56x_mtl_dgpu_ec_v1.0.0.rom.sha256
[novacustom_v56x_mtl_dgpu_ec_v1.0.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_dgpu/novacustom_v560tnx_mtl/uefi/v1.0.0/novacustom_v56x_mtl_dgpu_ec_v1.0.0.rom.sha256.sig
[novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cab_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_dgpu/novacustom_v560tnx_mtl/uefi/v1.0.0/novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cab
[novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cab_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_dgpu/novacustom_v560tnx_mtl/uefi/v1.0.0/novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cab.sha256
[novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cab_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_dgpu/novacustom_v560tnx_mtl/uefi/v1.0.0/novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cab.sha256.sig
[novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cap_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_dgpu/novacustom_v560tnx_mtl/uefi/v1.0.0/novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cap
[novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_dgpu/novacustom_v560tnx_mtl/uefi/v1.0.0/novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cap.sha256
[novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_dgpu/novacustom_v560tnx_mtl/uefi/v1.0.0/novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.cap.sha256.sig
[novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_dgpu/novacustom_v560tnx_mtl/uefi/v1.0.0/novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.rom
[novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_dgpu/novacustom_v560tnx_mtl/uefi/v1.0.0/novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.rom.sha256
[novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_dgpu/novacustom_v560tnx_mtl/uefi/v1.0.0/novacustom_v56x_mtl_dgpu_v1.0.0_btg_prod.rom.sha256.sig

## v0.9.1 - 2024-11-07

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/NovaCustom/MTL_14th_Gen/V560TNX/v0.9.1-results.csv).

### Added

- Support for NovaCustom Meteor Lake platform (discrete graphics)
- [Vboot Verified Boot](https://docs.dasharo.com/guides/vboot-signing/)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [Vboot recovery notification in UEFI Payload](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)
- [UEFI Shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
- [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [Firmware update mode](https://docs.dasharo.com/guides/firmware-update/#firmware-update-mode)
- [BIOS boot medium write-protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [SMM BIOS write protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
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

- [No HDMI output in FW](https://github.com/Dasharo/dasharo-issues/issues/930)
- [Artifacts in video playback in some players using HW acceleration](https://github.com/Dasharo/dasharo-issues/issues/948)
- [Only native resolution listed for internal panel](https://github.com/Dasharo/dasharo-issues/issues/949)
- [Microphone mute Fn key doesn't work in Windows](https://github.com/Dasharo/dasharo-issues/issues/1006)
- [CPU frequency measurements sometimes go below known minimum](https://github.com/Dasharo/dasharo-issues/issues/1050)
- [Some flash drives may not be detected after reboot](https://github.com/Dasharo/dasharo-issues/issues/1051)
- [I2C controller timeout with SPD5118 driver](https://github.com/Dasharo/dasharo-issues/issues/1105)
- [Echo11 Docking station SD Reader failure (ME Disabled)](https://github.com/Dasharo/dasharo-issues/issues/1100)
- [Spurious USB 3 disconnects with Sonnet Echo 11 Thunderbolt 4 dock](https://github.com/Dasharo/dasharo-issues/issues/1081)
- [48GB SODIMMs get hot during MemTest86+](https://github.com/Dasharo/dasharo-issues/issues/1125)

### Binaries

[novacustom_v56x_mtl_ec_v0.9.1.rom][novacustom_v56x_mtl_ec_v0.9.1.rom_file]{.md-button}
[sha256][novacustom_v56x_mtl_ec_v0.9.1.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_ec_v0.9.1.rom_sig]{.md-button}

[novacustom_v56x_mtl_v0.9.1.rom][novacustom_v56x_mtl_v0.9.1.rom_file]{.md-button}
[sha256][novacustom_v56x_mtl_v0.9.1.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_v0.9.1.rom_sig]{.md-button}

[novacustom_v56x_mtl_v0.9.1_dev_signed.rom][novacustom_v56x_mtl_v0.9.1_dev_signed.rom_file]{.md-button}
[sha256][novacustom_v56x_mtl_v0.9.1_dev_signed.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_v0.9.1_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/dasharo-release-0.9.x-for-novacustom-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo fork of coreboot based on 24.02 revision c44f1998](https://github.com/Dasharo/coreboot/tree/c44f1998)
    + [License](https://github.com/Dasharo/coreboot/blob/c44f1998/COPYING)
- [Dasharo fork of EDKII based on edk2-stable202402 revision f3e18c6c](https://github.com/Dasharo/edk2/tree/f3e18c6c)
    + [License](https://github.com/Dasharo/edk2/blob/f3e18c6c/License.txt)
- [Dasharo fork of edk2-platforms based on 8ea6ec38 revision 3323ed48](https://github.com/Dasharo/edk2-platforms/tree/3323ed48)
    + [License](https://github.com/Dasharo/edk2-platforms/blob/3323ed48/License.txt)
- [Dasharo fork of System76 EC based on 485f3900 revision 3e931cf8](https://github.com/Dasharo/ec/tree/3e931cf8/)
    + [License](https://github.com/Dasharo/ec/blob/3e931cf8/LICENSE)
- [Dasharo fork of iPXE based on d2d194bc revision 35d84756](https://github.com/Dasharo/ipxe/tree/35d84756)
    + [License](https://github.com/Dasharo/ipxe/blob/35d84756/COPYING.GPLv2)
- [vboot based on 3d37d2aa revision 3d37d2aa](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/LICENSE)
- [Intel Management Engine based on v18.0.5.2040 revision 3541ad31](https://github.com/Dasharo/dasharo-blobs/blob/main/novacustom/v5x0tnx/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor based on v1.0 revision 3541ad31](https://github.com/Dasharo/dasharo-blobs/blob/main/novacustom/v5x0tnx/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel processor microcode based on MTL C0 0x0000001c revision microcode-20240531](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240531/intel-ucode/06-aa-04)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240531/license)

[novacustom_v56x_mtl_ec_v0.9.1.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_ec_v0.9.1.rom
[novacustom_v56x_mtl_ec_v0.9.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_ec_v0.9.1.rom.sha256
[novacustom_v56x_mtl_ec_v0.9.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_ec_v0.9.1.rom.sha256.sig
[novacustom_v56x_mtl_v0.9.1.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_v0.9.1.rom
[novacustom_v56x_mtl_v0.9.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_v0.9.1.rom.sha256
[novacustom_v56x_mtl_v0.9.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_v0.9.1.rom.sha256.sig
[novacustom_v56x_mtl_v0.9.1_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_v0.9.1_dev_signed.rom
[novacustom_v56x_mtl_v0.9.1_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_v0.9.1_dev_signed.rom.sha256
[novacustom_v56x_mtl_v0.9.1_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_v0.9.1_dev_signed.rom.sha256.sig
