# Dasharo Compatibility: Petitboot payload support

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

## PBT001.001 Boot into Petitboot

**Test description**

This test verifies that the DUT during booting procedure reaches Petitboot
menu.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Petitboot` to boot and note the result.

**Expected result**

The `Petitbooot` menu screen should be displayed.

## PBT002.001 Read System Information from Petitboot

**Test description**

This test verifies that Petitboot System Information option is available and
works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Petitboot` to boot.
1. Select the `System Information` option using the arrow keys and press
    `Enter`.
1. Note the result.

**Expected result**

After select `System Information` option, device information tree should be
displayed.

## PBT003.001 Rescan Devices by Petitboot

**Test description**

This test verifies that Petitboot Rescan Device option is available and
works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Petitboot` to boot.
1. Select the `Rescan Devices` option using the arrow keys and press `Enter`.
1. Note the results.
1. Attach `USB Stick` with bootable system to USB port in DUT.
1. Select the `Rescan Devices` again and note the results.

**Expected result**

Information about the attached `USB Stick` should be displayed after the
second use of the `Rescan Devices` option.
