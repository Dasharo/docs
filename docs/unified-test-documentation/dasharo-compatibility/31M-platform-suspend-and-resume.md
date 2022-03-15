# Dasharo Compatibility: Platform suspend and resume

## Test cases

### SUSP001.001 Platform suspend and resume

**Test description**

This test verifies whether the DUT might be put into suspend mode and then, by
using the power button, might be properly resumed. This test case may be
re-done several times to specify the platform stability.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Debian 11.0`

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
1. Open a terminal window and execute the following command:

```bash
date
```

1. Write down the output of the above-mentioned command.
1. Execute the following command in the terminal:

```bash
systemctl suspend -i
```

1. Check the status of the platform.
1. Press the power button once and note the result.
1. Execute the following command in the terminal:

```bash
journalctl | grep suspend
```

**Expected result**

1. After running suspend command the platform should enter the suspend mode.
1. After pressing power button the platform should initiate the resume
    procedure.
1. Output of the last command should contains the line with the following
    statement:

```bash
systemd-suspend.service: Succeeded
```

1. Date of the above-described event should be later than date from
    command `date` from the test steps' fourth point.
