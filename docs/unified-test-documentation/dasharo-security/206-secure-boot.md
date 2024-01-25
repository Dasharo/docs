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
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

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
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Secure Boot Configuration](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
   to enable the `Attempt Secure Boot` option in the
   `Secure Boot Configuration` menu.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. If a message `To enable Secure Boot, set Secure Boot Mode to Custom and
   enroll the keys/PK first` appears:
    1. Set `Secure Boot Mode` to `Custom Mode`
    1. Enter `Advanced Secure Boot Keys Management` submenu
    1. Select `Reset to default Secure Boot Keys`
    1. If a pop-up appears to confirm the selection, select `Yes`
    1. Press `Esc` to go back
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
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Secure Boot Configuration](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
   to enable the `Attempt Secure Boot` option in the
   `Secure Boot Configuration` menu.

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
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

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
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

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
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

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

## SBO006.001 Reset Secure Boot Keys option availability (firmware)

**Test description**

This test aims to verify, that the `Reset Secure Boot Keys` option is available
after flashing the platform with the Dasharo firmware.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set `Advanced Secure Boot Keys Management` submenu.
1. Verify the `Reset to default Secure Boot Keys` field.

**Expected result**

The `Reset Secure Boot Keys` option should be listed after entering the key
management submenu.

## SBO007.001 Attempt to boot the file after restoring keys to default (firmware)

**Test description**

This test verifies that the `Reset Secure Boot Keys` option works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. Additional `USB storage` - at least 1GB - for keeping files for booting

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

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
1. Select options in the given order: `Advanced Secure Boot Keys Management` ->
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
1. Enter the `Advanced Secure Boot Keys Management` submenu.
1. Select the `Reset to default Secure Boot keys` option using the arrow keys
   and Enter.
1. If necessary - press `Y` to confirm saving the changes.
1. Press `ESC` until the setup menu.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Verify that the `Current Secure Boot State` field says `Enabled`.
1. Press `ESC` until the setup menu.
1. Select the `One Time Boot` menu using the arrow keys and Enter.
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

1. After selecting the `Reset Secure Boot Keys` option, the Secure boot state
    should be automatically enabled.

## SBO008.001 Attempt to enroll the key in the incorrect format (firmware)

**Test description**

This test verifies that Secure Boot doesn't allow enrolling keys in the
incorrect format.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
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
1. Select options in the given order: `Advanced Secure Boot Keys Management` ->
    `DB Options` -> `Enroll Signature` -> `Enroll Signature Using File`
1. Select the file with the `.txt` extension from the `USB storage`.
1. Select the `Commit Changes and Exit` option.

**Expected result**

The popup with information about `ERROR: Unsupported file type!` should appear.

## SBO009.001 Attempt to boot file signed for intermediate certificate

**Test description**

This test verifies that a file signed with an intermediate certificate can be
executed.

**Test configuration data**

1. `FIRMWARE` = Dasharo.
1. Additional `USB storage` - at least 1GB - for keeping files for booting.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Run script `open-source-firmware-validation/scripts/secure-boot/generate-images/sb-img/wrapper.sh`
    to generate `INTERMIDIATE.img`.
1. Place `open-source-firmware-validation/scripts/secure-boot/images/INTERMIDIATE.img`
    on the `USB storage`.
1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Current Secure Boot State` field to `Enabled`.
1. Set the `Secure Boot Mode` field to `Custom Mode`.
1. Select options in the given order: `Custom Secure Boot Options` ->
    `DB Options` -> `Enroll Signature` -> `Enroll Signature Using File`.
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
    signed-hello.efi
    ```

**Expected result**

1. File boots correctly (no information: `Command Error Status: Access Denied`
    on the output).
1. The output of the command shows file content.

Example output:

```bash
Hello, world!
```

## SBO010.001 Check support for rsa2k signed certificates

**Test description**

This test verifies that a file can be booted via Secure Boot using an RSA2048
signed certificate.

**Test configuration data**

1. `FIRMWARE` = Dasharo.
1. Additional `USB storage` - at least 1GB - for keeping files for booting.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Run script `open-source-firmware-validation/scripts/secure-boot/generate-images/sb-img-wrapper.sh`
    to generate `RSA2048.img`.
1. Place `open-source-firmware-validation/scripts/secure-boot/images/RSA2048.img`
    on the `USB storage`.
1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Current Secure Boot State` field to `Enabled`.
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
    signed-hello.efi
    ```

**Expected result**

1. File boots correctly (no information: `Command Error Status: Access Denied`
    on the output).
1. The output of the command shows file content.

Example output:

```bash
Hello, world!
```

## SBO010.002 Check support for rsa3k signed certificates

**Test description**

This test verifies that a file can be booted via Secure Boot using an RSA3072
signed certificate.

**Test configuration data**

1. `FIRMWARE` = Dasharo.
1. Additional `USB storage` - at least 1GB - for keeping files for booting.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Run script `open-source-firmware-validation/scripts/secure-boot/generate-images/sb-img-wrapper.sh`
    to generate `RSA3072.img`.
1. Place `open-source-firmware-validation/scripts/secure-boot/images/RSA3072.img`
    on the `USB storage`.
1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Current Secure Boot State` field to `Enabled`.
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
    signed-hello.efi
    ```

**Expected result**

1. File boots correctly (no information: `Command Error Status: Access Denied`
    on the output).
1. The output of the command shows file content.

Example output:

```bash
Hello, world!
```

## SBO010.003 Check support for rsa4k signed certificates

**Test description**

This test verifies that a file can be booted via Secure Boot using an RSA4096
signed certificate.

**Test configuration data**

1. `FIRMWARE` = Dasharo.
1. Additional `USB storage` - at least 1GB - for keeping files for booting.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Run script `open-source-firmware-validation/scripts/secure-boot/generate-images/sb-img-wrapper.sh`
    to generate `RSA4096.img`.
1. Place `open-source-firmware-validation/scripts/secure-boot/images/RSA4096.img`
    on the `USB storage`.
1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Current Secure Boot State` field to `Enabled`.
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
    signed-hello.efi
    ```

**Expected result**

1. File boots correctly (no information: `Command Error Status: Access Denied`
    on the output).
1. The output of the command shows file content.

Example output:

```bash
Hello, world!
```

## SBO010.004 Check support for ecdsa256 signed certificates

**Test description**

This test verifies that a file can be booted via Secure Boot using an ESCDA256
signed certificate.

**Test configuration data**

1. `FIRMWARE` = Dasharo.
1. Additional `USB storage` - at least 1GB - for keeping files for booting.

**Test setup**

1. Proceed with the
[Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Run script `open-source-firmware-validation/scripts/secure-boot/generate-images/sb-img-wrapper.sh`
    to generate `ECDSA256.img`.
1. Place `open-source-firmware-validation/scripts/secure-boot/images/ECDSA256.img`
    on the `USB storage`.
1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Current Secure Boot State` field to `Enabled`.
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
    signed-hello.efi
    ```

**Expected result**

1. File boots correctly (no information: `Command Error Status: Access Denied`
    on the output).
1. The output of the command shows file content.

Example output:

```bash
Hello, world!
```

## SBO010.005 Check support for ecdsa384 signed certificates

**Test description**

This test verifies that a file can be booted via Secure Boot using an ESCDA384
signed certificate.

**Test configuration data**

1. `FIRMWARE` = Dasharo.
1. Additional `USB storage` - at least 1GB - for keeping files for booting.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Run script `open-source-firmware-validation/scripts/secure-boot/generate-images/sb-img-wrapper.sh`
    to generate `ECDSA384.img`.
1. Place `open-source-firmware-validation/scripts/secure-boot/images/ECDSA384.img`
    on the `USB storage`.
1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Current Secure Boot State` field to `Enabled`.
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
    signed-hello.efi
    ```

**Expected result**

1. File boots correctly (no information: `Command Error Status: Access Denied`
    on the output).
1. The output of the command shows file content.

Example output:

```bash
Hello, world!
```

## SBO010.006 Check support for ecdsa521 signed certificates

**Test description**

This test verifies that a file can be booted via Secure Boot using an ESCDA521
signed certificate.

**Test configuration data**

1. `FIRMWARE` = Dasharo.
1. Additional `USB storage` - at least 1GB - for keeping files for booting.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Run script `open-source-firmware-validation/scripts/secure-boot/generate-images/sb-img-wrapper.sh`
    to generate `ECDSA521.img`.
1. Place `open-source-firmware-validation/scripts/secure-boot/images/ECDSA521.img`
    on the `USB storage`.
1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Current Secure Boot State` field to `Enabled`.
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
    signed-hello.efi
    ```

**Expected result**

1. File boots correctly (no information: `Command Error Status: Access Denied`
    on the output).
1. The output of the command shows file content.

Example output:

```bash
Hello, world!
```

## SBO011.001 Attempt to enroll expired certificate and boot signed image

**Test description**

This test verifies that an expired certificate cannot be used to verify a booted
image.

**Test configuration data**

1. `FIRMWARE` = Dasharo.
1. Additional `USB storage` - at least 1GB - for keeping files for booting.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Run script `open-source-firmware-validation/scripts/secure-boot/generate-images/sb-img-wrapper.sh`
    to generate `EXPIRED.img`.
1. Place `open-source-firmware-validation/scripts/secure-boot/images/EXPIRED.img`
    on the `USB storage`.
1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Current Secure Boot State` field to `Enabled`.
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
    signed-hello.efi
    ```

**Expected result**

1. Files do not boot correctly: `Command Error Status: Access Denied`.

## SBO012.001 Boot OS Signed And Enrolled From Inside System (Ubuntu 22.04)

**Test description**

This test verifies that OS boots after enrolling keys and signing system from
inside.

**Test configuration data**

1. `FIRMWARE` = Dasharo.
1. `OPERATING_SYSTEM` = Ubuntu 22.04.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Secure Boot Mode` field to `Custom Mode`.
1. Erase Secure Boot keys select options in the given order: `Custom Secure Boot Options` ->
    `DB Options` -> `Enroll Signature` -> `Erase all Secure Boot Keys`
1. Press `F10` to save changes.
1. Press `ESC` until the setup menu.
1. Select the `Reset` option.
1. The DUT will now attempt to boot `OPERATING_SYSTEM`.
1. Login to `OPERATING_SYSTEM`.
1. Remove Old Secure Boot keys:

    ```bash
    rm -rf /usr/share/secureboot
    ```

    > Note: `root` right might be needed.

1. Generate new Secure Boot keys:

    ```bash
    sbctl create-keys
    ```

    > Note: `root` rights might be needed.

1. Enroll generated Secure Boot keys:

    ```bash
    sbctl enroll-keys --yes-this-might-brick-my-machine
    ```

    > Note: `root` rights might be needed.

1. Sign all components in `OPERATING_SYSTEM`:

    ```bash
    sbctl verify | awk -F ' ' '{print $2}' | tail -n+2 | xargs -I "#" sbctl sign "#"
    ```

    > Note: `root` rights might be needed.

1. Reboot `OPERATING_SYSTEM`.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Current Secure Boot State` field to `Enabled`.
1. Press `F10` to save changes.
1. Press `ESC` until the setup menu.
1. Select the `Reset` option.
1. The DUT will now attempt to boot `OPERATING_SYSTEM`.
1. Login to `OPERATING_SYSTEM`.
1. Check if Secure Boot is enabled:

    ```bash
    dmesg | grep secureboot
    ```

    > Note: `root` rights might be needed.

**Expected result**

1. In `dmesg` output should be a line informing that Secure Boot is enabled.

## SBO013.001 Check automatic certificate provisioning

**Test description**

This test verifies that the automatic certificate provisioning will install
custom keys which will make Ubuntu unbootable. Before launching test, make sure
that DTS with automatic certificate provisioning is attached and can be booted
on DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo.
1. `OPERATING_SYSTEM` = Ubuntu 22.04.
1. Additional `USB storage`for keeping Dasharo Tools Suite.
1. Dasharo Tools Suite with UEFI secure boot support.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the [DTS: Build image with UEFI Secure Boot
    support](../../dasharo-tools-suite/documentation.md#build-image-with-uefi-secure-boot-support).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Secure Boot Mode` field to `Custom Mode`.
1. Erase Secure Boot keys select options in the given order: `Custom Secure Boot Options` ->
    `DB Options` -> `Enroll Signature` -> `Erase all Secure Boot Keys`.
1. Press `F10` to save changes.
1. Press `ESC` until the setup menu.
1. Select the `Reset` option.
1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter the boot menu.
1. Boot Dasharo Tools Suite from `USB Storage`.
1. Wait until Dasharo Tools Suite enrolls keys and resets the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Current Secure Boot State` field to `Enabled`.
1. Press `F10` to save changes.
1. Press `ESC` until the setup menu.
1. Select the `Reset` option.
1. Verify by booting signed Dasharo Tools Suite:
    1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter the boot menu.
    1. Boot Dasharo Tools Suite from `USB Storage`.
1. Reboot the DUT.
1. Verify by booting unsigned Ubuntu:
    1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter the boot menu.
    1. Boot `OPERATING_SYSTEM`.

**Expected result**

1. Signed Dasharo Tools Suite should boot.
1. Unsigned Ubuntu should not boot.

## SBO013.002 Check automatic certificate provisioning KEK certificate

**Test description**

This test verifies that the automatic certificate provisioning installs the
expected KEK certificate. Before launching test, make sure that DTS with
automatic certificate provisioning is attached and can be booted on DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo.
1. `OPERATING_SYSTEM` = Dasharo Tools Suite.
1. Additional `USB storage`for keeping Dasharo Tools Suite.
1. Dasharo Tools Suite with UEFI secure boot support.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the [DTS: Build image with UEFI Secure Boot
    support](../../dasharo-tools-suite/documentation.md#build-image-with-uefi-secure-boot-support).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Secure Boot Mode` field to `Custom Mode`.
1. Erase Secure Boot keys select options in the given order: `Custom Secure Boot Options` ->
    `DB Options` -> `Enroll Signature` -> `Erase all Secure Boot Keys`.
1. Press `F10` to save changes.
1. Press `ESC` until the setup menu.
1. Select the `Reset` option.
1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter the boot menu.
1. Boot Dasharo Tools Suite from `USB Storage`.
1. Wait until Dasharo Tools Suite enrolls keys and resets the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Current Secure Boot State` field to `Enabled`.
1. Press `F10` to save changes.
1. Press `ESC` until the setup menu.
1. Select the `Reset` option.
1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter the boot menu.
1. Boot Dasharo Tools Suite from `USB Storage`.
1. Enter shell in Dasharo Tools Suite by pressing `9`.
1. Compare the current KEK certificate with the certificate that should be
    enrolled:
    1. Download the sample certificate:

        ```bash
        wget https://cloud.3mdeb.com/index.php/s/FGdaGq2QqnGWQew/download/KEK.crt -O /tmp/first_certificate.crt
        ```

    1. Convert the sample certificate:

        ```bash
        openssl x509 -in /tmp/first_certificate.crt -noout -text > /tmp/first_certificate.crt
        ```

    1. Export already enrolled certificate:

        ```bash
        mokutil --kek > /tmp/second_certificate.crt
        ```

    1. Compare the certificates:

        ```bash
        diff /tpm/first_certificate.crt /tmp/second_certificate.crt
        ```

**Expected result**

1. The data provided by both certificates should be equal, the form of the
compared data might differ.

## SBO014.001 Enroll certificates using sbctl

**Test description**

This test erases Secure Boot keys from the BIOS menu and verifies if new keys
can be enrolled from the operating system using `sbctl`.

**Test configuration data**

1. `FIRMWARE` = Dasharo.
1. `OPERATING_SYSTEM` = Ubuntu 22.04.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Secure Boot Mode` field to `Custom Mode`.
1. Erase Secure Boot keys select options in the given order: `Custom Secure Boot Options` ->
    `DB Options` -> `Enroll Signature` -> `Erase all Secure Boot Keys`
1. Press `F10` to save changes.
1. Press `ESC` until the setup menu.
1. Select the `Reset` option.
1. The DUT will now attempt to boot `OPERATING_SYSTEM`.
1. Login to `OPERATING_SYSTEM`.
1. Remove old Secure Boot keys:

    ```bash
    rm -rf /usr/share/secureboot
    ```

    > Note: `root` rights might be needed.

1. Generate new Secure Boot keys:

    ```bash
    sbctl create-keys
    ```

    > Note: `root` rights might be needed.

1. Enroll generated Secure Boot keys:

    ```bash
    sbctl enroll-keys --yes-this-might-brick-my-machine
    ```

    < Note: `root` rights might be needed.

1. Restart the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Current Secure Boot State` field to `Enabled`.
1. Press `F10` to save changes.
1. Press `ESC` until the setup menu.
1. Select the `Reset` option.

**Expected result**

1. You should not be able to boot the system after enrolling the keys and
enabling Secure Boot.

## SBO015.001 Attempt to enroll the key in the incorrect format (OS)

**Test description**

This test verifies that it is impossible to load a certificate in the wrong file
format from the operating system while using `sbctl`.

**Test configuration data**

1. `FIRMWARE` = Dasharo.
1. `OPERATING_SYSTEM` = Ubuntu 22.04.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI setup
    menu.
1. Enter the `Device Manager` menu using the arrow keys and Enter.
1. Enter the `Secure Boot Configuration` submenu.
1. Set the `Secure Boot Mode` field to `Custom Mode`.
1. Erase Secure Boot keys select options in the given order: `Custom Secure Boot Options` ->
    `DB Options` -> `Enroll Signature` -> `Erase all Secure Boot Keys`
1. Press `F10` to save changes.
1. Press `ESC` until the setup menu.
1. Select the `Reset` option.
1. The DUT will now attempt to boot `OPERATING_SYSTEM`.
1. Login to `OPERATING_SYSTEM`.
1. Remove Old Secure Boot keys:

    ```bash
    rm -rf /usr/share/secureboot
    ```

    > Note: `root` rights might be needed.

1. Generate new Secure Boot keys:

    ```bash
    sbctl create-keys
    ```

    > Note: `root` rights might be needed.

1. Generate wrong format keys and move them to the appropriate locations::

    ```bash
    openssl ecparam -genkey -name secp384r1 -out db.key && openssl req -new -x509 -key db.key -out db.pem -days 365 -subj "/CN=3mdeb_test"
    openssl ecparam -genkey -name secp384r1 -out PK.key && openssl req -new -x509 -key PK.key -out PK.pem -days 365 -subj "/CN=3mdeb_test"
    openssl ecparam -genkey -name secp384r1 -out KEK.key && openssl req -new -x509 -key KEK.key -out KEK.pem -days 365 -subj "/CN=3mdeb_test"
    mv db.key /usr/share/secureboot/keys/db/
    mv PK.key /usr/share/secureboot/keys/PK/
    mv KEK.key /usr/share/secureboot/keys/KEK/
    ```

    > Note: `root` rights might be needed.

1. Attempt to enroll generated Secure Boot keys:

    ```bash
    sbctl enroll-keys --yes-this-might-brick-my-machine
    ```

    > Note: `root` rights might be needed.

**Expected result**

1. `sbctl` should fail while enrolling keys.
