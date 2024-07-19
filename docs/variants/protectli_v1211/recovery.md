# Recovery

## Intro

The following documentation describes the process of recovering hardware from
the brick state with [RTE](../../transparent-validation/rte/introduction.md) and
Dasharo open-source firmware.

## Prerequisites

* [Prepared RTE](../../transparent-validation/rte/v1.1.0/quick-start-guide.md)
* 6x female-female wire cables

## Connections

To prepare the stand for flashing follow the steps described below:

1. Open the platform cover.
2. Connect the 6-pin flash header to the
   [SPI header](../../transparent-validation/rte/v1.1.0/specification.md)
   on RTE.

    | SPI header | 6 pin header |
    |:----------:|:------------:|
    | Vcc        | pin 1 (Vcc)  |
    | GND        | pin 2 (GND)  |
    | CS         | pin 4 (CS)   |
    | SCLK       | pin 6 (CLK)  |
    | MISO       | pin 5 (MISO) |
    | MOSI       | pin 3 (MOSI) |

    ```txt
                  ______
              >  |      |
     Vcc 3.3V  ----1  2----  GND
                 |      |
         MOSI  ----3  4----  CS
                 |      |
         MISO  ----5  6----  CLK
                 |______|
    ```

## Firmware flashing

To flash firmware follow the steps described below:

1. Login to RTE via `ssh` or `minicom`.
1. Turn on the platform by connecting the power supply.
1. Wait at least 5 seconds.
1. Turn off the platform by using the power button.
1. Wait at least 3 seconds.
1. Set the proper state of the SPI by using the following commands on RTE:

    ```bash
    # set SPI Vcc to 3.3V
    echo 1 > /sys/class/gpio/gpio405/value
    # SPI Vcc on
    echo 1 > /sys/class/gpio/gpio406/value
    # SPI lines ON
    echo 1 > /sys/class/gpio/gpio404/value
    ```

1. Wait at least 2 seconds.
1. Disconnect the power supply from the platform.
1. Wait at least 2 seconds.
1. Flash the platform by using the following command:

    ```bash
    flashrom -p linux_spi:dev=/dev/spidev1.0,spispeed=16000 -w [path_to_binary]
    ```

    > Flashing with flashrom takes about 1 minute.

1. Change back the state of the SPI by using the following commands:

    ```bash
    echo 0 > /sys/class/gpio/gpio404/value
    echo 0 > /sys/class/gpio/gpio406/value
    ```

1. Turn on the platform by connecting the power supply.

The first boot of the platform after proceeding with the above procedure can
take much longer than standard.
