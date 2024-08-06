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

    | RTE SPI header | 8 pin J1 header |
    |:--------------:|:---------------:|
    | Vcc            | pin 1 (Vcc)     |
    | GND            | pin 2 (GND)     |
    | CS             | pin 3 (CS)      |
    | SCLK           | pin 4 (CLK)     |
    | MISO           | pin 5 (MISO)    |
    | MOSI           | pin 6 (MOSI)    |

    ```txt
                  ______
              >  |      |
     Vcc 3.3V  ----1  2----  GND
                 |      |
           CS  ----3  4----  CLK
                 |      |
         MISO  ----5  6----  MOSI
                 |      |
           NC  ----7  8----  IO3L
                 |______|
    ```

> The IO3L signal is used to cut off the SPI flash from the SoC for flashing
> the board while it is powered. However, with RTE it is not necessary to
> drive this signal.

## Firmware flashing

To flash firmware follow the steps described below:

1. Login to RTE via `ssh` or `minicom`.
2. Turn off the platform by disconnecting the power supply (turn off the
   relay).
3. Set the proper state of the SPI by using the following commands on RTE:

    ```bash
    # set SPI Vcc to 3.3V
    echo 1 > /sys/class/gpio/gpio405/value
    # SPI Vcc on
    echo 1 > /sys/class/gpio/gpio406/value
    # SPI lines ON
    echo 1 > /sys/class/gpio/gpio404/value
    ```

4. Wait at least 2 seconds.
5. Flash the platform by using the following command:

    ```bash
    flashrom -p linux_spi:dev=/dev/spidev1.0,spispeed=16000 -w [path_to_binary]
    ```

    > Flashing with flashrom takes about 1 minute.

6. Change back the state of the SPI by using the following commands:

    ```bash
    echo 0 > /sys/class/gpio/gpio404/value
    echo 0 > /sys/class/gpio/gpio406/value
    ```

7. Turn on the platform by connecting the power supply.
