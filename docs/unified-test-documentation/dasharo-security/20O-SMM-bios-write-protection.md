# Dasharo Security: SMM BIOS write protection

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
1. Disable Secure Boot.

## SMM001.001 SMM BIOS write protection enabling (Ubuntu)

**Test description**

SMM BIOS write protection is the method to prevent a specific region of the
firmware from being flashed - when enabled allows only SMM code (the privileged
code installed by the firmware in the system memory) to write to BIOS flash.
This test aims to verify that, the SMM BIOS protection option is available in
the `Dasharo Security Options` and, if the mechanism works correctly - during
the attempt of firmware flashing information about the SMM protection is
returned.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Dasharo Security Options` submenu.
1. Verify that the `Enable SMM BIOS write protection` option is chosen - if not,
    press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Execute the following command in the terminal to check platform flashing
    conditions:

    ```bash
    flashrom -p internal
    ```

1. Note the result.

**Expected result**

The output of the flashing command should contain the information, that the
BIOS region SMM protection is enabled.

Example output:

```bash
Enabling flash write... Warning: BIOS region SMM protection is enabled!
```

## SMM002.001 SMM BIOS write protection disabling (Ubuntu)

**Test description**

SMM BIOS write protection is the method to prevent a specific region of the
firmware from being flashed - when enabled allows only SMM code (the privileged
code installed by the firmware in the system memory) to write to BIOS flash.
This test aims to verify that, after disabling the mechanism, information about
SMM protection is not returned any more.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Dasharo Security Options` submenu.
1. Verify that the `Enable SMM BIOS write protection` option is not chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Execute the following command in the terminal to check platform flashing
    conditions:

    ```bash
    flashrom -p internal
    ```

1. Note the result.

**Expected result**

The output of the flashing command should not contain the information, that the
BIOS region SMM protection is enabled.

Example output with unwanted results:

```bash
Enabling flash write... Warning: BIOS region SMM protection is enabled!
```
