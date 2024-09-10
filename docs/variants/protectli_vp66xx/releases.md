# Release Notes

Following Release Notes describe status of Open Source Firmware development
for Protectli VP6630/VP6650/VP6670

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>
[Subscribe to Protectli VP6630/VP6650/VP6670 Dasharo Release Newsletter]
[newsletter]{.md-button .md-button--primary .center}
</center>

Test results for this platform can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/VP66xx/).

## v0.9.0 - 2024-09-10

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/VP66xx/v0.9.0-results.csv)

### Added

- Initial support for Protectli Alder Lake devices VP66xx
- [UEFI compatible interface](../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md)
- [Support for discrete TPM](../../unified-test-documentation/dasharo-security/200-tpm-support.md)
- [UEFI Secure Boot support](../../unified-test-documentation/dasharo-security/206-secure-boot.md)
- [Boot logo customization support](../../unified-test-documentation/dasharo-compatibility/328-logo-customization-functionality.md)
- [USB boot support](../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md)
- [NVMe boot support](../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md)
- [TPM Measured Boot](../../unified-test-documentation/dasharo-security/203-measured-boot.md)
- [UEFI Shell](../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md)
- [UEFI Secure Boot](../../unified-test-documentation/dasharo-security/206-secure-boot.md)
- [Network boot](../../unified-test-documentation/dasharo-compatibility/315b-netboot-utilities.md)
- [Windows 11 booting](../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md)
- [Ubuntu LTS booting](../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md)
- [Serial port console redirection](../../unified-test-documentation/dasharo-compatibility/31G-ec-and-superio.md#sio004001-serial-port-in-firmware)
- [Vboot Verified Boot](../../unified-test-documentation/dasharo-security/201-verified-boot.md)
- [Intel ME HAP disable](../../unified-test-documentation/dasharo-security/20F-me-neuter.md)
- [BIOS flash protection for Vboot recovery region](../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md)
- [Setup menu password configuration](../../dasharo-menu-docs/overview.md#dasharo-menu-guides)
- [SMM BIOS write protection](../../dasharo-menu-docs/dasharo-system-features.md#dasharo-security-options)
- [USB stack disable option in setup menu](../../dasharo-menu-docs/dasharo-system-features.md#usb-configuration)
- [Network stack disable option in setup menu](../../dasharo-menu-docs/dasharo-system-features.md#networking-options)

## Known Issues

- [Display Port has trouble working with certain monitors](
    https://github.com/Dasharo/dasharo-issues/issues/1015)
- [STB002.001 encounters unlisted errors](
    https://github.com/Dasharo/dasharo-issues/issues/1013)

[newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL

<!--Empty pixel to avoid orphaned pages when overview is hidden-->
[![empty-pixel](../../images/empty_pixel.png)](overview.md)
