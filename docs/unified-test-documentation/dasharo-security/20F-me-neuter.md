# Dasharo Security: ME neuter

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup#os-boot-from-disk).

## MNE001.001 Intel ME mode option is available and has the correct default state

**Test description**

This test aims to verify that the `Intel ME mode` state after flashing the
platform with the Dasharo firmware is correct.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Intel Management Engine Options` submenu.
1. Verify the `Intel ME mode` field.

**Expected result**

The `Intel ME mode` field should inform that the current state is `Enabled`.

## MNE002.001 Intel ME mode option Enabled works correctly (Ubuntu 22.04)

**Test description**

This test aims to verify that `Intel ME mode` option in state Enabled works
correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Intel Management Engine Options` submenu.
1. Verify that the `Intel ME mode` option is state `Enabled` - if not, using the
    arrow keys and `Enter`, choose option `Enabled`.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lspci | grep "Management Engine"
    ```

1. Note the results.

**Expected result**

The output of the command should contain the information about Management Engine
Interface.

Example output:

```bash
Intel Corporation Comet Lake Management Engine Interface
```

## MNE003.001 Intel ME mode option Disable (Soft) works correctly (Ubuntu 22.04)

**Test description**

This test aims to verify that `Intel ME mode` option in state Disable (Soft)
works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Intel Management Engine Options` submenu.
1. Verify that the `Intel ME mode` option is state `Disable (Soft)` - if not,
    using the arrow keys and `Enter`, choose option `Disable (Soft)`.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lspci | grep "Management Engine"
    ```

1. Note the results.

**Expected result**

The output of the command shouldn't contain the information about Management
Engine Interface.

Example of unwanted output:

```bash
Intel Corporation Comet Lake Management Engine Interface
```

## MNE004.001 Intel ME mode option Disable (HAP) works correctly (Ubuntu 22.04)

**Test description**

This test aims to verify that `Intel ME mode` option in state Disable (HAP)
works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Intel Management Engine Options` submenu.
1. Verify that the `Intel ME mode` option is state `Disable (HAP)` - if not,
    using the arrow keys and `Enter`, choose option `Disable (HAP)`.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lspci | grep "Management Engine"
    ```

1. Note the results.

**Expected result**

The output of the command shouldn't contain the information about Management
Engine Interface.

Example of unwanted output:

```bash
Intel Corporation Comet Lake Management Engine Interface
```
