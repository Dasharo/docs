# Dasharo Performance: coreboot boot measure

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS preparation](../generic-test-setup.md#os-preparation).
1. Proceed with the
   [Generic test setup: OS post installation steps](../generic-test-setup.md#post-installation).gi
1. Download `cbmem` from the
    [cloud](https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd) to the DUT.
1. Disable Secure Boot.

## CBMEM001.201 coreboot booting time measure after coldboot (Ubuntu)

**Test description**

This test aims to verify whether the DUT boots after coldboot and how long this
process takes. This test case may be re-done several times to to average the
results and specify the platform stability.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Download `cbmem` from the
    [cloud](https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd) to the DUT.
1. Disable Secure Boot.

**Test steps**

1. Open a terminal window and execute the following command:

```bash
sudo ./cbmem -T
```

**Expected result**

The output of the command should contain the information about duration of
all boot stages.

## CBMEM002.201 coreboot booting time measure after warmboot (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## CBMEM003.201 coreboot booting time measure after system reboot (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop
