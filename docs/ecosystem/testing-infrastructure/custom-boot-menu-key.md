# Dasharo Compatibility: Custom boot menu key

## Test cases

### CBK001.001 Custom boot menu key

**Test description**

This test aims to verify that the DUT is configured to use the custom boot menu 
hotkey.

**Test configuration data**

1. `BOOT_MENU_KEY` = `ESC`
2. `BOOT_MENU_STRING` = `Press ESC for boot menu`

**Test setup**

1. Proceed with the [Generic test setup: firmware](../generic-test-setup.md/#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.

**Expected result**

The DUT boots into the boot menu using a specified hotkey. Depending on attached 
devices boot options should be visible.