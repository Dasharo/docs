# Dasharo Compatibility: Debian Stable and Ubuntu LTS support

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

### LBT001.001 Debian stable installation on USB storage

**Test description**

This test verifies that Debian stable distribution could be installed on USB
storage on the DUT via iPXE.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Debian 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Install system via iPXE on USB storage.

**Expected result**

The information about succesfull installation should be displayed.

### LBT001.002 Boot Debian from USB

**Test description**

This test verifies that Debian stable ditribution could be booted from USB
storage on the DUT.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Debian 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the `USB_STORAGE` on which the system was
    previously installed.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.

### LBT002.001 Ubuntu LTS installation on USB storage

**Test description**

This test verifies that Ubuntu LTS modern distribution could be installed on USB
storage on the DUT via iPXE.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Install system via iPXE on USB storage.

**Expected result**

The information about succesfull installation should be displayed.

### LBT002.002 Boot Ubuntu from USB

**Test description**

This test verifies that Ubuntu LTS modern ditribution could be booted from USB
storage on the DUT.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the `USB_STORAGE` on which the system was
    previously installed.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.

### LBT003.001 Debian stable installation on Hard Disk

**Test description**

This test verifies that Debian stable distribution could be installed on hard
disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Debian 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).

**Expected result**

The information about succesfull installation should be displayed.

### LBT003.002 Boot Debian from Hard Disk

**Test description**

This test verifies that Debian stable distribution could be booted from hard
disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Debian 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the hard disk on which the system was previously
    installed.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.

### LBT004.001 Ubuntu LTS installation on Hard Disk

**Test description**

This test verifies that Ubuntu LTS modern ditribution could be installed on hard
disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).

**Expected result**

The information about succesfull installation should be displayed.

### LBT004.002 Boot Ubuntu From Hard Disk

**Test description**

This test verifies that Ubuntu LTS modern ditribution could be booted from hard
disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the hard disk on which the system was previously
    installed.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.
