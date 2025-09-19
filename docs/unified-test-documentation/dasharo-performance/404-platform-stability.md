# Dasharo Performance: Platform stability

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

## STB001.001 Verify if no reboot occurs in the firmware

**Test description**

This test aims to verify that the DUT booted to the BIOS does not reset. The
test is performed in multiple iterations - after a defined time an attempt to
read the same menu is repeated.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While booting, press `SETUP_MENU_KEY` to enter the setup menu.
1. Note the results.
1. After the specified time has elapsed, repeat the operation described in
    step 3.

**Expected result**

The platform should remain in the setup menu in every testing iteration.

## STB001.201 Verify if no reboot occurs in the OS (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## STB001.301 Verify if no reboot occurs in the OS (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop
