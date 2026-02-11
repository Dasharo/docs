# Laboratory stand dedicated to MSI PRO B850 platforms assembly guide

## Introduction

This document describes platform-specific details for assembling an MSI PRO
B 850 testing stand. Use this document as reference while going
through [Generic Testing Stand
Setup](../../unified-test-documentation/generic-testing-stand-setup.md)

## Prerequisites

The below table contains information about all elements which are needed to
create the testing stand.

* MSI PRO B850 platform
* [RTE v1.1.0](https://shop.3mdeb.com/shop/open-source-hardware/open-source-hardware-3mdeb/rte/)
* Sonoff S20 type E
* 7x standard female-female connection wire 2.54 mm raster
* 7x standard female-female connection wire 2.54/2.00 mm raster

## Connections

The following sections describe how to enable all of the following features:

* serial connection to the platform,
* controlling power supply,
* enabling basic power actions with the platform (power off/power on/reset),
* external flashing with the RTE,
* device power status readout.
* enabling cmos clear

### Serial connection

1. Attach the jumpers in the RTE J16 header to enable header J18:

    | Jumper position (TX)      | Jumper position (RX)            |
    |:-------------------------:|:-------------------------------:|
    | EXT + COM                 | EXT + COM                       |

1. Connect the RTE J18 header to the platform JBD1 header as described in the
    table:

    | RTE             | MSI PRO B850            |
    |:---------------:|:-----------------------:|
    | J18 pin 1 (GND) | JCOM1 pin 5             |
    | J18 pin 2 (RX)  | JCOM1 pin 3             |
    | J18 pin 3 (TX)  | JCOM1 pin 2             |

### Power supply controlling

Connect SeaSonic FOCUS Plus Platinum to Sonoff.

### Basic power operations enabling

Connect the RTE J11 header to the platform JFP1 header as described in the
table:

| RTE            | MSI PRO B850                |
|:--------------:|:---------------------------:|
| J11 pin 9      | JFP1 pin 6 (PWR_ON)         |
| J11 pin 8      | JFP1 pin 7 (RST)            |
| J15 pin 1 (GND)| JFP1 pin 5 (GND)            |
| J10 pin 1      | JFP1 pin 2 (PWR_LED)        |

![msi_b850_lab_chip_power_connections](images/msi_b850_lab_chip_power_connections.jpg)

### CMOS Clear enabling

Connect the RTE J11 header to the platform JBAT1 header as described in the
table:

| RTE            | MSI PRO B850                    |
|:--------------:|:-------------------------------:|
| J11 pin 11  | JBAT1 pin 2(closer to JFP1)     |

![msi_b850_cmos](images/msi_b850_cmos.jpg)

### External flashing enabling

#### Without discrete TPM

Connect the RTE SPI header to the platform as described in the table:

| RTE SPI header      | MSI PRO B850                                         |
|:-------------------:|:----------------------------------------------------:|
| J7 pin 1 (Vcc)      | JTPM1 pin 1 (SPI Power)                              |
| J7 pin 2 (GND)      | JTPM1 pin 7 (GND)                                    |
| J7 pin 3 (CS)       | JTPM1 pin 5 (RESERVED / BIOS SPI CS pin)             |
| J7 pin 4 (SCLK)     | JTPM1 pin 6 (SPI Clock)                              |
| J7 pin 5 (MISO)     | JTPM1 pin 3 (MISO)                                   |
| J7 pin 6 (MOSI)     | JTPM1 pin 4 (MOSI)                                   |

> Note: external access to the flash chip is possible only from the JTPM
> header. JTPM1 is a 2mm pitch header, you will need 2mm to 2.54mm
> female-female dupont wires to connect to RTE.

![msi_b850_spi](images/msi_b850_spi.jpg)

### Complete Setup

After preparing all of the connections also three activities should be
performed to enable all of the test stand features:

1. Connect Sonoff to the mains:

    ![sonoff_connected](images/sonoff_connected.jpg)

1. Connect the RTE to the Internet by using the Ethernet cable.
1. Connect the RTE to the mains by using the microUSB 5 V/2 A power supply.

Complete setup should looks as follows:

![msi_b850_lab_complete](images/msi_b850_lab_complete.jpg)

## Theory of operation

The following sections describe how to use all of the enabled features:

* serial connection to the platform,
* controlling power supply,
* enabling basic power actions with the platform (power off/power on/reset),
* external flashing with the RTE,
* device power status readout.
* enabling Cmos clear

### Serial connection

The method of setting and using serial connection is described in the
[Serial connection guide](../../transparent-validation/rte/v1.1.0/serial-port-connection-guide.md).

### Power supply controlling

Power supply controlling (in this case: controlling the state of Sonoff)
should be performed based on the `sonoff.sh` script implemented in `meta-rte`
(OS image dedicated to the RTE platform).

> Note, that before using the above-mentioned script, it should be modified and
`SONOFF_IP` parameter should be set in accordance with obtained Sonoff IP address.

To perform basic power operations use the below-described commands:

1. Turn on the power supply:

    ```bash
    ./sonoff on
    ```

1. Turn off the power supply:

    ```bash
    ./sonoff on
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

> Note, that in order for the above commands to work properly, the platform
should be powered up: both Sonoff and the power supply must be turned on.

### External flashing

The external flashing procedure should be performed based on the scripts
implemented on the RTE platform. To perform the flashing operation reproduce,
the below-described steps:

> Note: the `flash.sh` script, used in this chapter, is available only in 0.8.1
> or newer RTE OS releases, check [meta-rte](https://github.com/3mdeb/meta-rte)
> for more inf..

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

### Device power status readout

To read the current power status use the following command:

```bash
cat /sys/class/gpio/gpio12/value
```

Example output:

* `1` means that the platform is turned on.
* `0` means that the platform is turned off.

### CMOS clear

To clear the CMOS, turn off the power with Sonoff or relay and use the
following commands:

```bash
echo 1 > /sys/class/gpio/gpio412/value
sleep 10
echo 0 > /sys/class/gpio/gpio412/value
```
