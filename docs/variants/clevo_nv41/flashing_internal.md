# coreboot internal flashing (Ubuntu 20.04)

## Intro

Flashing coreboot can be done from Linux using flashrom with the internal
programmer. This document describes the process of building, installing and
running flashrom on Ubuntu 20.04.

## Pre-setup

Ensure that the EC is running firmware 1.07.05. Follow the steps outlined in
[EC firmware update](../ec_update)

## Build flashrom

Currently, the latest flashrom release lacks support for Tiger Lake-U internal
flashing. Because of this, we need to build flashrom from source.

Install build dependencies:

```bash
sudo apt install git build-essential debhelper pkg-config libpci-dev libusb-1.0-0-dev libftdi1-dev meson
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

To read from the flash and save them to a file (`dump.rom`), execute the
following command:

```bash
sudo flashrom -p internal -r dump.rom
```

## Flashing coreboot

To flash coreboot to the laptop, execute the following command - replace [path]
with the path to the coreboot image you want to flash, e.g. `build/coreboot.rom`.

If stock firmware or coreboot version below v0.5.0 is currently installed:

```bash
sudo flashrom -p internal -w [path] --ifd -i bios
```

If version v0.5.0 or higher is currently installed, only the RW_SECTION_A
partition of the flash can be flashed from the operating system. Flash it using
the following command:

```bash
sudo flashrom -p internal -w [path] --fmap -i RW_SECTION_A
```

This command also preserves UEFI settings and the boot order.
