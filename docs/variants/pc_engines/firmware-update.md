# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update. If your device is currently flashed with the original PC
Engines firmware firmware please refer to the [Initial
deployment](initial-deployment.md) documentation.

The update process may be different, depending on the currently installed
Dasharo firmware version.

We recommend [Dasharo Tools Suite](../../dasharo-tools-suite/overview.md), but
if you really want to do this manually please follow guide below.

Before updating, ensure the SPI flash WP pin is not active - BIOS write
protect pin jumper on J2 (apu2) or J3 (apu3/4/6).

=== "(coreboot+UEFI) firmware"

    Additionally, before starting the update procedure be sure to disable Secure Boot:

    1. Power on the device.
    2. While the device is booting, hold the `DELETE` key to enter the UEFI Setup
       Menu.
    3. Enter the `Device Manager` menu.
    4. Enter the [Secure Boot Configuration](../../dasharo-menu-docs/device-manager.md#secure-boot-configuration)
       submenu.
    5. Verify that the `Current Secure Boot State` field says Disabled - if not,
       unselect the `Attempt Secure Boot` option below then press `F10` to save
       the changes.
    6. Reboot the device to properly apply the changes.

    The settings of all the above options can be restored after a firmware update.

    ## Updating Dasharo

    ```bash
    flashrom -p internal -w pcengines_apu<variant>_v<version>.rom --fmap -i WP_RO -i RW_SECTION_A
    ```

=== "(coreboot+SeaBIOS) firmware"

    ## Updating automatically using DTS

    Check DTS documentation for [firmware
    update](../../dasharo-tools-suite/documentation/features.md#firmware-update).

    ## Updating Dasharo manually

    1. Power on the device.
    1. While the device is booting, hold the `F10` key to enter the sortbootorder
       menu.
    1. Ensure [Firmware Write Protection](https://github.com/pcengines/sortbootorder?tab=readme-ov-file#bios-wp-option)
    1. [Boot into Dasharo Tools Suite](https://docs.dasharo.com/dasharo-tools-suite/documentation/#running)
    1. Enter Shell by choosing `9`
    1. Use following command:

    ```bash
    flashrom -p internal -w pcengines_apu<variant>_v<version>.rom --fmap -i COREBOOT
    ```
