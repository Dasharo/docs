# NovaCustom V560TU 14th Gen Dasharo (coreboot + heads) Release Notes

This document contains the release notes for Heads firmware for NovaCustom
V560TU series of laptops.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

[Subscribe to NovaCustom V54x 14th Gen Dasharo Release Newsletter]
[newsletter]{ .md-button .md-button--primary .center }

</center>

## v0.9.0 - 2025-01-30

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/tree/main/boards/NovaCustom/MTL_14th_Gen/V560TU/Heads/v0.9.0-results.csv).

### Added

- [This is a Dasharo Pro Package Release](https://docs.dasharo.com/dev-proc/versioning/#dasharo-entry-subscription-releases)
- Heads Linux is used as a payload

### Known issues

- [Some unexpected errors in dmesg](https://github.com/Dasharo/dasharo-issues/issues/1201)
- [Performance increase for -TU Series (comparison with NVIDIA variants) - coreboot issue](https://github.com/Dasharo/dasharo-issues/issues/1216)

### Binaries

[sha256][novacustom_v56x_mtl_ec_v0.9.0.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_ec_v0.9.0.rom_sig]{.md-button}

[sha256][novacustom_v56x_mtl_v0.9.0_heads.rom_hash]{.md-button}
[sha256.sig][novacustom_v56x_mtl_v0.9.0_heads.rom_sig]{.md-button}

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Entry Subscription subscriber](../../ways-you-can-help-us.md#become-a-dasharo-entry-subscription-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Entry Subscription newsletter.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://github.com/3mdeb/3mdeb-secpack/blob/master/customer-keys/novacustom/dasharo-release-0.9.x-for-novacustom-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo heads fork based on v0.2.1 revision bbbca5d4](https://github.com/Dasharo/heads/tree/bbbca5d4)
    + [License](https://github.com/Dasharo/heads/blob/bbbca5d4/COPYING)
- [Dasharo fork of System76 EC based on 485f3900 revision 368e08e0](https://github.com/Dasharo/ec/tree/368e08e0/)
    + [License](https://github.com/Dasharo/ec/blob/368e08e0/LICENSE)
- [vboot based on 3d37d2aa revision 3d37d2aa](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/LICENSE)
- [Intel Management Engine version v18.0.5.2040](https://github.com/Dasharo/dasharo-blobs/blob/32cffee4/novacustom/v5x0tu/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/32cffee4/novacustom/v5x0tu/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel microcode version MTL C0 0x1c 03/01/2024](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240531/intel-ucode/06-aa-04)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240531/license)
- [Intel Firmware Support Package for Meteor Lake-H version 2024/04/30 v4122_12](https://github.com/Dasharo/dasharo-blobs/tree/32cffee4/novacustom/v5x0tu/MeteorLakeFspBinPkg)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)

[newsletter]: https://newsletter.3mdeb.com/subscription/sB4G9eq9h
[novacustom_v56x_mtl_ec_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/heads/v0.9.0/novacustom_v56x_mtl_ec_v0.9.0.rom.sha256
[novacustom_v56x_mtl_ec_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/heads/v0.9.0/novacustom_v56x_mtl_ec_v0.9.0.rom.sha256.sig
[novacustom_v56x_mtl_v0.9.0_heads.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/heads/v0.9.0/novacustom_v56x_mtl_v0.9.0_heads.rom.sha256
[novacustom_v56x_mtl_v0.9.0_heads.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v56x_mtl/heads/v0.9.0/novacustom_v56x_mtl_v0.9.0_heads.rom.sha256.sig
