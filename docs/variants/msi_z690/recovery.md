# Recovery

## Intro

This project is in early development phase. On certain
hardware configurations, the Dasharo firmware may not boot correctly (i.e.
we will have "bricked" the platform). In such a case, the recovery procedure can
reinstall the original firmware from the board manufacturer.

There are two documented recovery methods: using a [CH341A programming kit](https://3mdeb.com/shop/modules/ch341a-flash-bios-usb-programmer-kit-soic8-sop8/)
or an [RTE](https://3mdeb.com/shop/open-source-hardware/rte/).

### MSI Flash BIOS Button

The [MSI Flash BIOS Button](https://www.youtube.com/watch?v=iTkXunUAriE)
would give us easy-to-use recovery method. We have tried that one to switch
from Dasharo firmware to the original one, but it did not work, unfortunately.
The details of how this process exactly works are unknown due to the closed
nature of it's implementation. We can research this topic more in the future,
so maybe it can be utilized later for deployment and/or recovery of the
platform.

### External flashing with programmer

#### RTE

In this case, using external programmer is necessary. We are using
[RTE](https://3mdeb.com/open-source-hardware/#rte)
here.

* Connect programmer to the flash chip as shown in the
  [Hardware connection / SPI](../development/#hardware-connection) section of
  the `Development` documentation.

* Download official BIOS from vendor's website (this is the newest version, you
  may choose an older one too or in the best case use your firmware backup):

```bash
wget https://download.msi.com/bos_exe/mb/7D25v13.zip
unzip 7D25v13.zip
```

* Flash via external programmer:

> The command line will be different, depending on the programmer you use

```bash
flashrom -p linux_spi:dev=/dev/spidev1.0,spispeed=16000 -w 7D25v13/E7D25IMS.130
```

* First boot after the recovery process is significantly longer

### CH341A

#### Prerequisites

The full set is now available at our [online shop](https://3mdeb.com/shop/modules/ch341a-flash-bios-usb-programmer-kit-soic8-sop8/).

1. CH341A kit with 1.8V level-shifter. Can be bought on e.g. [Amazon](https://www.amazon.com/programmer-ch341a-Programmer-Adapter-Converter/dp/B07WP9FKZ2)

    ![](/images/ch341a_rec/ch341a_kit.jpg)

2. WSON8 probe. Can be bought from China on Aliexpress or eBay.

    ![](/images/ch341a_rec/wson8_probe.jpg)

3. USB2.0 Female-Male extension cord 0.5m or longer (optional)

    ![](/images/ch341a_rec/usb_ext.jpg)

4. Machine with Linux and flashrom.

#### Connection

First start with assembling the CH341A and the 1.8V adapter. Pay attention to
which holes you attach the adapter. You should use the holes marked as 25XX
(closer to the USB plug):

![](/images/ch341a_rec/ch341a.jpg)

Place the 1.8V adapter in the holes and lock it with the lever. Be sure that
the arrow on the adapter is facing the black lever (opposite side of USB plug):

![](/images/ch341a_rec/adapter_assemble.jpg)

Now take the breakout board with pin headers:

![](/images/ch341a_rec/pin_breakout.jpg)

and plug it into the other 1.8V adapter, be sure that numbers 1-4 on the breakout
match the numbers 1 and 4 on the adapter:

![](/images/ch341a_rec/adapter_shifter.jpg)

Numbers should be visible on the upper side after assembling:

![](/images/ch341a_rec/breakout_assemble.jpg)

Next, take the WSON8 probe and locate the white dot on the needles side (it
will indicate the first reference pin, although you may use any other corner pin):

![](/images/ch341a_rec/wson8_probe2.jpg)

Check which wire is connecting to this pin (the connection should be 1 to 1).
In my case it is white wire and it will be used as reference to connect the
wires to the breakout board:

![](/images/ch341a_rec/wire_attach2.jpg)

The wires should follow the same order of colors as on the probe (keep them
straight, and do not cross). Repeat with the other 4 wires on the other side of the
probe:

![](/images/ch341a_rec/wire_attach1.jpg)

Now the connection is ready. Time to locate the flash chip of the board.

#### Flashing

Connect the CH341A USB plug to the host machine which will be doing the
flashing process (optionally use the USB extension cord for convenience).
Locate the flash chip on the MSI PRO Z690-A DDR4 board:

![](/images/ch341a_rec/msi_z690a.jpg)

Locate the first pin on the flash chip (marked with a circle on the flash chip
package and indicated by number 1 printed on the board - red circle):

![](/images/ch341a_rec/msi_flash.jpg)

Attach the WSON8 probe matching the first pin of the probe (white wire) and
first pin of the flash chip:

![](/images/ch341a_rec/probe_attach.jpg)

Now on the Linux machine check if the flash is detected using a sample command

```bash
sudo flashrom -p ch341a_spi -r firmware.bin
```

You should see something like this:

```bash
flashrom v1.2-567-gf4eb405 on Linux 5.19.9-200.fc36.x86_64 (x86_64)
flashrom is free software, get the source code at https://flashrom.org

Using clock_gettime for delay loops (clk_id: 1, resolution: 1ns).
Found Winbond flash chip "W25Q256.W" (32768 kB, SPI) on ch341a_spi.
Reading flash... done.
```

You don't need to wait for the command completion and interrupt it with Ctrl+C
shortcut, it just serves as a confirmation of good connection. If you decide to
interrupt it, reset the CH341A programmer by unpluging and repluging it to USB
port. Now stabilize your hand holding the WSON8 probe on the flash chip and
invoke the real flashing command (e.g. if your original/working firmware backup
is saved as `firmware_backup.bin`):

```bash
sudo flashrom -p ch341a_spi -w firmware_backup.bin
```

Note that USB programmers are pretty slow, the whole operation make take
several minutes (can be 10-15 minutes in worst case). At the end of operation
you should see:

```bash
flashrom v1.2-567-gf4eb405 on Linux 5.19.9-200.fc36.x86_64 (x86_64)
flashrom is free software, get the source code at https://flashrom.org

Using clock_gettime for delay loops (clk_id: 1, resolution: 1ns).
Found Winbond flash chip "W25Q256.W" (32768 kB, SPI) on ch341a_spi.
Reading old flash chip contents... done.
Erasing and writing flash chip... Erase/write done.
Verifying flash... VERIFIED.
```

## SMBIOS unique data recovery

### Serial number format and recovery

[SMBIOS specification](https://www.dmtf.org/sites/default/files/standards/documents/DSP0134_3.4.0.pdf)
sections 7.2 and 7.3 defines two spaces for serial number: the system serial
number and baseboard serial number. The original MSI PRO Z690-A firmware
provides only the baseboard serial number.

In case you have lost your serial number in the process of flashing Dasharo or
newer MSI firmware, there is a way to retrieve it. The board has a QR code
printed on the mainboard between the chipset heatsink and dPGU PCIe slot:

![](/images/msi_sn_qr.jpg)

If you read the QR code with your smartphone you will get the full serial
number. The serial number has the format `07D25xx_LyzEaaaaaa` where:

* `07D25` - is the board model, i.e. MS-7D25 for this particular board
* `xx` is the mainboard revision which should match the revision imprinted
  between the M2_1 slot and dGPU slot. E.g. `xx=11` means VER:1.1
* `yz` is the manufacturing date in hex, i.e. `y` is the month, `z` is the
  year, for example `A1` means **October** 202**1**, `12` means **January**
  202**2**
* `aaaaaa` is the unique 6-digit number which is imprinted under the serial
  number QR code

### System UUID format and recovery

[SMBIOS specification](https://www.dmtf.org/sites/default/files/standards/documents/DSP0134_3.4.0.pdf)
section 7.2 defines a field for unique system identification with a special
number called UUID (Universally Unique IDentifier). UUID is specified by
[RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122). MSI firmware
provides the system UUID in the SMBIOS system information structure.

The problem with UUID is that it cannot be recovered if the backup binary or
SMBIOS logs are lost. You can backup the SMBIOS information with our
[Dasharo Tools Suite bootable stick](../../../dasharo-tools-suite/documentation#bootable-usb-stick).
The `dmidecode.log` will have all the necessary information. Things we know
about MSI system UUID:

* UUID format is as follows: `33221100-5544-7766-8899-AABBCCDDEEFF`, the hex
  numbers represent the order of bytes in memory for the little-endian format
  as required by SMBIOS
* MSI UUIDs do not conform to any of the RFC 4122 UUID variants/versions (the
  bits responsible for UUID version and variant identification are not constant
  across multiple boards)
* the last octet group `AABBCCDDEEFF` is equal to the MAC address of the
  on-board Intel i225 Ethernet, so **be sure to NOT share the UUID** with
  anybody as it contains system sensitive information
* the first four groups are either random numbers or some cryptographically
  acquired value from e.g. combination of some board data, unfortunately it is
  not known by us

The MAC address is printed on a sticker placed on the 2x2 SATA connector:

![](/images/msi_mac.jpg)

### SMBIOS data migration

For Dasharo simply follow the [Initial Deployment](initial-deployment.md) how
to migrate the data.

For MSI firmware you will probably need an AMI DMI/SMBIOS editor to save those
values back if you do not have a backup binary.
