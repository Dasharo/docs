# Dasharo Security: Boot menu enable/disable

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../generic-test-setup#firmware).

## BMA001.001 Boot menu enabling

**Test description**

This test aims to verify that, the boot menu is accessible when the
`Boot menu enabled` option in the `Dasharo Security Options` submenu is chosen.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
   Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Dasharo Security Options` submenu.
1. Verify that the `Boot menu enabled` option is chosen - if not, press `Space`
   and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter the UEFI Boot
   Menu.

**Expected result**

1. While the DUT is booting, the prompt
   `BOOT_MENU_KEY to enter Boot Manager Menu` should be displayed.
   Example output:

    ```bash
    F11 to enter Boot Manager Menu
    ```

1. After using the `BOOT MENU KEY` during boot, the boot menu should be
   displayed.

## BMA002.001 Boot menu disabling

**Test description**

This test aims to verify that, the boot menu is not accessible when the
`Boot menu enabled` option in the `Dasharo Security Options` submenu is not
chosen.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
   Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Dasharo Security Options` submenu.
1. Verify that the `Boot menu enabled` option is not chosen - if so, press
   `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Boot
   Menu.

**Expected result**

1. While the DUT is booting, the prompt
   `BOOT_MENU_KEY to enter Boot Manager Menu` should not be displayed.
   Example of unwanted output:

    ```bash
    F11 to enter Boot Manager Menu
    ```

1. Despite using the `BIOS_SETUP_KEY` boot menu should not be displayed.
