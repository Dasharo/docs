# MSI PRO B850-P WIFI Dasharo Release Notes

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries, you need to [subscribe to the Dasharo Pro Package
subscriber](https://docs.dasharo.com/ways-you-can-help-us/#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our
[shop](https://shop.3mdeb.com/shop/dasharo-pro-package/1year-desktop/). As a
subscriber, you will receive access to all firmware updates for the duration
of your subscription via the Dasharo Pro Package newsletter, and gain entry to
the Dasharo Premier Support invite-only live chat on the Matrix network,
enabling direct engagement with the Dasharo Team and fellow subscribers for
personalized, priority assistance.

Following Release Notes describe status of Open Source Firmware development
for MSI PRO B850-P WIFI.

For detailed information on our validation setup, please refer to the
[Hardware Configuration Matrix](hardware-matrix.md).

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("0c1e3004-3e81-49f5-8bd4-422d5f3da63a",
"Subscribe to Dasharo compatible with MSI PRO B850-P WIFI Newsletter") }}

## v0.9.0 - 2026-07-30

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/msi/ms7e56/v0.9.0-results.csv).

### Added

- Initial support for the MSI PRO B850-P WIFI board, based on AMD Phoenix
- [UEFI compatible interface](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface/)
- [Configurable boot order](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/325-custom-boot-order/)
- Configurable boot options
- [UEFI Secure Boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [USB boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31N-usb-boot/)
- [NVMe boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/312-nvme-support/)
- [Ubuntu LTS booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support/)
- [Windows 11 booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31A-windows-booting/)
- [Serial port console redirection](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31G-ec-and-superio/#sio004001-serial-port-in-firmware)
- [AMD fTPM support in coreboot and EDK2 UEFI Payload](https://docs.dasharo.com/unified-test-documentation/dasharo-security/200-tpm-support/)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [SMM BIOS write protection with AMD ROM Armor 3](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Firmware update mode](https://docs.dasharo.com/guides/firmware-update/#firmware-update-mode)
- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
- [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Network stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#networking-options)
- TPM PPI support with UEFI variable backend
- [SBOM generation for AMD PSP blobs, video and LAN drivers](https://doc.coreboot.org/sbom/sbom.html)
- [UEFI Capsule Update v1 support](https://docs.dasharo.com/unified-test-documentation/dasharo-stability/capsule-update/)
- Rebased coreboot on 25.12 tag
- Rebased iPXE on last commit of February 2026
- [Support for firmware flashing via MSI FlashBIOS](https://docs.dasharo.com/unified/msi/recovery/#using-msi-flashbios-button)
- [TCG OPAL disk password support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/208-opal-disk-password-support/)
- SATA disk password support
- [Auto boot option creation for pre-installed OSes](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/361-esp-scanning/)
- Quiet boot/Fast boot options
- AMD memory context save/restore support
- SMBIOS 3.8.0 specification support
- AMD CPU temperature reporting via ACPI Thermal Zone
- MSI EZ Debug LED support for DRAM and CPU initialization signaling

### Known issues

- [UEFI Capsules do not survive resets, only immediate Capsule on Disk
  supported](https://github.com/Dasharo/dasharo-issues/issues/1843)
- [Previous power state restoration does not work for powered off
  state](https://github.com/Dasharo/dasharo-issues/issues/1844)
- [Ubuntu 26.04 with serial console sometimes halts during boot on MSI PRO
  B850-P](https://github.com/Dasharo/dasharo-issues/issues/1897)
- [Firmware flashing and reset to defaults do not give the same
  measurements](https://github.com/Dasharo/dasharo-issues/issues/1842)
- [WiFi occasionally disappears on MSI PRO B850-P
  WIFI](https://github.com/Dasharo/dasharo-issues/issues/1896)

### Binaries

#### Raw Dasharo image

[sha256][msi_ms7e56_v0.9.0.rom_hash]{.md-button}
[sha256.sig][msi_ms7e56_v0.9.0.rom_sig]{.md-button}
(msi_ms7e56_v0.9.0.rom)

#### SBOM CycloneDX

[msi_ms7e56_v0.9.0.sbom.json][msi_ms7e56_v0.9.0.sbom.json_file]{.md-button}
[sha256][msi_ms7e56_v0.9.0.sbom.json_hash]{.md-button}
[sha256.sig][msi_ms7e56_v0.9.0.sbom.json_sig]{.md-button}

This is a Dasharo Pro Package release. For this platform, access to pre-built
binaries is provided exclusively through the
[Full Build for MSI PRO B850-P WIFI](https://shop.3mdeb.com/product/dasharo-full-pc-build-msi-pro-b850-p-wifi-ddr5/),
a bundled hardware-and-firmware product available in
the 3mdeb shop. A standalone Dasharo Pro Package subscription is not offered
for this platform.

With the Full Build, you receive firmware updates for the duration of your
subscription via the Dasharo Pro Package newsletter, and gain entry to the
Dasharo Premier Support invite-only live chat on the Matrix network, enabling
direct engagement with the Dasharo Team and fellow subscribers for
personalized, priority assistance.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/refs/heads/master/dasharo/msi_ms7e06/dasharo-release-0.x-compatible-with-msi-ms-7e06-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.12 revision 713a0b76](https://github.com/Dasharo/coreboot/tree/713a0b76)
    + [License](https://github.com/Dasharo/coreboot/blob/713a0b76/COPYING)
- [Dasharo EDKII fork based on edk2-stable202602 revision baafe898](https://github.com/Dasharo/edk2/tree/baafe898)
    + [License](https://github.com/Dasharo/edk2/blob/baafe898/License.txt)
- [Dasharo iPXE fork based on 2026.02 revision ad8cbcee](https://github.com/Dasharo/ipxe/tree/ad8cbcee)
    + [License](https://github.com/Dasharo/ipxe/blob/ad8cbcee/COPYING.GPLv2)
- [AMD openSIL based on phoenix_poc revision e71fca32](https://github.com/3mdeb/openSIL/tree/e71fca32)
    + [License](https://github.com/3mdeb/openSIL/blob/genoa_poc/LICENSE/MIT-License.txt)

An [integrated SBOM](https://doc.coreboot.org/sbom/sbom.html) is also
included in the firmware images. It describes a complete set of components
and their versions used to build the firmware images. The published SBOM
artifact is in CycloneDX format and can be viewed by SBOM tools, for example
[sbom-tools](https://github.com/sbom-tool/sbom-tools).

[msi_ms7e56_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e56/uefi/v0.9.0/msi_ms7e56_v0.9.0.rom.sha256
[msi_ms7e56_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e56/uefi/v0.9.0/msi_ms7e56_v0.9.0.rom.sha256.sig

[msi_ms7e56_v0.9.0.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e56/uefi/v0.9.0/msi_ms7e56_v0.9.0.sbom.json
[msi_ms7e56_v0.9.0.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e56/uefi/v0.9.0/msi_ms7e56_v0.9.0.sbom.json.sha256
[msi_ms7e56_v0.9.0.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e56/uefi/v0.9.0/msi_ms7e56_v0.9.0.sbom.json.sha256.sig
