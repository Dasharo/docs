# Dasharo Performance: CPU frequency

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).

### CPF001.001 CPU not stuck on initial frequency

**Test description**

Check whether the mounted CPU does not stuck on the initial frequency.

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
    cat /proc/cpuinfo | grep -i mhz
    ```

1. Note the results.

**Expected result**

The output of the command should contain information about the current 
frequency of each CPU. If the current frequency of is the same as initial 
frequency, the test should be considered as failed.

Example of unwanted results:

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

### CPF002.001 CPU running on expected frequency without load

**Test description**

Check whether the mounted CPU is running on expected frequency with charger 
connected.

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
    cat /proc/cpuinfo | grep -i mhz
    ```

1. Note the results.
1. Run the following command in the terminal:

    ```bash
    lscpu | grep i mhz
    ```
1. Compare the results

**Expected result**

Each CPU frequency should be lower than max frequency and grather than min 
frequency defined in output of last command.

### CPF003.001 CPU running on expected frequency without load (battery)

**Test description**

Check whether the mounted CPU is running on expected frequency without charger 
connected.

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
    cat /proc/cpuinfo | grep -i mhz
    ```

1. Note the results.
1. Run the following command in the terminal:

    ```bash
    lscpu | grep i mhz
    ```
1. Compare the results

**Expected result**

Each CPU frequency should be lower than max frequency and grather than min 
frequency defined in output of last command.

### CPF004.001 CPU running on expected frequency with load

**Test description**

Check whether the mounted CPU is running on expected frequency with charger 
connected during stress test.

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
    stress-ng --cpu 0 --timer 32 --timer-freq 1000000 -t 60s --thermalstat 5 --cpu-load 100
    ```

1. Note the results.
1. Run the following command in the terminal:

    ```bash
    lscpu | grep i mhz
    ```
1. Compare the results

**Expected result**

Each the information about CPU frequency, which are displayed should be lower 
than max frequency and grather than min frequency defined in output of last
command.

### CPF005.001 CPU running on expected frequency with load (battery)

**Test description**

Check whether the mounted CPU is running on expected frequency without charger 
connected during stress test.

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
    stress-ng --cpu 0 --timer 32 --timer-freq 1000000 -t 60s --thermalstat 5 --cpu-load 100
    ```

1. Note the results.
1. Run the following command in the terminal:

    ```bash
    lscpu | grep i mhz
    ```
1. Compare the results


**Expected result**

Each the information about CPU frequency, which are displayed should be lower 
than max frequency and grather than min frequency defined in output of last
command.
