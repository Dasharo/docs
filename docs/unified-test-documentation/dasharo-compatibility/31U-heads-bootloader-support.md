# Dasharo Compatibility: Heads bootloader support

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

## HDS001.001 Heads installation

**Test description**

This test aims to verify that Heads could be installed on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Flash bootkernel partition with Heads in accordance with the
    [documentation](../../variants/talos_2/initial-deployment.md#heads-installation).

**Expected result**

The output of the `pflash` command should contain information, that flashing
procedure has been ended without any errors.

Example output:

```bash
Programming & Verifying...
[==================================================] 100% ETA:0s
```

## HDS002.001 Boot into Heads

**Test description**

This test aims to verify that the DUT during the booting procedure reaches
Heads bootloader.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Heads` to boot and note the result.

**Expected result**

The `Heads` bootloader screen should be displayed.

## HDS003.001 Boot from USB option is available and works correctly

**Test description**

This test aims to verify that the `Boot from USB` option in the
`Default boot menu` is available (if there is no option to boot OS from the
Hard Disk) and allows to boot system mounted on the USB.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. `USB storage` with the installed OS.

**Test steps**

1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select `Boot from USB` option using the arrow keys and Enter.
1. Select a partition from the `USB storage` from which the system will be
    booted.
1. Note the results.

**Expected result**

The operating system from `USB storage` should boot properly.

## HDS004.001 Continue to the main menu option is available and works correctly

**Test description**

This test aims to verify that the `Continue to the main menu` option in the
`Default boot menu` is available and works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Note the results.

**Expected result**

After selecting `Continue to the main menu`, the `Heads Boot Menu` should be
displayed.

## HDS005.001 Exit to recovery shell option is available and works correctly

**Test description**

This test aims to verify that the `Exit to recovery shell` option in the
`Default boot menu` is available and works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Exit to recovery shell` option using the arrow keys and Enter.
1. Note the results.

**Expected result**

After selecting `Exit to recovery shell`, the recovery shell should be shown.

Example output:

```bash
!!!!! User requested recovery shell
!!!!! Starting recovery shell
~ #
```

## HDS006.001 Default boot option is available and works correctly

**Test description**

This test aims to verify that the `Default boot` option in the `Heads boot menu`
is available and works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Default boot` option in the `Heads boot menu`.
1. Note the results.

**Expected result**

After selecting `Default boot`, the `Default boot menu` should be displayed.

## HDS007.001 Options submenu is available and works correctly

**Test description**

This test aims to verify that the `Options -->` option in the `Heads boot menu`
is available and works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Note the results.

**Expected result**

After selecting `Options -->`, the `HEADS Options` menu should be displayed.

Example view of `HEADS Options`:

```bash
b  Boot Options -->
t  TPM/TOTP/HOTP Options -->
u  Update checksums and sign all files in /boot
c  Change configuration settings -->
f  Flash/Update the BIOS -->
g  GPG Options -->
F  OEM Factory Reset -->
x  Exit to recovery shell
r  <-- Return to main menu
```

## HDS008.001 System info option is available and works correctly

**Test description**

This test aims to verify that the `System Info` option in the `Heads boot menu`
allows displaying all basic system information.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `System Info` option in the `Heads boot menu`.
1. Note the results.

**Expected result**

After selecting `System Info`, the basic system information should be displayed.

Example output:

```bash
┌─────────────────────┤ System Info ├──────────────────────┐
│                                                          │
│ Talos 2 Server                                           │
│                                                          │
│ FW_VER: v0.5.0                                           │
│ Kernel: Linux 5.5.0-openpower1                           │
│                                                          │
│ CPU: IBM POWER9 “Sforza”                                 │
│ RAM: 8 GB                                                │
│                                                          │
│ Disk /dev/nvme0n1: 477 GB                                │
│                                                          │
│                                                          │
│                          <Ok>                            │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## HDS009.001 Power off option is available and works correctly

**Test description**

This test aims to verify that the `Power Off` option in the `Heads boot menu`
allows turning off the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Power Off` option in the `Heads boot menu`.
1. Note the results.

**Expected result**

After selecting `Power Off`, the DUT should be turned off without any
complications.

## HDS010.001 OEM Factory Reset option is available and works correctly

**Test description**

This test aims to verify that the `OEM Factory Reset / Re-Ownership -->` option
in the `HEADS Options` submenu is available and works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `USB Security Dongle`
1. Previously installed OS

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Plug the `USB Security Dongle` into DUT.
1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `OEM Factory Reset / Re-Ownership -->` option in the
   `HEADS Options` submenu.
1. Choose `<Continue>` in the displayed `OEM Factory Reset / Re-Ownership`
   window using the arrow keys and Enter.
1. Go through the installation process by answering the questions.
1. Note the results.

**Expected result**

1. The `Provisioned Security Components Secrets` should be displayed at the end
   of the installation.
1. The new GPG keys should be placed on the `USB Security Dongle`.

## HDS011.001 Add GPG key to running BIOS and reflash

**Test description**

This test aims to verify that the `Add GPG key to running BIOS and reflash`
option in the `GPG Management Menu` is available and works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. Additional `USB storage` - at least 1GB, with GPG public key

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `GPG Options -->` option in the `HEADS Options` submenu.
1. Select the `Add GPG key to running BIOS and reflash` option in the
   `GPG Management Menu`.
1. Choose `<Yes>` in the displayed `GPG public key required` window using the
   arrow keys and Enter.
1. Choose GPG public key from the `USB storage` and press Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `GPG Options -->` option in the `HEADS Options` submenu.
1. Select the `List GPG keys in your keyring` option in the
   `GPG Management Menu`.
1. Note the results.

**Expected result**

The `GPG Keyring` window should contain information about the given GPG key.

## HDS012.001 Add GPG key to standalone BIOS image and flash

**Test description**

This test aims to verify that the
`Add GPG key to standalone BIOS image and flash` option in the
`GPG Management Menu` is available and works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. Additional `USB storage` - at least 1GB, with GPG public key and BIOS image

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `GPG Options -->` option in the `HEADS Options` submenu.
1. Select the `Add GPG key to standalone BIOS image and flash` option in the
   `GPG Management Menu`.
1. Choose `<Yes>` in the displayed `GPG public key required` window using the
   arrow keys and Enter.
1. Choose GPG public key from the `USB storage` and press Enter.
1. Choose BIOS image(*.rom) from the `USB storage` and press Enter.
1. Choose `<Yes>` in the displayed `Flash ROM?` window using the arrow keys and
   Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `GPG Options -->` option in the `HEADS Options` submenu.
1. Select the `List GPG keys in your keyring` option in the
   `GPG Management Menu`.
1. Note the results.

**Expected result**

The `GPG Keyring` window should contain information about the given GPG key.

## HDS013.001 Replace GPG key(s) in the current ROM and reflash

**Test description**

This test aims to verify that the
`Replace GPG key(s) in the current ROM and reflash` option in the
`GPG Management Menu` is available and replaces GPG keys correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. Additional `USB storage` - at least 1GB, with GPG public key

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Plug the `USB storage` into DUT.
1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `GPG Options -->` option in the `HEADS Options` submenu.
1. Select the `Replace GPG key(s) in the current ROM and reflash` option in the
   `GPG Management Menu`.
1. Choose `<Yes>` in the displayed `GPG public key required` window using the
   arrow keys and Enter.
1. Choose GPG public key from the `USB storage` and press Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `GPG Options -->` option in the `HEADS Options` submenu.
1. Select the `List GPG keys in your keyring` option in the
   `GPG Management Menu`.
1. Note the results.

**Expected result**

The `GPG Keyring` window should contain information about the given GPG key.

## HDS014.001 List GPG keys in your keyring

**Test description**

This test aims to verify that the `List GPG keys in your keyring` option in the
`GPG Management Menu` is available and listed GPG keys correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `GPG Options -->` option in the `HEADS Options` submenu.
1. Select the `List GPG keys in your keyring` option in the
   `GPG Management Menu`.
1. Note the results.

**Expected result**

1. The `GPG Keyring` window should contain information about the GPG key if any
   was added.

    Example information in the `GPG Keyring` window:

    ```bash
    //.gnupg/pubring.kbx
    --------------------
    pub   rsa3072 2022-11-22 [SC]
          AFA824E4660A265253BA1571B640E02380808C34
    uid          [ultimate] OEM Key (OEM-generated key) <oem-20221122083831@example.co
    sub   rsa3072 2022-11-22 [A]
    sub   rsa3072 2022-11-22 [E]
    ```

1. The `GPG Keyring` window should be empty if no key has been added.

## HDS015.001 Export public GPG key to USB drive

**Test description**

This test aims to verify that the `Export public GPG key to USB drive` option in
the `GPG Management Menu` is available and exports GPG keys correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. Additional `USB storage` - at least 1GB

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `GPG Options -->` option in the `HEADS Options` submenu.
1. Select the `Export public GPG key to USB drive` option in the
   `GPG Management Menu`.
1. Choose `<Yes>` in the displayed `Export Public Key(s) to USB drive?` window
   using the arrow keys and Enter.
1. Note the results.

**Expected result**

1. `The GPG Key Copied Successfully` window should be displayed.
1. The `public-key.asc` file should be on `USB storage`.

## HDS016.001 Generate GPG keys manually on a USB security token

**Test description**

This test aims to verify that the
`Generate GPG keys manually on a USB security token` option in the
`GPG Management Menu` is available and works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `USB Security Dongle`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Plug the `USB Security Dongle` into DUT.
1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `GPG Options -->` option in the `HEADS Options` submenu.
1. Select the `Generate GPG keys manually on a USB security token` option in the
   `GPG Management Menu`.
1. Confirm that the `USB Security Dongle` is inserted, type `Y` and press Enter.
1. Wait for `gpg/card>` prompt is appeared.
1. Type `admin` and press Enter.
1. Type `generate` and press Enter.
1. Answer `y` to question `Replace existing keys?`.
1. Note the results.

**Expected result**

1. Information about the successful generation of GPG keys should be displayed.
1. The new GPG keys are on the `USB Security Dongle`.

## HDS017.001 Clear GPG key(s) and reset all user settings

**Test description**

This test aims to verify that the
`Clear GPG key(s) and reset all user settings` option in the
`Config Management Menu` is available and works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `Change configuration settings -->` option in the `HEADS Options`
   submenu.
1. Select the `Clear GPG key(s) and reset all user settings` option in the
   `Config Management Menu`.
1. Choose `<Yes>` in the displayed `Reset Configuration?` window using the
   arrow keys and Enter.
1. Reboot the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `GPG Options -->` option in the `HEADS Options` submenu.
1. Select the `List GPG keys in your keyring` option in the
   `GPG Management Menu`.
1. Note the results.

**Expected result**

The `GPG Keyring` window should be empty.

## HDS018.001 Reset TPM option is available and works correctly

**Test description**

This test aims to verify that the `Reset TPM` option in the
`TPM/TOTP/HOTP Options` submenu is available and works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `TPM/TOTP/HOTP Options -->` option in the `HEADS Options` submenu.
1. Select the `Reset the TPM` option in the `TPM/TOTP/HOTP Options` submenu.
1. Choose `<Yes>` in the displayed `Reset the TPM` window using the arrow keys
   and Enter.
1. Set the TPM owner password.
1. Scan the QR code using a mobile application to add the new TOTP secret and
   press Enter.
1. Reboot the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.

**Expected result**

After selecting the `Continue to the main menu` option, should be prompted for
the TPM owner password.

## HDS019.001 Generate new TOTP/HOTP secret

**Test description**

This test aims to verify that the `Generate new TOTP/HOTP secret` option in the
`TPM/TOTP/HOTP Options` submenu is available and works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.
1. Select the `Options -->` option in the `Heads boot menu`.
1. Select the `TPM/TOTP/HOTP Options -->` option in the `HEADS Options` submenu.
1. Select the `Generate new TOTP/HOTP secret` option in the
   `TPM/TOTP/HOTP Options` submenu.
1. Scan the QR code using a mobile application to add the new TOTP secret and
   press Enter.
1. Reboot the DUT.
1. Wait for the `Default boot menu` appears.
1. Select the `Continue to the main menu` option using the arrow keys and Enter.

**Expected result**

After selecting the `Continue to the main menu` option, should be prompted for
the TOTP password.
