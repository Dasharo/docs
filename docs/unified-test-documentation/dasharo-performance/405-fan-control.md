# Dasharo Performance: Fan Control

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).

### FAN001.001 Fan does not stuck after coldboot (Ubuntu 22.04)

**Test description**

This test aims to verify that fan is not stuck at initial frequency after
coldboot

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Disconnect DUT from power surce.
1. Reconnect DUT to power source.
1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Check if package `lm-sensors` is installed and if not, use bellow command in
the terminal to install:

    ```bash
    apt-get install --assume-yes lm-sensors
    ```

1. In the terminal window run the following command:

    ```bash
    sensors | grep fan1
    ```

1. Repeat command every one minute, for 60 minutes.
1. Compare the results.

**Expected result**

The output of the command should contain information about the current
fan RPM. If the current RPM is the same as initial speed, the test should be
considered as failed.

Example output:

```bash
fan1:        1131 RPM  (min =  329 RPM)
```

### FAN002.001 Fan does not stuck after warmboot (Ubuntu 22.04)

**Test description**

This test aims to verify that fan is not stuck at initial frequency after
warmboot

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Check if package `lm-sensors` is installed and if not, use bellow command in
the terminal to install:

    ```bash
    apt-get install --assume-yes lm-sensors
    ```

1. In the terminal window run the following command:

    ```bash
    sensors | grep fan1
    ```

1. Repeat command every one minute, for 60 minutes.
1. Compare the results.

**Expected result**

The output of the command should contain information about the current
fan RPM. If the current RPM is the same as initial speed, the test should be
considered as failed.

Example output:

```bash
fan1:        1131 RPM  (min =  329 RPM)
```

### FAN003.001 Fan does not stuck after reboot (Ubuntu 22.04)

**Test description**

This test aims to verify that fan is not stuck at initial frequency after
reboot

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Check if package `lm-sensors` is installed and if not, use bellow command in
the terminal to install:

    ```bash
    apt-get install --assume-yes lm-sensors
    ```

1. In the terminal window run the following command:

    ```bash
    sensors | grep fan1
    ```

1. Repeat command every one minute, for 60 minutes.
1. Compare the results.

**Expected result**

The output of the command should contain information about the current
fan RPM. If the current RPM is the same as initial speed, the test should be
considered as failed.

Example output:

```bash
fan1:        1131 RPM  (min =  329 RPM)
```
