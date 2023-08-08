# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update. If your device is currently flashed with the proprietary
firmware please refer to the [Initial deployment](initial-deployment.md)
documentation.

The update process may be different, depending on the currently installed
Dasharo firmware version.

For simplicity of the update process, we recommend using
[Dasharo Tools Suite](../../dasharo-tools-suite/overview.md).

Before starting the update procedure be sure to disable Secure Boot:

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
flashrom -p internal -w protectli_<variant>_v<version>.rom --fmap -i COREBOOT
```
