# Dasharo Security: Network stack enable/disable

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../generic-test-setup#firmware).
1. The DUT should be connected to the Internet by using an Ethernet cable.

## NBA001.001 Enable Network Boot (firmware)

**Test description**

This test aims to verify that the Network Boot option might be enabled. If this
option is activated, an additional option in the Boot menu which allows to boot
the system from iPXE servers will appear.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Networking Options` menu option.
1. Verify that the `Enable Network Boot` field is checked - if not, use
    `Spacebar` to change option settings.
1. Save using `F10`, and exit from the menu using `Esc`.
1. Reboot the device.
1. While booting, press `BOOT_MENU_KEY` on the USB keyboard to enter Setup
    Menu.
1. Note the results.

**Expected result**

The `Network Boot` option in the `Boot menu` should be visible.

## NBA002.001 Disable Network Boot (firmware)

**Test description**

This test aims to verify that the Network Boot option might be disabled. If this
option is deactivated, an additional option in the Boot menu which allows to
boot the system from iPXE servers will be hidden.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Networking Options` menu option.
1. Verify that the `Enable Network Boot` field is checked - if so, use
    `Spacebar` to change option settings.
1. Save using `F10`, and exit from the menu using `Esc`.
1. Reboot the device.
1. While booting, press `BOOT_MENU_KEY` on the USB keyboard to enter Setup
    Menu.
1. Note the results.

**Expected result**

The `Network Boot` option in the `Boot menu` should not be visible.
