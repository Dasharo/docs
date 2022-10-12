# Serial port connection guide

This document describes how to set up a serial connection between RTE and
another device.

## Prerequisites

* [Prepared RTE](../v1.1.0/quick-start-guide.md)
* Two jumpers
* Choose one of the following cables depending on the connectivity to your
    platform:
    - RS232-RJ45 cable
    - RS232-RS232 cable
    - 3 wire cables

## Setting serial connection

1. Connect the RTE header (J14 or J18) with the device serial port.
1. Put the two jumpers on
    [RTE J16 Header](../specification/#uart-output-select-header):

    1. For the RS232 port, they join COM and RS232 rows both on RX and TX
        columns.
    1. For the UART port, they join COM and EXT rows both on RX and TX
        columns.

1. Connect with RTE via `ssh` or `minicom`.
1. There are two ways to open a serial connection:
    1. Telnet - by executing the following command:

        ```bash
        telnet 192.168.X.X 13541
        ```

        > To configure telnet, update the file `/etc/ser2net.conf`

    1. Minicom - by executing the following command:

        ```bash
        minicom -D /dev/ttyS1 -o -b 115200
        ```

        > `ttyS1` can be different in some cases.
