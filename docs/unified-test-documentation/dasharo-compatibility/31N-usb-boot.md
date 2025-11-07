# Dasharo Compatibility: USB Boot

## UBT001.001 USB detect and boot after coldboot

**Test description**

This test aims to verify that the DUT properly detects USB device and boots
into the operating system after coldboot (reboot realized by power supply
cutting off then restoring back). This test case may be re-done several times
to specify the platform and connection stability.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Debian`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Cut the power off.
2. Restore power to the DUT.
3. Wait for boot until `BOOT_MENU_STRING` appears.
4. Press `BOOT_MENU_KEY` to enter the boot menu.
5. Check if `USB_STICK` entry is available.
6. Select the proper number for `USB_STICK` option.
7. Wait for `Debian GNU/Linux`.

**Expected result**

The `Debian GNU/Linux` is visible and confirms successful boot into OS after
coldboot.

## UBT002.001 USB detect and boot after warmboot

**Test description**

This test aims to verify that the DUT properly detects USB device and boots
into the operating system after warmboot (reboot realized by device turning
off then turning on). This test case may be re-done several times to specify
the platform and connection stability.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Debian`

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

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

## UBT003.001 USB detect and boot after system reboot

**Test description**

This test aims to verify that the DUT properly detects USB device and boots
into the operating system after system reboot (reboot performed by relevant
command). This test case may be re-done several times to specify the
platform and connection stability.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Debian`

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Check if `USB_STICK` entry is available.
5. Select the proper number for `USB_STICK` option.
6. Wait for `Debian GNU/Linux`.
7. Wait for `debian login:`.
8. Type the `root` login.
9. Wait for `Password:`.
10. Type the proper password.
11. Wait for `root@debian:~#`.
12. Execute `reboot` command.
13. Wait for boot until `BOOT_MENU_STRING` appears.
14. Press `BOOT_MENU_KEY` to enter the boot menu.
15. Check if `USB_STICK` entry is available.
16. Select the proper number for `USB_STICK` option.
17. Wait for `Debian GNU/Linux`.

**Expected result**

The `Debian GNU/Linux` is visible and confirms successful boot into OS after
system reboot.
