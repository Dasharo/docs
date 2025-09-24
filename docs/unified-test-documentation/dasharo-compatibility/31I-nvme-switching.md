# Dasharo Compatibility: M.2 automatic SATA/NVMe switching support

## MSS001.001 M.2 automatic SATA/NVMe switching support (Ubuntu)

**Test description**

This test aims to verify detection of the NVMe and SATA disk in M.2 hybrid slot
via the Operating System slot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Insert an NVMe disk into the M.2 slot on the DUT.
1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS preparation](../generic-test-setup.md#os-preparation).
1. Proceed with the
   [Generic test setup: OS post installation steps](../generic-test-setup.md#post-installation).

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Open a terminal window and execute `sudo parted -l`.
5. Check if the connected disk is present on the list.
6. Power off the DUT.
7. Replace the NVMe disk with SATA M.2 disk.
8. Repeat steps 1-5.

**Expected result**

1. The NVMe M.2 disk is detected in OS:

    ```bash
    Model: SAMSUNG MZVLB256HBHQ-00000 (nvme)
    Disk /dev/nvme0n1: 256GB
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt
    Disk Flags:

    Number  Start   End     Size    File system  Name                  Flags
     1      1049kB  2097kB  1049kB
     2      2097kB  540MB   538MB   fat32        EFI System Partition  boot, esp
     3      540MB   67,6GB  67,1GB  ext4
     6      67,6GB  126GB   57,9GB  ext4
     4      126GB   193GB   67,7GB  ext4
     5      193GB   256GB   62,9GB  ext4
    ```

2. The SATA M.2 disk is detected in OS:

    ```bash
    Model: ATA Hoodisk SSD (scsi)
    Disk /dev/sda: 32,0GB
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt
    Disk Flags:

    Number  Start   End     Size    File system  Name                  Flags
     1      1049kB  538MB   537MB   fat32        EFI System Partition  boot, esp
     2      538MB   32,0GB  31,5GB  ext4
    ```
