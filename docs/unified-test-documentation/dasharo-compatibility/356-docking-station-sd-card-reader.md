# Dasharo Compatibility: SD Card Reader

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup#os-boot-from-disk).
1. Plug the docking station into the laptop's USB - C port.
1. Insert an SD card into the SD Card slot in the docking station.

## DSD001.001 Docking station SD Card reader detection (Ubuntu 22.04)

**Test description**

This test aims to verify that the SD Card reader built into the docking station 
is enumerated correctly and can be detected from the operating system.

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
1. Open a terminal window and execute the following command:

```bash
lsusb | grep "Card Reader"
```

**Expected result**

The output from the command should contain the line:

```bash
Bus 002 Device 007: ID 067b:2733 Prolific Technology, Inc. USB SD Card Reader
```

## DSD001.002 SD Card reader detection (Windows 11)

**Test description**

This test aims to verify that the SD Card reader built into the docking station 
is enumerated correctly and can be detected from the operating system.

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
1. Open PowerShell as administrator.
1. Run below command and note result:

    ```PowerShell
    Get-PnpDevice -Status "OK" -Class "DiskDrive"
    ```

**Expected result**

The output of the command should contain basic information about mounted
disk drives. Look for the lines containing nformation about SD Card Reader:

```powershell
    OK         DiskDrive       Generic- USB3.0 CRW   -SD USB Device
```

or:

```powershell
    OK         DiskDrive       SD Card Reader USB Device
```

## DSD002.001 SD Card read/write (Ubuntu 22.04)

**Test description**

This test aims to verify that the SD Card reader is initialized correctly and
can be used from the operating system.

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
1. Unplug the SD card from SD card slot built into the docking station.
1. Open a terminal window and execute the following command:

```bash
lsblk | grep "sd"
```
Output example:

```bash
sda           8:0    1     0B  0 disk 
sdb           8:16   1     0B  0 disk 
```

1. Next, plug the SD card into the SD card slot built into the docking station
and execute the command again.

Output example:

```bash
sda           8:0    1  29,5G  0 disk 
└─sda1        8:1    1  29,5G  0 part /media/user/DCB0-C7E8
sdb           8:16   1     0B  0 disk 
```

In this case, the inserted SD card is mounted as `sda`.

1. Execute the following commands as root:

```bash
dd if=/dev/urandom of=/tmp/in.bin bs=4K count=100
dd if=/tmp/in.bin of=/dev/sda bs=4K count=100
dd if=/dev/sda of=/tmp/out.bin bs=4K count=100
sha256sum /tmp/in.bin /tmp/out.bin
```

**Expected result**

The output from the last command should contain 2 identical checksums:

```bash
2083776668ed0c8095a9ac42188153c02f360e116c14b36d2ef5c98665d75dcb  /tmp/in.bin
2083776668ed0c8095a9ac42188153c02f360e116c14b36d2ef5c98665d75dcb  /tmp/out.bin
```

## DSD002.002 SD Card read/write (Windows 11)

**Test description**

This test aims to verify that the SD Card reader is initialized correctly and
can be used from the operating system.

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
1. Determine the localization of the mounted SD card.
1. Open PowerShell as administrator.
1. Run below commands and note results:

    ```powershell
    New-Item -Path "${drive_location}:\" -Name "testfile.txt" -ItemType "file" -Value "This is a test string."
    Get-Content -Path "${drive_location}:\testfile.txt"
    ```

**Expected result**

Last command should return `This is a test string.`