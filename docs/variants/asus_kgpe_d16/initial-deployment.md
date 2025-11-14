# Initial deployment

Initial deployment of Dasharo firmware on ASUS KGPE-D16 can only be done
manually. Support for DTS deployment has been dropped in versions `> 2.7.1`.

## Initial deployment manually

Initial flashing of Dasharo firmware can be done from Linux using flashrom with
the internal programmer. This document describes the process of building,
installing and running flashrom on Ubuntu 20.04.

### Build flashrom

Please follow generic guide for [Dasharo flashrom fork](../../osf-trivia-list/deployment.md#how-to-install-dasharo-flashrom-fork).

### Reading flash contents

Always prepare a backup of the current firmware image. To read from the flash
and save it to a file (`backup.rom`), execute the following command:

```bash
flashrom -p internal -r backup.rom
```

### Flashing Dasharo

To flash Dasharo on the platform, execute the following command - replace
`[path]` with the path to the Dasharo image you want to flash, e.g.
`asus_kgpe-d16_v0.3.0_2M_vboot_TPM1.2.rom`.

```bash
flashrom -p internal -w [path]
```

This will flash the full image, including the Intel ME. The operation requires
a hard reset of the platform. To perform a hard reset:

1. Power off the platform. Note, it may not power off completely due to flashed
   ME.
1. Disconnect power supply from the board when OS finishes all tasks after
   power off (the screen goes dark or black).
1. The platform should power on normally now. You can connect the battery back
   if it was disconnected.
