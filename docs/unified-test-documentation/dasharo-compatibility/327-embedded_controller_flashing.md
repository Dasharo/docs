# Dasharo Compatibility: Embedded controller flashing

## ECF001.001 EC firmware external flashing

**Test description**

This test aims to verify whether there is the possibility to flash the DUT
EC firmware externally using Arduino.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Make yourself familiar with
    [EC recovery documentation](../../unified/novacustom/recovery.md#ec-firmware-recovery).

**Test steps**

1. Perform EC firmware flashing in accordance with the [EC Recovery section](../../unified/novacustom/recovery.md#ec)
1. Note the results.

**Expected result**

The output of the last command should contain information about the correctly
performed procedure:

```bash
Successfully programmed SPI ROM
```
