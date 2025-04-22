# Dasharo Compatibility: M.2 WiFi/Bluetooth

The test suite is fully automated for Windows and most Linux-based systems.
Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

If your OS is not supported by the OSFV, refer to the guide below.

## Test cases common documentation

**Important notice**

If both are technically supported, as is the case for NovaCustom NV4x, the
test should be carried out separately for both the default Intel network card
and the Atheros one.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../generic-test-setup.md#os-boot-from-disk).

## WLE001.0XX Wireless card detection (Linux generic)

**Test description**

This test aims to verify that the Wi-Fi/Bluetooth card is enumerated correctly
and can be detected from the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

```bash
lspci | grep "Network Controller"
```

**Expected result**

The output of the command should contain information about mounted on the board
network controller.

Example output:

```bash
2f:00.0 Network controller: Intel Corporation Wi-Fi 6 AX201 (rev 1a)
```

## WLE001.010 Wireless card detection (XCP-NG)

Follows the [generic WLE001.0XX Linux-based test case](#wle0010xx-wireless-card-detection-linux-generic)
