# Dasharo compatibility: Memory HCL

## HCL001.001 Memory HCL - boot into OS (Ubuntu)

**Test description**

This test aims to verify that the DUT can boot with the memory
module combinations specified in the HCL.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Prepare the memory modules specified in the HCL.
1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS preparation](../generic-test-setup.md#os-preparation).
1. Proceed with the
   [Generic test setup: OS post installation steps](../generic-test-setup.md#post-installation).

**Test steps**

1. Insert the memory module into the DUT's memory port, starting with the first
    position from the HCL.
1. Power on the DUT.
1. Boot into the system.
1. Power off the DUT.
1. Repeat the `test steps` for all positions in the HCL.

**Expected result**

1. The expected result is that the OS boots successfully with all memory
   combinations specified in the HCL
* If the `OPERATING_SYSTEM` boots, note the success and power the DUT OFF
* If the `OPERATING_SYSTEM` doesn't boot, check the logs (optional - if
    connected over serial console) for the
    `FSP Memory Init has returned an error` and note the failure
