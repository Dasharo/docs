# Laboratory stand dedicated to Protectli platforms assembly guide

## Introduction

This document describes platform-specific details for assembling Protectli
VP2410, VP2420, VP4630/VP4650/VP4670, V1000 series testing stands.
Use this document as reference while going through
[Generic Testing Stand Setup](../../unified-test-documentation/generic-testing-stand-setup.md)

## Prerequisites

The below table contains platform-specific information about all elements which
are needed to create testing stands for Protectli machines.

* [RTE v1.1.0](https://shop.3mdeb.com/shop/open-source-hardware/open-source-hardware-3mdeb/rte/)
* RTE power supply 5V 2A Micro-USB
* 6x standard female-female connection wire 2.54 mm raster
* 6x standard female-female connection wire 2.54/2.00 mm raster
* 2x RJ45 cable: 1 for RTE and 1 for the platform

When there are 4 or more Ethernet ports on the platform,
connect ports 3 and 4 together with an additional RJ45 cable.

=== "VP2410"

    * VP2410 platform
    * Power supply for the platform: 12V 5A
    * Micro-USB to USB-A male-male cable for console

=== "VP2420"

    * VP2420 platform
    * Power supply for the platform: 12V 5A
    * Micro-USB to USB-A male-male cable for console

=== "VP46XX"

    * VP46XX platform
    * Sonoff S20 type E (relay unused due to disruptions in power during high CPU load)
    * USB-UART converter with 4-wire cable
    * 4-pin header 2.54 mm raster
    * Pomona SOIC8 clip
    * Micro-USB to USB-A male-male cable for console
    * Power supply for the platform:
        - VP4630: 12V 5A
        - VP4650/VP4670: 12V 7.5A

=== "V1000 series"

    * V1000 series platform
    * Power supply for the platform: 12V 4A
    * USB-C to USB-A male-male cable for console

=== "VP66XX"

    * VP66XX platform
    * Sonoff S20 type E (relay unused due to disruptions in power during high CPU load)
    * USB-UART converter with 4-wire cable
    * 4-pin header 2.54 mm raster
    * Pomona SOIC8 clip
    * USB-C to USB-A male-male cable for console
    * Power supply for the platform: 12V 10A

### External flashing enabling

=== "VP2410"

    External flashing not possible with Pomona clip, the flash chip lies under
    the chassis, which serves the cooling purposes. One option is to drill a
    hole in the case where the flash chip lies.

=== "VP2420"

    External flashing not possible with Pomona clip, the flash chip lies under
    the SODIMM module.

=== "VP46XX"

    Flash chip is socketed. One has to desolder the socket, solder the flash
    chip in place of the socket and connect the Pomona SOIC8 clip.

=== "V1000 series"

    Connect the RTE SPI header to the platform using the 2.54mm female-female
    wires as described in the table:

    | RTE SPI header      | 6pin flash header                      |
    |:-------------------:|:--------------------------------------:|
    | J7 pin 1 (Vcc)      | <TBD marking> pin 1 (SPI Power)        |
    | J7 pin 2 (GND)      | <TBD marking> pin 2 (GND)              |
    | J7 pin 3 (CS)       | <TBD marking> pin 4 (BIOS SPI CS pin)  |
    | J7 pin 4 (SCLK)     | <TBD marking> pin 6 (SPI Clock)        |
    | J7 pin 5 (MISO)     | <TBD marking> pin 5 (MISO)             |
    | J7 pin 6 (MOSI)     | <TBD marking> pin 3 (MOSI)             |

=== "VP66XX"

    Connect the J1 and J2 flash headers to the SPI header on RTE.

    | RTE SPI header      | J2 flash header                        |
    |:-------------------:|:--------------------------------------:|
    | J7 pin 1 (Vcc)      | pin 1 (Vcc)                            |
    | J7 pin 4 (SCLK)     | pin 3 (CLK)                            |
    | J7 pin 6 (MOSI)     | pin 4 (MOSI)                           |

    | RTE SPI header      | J1 flash header                        |
    |:-------------------:|:--------------------------------------:|
    | J7 pin 2 (GND)      | pin 4 (GND)                            |
    | J7 pin 3 (CS)       | pin 1 (CS)                             |
    | J7 pin 5 (MISO)     | pin 2 (MISO)                           |

### CMOS reset circuit

=== "VP2410"

    Connect the RTE J11 header to the platform JCMOS1 header using 2.54mm to 2mm
    wires as described in the table:

    | RTE       | Protectli                  |
    |:---------:|:--------------------------:|
    | J11 pin 8 | JCMOS1 pin 1 (CLR_CMOS)    |
    | Any GND   | JCMOS1 pin 2 (GND)         |

    Resetting CMOS is required for proper external flashing.

=== "VP2420"

    Connect the RTE J11 header to the platform JCMOS1 header using 2.54mm to 2mm
    wires as described in the table:

    | RTE       | Protectli                  |
    |:---------:|:--------------------------:|
    | J11 pin 8 | JCMOS1 pin 1 (CLR_CMOS)    |
    | Any GND   | JCMOS1 pin 2 (GND)         |

    Resetting CMOS is required for proper external flashing.

=== "VP46XX"

    Connect the RTE J11 header to the platform JCMOS1 header using 2.54mm to 2mm
    wires as described in the table:

    | RTE       | Protectli                  |
    |:---------:|:--------------------------:|
    | J11 pin 8 | JCMOS1 pin 2 (CLR_CMOS)    |
    | Any GND   | JCMOS1 pin 1 (GND)         |

    Resetting CMOS is required for proper external flashing.

=== "V1000 series"

    Connect the RTE J11 header to the platform CLR_CMOS1 header using 2.54mm to 2mm
    wires as described in the table:

    | RTE       | Protectli                  |
    |:---------:|:--------------------------:|
    | J11 pin 8 | CLR_CMOS1 pin 2 (CLR_CMOS) |
    | Any GND   | CLR_CMOS1 pin 3 (GND)      |

    Resetting CMOS is required for proper external flashing.

=== "VP66XX"

    Connect the RTE J11 header to the platform JCMOS1 header using 2.54mm to 2mm
    wires as described in the table:

    | RTE       | Protectli                  |
    |:---------:|:--------------------------:|
    | J11 pin 8 | JCMOS1 pin 2 (CLR_CMOS)    |
    | Any GND   | JCMOS1 pin 1 (GND)         |

    Resetting CMOS is required for proper external flashing.

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

=== "VP2410"

    Power supply controlling is performed with the relay module on RTE
    connected to one of RTE GPIOs. Power operation should be performed using
    the `rte_ctrl` script implemented in `meta-rte` (OS image dedicated to the
    RTE platform).

    To toggle the power supply use the below command:

        ```bash
        rte_ctrl rel
        ```

=== "VP2420"

    Power supply controlling is performed with the relay module on RTE
    connected to one of RTE GPIOs. Power operation should be performed using
    the `rte_ctrl` script implemented in `meta-rte` (OS image dedicated to the
    RTE platform).

    To toggle the power supply use the below command:

        ```bash
        rte_ctrl rel
        ```

=== "VP46XX"

    Power supply controlling (in this case: controlling the state of Sonoff)
    should be performed based on the `sonoff.sh` script implemented in
    `meta-rte` (OS image dedicated to the RTE platform).

    > Note, that before using the above-mentioned script, it should be modified and
    `SONOFF_IP` parameter should be set in accordance with obtained Sonoff IP address.

    To perform basic power operations use the below-described commands:

    1. Turn on the power supply:

        ```bash
        osfv_cli sonoff --sonoff_ip <sonoff_ip_address> on
        ```

    2. Turn off the power supply:

        ```bash
        osfv_cli sonoff --sonoff_ip <sonoff_ip_address> off
        ```

=== "V1000 series"

    Power supply controlling is performed with the relay module on RTE
    connected to one of RTE GPIOs. Power operation should be performed using
    the `rte_ctrl` script implemented in `meta-rte` (OS image dedicated to the
    RTE platform).

    To toggle the power supply use the below command:

        ```bash
        rte_ctrl rel
        ```

=== "VP66XX"

    Power supply controlling (in this case: controlling the state of Sonoff)
    should be performed based on the `sonoff.sh` script implemented in
    `meta-rte` (OS image dedicated to the RTE platform).

    > Note, that before using the above-mentioned script, it should be modified and
    `SONOFF_IP` parameter should be set in accordance with obtained Sonoff IP address.

    To perform basic power operations use the below-described commands:

    1. Turn on the power supply:

        ```bash
        osfv_cli sonoff --sonoff_ip <sonoff_ip_address> on
        ```

    2. Turn off the power supply:

        ```bash
        osfv_cli sonoff --sonoff_ip <sonoff_ip_address> off
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

### CMOS clear

To clear the CMOS, turn off the power with Sonoff or relay and use the
following commands:

```bash
echo 1 > /sys/class/gpio/gpio412/value
sleep 10
echo 0 > /sys/class/gpio/gpio412/value
```

### USB devices

Since some issues with USB controllers may only happen on select USB ports,
it's important to plug in USB devices to all 4 USB ports of the board.
