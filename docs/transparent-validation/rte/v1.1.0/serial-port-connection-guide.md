# Serial port connection guide

This document describes how to set up a serial connection between RTE and
another device.

## Prerequisites

* [Prepared RTE](../v1.1.0/quick-start-guide.md)
* Two jumpers
* Choose one of the following cables depending on the connectivity to your
    platform:
    - RS232<->RJ45 cable,
    - RS232<->RS232 cable,
    - USB<->RS232 cable,
    - micro-USB<->USB cable,
    - 3-wire cable.

## Setting serial connection

1. Put the two jumpers on
    [RTE J16 Header](./specification.md#uart-output-select-header):

    1. For the RS232 port, they join COM and RS232 rows both on RX and TX
        columns.
    1. For the UART port (only during using a 3-wire cable), they join COM and
        EXT rows both on RX and TX columns.
    1. For the micro-USB-USB cable, jumpers aren't required.

1. Connect the RTE header (J14 or J18) with the device serial port. Use the
    cable according to the DUT specification:

    1. DUT has a serial port -> needs to use an RS232<->RS232 cable.
    1. DUT has the debug port in the form of the RJ45 -> needs to use an
        RS232<->RJ45 cable.
    1. DUT has the debug port in the form of the USB -> needs to use an
        RS232<->USB cable.
    1. DUT has the debug port in the form of the micro-USB -> needs to use a
        micro-USB<->USB cable.
    1. DUT doesn't have a port but has pins for serial connection on the board
        -> need to use a 3-wire cable.

1. Connect with RTE via `ssh` or `minicom`. To connect via `ssh` is required to
    know RTE IP and connection to the internet on both sides. While using a
    `minicom` there is a need to use the USB-UART converter.
1. There are two ways to open a serial connection:
    1. Telnet - by executing the following command:

        ```bash
        telnet 192.168.X.X 13541
        ```

        > To configure telnet connections, update the file `/etc/ser2net.conf`
        > using `vim`. Then reboot the RTE to apply the changes. The `dmesg`
        > command allows to identify the latest connected devices.

    1. Minicom - by executing the following command:

        ```bash
        minicom -D /dev/ttyS1 -o -b 115200
        ```

        > Replace `ttyS1` with `ttyUSB0` while using micro-USB-USB cable.
