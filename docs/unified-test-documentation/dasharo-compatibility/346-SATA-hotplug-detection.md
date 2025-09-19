# Dasharo compatibility: SATA hot plug

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

## SHT001.001 SATA hot plug (firmware)

**Test description**

This test aims to verify that the disk connected to the SATA port could be
detected after hot-plug.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Any operating system should be installed on the SATA disk.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `UEFI Shell` option using the arrow keys and press `Enter`.
1. Execute the following command in the shell:

    ```bash
    map -t hd
    ```

1. Note the results.
1. Connect the disk to the SATA port.
1. Execute the following command in the shell:

    ```bash
    map -t hd -r
    ```

**Expected result**

1. The output of the first command should contain mapping table for all hard
    disks connected to the device.
1. The output of the second command should contain refreshed mapping table for
    all hard disks connected to the device.
1. The refreshed list should contain additional item - mounted SATA disk.

## SHT001.002 SATA hot plug (Ubuntu)

**Test description**

This test aims to verify that the disk connected to the SATA port could be
detected after hot-plug.

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
1. Connect the disk to the SATA port.
1. Check that the connected disk is detected by running the following command:

    ```bash
    sudo parted -l
    ```

1. Note the results.

**Expected result**

The SATA disk should be detected in OS, example output:

```bash
(...)
Model: ATA SSDPR-CL100-240- (scsi)
Disk /dev/sda: 240GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:

Number  Start   End     Size    File system  Name                  Flags
 1      1049kB  538MB   537MB   fat32        EFI System Partition  boot, esp
 2      538MB   240GB   240GB   ext4
(...)
```

## SHT001.003 SATA hot plug (Windows)

**Test description**

This test aims to verify that the disk connected to the SATA port could be
detected after hot-plug.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect the disk to the SATA port.
1. Check that the connected disk is detected by running the following command:

    ```powershell
    Get-WMIObject -Class Win32_DiskDrive
    ```

1. Note the results.

**Expected result**

The SATA disk should be detected in OS, example output:

```powershell
(...)
Partitions : 4
DeviceID   : \\.\PHYSICALDRIVE0
Model      : SSDPR-CL100-240-G2
Size       : 240054796800
Caption    : SSDPR-CL100-240-G2
(...)
```
