# STM32 Nucleo L432KC I2C EC debugger

## Introduction

This document describes the process of configuring, connecting and using an
STM32 based Dasharo EC debugger.

## Prerequisites

To make use of this debugger, you will need:

- STM32 Nucleo L432KC board
- USB Type micro-B (to Type A or C) cable for connecting to host
- A DUT (Device Under Test) with the required debugging wires installed
- Some jumper wires
- minicom installed on the host system

To build the required Nucleo firmware, you'll also need to:

- [Follow Zephyr Getting Started](https://docs.zephyrproject.org/latest/develop/getting_started/installation_linux.html#installation-linux)
- [Install Zephyr SDK](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html#install-zephyr-sdk-on-linux)
- [Install West](https://docs.zephyrproject.org/latest/develop/west/install.html)

## Preparation

To build and flash the required Nucleo firmware:

1. Build the I2C to UART relay firmware:

    ```bash
    $ west init -m https://github.com/Dasharo/zephyr-i2c-to-uart.git --mr master
    $ west update
    $ west build --board nucleo_l432kc zephyr-i2c-to-uart/app/
    ```

1. Connect the Nucleo to your host system via USB

1. Flash the firmware to the board:

    ```bash
    $ west flash
    ```

## Connections

Make the following connections:

- Laptop SCL to Nucleo pin `D1/TX`
- Laptop SDA to Nucleo pin `D0/RX`
- Laptop ground to any of the `GND` pins on the Nucleo

## Test

Verify that the UART relay is working correctly:

- Enable `Serial Console Redirection` in the UEFI Setup menu on the DUT
- Connect the Nucleo to your host system
- Run the following command:

    ```bash
    $ minicom -D /dev/ttyACM0
    ```

You should see the UEFI console in your minicom window.

> Only input (capturing logs) is supported at this moment. Output (control of
> the DUT) is currently unimplemented.
