# Dasharo Compatibility: Custom boot menu key

## Test cases

### CBK001.001 Custom boot menu key

**Test description**

This test aims to verify that the DUT is configured to use custom boot menu and
setup menu (if it exists) hotkeys.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup/#firmware).

**Test steps**

1. Power on the DUT and hold the `BIOS_SETUP_KEY` to enter the UEFI Setup Menu.
1. Once the DUT has booted into the setup menu, power it off using the power
    button.
1. Power on the DUT again and hold the `BOOT_MENU_KEY` to enter the UEFI Boot
    Menu.

**Expected result**

The DUT boots into an UEFI Setup menu and Boot menu using the specified hotkeys.
