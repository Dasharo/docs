# Dasharo Compatibility: USB Boot

## Test cases

### UBB001.001 USB detect and boot after coldboot

**Test description**

This test aims to verify that the DUT properly detects USB device and boots into
operating system after coldboot.

**Test configuration data**

1. `BOOT_MENU_KEY` = `ESC`
2. `BOOT_MENU_STRING` = `Press ESC for boot menu`
3. `USB_STICK` = `USB MSC Drive General USB Flash Disk 1100`

**Test setup**

1. Proceed with the [Generic test setup: firmware](generic-test-setup.md#firmware).

**Test steps**

1. Disconnect the DUT from the power source and then wait a few seconds.
2. Power on the DUT.
3. Wait for boot until `BOOT_MENU_STRING` appears.
4. Press `BOOT_MENU_KEY` to enter the boot menu.
5. Check if `USB_STICK` entry is available.
6. Select the proper number for `USB_STICK` option.
7. Wait for `Debian GNU/Linux`.

**Expected result**

The `Debian GNU/Linux` is visible and confirms successful boot into OS after
coldboot.

### UBB001.002 USB detect and boot after warmboot

**Test description**

This test aims to verify that the DUT properly detects USB device and boots into
operating system after warmboot.

**Test configuration data**

1. `BOOT_MENU_KEY` = `ESC`
2. `BOOT_MENU_STRING` = `Press ESC for boot menu`
3. `USB_STICK` = `USB MSC Drive General USB Flash Disk 1100`

**Test setup**

1. Proceed with the [Generic test setup: firmware](generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Check if `USB_STICK` entry is available.
5. Select the proper number for `USB_STICK` option.
6. Wait for `Debian GNU/Linux`.

**Expected result**

The `Debian GNU/Linux` is visible and confirms successful boot into OS after
warmboot.

### UBB001.003 USB detect and boot after system reboot

**Test description**

This test aims to verify that the DUT properly detects USB device and boots into
operating system after system reboot.

**Test configuration data**

1. `BOOT_MENU_KEY` = `ESC`
2. `BOOT_MENU_STRING` = `Press ESC for boot menu`
3. `USB_STICK` = `USB MSC Drive General USB Flash Disk 1100`

**Test setup**

1. Proceed with the [Generic test setup: firmware](generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Check if `USB_STICK` entry is available.
5. Select the proper number for `USB_STICK` option.
6. Wait for `Debian GNU/Linux`.
7. Log into `Debian` as `root`.
8. Execute `reboot` command.
9. Wait for boot until `BOOT_MENU_STRING` appears.
10. Press `BOOT_MENU_KEY` to enter the boot menu.
11. Check if `USB_STICK` entry is available.
12. Select the proper number for `USB_STICK` option.
13. Wait for `Debian GNU/Linux`.

**Expected result**

The `Debian GNU/Linux` is visible and confirms successful boot into OS after
system reboot.