# Dasharo Compatibility: Debian Stable and Ubuntu LTS support

## Test cases

### LBT001.001 Debian boot from USB

**Test description**

This test aims to verify that DUT boots properly Debian from USB.

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
5. Wait for `Debian GNU/Linux`

**Expected result**

The `Debian GNU/Linux` is visible and confirms successful boot into OS.

### LBT001.002 Log into booted Debian

**Test description**

This test aims to verify that DUT logs properly into Debian booted from USB.

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
6. Type proper login
8. Wait for `Password:`
9. Type the proper password
10. Wait for `root@debian:~#`

**Expected result**

The `root@debian:~#` is visible after successful login.

### LBT002.001 Ubuntu boot from USB

**Test description**

This test aims to verify that DUT boots properly Ubuntu from USB.

**Test configuration data**

1. `BOOT_MENU_KEY` = `ESC`
2. `BOOT_MENU_STRING` = `Press ESC for boot menu`
3. `USB_STICK` = `USB MSC Drive  USB  SanDisk 3.2Gen1 1.00`

**Test setup**

1. Proceed with the [Generic test setup: firmware](generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Select the proper number for `USB_STICK` option.
5. Wait for `Ubuntu GNU/Linux`

**Expected result**

The `Ubuntu GNU/Linux` is visible and confirms successful boot into OS.

### LBT002.002 Log into booted Ubuntu

**Test description**

This test aims to verify that DUT logs properly into Ubuntu booted from USB.

**Test configuration data**

1. `BOOT_MENU_KEY` = `ESC`
2. `BOOT_MENU_STRING` = `Press ESC for boot menu`
3. `USB_STICK` = `USB MSC Drive  USB  SanDisk 3.2Gen1 1.00`

**Test setup**

1. Proceed with the [Generic test setup: firmware](generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Select the proper number for `USB_STICK` option.
5. Wait for `ubuntu login:`.
6. Type proper login
7. Wait for `Password:`
8. Type the proper password
9. Wait for `root@ubuntu:~#`

**Expected result**

The `root@ubuntu:~#` is visible after successful login.
