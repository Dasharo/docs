# Dasharo compatible with Dell OptiPlex 7010/9010 SFF

**Please read the [overview page](overview.md) first!**

Following Release Notes describe status of Open Source Firmware development for
Dell OptiPlex 7010 SFF, DT and Dell OptiPlex 9010 SFF, MT.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

## v0.1.0

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Dell/OptiPlex_7010_9010/results.csv).

### Added

- Support for Dell OptiPlex 7010/9010
- [UEFI Boot Support](../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md)
- [Configurable boot order](../../unified-test-documentation/dasharo-compatibility/325-custom-boot-order.md)
- Configurable boot options
- [UEFI Secure Boot support](../../unified-test-documentation/dasharo-security/206-secure-boot.md)
- [Custom boot logo](../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md)
- [Dasharo setup menu full screen mode support](https://github.com/Dasharo/dasharo-issues/issues/118)
- [SMM BIOS write protection](../../dasharo-menu-docs/dasharo-system-features.md#dasharo-security-options)
- [Firmware update mode](../../guides/firmware-update.md#firmware-update-mode)
- [Setup menu password configuration](../../dasharo-menu-docs/overview.md#dasharo-menu-guides)
- [USB stack disable option in setup menu](../../dasharo-menu-docs/dasharo-system-features.md#usb-configuration)
- [Network stack disable option in setup menu](../../dasharo-menu-docs/dasharo-system-features.md#networking-options)
- [Serial Console Redirection option](../../dasharo-menu-docs/dasharo-system-features.md#serial-port-configuration)

### Known issues

- [No ability to set SMM BIOS write protection](https://github.com/Dasharo/dasharo-issues/issues/971)

[Subscribe to Dell OptiPlex 7010/9010 Dasharo Release Newsletter](https://newsletter.3mdeb.com/subscription/8dp1vv5mR)
{ .md-button .md-button--primary .center }
<!--

## Unreleased

Software BOM:

- coreboot 4.12-1428-g20cf396c96 (with additional commits for custom platform
  config and CI YAML)
- EDKII

### Added

- UEFI boot support
- Discrete graphics support
- SATA password
- TCG OPAL password
- configurable boot order
- configurable boot options
- UEFI iPXE for EFI network boot support
- UEFI Secure Boot
- Internal UEFI Shell
- One-time boot feature

### Removed

- Legacy boot support

### Binaries

## v0.1.0 - 2021-01-18

### Added

- Dell OptiPlex 7010 and 9010 platforms supported
- Dasharo bootsplash
- Legacy boot support
- USB, SATA, and NVMe boot supported
- Measured boot with TPM 1.2
- ME neutralized with me_cleaner
- Environmental Controller fan control
- Environmental Controller firmware update support (the DELL EC firmware is
  included in the image, the firmware update process is open-source, but the EC
  firmware code is in binary form only and we have no control over what is
  executed on EC)
- Integrated graphics initialization with open-source libgfxinit library for
  both VGA and 2 DP ports
- Onboard serial port supported

### Binaries

[Dell OptiPlex 7010/9010 Dasharo](TBD){ .md-button }
[SHA256](TBD){ .md-button }
[SHA256.sig](TBD){ .md-button }

[All in one zip](TBD){ .md-button }

### SBOM (Software Bill of Materials)

- [coreboot 4.12-1428-g20cf396c96 (with additional commits for custom platform
  config and CI YAML)](https://github.com/Dasharo/coreboot/compare/dell_optiplex_9010_v0.0.0...dell_optiplex_9010_v0.0.0)
- [SeaBIOS 1.13.0](https://web.archive.org/web/20230415000000*/https://review.coreboot.org/plugins/gitiles/seabios/+/refs/tags/rel-1.13.0)

#### Binary blobs

TBD

-->
