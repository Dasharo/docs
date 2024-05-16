# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update. If your device is currently flashed with the proprietary
firmware please refer to the [Initial deployment](initial-deployment.md)
documentation.

For simplicity of the update process, we recommend using
[Dasharo Tools Suite](https://docs.dasharo.com/dasharo-tools-suite/overview).

Before starting the update procedure be sure to disable Dasharo BIOS Boot medium
lock, SMM BIOS Write Protection and Secure boot:

1. Power on the device.
1. While the device is booting, hold the `DELETE` key to enter the UEFI Setup
   Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the [Dasharo Security Options](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
   submenu.
1. Verify the state of the `Lock the BIOS boot medium` and
   `Enable SMM BIOS write protection` options - if any of those are set, press
   `Space` to unselect them and then `F10` to save the changes.
1. Go back to the main menu using the `ESC` key.
1. Enter the `Device Manager` menu.
1. Enter the [Secure Boot Configuration](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
   submenu.
1. Verify that the `Current Secure Boot State` field says Disabled - if not,
   unselect the `Attempt Secure Boot` option below then press `F10` to save the
   changes.
1. Reboot the device to properly apply the changes.

The settings of all the above options can be restored after a firmware update.

## Updating minor versions v1.x.y (e.g. from v1.0.x to v1.1.0)

Full binary should be flashed:

```bash
flashrom -p internal -w [path]
```

## Updating patch version v1.0.x/v1.1.x

Only the `COREBOOT` and `IFWI` partition of the flash needs to be updated.
Flash it using the following command:

```bash
flashrom -p internal -w [path] --fmap -i COREBOOT -i IFWI
```

This command also preserves Dasharo UEFI settings and the boot order.
