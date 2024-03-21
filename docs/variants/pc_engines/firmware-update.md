# Legacy -> UEFI Update

This document describes the process of updating the platform's legacy SeaBIOS
to Dasharo firmware based on EDK II.

## OS compatibility

Switching from BIOS to UEFI-based firmware might cause compatibility issues if
you already had an operating system installed on your platform. Some OSs can
handle the switch without any issues, while others may need to be reinstalled.
We have tested the update on several operating systems. The results are
presented in the table below:

### Ubuntu

Can be booted from UEFI.

### OPNSense

Can be booted from UEFI.

### pfSense

Requires OS reinstall.

### OpenWrt

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
