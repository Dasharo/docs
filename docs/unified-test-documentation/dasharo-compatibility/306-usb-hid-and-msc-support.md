# Dasharo compatibility: USB HID and MSC Support

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

## USB001.001 USB devices detection (firmware)

**Test description**

This test aims to verify that the external USB devices are detected
correctly by the firmware and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Connect the flash drive using the USB port.

**Test steps**

1. Power on the DUT.
1. Enter the boot menu using the `BIOS_SETUP_KEY`.
1. Select the `Boot Menu`, press `Enter` and note the result.

**Expected result**

1. Flash drive entry is listed in the boot menu.

## USB001.0XX USB devices detection in OS (Linux generic)

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    watch -n1 lsusb
    ```

1. Connect external USB devices to DUT USB A port and note the result.

**Expected result**

1. After each device is connected to the USB port, a new USB device entry
    in `lsusb` command output should appear.

## USB001.201 USB devices detection in OS (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## USB001.010 USB devices detection in OS (XCP-NG)

Follows the [generic USB001.0XX Linux-based test case](#usb0010xx-usb-devices-detection-in-os-linux-generic)

## USB001.011 USB devices detection in OS (ESXI)

Follows the [generic USB001.0XX Linux-based test case](#usb0010xx-usb-devices-detection-in-os-linux-generic)

## USB001.301 USB devices detection in OS (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## USB002.201 USB keyboard detection (firmware)

**Test description**

This test aims to verify that the external USB keyboard is detected correctly
by the firmware and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Connect the external USB keyboard using the USB port.

**Test steps**

1. Power on the DUT
1. Enter the boot menu using the `BIOS_SETUP_KEY`.
1. Use the arrow keys, Esc key and the Enter key to navigate the menus.

**Expected result**

1. All menus can be entered using the external USB keyboard.

## USB002.0XX USB keyboard detection (Linux generic)

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `libinput-tools` on the DUT.
1. Connect the external USB keyboard using the USB port.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Run the following command in the terminal:

    ```bash
    libinput debug-events --show-keycodes
    ```

1. Test the alphanumeric keys and note the generated keycodes.
1. Test non-alphanumeric keys and verify that they generate the correct
    keycodes.
1. Test key combinations with the `Shift`, `Ctrl` and `Alt` modifier keys
    (this tests 2-key rollover).

**Expected result**

1. The external USB keyboard is detected in OS.
1. All standard keyboard keys generate the correct keycodes and events as per
   their labels.
1. Key combinations are detected correctly.

## USB002.002 USB keyboard detection (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## USB002.010 USB keyboard detection (XCP-NG)

Follows the [generic USB002.0XX Linux-based test case](#usb0020xx-usb-keyboard-detection-linux-generic)

## USB002.011 USB keyboard detection (ESXI)

Follows the [generic USB002.0XX Linux-based test case](#usb0020xx-usb-keyboard-detection-linux-generic)

## USB002.301 USB keyboard detection (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## USB003.201 Upload 1GB file on USB storage (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## USB003.002 Upload 1GB file on USB storage (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop
