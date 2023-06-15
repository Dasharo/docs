# Dasharo Stability: USB devices

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

## SUD0001.001 USB devices detection after cold boot (Ubuntu 22.04)

**Test description**

This test aims to verify that the external USB devices are detected correctly
after performing cold boot. The test is performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubutnu 22.04

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.
1. Disconnect power source, and remove battery if present.
1. Connect power and battery again.
1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**


## SUD0002.001 USB devices detection after warm boot (Ubuntu 22.04)

**Test description**

This test aims to verify that the external USB devices are detected correctly
after performing warm boot. The test is performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubutnu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.
1. Power off the DUT using power button.
1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**

## SUD0003.001 USB devices detection after reboot (Ubuntu 22.04)

**Test description**

This test aims to verify that the external USB devices are detected correctly
after performing reboot. The test is performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../generic-test-setup#firmware)

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.
1. Disconnect power source, and remove battery if present.
1. Connect power and battery again.
1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**


## SUD0004.001 USB devices detection after suspension (Ubuntu 22.04)

**Test description**

This test aims to verify that the external USB devices are detected correctly
after performing suspend. The test is performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04
1. `SUSPEND_KEY` = `Fn + F12`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.
1. Suspend the DUT using `SUSPEND_KEY`.
1. Wake the device from suspend pressing any key on keyboard.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**

