# SDWire usage

## Environment preparation

SDWire has dedicated software which is a simple tool meant to control the
hardware. Source code of the tool is published on [tizen
git](https://git.tizen.org/cgit/tools/testlab/sd-mux/) server. This is simple to
use, command-line utility software written in C and based on open-source libFTDI
library.

To prepare the environment reproduce the following steps:

1. Clone the repository:
    ```
    git clone git://git.tizen.org/tools/testlab/sd-mux
    ```
2. Check whether the installation requirements for sd-mux are met:
    * libftdi1 1.4 development library is installed. To do this, open the 
       terminal and type the following command:
        ```
        dpkg -L libftdi1-dev
        ```
        If the library is installed, after typing the above command you will see 
        information about the paths to the library components. 
    * popt development library is installed. To do this, open the terminal and
       type the following command:
        ```
        dpkg -L libftdi1-dev
        ```
        If the library is installed, after typing the above command you will see 
        information about the paths to the library components. 
    * cmake binary tool is installed. To do this, open the terminal and type 
       the following command:
        ```
        cmake --version
        ```
        If the tool is installed, after typing the above command you will see 
        information about the installed on your computer cmake version. 
    
    If any above-mentioned requirements are not met - go to point 3. If they are
    met - go to point 4. 

3. Install missing libraries and/or tools:
    * libftdi1 1.4 development library. To do this, open the terminal and type 
       the following command: 
        ```
        sudo apt-get install libftdi1-dev
        ```
    * popt development library. To do this, open the terminal and type the
       following command: 
        ```
        sudo apt-get install libpopt-dev
        ```
    * cmake binary tool. To do this, open the terminal and type the following 
        command:  
        ```
        sudo apt-get install cmake
        ```

4. Enter into sd-mux project directory and reproduce the following steps to 
    build project:
    * open directory in terminal
    * create 'build' directory by the following command:
        ```
        mkdir build
        ```
    * enter into 'build' directory by the following command:
        ```
        cd build
        ```
    * run the following commands one by one:
        ```
        cmake ..
        make
        ```

5. In the above-described directory (`sd-mux/build`) run the following command to 
    build binary:
    ```
    sudo make install
    ```
    Note, that the above-described command installs binary into '/usr/local/bin'.
    If you want to install files in directory rather than the default one add an 
    argument to cmake command: 
    ```
    cmake -DCMAKE_INSTALL_PREFIX=/usr .. 
    ```
    Then it is obligatory to run again the following commands:
    ```
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

To perform first use procedure reproduce the following steps:

1. Prepare environment in accordance with this
   [section](#environment-preparation).
2. Insert SD card to the SDWire.
3. Put SDWire into the DUT (Device Under Test) and connect it to the TS with 
    the micro USB - USB cable.
4. Check whether SDWire is configured by reproducing the following steps:
    * run in terminal the following command:
        ```
        dmesg -w
        ```
    * connect the SDWire to your machine using micro-USB --> USB cable.
    * after connecting your `dmesg` output should looks like this:
        ```
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
        ```
        sudo  sd-mux-ctrl --list
        ```
        If output looks like below, it means that SDWire is configured and ready
        to use. Now, you can go to point 5 in this section.
        ```
        Number of FTDI devices found: 1
        Dev: 0, Manufacturer: SRPOL, Serial: sd-wire_11, Description: sd-wire
        ```
        Otherwise, if output shows no devices (like in the example below):
        ```
        Number of FTDI devices found: 0
        ```
        you have to configure SDWire:
        ```
        sudo sd-mux-ctrl --device-serial=DB007V7V --vendor=0x0403 --product=0x6015 --device-type=sd-wire --set-serial=sd-wire_11
        ```
        where:
        ```
        --device-serial=<SerialNumber> (from dmesg output)

        --vendor=0x<idVendor> (from dmesg output)

        --product=0x<idProduct> (from dmesg output)

        --set-serial=<New serial device>
        ```
        After above-desribed procedure check again if SDWire is properly 
        configured:
        ```
        sudo  sd-mux-ctrl --list
        ```
        Should output:
        ```
        Number of FTDI devices found: 1
        Dev: 0, Manufacturer: SRPOL, Serial: sd-wire_11, Description: sd-wire
        ```

5. Connect SD card to the TS (test server):
    ```
    sudo sd-mux-ctrl --device-serial=sd-wire_11 --ts
    ```
6. Flash the SD card using `bmaptool` or balenaEtcher.

7. Connect SD card to the DUT using `sd-mux-ctrl`:
    ```
    sudo sd-mux-ctrl --device-serial=sd-wire_11 --DUT
    ```
8. Connect power supply to the DUT and check if it boots properly from newly
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
    ```
    sudo  sd-mux-ctrl --list
    ```
    Output:
    ```
    Number of FTDI devices found: 1
    Dev: 0, Manufacturer: SRPOL, Serial: sd-wire_11, Description: sd-wire
    ```
5. Disconnect power supply using RTE.
6. Connect SD card to the TS (using sd-mux-ctrl)
    ```
    sudo sd-mux-ctrl --device-serial=sd-wire_11 --ts
    ```
7. Flash the SD card using `bmaptool` or balenaEtcher.
8. Connect SD card to the DUT (using sd-mux-ctrl)
    ```
    sudo sd-mux-ctrl --device-serial=sd-wire_11 --ts
    ```
9. Connect power supply using RTE.
10. DUT should boot from freshly burned SD card.

    > Command `sudo sd-mux-ctrl --device-serial=sd-wire_11 --status` returns
    information if SDWire is connected to DUT or TS.
    ```
    ➜  ~ sudo sd-mux-ctrl --device-serial=sd-wire_11 --status
    SD connected to: TS
    ```
    At the moment RTE does not support sd-mux-ctrl, so SDWire must be controlled
    from configured TS (host computer).

---

References:

* [https://wiki.tizen.org/SD_MUX](https://wiki.tizen.org/SD_MUX)
* [https://wiki.tizen.org/SD_MUX/manpage](https://wiki.tizen.org/SD_MUX/manpage)

[shop1]: https://3mdeb.com/shop/open-source-hardware/open-source-hardware-3mdeb/rte/