# Dasharo Compatibility: UEFI compatible interface

## Test cases

### EFI001.001 Boot into UEFI OS (Ubuntu 20.04)

**Test description**

This test verifies the presence of UEFI compatible interfaces by booting
UEFI-aware Operating System.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
   [Generic test setup: Firmware](../generic-test-setup/#firmware).
1. Proceed with the
   [Generic test setup: OS installer](../generic-test-setup/#os-installer).

**Test steps**

1. Power on the DUT.
1. Enter the boot menu using the `BIOS_SETUP_KEY`.
1. Select the `Boot Menu` and press `Enter`.
1. Select the USB stick and press `Enter`.
1. Select the `Ubuntu (safe graphics)` in the GRUB menu.
1. Wait for the `OPERATING_SYSTEM` to boot finalize booting, by either of the:
   - `OPERATING_SYSTEM` installer initialization,
   - login form initialization.
1. Power OFF the DUT.

**Expected result**

1. Either the login screen or the `OPERATING_SYSTEM` installer appears on the
   internal LCD.

### EFI001.002 Boot into UEFI OS (Windows 11)

**Test description**

This test aims to verify the presence of UEFI compatible interfaces by booting
UEFI-aware Operating System.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the
   [Generic test setup: Firmware](../generic-test-setup/#firmware).
1. Proceed with the
   [Generic test setup: OS installer](../generic-test-setup/#os-installer).

**Test steps**

1. Power on the DUT.
1. Enter the boot menu using the `BIOS_SETUP_KEY`.
1. Select the `Boot Menu` and press `Enter`.
1. Select the USB stick and press `Enter`.
1. Wait for the `OPERATING_SYSTEM` to boot finalize booting, by either of the:
   - `OPERATING_SYSTEM` installer initialization,
   - login form initialization.
1. Power OFF the DUT.

**Expected result**

1. Either the login screen or the `OPERATING_SYSTEM` installer appears on the
   internal LCD.
