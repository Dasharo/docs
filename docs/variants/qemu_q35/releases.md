# emulation qemu_q35 Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
QEMU Q35 (Emulator).

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

## v0.2.1 - 2025-05-30

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/QEMU/Q35/v0.2.1_results.csv).

### Changed

- The Local APIC timer is now used instead of the HPET

### Fixed

- The time in the firmware flows at a correct pace now resulting in much
  quicker boot times.

### Known issues

- [Measured Boot PCR values don't match the TPM measurement log](https://github.com/Dasharo/dasharo-issues/issues/1354)

### Binaries

Binaries can be found in
[GitHub release](https://github.com/Dasharo/coreboot/releases/tag/qemu_q35_v0.2.1).

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.03 revision b8e6b3eb](https://github.com/Dasharo/coreboot/tree/b8e6b3eb)
    + [License](https://github.com/Dasharo/coreboot/blob/b8e6b3eb/COPYING)
- [Dasharo EDKII fork based on edk2-stable202502 revision e8cd1856](https://github.com/Dasharo/edk2/tree/e8cd1856)
    + [License](https://github.com/Dasharo/edk2/blob/e8cd1856/License.txt)
- [Dasharo iPXE fork based on 2024.07 revision 63ed3e35](https://github.com/Dasharo/ipxe/tree/63ed3e35)
    + [License](https://github.com/Dasharo/ipxe/blob/63ed3e35/COPYING.GPLv2)

## v0.2.0 - 2024-06-26

Tests reports and logs can be found
[here](https://dl.3mdeb.com/open-source-firmware/Dasharo/qemu/q35/v0.2.0/).
This release is the first `Dasharo (coreboot+UEFI)` image, contrary to
`Dasharo (UEFI)` used previously. This makes QEMU Q35 more similar to other
platforms, which hopefully will make testing on it more viable.

### Added

- Two different variants available, one with only functional menus, and another
  with all Dasharo System Features menus enabled
- Both variants can be created with `build.sh`, both are built by CI
- Full image has the same menus enabled as previous release, but their contents
  are limited by coreboot (e.g. if an option is specific to SoC).

### Changed

- Firmware image now contains coreboot, in addition to edk2. This changes the
  way some things work:
    + UEFI variables are saved in SMMSTORE, as in other platforms supported by
      Dasharo.
    + Availability of some menu options is controlled by coreboot, and may
      differ based on the way QEMU is started. Examples of this are CPU
      Configuration menu (its content depends on `-smp` parameter) and lack of
      flash protection mechanisms.
    + OVMF package isn't used, instead a common DasharoPlatformPkg is. This
      makes this release more in line with the rest of Dasharo platforms.
- Debug output is printed on serial output, instead of dedicated `debugcon`.
  This makes it easier to synchronize output from coreboot, edk2 and OS.

### Known issues

- [Virtio drivers are not available in the firmware](https://github.com/Dasharo/dasharo-issues/issues/901).
  It is possible to install OS on disk mounted with `if=virtio`, however, it
  won't be detected by UEFI and won't be bootable because of that.
- [S3 doesn't work](https://github.com/Dasharo/dasharo-issues/issues/902).
- [Booting is slow](https://github.com/Dasharo/dasharo-issues/issues/898).
- [`Reset to Defaults` doesn't work as it should](https://github.com/Dasharo/dasharo-issues/issues/887).
    + Another manifestation of the same issue is that build fails if [Watchdog
      configuration menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#chipset-configuration)
      is enabled. This option has been disabled even in full variant until
      resolved.

### Binaries

Binaries can be found in
[GitHub release](https://github.com/Dasharo/coreboot/releases/tag/qemu_q35_v0.2.0).

### SBOM

- [Dasharo coreboot fork based on 0a280ff7 revision 26c5df90](https://github.com/Dasharo/coreboot/tree/26c5df90)
- [Dasharo EDK II fork based on edc66812 revision 11b26796](https://github.com/Dasharo/edk2/tree/11b26796)
- [Dasharo iPXE fork based on fa622132 revision 838611b3](https://github.com/Dasharo/ipxe/commit/838611b3)

## v0.1.0 - 2023-12-06

Tests reports and logs can be found
[here](https://dl.3mdeb.com/open-source-firmware/Dasharo/qemu/q35/v0.1.0/).

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

Following features are visible in setup menu and can be used for testing the
menus, but have no actual backend hooked up:

- [PS/2 Controller enable/disable option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#chipset-configuration)
- [Watchdog configuration menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#chipset-configuration)
- [Early boot DMA protection menu option](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20L-early-boot-dma-protection/)
- [Intel ME disable support and menu options](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20F-me-neuter/)
- [SED/OPAL disk password support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/208-opal-disk-password-support/)
- [SATA disk password support](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#hdd-security-configuration)
- SMM BIOS Write Protection support and enable/disable option
- [USB stack and mass storage enable/disable option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Firmware Update Mode feature](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [One of the two fan profiles can now be selected in Setup Menu](https://docs.dasharo.com/unified/novacustom/features/)
- [Setup menu option for switching between S0ix and S3 suspend mode](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Wi-Fi / Bluetooth module disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Built-in webcam disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Battery threshold options in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [PCIe Configuration menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#pcipcie-configuration)
- [Memory configuration menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#memory-configuration)
  [Power state after power fail option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)

### Binaries

Binaries can be found in
[GitHub release](https://github.com/Dasharo/edk2/releases/tag/qemu_q35_v0.1.0).

### SBOM

- [Dasharo EDKII fork based on dd7523b5b1 revision 11746340](https://github.com/Dasharo/edk2/tree/11746340)
- [iPXE revision 77b07ea4](https://github.com/ipxe/ipxe/tree/77b07ea4)
