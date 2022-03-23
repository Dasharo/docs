# Dasharo for NovaCustom NS5X - Installation manual

## Intro

Flashing coreboot can be done from Linux using flashrom with the internal
programmer. This document describes the process of building, installing and
running flashrom on Ubuntu 20.04.

## Build flashrom

Currently, the latest flashrom release lacks support for Tiger Lake-U internal
flashing. Because of this, we need to build flashrom from source.

Install build dependencies:

```bash
# apt install git build-essential debhelper pkg-config libpci-dev libusb-1.0-0-dev libftdi1-dev meson
```

Obtain source code:

```bash
$ git clone https://review.coreboot.org/flashrom.git
$ cd flashrom
```

Build flashrom:

```bash
$ make
$ sudo make install
```

## Reading flash contents

To read from the flash and save them to a file (`dump.rom`), execute the
following command:

```bash
# flashrom -p internal -r dump.rom
```

## Installing Dasharo

### Initial Installation

During initial installation of Dasharo, you should deploy supported Intel ME
version (and configuration) on the device.

> Publicly released binaries do not contain ME binary. If you need an Intel ME
> update for your device, contact us via already established commercial support
> channel.

When flashing binaries with ME binary included, flashing of the whole chip is
recommended. To flash firmware to the laptop, execute the following command -
replace [path] with the path to the firmware image you want to flash, e.g.
`novacustom_ns5x_full_v1.0.0.rom`

```bash
# flashrom -p internal -w [path]
```

### Updating Dasharo

If Dasharo is currently installed, only the RW_SECTION_A partition of the flash
needs to be updated. Flash it using the following command:

```bash
# flashrom -p internal -w [path] --fmap -i RW_SECTION_A
```

This command also preserves UEFI settings and the boot order.
