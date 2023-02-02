# Dasharo Compatibility: OPNsense support

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../generic-test-setup/#firmware).

## OPN001.001 OPNsense stable (serial output) installation on Hard Disk

**Test description**

This test aims to verify that OPNsense stable (serial output) could be installed
on the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = OPNsense stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../../generic-test-setup#os-installer)
   perform the OS installation process.

**Expected result**

The information about successful installation should be displayed.

## OPN001.002 Boot OPNsense stable (serial output) from Hard Disk

**Test description**

This test aims to verify that OPNsense stable serial could be booted from the
hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = OPNsense stable

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

## OPN002.001 OPNsense stable (VGA output) installation on Hard Disk

**Test description**

This test aims to verify that OPNsense stable (VGA output) could be installed on
the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = OPNsense stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../../generic-test-setup#os-installer)
   perform the OS installation process.

**Expected result**

The information about successful installation should be displayed.

## OPN002.002 Boot OPNsense stable (VGA output) from Hard Disk

**Test description**

This test aims to verify that OPNsense stable (VGA output) could be booted from
the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = OPNsense stable

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
