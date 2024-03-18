# Flashing custom firmware

This document describes the steps for installing, reinstalling or downgrading
Dasharo firmware.

!!! warning

    This guide is for advanced users and firmware developers looking to install
    custom, older or development versions of firmware. If you're not sure if
    this applies to you, you probably don't need to follow this guide.

## Prerequisites

If you're flashing firmware that is not signed with Dasharo vboot keys, you will
need to disable some security measures first. Enter the UEFI setup menu and
disable (if present):

- SMM BIOS Write Protection
- BIOS Boot Medium Lock
- UEFI Secure Boot

If you plan on reflashing Intel ME firmware, you should also disable it using
any of the available methods first.

## Flashing

To install vendor firmware:

```bash
flashrom -p internal -w [firmware.bin]
```

To install a previous or custom version of Dasharo:

!!! warning

    In general flashing only the BIOS region is needed when flashing older or
    custom versions of Dasharo. However, sometimes, an update of other regions
    is also necessary. If unsure, consult the release notes for your mainboard.

```bash
flashrom -p internal --ifd -i bios -w [firmware.bin]
```
