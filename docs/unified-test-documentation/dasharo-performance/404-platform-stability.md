# Dasharo Performance: Platform stability

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).

## STB001.001 Verify if no reboot occurs in the firmware

**Test description**

This test aims to verify that the DUT booted to the Boot Menu does not reset
after a certain time.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. During boot, press `BOOT MENU KEY`.
1. Press any key to stop further booting.
1. Observe if platform is not resetting on its own.
1. Note the results.

**Expected result**

Platform should remain in boot menu without rebooting during whole observation.

## STB001.002 Verify if no reboot occurs in the OS (Ubuntu 22.04)

**Test description**

This test aims to verify that the DUT booted to the Operation System does not
reset after a certain time.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Cut the power off while DUT is turned on.
1. Restore power and power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Observe if platform is not resetting on its own.
1. Note the results.

**Expected result**

Platform should remain in system without rebooting during whole observation.
