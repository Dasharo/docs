# SD-Wire usgae:

## Evnironment preparation:

### Software
SD-MUX has dedicated software which is a simple tool meant to control
the hardware. Source code of the tool is published on
[tizen git](https://git.tizen.org/cgit/tools/testlab/sd-mux/) server. 
This is simple to use, command-line utility software written in C
and based on open-source libFTDI library.

Clone the repository:
```
git clone git://git.tizen.org/tools/testlab/sd-mux
```
Follow the instruction included in sd-mux/README:

```
Requirements:
  1. libftdi1 1.4 - development library
  2. popt - development library
  3. cmake - binary tool

Build:
 - enter into project directory
 - create 'build' directory
 - enter into "build" directory
 - run 'cmake ..'
 - run 'make'

Install:
 - enter into 'build' directory
 - run 'sudo make install' to install binary into '/usr/local/bin' (the default one) directory

Note:
If you want to install files into different directory then add argument to cmake command:
 cmake -DCMAKE_INSTALL_PREFIX=/usr ..
Then again run:
 make
 make install
 ```
 Now the environment is ready to configure and control the SD-Wire.

 ## First use:
 1. Run `dmesg -w` in the terminal
 2. Connect the SD-wire to your machine using micro-USB-->USB cabel.
 3. Dmesg output you should looks like this:

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
4. Check if SD-wire is configured:
```
sudo  sd-mux-ctrl --list
```
If output looks like below, it means that SD-Wire is configured, go to "Everyday use" section.
```
Number of FTDI devices found: 1
Dev: 0, Manufacturer: SRPOL, Serial: sd-wire_11, Description: sd-wire
```
If output looks like below, you have to configure SD-Wire:

```
Number of FTDI devices found: 0
```
Configure SD-Wire:

```
sudo sd-mux-ctrl --device-serial=DB007V7V --vendor=0x0403 --product=0x6015 --device-type=sd-wire --set-serial=sd-wire_11
```
where:

--device-serial=*SerialNumber* (from dmesg output)

--vendor=0x*idVendor* (from dmesg output)

--product=0x*idProduct* (from dmesg output)

--set-serial=*New serial device*

5. Check if SD-wire is properly configured:

```
pawelsutryk@Pawel:~/Projects/sd-mux$ sudo  sd-mux-ctrl --list
Number of FTDI devices found: 1
Dev: 0, Manufacturer: SRPOL, Serial: sd-wire_11, Description: sd-wire
```

## Everyday use:

Typical scenario is: 

1. Disconnect power supply from the DUT.
2. Disconnect micro SD card from the DUT.
3. Connect micro SD card to the TS (using card reader)
4. Flash the SD card.
5. Connect SD card to the DUT.
6. Connect power supply to the DUT.
7. Boot DUT from new image.

Using SD-Wire there is no need to disconnect SD card from DUT.

Scenario using SD-Wire:

1. Insert card to the SD-Wire and connect it to the DUT
2. Connect 

At the moment RTE does not support sd-mux-ctrl, so SD-Wire must be
controlled from configured TS.


TS - Test server
DUT - Device under test


References:

https://wiki.tizen.org/SD_MUX
