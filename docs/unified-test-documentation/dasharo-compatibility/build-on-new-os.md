# Dasharo Compatibility: Building from source on a newly installed OS works

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).

## BNO001.001 Build on a Newly installed OS (Ubuntu)

**Test description**

This test aims to verify that Dasharo is buildable on freshly installed Ubuntu.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test steps**
1. If the Ubuntu on the device is not freshly installed, install a clean one.
Use an autoinstaller [Preseeds](https://github.com/dasharo/preseeds) as
suggested in [Generic Test Setup](../generic-test-setup.md#os-installer)
1. Boot into Ubuntu
1. Build the Dasharo firmware for the DUT following the build instructions
from docs.dasharo.com documentation for this device. For example
[Novacustom building manual](../../unified/novacustom/building-manual.md)
in the case of testing on a Novacustom laptop.

**Expected result**
The build process should result in creating a rom file.

## BNO001.002 Boot (Ubuntu)

**Test description**

This test aims to verify that Ubuntu Linux is bootable with the firmware built
using the instructions at docs.dasharo.com.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test steps**
1. Flash the firmware built on a newly installed OS using the
instructions for the device from docs.dasharo.com. For example
[Novacustom firmware update](../../unified/novacustom/firmware-update.md)
in the case of testing on a Novacustom laptop.
1. Power on the DUT.
1. Boot into Ubuntu.

**Expected result**
There was no message that the device booted from recovery.
The OS boots properly.
