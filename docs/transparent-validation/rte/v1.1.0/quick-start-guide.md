# Quick start guide

The canonical example of RTE usage is hooking it to some hardware for SPI
flashing, power control and serial logs gathering. This document describes the
common preparation of RTE without listed functions.

## Prerequisites

* [RTE board](https://3mdeb.com/shop/open-source-hardware/open-source-hardware-3mdeb/rte/)
    (this document is based on v1.1.0)
* Micro-USB 5V 2.5A power supply
* Orange Pi
* SD card
* Ethernet cable
* USB-UART converter with 3 wire cables
* Ubuntu (based on 22.04)

## Preparation of RTE

1. Build RTE image using the
    [meta-rte repository](https://github.com/3mdeb/meta-rte).
1. Flash SD card using this image. The flashing method isn't imposed but an
    [etcher](https://www.balena.io/etcher/) is recommended.
1. Insert SD card into Orange Pi.
1. Insert Orange Pi into RTE.
1. Connect the ethernet cable to Orange Pi.
1. Plug the USB-UART converter into your computer and connect its pins with
    [RTE J2 Header](../specification/#uart0-header). (you may need a
    USB extension cable)

    |UART Converter | RTE J2 Header|
    |:-------------:|:------------:|
    | GND           | GND          |
    | TXD           | RX           |
    | RXD           | TX           |

1. Open the serial connection with RTE from your PC using a previously connected
    USB-UART converter by executing the following command:

    ```bash
    sudo minicom -D /dev/ttyUSB<x>
    ```

    Substitute `<x>` with the device number corresponding to your USB-UART
    Converter for example `/dev/ttyUSB0` if it is the only converter connected
    to your PC.

1. Plug the power supply into the RTE J17 Micro-USB slot.
1. Login into the device by using the default credentials:
    - Login: `root`
    - Password: `meta-rte`
