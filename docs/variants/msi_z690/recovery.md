# Dasharo compatible with MSI PRO Z690-A WIFI DDR4 - recovery

## Intro

The project is in early development phase. It may happen that on certain
hardware configurations the Dasharo firmware will not boot correctly (i.e.
we will have "bricked" platform). In such a case, recovery procedure can
install back the original firmware from the board manufacturer.

### MSI Flash BIOS Button

The [MSI Flash BIOS Button](https://www.youtube.com/watch?v=iTkXunUAriE)
would give us easy-to-use recovery method. We have tried that one to switch
from Dasharo firmware to the original one, but it did not work, unfortunately.
The details of how this process exactly works are unknown due to the closed
nature of it's implementation. We can research this topic more in the future,
so maybe it can be utilized later for deployment and/or recovery of the
platform.

### External flashing with programmer

In this case, using external programmer is necessary. We are using
[RTE](https://3mdeb.com/open-source-hardware/#rte)
here.

* Connect programmer to the flash chip as shown in the
  [Hardware connection / SPI](../development/#hardware-connection) section of
  the `Development` documentation.

* Download official BIOS from vendor's website (this is the newest version, you
  may choose an older one too or in the best case use your firmware backup):

```bash
$ wget https://download.msi.com/bos_exe/mb/7D25v13.zip
$ unzip 7D25v13.zip
```

* Flash via external programmer:

> The command line will be different, depending on the programmer you use

```bash
$ flashrom -p linux_spi:dev=/dev/spidev1.0,spispeed=16000 -w 7D25v13/E7D25IMS.130
```

* First boot after the recovery process is significantly longer

## SMBIOS unique data recovery

### Serial number format and recovery

[SMBIOS specification](https://www.dmtf.org/sites/default/files/standards/documents/DSP0134_3.4.0.pdf)
sections 7.2 and 7.3 defines two spaces for serial number: the system serial
number and baseboard serial number. The original MSI PRO Z690-A firmware
provides only baseboard serial number.

In case you have lost your serial number in the process of flashing Dasharo or
newer MSI firmware, there is a way to retrieve it. The board has a QR code
imprinted between the chipset heatsink and dPGU PCIe slot:

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
[fwdump-docker](https://github.com/3mdeb/fwdump-docker). The `dmidecode.log`
will have all the necessary information. Things we know about MSI system UUID:

- UUID format is as follows: `33221100-5544-7766-8899-AABBCCDDEEFF`, the hex
  numbers represent the order of bytes in memory for the little-endian format
  as required by SMBIOS
- MSI UUIDs do not conform to any of the RFC 4122 UUID variants/versions (the
  bits responsible for UUID version and variant identification are not constant
  across multiple boards)
- the last octet group `AABBCCDDEEFF` is equal to the MAC address of the
  on-board Intel i225 Ethernet, so **be sure to NOT share the UUID** with
  anybody as it contains system sensitive information
- the first four groups are either random numbers or some cryptographically
  acquired value from e.g. combination of some board data, unfortunately it is
  not known by us

The MAC address is printed on a sticker placed on the 2x2 SATA connector:

![](/images/msi_mac.jpg)

### SMBIOS data migration

For Dasharo simply follow the [Installation manual](installation-manual.md) how
to migrate the data.

For MSI firmware you will probably need an AMI DMI/SMBIOS editor to save those
values back if you do not have a backup binary.
