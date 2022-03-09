# Dasharo Security: UEFI Secure Boot

## Test cases

### SBO001.001 UEFI Secure Boot (Ubuntu 20.04)

**Test description**

Secure boot is a verification mechanism for ensuring that code launched by
firmware is trusted. This test verifies that secure boot can be enabled from
Tianocore and, after the DUT reset, it is seen from the OS.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../dasharo-compatibility/generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../../dasharo-compatibility/generic-test-setup/#os-installer)
1. Proceed with the
   [Generic test setup: OS installation](../../dasharo-compatibility/generic-test-setup/#os-installation)

**Test steps**

1. Power on the DUT
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu
1. Enter the `Device Manager` menu using the arrow keys and Enter
1. Enter the `Secure Boot Configuration` submenu
1. Verify that the `Current Secure Boot State` field says `Enabled` - if not,
    select the `Attempt Secure Boot` option below.
1. Go back to the main menu using the `ESC` key
1. Select the `Reset` option to apply the settings and reboot
1. The DUT will now attempt to boot `OPERATING_SYSTEM` with Secure Boot enabled
1. Log in to the default user session
1. Open a terminal window and execute the following command:

```
sudo dmesg | grep secureboot
```

**Expected result**

The output of the command should contain the line:

```
secureboot: Secure boot enabled
```

### SBO001.002 UEFI Secure Boot (Windows 10)

**Test description**

Secure boot is a verification mechanism for ensuring that code launched by
firmware is trusted. This test verifies that secure boot can be enabled from
Tianocore and, after the DUT reset, it is seen from the OS.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 10

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../dasharo-compatibility/generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../../dasharo-compatibility/generic-test-setup/#os-installer)
1. Proceed with the
   [Generic test setup: OS installation](../../dasharo-compatibility/generic-test-setup/#os-installation)

**Test steps**

1. Power on the DUT
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
   Menu
1. Enter the `Device Manager` menu using the arrow keys and Enter
1. Enter the `Secure Boot Configuration` submenu
1. Verify that the `Current Secure Boot State` field says `Enabled` - if not,
   select the `Attempt Secure Boot` option below.
1. Go back to the main menu using the `ESC` key
1. Select the `Reset` option to apply the settings and reboot
1. The DUT will now attempt to boot `OPERATING_SYSTEM` with Secure Boot enabled
1. Log in to the default user session
1. Press Windows+R to open Run Window. Type msinfo32 and press Enter.
1. In the System Information window, go to System Summary, and in the right pane
   select the Secure Boot State and check its state.

**Expected result**

The Secure Boot State should be enabled.
