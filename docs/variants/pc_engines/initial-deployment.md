# Initial deployment

This document describes the process of updating [PC Engines coreboot
firmware](https://pcengines.github.io/) to Dasharo firmware based on EDK II
(aka Dasharo (coreboot+UEFI)) or Dasharo (coreboot+SeaBIOS).

## OS compatibility for Dasharo (coreboot+UEFI)

Switching from BIOS to UEFI-based firmware might cause compatibility issues if
you already had an operating system installed on your platform. Some OSs can
handle the switch without any issues, while others may need to be reinstalled.
We have tested the update on several operating systems. The results are
available in the [test results
spreadsheet](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit#gid=1670191276)
and in the table below:

| OS | Can be booted from UEFI  |
|----|------------------------- |
| Ubuntu | :x:   |
| OPNSense | :heavy_check_mark: |
| pfSense | :x:                 |
| OpenWrt | Depends[^1]         |

Initial flashing of Dasharo firmware can be done from Linux using flashrom
with the internal programmer.

## Deploy using Dasharo Tools Suite

For simplicity we recommend using [Dasharo Tools
Suite](../../dasharo-tools-suite/documentation/features.md#dasharo-zero-touch-initial-deployment)
to omit all manual compilation and flashing steps, and deploy Dasharo
seamlessly.

- Ensure [Firmware Write Protection](https://github.com/pcengines/sortbootorder?tab=readme-ov-file#bios-wp-option)
  is disabled in sortbootorder
- [Boot into Dasharo Tools
  Suite](https://docs.dasharo.com/dasharo-tools-suite/documentation/running/)
- Enter your DPP subscription credentials
- Follow the instructions from [Dasharo Transition documentation](../../dasharo-tools-suite/documentation/dasharo-transition.md)

## Manual installation

The steps below describe the process of manual installation of Dasharo on your
apu.

### Build flashrom

Please follow generic guide for [flashrom
building](https://www.flashrom.org/dev_guide/building_from_source.html), or
install it from the OS' package manager (minimum supported version is v1.0).

### Reading flash contents

Always prepare a backup of the current firmware image. If you are using DTS,
the backup will be made automatically with [HCL
report](../../dasharo-tools-suite/documentation/features.md#hcl-report). When deploying
manually, to read from the flash and save it to a file (`dump.rom`), execute
the following command:

```bash
flashrom -p internal -r dump.rom
```

### Flashing Dasharo

To flash Dasharo on the platform, execute the following command - replace
`<variant>` with the APU variant (2, 3, 4 or 6) and `<version>` with the
Dasharo image version, e.g. `v0.9.0` or `v24.02.01.01` or `v4.0.34`.

```bash
flashrom -p internal -w pcengines_apu<variant>_<version>.rom
```

After the operation is successful, reboot the platform.

[^1]:
    Depending on installed image, can be booted from UEFI or has to be reinstalled.
    The image types are listed in the
    [OpenWrt documentation](https://openwrt.org/docs/guide-user/installation/openwrt_x86#download_disk_images).
    If you used a `*-combined-efi` image, then you can boot it from UEFI. Otherwise,
    you need to reinstall OpenWrt using such image. If you do not remember which
    image you used or if you got it from another source, you should check whether
    your disk has an EFI system partition (ESP). You can check it by executing the
    `lsblk` command:

    ```bash
    lsblk -f
    ```

    If your disk has a small FAT16 or FAT32 partition at the beginning, then it's
    likely the ESP:

    ```bash
    vda1
       vfat   FAT16 kernel       1234-ABCD
    ```

    If there are no FAT partitions, then you need to reinstall
    OpenWrt.
