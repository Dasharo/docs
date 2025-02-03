# Hardkernel Odroid H4 Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
Hardkernel Odroid H4

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

[Subscribe to Hardkernel Odroid H4 Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

</center>

## v0.9.0 - 2025-02-03

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Hardkernel/Odroid_H4/v0.9.0_results.csv).

### Added

- Initial support for the Hardkernel Odroid H4 device, based on Intel Alder
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
- [Intel ME HAP disable](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20F-me-neuter/)
- [BIOS flash protection for Vboot recovery region](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20J-bios-lock-support/)
- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
- [SMM BIOS write protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Network stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#networking-options)

### Known issues

- [S3 sleep too short on Odroid H4 Plus](https://github.com/Dasharo/dasharo-issues/issues/1213)

### Binaries

[sha256][hardkernel_odroid_h4_v0.9.0.rom_hash]{.md-button}
[sha256.sig][hardkernel_odroid_h4_v0.9.0.rom_sig]{.md-button}

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Pro Package newsletter.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/hardkernel_odroid_h4/dasharo-release-0.x-compatible-with-hardkernel-odroid-h4-family-signing-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 24.02 revision 93eb5819](https://github.com/Dasharo/coreboot/tree/93eb5819)
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

[newsletter]: https://newsletter.3mdeb.com/subscription/pULA4K0Eo
[hardkernel_odroid_h4_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/v0.9.0/hardkernel_odroid_h4_v0.9.0.rom.sha256
[hardkernel_odroid_h4_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/v0.9.0/hardkernel_odroid_h4_v0.9.0.rom.sha256.sig
