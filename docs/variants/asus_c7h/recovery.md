# Recovery

## Prerequisites

To proceed with the firmware recovery procedure you need, depending on your method,
either the UEFI cap file distributed by Asus, a manual backup of the bios, or the
UEFI cap file stripped of its header.

The backup file should be generated before making any changes in the device flash
chip according to documentation.

## USB BIOS FlashBack

This procedure only functions when using the vendor's UEFI cap file.
A video demonstration is available here ![type:video](https://www.youtube.com/embed/FPyElZcsW6o)

1. Obtain a copy of the vendor firmware.
2. Extract the zipfile and rename `ROG-CROSSHAIR-VII-HERO-WIFI-ASUS-<version>.CAP`
to `C7HWIFI.CAP`
3. Create an MBR partitioned USB 2.0 flash drive with a single partition formatted
to FAT32.
4. Place `C7HWIFI.CAP` in the root of this flash drive.
5. Power down the computer if not already offline.
6. Insert the prepared USB flashdrive into the USB BIOS flashback port; this is
the bottommost USB port under the PS/2 keyboard/mouse port
7. Press and hold the BIOS flashback button for around 3-5 seconds until its LED
flashes three times.
8. Wait until this LED ceases flashing, indicating that the flashback process is
complete.

## External flashing

The motherboard has a +1v8 wson8 spi flash chip so you must use an appropriate programmer
or an adapter to step down the voltages. As its a wson8 you cannot easily clip to it
with a pomona or similar, so you have two options, a wson8 probe, or using the on-board flash header.

### On-Board Header
The onboard header is 2.0mm pitch, with the following pinout:

|Signal|Pin|Pin|Signal|
|------|---|---|------|
|NC    | 1 | 2 |WP#   |
|VCC   | 3 | 4 |GND   |
|CS#   | 5 | 6 |CLK   |
|MISO  | 7 | 8 |MOSI  |
|HOLD# | 9 | x |Key   |

### BIOS recovery
