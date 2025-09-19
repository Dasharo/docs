# Dasharo Compatibility: coreboot Fan Control

## CFN001.001 Check CPU entry temperature and CPU fan speed

**Test description**

This test aims to verify that data for CPU temperature and CPU fan speed is
available.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS preparation](../generic-test-setup.md#os-preparation).
1. Proceed with the
   [Generic test setup: OS post installation steps](../generic-test-setup.md#post-installation).

**Test steps**

1. Power on the DUT.
1. Wait for boot until `BOOT_MENU_STRING` appears.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. Select the proper number for `USB_STICK` option.
1. Wait for `debian login:`.
1. Type proper login.
1. Wait for `Password:`.
1. Type the proper password.
1. Wait for `root@debian:~#`.
1. Execute `watch -n 1 "sensors w83795g-i2c-1-2f |grep fan1 -A 16"`.

**Expected result**

There are visible data for `fan1` and `temp7` which represents CPU fan speed and
CPU temperature.

## CFN001.002 Check if increasing CPU temperature increases CPU fan speed

**Test description**

This test aims to verify that CPU fan speed responds properly to increasing CPU
temperature.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS preparation](../generic-test-setup.md#os-preparation).
1. Proceed with the
   [Generic test setup: OS post installation steps](../generic-test-setup.md#post-installation).

**Test steps**

1. Power on the DUT.
1. Wait for boot until `BOOT_MENU_STRING` appears.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. Select the proper number for `USB_STICK` option.
1. Wait for `debian login:`.
1. Type proper login.
1. Wait for `Password:`.
1. Type the proper password.
1. Wait for `root@debian:~#`.
1. Install `stress-ng` package by executing: `sudo apt install stress-ng`.
1. Confirm installation by typing `Y` and pressing `Enter` when asked.
1. Execute command: `watch -n 1 "sensors w83795g-i2c-1-2f |grep fan1 -A 16"`
    and check current CPU temperature and CPU fan speed.
1. Execute command:
    `stress-ng --cpu 16 --io 8 --vm 4 --vm-bytes 4G --timeout 30s --metrics`.
1. Wait 2 minutes.
1. Execute command: `watch -n 1 "sensors w83795g-i2c-1-2f |grep fan1 -A 16"`
    and check current CPU temperature and CPU fan speed.

**Expected result**

1. The CPU temperature after the second check is higher at least 20 degrees.
1. The CPU fan speed after the second check is higher at least 1000 RPM.
