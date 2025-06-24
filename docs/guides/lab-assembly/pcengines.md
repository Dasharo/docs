# Laboratory stand dedicated to PC Engines platforms assembly guide

## Introduction

This document describes platform-specific details for assembling PC Engines
apu2/3/4/6 series testing stands. Author get through the procedure on PC
Engines apu3 in his homelab. Use this document as reference while going through
[Generic Testing Stand
Setup](../../unified-test-documentation/generic-testing-stand-setup.md)

## Prerequisites

The below table contains platform-specific information about all elements which
are needed to create testing stands for Protectli machines.

!!! warning
    Please note that using RTE v1.0.0 or older change way how [OSFV
    cli](https://github.com/Dasharo/osfv-scripts/blob/main/osfv_cli/src/osfv/libs/rte.py#L284)
    works. On v1.0.0 and older there is no need for additional step of enabling
    SPI GPIO, it is required only from v1.1.0 onwards. If it would not be
    reflected in [model file](https://github.com/Dasharo/osfv-scripts/tree/main/osfv_cli/src/osfv/models)
    it may lead to issues. For more details please check [here](https://github.com/Dasharo/osfv-scripts/issues/86).

* [RTE
v1.1.0](https://shop.3mdeb.com/shop/open-source-hardware/open-source-hardware-3mdeb/rte/)
or RTE v1.0.0
* RTE power supply 5V 2A Micro-USB
* 10x standard female-female connection wire 2.54 mm raster
* 4x RJ45 cable: 1 for RTE and 3 for the platform OR
    - 5x RJ45 cable for apu4: 1 for RTE and 4 for the platform

* [apu2/3/4/6](https://www.pcengines.ch/apu2.htm)

* RS-232 D-Sub-D-Sub cross cable
* Power to the apu2/3/4/6 is delivered by 2.5/5.5 mm DC Jack cable.

### External flashing enabling

| RTE J7 pin        | PC Engines SPI pin  |
|:-----------------:|:-------------------:|
| 1 (VCC)           | 1 (VCC)             |
| 2 (GND)           | 2 (GND)             |
| 3 (CS)            | 3 (SPICS#)          |
| 4 (SCLK)          | 4 (SPICLK)          |
| 5 (MISO)          | 5 (SPIDI)           |
| 6 (MOSI)          | 6 (SPIDO)           |
| 7 (NC)            | Not connected       |
| 8 (NC)            | Not connected       |

SPI connection can be realized with IDC 8 pin wire, but 7th and 8th wires
have to be opened.

### Power and Reset switch connection

Connect the RTE J11 header to the platform front panel header using 2.54mm
wires as described in the table:

=== "APU2/APU4"

    | RTE       | PC Engines             |
    |:---------:|:----------------------:|
    | J11 pin 6 | J2 pin 3 (PWR)         |
    | J11 pin 5 | J2 pin 5 (RST)         |

=== "APU3/APU6"

    | RTE       | PC Engines             |
    |:---------:|:----------------------:|
    | J11 pin 6 | J3 pin 3 (PWR)         |
    | J11 pin 5 | J3 pin 5 (RST)         |

### Device power status readout

Connect the RTE J1 header to the platform front panel header using 2.54mm
wires as described in the table:

=== "APU2"

    | RTE                             | PC Engines             |
    |:-------------------------------:|:----------------------:|
    | J1 pin 1(Closer to J7 header)   | J4 pin 8 (APU_LED1)    |
    | J1 pin 2                        | J4 pin 7 (APU_LED2)    |
    | J1 pin 3                        | J4 pin 6 (APU_LED3)    |

=== "APU3/APU4/APU6"

    | RTE                             | PC Engines             |
    |:-------------------------------:|:----------------------:|
    | J1 pin 1(Closer to J7 header)   | J5 pin 8 (APU_LED1)    |
    | J1 pin 2                        | J5 pin 7 (APU_LED2)    |
    | J1 pin 3                        | J5 pin 6 (APU_LED3)    |

## Theory of operation

The following sections describe how to use all of the enabled features:

* serial connection to the platform,
* controlling power supply,
* enabling basic power actions with the platform (power off/power on/reset),
* external flashing with the RTE,
* CMOS reset.

### Serial connection

The method of setting and using serial connection is described in the
[Serial connection guide](../../transparent-validation/rte/v1.1.0/serial-port-connection-guide.md).

### Power supply controlling

Power supply controlling is performed with the relay module on RTE
connected to one of RTE GPIOs. Power operation should be performed using
the `rte_ctrl` script implemented in `meta-rte` (OS image dedicated to the
RTE platform).

To toggle the power supply use the below command:

```bash
rte_ctrl rel
```

Or using [OSFV cli](https://github.com/Dasharo/osfv-scripts) from remote
machine:

```sh
osfv_cli rte --model=<APU2/3/4/6> --rte_ip <ip_address> rel tgl
```

### Basic power operations

Basic power operations should be performed based on the `rte_ctrl` script
implemented in `meta-rte` (OS image dedicated to the RTE platform). To perform
basic power operations use the below-described commands:

1. Turn on the platform:

    ```bash
    rte_ctrl pon
    ```

1. Turn off the platform:

    ```bash
    rte_ctrl poff
    ```

1. Reset the platform:

    ```bash
    rte_ctrl reset
    ```

Or using OSFV cli from remote machine:

```sh
osfv_cli rte --model=<APU2/3/4/6> --rte_ip <ip_address> pwr on
```

```sh
osfv_cli rte --model=<APU2/3/4/6> --rte_ip <ip_address> pwr off
```

```sh
osfv_cli rte --model=<APU2/3/4/6> --rte_ip <ip_address> pwr reset
```

### CMOS clear

To clear the CMOS, turn off the power with Sonoff or relay and use the
following commands:

```bash
echo 1 > /sys/class/gpio/gpio412/value
sleep 10
echo 0 > /sys/class/gpio/gpio412/value
```

### S1 button

S1 button is used to re-enable disabled serial console. More information about
this feature can be found in:

* [S1 switch button properties](https://pcengines.github.io/apu2-documentation/gpios/#s1-switch-button)
* [Disable serial console and enable with S1 button](https://pcengines.github.io/apu2-documentation/theory-of-operation/#pc-engines-apu-firmware-features)

To expose this feature to OSFV we have to add additional wire between:

=== "APU2"

    | RTE J11 pin       | PC Engines J4 pin   |
    |:-----------------:|:-------------------:|
    | 7                 | 5 (MODESW#)         |

=== "APU3/APU4/APU6"

    | RTE J11 pin       | PC Engines J5 pin   |
    |:-----------------:|:-------------------:|
    | 7                 | 5 (MODESW#)         |

### USB devices

Since some issues with USB controllers may only happen on select USB ports,
it's important to plug in USB devices to all external USB ports of the board.

### SD card

Insert at least 16GB SD card into platform SD card socket.

### BIOS WP

BIOS WP (aka SPIWP#) pin can be used to enable or disable write protection.
Feature was described in [sortbootorder
documentation](https://github.com/pcengines/sortbootorder?tab=readme-ov-file#bios-wp-option).

=== "APU2"

    | RTE J11 pin       | PC Engines J2 pin   |
    |:-----------------:|:-------------------:|
    | 9                 | 1 (SPIWP#)          |

=== "APU3/APU4/APU6"

    | RTE J11 pin       | PC Engines J3 pin   |
    |:-----------------:|:-------------------:|
    | 9                 | 1 (SPIWP#)          |
