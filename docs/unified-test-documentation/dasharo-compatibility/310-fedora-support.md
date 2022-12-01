# Dasharo Compatibility: Fedora support

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

## FED001.001 Fedora installation

**Test description**

This test aims to verify that Fedora Stable distribution could be installed.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Fedora 37

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](/unified-test-documentation/generic-test-setup#os-installation)
    perform the OS installation process.

**Expected result**

The information about successful installation should be displayed.

## FED001.002 Boot Fedora

**Test description**

This test aims to verify that Fedora Stable distribution could be booted.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Fedora 37

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the `DISK` on which the system was
    previously installed.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.
