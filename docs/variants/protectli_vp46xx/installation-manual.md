# Protectli Dasharo on VP46xx - installation manual

Flashing coreboot can be done from Linux using flashrom with the internal
programmer. This document describes the process of building, installing and
running flashrom on Ubuntu 20.04.

## Build flashrom

Currently, the latest flashrom release lacks support for Comet Lake U internal
flashing. Because of this, we need to build flashrom from source.

Install build dependencies:

```bash
apt install git build-essential debhelper pkg-config libpci-dev libusb-1.0-0-dev libftdi1-dev meson
```

Obtain source code:

```bash
git clone https://review.coreboot.org/flashrom.git
cd flashrom
```

Build flashrom:

```bash
make
sudo make install
```

## Reading flash contents

Always prepare a backup of the current firmware image. To read from the flash
and save them to a file (`dump.rom`), execute the following command:

```bash
flashrom -p internal -r dump.rom
```

## Flashing Dasharo

To flash Dasharo on the platform, execute the following command - replace `[path]`
with the path to the Dasharo image you want to flash, e.g. `protectli_vault_cml_v1.0.13.rom`.

If stock firmware is currently installed:

```bash
flashrom -p internal -w protectli_vault_cml_v1.0.13.rom
```

This will flash the full image including Intel ME. The operation requires a
hard reset of the platform. To perform a hard reset:

1. Power off the platform. Note, it may not power off completely due to flashed
   ME.
2. Disconnect power supply from the board when OS finishes all tasks before
   power off (the screen goes dark or black).
3. Disconnect the RTC/CMOS battery OR clear the CMOS using the pin header
   located near memory slots. Wait about half a minute (unshort the pins).
4. Connect the power supply back.
5. The platform should power on normally now. You can connect the battery back
   if it was disconnected.

If Dasharo v1.0.16 is currently installed, only the RW_SECTION_A partition of
the flash needs to be updated. Flash it using the following command:

```bash
flashrom -p internal -w protectli_vault_cml_v1.0.13.rom --fmap -i RW_SECTION_A
```

This command also preserves Dasharo UEFI settings and the boot order.

If you have Dasharo older than v1.0.16, use the following command upgrade
instead:

```bash
flashrom -p internal -w protectli_vault_cml_v1.0.13.rom --ifd -i bios
```
