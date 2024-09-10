# Release Notes

Following Release Notes describe status of Open Source Firmware development
for Protectli V1000 series

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>
[Subscribe to Protectli V1000 series Dasharo Release Newsletter]
[newsletter]{.md-button .md-button--primary .center}
</center>

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit#gid=1316498194).

[newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL

<!--Empty pixel to avoid orphaned pages when overview is hidden-->
[![empty-pixel](../../images/empty_pixel.png)](../../unified/protectli/overview.md)

## Protectli V1210 Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
Protectli V1210

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

[Subscribe to Protectli V1210 Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

</center>

### v0.9.3 - 2024-09-09

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit?gid=1207991922#gid=1207991922).

#### Added

- Intel-specific HDA verbs, for proper audio functionality

#### Changed

- Disabled DSP
- Disabled SATA due to lack of HW support
- Disabled SSID programming to prevent Windows default drives from not probing
  successfully
- Removed differences in SMBIOS fields compared to proprietary FW
- Disabled WiFi L0 to prevent errors from showing up in dmesg

#### Known Issues

- There is no PC speaker populated on the platform, so it does not give sound
  signals on errors and boot
- The chassis is getting very hot

#### Binaries

[protectli_v1210_v0.9.3.rom][protectli_v1210_v0.9.3.rom_file]{.md-button}
[sha256][protectli_v1210_v0.9.3.rom_hash]{.md-button}
[sha256.sig][protectli_v1210_v0.9.3.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/dasharo-open-source-firmware-engineering-release-signing-key.asc)

#### SBOM (Software Bill of Materials)

- [coreboot based on 4.21 revision ee437086](https://github.com/Dasharo/coreboot/tree/ee437086)
    + [License](https://github.com/Dasharo/coreboot/blob/ee437086/COPYING)
- [Dasharo EDKII fork based on f06673308f revision f0667330](https://github.com/Dasharo/edk2/tree/f0667330)
    + [License](https://github.com/Dasharo/edk2/blob/f0667330/License.txt)
- [Dasharo iPXE fork based on 838611b34e revision 838611b3](https://github.com/Dasharo/ipxe/tree/838611b3)
    + [License](https://github.com/Dasharo/ipxe/blob/838611b3/COPYING.GPLv2)
- [Intel Management Engine based on v13.50.27.1987 revision 9712e97a](https://github.com/Dasharo/dasharo-blobs/blob/9712e97a/protectli/vault_jsl/)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor based on v1.0 revision 9712e97a](https://github.com/Dasharo/dasharo-blobs/blob/9712e97a/protectli/vault_jsl/)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package based on JSL 2021/08/23 v2115 revision 9712e97a](https://github.com/Dasharo/dasharo-blobs/blob/9712e97a/protectli/vault_jsl/JasperLakeFspBinPkg)
    + [License](https://github.com/intel/FSP/blob/9712e97a/FSP_License.pdf)
- [Intel microcode based on JSL A0 0x24000026 revision microcode-20240312](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240312/intel-ucode/06-9c-00)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240312/license)

[newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
[protectli_v1210_v0.9.3.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1210_v0.9.3.rom
[protectli_v1210_v0.9.3.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1210_v0.9.3.rom.sha256
[protectli_v1210_v0.9.3.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_jsl/v0.9.3/protectli_v1210_v0.9.3.rom.sha256.sig
