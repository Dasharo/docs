# Dasharo Compatibility: Fan Control

## Test cases

### FAN001.001 Check CPU entry temperature and CPU fan speed

**Test description**

This test aims to verify that data for CPU temperature and CPU fan speed is
available.

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
4. Select the proper number for `USB_STICK` option.
5. Wait for `debian login:`.
6. Type proper login.
8. Wait for `Password:`.
9. Type the proper password.
10. Wait for `root@debian:~#`.
11. Execute `watch -n 1 "sensors w83795g-i2c-1-2f |grep fan1 -A 16"`.

**Expected result**

There are visible data for `fan1` and `temp7` which represents CPU fan speed and
CPU temperature.

### FAN001.002 Check if increasing CPU temperature increases CPU fan speed

**Test description**

This test aims to verify that CPU fan speed responds properly to increasing CPU
temperature.

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
4. Select the proper number for `USB_STICK` option.
5. Wait for `debian login:`.
6. Type proper login.
8. Wait for `Password:`.
9. Type the proper password.
10. Wait for `root@debian:~#`.
11. Install `stress-ng` package by executing: `sudo apt install stress-ng`.
12. Confirm installation by typing `Y` and pressing `Enter` when asked.
13. Execute command: `watch -n 1 "sensors w83795g-i2c-1-2f |grep fan1 -A 16"`
    and check current CPU temperature and CPU fan speed.
14. Execute command: `stress-ng --cpu 16 --io 8 --vm 4 --vm-bytes 4G --timeout 30s --metrics`.
15. Wait 2 minutes.
16. Execute command: `watch -n 1 "sensors w83795g-i2c-1-2f |grep fan1 -A 16"`
    and check current CPU temperature and CPU fan speed.

**Expected result**

1. The CPU temperature after the second check is higher at least 20 degrees.
2. The CPU fan speed after the second check is higher at least 1000 RPM.
