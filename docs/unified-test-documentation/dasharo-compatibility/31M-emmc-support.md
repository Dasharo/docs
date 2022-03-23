# Dasharo Compatibility: eMMC support

## Test cases

### MMC001.001 eMMC support (Ubuntu 20.04)

**Test description**

This test aims to verify detection of the eMMC driver via the Operating System.

**Test configuration data**

1. `FIRMWARE` = coreboot
2. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
2. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into system by using the proper login and password.
4. Open a terminal window and execute `sudo parted -l`.
5. Check if the eMMC is present on the list.

**Expected result**

1. The eMMC disk is detected in OS.
