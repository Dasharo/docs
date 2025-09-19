# Dasharo compatibility: Super I/O initialization - QubesOS

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

## PPS001.001 PS/2 keyboard detection

**Test description**

This test aims to verify that the external PS/2 keyboard is detected correctly
by the `OPERATING_SYSTEM` and that all basic keys work according to their
labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = QubesOS stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `libinput-tools` in `dom0` on the DUT.
1. Connect the external PS/2 keyboard to the PS/2 port.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window in `dom0` and run the following command:

    ```bash
    sudo dmesg | grep -i PS/2
    ```

1. Run the following command in the terminal:

    ```bash
    libinput debug-events --show-keycodes
    ```

1. Test the alphanumeric keys and note the generated keycodes.
1. Test non-alphanumeric keys and verify that they generate the correct
   keycodes.
1. Test key combinations with the `Shift`, `Ctrl` and `Alt` modifier keys
   (this tests 2-key rollover).

**Expected result**

1. The external PS/2 keyboard is detected in OS.
1. All standard keyboard keys generate the correct keycodes and events as per
   their labels.
1. Key combinations are detected correctly.
