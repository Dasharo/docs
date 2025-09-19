# Dasharo Stability: USB Type-A devices detection

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
1. Connect the `USB device` to the USB Type-A port.

## SUD0001.201 USB devices detection after cold boot (Ubuntu)

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

## SUD0002.201 USB devices detection after warm boot (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## SUD0003.201 USB devices detection after reboot (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## SUD0004.201 USB devices detection after suspension (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop
