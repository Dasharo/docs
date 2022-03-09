# Dasharo Compatibility: Windows 10 booting

## Test cases

### WBT001.001 Windows 10 installation and boot

**Test description**

This test verifies that Windows 10 OS could be installed on the Device 
Under Test and works properly.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 10

**Test setup**

1. Proceed with the
   [Generic test setup: Firmware](../generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup/#os-installation)

**Test steps**

1. Power on the DUT
1. Wait for the `OPERATING_SYSTEM` to boot and note the result


**Expected result**

The Windows 10 login screen should be displayed.
