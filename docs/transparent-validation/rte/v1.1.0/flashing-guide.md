# Flashing guide

This document describes how to set up external flashing for the devices using
RTE.

## Prerequisites

* [Prepared RTE](../v1.1.0/quick-start-guide.md)

## Connection to SPI header

To prepare the stand for flashing follow the steps described below:

1. Open the platform cover.

2. Connect the 6-pin flash header to the SPI header on RTE.

```text
    SPI header 	6 pin header
    Vcc 	pin 1 (Vcc)
    GND 	pin 2 (GND)
    CS 	pin 4 (CS)
    SCLK 	pin 6 (CLK)
    MISO 	pin 5 (MISO)
    MOSI 	pin 3 (MOSI)
```

```text
            ______
        >  |      |
Vcc 3.3V  ----1  2----  GND
            |      |
    MOSI  ----3  4----  CS
            |      |
    MISO  ----5  6----  CLK
            |______|
```

## Platform-specific steps

To find more specific information, regarding recovery of a given platform,
navigate to a recovery section in the documentation for a specific platform:

1. [Supported hardware](https://docs.dasharo.com/variants/overview/)
2. Choose a vendor. For example, `Protectli`
3. Navigate to the `Recovery` section

For example:

* [Protectli recovery
  guide](https://docs.dasharo.com/unified/protectli/recovery/)
* [NovaCustom recovery
  guide](https://docs.dasharo.com/unified/novacustom/recovery/)

## Remote flashing

To remotely initiate flashing via RTE, use the `osfv_cli` tool.

Example flashing command:

`osfv_cli rte --rte_ip=<RTE_IP> flash write --rom <PATH_TO_ROM_FILE>`

More information about `osfv_cli`:

* [osfv-scripts repository](https://github.com/Dasharo/osfv-scripts/)

* [osfv_cli
  documentation](https://github.com/Dasharo/osfv-scripts/blob/main/osfv_cli/README.md)
