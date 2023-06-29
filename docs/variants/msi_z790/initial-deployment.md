# Initial Deployment

Initial deployment of Dasharo firmware on MSI PRO Z790-P can be done:

* using DTS,
* manually.

## Initial deployment using DTS

To ensure a smooth deployment process, it is recommended to use the latest
version of DTS available from the [releases
page](../../dasharo-tools-suite/releases.md). Once you have obtained it, you can
then proceed with following the [Dasharo zero-touch initial deployment
section](../../dasharo-tools-suite/documentation.md#dasharo-zero-touch-initial-deployment)
procedure. This will help you set up Dasharo effectively and without manual
intervention.

## Initial deployment manually

Flashing coreboot can be done from Linux using flashrom with the internal
programmer. This document describes the process of building, installing and
running flashrom on Ubuntu 22.04.

### Build flashrom

Currently, the latest flashrom release lacks support for Alder Lake S internal
flashing. Because of this, we need to build flashrom from
[3mdeb fork](https://github.com/Dasharo/flashrom/tree/dasharo-release).
The procedure is based on
[Ubuntu 22.04 desktop amd64 ISO](https://old-releases.ubuntu.com/releases/jammy/ubuntu-22.04.1-desktop-amd64.iso)
burned on the USB stick. Ubuntu 22.04 or newer if preferred, as it contains the
network drivers for Ethernet and WiFi. Older versions of Ubuntu would require
a USB to Ethernet adapter or equivalent to get a network connection and install
required software packages.

Boot the Ubuntu live image and select the `Try Ubuntu` option. Open a terminal
and proceed with the commands below.

Install build dependencies:

```bash
sudo apt-get update
sudo apt-get install git build-essential pkg-config libpci-dev udev
```

Obtain source code:

```bash
git clone https://github.com/Dasharo/flashrom.git -b dasharo-release
cd flashrom
```

Build and install flashrom:

```bash
sudo make install
```

### Flashing

All flash operations require UEFI Secure Boot to be disabled. You may download
the binary using `scp` (need to install openssh-server package) or `wget`
command. The binaries can be found on the [release page](releases.md).

#### Reading flash contents

Always prepare a backup of the current firmware image. To read the original
firmware from the flash and save it to a file (`dump.rom`), execute the
following command:

```bash
sudo flashrom -p internal -r dump.rom
```

**IMPORTANT!** You will need a second USB storage to keep the dumped firmware
backup or alternatively upload it to some cloud or network drive (Ubuntu live
has a Firefox browser installed). Ubuntu live image is volatile and has no
persistent storage. All changes made in the live image will be lost after
reboot.

#### Flashing Dasharo

**WARNING**: If you use an external/discrete GPU and migrate to Dasharo, be
sure to unplug the dGPU first (when the machine is powered off before proceeding
with flashing), as Dasharo firmware does not support all GPU cards properly yet
(as of version v1.0.0). There is a high risk for the graphical output to break
in the firmware when dGPU is connected. Effectively it leaves the only option to
boot in blind into a previously installed OS (if the platform does not brick and
if an OS is present on a disk). The first boot may take up to 2 minutes to
fully train the memory, so be patient and wait for the Dasharo logo to appear,
subsequent boots will take only seconds. MSI EZ debug leds are not supported by
Dasharo and you may notice a red led to be lit. If the platform boots with an
integrated GPU, you may try to plug the external GPU back and boot again.

To flash Dasharo on the platform, execute the following command:

> Replace the `VERSION` in firmware file name with the version you want to
> flash. For example: `msi_ms7e06_v0.9.0_ddr5.rom`.

```bash
sudo flashrom -p internal -w msi_ms7e06_vVERSION{_ddr4,_ddr5}.rom --ifd -i bios
```

**IMPORTANT!** After the command succeeds, invoke `sudo reboot` or click the
reboot/restart in the GUI to reboot the board. Press `ENTER` when prompted on
the screen to remove the installation media (if Ubuntu live is used). DO NOT
POWEROFF THE BOARD as SMI handlers of original MSI firmware may overwrite flash
contents and cause a brick.

After migration from MSI firmware to Dasharo and reboot, the firmware will
fail the memory training. After reboot wait approximately 30 seconds and then
power the board off by holding the power button pushed for 5 seconds. Dasharo
will signal the memory training failure with PC speaker beeps and blinking
SATA LED. When it happens use the power button to power the board off (no need
to wait 30 seconds in such case). Power on the board back. Now the memory
training should not fail and after approximately 1 minute (can be nearly 2
minutes or more for DDR5 memory), you should get a Dasharo splash screen on
the monitor. Subsequent boots will take only a few seconds.

#### Flashing back vendor firmware

```bash
sudo flashrom -p internal -w dump.rom --ifd -i bios
```
