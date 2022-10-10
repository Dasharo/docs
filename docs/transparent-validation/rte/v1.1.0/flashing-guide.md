# Flashing guide

This document describes how to set up external flashing on some devices using
RTE.

## NS50/70PU

## Prerequisites

* [Prepared RTE](../v1.1.0/quick-start-guide.md)
* WSON PROBE
* 8 wire cables

## Flashing

1. RTE CONNECTION WITH PROBE WSON TBD.
1. Unscrew the bottom cover of the laptop.
1. Disconnect the battery

    > All power must be removed from the laptop during flashing.

1. Localize the flash chip: photo?
1. Connect and ...

    <!-- 1. Turn on SPI header by executing the following commands:

    ```bash
    echo 1 > /sys/class/gpio/gpio405/value
    sleep 1
    echo 1 > /sys/class/gpio/gpio404/value
    sleep 1
    echo 1 > /sys/class/gpio/gpio406/value
    ```

    1. Flash chip by executing the following command:

        ```bash
        flashrom -p linux_spi:dev=/dev/spidev1.0,spispeed=16000 -w coreboot.rom
        ```

    1. Turn off SPI header by executing the following commands:

        ```bash
        echo 0 > /sys/class/gpio/gpio406/value
        echo 0 > /sys/class/gpio/gpio404/value
        echo 0 > /sys/class/gpio/gpio405/value
        ``` -->

1. Reconnect the battery and screw in the bottom cover.
1. Power on the device.
