# Dasharo compatible with MinnowBoard Turbot - development

## Intro

This document gathers various notes and documentation useful for development of
Dasharo compatible with the MinnowBoard Turbot platform.

## Hardware connection

### Requirements

- [RTE](https://3mdeb.com/open-source-hardware/#rte)

- USB-UART converter

- DC Jack - DC Jack wire

### Serial

MinnowBoard exposes a pin header with debug UART on `J4`.

- Attach the pins on MinnowBoard to the USB-UART converter.

| USB-UART converter | Minnowboard Uart header (J4)|
|:------------------:|:-------------------------:  |
|    GND             | 1 (GND)                     |
|    TX              | 4 (RX)                      |
|    RX              | 5 (TX)                      |

### SPI

| RTE header J7 pin | Minnowboard header J1 pin       |
|:-----------------:|:-------------------------:      |
| 1 (NC)            | 3.3V connect from RTE J9 pin 1  |
| 2 (GND)           | 2 (GND)                         |
| 3 (CS)            | 3 (SPICS#) via 1.2 kOhm resistor|
| 4 (SCLK)          | 4 (SPICLK)                      |
| 5 (MISO)          | 5 (SPIDI)                       |
| 6 (MOSI)          | 6 (SPIDO)                       |
| 7 (NC)            | Not connected                   |
| 8 (NC)            | Not connected                   |

### Power supply

- Connect 5V power supply to RTE `J12` connector
- Connect RTE `J13` connector to MinnowBoard `J9` connector with a DC Jack - DC
  Jack wire

There are two ways to control the power supply.

- You can toggle power supply using the `rte_ctrl` located in `/usr/bin/`:

```bash
/usr/bin rte_ctrl rel
```

- You can control power supply by directly setting the state of GPIO 199. Turn
on power by setting it to `1` and turn it off by setting it to `0`:

```bash
echo 1 > /sys/class/gpio/gpio199/value
```

```bash
echo 0 > /sys/class/gpio/gpio199/value
```
