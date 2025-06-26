# NovaCustom V56xTNx 14th Gen Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
NovaCustom V56xTNx 14th Gen

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("afc2dba2-664f-4b85-9fea-70df53400f1f",
"Subscribe to NovaCustom V56xTNx 14th Gen Dasharo Release Newsletter") }}

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
    * [License](https://github.com/Dasharo/coreboot/blob/c44f1998/COPYING)
- [Dasharo fork of EDKII based on edk2-stable202402 revision f3e18c6c](https://github.com/Dasharo/edk2/tree/f3e18c6c)
    * [License](https://github.com/Dasharo/edk2/blob/f3e18c6c/License.txt)
- [Dasharo fork of edk2-platforms based on 8ea6ec38 revision 3323ed48](https://github.com/Dasharo/edk2-platforms/tree/3323ed48)
    * [License](https://github.com/Dasharo/edk2-platforms/blob/3323ed48/License.txt)
- [Dasharo fork of System76 EC based on 485f3900 revision 3e931cf8](https://github.com/Dasharo/ec/tree/3e931cf8/)
    * [License](https://github.com/Dasharo/ec/blob/3e931cf8/LICENSE)
- [Dasharo fork of iPXE based on d2d194bc revision 35d84756](https://github.com/Dasharo/ipxe/tree/35d84756)
    * [License](https://github.com/Dasharo/ipxe/blob/35d84756/COPYING.GPLv2)
- [vboot based on 3d37d2aa revision 3d37d2aa](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/)
    * [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/LICENSE)
- [Intel Management Engine based on v18.0.5.2040 revision 3541ad31](https://github.com/Dasharo/dasharo-blobs/blob/main/novacustom/v5x0tnx/me.bin)
    * [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor based on v1.0 revision 3541ad31](https://github.com/Dasharo/dasharo-blobs/blob/main/novacustom/v5x0tnx/descriptor.bin)
    * [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel processor microcode based on MTL C0 0x0000001c revision microcode-20240531](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240531/intel-ucode/06-aa-04)
    * [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240531/license)

[novacustom_v56x_mtl_ec_v0.9.1.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_ec_v0.9.1.rom
[novacustom_v56x_mtl_ec_v0.9.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_ec_v0.9.1.rom.sha256
[novacustom_v56x_mtl_ec_v0.9.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_ec_v0.9.1.rom.sha256.sig
[novacustom_v56x_mtl_v0.9.1.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_v0.9.1.rom
[novacustom_v56x_mtl_v0.9.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_v0.9.1.rom.sha256
[novacustom_v56x_mtl_v0.9.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_v0.9.1.rom.sha256.sig
[novacustom_v56x_mtl_v0.9.1_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_v0.9.1_dev_signed.rom
[novacustom_v56x_mtl_v0.9.1_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_v0.9.1_dev_signed.rom.sha256
[novacustom_v56x_mtl_v0.9.1_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/v0.9.1/novacustom_v56x_mtl_v0.9.1_dev_signed.rom.sha256.sig
