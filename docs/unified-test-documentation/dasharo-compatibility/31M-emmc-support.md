# Dasharo Compatibility: eMMC support

## MMC001.001 eMMC support (Ubuntu 22.04)

**Test description**

This test aims to verify detection of the eMMC driver via the Operating System.

**Test configuration data**

1. `FIRMWARE` = coreboot
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
2. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Open a terminal window and execute `sudo parted -l`.
5. Check if the eMMC is present on the list.

**Expected result**

1. The eMMC disk is detected in OS:

    ```bash
    Model: MMC 8GTF4R (sd/mmc)
    Disk /dev/mmcblk0: 7818MB
    Sector size (logical/physical): 512B/512B
    Partition Table: msdos
    Disk Flags:

    Number  Start   End     Size    Type      File system  Flags
     1      1049kB  538MB   537MB   primary   fat32
     2      538MB   1076MB  538MB   primary   fat32        boot, esp
     3      1077MB  7817MB  6740MB  extended
     5      1077MB  7817MB  6740MB  logical   ext4
    ```
