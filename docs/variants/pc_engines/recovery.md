# Recovery

## Intro

The following documentation describes the process of recovering hardware from
the brick state with [RTE](../../transparent-validation/rte/introduction.md) and
Dasharo open-source firmware.

## Prerequisites

1. Recovery with RTE:
    - [Prepared RTE](../../transparent-validation/rte/v1.1.0/quick-start-guide.md)
    - 6x female-female wire cables
2. Recovery with spi1a recovery dongle:
    - [spi1a](https://www.pcengines.ch/spi1a.htm)

## Recovery with RTE

### Connections

To prepare the stand for flashing follow the steps described below:

1. Open the platform cover.
2. Connect the 6-pin flash header to the
   [SPI header](../../transparent-validation/rte/v1.1.0/specification.md)
   on RTE.

    | SPI header | J9 pin header |
    |:----------:|:- -----------:|
    | Vcc        | pin 1 (Vcc)   |
    | GND        | pin 2 (GND)   |
    | CS         | pin 3 (CS)    |
    | SCLK       | pin 4 (CLK)   |
    | MISO       | pin 5 (MISO)  |
    | MOSI       | pin 6 (MOSI)  |

    ```txt
                    J9
                  ______
              >  |      |
     Vcc 3.3V  ----1  2----  GND
                 |      |
         CS  ----3    4----  CLK
                 |      |
         MISO  ----5  6----  MOSI
                 |______|
    ```

### Firmware flashing

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

## Recovery with spi1a dongle

1. Power off the platform.
2. Plug the spi1a into J9 header on apu, so that the thick white line on the
   dongle matches the thick line printed on board near J9 header.
3. Power on the platform.
4. Boot to operating system, e.g. Dasharo Tools Suite.
5. Remove the dongle.
6. Perform [Initial Deployment](initial-deployment.md) with the target
   firmware variant.

!!! warning "Do not keep the spi1a dongle plugged while in OS"

    Remove the dongle as soon as you boot the operating system to avoid
    accidental flashing of the dongle itself. The dongle is designed in a way
    that the SPI flash controller directs the SPI transactions to the dongle,
    instead of the on-board SPI flash. Be sure to remove the dongle,
    before you attempt to flash a new, working firmware image.
