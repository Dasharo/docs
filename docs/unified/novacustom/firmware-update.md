# Firmware update

## Introduction

This document describes the firmware update for NovaCustom laptops running
Dasharo firmware to the latest version available. The proceess is slightly
different depending on model and installed firmware version.

Choose your generation below:

=== "12th Gen (Alder Lake)"
    ### Update using flashrom

    * Boot into
      [Dasharo Tools Suite](/dasharo-tools-suite/documentation/#running)

    * Follow the procedure described in [DTS firmware update documentation](https://docs.dasharo.com/dasharo-tools-suite/documentation/#firmware-update)

=== "11th Gen (Tiger Lake)"
    Check your currently installed firmware version:

    ```bash
    sudo dmidecode -t bios
    ```

    Alternatively, firmware version can also be checked in the BIOS setup menu.

    ### Versions before v1.3.0

       Firmware v1.3.0 introduced open-source Embedded Controller firmware. Changes
       related to the EC mean that special care must be taken when updating to this
       version.

       Update to version v1.3.0 first, by following
       [this procedure](/dasharo-tools-suite/documentation/#ec-transition).

    ### Version v1.3.0 or newer

    #### Update using flashrom

    * Boot into
       [Dasharo Tools Suite](/dasharo-tools-suite/documentation/#running)

    * Update the BIOS using the following command:

         ```bash
         flashrom -p internal -w [novacustom_model_version.rom] --fmap -i RW_SECTION_A
         ```

         > This command also preserves UEFI settings and the boot order.

    * Update the EC using the following command:

         ```bash
         system76_ectool flash [novacustom_model_version_ec.rom]
         ```
