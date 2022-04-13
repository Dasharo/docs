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
[RTE](https://3mdeb.com/shop/open-source-hardware/open-source-hardware-3mdeb/rte/)
here.

* Connect programmer to the flash chip as shown in the
  [Hardware connection / SPI](development.md/#hardware-connection) section of
  the `Development` documentation.

* Download official BIOS from vendor's website:

```bash
$ wget https://download.msi.com/bos_exe/mb/7D25vA31.zip
$ unzip 7D25vA31.zip
```

* Flash via external programmer:

> The command line will be different, depending on the programmer you use

```bash
$ flashrom -p linux_spi:dev=/dev/spidev1.0,spispeed=16000 -w 7D25vA31/E7D25IMS.A31
```

* First boot after the recovery process is significantly longer
