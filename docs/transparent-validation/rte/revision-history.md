# RTE Board changelog

This is a changelog for the
[RTE Board](https://3mdeb.com/open-source-hardware/#rte).

For the source/schematics, check out
[Repository](https://github.com/3mdeb/rte-schematics)

## v. 1.1.0

Added:

- 3.3V voltage stabilizer
- 1.8V voltage stabilizer
- A SPI logic level converter
- A Voltage selector based on a relay
- An Open Hardware logo
- An UART header selector
- A `MAX3232` enable jumper
- A relay state diode
- A circuit for cut-off the current flow
- A `.gitignore` file

Modified:

- OC header (from now on, there are only 9 open-collector pins free to use)
- Resistors and capacitors footprints

Removed:

- ARK joint for relay module
- Header for relay module control

## v. 1.0.0

Added:

- RoHS logo
- Crossed Wheelie Bin logo

Modified:

- footprints of the pin headers

## v. 0.5.3

Modified:

- enlarged added holes

## v. 0.5.2

Modified:

- I2C GPIO expander outputs connections (now 4 of them are connected to the
  dedicated header)
- version number on board

Removed:

- SPI header for APU recovery with output pin role information labels
- 7 and 8 pin of SPI header with GPIO expander connection

## v. 0.5.1

Added:

- microUSB connector for power supply
- 5 V power supply pins
- SPI connector for APU SPI recovery
- fiducials on bottom layer
- pins information labels

Modified:

- relay control system elements placement
- SPI connector for APU paths placement
- project text descriptions

Removed:

- 2 pin GPIO expander connector

## v. 0.5

Added:

- 5 V power supply signal diode (red) + limiting current resistor
- 3.3 V power supply signal diode (orange) + limiting current resistor

Modified:

- relay NO/NC connection switched to previous configuration
- switched `SPI1_MISO`with `SPI1_MOSI` output
- mirrored `RS232` socket pads

Removed:

- I2C pull-up resistors

## v. 0.3.6

Modified:

- relay NO/NC connection switched

## v. 0.3.5

Modified:

- enlarge the hole diameter by 0.1 mm

## v. 0.3.4

Added:

- 3mdeb logo and board name on PCB

Modified:

- elements marks placing

## v. 0.3.3

Added:

- SPI output IO pins connection with GPIO
- PCB mechanical schematic
- I2C INT pins connection
- mounting holes
- fiducials

Modified:

- mosfet transistor pinout numeration
- USB footprint from horizontal to vertical
- I2C GPIO expander with OC buffers connection

## v. 0.3.2

Added:

- mounting holes

Modified:

- relay pinout

Removed:

- I2C to GND connection

## v. 0.3.1

Modified:

- power supply from 5V to 3V3 for I2C bus `MCP23017`, and `MAX3232`

Removed:

- capacitors connected to I2C bus

## v. 0.3

Added:

- I2C bus with output header
- `MCP23017` I2C GPIO expander
- second `SN74LS06` OC buffer
- relay with required neighboring items
- `MAX3232` RS232 electrical level changer
- RS232 socket
- GPIO output header for pins unused to OC buffer control

Modified:

- Some of input pins connection
- footprints of the pin headers
