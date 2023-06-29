# Initial deployment

Initial flashing of Dasharo firmware can be done from Linux using flashrom with
the internal programmer. This document describes the process of building,
installing and running flashrom on Ubuntu 22.04.

## Deploy using Dasharo Tools Suite

For simplicity we recommend using
[Dasharo Tools Suite](../../../dasharo-tools-suite/overview) to
omit all compilation steps and deploy the Dasharo firmware seamlessly.

1. Boot Dasharo Tools Suite.
2. Perform Dasharo installation.

This will flash the BIOS region only. After the successful operation, DTS will
reboot the platform.

This concludes Dasharo deployment process using DTS.

## Build flashrom

Currently, the latest flashrom release lacks support for Comet Lake U internal
flashing. Because of this, we need to build flashrom from source.

Install build dependencies:

```bash
apt install git build-essential debhelper pkg-config libpci-dev \
    libusb-1.0-0-dev libftdi1-dev meson
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
and save it to a file (`dump.rom`), execute the following command:

```bash
flashrom -p internal -r dump.rom
```

## Flashing Dasharo

To flash Dasharo on the platform, execute the following command - replace
`[path]` with the path to the Dasharo image you want to flash, e.g.
`protectli_vault_pt201_v0.9.0.rom`.

```bash
flashrom -p internal -w protectli_vault_pt201_v0.9.0.rom --ifd -i bios
```

This will flash the BIOS region only. After the operation is successful,
reboot the platform.

