# Firmware update

Following documentation describes the  process of Dasharo open-source firmware
update.

The process may be different, depending on the currently installed Dasharo
firmware version.

For simplicity we recommend using
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

## Updating to Dasharo v1.0.18 or v1.0.19

From v1.0.18 Dasharo firmware is rebased on the more up-to-date revision of
coreboot.

If the current version of the firmware on the device is older than v1.0.18 or
you are migrating from proprietary firmware the whole flash chip should be
flashed as described in [Initial Deployment](initial-deployment.md).

If the current version of the firmware on the device is v1.0.18 and it should
be updated to v1.0.19, only the `WP_RO` and `RW_SECTION_A` should be flashed.
To do this the following command should be used:

```bash
flashrom -p internal -w protectli_vault_cml_v1.0.19.rom --fmap -i WP_RO -i RW_SECTION_A
```

## Updating on Dasharo v1.0.16 or v1.0.17

Only the `RW_SECTION_A` partition of the flash needs to be updated. Flash it
using the following command:

```bash
flashrom -p internal -w protectli_vault_cml_v1.0.16.rom --fmap -i RW_SECTION_A
```

This command also preserves Dasharo UEFI settings and the boot order.

## Updating on older Dasharo versions

In this case, the whole `bios` region must be updated.

```bash
flashrom -p internal -w protectli_vault_cml_v1.0.13.rom --ifd -i bios
```
