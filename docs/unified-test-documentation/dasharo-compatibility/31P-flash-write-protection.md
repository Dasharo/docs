# Dasharo Security: Flash write protection

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Make yourself familiar with
    [SPI hardware write protection](../../../variants/asus_kgpe_d16/spi-wp.md).

### HWP001.001 Hardware flash write protection support

**Test description**

This test aims to verify whether the DUT supports hardware write protection
mechanism.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Debian 11.0`

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Open a terminal window and execute the following command:

```bash
sudo ./flashrom -p internal --wp-list
```

**Expected result**

The output of the command should contain the information about lst of
available write protection ranges, exmaple has been shown below:

```bash
Available write protection ranges:
	start=0x00000000 length=0x00000000 (none)
	start=0x00000000 length=0x00001000 (lower 1/2048)
	start=0x007ff000 length=0x00001000 (upper 1/2048)
	start=0x00000000 length=0x00002000 (lower 1/1024)
	start=0x007fe000 length=0x00002000 (upper 1/1024)
	start=0x00000000 length=0x00004000 (lower 1/512)
	start=0x007fc000 length=0x00004000 (upper 1/512)
	start=0x00000000 length=0x00008000 (lower 1/256)
	start=0x007f8000 length=0x00008000 (upper 1/256)
	start=0x00000000 length=0x00020000 (lower 1/64)
	start=0x007e0000 length=0x00020000 (upper 1/64)
	start=0x00000000 length=0x00040000 (lower 1/32)
	start=0x007c0000 length=0x00040000 (upper 1/32)
	start=0x00000000 length=0x00080000 (lower 1/16)
	start=0x00780000 length=0x00080000 (upper 1/16)
	start=0x00000000 length=0x00100000 (lower 1/8)
	start=0x00700000 length=0x00100000 (upper 1/8)
	start=0x00000000 length=0x00200000 (lower 1/4)
	start=0x00600000 length=0x00200000 (upper 1/4)
	start=0x00000000 length=0x00400000 (lower 1/2)
	start=0x00400000 length=0x00400000 (upper 1/2)
	start=0x00000000 length=0x00600000 (lower 3/4)
	start=0x00200000 length=0x00600000 (upper 3/4)
	start=0x00000000 length=0x00700000 (lower 7/8)
	start=0x00100000 length=0x00700000 (upper 7/8)
	start=0x00000000 length=0x00780000 (lower 15/16)
	start=0x00080000 length=0x00780000 (upper 15/16)
	start=0x00000000 length=0x007c0000 (lower 31/32)
	start=0x00040000 length=0x007c0000 (upper 31/32)
	start=0x00000000 length=0x007e0000 (lower 63/64)
	start=0x00020000 length=0x007e0000 (upper 63/64)
	start=0x00000000 length=0x007f8000 (lower 255/256)
	start=0x00008000 length=0x007f8000 (upper 255/256)
	start=0x00000000 length=0x007fc000 (lower 511/512)
	start=0x00004000 length=0x007fc000 (upper 511/512)
	start=0x00000000 length=0x007fe000 (lower 1023/1024)
	start=0x00002000 length=0x007fe000 (upper 1023/1024)
	start=0x00000000 length=0x007ff000 (lower 2047/2048)
	start=0x00001000 length=0x007ff000 (upper 2047/2048)
	start=0x00000000 length=0x00800000 (all)
```

### HWP002.001 Hardware flash write protection enable / disable

**Test description**

This test aims to verify whether there is a possibility to set and erase 
hardware write protection on the DUT.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Debian 11.0`

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Based on [the documentation](../../../variants/asus_kgpe_d16/spi-wp.md)
    erase current write protection.
1. Based on [the documentation](../../../variants/asus_kgpe_d16/spi-wp.md)
    set write protection for a specific range.
1. Execute the following command in the terminal to check the status and the
    range of write protection:

    ```bash
    sudo ./flashrom -p internal --wp-status
    ```

**Expected result**

1. The output of the command should contain the information about protection 
    mode:

    ```bash
    Protection mode: hardware
    ```

1. Protection range: read from the command output and set before should be the
    same.

### CBMEM003.001 Serial boot measure: coreboot booting time after system reboot

**Test description**

This test aims to verify whether the DUT boots after system reboot and how long
this process takes. This test case may be re-done several times to to average
the results and specify the platform stability.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = `Debian 11.0`

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Open a terminal window and execute the following command:

```bash
sudo ./cbmem -T
```

**Expected result**

The output of the command should contain the information about duration of 
all boot stages.
