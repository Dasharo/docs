# Dasharo compatibility: platform suspend and resume

## Test cases

### SUSP001.001 Platform suspend and resume

**Test description**

This test verifies whether the DUT might be put into suspend mode and then, by 
using the power button, might be resume properly. This test case may be re-done 
several times to specify the platform stability.

**Test configuration data**

1. `FIRMWARE` = coreboot
2. `BOOT_MENU_KEY` = `ESC`
3. `OPERATING_SYSTEM` = `Debian 11.0`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](generic-test-setup#firmware)

**Test steps**

1. Power on the DUT.
1. Boot into OS.
1. Run command `date` and write down output of the command.
1. Run command `systemctl suspend -i`
1. Control status of the platform.
1. Press the power button once and note the result.
1. Run the following command: `journalctl | grep suspend`.

**Expected result**

1. After running suspend command the platform should enter the suspend mode.
2. After pressing power button the platform should initiate the resume 
    procedure.
3. Output of the last command should contains the line with the statement:

            systemd[1]: systemd-suspend.service: Succeeded

4. Date of the above-described event should be later than date from 
    command `date` from point 3.
