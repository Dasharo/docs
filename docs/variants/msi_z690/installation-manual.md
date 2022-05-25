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
$ git clone https://github.com/Dasharo/flashrom.git -b dasharo-release
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

**IMPORTANT!** You will need a second USB storage to keep the dumped firmware
backup or alternatively upload it to some cloud or network drive (Ubuntu live
has a Firefox browser installed). Ubuntu live image is volatile and has no
persistent storage. All changes made in live image will be lost after reboot.

### Migrating SMBIOS unique data

To migrate the SMBIOS system UUID and board serial number follow the Linux
instructions below before attempting to flash the binary. The procedure is
supported on Dasharo version v1.0.0 and later and requires cbfstool built from
coreboot tree.

```bash
echo -n `sudo dmidecode -s system-uuid` > system_uuid.txt
echo -n `sudo dmidecode -s baseboard-serial-number` > serial_number.txt
# assuming in coreboot root directory
./build/cbfstool build/coreboot.rom add -f serial_number.txt -n serial_number -t raw -r FW_MAIN_A
./build/cbfstool build/coreboot.rom add -f serial_number.txt -n serial_number -t raw -r FW_MAIN_B
./build/cbfstool build/coreboot.rom add -f serial_number.txt -n serial_number -t raw -r COREBOOT
./build/cbfstool build/coreboot.rom add -f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_A
./build/cbfstool build/coreboot.rom add -f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_B
./build/cbfstool build/coreboot.rom add -f system_uuid.txt -n system_uuid -t raw -r COREBOOT
```

One may use `msi_ms7d25_v1.0.0.rom` binary directly and simply build the
cbfstool only from coreboot repository:

```bash
cd coreboot
make -C util/cbfstool
```

Then instead of `./build/cbfstool build/coreboot.rom add ...` type
`util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.0.0.rom add ...`.

Not you will need to resign the binary after adding the SMBIOS data. Please
check [Vboot documentation](../../common-coreboot-docs/vboot_signing.md) how to
resign the data. Dasharo uses the default vboot keys, available in
`coreboot/3rdparty/vboot/tests/devkeys`. It is user responsibility to generate
and use own keys during updates.

### Flashing Dasharo

To flash Dasharo on the platform, execute the following command:

> Replace the `VERSION` in firmware file name with the version you want to
> flash. For example: `msi_ms7d25_v0.1.0.rom`.

```bash
$ sudo flashrom -p internal -w msi_ms7d25_vVERSION.rom --ifd -i bios
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
