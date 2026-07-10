# Dasharo Compatibility: OPNSense support

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).

## OPN001.503 Install operating system on disk (OPNSense)

**Test description**

This test aims to verify that OPNSense stable (serial output) could be installed
on the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = OPNSense stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../generic-test-setup.md#os-installer)
   perform the OS installation process.

**Expected result**

The information about successful installation should be displayed.

## OPN002.503 Boot operating system from disk (OPNSense)

**Test description**

This test aims to verify that OPNSense stable serial could be booted from the
hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = OPNSense stable

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

## OPN002.001 OPNSense stable (VGA output) installation on Hard Disk

**Test description**

This test aims to verify that OPNSense stable (VGA output) could be installed on
the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = OPNSense stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../generic-test-setup.md#os-installer)
   perform the OS installation process.

**Expected result**

The information about successful installation should be displayed.

## OPN002.002 Boot OPNSense stable (VGA output) from Hard Disk

**Test description**

This test aims to verify that OPNSense stable (VGA output) could be booted from
the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = OPNSense stable

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
