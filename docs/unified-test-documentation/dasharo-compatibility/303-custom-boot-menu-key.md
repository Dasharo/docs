# Dasharo compatibility: Custom boot menu key

## Test cases

### CBK001.001 Custom boot menu key

**Test description**

This test aims to verify that the DUT is configured to use custom boot menu
(if it exists) hotkey.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Power on the DUT.
1. Hold the `BIOS_MENU_KEY` to enter the UEFI Setup Menu.

**Expected result**

The DUT boots into an UEFI Boot menu using the specified hotkey.

### CBK002.001 Custom setup menu key

**Test description**

This test aims to verify that the DUT is configured to use custom setup menu
(if it exists) hotkey.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Power on the DUT.
1. Hold the `SETUP_MENU_KEY` to enter the UEFI Setup Menu.

**Expected result**

The DUT boots into an UEFI Setup menu using the specified hotkey.
