# Presale device assembly and validation

## Introduction

This document describes the assembly procedure of the PiKVM (device based on
Raspberry Pi 4 or Raspberry Pi Zero 2W) with components specified in
[requirements](#requirements).

## Requirements

> Note that the PiKVM build might be basing on two types of Raspberry Pi: RPi 4
    or RPi Zero 2W.

Hardware components necessary to build PiKVM on RPi Zero 2W:

* Raspberry Pi Zero 2W,
* microSD card 16 GB,
* USB-A 5 V 3.1 A charger (female socket),
* HDMI to CSI-2 bridge,
* Raspberry Pi Zero Camera Cable,
* HDMI-HDMI cable,
* USB A - micro USB cable (male, male),
* Y-splitter cable.
* (Optional) UART -> USB converter

Hardware components necessary to build PiKVM on RPi 4:

* Raspberry Pi 4,
* microSD card 16 GB,
* USB-A 5 V 3.1 A charger (female socket),
* HDMI to CSI-2 bridge,
* HDMI-HDMI cable,
* USB A - USB C cable,
* Y-splitter cable.
* (Optional) UART -> USB converter

## Device assembly

The following section of the documentation shows the assembly procedure for
PiKVM including setting up a WiFi connection and methods for reading device IP.

### Set based on RPi Zero 2W preparation

The section below describes the method of preparing PiKVM hardware based on
RPI Zero 2W.

1. Connect SD card and HDMI to CSI-2 bridge with camera cable:

    ![Connections](images/camera_cable_setup.jpg)

1. Block USB power from device under test by preparing USB cable:

    ![USB](images/usb_cable.jpg)

1. Connect HDMI cable from the device under test to HDMI -> CSI-2 bridge.
1. Connect the USB splitter to the Raspberry Pi micro USB port.
1. Connect one side of the splitter to USB-A 5 V 3.1 A charger.
1. Connect other side to device under test via USB cable with blocked power.

### Set based on RPi 4 preparation

To build PiKVM on RPi 4, use the
[RPI 0 set documentation](#set-based-on-rpi-zero-2w) and replace the cable for
connecting to the RPi and the cable for connecting with the CSI-2 bridge.

### OS image building and flashing

1. Prepare the OS in accordance with the
[PiKVM Handbook](https://docs.pikvm.org/building_os/).

1. Flash the SD card using `bmaptool` or `balenaEtcher`.
    - to do this by `balenaEtcher` go to the [producer site](https://www.balena.io/etcher/)
        and follow his procedure on how to download and flash an SD card.
    - to do this by `bmaptool` reproduce the following steps:
        + install `bmaptool` by opening the terminal and typing the following
            command:

            ```bash
            sudo apt install bmap-tools
            ```

        + create the bmap by typing the following command:

            ```bash
            bmaptool create /path/to/your/image > /path/where/you/want/bmap/file/saved/bmapfilename.bmap
            ```

        + flash image to the SD card by typing the following command:

            ```bash
            sudo bmaptool copy --bmap ~/path/where/your/bmap/file/is/located /path/where/your/image/is/located /path/to/memory/device
            ```

1. Insert the flashed SD card into the SD card slot on the PiKVM.

### Set up WiFi

The section below describes the method of setting up a WiFi connection for the
PiKVM. This section is dedicated especially to the PiKVMs based on RPi Zero 2W,
which is not equipped with an Ethernet port.

1. Mount the first partition of the memory card.

1. Edit or make the `pikvm.txt` file in the following convention:

    ```bash
    FIRSTBOOT=1
    WIFI_ESSID="name"
    WIFI_PASSWD="password"
    ```

    > Note: Do not remove line `FIRSTBOOT=1` or `FIRST_BOOT-1` line. It may
        occur with troubles with the device starts.

1. Unmount the first partition of the memory card.

> Note: In some countries, in which WiFi channel 13 is in use, the device
    might not connect to the WiFi. To prevent this, the router should be
    configured properly: channels 12-14 or Auto Scan mode should be disabled.

### Alternative method of setting up WiFi

The  section below describes how to configure wireless network connection if
the method mentioned above does not bring expected results.

1. Make the filesystem read - write by executing following command:

    ```bash
    rw
    ```

1. Run following command to check if wireless device is up:

    ```bash
    ip link show wlan0
    ```

    Example output:

    ```bash
    3: wlan0: (BROADCAST,MULTICAST) mtu 1500 qdisc noop state DOWN mode DEFAULT qlen 1000
    link/ether 74:e5:43:a1:ce:65 brd ff:ff:ff:ff:ff:ff
    ```

    Look for the word "UP" inside the brackets in the first line of the output. 

1. In the above example, wlan0 is not UP. Execute the following command to bring it up:

    ```bash
    ip link set wlan0 up
    ```

1. Scan to find out what WiFi network(s) are detected:

    ```bash
    /sbin/iw wlan0 scan
    ```

    The command will output all avaliable wireless networks. Example output:

    ```bash
    BSS 60:38:e0:d6:46:99(on wlp0s20f3) -- associated
	last seen: 1588.726s [boottime]
	TSF: 2351559493374 usec (27d, 05:12:39)
	freq: 2417
	beacon interval: 100 TUs
	capability: ESS Privacy ShortPreamble ShortSlotTime (0x0431)
	signal: -77.00 dBm
	last seen: 10532 ms ago
	Information elements from Probe Response frame:
	SSID: test_network
	Supported rates: 1.0* 2.0* 5.5* 11.0* 22.0 6.0 9.0 12.0 
	DS Parameter set: channel 2
	ERP: <no flags>
	Extended supported rates: 18.0 24.0 36.0 48.0 54.0
    ...
    ```

1. Generate a configuration file for wpa_supplicant that contains the
    pre-shared key ("passphrase") for the WiFi network. Above network is going
    to be used as an example. Run following command:

    ```bash
    wpa_passphrase test_network >> /etc/wpa_supplicant.conf
    ```

    After executing the command above, type in the password for the network.

1. Check the wpa_supplicant configuration file using following command:

    ```bash
    cat /etc/wpa_supplicant/wpa_supplicant.conf
    ```

    Example output:

    ```bash
    # reading passphrase from stdin
    network={
	ssid="test_network"
	#psk="testtest"
	psk=4dfe1c985520d26a13e932bf0acb1d4580461dd854ed79ad1a88ec221a802061
    }
    ```

1. Run wpa_supplicant with the new configuration file using following command:

    ```bash
    wpa_supplicant -B -D wext -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf
    ```

1. You should now be connected to the desired network. To verify this, run
    following command:

    ```bash
    /sbin/iw wlan0 link
    ```

    Example output:

    ```bash
    Connected to 00:14:d1:9c:1f:c8 (on wlan0)
	SSID: test_network
	freq: 2412
	RX: 63825 bytes (471 packets)
	TX: 1344 bytes (12 packets)
	signal: -27 dBm
	tx bitrate: 6.5 MBit/s MCS 0
	bss flags:	short-slot-time
	dtim period:	0
	beacon int:	100
    ```

1. Obtain IP address by DHCP by executing following command:

    ```bash
    dhclient wlan0
    ```

1. Verify the IP address obtained by DHCP by running following command:

    ```bash
    ip addr show wlan0
    ```

    Example output:

    ```bash
    3: wlan0:  mtu 1500 qdisc mq state UP qlen 1000
    link/ether 74:e5:43:a1:ce:65 brd ff:ff:ff:ff:ff:ff
    inet 192.168.4.113/24 brd 192.168.1.255 scope global wlan0
    inet6 fe80::76e5:43ff:fea1:ce65/64 scope link 
       valid_lft forever preferred_lft forever
    ```

1. Make the filesystem read - only by executing following command:

    ```bash
    ro
    ```


### Read IP address

The section below describes the known methods of reading PiKVM IP.

1. First option: from `os` repository run the following command:

    ```bash
    make scan
    ```

    Example output:

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

1. Second option: open the web interface of your router and find the list of
    issued IP addresses. Localization of the mentioned list depends on the
    router model.

1. Third option:
    - solder pins for serial output as on images below:

        ![Pins](images/soldered_pins.jpg)
        ![Schematics](images/pin_schem.jpg)

    - Check Raspberry Pi Zero2W IP by booting to system and reading
        information via serial (eg.) UART -> USB converter.

## Device validation

1. Connect the device to the mains.
1. Login to RTE via `ssh` (by using earlier obtained IP address) or
    `minicom` (by using USB-UART converter with 3 wire cables).

## Where to buy?

The PiKVM is available in our [online shop](https://3mdeb.com/shop/open-source-hardware/pikvm/).