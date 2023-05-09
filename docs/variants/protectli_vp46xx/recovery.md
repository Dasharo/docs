# Recovery

## Intro

Following documentation describes the process of recovering hardware from brick
state with [RTE](../../transparent-validation/rte/introduction.md) and Dasharo
open-source firmware.

# Prerequisites

* [Prepared RTE](../../transparent-validation/rte/v1.1.0/quick-start-guide.md)
* Pomona clip

# Connections

* Power supply - TBD (photos + info)
* SPI - TBD (photos + table)

# Firmware flashing using flashrom

To flash Protectli's firmware follow the steps shown below:

1. Login to RTE via `ssh` or `minicom`.
1. Turn on platform power supply by using the following command:

    ```bash
    echo 1 > /sys/class/gpio/gpio199/value
    ```

1. Wait at least 5 seconds.
1. Turn off the platform by using the following command:

    ```bash
    ./rte_ctrl -poff
    ```

1. Wait at least 3 seconds.
1. Set the proper state of the SPI by using the following commands:

    ```bash
    # set SPI Vcc to 3.3V
    echo 1 > /sys/class/gpio/gpio405/value
    # SPI Vcc on
    echo 1 > /sys/class/gpio/gpio406/value
    # SPI lines ON
    echo 1 > /sys/class/gpio/gpio404/value
    ```

1. Wait at least 2 seconds.
1. Cut off the platform's power supply by using the following command:

    ```bash
    ./rte_ctrl -rel
    ```

1. Wait at least 2 seconds.
1. Flash the platform by using the following command:

    ```bash
    flashrom -p linux_spi:dev=/dev/spidev1.0,spispeed=16000 -w $1 -c "MX25L12835F/MX25L12845E/MX25L12865E"
    ```

    > Where $1 is the directory to the firmware with its name. Flashing with
      flashrom takes about 1-2 minutes.

1. Reset CMOS by using the folling commands:

    ```bash
    # set GPIO 413 state low
    echo 1 > /sys/class/gpio/gpio413/value
    # Wait for battery discharge
    sleep 10
    # set GPIO 413 state high
    echo 0 > /sys/class/gpio/gpio413/value
    ```
