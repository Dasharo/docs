# Dasharo Compatibility: Embedded controller flashing

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

### ECF001.001 Flash EC firmware externally using Arduino

**Test description**

This test aims to verify whether there is the possibility to flash the DUT
EC firmware externally using Arduino.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.
1. Prepare the necessary hardware according to the
    [Prerequisites](../../../variants/novacustom_ns5x/ec-recovery/#prerequisites)
    section.
1. Prepare the firmware according to the
    [Preparation](../../../variants/novacustom_ns5x/ec-recovery/#preparation)
    section.

**Test steps**

1. Go throw [flashing](../../../variants/novacustom_ns5x/ec-recovery/#flashing)
    procedure.
1. Note the results.

**Expected result**

The output of the last command should contain information about the correctly
performed procedure:

```bash
Successfully programmed SPI ROM
```
