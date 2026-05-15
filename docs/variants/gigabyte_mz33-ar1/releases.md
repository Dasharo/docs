# Gigabyte MZ33-AR1 Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development
for Gigabyte MZ33-AR1.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

{{ subscribe_form("54954349-8626-4c32-836f-90e9738c0510",
"Subscribe to Gigabyte MZ33-AR1 Dasharo Release Newsletter") }}

</center>

!!! note "Note"

    Before using this firmware, please review the [Dasharo Terms of
    Service](https://www.dasharo.com/pages/terms/) and AMD's [openSIL project
    page](https://github.com/openSIL/openSIL), which describes openSIL's
    current Proof-of-Concept status and AMD's evaluation-only support model.
    Use of this firmware is at the user's own responsibility.

## v0.9.0 - 2026-05-14

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Gigabyte/MZ33-AR1/v0.9.0_results.csv).

### Added

- Initial support for the Gigabyte MZ33-AR1 server board, based on AMD Turin
- [UEFI compatible interface](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface/)
- [Configurable boot order](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/325-custom-boot-order/)
- Configurable boot options
- [UEFI Secure Boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [USB boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31N-usb-boot/)
- [NVMe boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/312-nvme-support/)
- [Ubuntu LTS booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support/)
- [Windows 11 booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31A-windows-booting/)
- [Serial port console redirection](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31G-ec-and-superio/#sio004001-serial-port-in-firmware)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [SMM BIOS write protection with AMD ROM Armor](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Firmware update mode](https://docs.dasharo.com/guides/firmware-update/#firmware-update-mode)
- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
- [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Network stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#networking-options)
- TPM PPI support with UEFI variable backend
- [SBOM generation for AMD PSP blobs](https://doc.coreboot.org/sbom/sbom.html)
- AMD SME and AMD SEV-SNP support
- [UEFI Capsule Updarte v1 support](https://docs.dasharo.com/unified-test-documentation/dasharo-stability/capsule-update/)
- Rebased coreboot on 25.12 tag
- Rebased iPXE on last commit of February 2026
- [Option to customize the SMBIOS Serial Number and UUID](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/362-dcu/)
- Support for firmware flashing via BMC with RBU files
- [TCG OPAL disk password support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/208-opal-disk-password-support/)
- SATA disk password support
- [Boot manager menu disable option](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20P-boot-menu/)
- [Auto boot option creation for pre-installed OSes](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/361-esp-scanning/)
- Early graphical sign of life
- Quiet boot/Fast boot options
- AMD memory context save/restore support
- SMBIOS 3.8.0 specification support
- AMD PSP HSTI reporting to reach fwupd HSI2 level and fulfill HSI4 requirements
- AMD CPU temperature reporting via ACPI Thermal Zone

### Known issues

- [UEFI Capsules do not survive resets, only immediate Capsule on Disk supported](https://github.com/Dasharo/dasharo-issues/issues/1843)
- [Previous power state restoration does not work for powered off state](https://github.com/Dasharo/dasharo-issues/issues/1844)
- [I3C controller initialization fails in Linux](https://github.com/Dasharo/dasharo-issues/issues/1845)
- [Fast Boot does not reduce boot time](https://github.com/Dasharo/dasharo-issues/issues/1841)
- [Firmware flashing and reset to defaults do not give the same measurements](https://github.com/Dasharo/dasharo-issues/issues/1842)

### Binaries

{{ tos_checkbox("gigabyte-mz33-ar1-v090-binaries") }}

<div id="gigabyte-mz33-ar1-v090-binaries" class="tos-gate-content" markdown="1" style="display: none">

#### Raw Dasharo image

[sha256][gigabyte_mz33_ar1_v0.9.0.rom_hash]{.md-button}
[sha256.sig][gigabyte_mz33_ar1_v0.9.0.rom_sig]{.md-button}
(gigabyte_mz33_ar1_v0.9.0.rom)

#### Update via BMC image

[sha256][gigabyte_mz33_ar1_v0.9.0.rbu_hash]{.md-button}
[sha256.sig][gigabyte_mz33_ar1_v0.9.0.rbu_sig]{.md-button}
(gigabyte_mz33_ar1_v0.9.0.rbu)

#### SBOM CycloneDX

[gigabyte_mz33_ar1_v0.9.0.sbom.json][gigabyte_mz33_ar1_v0.9.0.sbom.json_file]{.md-button}
[sha256][gigabyte_mz33_ar1_v0.9.0.sbom.json_hash]{.md-button}
[sha256.sig][gigabyte_mz33_ar1_v0.9.0.sbom.json_sig]{.md-button}

</div>

This is a Dasharo Pro Package release. For this platform, access to pre-built
binaries is provided exclusively through the
[Full Build for Gigabyte MZ33-AR1](https://shop.3mdeb.com/product/full-build-gigabyte-mz33-ar1-with-dasharo-corebootuefi-pro-package-for-servers/),
a bundled hardware-and-firmware product available in
the 3mdeb shop. A standalone Dasharo Pro Package subscription is not offered
for this platform; additional purchase options (Enterprise Build and Barebones
Build) are expected in the next 3-6 months.

With the Full Build, you receive firmware updates for the duration of your
subscription via the Dasharo Pro Package newsletter, and gain entry to the
Dasharo Premier Support invite-only live chat on the Matrix network, enabling
direct engagement with the Dasharo Team and fellow subscribers for
personalized, priority assistance.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/gigabyte_mz33-ar1/dasharo-release-0.x-compatible-with-gigabyte-mz33-ar1-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.12 revision b7796125](https://github.com/Dasharo/coreboot/tree/b7796125)
    + [License](https://github.com/Dasharo/coreboot/blob/b7796125/COPYING)
- [Dasharo EDKII fork based on edk2-stable202502 revision eedcdea6](https://github.com/Dasharo/edk2/tree/eedcdea6)
    + [License](https://github.com/Dasharo/edk2/blob/eedcdea6/License.txt)
- [Dasharo iPXE fork based on 2026.02 revision ad8cbcee](https://github.com/Dasharo/ipxe/tree/ad8cbcee)
    + [License](https://github.com/Dasharo/ipxe/blob/ad8cbcee/COPYING.GPLv2)
- [AMD openSIL based on turin_poc revision df18968a](https://github.com/openSIL/openSIL/tree/df18968a)
    + [License](https://github.com/openSIL/openSIL/blob/genoa_poc/LICENSE/MIT-License.txt)

An [integrated SBOM](https://doc.coreboot.org/sbom/sbom.html) is also
included in the firmware images. It describes a complete set of components
and their versions used to build the firmware images. The published SBOM
artifact is in CycloneDX format and can be viewed by SBOM tools, for example
[sbom-tools](https://github.com/sbom-tool/sbom-tools).

[gigabyte_mz33_ar1_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/gigabyte_mz33_ar1/uefi/v0.9.0/gigabyte_mz33_ar1_v0.9.0.rom.sha256
[gigabyte_mz33_ar1_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/gigabyte_mz33_ar1/uefi/v0.9.0/gigabyte_mz33_ar1_v0.9.0.rom.sha256.sig

[gigabyte_mz33_ar1_v0.9.0.rbu_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/gigabyte_mz33_ar1/uefi/v0.9.0/gigabyte_mz33_ar1_v0.9.0.rbu.sha256
[gigabyte_mz33_ar1_v0.9.0.rbu_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/gigabyte_mz33_ar1/uefi/v0.9.0/gigabyte_mz33_ar1_v0.9.0.rbu.sha256.sig

[gigabyte_mz33_ar1_v0.9.0.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/gigabyte_mz33_ar1/uefi/v0.9.0/gigabyte_mz33_ar1_v0.9.0.sbom.json
[gigabyte_mz33_ar1_v0.9.0.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/gigabyte_mz33_ar1/uefi/v0.9.0/gigabyte_mz33_ar1_v0.9.0.sbom.json.sha256
[gigabyte_mz33_ar1_v0.9.0.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/gigabyte_mz33_ar1/uefi/v0.9.0/gigabyte_mz33_ar1_v0.9.0.sbom.json.sha256.sig
