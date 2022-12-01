# Dasharo Compatibility: QubesOS support

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

## QOS001.001 QubesOS Stable installation

**Test description**

This test aims to verify that QubesOS Stable distribution could be installed.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = QubesOS 4.1.1

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../generic-test-setup#os-installer)
    perform the OS installation process.

    - [QubeOS downloads site](https://www.qubes-os.org/downloads/)

**Expected result**

The information about successful installation should be displayed.

## QOS001.002 Boot QubesOS

**Test description**

This test aims to verify that QubesOS Stable distribution could be booted.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = QubesOS 4.1.1

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
