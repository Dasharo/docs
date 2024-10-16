# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update. If your device is currently flashed with the proprietary
firmware please refer to the [Initial deployment](initial-deployment.md)
documentation.

The update process may be different, depending on the currently installed
Dasharo firmware version.

For simplicity of the process we recommend using
[Dasharo Tools Suite](../../dasharo-tools-suite/overview.md).

Before starting the update procedure be sure to disable Dasharo BIOS Boot
medium lock and Secure Boot:

1. Power on the device.
2. While the device is booting, hold the `DELETE` key to enter the UEFI Setup
    Menu.
3. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
4. Enter the [Dasharo Security Options](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
    submenu.
5. Verify the state of the `Lock the BIOS boot medium` option - if the option
    is chosen, press `Space` and then `F10` to save the changes.
6. Go back to the main menu using the `ESC` key.
7. Enter the `Device Manager` menu.
8. Enter the [Secure Boot Configuration](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
    submenu.
9. Verify that the `Current Secure Boot State` field says Disabled - if not,
    unselect the `Attempt Secure Boot` option below then press `F10` to save
    the changes.
10. Reboot the device to properly apply the changes.

The settings of all the above options can be restored after a firmware
update.

## Updating Dasharo

```bash
flashrom -p internal -w hardkernel_odroid_h4_v<version>.rom --fmap -i WP_RO -i RW_SECTION_A
```
