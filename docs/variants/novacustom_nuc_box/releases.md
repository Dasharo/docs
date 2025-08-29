# NovaCustom NUC BOX 14th Gen Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
NovaCustom NUC BOX 14th Gen

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

{{ subscribe_form("d982d4ac-f1b5-4926-9d89-e7bb71457dd9",
"Subscribe to NovaCustom NUC BOX 14th Gen Dasharo Release Newsletter") }}

</center>

## v0.9.0 - 2025-08-27

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/NovaCustom/MTL_14th_Gen/NUC_BOX/v0.9.0_results.csv).

### Added

- Support for NovaCustom NUC BOX (Meteor Lake)
- [Introduce updates via UEFI capsules (from this firmware onward)](https://docs.dasharo.com/kb/capsule-updates-overview/)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [Vboot Verified Boot](https://docs.dasharo.com/guides/vboot-signing/)
- [Intel ME soft disable](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20F-me-neuter/)
- [Vboot recovery notification in UEFI Payload](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)
- [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [Firmware update mode](https://docs.dasharo.com/guides/firmware-update/#firmware-update-mode)
- [BIOS boot medium write-protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [SMM BIOS write protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Early Sign of Life display output](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/347-sign-of-life/)
- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
- [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Network stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#networking-options)
- [Intel ME disable option in setup menu](https://docs.dasharo.com/osf-trivia-list/me/)
- [Power on AC option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Fan profiles in setup Menu](https://docs.dasharo.com/unified/novacustom/fan-profiles/)
- [Quiet boot/Fast boot](https://docs.dasharo.com/dasharo-menu-docs/boot-maintenance-mgr/)
- [Throttling temperature adjustment in setup menu](https://docs.dasharo.com/unified/novacustom/features/#cpu-throttling-threshold)

### Known issues

- [S3 not supported on Windows](https://github.com/Dasharo/dasharo-issues/issues/1521)
- [Varmilo USB keyboard doesn't work in firmware menu](https://github.com/Dasharo/dasharo-issues/issues/1477)
- [Qubes OS spd5118 error in dmesg](https://github.com/Dasharo/dasharo-issues/issues/1493)
- [NUCBOX unexpected dmesg errors](https://github.com/Dasharo/dasharo-issues/issues/1531)
- [Wake by USB keyboard not working in Qubes](https://github.com/Dasharo/dasharo-issues/issues/731)

### Binaries

[novacustom_nuc_box_mtl_v0.9.0.rom][novacustom_nuc_box_mtl_v0.9.0.rom_file]{.md-button}
[sha256][novacustom_nuc_box_mtl_v0.9.0.rom_hash]{.md-button}
[sha256.sig][novacustom_nuc_box_mtl_v0.9.0.rom_sig]{.md-button}
[novacustom_nuc_box_mtl_v0.9.0_dev_signed.rom][novacustom_nuc_box_mtl_v0.9.0_dev_signed.rom_file]{.md-button}
[sha256_dev_signed][novacustom_nuc_box_mtl_v0.9.0_dev_signed.rom_hash]{.md-button}
[sha256.sig_dev_signed][novacustom_nuc_box_mtl_v0.9.0_dev_signed.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/dasharo-release-0.9.x-for-novacustom-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.03 revision fdea68ac](https://github.com/Dasharo/coreboot/tree/fdea68ac)
- [Dasharo EDKII fork based on edk2-stable202502 revision ac25544f](https://github.com/Dasharo/edk2/tree/ac25544f)
- [Dasharo iPXE fork based on 2025.03 revision 8b8a50a8](https://github.com/Dasharo/ipxe/tree/8b8a50a8)
    + [License](https://github.com/Dasharo/ipxe/blob/8b8a50a8/COPYING.GPLv2)
- [vboot based on f1f70f46dc revision f1f70f46](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/LICENSE)
- [Intel Management Engine version v18.0.5.2028](https://github.com/Dasharo/dasharo-blobs/blob/52647f9c/novacustom/nuc_box/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package for Meteor Lake-H version 2024/04/30 v4122_12](https://github.com/Dasharo/dasharo-blobs/tree/52647f9c/novacustom/v5x0tu/MeteorLakeFspBinPkg)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/52647f9c/novacustom/nuc_box/ifd.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel microcode version MTL C0 0x00000020 0x25 19/03/2025](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20250812/intel-ucode/06-aa-04)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20250812/license)

[novacustom_nuc_box_mtl_v0.9.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nuc_box_mtl/uefi/v0.9.0/novacustom_nuc_box_mtl_v0.9.0.rom
[novacustom_nuc_box_mtl_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nuc_box_mtl/uefi/v0.9.0/novacustom_nuc_box_mtl_v0.9.0.rom.sha256
[novacustom_nuc_box_mtl_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nuc_box_mtl/uefi/v0.9.0/novacustom_nuc_box_mtl_v0.9.0.rom.sha256.sig
[novacustom_nuc_box_mtl_v0.9.0_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nuc_box_mtl/uefi/v0.9.0/novacustom_nuc_box_mtl_v0.9.0_dev_signed.rom
[novacustom_nuc_box_mtl_v0.9.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nuc_box_mtl/uefi/v0.9.0/novacustom_nuc_box_mtl_v0.9.0_dev_signed.rom.sha256
[novacustom_nuc_box_mtl_v0.9.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nuc_box_mtl/uefi/v0.9.0/novacustom_nuc_box_mtl_v0.9.0_dev_signed.rom.sha256.sig
