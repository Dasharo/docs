# Dasharo Compatibility: pfSense support

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).

## PFS001.001 pfSense stable (serial output) installation on Hard Disk

**Test description**

This test aims to verify that PfSense stable (serial output) could be installed
on the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = pfSense stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../generic-test-setup.md#os-installer)
   perform the OS installation process.

**Expected result**

The information about successful installation should be displayed.

## PFS001.002 Boot pfSense stable (serial output) from Hard Disk

**Test description**

This test aims to verify that pfSense stable (serial output) could be booted
from the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = pfSense stable

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

## PFS002.001 pfSense stable (VGA output) installation on Hard Disk

**Test description**

This test aims to verify that pfSense stable (VGA output) could be installed on
the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = pfSense stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../generic-test-setup.md#os-installer)
    perform the OS installation process.

**Expected result**

The information about successful installation should be displayed.

## PFS002.002 Boot pfSense stable (VGA output) from Hard Disk

**Test description**

This test aims to verify that pfSense stable (VGA output) could be booted from
the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = pfSense stable

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
