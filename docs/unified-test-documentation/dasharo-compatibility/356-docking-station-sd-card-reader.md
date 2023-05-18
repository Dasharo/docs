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
1. The `USB-C docking station` connected to the USB-C port.
1. The `SD card` put into the slot on the `USB-C docking station`.

## DSD001.001 Docking station SD Card reader detection (Ubuntu 22.04)

**Test description**

This test aims to verify that the SD Card reader built into the docking station
is enumerated correctly and might be detected by the operating system.

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

1. Note the result.

**Expected result**

The output from the command should contain information about the connected USB
SD Card Reader.

Example output:

```bash
Bus 002 Device 007: ID 067b:2733 Prolific Technology, Inc. USB SD Card Reader
```

## DSD001.002 SD Card reader detection (Windows 11)

**Test description**

This test aims to verify that the SD Card reader built into the docking station
is enumerated correctly and can be detected by the operating system.

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
1. Open PowerShell and execute the following command:

    ```PowerShell
    Get-PnpDevice -Status "OK" -Class "DiskDrive"
    ```

1. Note the result.

**Expected result**

The output from the command should contain information about the connected USB
SD Card Reader.

Example output:

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
1. Open a terminal window and execute the following commands to identify the SD
    card mounting point:

    ```bash
    lsblk | grep "sd"
    ```

1. Execute the following commands for generating, copying and comparing
    generated file:

    ```bash
    dd if=/dev/urandom of=/tmp/in.bin bs=4K count=100
    dd if=/tmp/in.bin of=/dev/sda bs=4K count=100
    dd if=/dev/sda of=/tmp/out.bin bs=4K count=100
    sha256sum /tmp/in.bin /tmp/out.bin
    ```

1. Note the result.

**Expected result**

1. The output from the command to identify the SD card mounting point should
    return information about the SD card mounting location.

    Example output:
    
    ```bash
    sda           8:0    1  29,5G  0 disk 
    └─sda1        8:1    1  29,5G  0 part /media/user/DCB0-C7E8
    sdb           8:16   1     0B  0 disk 
    ```

1. The output from the last command should contain 2 identical checksums.

    Example output

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
1. Open PowerShell and execute the following commands:

    ```powershell
    New-Item -Path "${drive_location}:\" -Name "testfile.txt" -ItemType "file" -Value "This is a test string."
    Get-Content -Path "${drive_location}:\testfile.txt"
    ```

1. Note the result.

**Expected result**

The last command should return the following message:  `This is a test string.`
