# Initial deployment

Initial flashing of Dasharo firmware can be done from Linux using flashrom with
the internal programmer or using the Dasharo Tools Suite included in the Dasharo
Pro Package subscription (formerly Dasharo Entry Subscription). An instruction
on how to use the DTS can be found in the [DTS documentation](../../dasharo-tools-suite/documentation/features.md#dasharo-zero-touch-initial-deployment)

This document describes the process of building, installing and running
flashrom on Ubuntu 24.04.

## Build flashrom

Please follow generic guide for [Dasharo flashrom fork](../../osf-trivia-list/deployment.md#how-to-install-dasharo-flashrom-fork).

## Reading flash contents

Always prepare a backup of the current firmware image. To read from the flash
and save it to a file (`dump.rom`), execute the following command:

```bash
flashrom -p internal -r dump.rom
```

If you forgot to do this, you can get the original, proprietary
firmware from the [ODROID wiki website](https://wiki.odroid.com/odroid-h4/hardware/h4_bios_update#bios_release)
 to restore it in case it is bricked. Using the firmware other than
your own backup should be the last resort.

## Flashing Dasharo

To flash Dasharo on the platform, execute the following command - replace
`[path]` with the path to the Dasharo image you want to flash, e.g.
`hardkernel_odroid_h4_v0.9.0.rom`.

```bash
sudo flashrom -p internal -w [path] --ifd -i bios
```

For Slim Bootloader flavor the flash descriptor has to be updated as well to
match Slim Bootloader requirements for Top Swap size:

```bash
sudo flashrom -p internal --ifd -i bios -i fd \
    -w hardkernel_odroid_h4_v0.9.0_slim_bootloader_uefi.rom
```

After successful operation reboot the platform.

If the platforms fails to boot, try performing a CMOS reset:

1. Disconnect the power supply and the CMOS battery.
1. Wait for 10 seconds
1. Reconnect the power supply and the CMOS battery
1. Press the power button
