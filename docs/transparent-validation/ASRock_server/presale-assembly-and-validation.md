# Presale device assembly and validation

## Introduction

This document describes the assembly procedure of the ASRock SPC741D8 with
specified components in [requirements](#requirements).

## Requirements

| Part         | Model Name                                                      | Image                                   |
|:-------------|:---------------------------------------------------------------:|:---------------------------------------:|
| Motherboard  | ASRock SPC741D8                                                 |![Motherboard](images/motherboard.jpg)   |
| CPU          | Intel Xeon Silver 4410Y                                         |![CPU](images/cpu.jpg)                   |
| Cooling      |                                                                 |![Cooler](images/cpu-cooler.jpg)         |
| RAM          |                                                                 |![RAM](images/memory.jpg)                |
| Power Supply |                                                                 |![Power Supply](images/power-supply.jpg) |
| Storage      |                                                                 |![Storage](images/storage.jpg)           |
| Enclosure    |                                                                 |![Enclosure](images/enclosure.jpg)       |

Additionally, you will need a screwdriver with bits P2, P1, T30 and thermal paste.
Try not to tighten all the elements to the maximum, as it will make disassembly
difficult. Remember that make all connections in the grounding strap.

## Device assembly

### Full set assembly

Section below describes the procedure of complete assembling of the
working station.

1. Place the motherboard in front of you, this is the component with which most
   of the operations will be performed. It's best to put something softer under
   the board so as not to damage it, e.g. during the installation of RAM
   modules.

    ![Motherboard](images/)

1. In box with cooler find CPU bracket marked "".

    ![CPU bracket](images/)

1. Attach the bracket to CPU cooler as shown.

    ![Cooler Bracket](images/)

1. Put thermal Paste on the CPU and attach it to Cooler by
   lining triangles in the corner.

    ![Thermal Paste](images/)
    ![CPU Cooler](images/)

1. Take out the socket cover and very carefully insert the Cooler
   with attached CPU carefully making sure to line up triangles.

    ![Socket Cover](images/)
    ![Install CPU](images/)

1. Tighten CPU Cooler accordingly to numbering near the screws 1-4

    ![Cooler Screws](images/)

1. Connect CPU Fan to the header on the motherboard

    ![FAN Header](images/)

1. Install the memory modules into the DIMM slots. To insert a single module,
   open the latch on both sides. Then insert the RAM and gently press the
   module downward at both ends of the module and the latch will close
   automatically. Always insert memory modules in the XXX slot first.

    ![Installed RAM](images/)

1. Install the M.2 solid-state drive (SSD) into the M.2 slot
   and tighten the screws holding it.

    ![Install Storage](images/)

1. Open the chassis by removing 6 screws from the top panel.

    ![Open Chassis](images/)

1. Install the IO shield by inserting it from the inside of the enclosure
   and pressing it lightly.

    ![IO shield](images/)

1. Insert the motherboard into the case and place screws in marked spots.

    ![Screws Placement](images/)

1. Connect the cables from the front panel to the appropriately marked spots.

    ![Front Panel](images/)

1. Connect the speaker to the slot marked "".

    ![Speaker](images/)

1. Connect the power supply to the motherboard as shown.

    ![Power Supply](images/)

1. Connect the fan built into the enclosure to the indicated place
   using Fan extension cable.

    ![Fan](images/)

1. Bundle the cables so that they don't interfere with the fans or other
   components.

1. Close the case by screwing back all 6 screws.

### Motherboard assembly only

Section below describes the procedure of assembling the motherboard.

To prepare the motherboard the following operations should be performed:

## Device validation

1. Connect the device to the mains power.
1. Open the frontpanel using attached key.
1. Power on the device with the button located on the front panel.
1. If all connections have been made correctly, the device should start and
   the boot logo should be shown.
1. Install Dasharo firmware in accordance with
    ![Initial Deployment]() -
1. Power on the device.
1. Boot to Linux system (Ubuntu is recommended).
1. Open a terminal window and run the following command:

    ```bash
    sudo dmidecode -t 0 | grep Version
    ```

1. The output of the command above should be similar to:
    `Version: Dasharo (coreboot+UEFI) <version>` where the version should
    correspond to the version of the flashing binary used eg. v1.0.0.
1. Check in the system that everything is working properly.

## Useful content

* [Building manual][Build] - documentation contains information on how to
    build Dasharo compatible with ASRock SPC741D8
* [Board manual][Board] - documentation contains detailed information about
    the motherboard and its operations.
* [CPU Cooler Manual][Cooler] - documentation contains information on how to
    properly assamble CPU Cooler and mount CPU to it

[Build]:
[Board]:
[Cooler]:
