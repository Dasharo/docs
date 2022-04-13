# Dasharo compatible with MSI PRO Z690-A WIFI DDR4 - installation manual

Flashing coreboot can be done from Linux using flashrom with the internal
programmer. This document describes the process of building, installing and
running flashrom on Ubuntu 21.04.

## Build flashrom

Currently, the latest flashrom release lacks support for Alder Lake S internal
flashing. Because of this, we need to build flashrom from
[3mdeb fork](https://github.com/3mdeb/flashrom/tree/alder_lake_s).
The procedure is based on
[Ubuntu 21.04 desktop amd64 ISO](http://www.releases.ubuntu.com/21.04/ubuntu-21.04-desktop-amd64.iso)
burned on the USB stick.

Boot the Ubuntu live image and select `Try ubuntu` option. Open a terminal and
proceed with commands below.

Install build dependencies:

```bash
$ sudo apt-get install git build-essential pkg-config libpci-dev udev
```

Obtain source code:

```bash
$ git clone https://github.com/3mdeb/flashrom.git -b alder_lake_s
$ cd flashrom
```

Build and install flashrom:

```bash
$ sudo make install
```

## Flashing

All flash operations require UEFI Secure Boot to be disabled. You may download
the binary using `scp` (need to install openssh-server package) or `wget`
command. The binaries can be found on the [release page](releases.md).

### Reading flash contents

Always prepare a backup of the current firmware image. To read the original
firmware from the flash and save it to a file (`dump.rom`), execute the
following command:

```bash
$ sudo flashrom -p internal -r dump.rom
```

### Flashing Dasharo

To flash Dasharo on the platform, execute the following command:

```bash
$ sudo flashrom -p internal -w msi_ms7d25_v0.1.0.rom --ifd -i bios
```

After the command succeeds, invoke `poweroff` or click the power off in the GUI
to shutdown the board. Press `ENTER` when prompted on the screen. Power on the
board back. Reboot will not work as some memory settings are preserved after
reboot and FSP fails to train the memory. Poweroff is required.

### Flashing back vendor firmware

```bash
$ sudo flashrom -p internal -w dump.rom --ifd -i bios
```

NOTE: Dasharo version v0.1.0 will not have network connection. Use a different
USB storage or an USB to Ethernet/USB WiFi adapter to move the binary to the
live system.
