# Dasharo Stability: NVMe detection

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS boot from disk](../generic-test-setup.md#os-boot-from-disk).

## SNV0001.201 NVMe detection after cold boot (Ubuntu)

**Test description**

This test aims to verify that the NVMe disk is correctly detected after
performing a cold boot. The test should be performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lspci | grep -i nvme
    ```

1. Disconnect the power source, and remove the battery if present.
1. Connect power and battery again.
1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lspci | grep -i nvme
    ```

**Expected result**

The output of each `lspci` command should contain information about the mounted
on the DUT NVMe disk. Example output:

```bash
01:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller 980
```

## SNV0001.201 NVMe detection after warm boot (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## SNV0003.201 NVMe detection after reboot (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## SNV0004.201 NVMe detection after suspension (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop
