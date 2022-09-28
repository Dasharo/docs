# Dasharo Performance: CPU frequency measure

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).

## CPF001.001 CPU not stuck on initial frequency (Ubuntu 22.04)

**Test description**

This test aims to verify whether the mounted CPU does not stuck on the
initial frequency after booting into the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

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

## CPF001.002 CPU not stuck on initial frequency (Windows 11)

**Test description**

This test aims to verify whether the mounted CPU does not stuck on the
initial frequency after booting into the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Windows 11`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a powershell as administrator and run the follwing command:

```powershell
while(1){(Get-CimInstance CIM_Processor).MaxClockSpeed*((Get-Counter -Counter "\Processor Information(_Total)\% Processor Performance").CounterSamples.CookedValue)/100}
```

1. Note the results.

**Expected result**

The output of the command should contain information about the current
frequency of CPU. If the following frequency values are the same, the test
should be considered as failed.

Example output with unwanted results:

```bash
2800.00000000000
2800.00000000000
2800.00000000000
2800.00000000000
2800.00000000000
2800.00000000000
2800.00000000000
2800.00000000000
```

## CPF002.001 CPU runs on expected frequency (Ubuntu 22.04)

**Test description**

This test aims to verify whether the mounted CPU is running on
expected frequency.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

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

1. Repeat command every one minute, for 60 minutes.
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

## CPF002.002 CPU runs on expected frequency (Windows 11)

**Test description**

This test aims to verify whether the mounted CPU is running on
expected frequency.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Windows 11`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a powershell as administrator and run the follwing command:

```powershell
(Get-CimInstance CIM_Processor).MaxClockSpeed
```

1. Note the result.
1. Run the following command in the powershell:

```powershell
while(1){(Get-CimInstance CIM_Processor).MaxClockSpeed*((Get-Counter -Counter "\Processor Information(_Total)\% Processor Performance").CounterSamples.CookedValue)/100}
```

1. Repeat command every one minute, for 60 minutes.
1. Note the results.

**Expected result**

1. The result of running the first command should contain the information about
   maximum CPU frequency.

    Example output:

    ```powershell
    2419
    ```

1. None of displayed values ​​that follow the second command should be higher than
   maximum frequency.

    Example output:

    ```bash
    1023.98759600614
    1009.23827168367
    940.831608527132
    1201.62695181908
    1140.59449053201
    1021.87762893503
    983.647614379085
    1206.27777992278
    ```

## CPF003.001 CPU runs on expected frequency (Ubuntu 22.04, battery)

**Test description**

This test aims to verify whether the mounted CPU is running on expected
frequency when charger is disconnected. The DUT during test works on battery.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

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

1. Repeat command every one minute, for 60 minutes.
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

## CPF003.002 CPU runs on expected frequency (Windows 11, battery)

**Test description**

This test aims to verify whether the mounted CPU is running on expected
frequency when charger is disconnected. The DUT during test works on battery.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Windows 11`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a powershell as administrator and run the follwing command:

```powershell
(Get-CimInstance CIM_Processor).MaxClockSpeed
```

1. Note the result.
1. Run the following command in the powershell:

```powershell
while(1){(Get-CimInstance CIM_Processor).MaxClockSpeed*((Get-Counter -Counter "\Processor Information(_Total)\% Processor Performance").CounterSamples.CookedValue)/100}
```

1. Repeat command couple times
1. Note the results.

**Expected result**

1. The result of running the first command should contain the information about
   maximum CPU frequency.

    Example output:

    ```powershell
    2419
    ```

1. None of displayed values ​​that follow the second command should be higher than
   maximum frequency.

    Example output:

    ```bash
    1023.98759600614
    1009.23827168367
    940.831608527132
    1201.62695181908
    1140.59449053201
    1021.87762893503
    983.647614379085
    1206.27777992278
    ```

## CPF004.001 CPU with load runs on expected frequency (Ubuntu 22.04)

**Test description**

This test aims to verify whether the mounted CPU is running on expected
frequency during the stress test.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    lscpu | grep -i mhz
    ```

1. Note the results.
1. Open a terminal window and run the following command to turn on the stressor:

    ```bash
    stress-ng --cpu 0 --tz -t 60m
    ```

    Stress test duration time might be changed by change the value of the
    parameter `-t`.

1. While test runs, open a terminal window and run the following command every
   one minute until the test finishes, to check the current frequency.

    ```bash
    cat /proc/cpuinfo | grep -i mhz
    ```

1. Note the results.

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

## CPF004.002 CPU with load runs on expected frequency (Windows 11)

**Test description**

This test aims to verify whether the mounted CPU is running on
expected frequency during the stress test.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Windows 11`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a powershell as administrator and run the follwing command:

```powershell
(Get-CimInstance CIM_Processor).MaxClockSpeed
```

1. Note the result.
1. Run the stressor.
1. While test runs, open Powershell and run the following command every
    one minute until the test finishes, to check the current frequency:

```powershell
(Get-CimInstance CIM_Processor).MaxClockSpeed*((Get-Counter -Counter "\Processor Information(_Total)\% Processor Performance").CounterSamples.CookedValue)/100
```

1. Repeat command couple times.
1. Note the results.

**Expected result**

1. The result of running the first command should contain the information about
   maximum CPU frequency.

    Example output:

    ```powershell
    2419
    ```

1. None of displayed values ​​that follow the second command should be higher than
   maximum frequency.

    Example output:

    ```bash
    1023.98759600614
    1009.23827168367
    940.831608527132
    1201.62695181908
    1140.59449053201
    1021.87762893503
    983.647614379085
    1206.27777992278
    ```

## CPF005.001 CPU with load runs on expected frequency (Ubuntu 22.04, battery)

**Test description**

This test aims to verify whether the mounted CPU is running on expected
frequency during the stress test. The DUT during test works on battery.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    lscpu | grep -i mhz
    ```

1. Note the results.
1. Open a terminal window and run the following command to turn on the stressor:

    ```bash
    stress-ng --cpu 0 --tz -t 60m
    ```

    Stress test duration time might be changed by change the value of the
    parameter `-t`.

1. While test runs, open a terminal window and run the following command every
   one minute until the test finishes, to check the current frequency.

    ```bash
    cat /proc/cpuinfo | grep -i mhz
    ```

1. Note the results.

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

## CPF005.002 CPU with load runs on expected frequency (Windows 11, battery)

**Test description**

This test aims to verify whether the mounted CPU is running on
expected frequency during the stress test.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Windows 11`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a powershell as administrator and run the follwing command:

```powershell
(Get-CimInstance CIM_Processor).MaxClockSpeed
```

1. Note the result.
1. Run the stressor.
1. While test runs, open Powershell and run the following command every
    one minute until the test finishes, to check the current frequency:

```powershell
(Get-CimInstance CIM_Processor).MaxClockSpeed*((Get-Counter -Counter "\Processor Information(_Total)\% Processor Performance").CounterSamples.CookedValue)/100
```

1. Repeat command couple times.
1. Note the results.

**Expected result**

1. The result of running the first command should contain the information about
   maximum CPU frequency.

    Example output:

    ```powershell
    2419
    ```

1. None of displayed values that follow the second command should be higher than
   maximum frequency.

    Example output:

    ```bash
    1023.98759600614
    1009.23827168367
    940.831608527132
    1201.62695181908
    1140.59449053201
    1021.87762893503
    983.647614379085
    1206.27777992278
    ```
