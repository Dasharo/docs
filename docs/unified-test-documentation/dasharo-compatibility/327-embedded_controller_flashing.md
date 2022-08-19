# Dasharo Compatibility: Embedded controller flashing

## ECF001.001 EC firmware external flashing

**Test description**

This test aims to verify whether there is the possibility to flash the DUT
EC firmware externally using Arduino.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Make yourself familiar with
    [EC recovery documentation](../../../variants/novacustom_ns5x/ec-recovery/).

**Test steps**

1. Prepare the hardware for flashing in accordance with the
    [Prerequisites section](../../../variants/novacustom_ns5x/ec-recovery/#prereqisites).
1. Prepare the firmware in accordance with the
    [Preparation section](../../../variants/novacustom_ns5x/ec-recovery/#preparation).
1. Flash the EC firmware in accordance with the 
    [Flashing section](../../../variants/novacustom_ns5x/ec-recovery/#flashing).
1. Note the results.

**Expected result**

The output of the last command should contain information about the correctly
performed procedure:

```bash
Successfully programmed SPI ROM
```
