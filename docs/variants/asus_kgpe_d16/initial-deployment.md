# Initial deployment

Initial deployment of Dasharo firmware on ASUS KGPE-D16 can be done:

* using DTS v1.1.0,
* manually.

## Initial deployment using DTS

Initial deployment for Dell OptiPlex 7010/9010 in supported in DTS since version
v1.1.0. Please check [Dasharo zero-touch initial deployment
section](../../dasharo-tools-suite/documentation.md#dasharo-zero-touch-initial-deployment).

## Initial deployment manually

Initial flashing of Dasharo firmware can be done from Linux using flashrom with
the internal programmer. This document describes the process of building,
installing and running flashrom on Ubuntu 20.04.

### Build flashrom

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
