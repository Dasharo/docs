# Dell OptiPlex 7010/9010 Dasharo Pro Package Release Notes

Following Release Notes describe status of open-source firmware development for
Dell OptiPlex 7010/9010

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

## Binaries

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become a Dasharo Pro Package subscriber](https://docs.dasharo.com/ways-you-can-help-us/#become-a-dasharo-pro-package-subscriber)
. You will get access to all of the firmware updates for the duration of the
subscription via Dasharo Pro Package newsletter.

To verify binary integrity with hash and signature please follow the
instructions in
[Dasharo release signature verification](https://docs.dasharo.com/guides/signature-verification)
using
[this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/dell_optiplex_9010/dasharo-release-0.x-compatible-with-dell-optiplex-x010-signing-key.asc)
.

## v0.1.0 - 2024-09-12

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Dell/OptiPlex_7010_9010/v0.1.0-results.csv).

    This release is compatible with both the Dell OptiPlex 7010 and 9010
    platforms, as they're essentially identical from a hardware standpoint.
    However, we have only tested the release on a 7010 unit. We cannot formally
    guarantee that the same scope of features will be functional on a 9010 unit
    - therefore we encourage all recipients to test the release personally, if
    they have a 9010 platform, and report any potential issues.

### Added

- Support for Dell OptiPlex 7010/9010
- [UEFI Boot Support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface/)
- [Configurable boot order](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/325-custom-boot-order/)
- Configurable boot options
- [UEFI Secure Boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [Custom boot logo](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/304-custom-logo/)
- [Dasharo setup menu full screen mode support](https://github.com/Dasharo/dasharo-issues/issues/118)
- [SMM BIOS write protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Firmware update mode](https://docs.dasharo.com/guides/firmware-update/#firmware-update-mode)
- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
- [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Network stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#networking-options)
- [Serial Console Redirection option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#serial-port-configuration)

### Known issues

- [Network Boot enabled by default](https://github.com/Dasharo/dasharo-issues/issues/979)
- [Wake by USB keyboard not working](https://github.com/Dasharo/dasharo-issues/issues/1044)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 24.02 revision 83c8b094](https://github.com/Dasharo/coreboot/tree/83c8b094)
- [Dasharo EDKII fork based on edk2-stable202405 revision ae0ecedb](https://github.com/Dasharo/edk2/tree/ae0ecedb)
- [Dasharo iPXE fork based on 838611b34e revision 838611b3](https://github.com/Dasharo/ipxe/tree/838611b3)
- [Intel microcode based on IVB E1/L1 0x00000021 revision microcode-20240531](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240531/intel-ucode/06-3a-09)
- [Intel microcode based on SNB D2/G1/Q0 0x0000002f revision microcode-20240531](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240531/intel-ucode/06-2a-07)
