# Dasharo Compatibility: Ubuntu Server support

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).

## USS001.001 Ubuntu Server stable installation on Hard Disk

**Test description**

This test aims to verify that Ubuntu Server stable could be installed on the
hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu Server stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../generic-test-setup.md#os-installer)
   perform the OS installation process.

**Expected result**

The information about successful installation should be displayed.

## USS001.002 Boot Ubuntu Server stable from Hard Disk

**Test description**

This test aims to verify that Ubuntu Server stable could be booted from the hard
disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu Server stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the device on which the system was previously
   installed.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.
