# Dasharo Performance: CPU frequency measure

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).

### CPF001.001 CPU not stuck on initial frequency (Ubuntu 22.04)

**Test description**

This test aims to verify whether the mounted CPU does not stuck on the
initial frequency after booting into the OS.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    cat /proc/cpuinfo | grep -i mhz
    ```

1. Note the results.

**Expected result**

The output of the command should contain information about the current
frequency of each CPU core. If the current frequency for each core is the
same as initial frequency, the test should be considered as failed.

Example output with unwanted results:

```bash
cpu MHz		: 2800.000
cpu MHz		: 2800.000
cpu MHz		: 2800.000
cpu MHz		: 2800.000
cpu MHz		: 2800.000
cpu MHz		: 2800.000
cpu MHz		: 2800.000
cpu MHz		: 2800.000
```

### CPF002.001 CPU runs on expected frequency (Ubuntu 22.04)

**Test description**

This test aims to verify whether the mounted CPU is running on
expected frequency.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    lscpu | grep -i mhz
    ```

1. Note the results.
1. Run the following command in the terminal:

    ```bash
    cat /proc/cpuinfo | grep -i mhz
    ```

1. Compare the results.

**Expected result**

1. The result of running the first command should contain the information about
    current, minimum and maximum CPU frequency.

    Example output:

    ```bash
    CPU MHz:                         2800.0000
    CPU max MHz:                     4700.0000
    CPU min MHz:                     400.0000
    ```

1. The result of running the second command should contain the information
    about current frequency of each CPU core.

    Example output:

    ```bash
    cpu MHz		: 2800.000
    cpu MHz		: 2800.000
    cpu MHz		: 2800.000
    cpu MHz		: 2800.000
    cpu MHz		: 2800.000
    cpu MHz		: 2800.000
    cpu MHz		: 900.542
    cpu MHz		: 461.831
    ```

1. None of CPU core frequencies should be higher than maximum frequency or
    lower than minimum frequency.

### CPF003.001 CPU runs on expected frequency (Ubuntu 22.04, battery)

**Test description**

This test aims to verify whether the mounted CPU is running on expected
frequency when charger is disconnected. The DUT during test works on battery.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    lscpu | grep -i mhz
    ```

1. Note the results.
1. Run the following command in the terminal:

    ```bash
    cat /proc/cpuinfo | grep -i mhz
    ```

1. Compare the results.

**Expected result**

1. The result of running the first command should contain the information about
    current, minimum and maximum CPU frequency.

    Example output:

    ```bash
    CPU MHz:                         1800.000
    CPU max MHz:                     3900.0000
    CPU min MHz:                     1600.0000
    ```

1. The result of running the second command should contain the information
    about current frequency of each CPU core.

    Example output:

    ```bash
    cpu MHz		: 1700.000
    cpu MHz		: 3719.954
    cpu MHz		: 1600.000
    cpu MHz		: 1600.000
    cpu MHz		: 3778.321
    cpu MHz		: 1800.000
    cpu MHz		: 1700.000
    cpu MHz		: 3806.530
    ```

1. None of CPU core frequencies should be higher than maximum frequency or
    lower than minimum frequency.

### CPF004.001 CPU with load runs on expected frequency (Ubuntu 22.04)

**Test description**

This test aims to verify whether the mounted CPU is running on expected
frequency after stress test.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    lscpu | grep -i mhz
    ```

1. Note the results.
1. Run the follwing command in the terminal to start the stress test:

    ```bash
    stress-ng --cpu 0 --timer 32 --timer-freq 1000000 -t 60s --cpu-load 100
    ```

1. After ending the stress test run the following command in the terminal:

    ```bash
    cat /proc/cpuinfo | grep -i mhz
    ```

1. Compare the output from the first and the third command.

**Expected result**

1. The result of running the first command should contain the information about
    current, minimum and maximum CPU frequency.

    Example output:

    ```bash
    CPU MHz:                         1800.000
    CPU max MHz:                     3900.0000
    CPU min MHz:                     1600.0000
    ```

1. The result of running the third command should contain the information
    about current frequency of each CPU core.

    Example output:

    ```bash
    cpu MHz		: 1900.000
    cpu MHz		: 1600.000
    cpu MHz		: 2849.923
    cpu MHz		: 1700.000
    cpu MHz		: 2200.000
    cpu MHz		: 3386.400
    cpu MHz		: 1600.000
    cpu MHz		: 1600.000
    ```

1. None of CPU core frequencies should be higher than maximum frequency or
    lower than minimum frequency.

### CPF005.001 CPU with load runs on expected frequency (Ubuntu 22.04, battery)

**Test description**

This test aims to verify whether the mounted CPU is running on expected
frequency after stress test. The DUT during test works on battery.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    lscpu | grep -i mhz
    ```

1. Note the results.
1. Run the follwing command in the terminal to start the stress test:

    ```bash
    stress-ng --cpu 0 --timer 32 --timer-freq 1000000 -t 60s --cpu-load 100
    ```

1. After ending the stress test run the following command in the terminal:

    ```bash
    cat /proc/cpuinfo | grep -i mhz
    ```

1. Compare the output from the first and the third command.

**Expected result**

1. The result of running the first command should contain the information about
    current, minimum and maximum CPU frequency.

    Example output:

    ```bash
    CPU MHz:                         1800.000
    CPU max MHz:                     3900.0000
    CPU min MHz:                     1600.0000
    ```

1. The result of running the third command should contain the information
    about current frequency of each CPU core.

    Example output:

    ```bash
    cpu MHz		: 1900.000
    cpu MHz		: 1600.000
    cpu MHz		: 2849.923
    cpu MHz		: 1700.000
    cpu MHz		: 2200.000
    cpu MHz		: 3386.400
    cpu MHz		: 1600.000
    cpu MHz		: 1600.000
    ```

1. None of CPU core frequencies should be higher than maximum frequency or
    lower than minimum frequency.
