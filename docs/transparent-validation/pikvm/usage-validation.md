# PiKVM usage

## First use

> The following procedure should be performed not only before the first use of
the device, but also as the presale validation procedure!

### Hardware requirements

* Raspberry Pi Zero2W,
* microSD card 16 GB,
* USB-A 5 V 3.1 A charger (female socket),
* HDMI to CSI-2 bridge,
* Raspberry Pi Zero Camera Cable,
* HDMI-HDMI cable,
* USB A - micro USB cable (male, male),
* Y-splitter cable.

### Building the OS

To prevent any mix-up in libraries and dependencies process will include Docker.

1. Install and configure Docker:

    ```bash
    sudo apt-get install git make curl binutils -y
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    ```

    - Restart PC or relogin to apply changes.

1. Get OS repository:

    ```bash
    git clone --depth=1 https://github.com/pikvm/os
    cd os
    ```

1. Create `config.mk` file as follows:

    ```bash
    [user@localhost os]$ cat config.mk
    # rpi3 for Raspberry Pi 3; rpi2 for the version 2, zero2w for Zero2W
    BOARD = zero2w

    # Hardware configuration
    PLATFORM = v2-hdmi

    # Target hostname
    HOSTNAME = pikvm

    # ru_RU, etc. UTF-8 only
    LOCALE = en_US

    # See /usr/share/zoneinfo
    TIMEZONE = Europe/Warsaw

    # For SSH root user
    ROOT_PASSWD = root

    # Web UI credentials: user=admin, password=<this>
    WEBUI_ADMIN_PASSWD = admin

    # IPMI credentials: user=admin, password=<this>
    IPMI_ADMIN_PASSWD = admin

    # SD card device eg.: CARD = /dev/mmcblk0
    CARD = <SD_card_location>
    ```

1. Build the OS:

    ```bash
    make os
    ```

    - If any error occurs, see
    [original documentation](https://github.com/pikvm/pikvm/blob/master/docs/building_os.md).

1. Create the Image:

    ```bash
    make image
    ```

1. Install the image on the SD card using eg.
    [balenaEtcher](https://www.balena.io/etcher/).

- wifi

### Completing Setup

- welding
- sd card
- cables
- blocking usb power from pc
- wifi
- 