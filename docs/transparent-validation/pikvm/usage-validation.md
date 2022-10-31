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
* (Optional) UART -> USB converter

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
    BOARD = zero2w

    PLATFORM = v2-hdmi

    HOSTNAME = pikvm

    LOCALE = en_US

    TIMEZONE = Europe/Warsaw

    ROOT_PASSWD = root

    WEBUI_ADMIN_PASSWD = admin

    IPMI_ADMIN_PASSWD = admin

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

1. If you want to connect PiKVM to a Wi-Fi network, you need to tell the device
    ESSID and password before first boot. To do this, mount the first partition
    of the memory card (FAT32) and edit or make the `pikvm.txt` file there. Do
    not remove line `FIRSTBOOT=1` or `FIRST_BOOT-1` for first time booting, just
    add your wifi settings like this:

    ```bash
    FIRSTBOOT=1
    WIFI_ESSID="name"
    WIFI_PASSWD="password"
    ```

    There is a possibility that, in countries that support CH13, the device will
    not connect. You will need to configure your router to disable channels
    12-14 or disable Auto scan mode so it will connect.

### Completing Setup

1. Connect SD card and HDMI to CSI-2 bridge with camera cable:

    ![Connections](images/camera_cable_setup.jpg)

1. Read IP:

    - First option:
        + From `os` repository run:

            ```bash
            make scan
            ```

        + Example output:

            ```bash
            .
            .
            .
            ===== Toolbox image is ready =====
            ===== Searching for Pis in the local network =====
            docker run \
            		--rm \
            		--tty \
            		--net host \
            	pi-builder-arm-toolbox arp-scan --localnet | grep -Pi "\s(b8:27:eb:|dc:a6:32:)" || true
            192.168.4.13	dc:a6:32:aa:aa:aa	Raspberry Pi Trading Ltd
            ```

    - Second option:
        + Open the web interface of your router and find the list of issued IP
            addresses there. It depends on the router model.

    - Third option:
        + Solder pins for serial output as on images below:

            ![Pins](images/soldered_pins.jpg)
            ![Schematics](images/pin_schem.jpg)

        + Check Raspberry Pi Zero2W IP by booting to system and reading
            information via serial (eg.) UART -> USB converter.

1. Block USB power from device under test by preparing USB cable:

    ![USB](images/usb_cable.jpg)

1. Connect HDMI cable from devie under test to HDMI -> CSI-2 bridge
1. Connect USB splitter to Raspberry Pi micro USB port.
1. One side of the splitter connect to USB-A 5 V 3.1 A charger.
1. Other side connect to device under test via USB cable with blocked power.
1. From browser connect to Raspberry Pi address eg. `192.168.4.13`.
1. Setup is now fully functional.
