# Dasharo Performance: CPU temperature

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).

### CPT001.001 CPU temperature without load (Ubuntu 22.04)

**Test description**

This test aims to verify whether the temperature of CPU after system booting
is not higher than the maximum allowed temperature.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    cat /sys/class/thermal/thermal_zone*/temp
    ```

1. Note the result.

**Expected result**

Example output:

    ```bash
    38000
    49000
    ```

To properly determine the current temperature of the CPU, output value
should be divided by 1000. Displayed temperature should be not higher than
defined by the DUT producer maximum temperature.

### CPT001.001 CPU temperature after stress test (Ubuntu 22.04)

**Test description**

Check whether the temperature of CPU is not greater than the maximum allowed 
temperature after stress test.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.
1. Install the `stress-ng` package: `sudo apt install stress-ng`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    stress-ng --cpu 0 --tz -t 60s
    ```

1. Note the result.


**Expected result**

Example output:

    ```bash
    stress-ng: info:  [5706] setting to a 60 second run per stressor
    stress-ng: info:  [5706] dispatching hogs: 8 cpu
    stress-ng: info:  [5706] successful run completed in 60.01s
    stress-ng: info:  [5706] cpu:
    stress-ng: info:  [5706]            iwlwifi_1   35.25 C (308.40 K)
    stress-ng: info:  [5706]         x86_pkg_temp   50.12 C (323.27 K)
    ```

Displayed temperature should not exceed `80 C`.
