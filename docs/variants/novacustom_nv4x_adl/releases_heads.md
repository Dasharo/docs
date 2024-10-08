# NovaCustom NV4x 12th Gen Dasharo (coreboot + heads) Release Notes

Following Release Notes describe status of development of Dasharo (coreboot +
Heads) firmware for NovaCustom NV4x 12th Gen.

## v0.9.1 - 2024-06-27

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1yWZ--zFPIsQhXZByf7nJIrasQYuRSf1yCi60lY_RGsQ/edit#gid=2042954457).

### Fixed

- [NK3 not detected/discovered at OEM Factory Reset/Re-Ownership](https://github.com/Dasharo/dasharo-issues/issues/831)
- [NK3 v1.7.1 firmware update compatibility](https://www.nitrokey.com/blog/2024/heads-v25-and-nitrokey-3-firmware-v171-security-update)
- [Heads shuts down instead of rebooting](https://github.com/Dasharo/dasharo-issues/issues/711)
- [Laptop boots when plugging in the power adapter](https://github.com/Dasharo/dasharo-issues/issues/766)

### Known issues

- [Power button does not work in Qubes](https://github.com/Dasharo/dasharo-issues/issues/710)
- [Existing Qubes installation is not found as bootable after transition back to EDK2](https://github.com/Dasharo/dasharo-issues/issues/713)
- [Builds are not fully reproducible](https://github.com/linuxboot/heads/issues/1616)

### Binaries

[sha256][novacustom_nv4x_adl_v0.9.1_heads.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_v0.9.1_heads.rom_sig]{.md-button}

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-entry-subscription-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Pro Package newsletter.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://github.com/3mdeb/3mdeb-secpack/blob/master/customer-keys/novacustom/dasharo-release-0.9.x-for-novacustom-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo heads fork based on v0.2.0 revision 0fb3886f](https://github.com/Dasharo/heads/tree/0fb3886f)
- [Dasharo coreboot fork based on 4.21 revision 3a9aa3a4](https://github.com/Dasharo/coreboot/tree/3a9aa3a4)
- [Intel Management Engine based on v16.1.30.2307 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/novacustom/nv4x_adl/me.bin)
- [Intel Flash Descriptor based on v1.0 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/novacustom/nv4x_adl/descriptor.bin)
- [Intel Firmware Support Package based on ADL-P C.1.75.10 revision 481ea7cf](https://github.com/intel/FSP/tree/481ea7cf/AlderLakeFspBinPkg/Client/AlderLakeP)
- [Intel microcode based on ADL L0/R0 0x0000042c revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-9a-04)
- [Intel microcode based on RPL J0/Q0 0x00004119 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-ba-02)

## v0.9.0 - 2024-02-29

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1yWZ--zFPIsQhXZByf7nJIrasQYuRSf1yCi60lY_RGsQ/edit#gid=2042954457).

### Changed

- [This is a Dasharo Pro Package release](https://docs.dasharo.com/dev-proc/versioning/#dasharo-entry-subscription-releases)
- Heads Linux is used as a payload

### Known issues

- [Power button does not work in Qubes](https://github.com/Dasharo/dasharo-issues/issues/710)
- [Heads shuts down instead of rebooting](https://github.com/Dasharo/dasharo-issues/issues/711)
- [Existing Qubes installation is not found as bootable after transition back to EDK2](https://github.com/Dasharo/dasharo-issues/issues/713)
- [Builds are not fully reproducible](https://github.com/linuxboot/heads/issues/1616)

### Binaries

[sha256][novacustom_nv4x_adl_v0.9.0_heads.rom_hash]{.md-button}
[sha256.sig][novacustom_nv4x_adl_v0.9.0_heads.rom_sig]{.md-button}

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-entry-subscription-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Pro Package newsletter.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://github.com/3mdeb/3mdeb-secpack/blob/master/customer-keys/novacustom/dasharo-release-0.9.x-for-novacustom-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo heads fork based on v0.2.0 revision ccf49703](https://github.com/Dasharo/heads/tree/ccf49703)
- [Dasharo coreboot fork based on 4.21 revision 3a9aa3a4](https://github.com/Dasharo/coreboot/tree/3a9aa3a4)
- [Intel Management Engine based on v16.1.30.2307 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/novacustom/nv4x_adl/me.bin)
- [Intel Flash Descriptor based on v1.0 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/novacustom/nv4x_adl/descriptor.bin)
- [Intel Firmware Support Package based on ADL-P C.1.75.10 revision 481ea7cf](https://github.com/intel/FSP/tree/481ea7cf/AlderLakeFspBinPkg/Client/AlderLakeP)
- [Intel microcode based on ADL L0/R0 0x0000042c revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-9a-04)
- [Intel microcode based on RPL J0/Q0 0x00004119 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-ba-02)

[novacustom_nv4x_adl_v0.9.0_heads.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/heads/v0.9.0/novacustom_nv4x_adl_v0.9.0_heads.rom.sha256
[novacustom_nv4x_adl_v0.9.0_heads.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_nv4x_adl/heads/v0.9.0/novacustom_nv4x_adl_v0.9.0_heads.rom.sha256.sig
