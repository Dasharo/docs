# Dasharo Compatibility: Memory HCL

## Test cases

### HCL001.001 Memory HCL - boot into OS (Ubuntu 20.04)

**Test description**

This test aims to verify that the DUT can boot with the memory
module combinations specified in the HCL

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `BIOS_SETUP_KEY` = `F2`
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Prepare the memory modules specified in the HCL.
1. Proceed with the
   [Generic test setup: Firmware](../generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../../dasharo-compatibility/generic-test-setup/#os-installer)
1. Proceed with the
   [Generic test setup: OS installation](../../dasharo-compatibility/generic-test-setup/#os-installation)

**Test steps**

1. Insert the memory module to the DUT's memory port, starting with the first 
    position from the HCL.
1. Power On DUT.
1. Power OFF DUT.
1. Repeat the `test steps` for all positions in the HCL

**Expected result**

1. The expected result is that the OS boots successfully with all memory
   combinations specified in the HCL
  * If the `OPERATING_SYSTEM` boots, note the success and power the DUT OFF
  * If the `OPERATING_SYSTEM` doesn't boot, check the logs (optional - if
    connected over serial console) for the
    `FSP Memory Init has returned an error` and note the failure
