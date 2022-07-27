# Firmware update

Following documentation describes the  process of Dasharo open-source firmware
update.

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

## Updating Dasharo

The whole `bios` region must be updated.

```bash
flashrom -p internal -w [path] --ifd -i bios
```
