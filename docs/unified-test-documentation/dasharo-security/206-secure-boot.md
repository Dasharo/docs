# Dasharo Security: UEFI Secure Boot

## SBO001.001 Check Secure Boot default state (firmware)

**Test description**

Secure Boot is a verification mechanism for ensuring that code launched by
firmware is trusted. This test aims to verfiy that Secure Boot state after
flashing the platform with the Dasharo firmware is correct.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Verify the `Current Secure Boot State` field.

**Expected result**

Secure Boot state should be compatibile with `platform settings`.

## SBO002.001 UEFI Secure Boot (Ubuntu 22.04)

**Test description**

This test verifies that Secure Boot can be enabled from boot menu and, after
the DUT reset, it is seen from the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Verify that the `Current Secure Boot State` field says `Enabled` - if not,
    select the `Attempt Secure Boot` option below.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. The DUT will now attempt to boot `OPERATING_SYSTEM` with Secure Boot enabled.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    cat /proc/cpuinfo | grep -i mhz
    ```

1. Note the results.

**Expected result**

The output of the command should contain the line:

```bash
secureboot: Secure boot enabled
```

## SBO002.002 UEFI Secure Boot (Windows 11)

**Test description**

This test verifies that Secure Boot can be enabled from boot menu and, after
the DUT reset, it is seen from the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../dasharo-compatibility/generic-test-setup/#firmware).
1. Proceed with the
   [Generic test setup: OS installer](../../dasharo-compatibility/generic-test-setup/#os-installer).
1. Proceed with the
   [Generic test setup: OS installation](../../dasharo-compatibility/generic-test-setup/#os-installation).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
   Menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Verify that the `Current Secure Boot State` field says `Enabled` - if not,
   select the `Attempt Secure Boot` option below.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. The DUT will now attempt to boot `OPERATING_SYSTEM` with Secure Boot enabled.
1. Log into the system by using the proper login and password.
1. Open Powershell as administrator and run the follwing command:

    ```powershell
    Confirm-SecureBootUEFI
    ```

1. Note the results.

**Expected result**

The output of the command should return the information, that Secure Boot is
enabled:

```bash
True
```
