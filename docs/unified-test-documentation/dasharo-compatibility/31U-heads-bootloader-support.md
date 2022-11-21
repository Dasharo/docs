# Dasharo Compatibility: Heads bootloader support

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
2. Make yourself familiar with
    [Heads installation](/variants/talos_2/initial-deployment/#heads-installation).

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
    [documentation](/variants/talos_2/initial-deployment/#heads-installation).

**Expected result**

1. The output of the `pflash` command shouldn't contain any errors.
1. The output of the `pflash` command should contain:

    ```bash
    Programming & Verifying...
    [==================================================] 100% ETA:0s
    ```

## HDS002.001 Boot into Heads

**Test description**

This test aims to verify that the DUT during booting procedure reaches Heads
bootloader.

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
`Default boot menu` allows booting from USB. This option is displayed if there
are no other booting options (i.e. NVME with bootable OS).

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
1. Select the `Boot from USB` option using the arrow keys and Enter.
1. Select a partition from the `USB storage` from which the system will be
    booted.
1. Note the results.

**Expected result**

The operating system on `USB storage` should boot properly.

## HDS004.001 Continue to the main menu option is available and works correctly

**Test description**

This test aims to verify that the `Continue to the main menu` option in the
`Default boot menu` works correctly.

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
`Default boot menu` works correctly.

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
works correctly.

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
works correctly.

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

After selecting `Options -->`, the `HEADS Options` should be displayed.

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
displays all basic system information.

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
turns off the DUT.

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
