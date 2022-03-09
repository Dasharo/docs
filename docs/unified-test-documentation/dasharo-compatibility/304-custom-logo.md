# Dasharo Compatibility: Custom Logo

## Test cases

### CLG001.001 Custom boot logo

**Test description**

This test aims to verify that the DUT is configured to display the specified
(customized) logo at boot.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup/#firmware)

**Test steps**

1. Power on the DUT
1. Wait for the boot logo to appear
1. Verify that it's the NovaCustom logo

**Expected result**

The NovaCustom logo should be displayed at boot:

![NovaCustom logo](../../images/novacustom_logo.bmp)
