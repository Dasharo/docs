# Dasharo Security: USB stack

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

## USS001.001 Enable USB stack (firmware)

**Test description**

This test aims to verify that the USB stack might be enabled. If the stack is
activated, there will be an option to use USB bootable drives and USB keyboards
on the firmware level.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Connect PS/2 keyboard to the device.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Dasharo System Features` menu option.
1. Verify that the `Enable USB stack` field is checked - if not, use `Spacebar`
    to change option settings.
1. Save using `F10`, and exit from the menu using `Esc`.
1. Connect any USB with a bootable system and USB keyboard to the DUT.
1. Reboot the device.
1. While booting, press `BOOT_MENU_KEY` on the USB keyboard to enter Setup
    Menu.
1. Note the results.

**Expected result**

1. USB keyboard should be operable.
1. USB installer should be visible as a bootable device.

## USS002.001 Disable USB stack (firmware)

**Test description**

This test aims to verify that the USB stack might be disabled. If the stack is
deactivated, there will be no option to use USB bootable drives and USB
keyboards on the firmware level.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Connect PS/2 keyboard to the device.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Dasharo System Features` menu option.
1. Verify that the `Enable USB stack` field is not checked - if so, use
    `Spacebar` to change option settings.
1. Save using `F10`, and exit from the menu using `Esc`.
1. Connect any USB with a bootable system and USB keyboard to the DUT.
1. Reboot the device.
1. While booting, press `BOOT_MENU_KEY` on the PS/2 keyboard to enter Setup
    Menu.
1. Try to navigate through the menu by using the USB keyboard.
1. Note the results.

**Expected result**

1. USB keyboard should be non-operable.
1. USB installer should not be visible as a bootable device.

## USS003.001 Enable USB Mass Storage (firmware)

**Test description**

This test aims to verify that USB Mass Storage might be enabled. If the storage
support is activated, there will be an option to use USB bootable drives on the
firmware level.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Dasharo System Features` menu option.
1. Verify that the `Enable USB Mass Storage` field is checked - if not, use
    `Spacebar` to change option settings.
1. Save using `F10`, and exit from the menu using `Esc`.
1. Connect any USB with a bootable system and USB keyboard to the DUT.
1. Reboot the device.
1. While booting, press `BOOT_MENU_KEY` to enter Setup Menu.
1. Note the result.

**Expected result**

USB installer should be visible as a bootable device.

## USS004.001 Disable USB Mass Storage (firmware)

**Test description**

This test aims to verify that USB Mass Storage might be disabled. If the storage
support is deactivated, there will be no option to use USB bootable drives on
the firmware level.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Dasharo System Features` menu option.
1. Verify that the `Enable USB Mass Storage` field is not checked - if so, use
    `Spacebar` to change option settings.
1. Save using `F10`, and exit from the menu using `Esc`.
1. Connect any USB with a bootable system and USB keyboard to the DUT.
1. Reboot the device.
1. While booting, press `BOOT_MENU_KEY` to enter Setup Menu.
1. Note the result.

**Expected result**

USB installer should not be visible as a bootable device.
