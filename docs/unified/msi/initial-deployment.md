# Initial Deployment

Initial deployment of Dasharo firmware on MSI PRO Z690-A and PRO Z790-P can be
done:

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

Please follow generic guide for [Dasharo flashrom fork](../../../osf-trivia-list/deployment/#how-to-install-dasharo-flashrom-fork).

### Flashing

All flash operations require UEFI Secure Boot to be disabled. You may download
the binary using `scp` (need to install openssh-server package) or `wget`
command. The binaries can be found on the

* [MSI PRO Z690-A release page](../../variants/msi_z690/releases.md)
* [MSI PRO Z790-P release page](../../variants/msi_z790/releases.md).

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
coreboot tree. Follow the [Building Manual](building-manual.md) using the
Z690-A v1.0.0/Z790-P v0.9.0 version or newer and then:

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

=== "PRO Z690-A (WIFI) DDR4"
    One may use `msi_ms7d25_v1.1.1_ddr4.rom` (or newer) binary directly and
    simply build the cbfstool only from coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot -b msi_ms7d25/release
    cd coreboot
    make -C util/cbfstool
    echo -n `sudo dmidecode -s system-uuid` > system_uuid.txt
    echo -n `sudo dmidecode -s baseboard-serial-number` > serial_number.txt
    # assuming in coreboot root directory
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr4.rom expand -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr4.rom expand -r FW_MAIN_B
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr4.rom add \
    	-f serial_number.txt -n serial_number -t raw -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr4.rom add \
    	-f serial_number.txt -n serial_number -t raw -r FW_MAIN_B
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr4.rom add \
    	-f serial_number.txt -n serial_number -t raw -r COREBOOT
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr4.rom add \
    	-f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr4.rom add \
    	-f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_B
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr4.rom add \
    	-f system_uuid.txt -n system_uuid -t raw -r COREBOOT
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr4.rom truncate -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr4.rom truncate -r FW_MAIN_B
    ```

=== "PRO Z690-A (WIFI)"
    One may use `msi_ms7d25_v1.1.1_ddr5.rom` (or newer) binary directly and
    simply build the cbfstool only from coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot -b msi_ms7d25/release
    cd coreboot
    make -C util/cbfstool
    echo -n `sudo dmidecode -s system-uuid` > system_uuid.txt
    echo -n `sudo dmidecode -s baseboard-serial-number` > serial_number.txt
    # assuming in coreboot root directory
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr5.rom expand -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr5.rom expand -r FW_MAIN_B
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr5.rom add \
    	-f serial_number.txt -n serial_number -t raw -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr5.rom add \
    	-f serial_number.txt -n serial_number -t raw -r FW_MAIN_B
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr5.rom add \
    	-f serial_number.txt -n serial_number -t raw -r COREBOOT
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr5.rom add \
    	-f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr5.rom add \
    	-f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_B
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr5.rom add \
    	-f system_uuid.txt -n system_uuid -t raw -r COREBOOT
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr5.rom truncate -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7d25_v1.1.1_ddr5.rom truncate -r FW_MAIN_B
    ```

=== "PRO Z790-P (WIFI) DDR4"
    One may use `msi_ms7e06_v0.9.0_ddr4.rom` (or newer) binary directly and
    simply build the cbfstool only from coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot -b msi_ms7d25/release
    cd coreboot
    make -C util/cbfstool
    echo -n `sudo dmidecode -s system-uuid` > system_uuid.txt
    echo -n `sudo dmidecode -s baseboard-serial-number` > serial_number.txt
    # assuming in coreboot root directory
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr4.rom expand -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr4.rom expand -r FW_MAIN_B
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr4.rom add \
    	-f serial_number.txt -n serial_number -t raw -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr4.rom add \
    	-f serial_number.txt -n serial_number -t raw -r FW_MAIN_B
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr4.rom add \
    	-f serial_number.txt -n serial_number -t raw -r COREBOOT
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr4.rom add \
    	-f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr4.rom add \
    	-f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_B
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr4.rom add \
    	-f system_uuid.txt -n system_uuid -t raw -r COREBOOT
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr4.rom truncate -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr4.rom truncate -r FW_MAIN_B
    ```

=== "PRO Z790-P (WIFI)"
    One may use `msi_ms7e06_v0.9.0_ddr5.rom` (or newer) binary directly and
    simply build the cbfstool only from coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot -b msi_ms7d25/release
    cd coreboot
    make -C util/cbfstool
    echo -n `sudo dmidecode -s system-uuid` > system_uuid.txt
    echo -n `sudo dmidecode -s baseboard-serial-number` > serial_number.txt
    # assuming in coreboot root directory
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr5.rom expand -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr5.rom expand -r FW_MAIN_B
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr5.rom add \
    	-f serial_number.txt -n serial_number -t raw -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr5.rom add \
    	-f serial_number.txt -n serial_number -t raw -r FW_MAIN_B
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr5.rom add \
    	-f serial_number.txt -n serial_number -t raw -r COREBOOT
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr5.rom add \
    	-f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr5.rom add \
    	-f system_uuid.txt -n system_uuid -t raw -r FW_MAIN_B
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr5.rom add \
    	-f system_uuid.txt -n system_uuid -t raw -r COREBOOT
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr5.rom truncate -r FW_MAIN_A
    ./util/cbfstool/cbfstool /path/to/msi_ms7e06_v0.9.0_ddr5.rom truncate -r FW_MAIN_B
    ```

Note you will need to resign the binary after adding the SMBIOS data. Please
check [Vboot documentation](../../../guides/vboot-signing) how to
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

=== "PRO Z690-A (WIFI) DDR4"
    > Replace the `VERSION` in firmware file name with the version you want to
    > flash. For example: `msi_ms7d25_v1.1.1_ddr4.rom`.

    ```bash
    sudo flashrom -p internal -w msi_ms7d25_vVERSION_ddr4.rom --ifd -i bios
    ```

=== "PRO Z690-A (WIFI)"
    > Replace the `VERSION` in firmware file name with the version you want to
    > flash. For example: `msi_ms7d25_v1.1.1_ddr5.rom`.

    ```bash
    sudo flashrom -p internal -w msi_ms7d25_vVERSION_ddr5.rom --ifd -i bios
    ```

=== "PRO Z790-P (WIFI) DDR4"
    > Replace the `VERSION` in firmware file name with the version you want to
    > flash. For example: `msi_ms7e06_v0.9.0_ddr4.rom`.

    ```bash
    sudo flashrom -p internal -w msi_ms7e06_vVERSION_ddr4.rom --ifd -i bios
    ```

=== "PRO Z790-P (WIFI)"
    > Replace the `VERSION` in firmware file name with the version you want to
    > flash. For example: `msi_ms7e06_v0.9.0_ddr5.rom`.

    ```bash
    sudo flashrom -p internal -w msi_ms7e06_vVERSION_ddr5.rom --ifd -i bios
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
