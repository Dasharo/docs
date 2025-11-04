# Initial Deployment

## Initial deployment manually

Initial flashing of Dasharo firmware can be done from Linux using flashrom with
the internal programmer. This document describes the process of building,
installing and running flashrom on Ubuntu 20.04.

### Build flashrom

Currently, the latest flashrom release lacks support for Ryzen internal flashing.
Because of this, we need to build flashrom from source.

Install build dependencies:

```bash
apt install git build-essential debhelper pkg-config libpci-dev \
	libusb-1.0.0-dev libftdi1-dev meson
```

Obtain source code:

[TODO]: # (currently segfaults in operation on the Asus Pro-WS x570-ACE)

```bash
git clone https://review.coreboot.org/flashrom-stable
cd flashrom-stable
git fetch https://review.coreboot.org/flashrom-stable refs/changes/84/72584/4
git checkout -b change-72584 FETCH_HEAD
```

Build flashrom:

```bash
make
sudo make install
```

### Reading flash contents

Always prepare a backup of the current firmware image. To read the flash
and save it to a file (`backup.rom`), execute the following command:

```bash
flashrom -p internal -r backup.rom
```

### Flashing Dasharo

To flash Dasharo on the platform, execute the following command - replace
`[path]` with the path to the Dasharo image you want to flash, e.g.
`TODO_placeholder_flash_name.rom`.

[TODO]: # (determine actual flash image name)

```bash
flashrom -p internal -w [path]
```
