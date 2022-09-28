# Dasharo compatibility: Custom Boot Keys

## CBK001.001 Custom Boot Menu Key

**Test description**

This test aims to verify that the DUT is configured to use custom Boot Menu
hotkey (if it exists).

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the Boot Menu.

**Expected result**

The DUT boots into the Boot Menu after using the specified hotkey.

## CBK002.001 Custom BIOS Menu Key

**Test description**

This test aims to verify that the DUT is configured to use custom BIOS Menu
hotkey.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Power on the DUT.
1. Hold the `BIOS_MENU_KEY` to enter the BIOS menu.

**Expected result**

The DUT boots into the BIOS menu after using the specified hotkey.
