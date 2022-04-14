# Dasharo Compatibility: Heads support

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

### HDS001.001 Boot into Heads

**Test description**

This test verifies that the DUT during booting procedure can reach Heads 
bootloader.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Heads` to boot and note the result.

**Expected result**

The `Heads` bootloader screen should be displayed.
