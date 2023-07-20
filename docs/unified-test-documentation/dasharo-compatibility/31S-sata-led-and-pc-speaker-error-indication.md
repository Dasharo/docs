# Dasharo Compatibility: SATA LED and PC speaker error indication

## ERR001.001 SATA LED and PC speaker error indication support (firmware)

**Test description**

This test aims to verify if SATA LED blink and PC speaker beeps on critical
firmware errors.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. DUT with PC speaker
3. DUT with SATA LED
4. DUT with removable RAM modules.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Remove power from DUT.
2. Remove all RAM memory modules from the DUT.
3. Connect power supply and power on the DUT.
4. Observe the DUT starts blinking the SATA LED and beeps with PC speaker.

**Expected result**

When no memory modules are connected, this is considered a critical firmware
error and the platform can not proceed with booting. Error indication path will
be triggered causing the platform to beep and blink the SATA LED. There should
be only 12 beeps, but the SATA LED should blink endlessly (until DUT is powered
off or reset).
