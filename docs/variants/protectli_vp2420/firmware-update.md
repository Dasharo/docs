# Firmware update

The following documentation describes the  process of Dasharo open-source
firmware update. If your device is currently flashed with the proprietary
firmware please refer to [Initial deployment](initial-deployment.md)
documentation.

For simplicity of the update process, we recommend using
[Dasharo Tools Suite](../../../common-coreboot-docs/dasharo_tools_suite).

Before starting the update procedure be sure to disable Dasharo BIOS Boot medium
lock:

1. Power on the device.
1. While the device is booting, hold the `DELETE` key to enter the UEFI Setup
   Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Dasharo Security Options` submenu.
1. Verify the state of the `Lock the BIOS boot medium` option - if the option
   is chosen, press `Space` and then `F10` to save the changes.
1. Reboot the device to properly apply the changes.

Only the `RW_SECTION_A` partition of the flash needs to be updated. Flash it
using the following command:

```bash
flashrom -p internal -w [path] --fmap -i RW_SECTION_A
```

This command also preserves Dasharo UEFI settings and the boot order.
