# Hardkernel ODROID H4 Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
Hardkernel ODROID H4

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

{{ subscribe_form("97b9ea9e-7b59-4160-9779-c0348f0debce",
"Subscribe to Hardkernel ODROID H4 Dasharo Release Newsletter") }}

</center>

## v0.9.0 - 2025-08-12

### Added

- Initial support for the Hardkernel ODROID H4 device, based on Intel Alder
  Lake N
- [UEFI compatible interface](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface/)
- [USB boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31N-usb-boot/)
- [NVMe boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/312-nvme-support/)
- [UEFI Shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
- [Ubuntu LTS booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support/)
- [Serial port console redirection](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31G-ec-and-superio/#sio004001-serial-port-in-firmware)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [Verified Boot](https://slimbootloader.github.io/security/verified-boot.html)
- [Measured Boot](https://slimbootloader.github.io/security/measured-boot.html)

### Known issues

- [Universal Payload hangs when SMM and SPI variable support is enabled](https://github.com/Dasharo/dasharo-issues/issues/1485)
- [Dasharo (Slim Bootloader+UEFI) - Can't shutdown via power button in BIOS](https://github.com/Dasharo/dasharo-issues/issues/1513)
- [Dasharo (Slim Bootloader + UEFI) freezes when trying to read flash](https://github.com/Dasharo/dasharo-issues/issues/1494)

### Binaries

[sha256][hardkernel_odroid_h4_v0.9.0_slim_bootloader_uefi.rom_hash]{.md-button}
[sha256.sig][hardkernel_odroid_h4_v0.9.0_slim_bootloader_uefi.rom_sig]{.md-button}

[sha256][hardkernel_odroid_h4_v0.9.0_slim_bootloader_uefi_dev_signed.rom_hash]{.md-button}
[sha256.sig][hardkernel_odroid_h4_v0.9.0_slim_bootloader_uefi_dev_signed.rom_sig]{.md-button}

This is a Dasharo Pro Package Release. To access the pre-built binaries, you
need to [subscribe to the Dasharo Pro Package
subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our
[shop](https://shop.3mdeb.com/shop/dasharo-pro-package/dasharo-slim-bootloaderuefi-pro-package-for-network-appliance/).
As a subscriber, you will receive access to all firmware updates for the
duration of your subscription via the Dasharo Pro Package newsletter, and gain
entry to the Dasharo Premier Support invite-only live chat on the Matrix
network, enabling direct engagement with the Dasharo Team and fellow
subscribers for personalized, priority assistance.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/hardkernel_odroid_h4/dasharo-release-0.x-compatible-with-hardkernel-odroid-h4-family-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo Slim Bootloader fork based on d888673acdc4cf92bb5ebf4d8e73e66222654596 revision 00796934](https://github.com/Dasharo/slimbootloader/tree/00796934)
    + [License](https://github.com/Dasharo/slimbootloader/blob/00796934/LICENSE)
- [TianoCore EDKII based on edk2-stable202505 revision 6951dfe7](https://github.com/tianocore/edk2/tree/6951dfe7)
    + [License](https://github.com/tianocore/edk2/blob/6951dfe7/License.txt)
- [Intel Management Engine version v16.50.10.1351](https://github.com/Dasharo/dasharo-blobs/blob/cbfff4d0/hardkernel/odroid_h4/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/cbfff4d0/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.1](https://github.com/Dasharo/dasharo-blobs/blob/cbfff4d0/hardkernel/odroid_h4/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/cbfff4d0/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version IoT ADL-N IPU25.3 (6114_00)](https://github.com/intel/FSP/commits/15848ee4934acbd94069454f369e9869bb0f1295/AlderLakeFspBinPkg/IoT/AlderLakeN)
    + [License](https://github.com/intel/FSP/blob/15848ee4934acbd94069454f369e9869bb0f1295/FSP_License.pdf)
- [Intel microcode version ADL-N 0x1d 06/12/2024](https://github.com/slimbootloader/firmwareblob/tree/58900f79bf77d5032ce85cf4196b640123e316d8/m_19_b06e0_0000001d.mcb)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/58900f79bf77d5032ce85cf4196b640123e316d8/Microcode/AlderLake/IntelMicrocodeLicense.txt)
- [Intel microcode version ADL-S 0x3a 12/12/2024](https://github.com/slimbootloader/firmwareblob/tree/58900f79bf77d5032ce85cf4196b640123e316d8/m_07_90672_0000003a.mcb)
    + [License](https://github.com/slimbootloader/firmwareblob/blob/58900f79bf77d5032ce85cf4196b640123e316d8/Microcode/AlderLake/IntelMicrocodeLicense.txt)
- [Intel microcode version ADL-P 0x434 22/02/2024](https://github.com/slimbootloader/firmwareblob/tree/58900f79bf77d5032ce85cf4196b640123e316d8/m_80_906a3_00000434.mcb)
    + [License](https://github.com/slimbootloader/firmwareblob/blob/58900f79bf77d5032ce85cf4196b640123e316d8/Microcode/AlderLake/IntelMicrocodeLicense.txt)

[hardkernel_odroid_h4_v0.9.0_slim_bootloader_uefi.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.0/hardkernel_odroid_h4_v0.9.0_slim_bootloader_uefi.rom.sha256
[hardkernel_odroid_h4_v0.9.0_slim_bootloader_uefi.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.0/hardkernel_odroid_h4_v0.9.0_slim_bootloader_uefi.rom.sha256.sig
[hardkernel_odroid_h4_v0.9.0_slim_bootloader_uefi_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.0/hardkernel_odroid_h4_v0.9.0_slim_bootloader_uefi_dev_signed.rom.sha256
[hardkernel_odroid_h4_v0.9.0_slim_bootloader_uefi_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/hardkernel_odroid_h4/uefi/v0.9.0/hardkernel_odroid_h4_v0.9.0_slim_bootloader_uefi_dev_signed.rom.sha256.sig
