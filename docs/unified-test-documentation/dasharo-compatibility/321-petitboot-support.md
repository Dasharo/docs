# Dasharo Compatibility: Petitboot support

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

### PBT001.001 Boot into Petitboot

**Test description**

This test verifies that the DUT during booting procedure can reach Petitboot
menu.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Petitboot` to boot and note the result.

**Expected result**

The `Petitbooot` menu screen should be displayed.

### PBT002.001 Read System Information from Petitboot

**Test description**

This test verifies that Petitboot System Information option is available and
works correctly.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Petitboot` to boot.
1. Select the `System Information` option using the arrow keys and press
    `Enter`.
1. Note results.

**Expected result**

After select `System Information` option, informations about `Petitboot` should
be displayed.

### PBT003.001 Rescan Devices by Petitboot

**Test description**

This test verifies that Petitboot Rescan Device option is available and
works correctly.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Petitboot` to boot.
1. Select the `Rescan Devices` option using the arrow keys and press `Enter`.
1. Note results.
1. Attach `USB Stick` with bootable system to USB port in DUT.
1. Select the `Rescan Devices` again and note results.

**Expected result**

Information of inserted `USB Stick` should be displayed after the next use of
the `Rescan Devices` option.
