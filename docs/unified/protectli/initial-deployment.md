# Initial deployment

Initial flashing of Dasharo firmware can be done from Linux using flashrom with
the internal programmer. This document describes the process of building,
installing and running flashrom on Ubuntu 22.04.

## Build flashrom

Please follow generic guide for [Dasharo flashrom fork](../../osf-trivia-list/deployment.md#how-to-install-dasharo-flashrom-fork).

## Reading flash contents

Always prepare a backup of the current firmware image. To read from the flash
and save it to a file (`dump.rom`), execute the following command:

```bash
flashrom -p internal -r dump.rom
```

## Flashing Dasharo

To flash Dasharo on the platform, execute the following command - replace `[path]`
with the path to the Dasharo image you want to flash:

```bash
sudo flashrom -p internal -w [path]
```

This will flash the full image, including the Intel ME. The operation
requires a hard reset of the platform. To perform a hard reset:

    1. Power off the platform. Note, it may not power off completely due to
        flashed ME.
    2. Disconnect power supply from the board when OS finishes all tasks after
        power off (the screen goes dark or black).
    3. Disconnect the RTC/CMOS battery, connect it back after a couple seconds.
    4. Connect the power supply back.
    5. The platform should power on normally now.
