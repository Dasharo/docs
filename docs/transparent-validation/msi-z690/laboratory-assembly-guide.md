# Laboratory stand dedicated to MSI PRO Z690-A assembly guide

## Introduction

This document describes the assembly procedure dedicated to the MSI PRO Z690-A
testing stand.

## Prerequisites

The below table contains information about all elements which are needed to
create the testing stand.

* MSI PRO Z690-A platform
* [RTE v1.1.0](https://3mdeb.com/shop/open-source-hardware/open-source-hardware-3mdeb/rte/)
* Sonoff S20 type E
* 4x standard female-female connection wire 2.54 mm raster
* 7x standard female-female connection wire 2.54/2.00 mm raster
* USB-UART converter with 4-wire cable
* 4-pin header 2.54 mm raster

## Pre-setup activities

The following subsections describe the method of preparing all the
components of the laboratory stand.

### MSI PRO Z690-A

MSI PRO Z690-A platform should be prepared in accordance with the
[Motherboard assembly](presale-assembly-and-validation.md#motherboard-assembly-only)
documentation.

### RTE

RTE (acronym: Remote Testing Environment) should be prepared in accordance with
[Quick start guide](../rte/v1.1.0/quick-start-guide.md) documentation dedicated
to the device.

### Sonoff

Sonoff should be prepared in accordance with
[Quick start guide](../sonoff/quick-start-guide.md#quick-start-guide)
documentation dedicated to the device.

## Connections

The following sections describe how to enable all of the following features:

* serial connection to the platform,
* controlling power supply,
* enabling basic power actions with the platform (power off/power on/reset),
* external flashing with the RTE.

### Serial connection

1. Attach the jumpers in the RTE J16 header to enable header J18:

    | Jumper position (TX)      | Jumper position (RX)            |
    |:-------------------------:|:-------------------------------:|
    | EXT + COM                 | EXT + COM                       |

1. Connect the RTE J18 header to the platform JBD1 header as described in the
    table:

    | RTE             | MSI PRO Z690-A                            |
    |:---------------:|:-----------------------------------------:|
    | J18 pin 1 (GND) | JBD1 pin 1 (pin closer to JBAT1)          |
    | J18 pin 2 (RX)  | JBD1 pin 2 (pin further from JBAT1)       |

    > Note: Pins on JBD1 are not described in the documentation. They have been
    discovered experimentally. Pay attention to the connections.

    ![IMG](images/msi_z690_lab_serial_panel.jpg)
    ![IMG](images/msi_z690_lab_serial_RTE.jpg)

### Power supply controlling

Connect SeaSonic FOCUS Plus Platinum to Sonoff.

### Basic power operations enabling

Connect the RTE J11 header to the platform JFP1 header as described in the
table:

| RTE            | Msi Z690                    |
|:--------------:|:---------------------------:|
| J11 pin 9      | JFP1 pin 6 (PWR_ON)         |
| J11 pin 8      | JFP1 pin 7 (RST)            |
| J15 pin 1 (GND)| JFP1 pin 5 (GND)            |

![IMG](images/msi_z690_lab_chip_power_RTE.jpg)
![IMG](images/msi_z690_lab_chip_ground_RTE.jpg)
![IMG](images/msi_z690_lab_chip_power_connections.jpg)

### External flashing enabling

Connect the RTE SPI header to the platform as described in the table:

| RTE SPI header    | MSI Z690                                             |
|:-----------------:|:----------------------------------------------------:|
| J7 pin 1 (Vcc)    | JTPM1 pin 1 (SPI Power)                              |
| J7 pin 2 (GND)    | JTPM1 pin 7 (GND)                                    |
| J7 pin 3 (CS)     | Pin soldered to SPI chip pin 1 (CS), see image below |
| J7 pin 4 (SCLK)   | JTPM1 pin 6 (SPI Clock)                              |
| J7 pin 5 (MISO)   | JTPM1 pin 3 (MISO)                                   |
| J7 pin 6 (MOSI)   | JTPM1 pin 4 (MOSI)                                   |

> Note: external access to the flash chip is possible only from the JTPM header.
As the header does not provide a connection to the `CS` pin, the connection
should be provided by direct soldering to the one of flash chip pins

![IMG](images/msi_z690_lab_chip_weld.jpg)
![IMG](images/msi_z690_spi.jpeg)
![IMG](images/msi_z690_lab_SPI_RTE.jpg)

### Complete Setup

After preparing all of the connections also three activities should be
performed to enable all of the test stand features:

1. Connect Sonoff to the mains:

    ![IMG](images/sonoff_connected.jpg)

1. Connect the RTE to the Internet by using the Ethernet cable.
1. Connect the RTE to the mains by using the microUSB 5 V/2 A power supply.

Complete setup should looks as follows:

![Complete](images/msi_z690_lab_complete.jpg)

## Theory of operation

The following sections describe how to use all of the enabled features:

* serial connection to the platform,
* controlling power supply,
* enabling basic power actions with the platform (power off/power on/reset),
* external flashing with the RTE.

### Serial connection

The method of setting and using serial connection is described in the
[Serial connection guide](../rte/v1.1.0/serial-port-connection-guide).

### Power supply controlling

Power supply controlling (in this case: controlling the state of Sonoff)
should be performed based on the `sonoff.sh` script implemented in `meta-rte`
(OS image dedicated to the RTE platform).

[Sonoff power supply controlling](../sonoff/quick-start-guide.md#power-supply-controlling)

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

> Note, that in order for the above commands to work properly, the platform
should be powered up: both Sonoff and the power supply must be turned on.

### External flashing

The external flashing procedure should be performed based on the scripts
implemented on the RTE platform. To perform the flashing operation reproduce,
the below-described steps:

1. By using `scp` put the requested Dasharo file to the RTE:

    ```bash
    scp <path_to_firmware>/<firmware_file> root@<RTE_IP>:/tmp/coreboot.rom
    ```

    Where:

    - `path_to_firmware` - path to firmware, which should send to RTE,
    - `firmware_file` - the name of the firmware file, which should be sent
        to RTE,
    - `RTE_IP` - IP address of the connected RTE.

1. Login to RTE via `ssh` or `minicom`.
1. Read the flash chip by executing the following command on RTE:

    ```bash
    ./flash.sh read tmp/dump.rom
    ```

1. If the reading was successful, the output from the command above should
    contain the phrase `Verifying flash... VERIFIED`.
1. Write the flash chip by executing the following command on RTE:

    ```bash
    ./flash.sh write /tmp/coreboot.rom
    ```

    > Do not interrupt the flashing procedure in any way (especially by
    changing connections). It may cause hardware damage!

1. If the reading was successful, the output from the command above should
    contain the phrase `Verifying flash... VERIFIED`.
