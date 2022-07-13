# Dasharo Security: BIOS lock support

## Test cases

### BLS001.001 BIOS lock support (Ubuntu 22.04)

**Test description**

BIOS lock is a method to prevent flashing the firmware. This test aims to
verify that the BIOS lock function works correctly - if it is turn on internal
flashing should failed.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.22

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).
1. Disable Secure Boot.
1. Obtain any other binary (e.g. vendor firmware or older Dasharo firmware).

**Test steps**

1. Power on the DUT
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Feautures` menu using the arrow keys and Enter.
1. Enter the `Dasharo Security Options` submenu.
1. Verify that the `Lock the BIOS boot medium` option is chosen - if not,
    press `Enter` and then `F10` to save the changes.
1. If it neccessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

    ```bash
    dmidecode -t bios
    ```

1. Open a terminal window and run the following commands:

    ```bash
    flashrom -p internal -w [path_to_obtained_firmware]
    ```

1. Reboot the system
1. Open a terminal window and execute the following command:

    ```bash
    dmidecode -t bios
    ```

**Expected result**

1. The output of the flashing command should contain the following information:

    ```bash
    SPI Configuration is locked down.
    PR0: Warning: 0x00c00000-0x00ffffff is read-only.
    At least some flash regions are write protected. For write operations,
    you should use a flash layout and include only writable regions. See
    manpage for more details.
    ```

1. The output of the `dmidecode` command should show that the firmware version
    has not changed.
