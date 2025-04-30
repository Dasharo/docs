# Dasharo Compatibility: miniPCIe slot verification

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

## MWL001.201 Wireless card detection (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## MWL001.301 Wireless card detection (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## MWL002.201 Wi-Fi scanning (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## MWL002.301 Wi-Fi scanning (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## MWL003.201 Bluetooth scanning (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## MWL003.301 Bluetooth scanning (Windows)

**Test description**

This test aims to verify that the Bluetooth functionality of card is initialized
correctly and can be used from within the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Enable Bluetooth and make it discoverable in any device nearby DUT

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Enter `Notification Center` in the bottom right part of the screen.
1. Using right mouse button click on the Bluetooth icon.
1. In shown drop-down menu click `Go to settings`.
1. Click the `+` icon described as `Add Bluetooth or other device`.
1. In the `Add a device` menu click `Bluetooth`.
1. Wait a few moments until DUT scans for nearby Bluetooth devices and note
   the result.

**Expected result**

Available Bluetooth devices should appear in the `Add a device` window.

## MWL004.201 LTE card detection (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop
