# Dasharo Compatibility: OPNsense support

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

## PFS001.001 OPNsense serial installation on hard disk

**Test description**

This test aims to verify that

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = OPNsense

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../../generic-test-setup#os-installer)
    perform the OS installation process. As disk choose the hard disk.

**Expected result**

The information about successful installation should be displayed.

## PFS001.002 Boot OPNsense serial from hard disk

**Test description**

This test aims to verify that

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = pfSense

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.

1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.

## PFS002.001 OPNsense VGA installation on hard disk

**Test description**

This test aims to verify that

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = pfSense

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../../generic-test-setup#os-installer)
    perform the OS installation process. As disk choose the hard disk.

**Expected result**

The information about successful installation should be displayed.

## PFS002.002 Boot OPNsense VGA from hard disk

**Test description**

This test aims to verify that

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = pfSense

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.

1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.
