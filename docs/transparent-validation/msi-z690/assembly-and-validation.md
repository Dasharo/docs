# Presale device assembly and validation

## Introduction

This document describes the assembly procedure of the MSI PRO Z690-A DDR4 with
specified components in [requirements](#requirements).

## Requirements

| Part         | Model Name                                                      | Image                                   |
|:-------------|:---------------------------------------------------------------:|:---------------------------------------:|
| Motherboard  | MSI PRO Z-690A DDR4                                             |![Motherboard](images/motherboard.jpg)   |
| CPU          | Intel Core i5-12600K, 3.7G                                      |![CPU](images/cpu.jpg)                   |
| Cooling      | Noctua CPU NH-U12S Redux (w/ Noctua NM-i17xx-MP78 Mounting Kit) |![Cooler](images/cpu-cooler.jpg)         |
| RAM          | Kingston Fury Beast, DDR4, 4*8GB (32GB Total), 3600MHz, CL17    |![RAM](images/memory.jpg)                |
| Power Supply | Seasonic Focus PX 750W 80 Plus Platinum                         |![Power Supply](images/power-supply.jpg) |
| Storage      | SSD Intel 670p 512 GB M.2 2280 PCI-E x4 Gen3 NVMe               |![Storage](images/storage.jpg)           |
| Enclosure    | SilentiumPC Armis AR1                                           |![Enclosure](images/enclosure.jpg)       |

Additionally, you will need a regular Phillips screwdriver and thermal paste.
Remember that make all connections in the grounding strap.

## Device assembly

1. Unpack all equipment.
1. Place the motherboard in front of you, this is the component with which most
    of the operations will be performed. It's best to put something softer under
    the board so as not to damage it, e.g. during the installation of RAM
    modules.

    ![Motherboard](images/msi_z690_montage_motherboard.png)

1. To install the CPU on the motherboard first, open the CPU socket:

    ![Demontage CPU socket](images/msi_z690_montage_cpu_1.png)

1. Insert the processor carefully and tighten it with the dedicated mechanism:

    ![Install CPU](images/msi_z690_montage_cpu_2.png)

1. To install the CPU cooler, the parts shown in the picture below are
    necessary:

    ![Items](images/msi_z690_montage_coller_items.jpg)

1. Attach the black stand to the bottom of the motherboard, then apply and screw
    down the remaining parts except the cooler itself and apply thermal paste.
    After these steps, the CPU area should look like this:

    ![CPU Cooler](images/msi_z690_montage_thermal_paste.jpg)

1. Then attach the cooler from above by tightening the two screws. Most likely,
    for this operation, it is necessary to dismantle the fan and restore it
    after tightening the screws.

    ![CPU Cooler 2](images/msi_z690_montage_coller.jpg)

1. Install the memory module into the DIMM slots. To insert a single module,
    open the latch on both sides. Then insert the RAM and gently press the
    module downward at both ends of the module and the latch will close
    automatically. Always insert memory modules in the DIMMA2 slot first.

    ![Installed RAM](images/msi_z690_montage_ram.jpg)

1. Install the M.2 solid-state drive (SSD) into the M.2 slot. Remove the two
    screws from the cover and the one responsible for disk stabilization. Insert
    the SSD into the M.2 slot and tighten the previously removed screws.

    ![Install Storage](images/msi_z690_montage_storage.jpg)

1. Take the enclosure of the computer and open one side as shown in the picture
    below:

    ![Open enclosure](images/msi_z690_montage_enclosure.jpg)

1. Install the rear panel by inserting it from the inside of the enclosure
    and pressing it lightly.

    ![Rear panel](images/msi_z690_montage_rear_panel.jpg)

1. Insert the motherboard into the case but do not twist it, some pins are
    hard to connect when the motherboard is screwed. The photo below shows the
    slots that should be filled in the next steps.

    ![Slots](images/msi_z690_montage_slots.png)

1. Connect the cables from the front panel to the appropriately marked places:

    ![Front Panel](images/msi_z690_montage_front_panel.png)

    A detailed description of the connection cable marked `B` can be found in
    the [Board manual](https://download.msi.com/archive/mnu_exe/mb/PROZ690-AWIFIDDR4_PROZ690-ADDR4100x150.pdf)
    in section: JFP1, JFP2: Front Panel Connectors.

1. Connect the speaker to the slot marked before `E`:

    ![Speaker](images/msi_z690_montage_speaker.jpg)

1. Screw the motherboard to the enclosure.

1. Connect the power supply to the motherboard using the cables marked RE25 for
    connection to the `G` and `H` slots and the cable marked RJ21 to connect the
    `F` slots.

    ![Power Supply](images/msi_z690_montage_power_supply.png)

1. Connect the fan built into the enclosure to the indicated place:

    ![Fan](images/msi_z690_montage_fan.jpg)

1. Close the case of the computer.
1. Connect the computer to power.
1. Power on a device with the button on the front panel.
1. If all connections have been made correctly, the computer will start up and
    log Dasharo should appear after a while.
1. Boot to any system to check that everything is working properly.

## Useful content

* [Building manual](../../variants/msi_z690/building-manual.md) - how to
    build Dasharo compatible with the MSI PRO Z690-A DDR4
* [Installation manual](../../variants/msi_z690/installation-manual.md) - how
    to install Dasharo firmware on the MSI PRO Z690-A DDR4
* [Board manual](https://download.msi.com/archive/mnu_exe/mb/PROZ690-AWIFIDDR4_PROZ690-ADDR4100x150.pdf)
    -there you will find detailed information about the motherboard and its
    operations.
