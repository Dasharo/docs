# Installation manual

Flashing coreboot can be done from Linux using flashrom with the internal
programmer. This document describes the process of building, installing and
running flashrom on Ubuntu 22.04.

## Build flashrom

Currently, the latest flashrom release lacks support for Alder Lake S internal
flashing. Because of this, we need to build flashrom from
[3mdeb fork](https://github.com/Dasharo/flashrom/tree/dasharo-release).
The procedure is based on
[Ubuntu 22.04 desktop amd64 ISO](https://releases.ubuntu.com/22.04/ubuntu-22.04.1-desktop-amd64.iso)
burned on the USB stick. Ubuntu 22.04 or newer if preferred, as it contains the
network drivers for Ethernet and WiFi. Older versions of Ubuntu would require
a USB to Ethernet adapter or equivalent to get network connection and install
required software packages.

Boot the Ubuntu live image and select `Try ubuntu` option. Open a terminal and
proceed with commands below.

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

## Flashing

All flash operations require UEFI Secure Boot to be disabled. You may download
the binary using `scp` (need to install openssh-server package) or `wget`
command. The binaries can be found on the [release page](releases.md).

### Reading flash contents

Always prepare a backup of the current firmware image. To read the original
firmware from the flash and save it to a file (`dump.rom`), execute the
following command:

```bash
sudo flashrom -p internal -r dump.rom
```

**IMPORTANT!** You will need a second USB storage to keep the dumped firmware
backup or alternatively upload it to some cloud or network drive (Ubuntu live
has a Firefox browser installed). Ubuntu live image is volatile and has no
persistent storage. All changes made in live image will be lost after reboot.

### Migrating SMBIOS unique data

To migrate the SMBIOS system UUID and board serial number follow the Linux
instructions below before attempting to flash the binary. The procedure is
supported on Dasharo version v1.0.0 and later and requires cbfstool built from
coreboot tree. Follow the [Building Manual](building-manual.md) using v1.0.0
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
check [Vboot documentation](../../common-coreboot-docs/vboot_signing.md) how to
resign the data. It is machine owner's responsibility to generate and use own
keys during updates.

### Flashing Dasharo

**WARNING**: If you use and external/discrete GPU and migrate to Dasharo, be
sure to unplug the dGPU first (when machine is powered off before proceeding
with flashing), as Dasharo firmware does not support all GPU cards properly yet
(as of version v1.0.0). There is high risk for the graphical output to break in
the firmware when dGPU is connected. Effectively it leaves the only option to
boot in blind into previously installed OS (if the platform does not brick and
if an OS is present on a disk). The first boot may take up to 2 minutes to
fully train the memory, so be patient and wait for the Dasharo logo to appear,
subsequent boots will take only seconds. MSI EZ debug leds are not supported by
Dasharo and you may notice red led to be lit. If the platform boots with
integrated GPU, you may try to plug the external GPU back and boot again.

To flash Dasharo on the platform, execute the following command:

> Replace the `VERSION` in firmware file name with the version you want to
> flash. For example: `msi_ms7d25_v0.1.0.rom`.

```bash
sudo flashrom -p internal -w msi_ms7d25_vVERSION.rom --ifd -i bios
```

After the command succeeds, invoke `sudo poweroff` or click the power off in
the GUI to shutdown the board. Press `ENTER` when prompted on the screen. Power
on the board back. Reboot will not work as some memory settings are preserved
after reboot and FSP fails to train the memory. Poweroff is required.

### Flashing back vendor firmware

```bash
sudo flashrom -p internal -w dump.rom --ifd -i bios
```

NOTE: Dasharo version v0.1.0 will not have network connection. Use a different
USB storage or an USB to Ethernet/USB WiFi adapter to move the binary to the
live system.
