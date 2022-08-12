# EC firmware recovery

## Introduction

This document describes the process of flashing EC firmware externally, in case
it has been flashed using incompatible or broken firmware. This document is not
intented for most users, but for developers, testers and advanced users
experimenting with the EC firmware.

## Prereqisites

You will need:

- an Arduino Mega 2560
- a 24-pin FFC cable with a 1.0mm pitch, same-sided (connectors on the same side
  on both ends of the cable)
- a 24-pin FFC breakout board with a 1.0mm pitch FFC connector and a 2.54mm
  pitch pin header
- A set of male-to-female jumper wires to connect the breakout to the Arduino
- USB-A to USB-B cable to connect the Arduino to the host
- USB-C cable for grouding

<!--
  The instructions assume pre-flashed Arduino at this point, so as to not
  overcomplicate this instruction. Depending on wiring, the code (GPIO map) will
  need modification. We will be supplying the first preassembled kits anyway

  Arduino flashing instructions available at:
  https://github.com/Dasharo/ec/blob/master/doc/mega2560.md
-->

## Preparation

- Clone the EC repository:

```bash
git clone https://github.com/Dasharo/ec.git
```

- Install dependencies:

```bash
./scripts/deps.sh
```

- If `rustup` was installed as part of the previous step, run:

```bash
source $HOME/.cargo/env
```

- Build the firmware for your laptop:

<!--
  TBD: Device specific instructions, I guess we should add our own mainboards
  in a different folder in the repository? For now let's just do system76/darp7
-->

```bash
make BOARD=system76/darp7
```

The firmware should now be built.

## Assembly

- Unscrew the bottom cover from the laptop
- Disconnect the battery

> All power must be removed from the laptop during flashing.

- Reattach the bottom cover (without screwing it in) and flip the laptop over
- Using a prying tool like a credit card, remove the keyboard from the laptop
- Connect the USB-C cable to the Thunderbolt port on the laptop and to the host
  computer. This will provide grounding
- Connect the FFC cable to the Arduino
- Connect the other end of the FFC cable to the keyboard connector on the
  laptop, taking care to align pin 1 of the FFC cable to pin 1 (leftmost) pin
  of the connector
- Connect the USB-A to USB-B cable to the host
- Flash the firmware:

```bash
make BOARD=system76/darp7 flash_external
```
