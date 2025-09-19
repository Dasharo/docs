# Dasharo Performance: Fan Control

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
1. Check if package `lm-sensors` is installed and if not, use below command in
    the terminal to install:

    ```bash
    apt-get install --assume-yes lm-sensors
    ```

## FNM001.001 Fan does not stuck after coldboot (Ubuntu)

**Test description**

This test aims to verify that the fan does not stuck on initial or any defined
speed after coldboot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Cut the power off while DUT is turned on.
1. Restore power and power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. In the terminal window run the following command\:

    ```bash
    sensors | grep fan1
    ```

1. Repeat command every one minute, for 60 minutes.
1. Compare the results.

**Expected result**

The output of the command should contain information about the current
fan speed. If the current speed is the same as initial speed, the test should
be considered as failed. If the current speed does not change in the long term,
the test should be considered as failed.

Example output:

```bash
fan1:        1131 RPM  (min =  329 RPM)
```

## FNM002.001 Fan does not stuck after warmboot (Ubuntu)

**Test description**

This test aims to verify that the fan does not stuck on initial or any defined
speed after warmboot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. In the terminal window run the following command:

    ```bash
    sensors | grep fan1
    ```

1. Repeat command every one minute, for 60 minutes.
1. Compare the results.

**Expected result**

The output of the command should contain information about the current
fan speed. If the current speed is the same as initial speed, the test should
be considered as failed. If the current speed does not change in the long term,
the test should be considered as failed.

Example output:

```bash
fan1:        1131 RPM  (min =  329 RPM)
```

## FNM003.001 Fan does not stuck after reboot (Ubuntu)

**Test description**

This test aims to verify that the fan does not stuck on initial or any defined
speed after reboot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. In the terminal window run the following command:

    ```bash
    sensors | grep fan1
    ```

1. Repeat command every one minute, for 60 minutes.
1. Compare the results.

**Expected result**

The output of the command should contain information about the current
fan speed. If the current speed is the same as initial speed, the test should
be considered as failed. If the current speed does not change in the long term,
the test should be considered as failed.

Example output:

```bash
fan1:        1131 RPM  (min =  329 RPM)
```
