# MSI PRO Z790-P (WIFI) (DDR4) Dasharo (coreboot + Heads) Release Notes

Following Release Notes describe status of Dasharo (coreboot + Heads) firmware
development compatible with MSI PRO Z790-P boards.

Please note that in order for the Heads to work correctly with the MSI
motherboard, two additional components are required:

1. TPM 2.0 MSI MS-4462, available at our [store](https://shop.3mdeb.com/shop/modules/tpm-2-0-msi-ms-4462/).
1. Nitrokey 3A Mini, also available for purchase at our [store](https://shop.3mdeb.com/shop/adapters/nitrokey-3a-mini/).

The Heads currently supports only integrated graphics (a non-F CPU). Discrete
graphics is NOT supported by the standard build.

## v0.9.0 - 2024-03-21

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1yWZ--zFPIsQhXZByf7nJIrasQYuRSf1yCi60lY_RGsQ/edit#gid=5649308).

### Added

- [Dual TPM feature in coreboot. When ME is disabled, fTPM becomes inactive as well and chipset will route the TPM traffic to SPI bus. coreboot will now probe for all possible TPMs and initialize the one that is currently active.](https://github.com/Dasharo/dasharo-issues/issues/113)

### Changed

- [This is a Dasharo Pro Package release](https://docs.dasharo.com/dev-proc/versioning/#dasharo-entry-subscription-releases)
- Heads Linux is used as a payload
- [Updated Flash Descriptor to enlarge BIOS region; refer to SBOM section below](https://github.com/Dasharo/dasharo-blobs/tree/main/msi/ms7e06)
- ME hardcoded to be HAP disabled for heads builds. Discrete SPI TPM in JTPM1
  header is required to provide TPM functionality.

### Known issues

- [Cannot wake from suspend via RTC on QubesOS](https://github.com/Dasharo/dasharo-issues/issues/484)
- [Builds are not fully reproducible](https://github.com/linuxboot/heads/issues/1616)

### Binaries

[sha256][msi_ms7e06_v0.9.0_ddr4_heads.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.0_ddr4_heads.rom_sig]{.md-button}

[sha256][msi_ms7e06_v0.9.0_ddr5_heads.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.0_ddr5_heads.rom_sig]{.md-button}

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-entry-subscription-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Pro Package newsletter.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7e06/dasharo-release-0.x-compatible-with-msi-ms-7e06-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo heads fork based on v0.2.0 revision 13aa08ce](https://github.com/Dasharo/heads/tree/13aa08ce)
- [Dasharo coreboot fork based on 4.21 revision 38215f5a](https://github.com/Dasharo/coreboot/tree/38215f5a)
- [Intel Management Engine based on v16.1.30.2307 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/msi/ms7e06/me.bin)
- [Intel Flash Descriptor based on v1.2 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/msi/ms7e06/descriptor.bin)
- [Intel Firmware Support Package based on RPL-S C.0.BD.40 revision 481ea7cf](https://github.com/intel/FSP/tree/481ea7cf/RaptorLakeFspBinPkg/Client/RaptorLakeS)
- [Intel microcode based on ADL/RPL C0/H0 0x0000002e revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-97-05)
- [Intel microcode based on RPL B0 0x00000119 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-b7-01)

[newsletter]: https://newsletter.3mdeb.com/subscription/D7dQvGx6k
[msi_ms7e06_v0.9.0_ddr4_heads.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/heads/v0.9.0/msi_ms7e06_v0.9.0_ddr4_heads.rom.sha256
[msi_ms7e06_v0.9.0_ddr4_heads.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/heads/v0.9.0/msi_ms7e06_v0.9.0_ddr4_heads.rom.sha256.sig
[msi_ms7e06_v0.9.0_ddr5_heads.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/heads/v0.9.0/msi_ms7e06_v0.9.0_ddr5_heads.rom.sha256
[msi_ms7e06_v0.9.0_ddr5_heads.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/heads/v0.9.0/msi_ms7e06_v0.9.0_ddr5_heads.rom.sha256.sig
