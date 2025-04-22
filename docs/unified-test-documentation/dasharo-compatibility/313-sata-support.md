# Dasharo compatibility: SATA Support

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

## SAT001.0XX SATA support (Linux generic)

**Test setup**

1. Insert a SATA storage device (e.g., SSD or HDD) into the SATA port on the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Run the following command:

    ```bash
    lsblk
    ```

1. Identify the SATA device in the list (e.g., `/dev/sda`, `/dev/sdb`, etc.).
1. Run the following command to verify the device is recognized and functional:

    ```bash
    smartctl -i /dev/sdX
    ```

    Replace `/dev/sdX` with the correct device path.

**Expected result**

1. The SATA device appears in the output of `lsblk` as a block device.
1. The output of `smartctl -i` shows valid device identification, similar to
    the following:

    ```text
    Device Model:     SSDPR-CX400-256-G2
    Serial Number:    410039098
    Firmware Version: HDFED3.2
    SATA Version:     SATA 3.2, 6.0 Gb/s (current: 6.0 Gb/s)
    SMART support is: Available - device has SMART capability.
    SMART support is: Enabled
    ```

## SAT001.001 SATA support (Ubuntu)

Follows the [generic SAT001.0XX Linux-based test case](#sat0010xx-sata-support-linux-generic)

## SAT001.010 SATA support (XCP-NG)

Follows the [generic SAT001.0XX Linux-based test case](#sat0010xx-sata-support-linux-generic)

## SAT001.011 SATA support (ESXi)

**Test setup**

1. Insert a SATA storage device (e.g., SSD or HDD) into the SATA port on the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the ESXi system.
1. Log into the ESXi host using the DCUI, SSH, or via remote console.
1. Run the following command to list available storage devices:

    ```bash
    esxcli storage core device list
    ```

1. Identify the SATA device by looking for the appropriate model, vendor, or type.
1. (Optional) Run the following command to query SMART data (if supported and available):

    ```bash
    esxcli storage core device smart get -d <DeviceName>
    ```

    Replace `<DeviceName>` with the appropriate device identifier (e.g., `t10.ATA_____...`).

**Expected result**

1. The SATA device is listed in `esxcli storage core device list`.
1. SMART data (if supported) shows valid identification details such as:

    ```text
    Model: SSDPR-CX400-256-G2
    Serial Number: 410039098
    Firmware Revision: HDFED3.2
    ```
