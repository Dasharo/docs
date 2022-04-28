# Dasharo Compatibility: SD Card Reader

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup#os-boot-from-disk).
1. Insert an SD card into the SD Card reader.

### SDC001.001 SD Card reader detection (Ubuntu 20.04)

**Test description**

This test aims to verify that the SD Card reader is enumerated correctly and
can be detected from the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the follwing command:

```bash
lspci | grep RTS522A
```

**Expected result**

The output from the command should contain the line:

```bash
2d:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS522A PCI Express Card Reader (rev 01)
```

### SDC001.002 SD Card reader detection (Windows 11)

**Test description**

This test aims to verify that the SD Card reader is enumerated correctly and
can be detected from the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open PowerShell as administrator.
1. Run below command and note result:

    ```powershell
    Get-PnpDevice -Status "OK" -Class "MTD"
    ```

**Expected result**

1. Command should output at least one card reader.

### SDC002.001 SD Card read/write (Ubuntu 20.04)

**Test description**

This test aims to verify that the SD Card reader is initialized correctly and
can be used from the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following commands as root:

```bash
dd if=/dev/urandom of=/tmp/in.bin bs=4K count=100
dd if=/tmp/in.bin of=/dev/mmcblk0 bs=4K count=100
dd if=/dev/mmcblk0 of=/tmp/out.bin bs=4K count=100
sha256sum /tmp/in.bin /tmp/out.bin
```

**Expected result**

The output from the last command should contain 2 indentical checksums:

```bash
2083776668ed0c8095a9ac42188153c02f360e116c14b36d2ef5c98665d75dcb  /tmp/in.bin
2083776668ed0c8095a9ac42188153c02f360e116c14b36d2ef5c98665d75dcb  /tmp/out.bin
```

### SDC002.002 SD Card read/write (Windows 11)

**Test description**

This test aims to verify that the SD Card reader is initialized correctly and
can be used from the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open PowerShell as administrator.
1. Run below commands and note results:

    ```powershell
    New-Item -Path "F:\" -Name "testfile.txt" -ItemType "file" -Value "This is a test string."
    Get-Content -Path "F:\testfile.txt"
    ```

**Expected result**

Last command should return `This is a test string.`
