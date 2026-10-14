# Presale device preparation and validation

## Introduction

This document describes the preparation (assembly, flashing and verification)
procedure of the Gigabyte MZ33-AR1 with specified components in
[requirements](#requirements).

## Requirements

| Part         | Model Name                                                      | Image                                                        |
|:-------------|:---------------------------------------------------------------:|:------------------------------------------------------------:|
| Motherboard  | Gigabyte MZ33-AR1                                               |![Motherboard](images/motherboard1.jpg)    |
| CPU          | AMD EPYC™ 9015                                                  |![CPU](images/cpu.jpg)                     |
| Cooling      | Arctic Freezer 4U-SP5                                           |![Cooler](images/cpu-cooler.jpg)           |
| RAM          | Kingston 16GB DDR5 ECC KSM48R40BS8KMM-16HMR                     |![RAM](images/memory.jpg)                  |
| Power Supply | Seasonic Vertex GX 850W 80 Plus Gold                            |![Power Supply](images/power-supply.jpg)   |
| Storage      | SSD Kingston KC3000 512 GB M.2 2280 NVMe                        |![Storage](images/storage.jpg)             |
| Enclosure    | SilverStone RM42-502 4U Rack Chassis                            |![Enclosure](images/enclosure.jpg)         |
| TPM          | GIGABYTE CTM012 TPM 2.0                                         |![TPM](images/tpm.png)                     |

You will need a screwdriver with bits P1, T20, and small pliers.
Remember to make all connections with the grounding strap.

## Device assembly

### Full set assembly

The section below describes the procedure for the complete assembly
of the working station.

1. Place the motherboard in front of you. This is the component with which
   most operations will be performed. It’s best to put something soft under
   the board to avoid damage during RAM installation and other steps.

    ![Motherboard](images/motherboard1.jpg)

1. (Optional)The unique BMC password can be found on the cpu dummy cover and
   the motherboard box. You might want to write it down. Default BMC login is
   `admin`.

1. Loosen the captive screw securing the CPU cover with a T20 screwdriver.

    ![CPU Cover](images/cpu_installation1.jpg)

1. Flip open the CPU cover.

    ![CPU Cover Lifted](images/cpu_installation2.jpg)

1. Flip open the CPU carrier using the two handles.

    ![CPU Carrier Handles](images/cpu_installation3.jpg)
    ![CPU Carrier Lifted](images/cpu_installation4.jpg)

1. Remove the CPU socket cover.

    ![CPU Carrier Handles](images/cpu_installation5.jpg)
    ![CPU Carrier Lifted](images/cpu_installation6.jpg)

1. Remove the CPU carrier cover.

    ![CPU Carrier Cover Removal](images/cpu_installation7.jpg)

1. Insert the CPU(already inside the blue frame) into the carrier. NOTE:
   Ensure the CPU is installed in the carrier in the correct orientation, with
   the triangle on the CPU(might be hidden under the blue frame) aligned to
   the top left corner of the carrier.

    ![CPU Being Inserted into CPU Carrier](images/cpu_installation8.jpg)

1. Flip the CPU carrier into place in the CPU socket

    ![CPU Carrier Flipped Into Place](images/cpu_installation9.jpg)

1. Flip the CPU cover into place and tighten the T20 screw holding it.

    ![CPU Cover Flipped Into Place](images/cpu_installation10.jpg)

1. CPU installation complete.

    ![CPU installation complete](images/cpu_installation11.jpg)

1. Install the memory modules into the DIMM slots.

    DIMM slots can be identified using this image.

    ![DRAM slots](images/dram_slots.png)

    To insert a single module, open the latches on both sides. Then insert the
    RAM and gently press downward until the latches close automatically.
    **NOTE: DDR5 STICKS HAVE A NOTCH THAT MUST LINE UP WITH THE RIDGE IN THE
    DIMM SLOT. INSTALLING THE STICK IN THE WRONG ORIENTATION WILL CAUSE
    PERMANENT DAMAGE.**

    Install memory according to the table. For example, if installing 1 stick
    place it in slot A1, if installing 4 sticks - in slots C1, A1, G1, I1.

    ![DRAM DIMM Table](images/dimm_table.png)

    ![Installed RAM](images/cpu_installation11.jpg)

1. Prepare the CPU cooler for installation on socket LGA 6096 SP5(installation
   kit should be found in the cooler set). Afterwards peel off the protective
   peel on the bottom of the cooler.

    ![CPU Cooler Peel Removal   ](images/cpu_cooler_installation1.jpg)

1. Apply thermal paste in an X pattern to the CPU.

    (image from different platform)
    ![CPU thermal paste](images/thermalpaste.jpg)

1. Gently place the cooler onto the CPU lining it up with the six screw holes.
   Tighten the six screws securing the cooler around halfway, then tighten the
   opposite corners fully. This is crucial for good contact between the CPU
   and the socket.

    ![CPU Cooler Placement](images/cpu_cooler_installation2.jpg)

1. Do not install the cooler fans yet as they would interfere with the
   motherboard mounting screws.

1. Using pliers, unscrew the SSD standoff and screw it back in one hole closer
   to the M.2 slot. Install the M.2 solid-state drive (SSD) into the M.2 slot
   and tighten the screw holding it. (You may need an additional M3 screw for
   that)

    ![M2 standoff](images/m2_installation1.jpg)
    ![M2 standoff closer](images/m2_installation2.jpg)
    ![M2 drive inserted](images/m2_installation3.jpg)

1. Install the M.2 heatsink(if provided). Thermal pad should be applied to the
   underside of the heatsink. Make sure the protective tape is removed from
   the thermal pad. Apply the heatsink on top of the M.2 drive and secure both
   the M.2 drive and the heatsink using the M3 screw.

    ![M2 heatsink](images/m2_installation5.jpg)

1. If installing M.2 drive without a heatsink, simply secure the drive using
   the M3 screw.

    ![M2 noheatsink](images/m2_installation4.jpg)

1. (Optional)Install the TPM module in the slot marked "SPI_TPM". Pay
   attention to the no-pin placement.

    ![TPM installation](images/spi_ctm012_installation.jpg)

1. Open the chassis by removing four screws from both sides of the top panel
   and remove the metal PCIe cards holder by unscrewing four screws on the
   left and right sides (not the top).

    ![Open Chassis](images/chassis-screws.jpg)
    ![Remove PCIe holder](images/PCIe-holder.jpg)

1. Install the IO shield by inserting it from inside the enclosure and
   pressing it lightly.

    ![IO shield](images/IO_installation1.jpg)

1. Prepare the screws and standoffs set for the motherboard installation.
   Install the standoffs in all the correct spots, as shown in the picture.

    ![Motherboard screws set](images/motherboard_installation1.jpg)
    ![Motherboard standoffs installation](images/motherboard_installation2.jpg)

1. Carefully place the motherboard into the chassis, aligning the screw holes
   with the standoffs and ports with holes in the IO shield. Screw in the
   motherboard using the 9 screws from the set.

    ![Motherboard installation](images/motherboard_installation3.jpg)

1. After motherboard is screwed in, CPU cooler fans can be installed by
   snapping them on. The fan with the Arctic logo on the front(intake fan)
   should be facing the front of the chassis.

    ![CPU cooler fans installed](images/cpu_cooler_installation3.jpg)

1. Connect the CPU cooler fans using the connector found on the front(intake)
   fan. Plug in the connector from the front fan into the motherboard
   CPU0_FAN1 connector.

    ![CPU cooler fans connected](images/cpu_cooler_installation4.jpg)
    ![CPU cooler fans plugged in](images/cpu_cooler_installation5.jpg)

1. Prepare the screw set for PSU. It should contain 4 screws.

    ![PSU screws](images/psu_installation1.jpg)

1. Before installing the power supply, locate and plug in the correct cables
   into the PSU - PCIe 6pin, ATX 24pin, two CPU cables.

    ![PSU CPU Cables](images/psu_installation2.jpg)

1. Install the PSU in the case by placing it in its slot on the right side of
   the case and securing it with four screws at the back.

1. Plug in the four PSU cables into the motherboard. The two CPU cables
   connect to P12V_AUX1 and P12V_AUX2 connectors. Pay attention to the
   orientation of the cable - the plastic lock on the cable should align with
   the plastic lock on the connector.

    ![PSU connectors](images/psu_installation4.jpg)
    ![PSU plugged in](images/psu_installation5.jpg)

1. Connect the front-panel cables. There are 7 cables to connect:

    - Case intrusion, into the CASE_OPEN connector
    - RESET SW
    - POWER SW
    - HDD LED
    - POWER LED-
    - POWER LED+
    - USB3

    ![front-panel pinouts](images/front_panel_pinouts.png)

    Install them as shown in the pictures. Pay attention to the cable
    orientation.

    ![front panel CASE OPEN](images/case_cables_installation1.jpg)

    ![front panel CASE OPEN connected](images/case_cables_installation2.jpg)

    ![front panel USB3](images/case_cables_installation3.jpg)

    ![front panel Controls](images/case_cables_installation4.jpg)

1. Fasten the front-panel cables using zip ties as shown in the picture.

    ![front-panel cable management](images/case_cables_installation5.jpg)

1. Connect the back case fan as shown in the picture.

    ![Back case fan](images/fan_back_installation.jpg)

1. Connect the front case fan as shown in the picture.

    ![Front case fan](images/fan_front_installation3.jpg)

1. Install the metal PCIe holder back into its slot. It might be easier to
   first unscrew it from the mounting brackets on the opposite ends and
   install those first.

    ![PCIe holder bracket installation](images/pcie_holder_installation1.jpg)
    ![PCIe holder installation](images/pcie_holder_installation2.jpg)

1. Before closing the case make sure to organize the cables in a way they
   won't interfere with other components such as fans.

    ![Case cable management](images/case.jpg)

1. Close the case by reinstalling all four screws.

1. Attach case keys to the front of the case to prevent loss or
   damage during shipping.

    ![Case keys](images/case-keys.jpg)

## Stock Firmware verification

Once the platform gets assembled, it is crucial to verify its functionality
before attempting to flash Dasharo firmware. This is to exclude the
possibility of the platform not booting due to bad hardware configuration.

Here's a list of steps that need to be performed:

1. Download the latest DTS version (pre-release (`rc`) included) from
    [releases](https://github.com/Dasharo/meta-dts/releases/) and [flash the
    image](https://docs.dasharo.com/dasharo-tools-suite/documentation/running/#bootable-usb-stick)
    to the flash drive. For non-technical users, it is recommended to use
    Etcher to flash the image onto the flash drive.

1. Plug the main power cable, video output cable and ethernet cable as shown
   in the picture

    ![IO cables](images/IO_installation2.jpg)

1. Open the front panel using the attached key.

    ![Front panel opening](images/front_panel_opening.jpg)

1. Plug the previously prepared flash drive into one of the available USB
   ports.

    ![Front panel ports](images/front_panel_opening2.jpg)

1. Power on the device with the button located on the front panel.
1. Make the platform boot from the flash drive.
1. Once DTS boots, run the HCL report with an option to send the logs to
   3mdeb.
1. Power off the device.

## Flashing Dasharo Firmware

The Dasharo firmware is flashed internally via BMC(recommended) or externally
via RTE/SPI. All methods are described in detail in the [recovery
guide](../../variants/gigabyte_mz33-ar1/recovery.md).

The BMC ip is shown when booting or in BIOS under "Server Management -> BMC
Network Configuration". Write it down.

 ![BMC ip](images/BMC_ip.jpg)

### Obtaining the firmware

1. Obtain the newest firmware for the platform. Log in to
   [Minio](https://dlui.dasharo.com), and go to the
   `dasharo-gigabyte-mz33-ar1-uefi/gigabyte-mz33-ar1` directory. The directory
   stores all available firmware versions. Go to the directory containing the
   newest available firmware version. Depending on the flashing method used,
   you will need different files:

    - BMC: .rbu
    - RTE/SPI: .rom

1. Download the chosen file and its respective sha256 signature file(.sha256).

1. Verify the downloaded file's signature, refer to [Signature
   verification](../../guides/signature-verification.md).

### Flashing and verification

#### BMC

1. Detailed instructions can be found at [Flashing via
   BMC](../../variants/gigabyte_mz33-ar1/recovery.md#flashing-via-bmc)

   Once steps from the BMC flashing guide are complete, the firmware is
   flashed successfully.

#### RTE/SPI

1. Detailed instructions can be found at [External
   flashing](../../variants/gigabyte_mz33-ar1/recovery.md#external-flashing)

1. Flash the firmware onto the BIOS memory chip and reinstall it into the
   socket by following the [recovery
   guide](../../variants/gigabyte_mz33-ar1/recovery.md#external-flashing). Use
   the firmware `.rom` file downloaded and verified above as the binary to
   flash. **NOTE THAT THIS ACTION IS DESTRUCTIVE. THE DEFAULT FIRMWARE WILL BE
   ERASED!**
1. Supply the power to the platform, and follow the procedure from the "[Stock
   Firmware Verification](#stock-firmware-verification)".

    The platform will take some time to boot for the first time, and it might
    switch on and off multiple times during the procedure.

    When DTS is booted, verify that the proper firmware version has been
    flashed.

    ![DTS FW version](images/dts_fw_ver.png)

    The picture above showcases the DTS menu. The firmware information and
    version shall be listed as in the image above. Note that the version shown
    in the picture is just an example.

When all steps were performed, the platform is ready to be backed up and
shipped.

## Useful content

* [Building manual][Build] - documentation contains information on how to
  build Dasharo compatible with Gigabyte MZ33-AR1.
* [Board Manual][BoardManual] - documentation contains detailed information
  about the motherboard and its operations.

[Deployment]: ../../variants/gigabyte_mz33-ar1/initial-deployment.md
[Build]: ../../variants/gigabyte_mz33-ar1/building-manual.md
[BoardManual]: https://download.gigabyte.com/FileList/Manual/server_manual_mz33ar1_e_v3.0.pdf
