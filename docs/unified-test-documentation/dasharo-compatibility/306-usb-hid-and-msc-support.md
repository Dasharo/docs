# Dasharo compatibility: USB HID and MSC Support

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

## USB001.201 USB devices detection in OS (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

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

## USB002.002 USB keyboard detection (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## USB002.301 USB keyboard detection (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## USB003.201 Upload 1GB file on USB storage (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## USB003.002 Upload 1GB file on USB storage (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop
