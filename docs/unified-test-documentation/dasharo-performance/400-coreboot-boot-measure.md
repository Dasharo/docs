# Dasharo Performance: coreboot boot measure

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Download `cbmem` from https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd
    to the DUT.

### CBMEM001.001  Serial boot measure: coreboot booting time after coldboot

**Test description**

This test aims to verify whether the DUT boots after coldboot and how long this
process takes. This test case may be re-done several times to to average the
results and specify the platform stability.

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

### CBMEM002.001 Serial boot measure: coreboot booting time after warmboot

**Test description**

This test aims to verify whether the DUT boots after warmboot and how long this
process takes. This test case may be re-done several times to to average the
results and specify the platform stability.

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
