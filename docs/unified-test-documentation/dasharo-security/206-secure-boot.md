# Dasharo Security: UEFI Secure Boot

## SBO001.001 Check Secure Boot default state (firmware)

**Test description**

Secure Boot is a verification mechanism for ensuring that code launched by
firmware is trusted. This test aims to verify that the Secure Boot state after
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

The `Secure Boot State` field should inform that the current state of
Secure Boot is `Disabled`.

## SBO002.001 UEFI Secure Boot (Ubuntu 22.04)

**Test description**

This test verifies that Secure Boot can be enabled from the boot menu and, after
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
1. Open a terminal window and run the following command:

    ```bash
    sudo dmesg | grep secureboot
    ```

1. Note the results.

**Expected result**

The output of the command should contain the line:

```bash
secureboot: Secure boot enabled
```

## SBO002.002 UEFI Secure Boot (Windows 11)

**Test description**

This test verifies that Secure Boot can be enabled from the boot menu and, after
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
1. Open Powershell as administrator and run the following command:

    ```powershell
    Confirm-SecureBootUEFI
    ```

1. Note the results.

**Expected result**

The output of the command should return the information, that Secure Boot is
enabled:

```powershell
True
```

## SBO003.001 Attempt to boot file with the correct key from Shell (firmware)

**Test description**

This test verifies that Secure Boot allows booting a signed file with a correct
key.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. Additional `USB storage` - at least 1GB - for keeping files for booting

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Download the signed with the correct key file from the
    [cloud](https://cloud.3mdeb.com/index.php/s/rAK4qfFeGnSnryD).
1. Download the certificate from the
    [cloud](https://cloud.3mdeb.com/index.php/s/sHRH2GeZcbgtpzF).
1. Place the certificate and the file on the `USB storage`.
1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Secure Boot Mode` field to `Custom Mode`.
1. Select options in the given order: `Custom Secure Boot Options` ->
    `DB Options` -> `Enroll Signature` -> `Enroll Signature Using File`
1. Select the certificate from the `USB storage`.
1. Select the `Commit Changes and Exit` option.
1. Press `ESC` until the setup menu.
1. Select the `Reset` option.
1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter the boot menu.
1. Select the `UEFI Shell` option using the arrow keys and press `Enter`.
1. In the shell open the `USB storage` by executing the following command:

    ```bash
    FS0:
    ```

    > One of the filesystems in the FS list will be the USB storage - typically
    > `FS0:`

1. Boot the previously prepared file by typing its full name:

    ```bash
    hello-valid-keys.efi
    ```

**Expected result**

1. File boots correctly (no information: `Command Error Status: Access Denied`
    on the output).
1. The output of the command shows file content.

Example output:

```bash
Hello, world!
```

## SBO004.001 Attempt to boot file without the key from Shell (firmware)

**Test description**

This test verifies that Secure Boot blocks booting a file without a key.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. Additional `USB storage` - at least 1GB - for keeping files for booting

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Download the not signed file from the
    [cloud](https://cloud.3mdeb.com/index.php/s/iCHCE695FgqZpRF).
1. Place the file on the `USB storage`.
1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter the boot menu.
1. Select the `UEFI Shell` option using the arrow keys and press `Enter`.
1. In the shell open the `USB storage` by executing the following command:

    ```bash
    FS0:
    ```

    > One of the filesystems in the FS list will be the USB storage - typically
    > `FS0:`

1. Boot the previously prepared file by typing its full name:

    ```bash
    hello.efi
    ```

**Expected result**

The output of the command doesn't show file content and information about access
denied is displayed.

Example output:

```bash
Command Error Status: Access Denied
```

## SBO005.001 Attempt to boot file with the wrong-signed key from Shell (firmware)

**Test description**

This test verifies that Secure Boot blocks booting a file with the wrong-signed
key.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. Additional `USB storage` - at least 1GB - for keeping files for booting

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Download the signed with the incorrect key file from the
    [cloud](https://cloud.3mdeb.com/index.php/s/rEWZp85ondabxE4).
1. Place the file on the `USB storage`.
1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter the boot menu.
1. Select the `UEFI Shell` option using the arrow keys and press `Enter`.
1. In the shell open the `USB storage` by executing the following command:

    ```bash
    FS0:
    ```

    > One of the filesystems in the FS list will be the USB storage - typically
    > `FS0:`

1. Boot the previously prepared file by typing its full name:

    ```bash
    hello-bad-keys.efi
    ```

**Expected result**

The output of the command doesn't show file content and information about access
denied is displayed.

Example output:

```bash
Command Error Status: Access Denied
```

## SBO006.001 Reset Secure Boot Keys option is available (firmware)

**Test description**

This test aims to verify, that the `Reset Secure Boot Keys` option is available
after flashing the platform with the Dasharo firmware.

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
1. Verify the `Reset Secure Boot Keys` field.

**Expected result**

The `Reset Secure Boot Keys` option should be listed after entering the
`Secure Boot Configuration` submenu.

## SBO007.001 Attempt to boot the file after restoring keys to default (firmware)

**Test description**

This test verifies that the `Reset Secure Boot Keys` option works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. Additional `USB storage` - at least 1GB - for keeping files for booting

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Download the signed with the correct key file from the
    [cloud](https://cloud.3mdeb.com/index.php/s/rAK4qfFeGnSnryD).
1. Download the certificate from the
    [cloud](https://cloud.3mdeb.com/index.php/s/sHRH2GeZcbgtpzF).
1. Place the certificate and the file on the `USB storage`.
1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Secure Boot Mode` field to `Custom Mode`.
1. Select options in the given order: `Custom Secure Boot Options` ->
    `DB Options` -> `Enroll Signature` -> `Enroll Signature Using File`
1. Select the certificate from the `USB storage`.
1. Select the `Commit Changes and Exit` option.
1. Press `ESC` until the setup menu.
1. Select the `Reset` option.
1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter the boot menu.
1. Select the `UEFI Shell` option using the arrow keys and press `Enter`.
1. In the shell open the `USB storage` by executing the following command:

    ```bash
    FS0:
    ```

    > One of the filesystems in the FS list will be the USB storage - typically
    > `FS0:`

1. Boot the previously prepared file by typing its full name:

    ```bash
    hello-valid-keys.efi
    ```

1. Exit the shell by executing the following command:

    ```bash
    exit
    ```

1. Press `ESC` until the setup menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Select the `Reset Secure Boot Keys` menu using the arrow keys and Enter.
1. If necessary - press `Y` to confirm saving the changes.
1. Press `ESC` until the setup menu.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter the boot menu.
1. Select the `UEFI Shell` option using the arrow keys and press `Enter`.
1. In the shell open the `USB storage` by executing the following command:

    ```bash
    FS0:
    ```

    > One of the filesystems in the FS list will be the USB storage - typically
    > `FS0:`

1. Boot the previously prepared file by typing its full name:

    ```bash
    hello-valid-keys.efi
    ```

**Expected result**

1. The first attempt to run the `hello-valid-keys.efi` script:
    1. File boots correctly (no information:
        `Command Error Status: Access Denied` on the output).
    1. The output of the command shows file content.

        Example output:

        ```bash
        Hello, world!
        ```

1. The second attempt to run the `hello-valid-keys.efi` script:
    1. The output of the command doesn't show file content and information about
        access denied is displayed.

        Example output:

        ```bash
        Command Error Status: Access Denied
        ```

## SBO008.001 Try to enroll the key in the incorrect format (firmware)

**Test description**

This test verifies that Secure Boot doesn't allow enrolling keys in the
incorrect format.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Additional `USB storage` - at least 1GB - for keeping files for booting

**Test steps**

1. Place the file with the `.txt` extension on the `USB storage`.
1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Secure Boot Mode` field to `Custom Mode`.
1. Select options in the given order: `Custom Secure Boot Options` ->
    `DB Options` -> `Enroll Signature` -> `Enroll Signature Using File`
1. Select the file with the `.txt` extension from the `USB storage`.
1. Select the `Commit Changes and Exit` option.

**Expected result**

The popup with information about `ERROR: Unsupported file type!` should appear.
