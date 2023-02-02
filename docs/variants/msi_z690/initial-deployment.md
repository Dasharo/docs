# Initial Deployment

Initial deployment of Dasharo firmware on ASUS KGPE-D16 can be done:

* using DTS v1.1.0,
* manually.

## Initial deployment using DTS

Initial deployment for MSI PRO Z690-A (WIFI) (DDR4) is supported in DTS since
version v1.1.0. Please check [Dasharo zero-touch initial deployment
section](../../dasharo-tools-suite/documentation.md#dasharo-zero-touch-initial-deployment).

<span style="color:red">
Please do not use DTS to deploy Dasharo on MSI PRO Z690-A (WIFI) DDR5;
otherwise, you will brick your hardware. There are at least two bugs that have
to be fixed before it is possible:

- [Power off problem](https://github.com/Dasharo/dasharo-issues/issues/316)
- [Unsupported mainboard flashing problem](https://github.com/Dasharo/dasharo-issues/issues/317).</span>

## Initial deployment manually

Flashing coreboot can be done from Linux using flashrom with the internal
programmer. This document describes the process of building, installing and
running flashrom on Ubuntu 22.04.

### Build flashrom

Currently, the latest flashrom release lacks support for Alder Lake S internal
flashing. Because of this, we need to build flashrom from
[3mdeb fork](https://github.com/Dasharo/flashrom/tree/dasharo-release).
The procedure is based on
[Ubuntu 22.04 desktop amd64 ISO](https://releases.ubuntu.com/22.04/ubuntu-22.04.1-desktop-amd64.iso)
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

#### Migrating SMBIOS unique data

To migrate the SMBIOS system UUID and board serial number follow the Linux
instructions below before attempting to flash the binary. The procedure is
supported on Dasharo version v1.0.0 and later and requires cbfstool built from
coreboot tree. Follow the [Building Manual](building-manual.md) using the v1.0.0
version or newer and then:

```bash
echo -n `sudo dmidecode -s system-uuid` > system_uuid.txt
echo -n `sudo dmidecode -s baseboard-serial-number` > serial_number.txt
# assuming in coreboot root directory
./build/cbfstool build/coreboot.rom expand -r FW_MAIN_A
./build/cbfstool build/coreboot.rom expand -r FW_MAIN_B
./build/cbfstool build/coreboot.rom add \
	-f serial_number.txt -n serial_number -t raw -r FW_MAIN_A
./build/cbfstool build/coreboot.rom add \
	-f serial_number.txt -n serial_number -t raw -r FW_MAIN_B
./build/cbfstool build/coreboot.rom add \
	-f serial_number.txt -n serial_number -t raw -r COREBOOT
./build/cbfstool build/coreboot.rom add \
	-f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_A
./build/cbfstool build/coreboot.rom add \
	-f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_B
./build/cbfstool build/coreboot.rom add \
	-f system_uuid.txt -n system_uuid -t raw -r COREBOOT
./build/cbfstool build/coreboot.rom truncate -r FW_MAIN_A
./build/cbfstool build/coreboot.rom truncate -r FW_MAIN_B
```

One may use `msi_ms7d25_v1.0.0.rom` (or newer) binary directly and simply build
the cbfstool only from coreboot repository:

```bash
git clone https://github.com/Dasharo/coreboot -b msi_ms7d25/release
cd coreboot
make -C util/cbfstool
echo -n `sudo dmidecode -s system-uuid` > system_uuid.txt
echo -n `sudo dmidecode -s baseboard-serial-number` > serial_number.txt
# assuming in coreboot root directory
./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.0.0.rom expand -r FW_MAIN_A
./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.0.0.rom expand -r FW_MAIN_B
./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.0.0.rom add \
	-f serial_number.txt -n serial_number -t raw -r FW_MAIN_A
./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.0.0.rom add \
	-f serial_number.txt -n serial_number -t raw -r FW_MAIN_B
./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.0.0.rom add \
	-f serial_number.txt -n serial_number -t raw -r COREBOOT
./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.0.0.rom add \
	-f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_A
./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.0.0.rom add \
	-f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_B
./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.0.0.rom add \
	-f system_uuid.txt -n system_uuid -t raw -r COREBOOT
./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.0.0.rom truncate -r FW_MAIN_A
./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.0.0.rom truncate -r FW_MAIN_B
```

Note you will need to resign the binary after adding the SMBIOS data. Please
check [Vboot documentation](/guides/vboot-signing.md) how to
resign the data. It is the machine owner's responsibility to generate and use
own keys during updates.

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
> flash. For example: `msi_ms7d25_v1.1.0_ddr4.rom`.

```bash
sudo flashrom -p internal -w msi_ms7d25_vVERSION{_ddr4,_ddr5}.rom --ifd -i bios
```

**IMPORTANT!** After the command succeeds, invoke `sudo reboot` or click the
reboot/restart in the GUI to reboot the board. Press `ENTER` when prompted on
the screen to remove the installation media (if Ubuntu live is used). DO NOT
POWEROFF THE BOARD as SMI handlers of original MSI firmware may overwrite flash
contents and cause a brick.

After migration from MSI firmware to Dasharo and reboot, the firmware will fail
the memory training. After reboot wait approximately 30 seconds and then power
the board off by holding the power button pushed for 5 seconds. Dasharo v1.1.0
or newer will signal the memory training failure with PC speaker beeps and
blinking SATA LED. When it happens use the power button to power the board off
(no need to wait 30 seconds in such case). Power on the board back. Now the
memory training should not fail and after approximately 1 minute (can be nearly
2 minutes for DDR5 memory), you should get a Dasharo splash screen on the
monitor. Subsequent boots will take only a few seconds.

#### Flashing back vendor firmware

```bash
sudo flashrom -p internal -w dump.rom --ifd -i bios
```

NOTE: Dasharo version v0.1.0 will not have a network connection. Use a different
USB storage or a USB to Ethernet/USB WiFi adapter to move the binary to the live
system.
