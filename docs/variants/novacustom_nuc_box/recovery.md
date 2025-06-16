# Recovery

## Intro

The following documentation describes the process of recovering the NovaCustom
NUC BOX-155H platform from a brick state using Dasharo open-source firmware and
one of two methods:

- **WSON8 chip flashing using a CH341A and socket adapter**
- **Remote/automated flashing via
    [qspimux](https://github.com/felixheld/qspimux) and
    [RTE](../../transparent-validation/rte/introduction.md)**

The default BIOS flash chip is a **WSON8 package**, mounted in a socket —
meaning **there are no exposed pins** for clip-on programmers. This makes
traditional flashing using Pomona clips impossible.

> ⚠️ Important: Repeated mechanical re-seating of the WSON8 chip may degrade
the socket or damage the chip. This method is **not suited for remote or
automated workflows**.

## External flashing

### CH341A with WSON8 socket adapter

This method involves manually extracting the BIOS chip and flashing it outside
the board using a CH341A programmer.

#### Prerequisites

- CH341A USB programmer
- WSON8 to SOIC8 socket adapter
- Known good firmware binary
- [flashrom](https://flashrom.org/) installed on host PC

#### Firmware flashing procedure

1. Power off the NUC BOX-155H and disconnect all power.
2. Carefully remove the WSON8 flash chip from the socket.
3. Insert it into the WSON8-to-SOIC8 adapter, ensuring correct orientation.
4. Plug the adapter into the CH341A programmer.
5. Connect the programmer to your PC.
6. Flash the firmware:

    ```bash
    flashrom -p ch341a_spi -w [path_to_binary]
    ```

7. Once completed, remove the chip from the adapter and reinsert it into the
  board’s socket.
8. Power on the platform.

> ⚠️ Note: This process is manual, not scalable, and fragile. It is **not
recommended for repetitive tasks** or automated CI setups.

---

### qspimux with RTE (recommended for automation)

The [qspimux](https://github.com/felixheld/qspimux) setup enables **remote
firmware flashing** without manually removing the flash chip. It supports SPI
muxing between the host board and an external flasher like the RTE.

> ⚠️ This method requires **hardware modifications**. The factory-mounted
WSON8 socket must be desoldered and replaced with a 9-pin qspimux header.
This involves **fine-pitch SMD soldering** and should only be done by
experienced individuals. Proceed at your own risk.

#### Benefits

- Fully automated flashing possible via
  [RTE](../../transparent-validation/rte/introduction.md)
- No physical chip handling after initial setup
- Safer and repeatable in lab/validation environments

#### Required mods

- Desolder the original WSON8 socket
- Solder a DIP-8 (or qspimux-compatible) header in its place
- Wire the RTE and qspimux per pinouts below

#### Prerequisites

- [RTE](https://3mdeb.com/open-source-hardware/#rte)
- qspimux board with WSON8 flash soldered onto SOIC8 adapter
- Proper GPIO lines connected for mux control
- `flashrom` installed on RTE

#### Pin Mapping (J7 to qspimux J101)

| RTE header J7 pin | qspimux J101 pin       |
|-------------------|------------------------|
| 1 (VCC)           | 2 (VCC_PROG)           |
| 2 (GND)           | 7 (GND)                |
| 3 (CS)            | 1 (CS_PROG#)           |
| 4 (SCLK)          | 6 (CLK_PROG)           |
| 5 (MISO)          | 8 (IO0_DI_PROG)        |
| 6 (MOSI)          | 3 (IO1_DO_PROG)        |

#### Extra GPIOs for qspimux control

| RTE header J10 pin | qspimux J101 pin      | Purpose                |
|--------------------|-----------------------|------------------------|
| 1 (GPIO400)        | 9 (MUX_SEL)           | Select board or programmer access |
| 2 (GPIO401)        | 4 (IO3_HOLD_PROG)     | Deassert HOLD#         |
| 3 (GPIO402)        | 5 (IO2_WP_PROG)       | Control #WP (write protect) |

#### Flashing procedure

1. Wire the RTE and qspimux according to tables above.
2. Tie `IO3_HOLD_PROG` high (3.3V) if not using GPIO401.
3. Set mux to programmer:

    ```bash
    echo "0" > /sys/class/gpio/gpio400/value  # MUX_SEL = 0 (external)
    echo "1" > /sys/class/gpio/gpio401/value  # HOLD# = high
    echo "1" > /sys/class/gpio/gpio402/value  # WP# = high (write enabled)
    ```

4. Flash the firmware:

    ```bash
    flashrom -p linux_spi:dev=/dev/spidev1.0,spispeed=16000 -w firmware.bin
    ```

5. Switch back to board:

    ```bash
    echo "1" > /sys/class/gpio/gpio400/value  # MUX_SEL = 1 (board)
    ```

6. Optionally, reassert write protection:

    ```bash
    echo "0" > /sys/class/gpio/gpio402/value
    ```

> ⚠️ First boot after flashing may take longer. Always confirm stable power
before flashing.

![](../../images/qspimux_pin_header.jpg)

More details and schematics:
[qspimux.pdf](https://github.com/felixheld/qspimux/blob/master/qspimux/qspimux.pdf).
