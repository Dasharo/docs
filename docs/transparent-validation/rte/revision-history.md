# Revision history

## v1.1.1

* Footprint of Q5 adapted to the recommended footprint of
  [Si9435bdy](https://www.vishay.com/docs/72245/si9435bd.pdf)
* Refactored the USB data lines routes to have more equal length
* Changed board version to v1.1.1 on PCB and the schematics

## v1.1.0

* added `Open hardware` logo
* added `SW1` reset button
* added `D5` relay state LED indicator
* added `J16` 2x3pin UART OUTPUT SELECT header
* added `J18` 1x2pin UART1 header
* added 1.8V stabilizer
* populated SPI `Vcc` pin
* modified capacitors near MAX3232 SOIC
* reduced OC buffers GPIO header (J11) from 12 to 9 pin
* eliminated issue with J6 USB port (unreliable detection of USB devices)

## v1.0.0

* added RoHS logo
* added Crossed Wheelie Bin logo
* modified footprints of the pin headers

## v0.5.3

* enlarged added holes

## v0.5.2

* modified I2C GPIO expander outputs connections (now 4 of them are connected to
  the dedicated header)
* modified version number on board
* removed SPI header for APU recovery with output pin role information labels
* removed 7 and 8 pin of SPI header with GPIO expander connection

## v0.5.1

* added micro USB connector for power supply
* added 5 V power supply pins
* added SPI connector for APU SPI recovery
* added fiducials on the bottom layer
* added pins information labels
* modified relay control system elements placement
* modified SPI connector for APU paths placement
* modified project text descriptions
* removed 2 pin GPIO expander connector

## v0.5

* added 5 V power supply signal diode (red) + limiting current resistor
* added 3.3 V power supply signal diode (orange) + limiting current resistor
* relay NO/NC connection switched to the previous configuration
* switched `SPI1_MISO`with `SPI1_MOSI` output
* mirrored `RS232` socket pads
* removed I2C pull-up resistors

## v0.3.6

* relay NO/NC connection switched

## v0.3.5

* enlarged the hole diameter by 0.1 mm

## v0.3.4

* added 3mdeb logo and board name on PCB
* modified elements marks placing

## v0.3.3

* added SPI output IO pins connection with GPIO
* added PCB mechanical schematic
* added I2C INT pins connection
* added mounting holes
* added fiducials
* modified MOSFET transistor pinout numeration
* modified USB footprint from horizontal to vertical
* modified I2C GPIO expander with OC buffers connection

## v0.3.2

* added mounting holes
* modified relay pinout
* removed I2C to GND connection

## v0.3.1

* modified power supply from 5V to 3V3 for I2C bus `MCP23017`, and `MAX3232`
* removed capacitors connected to the I2C bus

## v0.3

* added I2C bus with output header
* added `MCP23017` I2C GPIO expander
* added second `SN74LS06` OC buffer
* added relay with required neighboring items
* added `MAX3232` RS232 electrical level changer
* added RS232 socket
* added GPIO output header for pins unused to OC buffer control
* modified some of input pins connection
* removed ARK joint for the relay module
* removed header for relay module control
