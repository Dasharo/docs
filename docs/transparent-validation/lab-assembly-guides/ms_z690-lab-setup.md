# MSI PRO Z690-A WIFI DDR4 Lab Setup

## Introduction

This document describes assembly of MSI PRO Z690-A DDR4 lab setup. At this
point fully assembled platform prepared using
[Presale Device Assembly](msi_z690.md) and RTE should be ready.
- [Device under test assembly](msi_z690.md)
- [RTE assembly](../rte/v1.1.0/getting-started.md#quick-start-guide)

## Requirements

| Part              | Model Name                                                 | Image                                    |
|:------------------|:----------------------------------------------------------:|:----------------------------------------:|
| Device Under Test | MSI PRO Z-690A DDR4 - [Assembled](msi_z690.md)             |![Motherboard](images/motherboard.jpg)    |
| RTE               | RTE - [Assembled](../rte/introduction.md#rte-introduction) |![RTE](images/rte_built.jpg)              |
| Sonoff            | Sonoff - [Assembled](???)                                  |![Sonoff](images/sonoff_disconnected.jpg) |
| cables            | standard female-female connection wire 2.56mm raster       |![cables](images/female_female_cables.jpg)|

[comment]: <> (TODO: Create external Sonoff docs)

## Assembly

1. Connect serial panel to RTE:

    **IMPORTANT:** Cable colors on photos change due to insufficient lenght
    (ORANGE -> GREEN). For full view see: [Complete Setup](#complete-setup)

    ![IMG](images/msi_z690_lab_serial_panel.jpg)
    ![IMG](images/msi_z690_lab_serial_RTE.jpg)

1. Weld cable to SPI chip and connect it to the RTE `CS` as shown below:

    ![IMG](images/msi_z690_lab_chip_weld.jpg)
    ![IMG](images/msi_z690_lab_SPI_RTE.jpg)

1. Connect cables for SPI power menagment and grounding:

    ![IMG](images/msi_z690_lab_chip_power_RTE.jpg)
    ![IMG](images/msi_z690_lab_chip_ground_RTE.jpg)
    ![IMG](images/msi_z690_lab_chip_power_connections.jpg)

1. Make rest of neccesary SPI connections:

    ![IMG](images/msi_z690_spi.jpeg)
    ![IMG](images/msi_z690_lab_SPI_RTE.jpg)
    ![IMG](images/msi_z690_lab_SPI_RTE_2.jpg)

1. Connect MSI PRO Z690 power source to Sonoff:

    ![IMG](images/sonoff_connected.jpg)

1. Connect RTE to power source using MicroUSB 5V/2A power supply.

### Complete Setup

When all steps are finished, final setup should look as below:

![Complete](images/msi_z690_lab_complete.jpg)

### Usefull links for RTE theory of operation

1. Power On/Off and reset the platform:

- [comment]: <> (TODO: create external power control docs)

1. Control the power supply:

- [comment]: <> (TODO: create external power control docs)

1. External flash the BIOS chip:

- [Flashing guide](../rte/v1.1.0/getting-started.md#flashing-guide)

1. Set the communication with the platform:

- [Serial port connection guide](../rte/v1.1.0/getting-started.md#serial-port-connection-guide)

[comment]: <> (TODO: Verify links after merge)
