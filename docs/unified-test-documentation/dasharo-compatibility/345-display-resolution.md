# Dasharo compatibility: Display resolution - QubesOS

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

## DSR001.001 Changing the display resolution

**Test description**

This test aims to verify that the display resolution could be changed in the
`OPERATING_SYSTEM` and that the GUI is displayed correctly after this change.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = QubesOS stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Connect any display.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window in `dom0` and run the following command:

    ```bash
    xrandr -s <display_resolution>
    ```

1. Note the results.

**Expected result**

1. Changing the display resolution is possible.
1. After changing the resolution, all icons and subtitles should be displayed
   correctly.
