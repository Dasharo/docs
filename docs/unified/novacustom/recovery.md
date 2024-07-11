# Recovery

## Introduction

This document describes the recovery procedure of laptops flashed with bad
firmware (e.g. "bricked" devices), as well as external flashing in general,
which can sometimes be needed when switching between different firmware vendors.

This procedure can be used to restore both Dasharo and previous Insyde firmware.

## Prerequisites

!!! warning

    To proceed with the recovery procedure, the backup with the vendor firmware or
    vendor EC firmware will be necessary eg. `bios_backup.rom`, `ec_backup.rom`.

    The backup file should be generated before making any changes in the device
    flash chip according to the following documentation sections:

    - [Firmware backup](initial-deployment.md#bios-installation)
    - [EC firmware backup](initial-deployment.md#ec-firmware-installation)

> Restoring vendor BIOS requires restoring a compatible version of EC firmware.
  There is currently no way to do this internally.

### Necessary components

=== "BIOS"

    === "11th Gen models"
        You will need:

        - a CH341a programmer with 3.3V support
        - a SOIC-8 (Pomona) clip

    === "12th Gen models"
        You will need:

        - a CH341a programmer with 3.3V support
        - a WSON-8 probe

    === "14th Gen models"
        You will need:

        - a CH341a programmer with 1.8V support
        - a WSON-8 probe

    A complete set containing everything you need is available from
    [our shop](https://shop.3mdeb.com/shop/modules/ch341a-flash-bios-usb-programmer-kit-soic8-sop8/).

    Follow the [Initial deployment](initial-deployment.md#initial-installation)
    section to perform the external flash. When running the flashrom commands, use a
    backup file you've prepared previously, like `bios_backup.rom`.

=== "EC"

    === "NS5x / NS7x"
        You will need:

        - an Arduino Mega 2560
        - a 24-pin FFC cable with a 1.0mm pitch, same-sided (connectors on the same side
            on both ends of the cable)
        - a 24-pin FFC breakout board with a 1.0mm pitch FFC connector and a 2.54mm
             pitch pin header
        - USB-A to USB-B cable to connect the Arduino to the host
        - USB-C cable for grounding with power blocker

    === "NV4x"
        You will need:

        - an Arduino Mega 2560
        - a 24-pin FFC cable with a 0.5mm pitch, same-sided (connectors on the same side
          on both ends of the cable)
        - a 24-pin FFC breakout board with a 0.5mm pitch FFC connector and a 2.54mm
          pitch pin header
        - USB-A to USB-B cable to connect the Arduino to the host
        - USB-C cable for grounding with power blocker

    === "V540"
        You will need:

        - an Arduino Mega 2560
        - a 24-pin FFC cable with a 0.5mm pitch, same-sided (connectors on the same side
          on both ends of the cable)
        - a 24-pin FFC breakout board with a 0.5mm pitch FFC connector and a 2.54mm
          pitch pin header
        - USB-A to USB-B cable to connect the Arduino to the host
        - USB-C cable for grounding with power blocker

    === "V560"
        You will need:

        - an Arduino Mega 2560
        - a 24-pin FFC cable with a 1.0mm pitch, same-sided (connectors on the same side
          on both ends of the cable)
        - a 24-pin FFC breakout board with a 1.0mm pitch FFC connector and a 2.54mm
          pitch pin header
        - USB-A to USB-B cable to connect the Arduino to the host
        - USB-C cable for grounding with power blocker

    The full set for EC firmware recovery is available at our
    [online shop](https://shop.3mdeb.com/shop/open-source-hardware/ec-flashing-kit/).

## EC firmware recovery

The procedure will be slightly different depending on the model of your laptop.

!!! danger

    Ensure you choose the correct FFC cable, as they can be easily damaged.
    [Needed components](https://docs.dasharo.com/unified/novacustom/recovery/#ns5x--ns7x)

### Prerequisites

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

### Recovery steps

=== "everything else"

=== "V560"

    1. For the V560 laptops you will need to remove two stripes that are
       holding keyboard in place.

        ![](/images/v560tape1.webp)

    1. Second stripe is located under the heat sink.

        ![](/images/v560heatsink.webp)
        ![](/images/v560tape2.webp)

1. Remove the two screws holding the keyboard in place. They are indicated on the
   bottom cover with a keyboard symbol:

    ![](/images/ch341a_rec/ns5x_kbscrew.jpg)

1. Pry the keyboard away from the laptop. Use a plastic spudger to release the
   tabs holding it in place, starting from the top.

    !!! warning

        Be extra careful when removing the keyboard to avoid damaging the fragile
        keyboard cable!

1. Unplug the keyboard connector by lifting up the tab holding it in place:

    ![](/images/nvc_ec_flash/ns5x_keyboard_connectors.jpg)

1. Connect the FFC cable to the FFC breakout board

    ![](/images/nvc_ec_flash/ns5x_arduino_breakout.jpg)

    !!! warning

        In the example above, the FFC connector on the breakout has the pins on
        the **bottom** side of the connector and is located on the **same** side
        as the pins connecting to the Arduino. If your breakout is different,
        you may need an FFC cable with connectors on the **opposite** sides.

1. Insert the breakout into Arduino's digital pin header, pins 22-45, with the
   FFC connector facing outwards

    ![](/images/nvc_ec_flash/ns5x_arduino_breakout_attached.jpg)

1. Connect the other end of the FFC cable to the keyboard connector on the
   laptop, taking care to align pin 1 of the FFC cable to pin 1 (leftmost) pin
   of the connector

    ![](/images/nvc_ec_flash/ns5x_arduino_connected.jpg)

1. Connect the Arduino to the host using the USB-A to USB-B cable
1. Connect the USB-C cable together with power blocker from your host
   computer to the laptop.

    !!! warning

        This extra cable is for grounding. It's required, because there is no
        ground signal on the keyboard connector. If you are not using using
        [Power Blocker](https://shop.3mdeb.com/shop/adapters/usb-power-blocker/)
        Ensure the power pin on the cable is taped over to
        prevent the Embedded Controller chip from getting powered.

1. Build the flashing utility:

    ```bash
    cargo build --manifest-path ecflash/Cargo.toml --example isp --release
    ```

1. Flash the firmware:

    ```bash
    sudo ecflash/target/release/examples/isp [path to EC backup]
    ```

    The output will contain:

    ```bash
    Buffer size: 128
    ID: 5570 VER: 2
    ```

    If it contains other ID value or the connection times out, check all
    connections, using the photos above for reference.

1. Reassemble the laptop: disconnect the Arduino from the laptop, disconnect the
   USB-C grounding cable, reinstall the keyboard, reinstall keyboard screws.

## BIOS Flashing

Components Necessary to perform BIOS Recovery:
[Needed components](https://docs.dasharo.com/unified/novacustom/recovery/#ns5x--ns7x)

### Prerequisites

- Flashrom installed on a Linux host
- BIOS image file to flash

### Flashing

=== "11th Gen"

    1. Attach the SOIC-8 Pomona clip to the programmer. Take care to align CS pin
       with pin 1 on the programmer:

        ![](/images/ch341a_rec/ch341a_v17_with_breakout.webp)

        !!! danger

            If your CH341a programmer has a voltage switch, make sure it's at 3.3V.
            Improper voltage selection may result in hardware damage.

    ![](/images/CH341A-V2)

    1. Plug the programmer into your host computer.

    1. Remove bottom cover from the laptop.

        === "NS5x/7x 11th Gen"
            ![](/images/ns50mu_board_chips.jpg)

        === "NV4x 11th Gen"
            ![](/images/NV411th1.webp)

    1. Unplug the battery (1)

    1. Place the SOIC-8 Pomona clip on the BIOS chip, taking care to align the CS pin with the
       white dot on the BIOS chip:

        === "NS5x/7x 11th Gen"
            ![](/images/NS50x/BIOS-NS5x-11th.jpg)
            ![](/images/NS50x/SOIC-8-Pomona-Clip-NS5x-BIOS-11th.jpg)

        === "NV4x 11th Gen"

            ![](/images/NV411th2.webp)
            ![](/images/NV411th21.webp)

    1. Attach the SOIC-8 Pomona clip firmly in place and execute the following command
       on your host computer:

        ```bash
        sudo flashrom -p ch341a_spi -w path/to/firmware.bin
        ```

    1. Power on the laptop to verify the recovery passed. First boot may take a
       while, so be patient.

=== "12th Gen"

    1. Attach the WSON probe to the programmer. Take care to align pin 1 indicated
       on the probe's breakout board with pin 1 on the programmer:

        ![](/images/ch341a_rec/ch341a_v17_with_breakout.webp)

        !!! danger

            If your CH341a programmer has a voltage switch, make sure it's at 3.3V.
            Improper voltage selection may result in hardware damage.

        ![](/images/CH341A-V2)

    1. Plug the programmer into your host computer.

    1. Remove bottom cover from the laptop.

    === "NS5x/7x 12th Gen"

        ![](/images/ns5x_7x_adl_without_bottom_cover.webp)

    === "NV4x 12th Gen"

        ![](/images/NV412th1.webp)

    1. Unplug the battery (1)

    1. Place the WSON probe on the BIOS chip, taking care to align the dot on the
       WSON probe with the white dot on the BIOS chip:

    === "NS5x/7x 12th Gen"

        ![](/images/ch341a_rec/wson_probe_alignment.jpg)
        ![](/images/ch341a_rec/wson_probe_onchip.jpg)

    === "NV4x 12th Gen"

        ![](/images/NV412th2.webp)
        ![](/images/NV412th21.webp)

    1. Hold down the WSON probe firmly in place and execute the following command
       on your host computer:

        ```bash
        sudo flashrom -p ch341a_spi -w path/to/firmware.bin
        ```

    1. Power on the laptop to verify the recovery passed. First boot may take a
       while, so be patient.

=== "14th Gen"

    1. Attach the WSON probe to the programmer. Take care to align pin 1 indicated
       on the probe's breakout board with pin 1 on the programmer:

        ![](/images/ch341a_rec/ch341a_v17_with_breakout.webp)

        !!! danger

            If your CH341a programmer has a voltage switch, make sure it's at 1.8V.
            Improper voltage selection may result in hardware damage.

        ![](/images/CH341A-V.webp)

    1. Plug the programmer into your host computer.

    1. Remove bottom cover from the laptop.

    === "V540TND 14th Gen"

        ![](/images/540TND.webp)

    === "V540TU 14th Gen"

        ![](/images/540TU.webp)

    === "V560TND 14th Gen"

        ![](/images/560TND.webp)

    === "V560TU 14th Gen"

        ![](/images/560TU.webp)

    === "V560TNE 14th Gen"

        ![](/images/560TNE.webp)

    1. Unplug the battery (1)

    1. Remove memory module from RAM1 slot. This will make it easier to place the
       WSON probe correctly.

    1. Place the WSON probe on the BIOS chip, taking care to align the dot on the
       WSON probe with the white dot on the BIOS chip:

    === "V540TND 14th Gen"

        ![](/images/540TNDwson1.webp)
        ![](/images/540TNDwson2.webp)

    === "V540TU 14th Gen"

        ![](/images/540TUwson1.webp)
        ![](/images/540TUwson2.webp)

    === "V560TND 14th Gen"

        ![](/images/560TNDwson1.webp)
        ![](/images/560TNDwson2.webp)

    === "V560TU 14th Gen"

        ![](/images/560TUwson1.webp)
        ![](/images/560TUwson2.webp)

    === "V560TNE 14th Gen"

        ![](/images/560TNEwson1.webp)
        ![](/images/560TNEwson2.webp)

    1. Hold down the WSON probe firmly in place and execute the following command
       on your host computer:

        ```bash
        sudo flashrom -p ch341a_spi --ifd -i fd -i me -i bios -w [backup.bin]

        ```

    1. Power on the laptop to verify the recovery passed. First boot may take a
       while, so be patient.
