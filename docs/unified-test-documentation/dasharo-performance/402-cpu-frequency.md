# Dasharo Performance: CPU frequency measure

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS preparation](../generic-test-setup.md#os-preparation).
1. Proceed with the
   [Generic test setup: OS post installation steps](../generic-test-setup.md#post-installation).

## CPF001.201 CPU not stuck on initial frequency (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## CPF001.301 CPU not stuck on initial frequency (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## CPF001.003 CPU not stuck on initial frequency (Heads+Debian)

**Test description**

This test aims to verify whether the mounted CPU does not stuck on the
initial frequency after booting into the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Debian 12`

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

## CPF002.201 CPU runs on expected frequency (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## CPF002.301 CPU runs on expected frequency (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## CPF003.201 CPU runs on expected frequency (Ubuntu, battery)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## CPF003.301 CPU runs on expected frequency (Windows, battery)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## CPF004.201 CPU with load runs on expected frequency (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## CPF004.301 CPU with load runs on expected frequency (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## CPF005.201 CPU with load runs on expected frequency (Ubuntu, battery)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## CPF005.301 CPU with load runs on expected frequency (Windows, battery)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop
