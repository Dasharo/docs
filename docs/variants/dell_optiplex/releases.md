# Dell OptiPlex 7010/9010 Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
Dell OptiPlex 7010/9010

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

[Subscribe to Dell OptiPlex 7010/9010 Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

</center>

## v0.1.0 - 2024-09-12

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Dell/OptiPlex_7010_9010/v0.1.0-results.csv).

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

[newsletter]: https://newsletter.3mdeb.com/subscription/MY3m7fLpz
