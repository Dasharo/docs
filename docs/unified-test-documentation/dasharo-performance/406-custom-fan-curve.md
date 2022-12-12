# Dasharo Performance: Custom fan curve

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

## CFC001.001 CPU fan

**Test description**

The fan has been configured to follow a custom curve. This test aims to verify
that the fan curve is configured correctly and the fan spins up and down
according to the defined values.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `lm-sensors` and `stress-ng` on the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open the terminal window and run the following command:

    ```bash
    stress-ng -c 8
    ```

1. Open the terminal window and run the following command to get the
   temperature:

    ```bash
    sensors | grep 'Package id 0'
    ```

1. In the terminal window run the following command to get the RPM value of the
   CPU fan:

    ```bash
    sensors | grep RPM
    ```

1. Repeat steps 5-6 a couple of times.
1. Note the results.

**Expected result**

TBD
