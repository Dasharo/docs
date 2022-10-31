# Initial Deployment

## Intro

This document is a guide for the initial installation of Dasharo on a supported
device. It assumes some knowledge about external flashing and is primarily aimed
at technicians performing initial installation and not for end users of the
devices.

## Installing Dasharo

### Initial Installation

=== "12th Gen (Alder Lake)"

    During the initial installation of Dasharo, you should deploy the supported
    Intel ME version (and configuration) on the device. Since vendor firmware
    has enabled Intel Boot Guard and BIOS Guard, it is not possible to do this
    from within the operating system and external flashing of the whole flash
    chip using a programmer like the CH341a or
    [3mdeb RTE](http://docs.dasharo.com/transparent-validation/rte/introduction/)
    is required.

    > Publicly released binaries do not contain ME binary. If you need an Intel ME
    > update for your device, contact us via already established commercial support
    > channel.

    ### Preparation

    Install flashrom:

    ```bash
    sudo apt -y install flashrom
    ```

    ### Installation

    Steps for initial Dasharo installation:

    1. Open the laptop.

        === "NS5x / NS7x"
            ![ns5x chips](../../images/ns50mu_board_chips.jpg)

        === "NV4x"
            ![nv4x chips](../../images/nv4x_board_chips.jpg)

    1. Disconnect the primary battery. (1)
    1. Disconnect the CMOS battery. (2)
    1. Attach a WSON-8 probe to the SPI flash chip. (3)
    1. Execute the following command, replacing [path] with the path to the firmware
        image you want to flash, e.g. `novacustom_ns5xpu_ns7xpu_full_v1.0.0.rom`

        ```bash
        flashrom -p ch341a_spi -w [path]
        ```

    1. Detach the WSON-8 probe.
    1. Connect the primary battery and reconnect the CMOS battery
    1. Power on the laptop. The laptop may shut down once after training the memory.

    ### Transition to open EC

    If you have deployed the Dasharo using external programmer, time to switch to
    Open EC. This step is required to support all Dasharo features. To install Open
    EC Firmware on NS5xPU/NS7xPU, follow this instruction:
    [Dasharo EC Transition](../../../common-coreboot-docs/dasharo_tools_suite/#dasharo-ec-transition).

    If this is your first experience with DTS, first read its
    [documentation](https://docs.dasharo.com/common-coreboot-docs/dasharo_tools_suite/).
    We recommend using DTS with the
    [Bootable over network](https://docs.dasharo.com/common-coreboot-docs/dasharo_tools_suite/#bootable-over-network)
    method which is less time-consuming and just easier than DTS on the USB Stick.

    Successful transition to Open EC finishes the initial deployment process.

=== "11th Gen (Tiger Lake)"

    The following instructions describe how to flash Dasharo, but if you are
    interested in version v1.3.0 or higher, which is only compatible with Open EC
    Firmware, follow this instruction:
    [Dasharo EC Transition](../../../common-coreboot-docs/dasharo_tools_suite/#dasharo-ec-transition).

    If this is your first experience with DTS, first read its
    [documentation](https://docs.dasharo.com/common-coreboot-docs/dasharo_tools_suite/).
    We recommend using DTS with the
    [Bootable over network](https://docs.dasharo.com/common-coreboot-docs/dasharo_tools_suite/#bootable-over-network)
    method which is less time-consuming and just easier than DTS on the USB Stick.

    ### Preparation

    Flashing coreboot can be done from Linux using flashrom with the internal
    programmer. This document describes the process of building, installing and
    running flashrom on Ubuntu 22.04.

    ### Build flashrom

    Currently, the latest flashrom release lacks support for internal flashing
    on recent Intel processors. Because of this, we need to build flashrom from
    source.

    1. Install build dependencies:

        ```bash
        apt install git build-essential debhelper pkg-config libpci-dev libusb-1.0-0-dev libftdi1-dev meson
        ```

    1. Obtain source code:

        ```bash
        git clone https://review.coreboot.org/flashrom.git
        cd flashrom
        ```

    1. Build flashrom:

        ```bash
        make
        sudo make install
        ```

    ### Reading flash contents

    To read from the flash and save them to a file (`dump.rom`), execute the
    following command:

    ```bash
    flashrom -p internal -r dump.rom
    ```

    ### Flashing Dasharo

    During the initial installation of Dasharo, you should deploy the supported
    Intel ME version (and configuration) on the device.

    > Publicly released binaries do not contain ME binary. If you need an Intel ME
    > update for your device, contact us via already established commercial support
    > channel.

    When flashing binaries with ME binary included, flashing of the whole chip is
    required.

    ```bash
    flashrom -p internal -w [path]
    ```
