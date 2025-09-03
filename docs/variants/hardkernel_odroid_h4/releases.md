# Hardkernel ODROID H4 Dasharo Release Notes

This is a Dasharo Pro Package Release. o obtain access to the pre-built binaries,
you need to [subscribe to the Dasharo Pro Package subscriber](https://docs.dasharo.com/ways-you-can-help-us/#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our [shop](https://shop.3mdeb.com/shop/dasharo-pro-package/1-year-dasharo-entry-subscription-for-network-appliance/).
As a subscriber, you will receive access to all firmware updates for the
duration of your subscription via the Dasharo Pro Package newsletter,
and gain entry to the Dasharo Premier Support invite-only live chat
on the Matrix network, enabling direct engagement with the Dasharo Team
and fellow subscribers for personalized, priority assistance.

Following Release Notes describe status of open-source firmware development for
Hardkernel ODROID H4

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("d4b31e80-7663-4f6b-8fcb-f5ff551eb1d6",
"Subscribe to Hardkernel ODROID H4 Dasharo Release Newsletter") }}

## v0.9.1 - 2025-09-03

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Hardkernel/Odroid_H4/v0.9.1_results.csv).

### Added

- Support for the Hardkernel ODROID H4 Ultra device
- [Support for Net Card 2 module](https://github.com/Dasharo/dasharo-issues/issues/1281)
- [Capsule Update integration](https://github.com/Dasharo/dasharo-issues/issues/1471)
- [In-Band ECC option](https://github.com/Dasharo/dasharo-issues/issues/1276)
- [Quiet and fast boot option](https://github.com/Dasharo/dasharo-issues/issues/1278)
- [ME disable option](https://github.com/Dasharo/dasharo-issues/issues/1279)
- Boot Guard status information to UEFI setup menu
- Improved measured boot support
- Microsoft Option ROM UEFI CA to Secure Boot DB
- Check for flash descriptor writability when exposign HAP disable option

### Changed

- [VBT file to fix graphical output in firmware](https://github.com/Dasharo/dasharo-issues/issues/1353)
- Flash descriptor updated to v1.1 (see SBOM)
- Owner GUID of Secure Boot DB and KEK to Microsoft recommended values
- Updated DBX to 2025-06-13

### Fixed

- [S3 sleep too short on ODROID H4 Plus](https://github.com/Dasharo/dasharo-issues/issues/1213)
- [Can't delete signature of enrolled EFI file from DB as it's not shown](https://github.com/Dasharo/dasharo-issues/issues/1365)
- [Dismissing a pop-up in UEFI payload caused instant booting](https://github.com/Dasharo/dasharo-issues/issues/1539)
- [Recovery of damaged variable storage causing random settings reset](https://github.com/Dasharo/dasharo-issues/issues/1293)

### Binaries

If you wish to use a Net Card module, please use the files suffixed with
`netcard`. They have the proper 4x1 bifurcation in M.2 slot as explained on
[ODROID
wiki](https://wiki.odroid.com/accessory/connectivity/netcard3?s[]=netcard#netcard_bios_versions).

[sha256][hardkernel_odroid_h4_v0.9.1.cap_hash]{.md-button}
[sha256.sig][hardkernel_odroid_h4_v0.9.1.cap_sig]{.md-button}
(hardkernel_odroid_h4_v0.9.1.cap)

[sha256][hardkernel_odroid_h4_v0.9.1.rom_hash]{.md-button}
[sha256.sig][hardkernel_odroid_h4_v0.9.1.rom_sig]{.md-button}
(hardkernel_odroid_h4_v0.9.1.rom)

[sha256][hardkernel_odroid_h4_v0.9.1_dev_signed.cap_hash]{.md-button}
[sha256.sig][hardkernel_odroid_h4_v0.9.1_dev_signed.cap_sig]{.md-button}
(hardkernel_odroid_h4_v0.9.1_dev_signed.cap)

[sha256][hardkernel_odroid_h4_v0.9.1_dev_signed.rom_hash]{.md-button}
[sha256.sig][hardkernel_odroid_h4_v0.9.1_dev_signed.rom_sig]{.md-button}
(hardkernel_odroid_h4_v0.9.1_dev_signed.rom)

[sha256][hardkernel_odroid_h4_v0.9.1_netcard.cap_hash]{.md-button}
[sha256.sig][hardkernel_odroid_h4_v0.9.1_netcard.cap_sig]{.md-button}
(hardkernel_odroid_h4_v0.9.1_netcard.cap)

[sha256][hardkernel_odroid_h4_v0.9.1_netcard.rom_hash]{.md-button}
[sha256.sig][hardkernel_odroid_h4_v0.9.1_netcard.rom_sig]{.md-button}
(hardkernel_odroid_h4_v0.9.1_netcard.rom)

[sha256][hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.cap_hash]{.md-button}
[sha256.sig][hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.cap_sig]{.md-button}
(hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.cap)

[sha256][hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.rom_hash]{.md-button}
[sha256.sig][hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.rom_sig]{.md-button}
(hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.rom)

This is a Dasharo Pro Package Release. To access the pre-built binaries,
you need to [subscribe to the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our
[shop](https://shop.3mdeb.com/shop/dasharo-pro-package/1-year-dasharo-pro-package-for-network-appliance/).
As a subscriber, you will receive access to all firmware updates for the
duration of your subscription via the Dasharo Pro Package newsletter, and
gain entry to the Dasharo Premier Support invite-only live chat on the Matrix
network, enabling direct engagement with the Dasharo Team and fellow
subscribers for personalized, priority assistance.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/hardkernel_odroid_h4/dasharo-release-0.x-compatible-with-hardkernel-odroid-h4-family-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 24.12 revision 7d10ea62](https://github.com/Dasharo/coreboot/tree/7d10ea62)
    + [License](https://github.com/Dasharo/coreboot/blob/7d10ea62/COPYING)
- [Dasharo EDKII fork based on edk2-stable202502 revision 91a7a092](https://github.com/Dasharo/edk2/tree/91a7a092)
    + [License](https://github.com/Dasharo/edk2/blob/91a7a092/License.txt)
- [Dasharo iPXE fork based on 2025.03 revision 6c7068fc](https://github.com/Dasharo/ipxe/tree/6c7068fc)
    + [License](https://github.com/Dasharo/ipxe/blob/6c7068fc/COPYING.GPLv2)
- [vboot based on f1f70f46dc revision f1f70f46](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/LICENSE)
- [Intel Management Engine version v16.50.10.1351](https://github.com/Dasharo/dasharo-blobs/blob/52647f9c/hardkernel/odroid_h4/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/52647f9c/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.1](https://github.com/Dasharo/dasharo-blobs/blob/52647f9c/hardkernel/odroid_h4/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/52647f9c/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version IoT ADL-N MR6 (6023_00)](https://github.com/intel/FSP/commits/86c91116/AlderLakeFspBinPkg/IoT/AlderLakeN)
    + [License](https://github.com/intel/FSP/blob/86c91116/FSP_License.pdf)
- [Intel microcode version ADL-N N0 0x1d 06/12/2024](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20250812/intel-ucode/06-be-00)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20250812/license)

[hardkernel_odroid_h4_v0.9.1.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1.cap.sha256
[hardkernel_odroid_h4_v0.9.1.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1.cap.sha256.sig
[hardkernel_odroid_h4_v0.9.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1.rom.sha256
[hardkernel_odroid_h4_v0.9.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1.rom.sha256.sig
[hardkernel_odroid_h4_v0.9.1_dev_signed.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1_dev_signed.cap.sha256
[hardkernel_odroid_h4_v0.9.1_dev_signed.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1_dev_signed.cap.sha256.sig
[hardkernel_odroid_h4_v0.9.1_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1_dev_signed.rom.sha256
[hardkernel_odroid_h4_v0.9.1_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1_dev_signed.rom.sha256.sig
[hardkernel_odroid_h4_v0.9.1_netcard.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1_netcard.cap.sha256
[hardkernel_odroid_h4_v0.9.1_netcard.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1_netcard.cap.sha256.sig
[hardkernel_odroid_h4_v0.9.1_netcard.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1_netcard.rom.sha256
[hardkernel_odroid_h4_v0.9.1_netcard.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1_netcard.rom.sha256.sig
[hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.cap.sha256
[hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.cap.sha256.sig
[hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.rom.sha256
[hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.1/hardkernel_odroid_h4_v0.9.1_netcard_dev_signed.rom.sha256.sig

## v0.9.0 - 2025-02-20

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Hardkernel/Odroid_H4/v0.9.0_results.csv).

### Added

- Initial support for the Hardkernel ODROID H4 device, based on Intel Alder
  Lake N
- [UEFI compatible interface](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface/)
- [Support for discrete TPM](https://docs.dasharo.com/unified-test-documentation/dasharo-security/200-tpm-support/)
- [UEFI Secure Boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [Boot logo customization support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/328-logo-customization-functionality/)
- [USB boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31N-usb-boot/)
- [NVMe boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/312-nvme-support/)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [UEFI Shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
- [Network boot](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/315b-netboot-utilities/)
- [Windows 11 booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31A-windows-booting/)
- [Ubuntu LTS booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support/)
- [Serial port console redirection](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31G-ec-and-superio/#sio004001-serial-port-in-firmware)
- [Vboot Verified Boot](https://docs.dasharo.com/guides/vboot-signing/)
- [BIOS flash protection for Vboot recovery region](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20J-bios-lock-support/)
- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
- [SMM BIOS write protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Network stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#networking-options)

### Known issues

- [S3 sleep too short on ODROID H4 Plus](https://github.com/Dasharo/dasharo-issues/issues/1213)

### Binaries

[sha256][hardkernel_odroid_h4_v0.9.0.rom_hash]{.md-button}
[sha256.sig][hardkernel_odroid_h4_v0.9.0.rom_sig]{.md-button}

[dev_signed.sha256][hardkernel_odroid_h4_v0.9.0_dev_signed.rom_hash]{.md-button}
[dev_signed.sha256.sig][hardkernel_odroid_h4_v0.9.0_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/hardkernel_odroid_h4/dasharo-release-0.x-compatible-with-hardkernel-odroid-h4-family-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 24.02 revision 93eb5819](https://github.com/Dasharo/coreboot/tree/93eb5819)
    + [License](https://github.com/Dasharo/coreboot/blob/93eb5819/COPYING)
- [Dasharo EDKII fork based on edk2-stable202402 revision 7dbfe58b](https://github.com/Dasharo/edk2/tree/7dbfe58b)
    + [License](https://github.com/Dasharo/edk2/blob/7dbfe58b/License.txt)
- [Dasharo iPXE fork based on 2024.05 revision 35d84756](https://github.com/Dasharo/ipxe/tree/35d84756)
    + [License](https://github.com/Dasharo/ipxe/blob/35d84756/COPYING.GPLv2)
- [vboot based on 3d37d2aafe revision 3d37d2aa](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/LICENSE)
- [Intel Management Engine version v16.50.10.1351](https://github.com/Dasharo/dasharo-blobs/blob/c4ecc9e3/hardkernel/odroid_h4/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/c4ecc9e3/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/c4ecc9e3/hardkernel/odroid_h4/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/c4ecc9e3/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version IoT ADL-N MR4 (5061_00)](https://github.com/intel/FSP/commits/3819544e/AlderLakeFspBinPkg/IoT/AlderLakeN)
    + [License](https://github.com/intel/FSP/blob/3819544e/FSP_License.pdf)
- [Intel microcode version ADL-N N0 0x17 07/12/2023](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240531/intel-ucode/06-be-00)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240531/license)

[hardkernel_odroid_h4_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/v0.9.0/hardkernel_odroid_h4_v0.9.0.rom.sha256
[hardkernel_odroid_h4_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/v0.9.0/hardkernel_odroid_h4_v0.9.0.rom.sha256.sig
[hardkernel_odroid_h4_v0.9.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/v0.9.0/hardkernel_odroid_h4_v0.9.0_dev_signed.rom.sha256
[hardkernel_odroid_h4_v0.9.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/v0.9.0/hardkernel_odroid_h4_v0.9.0_dev_signed.rom.sha256.sig
