# Dasharo Performance: Platform stability

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).

### STB001.001 Verify if no reboot occurs in the firmware

**Test description**

This test aims to verify that DUT booted to firmware will not reboot during
given time.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. During boot, press `BOOT MENU KEY`.
1. Press `ARROW UP` or `ARROW DOWN` to stop further booting.
1. Wait some time and observe if platform is rebooting on its own.
1. Note the results.

**Expected result**

Platform should remain in boot menu without rebooting during whole observation.

### STB001.002 Verify if no reboot occurs in the OS (Ubuntu 22.04)

**Test description**

This test aims to verify that DUT booted to firmware will not reboot during
given time.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the `OPERATING_SYSTEM`.
1. Log into the system by using the proper login and password.
1. Wait some time and observe if platform is rebooting on its own.
1. Note the results.

**Expected result**

Platform should remain in system without rebooting during whole observation.
