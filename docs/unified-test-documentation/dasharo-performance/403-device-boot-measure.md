# Dasharo Performance: Device boot measure

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).

## DBM001.001 Device boot measure after cold boot (Ubuntu 22.04)

**Test description**

This test aims to verify whether the DUT boots after cold boot and how long this
process takes. This test case may be re-done several times to to average the
results and specify the platform stability.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Cut the power off while DUT is turned on.
1. Restore power and power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    systemd-analyze
    ```

1. Note the results.

**Expected result**

The output of the command should contain the information about duration of
all boot stages.

## DBM002.001 Device boot measure after warmboot (Ubuntu 22.04)

**Test description**

This test aims to verify whether the DUT boots after warmboot and how long this
process takes. This test case may be re-done several times to to average the
results and specify the platform stability.

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
    systemd-analyze
    ```

1. Note the results.

**Expected result**

The output of the command should contain the information about duration of
all boot stages.

## DBM003.001 Device boot measure after reboot (Ubuntu 22.04)

**Test description**

This test aims to verify whether the DUT boots after system reboot and how long
this process takes. This test case may be re-done several times to to average
the results and specify the platform stability.

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
    sudo reboot
    ```

1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    systemd-analyze
    ```

1. Note the results.

**Expected result**

The output of the command should contain the information about duration of
all boot stages.
