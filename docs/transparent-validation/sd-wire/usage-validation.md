# SDWire usage

## Environment preparation

SDWire has dedicated software which is a simple tool meant to control the
hardware. Source code of the tool is published on [tizen git][tizen] server.
This is simple to use, command-line utility software written in C and based on
open-source libFTDI library.

To prepare the environment reproduce the following steps:

1. Clone the repository:

    ```bash
    git clone https://git.tizen.org/cgit/tools/testlab/sd-mux
    ```

1. Install all needed dependencies:

    Ubuntu/Debian:

    ```bash
    sudo apt-get install libftdi1-dev libpopt-dev cmake
    ```

    Fedora/Red Hat:

    ```bash
    sudo dnf install libftdi-devel popt-devel cmake gcc gcc-c++
    ```

1. Enter into sd-mux project directory and reproduce the following steps to
    build project:
    * open directory in terminal
    * create 'build' directory by the following command:

        ```bash
        mkdir build
        ```

    * enter into 'build' directory by the following command:

        ```bash
        cd build
        ```

    * run the following commands one by one:

        ```bash
        cmake ..
        make
        ```

1. In the above-described directory (`sd-mux/build`) run the following command to
    build binary:

    ```bash
    sudo make install
    ```

    Note, that the above-described command installs binary into '/usr/local/bin'.
    If you want to install files in directory rather than the default one add an
    argument to cmake command:

    ```bash
    cmake -DCMAKE_INSTALL_PREFIX=/usr ..
    ```

    Then it is obligatory to run again the following commands:

    ```bash
    make
    make install
    ```

## First use

> The following procedure should be performed not only before the first use of
the device, but also as the presale validation procedure!

Hardware requirements:

* SDWire
* SD card
* DUT (Device Under Test) bootable from SD card (for example: RPI, Orange PI
  etc.)
* DUT power supply
* Micro-USB --> USB cable
* TS (Test Server) - in most cases personal computer with prepared environment.

To perform first use (assuming Raspberry Pi platform as a DUT) procedure
reproduce the following steps:

1. Prepare environment in accordance with this
   [section](#environment-preparation).
2. Insert SD card to the SDWire.
3. Put SDWire into the DUT (Device Under Test).
4. Prepare a micro USB --> USB cable. It will be used to connect SDWire to TS
    (Test Server).
5. Check whether SDWire is configured by reproducing the following steps:
    * run in TS terminal the following command:

        ```bash
        dmesg -w
        ```

    * connect the SDWire to your machine using micro-USB --> USB cable.
    * after connecting your `dmesg` output should looks like this:

        ```bash
        (...)
        [73278.307591] usb-storage 3-1.1:1.0: USB Mass Storage device detected
        [73278.307823] scsi host6: usb-storage 3-1.1:1.0
        [73278.384925] usb 3-1.2: new full-speed USB device number 45 using xhci_hcd
        [73278.492025] usb 3-1.2: New USB device found, idVendor=0403, idProduct=6015, bcdDevice=10.00
        [73278.492027] usb 3-1.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
        [73278.492028] usb 3-1.2: Product: FT200X USB I2C
        [73278.492029] usb 3-1.2: Manufacturer: FTDI
        [73278.492030] usb 3-1.2: SerialNumber: DB007V7V
        (...)
        ```

    * open new terminal window and run the following command:

        ```bash
        sudo  sd-mux-ctrl --list
        ```

        If output looks like below, it means that SDWire is configured and ready
        to use. Now, you can go to point 6 in this section.

        ```bash
        Number of FTDI devices found: 1
        Dev: 0, Manufacturer: SRPOL, Serial: sd-wire_11, Description: sd-wire
        ```

        Otherwise, if output shows no devices (like in the example below):

        ```bash
        Number of FTDI devices found: 0
        ```

        you have to configure SDWire:

        ```bash
        sudo sd-mux-ctrl --device-serial=DB007V7V --vendor=0x0403 --product=0x6015 --device-type=sd-wire --set-serial=sd-wire_11
        ```

        where:

        ```bash
        --device-serial=<SerialNumber> (from dmesg output)

        --vendor=0x<idVendor> (from dmesg output)

        --product=0x<idProduct> (from dmesg output)

        --set-serial=<New serial device>
        ```

        After above-desribed procedure check again if SDWire is properly
        configured:

        ```bash
        sudo  sd-mux-ctrl --list
        ```

        Should output:

        ```bash
        Number of FTDI devices found: 1
        Dev: 0, Manufacturer: SRPOL, Serial: sd-wire_11, Description: sd-wire
        ```

6. Connect SD card to the TS (Test Server):

    ```bash
    sudo sd-mux-ctrl --device-serial=sd-wire_11 --ts
    ```

7. Flash the SD card using `bmaptool` or balenaEtcher.
    * download the OS image for the target DUT - [link for RPi image][rpios]
    * to do this by `balenaEtcher` go to the [producer site][balena]
    and follow his procedure how to download and flash SD card
    * to do this by `bmaptool` reproduce the following steps:
        - install bmaptool by opening terminal and typing the following command:

            ```bash
            sudo apt install bmap-tools
            ```

        - create the bmap by typing the following command:

            ```bash
            bmaptool create /path/to/your/image > /path/where/you/want/bmap/file/saved/bmapfilename.bmap
            ```

        - flash image to the SD card by typing the following command:

            ```bash
            sudo bmaptool copy --bmap ~/path/where/your/bmap/file/is/located /path/where/your/image/is/located /path/to/memory/device
            ```

8. Connect SD card to the DUT using `sd-mux-ctrl`:

    ```bash
    sudo sd-mux-ctrl --device-serial=sd-wire_11 --dut
    ```

9. Connect power supply to the DUT and check if it boots properly from newly
   burned image.

## Everyday use scenario

1. Disconnect power supply from the DUT (Device Under Test).
2. Disconnect micro SD card from the DUT.
3. Connect micro SD card to the TS (Test Server) using card reader.
4. Flash the SD card.
5. Connect SD card to the DUT.
6. Connect power supply to the DUT.
7. Boot DUT from new image.

Using SDWire there is no need to disconnect SD card from DUT.

## SDWire with RTE use scenario

1. Insert SD card to the SDWire.
2. Insert SDWire into the DUT and connect it to the TS with micro-USB --> USB
   cable.
3. Connect [RTE][shop1] power control connectors to the DUT (RTE here is
   optional but highly recommended for remote work, because it helps with
   automated and remote power control of the connected device).
4. Check serial no. of SDWire:

    ```bash
    sudo  sd-mux-ctrl --list
    ```

    Output:

    ```bash
    Number of FTDI devices found: 1
    Dev: 0, Manufacturer: SRPOL, Serial: sd-wire_11, Description: sd-wire
    ```

5. Disconnect power supply using RTE.
6. Connect SD card to the TS (using sd-mux-ctrl)

    ```bash
    sudo sd-mux-ctrl --device-serial=sd-wire_11 --ts
    ```

7. Flash the SD card using `bmaptool` or `balenaEtcher` as described in the
   [First use](#first-use) section
8. Connect SD card to the DUT (using sd-mux-ctrl)

    ```bash
    sudo sd-mux-ctrl --device-serial=sd-wire_11 --dut
    ```

9. Connect power supply using RTE.
10. DUT should boot from freshly burned SD card.

    > Command `sudo sd-mux-ctrl --device-serial=sd-wire_11 --status` returns
    information if SDWire is connected to DUT or TS.

    ```bash
    ➜  ~ sudo sd-mux-ctrl --device-serial=sd-wire_11 --status
    SD connected to: TS
    ```

    At the moment RTE does not support sd-mux-ctrl, so SDWire must be controlled
    from configured TS (Test Server).

---

References & Projects:

* [https://wiki.tizen.org/SDWire](https://wiki.tizen.org/SDWire)
* [Ethernet camera module build – Automated flashing](https://www.kurokesu.com/main/2022/08/02/ethernet-camera-module-build-log-5-automated-flashing/)
* [SD Wire & 3d Printer Usage](https://github.com/arekm/OctoPrint-Sdwire)
* [sd-mux-ctrl in Debian](https://perezmeyer.com.ar/blog/2023/09/28/sd-mux-ctrl_in_debian/)
by Lisandro Damián Nicanor Pérez Meyer

[tizen]: https://git.tizen.org/cgit/tools/testlab/sd-mux/
[shop1]: https://shop.3mdeb.com/shop/open-source-hardware/open-source-hardware-3mdeb/rte/
[balena]: https://www.balena.io/etcher/
[rpios]: https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2021-05-28/2021-05-07-raspios-buster-armhf.zip
