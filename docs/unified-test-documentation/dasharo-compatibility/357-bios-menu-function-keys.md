# Dasharo Compatibility: BIOS menu function keys

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).

## BMF001.001 Reset to Defaults option

**Test description**

This test aims to verify that the `F9` key feature properly reset to Defaults
all Dasharo System Features settings.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Dasharo System Features` menu option.
1. Enter the any of submenus eg. `Power Management Options`.
1. Verify that the `F9=Reset to Defaults` entry is displayed at the bottom of
   the screen.
1. Press `F9` to reset options to defaults.
1. Press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key. If necessary - press `Y` to
   confirm saving the changes again.
1. Select the `Reset` option to apply the settings and reboot.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Dasharo System Features` menu option.
1. Check the state of each option in each submenu.
1. Note the results.

**Expected result**

1. The `F9=Reset to Defaults` entry is displayed in each submenu of Dasharo
   System Features.
1. After using the `F9` key, all `Dasharo System Features` options should be set
   to default. All options covered by this functionality can be found
   [here](https://docs.dasharo.com/../dasharo-menu-docs/dasharo-system-features/).
