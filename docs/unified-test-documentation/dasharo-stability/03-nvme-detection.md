# Dasharo Stability: NVMe detection

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
   [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
   [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
   [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).

## SNV0001.001 NVMe detection after cold boot (Ubuntu 22.04)

**Test description**

This test aims to verify that the NVMe disk is correctly detected after
performing a cold boot. The test should be performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

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

## SNV0001.001 NVMe detection after warm boot (Ubuntu 22.04)

**Test description**

This test aims to verify that the NVMe disk is correctly detected after
performing a warm boot. The test is performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

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

1. Power off the DUT using the power button.
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

## SNV0003.001 NVMe detection after reboot (Ubuntu 22.04)

**Test description**

This test aims to verify that the NVMe disk is correctly detected after
performing a reboot. The test is performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../generic-test-setup#firmware)

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

## SNV0004.001 NVMe detection after suspension (Ubuntu 22.04)

**Test description**

This test aims to verify that the NVMe disk is correctly detected after
performing suspension. The test is performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the [Firmware test suite](https://wiki.ubuntu.com/FirmwareTestSuite)
   package.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lspci | grep -i nvme
    ```

1. Execute the following command to suspend the system and automatically wake it
   up after 10 seconds:

    ```bash
    sudo fwts s3 --s3-sleep-delay=10
    ```

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
