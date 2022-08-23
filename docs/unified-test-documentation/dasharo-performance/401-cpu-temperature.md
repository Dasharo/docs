# Dasharo Performance: CPU temperature measure

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Install `lm-sensors` package: `sudo apt install lm-sensors`.

### CPT001.001 CPU temperature without load (Ubuntu 22.04)

**Test description**

This test aims to verify whether the temperature of CPU cores after system
booting is not higher than the maximum allowed temperature.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    sensors
    ```

1. Note the result.

**Expected result**

Example output:

```bash
    coretemp-isa-0000
    Adapter: ISA adapter
    Package id 0:  +34.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 0:        +34.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 1:        +34.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 2:        +32.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 3:        +33.0°C  (high = +100.0°C, crit = +100.0°C)
```

Displayed temperature should be not higher than displayed high and
critical temperatures. Also the temperature should be not higher than
temperature declared by the DUT producer.

### CPT002.001 CPU temperature during stress test (Ubuntu 22.04)

**Test description**

This test aims to verify whether the temperature of the CPU cores is not higher
than the maximum allowed temperature during stress test.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the [Common](#common) section.
1. Install the `stress-ng` package: `sudo apt install stress-ng`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command to turn on the stressor:

    ```bash
    stress-ng --cpu 0 --tz -t 60m
    ```

    Stress test duration time might be changed by change the value of the
    parameter `-t`.

1. While test runs, open a terminal window and run the following command every
   one minute until the test finishes, to check the current temperature.

    ```bash
    sensors
    ```

1. Note the results.

**Expected result**

Example output:

```bash
    coretemp-isa-0000
    Adapter: ISA adapter
    Package id 0:  +54.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 0:        +50.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 1:        +49.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 2:        +53.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 3:        +51.0°C  (high = +100.0°C, crit = +100.0°C)
```

The displayed temperatures should be not higher than displayed high and
critical. Also the temperatures should be not higher than
those declared by the DUT's producer.
