# Dasharo compatibility: SATA hot-plug detection

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

## SHT001.001 SATA hot-plug detection (firmware)

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
1. Connect the disk to the SATA port.
1. Press `ESC` to go to Setup Menu.
1. Select the `One Time Boot` position using arrows and click `Enter`.
1. Note the results.

**Expected result**

The position with the name of the connected SATA disk should be displayed in the
Boot Menu.

## SHT001.002 SATA hot-plug detection (Ubuntu 22.04)

**Test description**

This test aims to verify that the disk connected to the SATA port could be
detected after hot-plug.

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

## SHT001.003 SATA hot-plug detection (Windows 11)

**Test description**

This test aims to verify that the disk connected to the SATA port could be
detected after hot-plug.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11

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
