# Dasharo Security: Verified Boot support

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

## VBO006.001 Verified boot support (firmware)

**Test description**

Verified Boot is a method of verifying that the firmware components come from a
trusted source. This test aims to confirm that verified boot is enabled and
functional.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
1. Read coreboot loading logs.

**Expected result**

The logs should indicate that vboot is enabled and verstage has been entered:

```text
VBOOT: Loading verstage.
```

## VBO006.002 Verified boot support (Ubuntu)

**Test description**

Verified Boot is a method of verifying that the firmware components come from a
trusted source. This test aims to confirm that verified boot is enabled and
functional.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Download `cbmem` and `flashrom` from <https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd>
    to the DUT.
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

```bash
sudo ./cbmem -c | grep VBOOT
```

**Expected result**

The output of the command should indicate that vboot is enabled and verstage
has been entered:

```text
VBOOT: Loading verstage.
TPM: Extending digest for VBOOT: boot mode into PCR 0
TPM: Extending digest for VBOOT: GBB HWID into PCR 1
VBOOT WORK  8. 0x76c05000 0x00014000
PCR-0 2547cc736e951fa4919853c43ae890861a3b3264000000000000000000000000 SHA256 [VBOOT: boot mode]
PCR-1 e3324765a25f8a59c7c20cc35c1c33a8ab384159d2b40a269246b0b4491cdf89 SHA256 [VBOOT: GBB HWID]
```

## VBO007.001 Verified boot: Booting from Slot A (firmware)

**Test description**

If the signatures for firmware stored in vboot Slot A are correct, vboot should
proceed to boot from Slot A.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
1. Read coreboot loading logs.

**Expected result**

The logs should indicate that vboot has chosen to boot from slot A:

```text
Slot A is selected
```

## VBO007.002 Verified boot: Booting from Slot A (Ubuntu)

**Test description**

If the signatures for firmware stored in vboot Slot A are correct, vboot should
proceed to boot from Slot A.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Download `cbmem` and `flashrom` from <https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd>
   to the DUT.
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

```bash
sudo ./cbmem -c | grep "Slot A"
```

**Expected result**

The output of the command should indicate that vboot has chosen to boot from
slot A:

```text
Slot A is selected
```

## VBO008.001 Verified boot: Booting from Recovery (Ubuntu)

**Test description**

If the signatures for firmware stored in vboot Slot A are incorrect, vboot
should revert to booting from the recovery slot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Download `cbmem` and `flashrom` from <https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd>
   to the DUT.
1. Disable Secure Boot.
1. Obtain [coreboot binary](https://cloud.3mdeb.com/index.php/s/DAn2sdk3osSxG8A)
    signed with wrong vboot keys.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Flash coreboot signed with wrong vboot keys by executing the following
command:

    ```bash
    flashrom -p internal --fmap -i RW_SECTION_A -w [coreboot binary]
    ```

1. Power off the DUT
1. Connect to the DUT using the serial port.
1. Power on the DUT
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

    ```bash
    sudo ./cbmem -c | grep -i recovery
    ```

1. If booting into the system is impossible, read coreboot loading logs.

**Expected result**

The logs should indicate that vboot has chosen to boot from the recovery slot.

Example:

```bash
VB2:vb2_check_recovery() Recovery reason from previous boot: 0x3 / 0x3
VB2:vb2_check_recovery() We have a recovery request: 0x3 / 0x0
Recovery requested (1009000e)
```

## VBO009.001 Recovery boot popup (firmware)

**Test description**

This test aims to verify whether the recovery mode information is displayed
as the popup after rebooting the DUT which is flashed with the firmware with
the wrong vboot keys.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Disable Secure Boot.
1. Obtain `coreboot binary` signed with wrong vboot keys.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Flash coreboot signed with wrong vboot keys by executing the following
command:

    ```bash
    flashrom -p internal --fmap -i RW_SECTION_A -w [coreboot binary]
    ```

1. Reboot the DUT.
1. Wait for the popup to appear.

**Expected result**

Popup with information about recovery mode should be displayed.

## VBO010.001  Recovery boot popup confirmation (firmware)

**Test description**

This test aims to verify whether the recovery popup might be confirmed which
allows to proceed to the next booting stages.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Disable Secure Boot.
1. Obtain `coreboot binary` signed with wrong vboot keys.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Flash coreboot signed with wrong vboot keys by executing the following
command:

    ```bash
    flashrom -p internal --fmap -i RW_SECTION_A -w [coreboot binary]
    ```

1. Reboot the DUT.
1. Wait for the popup to appear.
1. Press `ENTER`.

**Expected result**

After pressing `ENTER` the DUT should immediately move to the next stages of
booting.

## VBO011.001 Booting after flashing with valid binary (Ubuntu)

**Test description**

This test aims to verify whether after flashing the DUT with the valid binary,
the DUT will boot correctly from the default slot and no recovery popup will be
displayed.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Download `cbmem` and `flashrom` from <https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd>
   to the DUT.
1. Disable Secure Boot.
1. Slot A is flashed with an binary with wrong-signed vboot keys.
1. Obtain the correct `coreboot binary` appropriate for the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Flash firmware with valid binary by executing the following command:

    ```bash
    flashrom -p internal --fmap -i RW_SECTION_A -w [coreboot binary]
    ```

1. Reboot the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

    ```bash
    sudo ./cbmem -c | grep -i recovery
    ```

**Expected result**

1. Popup with information about recovery mode should not be displayed.
1. The logs should indicate that vboot hasn't chosen to boot from the recovery
   slot. Example output:

    ```bash
    VB2:vb2_check_recovery() Recovery reason from previous boot: 0x0 / 0x0
    ```
