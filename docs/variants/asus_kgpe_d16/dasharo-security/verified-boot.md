# Dasharo Security: Verified Boot support

## Test cases

### VBO001.001 Verified boot support

**Test description**

Verified Boot is a method of verifying that the firmware compents come from a
trusted source. This test aims to confirm that verified boot is enabled and 
functional.

**Test setup**

1. Proceed with the [Generic test setup: firmware](generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
2. Read coreboot loading logs.

**Expected result**

The logs should indicate that vboot is enabled and verstage has been entered:

```
VBOOT: Loading verstage.
```

### VBO002.001 Verified boot: Booting from Slot A

**Test description**

If the signatures for firmware stored in vboot Slot A are correct, vboot should
proceed to boot from Slot A.

**Test setup**

1. Proceed with the [Generic test setup: firmware](generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
2. Read coreboot loading logs.

**Expected result**

The logs should indicate that vboot has chosen to boot from slot A:

```
Slot A is selected
```

### VBO003.001 Verified boot: Booting from Recovery (Debian)

**Test description**

If the signatures for firmware stored in vboot Slot A are incorrect, vboot
should revert to booting from the recovery slot.

**Test configuration data**

1. `BOOT_MENU_KEY` = `ESC`
2. `BOOT_MENU_STRING` = `Press ESC for boot menu`

**Test setup**

1. Proceed with the [Generic test setup: firmware](generic-test-setup.md#firmware).
2. Obtain [coreboot binary](https://cloud.3mdeb.com/index.php/apps/files/?dir=/projects/kgpe-d16/releases/Dasharo/v0.3.0/testing&fileid=419752)
signed with wrong vboot keys

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Select the proper number for `USB_STICK` option.
5. Wait for `debian login:`.
6. Type `root` login.
7. Wait for `Password:`.
8. Type the proper password.
9. Wait for `root@debian:~#`.
10. Install `flashrom` by `apt-get install flashrom` command.
11. Flash coreboot signed with wrong vboot keys by executing the following 
command:

        flashrom -p internal --fmap -i RW_SECTION_A -w [coreboot binary]

12. Power off the DUT
13. Power on the DUT
14. Read coreboot loading logs.

**Expected result**

The logs should indicate that vboot has chosen to boot from
the recovery slot.

Example:

```
VB2:vb2_check_recovery() Recovery reason from previous boot: 0x3 / 0x3
VB2:vb2_check_recovery() We have a recovery request: 0x3 / 0x0
Recovery requested (1009000e)
```

