# Dasharo Compatibility: SD Card Reader

## Test cases

### Common

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../generic-test-setup/#os-installer)
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup/#os-installation)
1. Proceed with the
   [Generic test setup: OS boot from disk](../generic-test-setup/#os-boot-from-disk)
1. Insert an SD card into the SD Card reader

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

1. Open a terminal window and execute the following command:

        lspci | grep RTS522A

**Expected result**

The output from the command should contain the line:

        2d:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS522A PCI Express Card Reader (rev 01)

### SDC001.002 SD Card reader detection (Windows 10)

**Test description**

This test aims to verify that the SD Card reader is enumerated correctly and
can be detected from the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 10

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Open `Device Manager`
1. Find `Memory technology devices` category and expand it
1. In the expanded section, find `Realtek PCIE CardReader` device
1. Double click `Realtek PCIE CardReader` and note the result

**Expected result**

1. `Realtek PCIE CardReader` should be listed in the `Device Manager`
and should not report any error.

### SDC002.001 SD Card read/write (Ubuntu 20.04)

**Test description**

This test aims to verify that the SD Card reader is initialized correctly and
can be used from the operating system

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Open a terminal window and execute the following commands as root:

        dd if=/dev/urandom of=/tmp/in.bin bs=4K count=100
        dd if=/tmp/in.bin of=/dev/mmcblk0 bs=4K count=100
        dd if=/dev/mmcblk0 of=/tmp/out.bin bs=4K count=100
        sha256sum /tmp/in.bin /tmp/out.bin

**Expected result**

The output from the last command should contain 2 indentical checksums:

        2083776668ed0c8095a9ac42188153c02f360e116c14b36d2ef5c98665d75dcb  /tmp/in.bin
        2083776668ed0c8095a9ac42188153c02f360e116c14b36d2ef5c98665d75dcb  /tmp/out.bin

### SDC002.002 SD Card read/write (Windows 10)

**Test description**

This test aims to verify that the SD Card reader is initialized correctly and
can be used from the operating system

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 10

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Open `Windows Explorer` and go to `This PC`
1. Find SD card icon and double click it
1. Click the right mouse button and choose `New` then choose `Text Document`
1. Name the new file and double click the icon to open it in `Notepad`
1. Write any text and press Ctrl+s
1. Close `Notepad`
1. In the `Windows Explorer` use the right mouse button to click icon
   of the SD Card and click `Eject`
1. Remove the SD Card and insert it again
1. Find SD card icon and double click it again
1. Find created text file, double click to open it and note the result

**Expected result**

Saved text should be readable ofter opening saved file in the `Notepad`.
