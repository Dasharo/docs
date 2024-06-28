# Dasharo Stability: USB Type-A devices detection

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS boot from disk](../generic-test-setup.md#os-boot-from-disk).
1. Connect the `USB device` to the USB Type-A port.

## SUD0001.001 USB devices detection after cold boot (Ubuntu)

**Test description**

This test aims to verify that the external USB devices are detected correctly
after performing a cold boot. The test should be performed in multiple
iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

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
1. Disconnect the power source, and remove the battery if present.
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

The output of each `lsusb` command should contain an entry of the connected
`USB device`.

## SUD0002.001 USB devices detection after warm boot (Ubuntu)

**Test description**

This test aims to verify that the external USB devices are detected correctly
after performing a warm boot. The test should be performed in multiple
iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

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
1. Power off the DUT using the power button.
1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**

The output of each `lsusb` command should contain an entry of the connected
`USB device`.

## SUD0003.001 USB devices detection after reboot (Ubuntu)

**Test description**

This test aims to verify that the external USB devices are detected correctly
after performing a reboot. The test should be performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware)

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.
1. Disconnect the power source, and remove the battery if present.
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

The output of each `lsusb` command should contain an entry of the connected
`USB device`.

## SUD0004.001 USB devices detection after suspension (Ubuntu)

**Test description**

This test aims to verify that the external USB devices are detected correctly
after performing suspension. The test should be performed in multiple
iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the [Firmware test suite](https://wiki.ubuntu.com/FirmwareTestSuite)
   package.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.
1. Execute the following command to suspend the system and automatically wake it
   up after 10 seconds:

    ```bash
    sudo fwts s3 --s3-sleep-delay=10
    ```

1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**

The output of each `lsusb` command should contain an entry of the connected
`USB device`.
