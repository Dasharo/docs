# Dasharo Compatibility: Power State After Power Failure

## PSF001.001 Check Power State After Power Failure default state (firmware)

**Test description**

This BIOS setup feature allows users to determine the system's power state
after a power failure. Users can choose between restoring the previous power
state or always returning to a powered off state. This test ensures that the
option is present, and the default state of this option after flashing is
correct.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Power Management Options` submenu.
1. Verify the `Power state after power failure` field.

**Expected result**

The `Power state after power failure` field should inform that the current
Power state after power failure is `Powered Off`.

## PSF002.001 Powered Off State Restoration Test

**Test description**

This test verifies that the `Powered Off` setting works correctly. After we
cut and restore power, the machine should not power on by itself.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Power Management Options` submenu.
1. Set the `Power state after power failure` field to `Powered Off`.
1. Simulate a power failure by cutting power to the system.
1. Restore power and verify that the system does not attempt to start on
its own.
1. Note the results.

**Expected result**

The system should remain in the power off state upon power restoration.

## PSF003.001 Powered On State Restoration Test

**Test description**

This test verifies that the `Powered On` setting works correctly. After we
cut and restore power, the machine should not power on by itself.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Power Management Options` submenu.
1. Set the `Power state after power failure` field to `Powered On`.
1. Simulate a power failure by cutting power to the system.
1. Restore power and verify that the system attempts to power on without
any external prompt.
1. Note the results.

**Expected result**

The system should attempt to power on upon power restoration.

## PSF004.001 Previous Power State Restoration Test - Powered Off

**Test description**

This test verifies that the `The state at the moment of power failure` setting
works correctly if the machine was **powered off** prior to the failure. After we
cut and restore power, the machine should remain powered off.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Power Management Options` submenu.
1. Set the `Power state after power failure` field to
`The state at the moment of power failure`.
1. Power off the DUT.
1. Simulate a power failure by cutting power to the system.
1. Restore power and verify that the system does not attempt to start on
its own.
1. Note the results.

**Expected result**

The system should remain in the powered off state upon power restoration.

## PSF004.002 Previous Power State Restoration Test - Powered On

**Test description**

This test verifies that the `The state at the moment of power failure` setting
works correctly if the machine was **powered on** prior to the failure. After
we cut and restore power, the machine should attempt to power on without any
external prompt.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Power Management Options` submenu.
1. Set the `Power state after power failure` field to
`The state at the moment of power failure`.
1. Do **not** power off the DUT.
1. Simulate a power failure by cutting power to the system.
1. Restore power and verify that the system attempts to power on without
any external prompt.
1. Note the results.

**Expected result**

The system should attempt to power on upon power restoration.
