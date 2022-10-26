# Dasharo Compatibility: Heads bootloader support

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
2. Make yourself familiar with
    [Heads installation](../../../variants/talos_2/initial-deployment/#heads-installation).

## HDS001.001 Boot into Heads

**Test description**

This test verifies that the DUT during booting procedure reaches Heads
bootloader.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Flash bootkernel partition in accordance with the
    [documentation](../../../variants/talos_2/initial-deployment/#heads-installation).
1. Power on the DUT.
1. Wait for the `Heads` to boot and note the result.

**Expected result**

The `Heads` bootloader screen should be displayed.
