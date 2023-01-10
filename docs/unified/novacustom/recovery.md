# Recovery

## Prerequisites

To proceed with the recovery procedure the backup with the vendor firmware or
vendor EC firmware will be necessary eg. `bios_backup.rom`, `ec_backup.rom`.

The backup file should be generated before making any changes in the device
flash chip according to documentation:

- [Firmware backup](initial-deployment.md#bios-installation)
- [EC firmware backup](initial-deployment.md#ec-firmware-installation)

> Restoring vendor BIOS requires restoring a compatible version of EC firmware.
  There is currently no way to do this internally.

## External flashing

### BIOS recovery

Follow the [Initial deployment](initial-deployment.md#initial-installation)
section to perform the external flash. When running the flashrom commands use a
backup file you've prepared previously, like `bios_backup.rom`.

### EC firmware recovery

The procedure will be slightly different depending on the model of your laptop.

=== "NS5x / NS7x"
    You will need:

    - an Arduino Mega 2560
    - a 24-pin FFC cable with a 1.0mm pitch, same-sided (connectors on the same side
        on both ends of the cable)
    - a 24-pin FFC breakout board with a 1.0mm pitch FFC connector and a 2.54mm
         pitch pin header
    - USB-A to USB-B cable to connect the Arduino to the host
    - USB-C cable for grounding

=== "NV4x"
    You will need:

    - an Arduino Mega 2560
    - a 24-pin FFC cable with a 0.5mm pitch, same-sided (connectors on the same side
      on both ends of the cable)
    - a 24-pin FFC breakout board with a 0.5mm pitch FFC connector and a 2.54mm
      pitch pin header
    - USB-A to USB-B cable to connect the Arduino to the host
    - USB-C cable for grounding

The full set for EC firmware recovery is available at our [online shop](https://3mdeb.com/shop/open-source-hardware/ec-flashing-kit/).

#### Preparation

- Clone the EC repository:

```bash
git clone https://github.com/Dasharo/ec.git
cd ec
```

- Install dependencies:

```bash
./scripts/deps.sh
```

- If `rustup` was installed as part of the previous step, run:

```bash
source $HOME/.cargo/env
```

- Connect the Arduino to the computer using a USB-A to USB-B cable

- Build and flash firmware for the Arduino, which will serve as the flasher:

```bash
make BOARD=arduino/mega2560
make BOARD=arduino/mega2560 flash
```

#### Flashing

- Unscrew the bottom cover from the laptop

=== "NS5x / NS7x"
    ![](/images/ns50mu_board_chips.jpg)

=== "NV4x"
    ![](/images/nv4x_board_chips.jpg)

- Disconnect the battery (1)

> All power must be removed from the laptop during flashing.

  ![](/images/nvc_ec_flash/ns5x_battery_unplugged.jpg)

- Reattach the bottom cover (without screwing it in) and flip the laptop over
- Using a prying tool like a credit card, pull up the keyboard from the laptop

> Start prying at the top of the keyboard. Be extra careful when removing the
> keyboard to avoid damaging the keyboard cable, which is extremely fragile

=== "NS5x / NS7x"
    ![](/images/nvc_ec_flash/ns5x_keyboard_connectors.jpg)

=== "NV4x"
    ![](/images/nvc_ec_flash/nv4x_keyboard_connectors.jpg)

- Disconnect the keyboard from the laptop

=== "NS5x / NS7x"
    ![](/images/nvc_ec_flash/ns5x_keyboard_removed.jpg)

=== "NV4x"
    ![](/images/nvc_ec_flash/nv4x_keyboard_removed.jpg)

- Connect the USB-C cable to the Thunderbolt port on the laptop and to the host
  computer. This will provide grounding
- Connect the FFC cable to the FFC breakout board

=== "NS5x / NS7x"
    ![](/images/nvc_ec_flash/ns5x_arduino_breakout.jpg)
    > Note: In the example above, the FFC connector on the breakout has the pins
    > on the **bottom** side of the connector and is located on the **same**
    > side as the pins connecting to the Arduino. If your breakout is different,
    > you may need an FFC cable with connectors on the **opposite** sides.

=== "NV4x"
    ![](/images/nvc_ec_flash/nv4x_arduino_breakout.jpg)
    > Note: In the example above, the FFC connector on the breakout has the pins
    > on the **upper** side of the connector and is located on the side
    > **opposite** of the pins connecting to the Arduino. If your breakout
    > is different, you may need an FFC cable with connectors on the
    > **opposite** sides.

- Insert the breakout into Arduino's digital pin header, pins 22-45, with the
  FFC connector facing outwards

  ![](/images/nvc_ec_flash/ns5x_arduino_breakout_attached.jpg)

- Connect the other end of the FFC cable to the keyboard connector on the
  laptop, taking care to align pin 1 of the FFC cable to pin 1 (leftmost) pin
  of the connector

=== "NS5x / NS7x"
    ![](/images/nvc_ec_flash/ns5x_arduino_connected.jpg)

=== "NV4x"
    ![](/images/nvc_ec_flash/nv4x_arduino_connected.jpg)

- Connect the Arduino to the host using the USB-A to USB-B cable
- Build the flashing utility:

```bash
cargo build --manifest-path ecflash/Cargo.toml --example isp --release
```

- Flash the firmware:

```bash
sudo ecflash/target/release/examples/isp [path to EC backup]
```

The output will contain:

```bash
Buffer size: 128
ID: 5570 VER: 2
```

If it contains other ID value or the connection times out, reattach the FFC
cable to the laptop and the breakout board. VER value may vary between models.

- Reassemble the laptop: disconnect the Arduino from the laptop, reattach the
  keyboard, disconnect the USB-C cable, reconnect the battery and screw in the
  bottom cover
