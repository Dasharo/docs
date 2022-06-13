# Dasharo Security: Verified Boot support

## Test cases

### VBO001.001 Verified boot support (firmware)

**Test description**

Verified Boot is a method of verifying that the firmware components come from a
trusted source. This test aims to confirm that verified boot is enabled and
functional.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
1. Read coreboot loading logs.

**Expected result**

The logs should indicate that vboot is enabled and verstage has been entered:

```text
VBOOT: Loading verstage.
```

### VBO001.002 Verified boot support (Ubuntu 20.04)

**Test description**

Verified Boot is a method of verifying that the firmware components come from a
trusted source. This test aims to confirm that verified boot is enabled and
functional.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).
1. Download `cbmem` and `flashrom` from <https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd>
    to the DUT.
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the follwing command:

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

### VBO002.001 Verified boot: Booting from Slot A (firmware)

**Test description**

If the signatures for firmware stored in vboot Slot A are correct, vboot should
proceed to boot from Slot A.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
1. Read coreboot loading logs.

**Expected result**

The logs should indicate that vboot has chosen to boot from slot A:

```text
Slot A is selected
```

### VBO002.002 Verified boot: Booting from Slot A (Ubuntu 20.04)

**Test description**

If the signatures for firmware stored in vboot Slot A are correct, vboot should
proceed to boot from Slot A.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).
1. Download `cbmem` and `flashrom` from <https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd>
   to the DUT.
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the follwing command:

```bash
sudo ./cbmem -c | grep "Slot A"
```

**Expected result**

The output of the command should indicate that vboot has chosen to boot from
slot A:

```text
Slot A is selected
```

### VBO003.001 Verified boot: Booting from Recovery (Ubuntu 20.04)

**Test description**

If the signatures for firmware stored in vboot Slot A are incorrect, vboot
should revert to booting from the recovery slot.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).
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
1. Open a terminal window and execute the follwing command:

```bash
sudo ./cbmem -c | grep -i recovery
```

1. If booting into the system is impossible, read coreboot loading logs.

**Expected result**



### VBO004.001 Recovery boot popup (firmware)

**Test description**

The test checks whether the information about recovery mode will be displayed 
after flash firmware with wrong vboot keys.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Disable Secure Boot.

**Test steps**


**Expected result**

The information about recovery mode should be displayed.

### VBO005.001  Recovery boot popup confirmation (firmware)

**Test description**

The test checks the functionality of confirming the popup: 
If we press Enter, we should immediately move to the next stages of booting.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Disable Secure Boot.

**Test steps**


**Expected result**

After pressing Enter the DUT should immediately move to the next stages of 
booting.
