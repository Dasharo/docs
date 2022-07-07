# Dasharo Compatibility: USB Detection

## Test cases

### UBD001.001 USB detection after coldboot

**Test description**

This test aims to verify that the DUT properly detects USB device after
coldboot (reboot realized by power supply cutting off then restoring back).
This test case may be re-done several times to specify the platform and
connection stability.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Debian 11.0`

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Cut the power off.
2. Restore power to the DUT.
3. Wait for boot until `BOOT_MENU_STRING` appears.
4. Press `BOOT_MENU_KEY` to enter the boot menu.
5. Check if `USB_STICK` entry is available.

**Expected result**

The `USB_STICK` entry is visible which confirms successful detection after
coldboot.

### UBD002.001 USB detect and boot after warmboot

**Test description**

This test aims to verify that the DUT properly detects USB device after
warmboot (reboot realized by device turning off then turning on). This test case
may be re-done several times to specify the platform and connection stability.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Debian 11.0`

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Check if `USB_STICK` entry is available.

**Expected result**

The `USB_STICK` entry is visible which confirms successful detection after
warmboot.

### UBD003.001 USB detect and boot after system reboot

**Test description**

This test aims to verify that the DUT properly detects USB device after system
reboot (reboot performed by relevant command). This test case may be re-done
several times to specify the platform and connection stability.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Debian 11.0`

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Check if `USB_STICK` entry is available.
5. Select the key with a proper number for `iPXE`.
6. Press `Ctrl+B` when prompted to stop iPXE from booting automatically.
7. Wait until `iPXE>` prompt appears.
8. Type in `dhcp` to obtain an IP address.
9. Type in `chain` and local iPXE address after a single space to load a network
boot menu.
10. Select `Debian stable netboot 4.14.y` option below `iPXE boot menu` header.
11. Wait for `debian login:`.
12. Type the `root` login.
13. Wait for `Password:`.
14. Type the proper password.
15. Wait for `root@debian:~#`.
16. Execute `reboot` command.
17. Wait for boot until `BOOT_MENU_STRING` appears.
18. Press `BOOT_MENU_KEY` to enter the boot menu.
19. Check if `USB_STICK` entry is available.

**Expected result**

The `USB_STICK` entry is visible which confirms successful detection after
system reboot.
