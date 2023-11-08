# Release Notes

Following Release Notes describe status of Open Source Firmware development for
QEMU Q35 (Emulator).

## v0.1.0 - 2023-10-13

### Added

Following features can be fully used:
- Configurable boot order
- Configurable boot options
- [Custom boot menu keys](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key/)
- [UEFI shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
- [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [TPM Support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/200-tpm-support/)
- [Dasharo setup password](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20R-uefi-setup-password/)
- [Serial Port Configuration menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#serial-port-configuration)
- [iPXE network boot](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/315-network-boot/)
- [ESP partition scanning in look for grubx64.efi or shimx64.efi or Windows bootmgr](https://github.com/Dasharo/dasharo-issues/issues/94)

Following features are visible in setup menu and can be used for testing the menus,
but have no actual backend hooked up:
- [PS/2 Controller enable/disable option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#chipset-configuration)
- [Watchdog configuration menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#chipset-configuration)
- [Early boot DMA protection menu option](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20L-early-boot-dma-protection/)
- [Intel ME disable support and menu options](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20F-me-neuter/)
- [SED/OPAL disk password support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/208-opal-disk-password-support/)
- [SATA disk password support](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#hdd-security-configuration)
- SMM BIOS Write Protection support and enable/disable option
- [USB stack and mass storage enable/disable option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Firmware Update Mode feature](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [One of the two fan profiles can now be selected in Setup Menu](https://docs.dasharo.com/unified/novacustom/fan-profiles/)
- [Setup menu option for switching between S0ix and S3 suspend mode](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Wi-Fi / Bluetooth module disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Built-in webcam disable option in setup menu](https://docs.dasharo.com/unified/novacustom/camera-switch/)
- [Battery threshold options in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [PCIe Configuration menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#pcipcie-configuration)
- [Memory configuration menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#memory-configuration)
  [Power state after power fail option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)

### Binaries

https://github.com/Dasharo/edk2/releases

### SBOM

- [Dasharo EDKII fork based on dd7523b5b1 revision TBD](https://github.com/Dasharo/edk2/tree/TBD)
