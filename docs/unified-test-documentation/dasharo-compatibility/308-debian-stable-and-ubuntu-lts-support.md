# Dasharo Compatibility: Debian Stable and Ubuntu LTS support

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

## LBT001.001 Debian Stable installation on USB storage

**Test description**

This test aims to verify that Debian Stable distribution could be installed
on USB storage attached to the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Debian 11

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../../generic-test-setup#os-installer)
    perform the OS installation process. As disk choose the USB stick.

**Expected result**

The information about successful installation should be displayed.

## LBT001.002 Boot Debian from USB

**Test description**

This test aims to verify that Debian Stable distribution could be booted
from USB storage attached to the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Debian 11

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the `USB_STORAGE` on which the system was
    previously installed.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.

## LBT002.001 Ubuntu LTS installation on USB storage

**Test description**

This test aims to verify that Ubuntu LTS modern distribution could be
installed on USB storage attached to the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../../generic-test-setup#os-installer)
    perform the OS installation process. As disk choose the USB stick.

**Expected result**

The information about successful installation should be displayed.

## LBT002.002 Boot Ubuntu from USB

**Test description**

This test aims to verify that Ubuntu LTS modern distribution could be booted
from USB storage attached to the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the `USB_STORAGE` on which the system was
    previously installed.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.

## LBT003.001 Debian Stable installation on Hard Disk

**Test description**

This test aims to verify that Debian Stable distribution could be installed
on the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Debian 11

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../../generic-test-setup#os-installer)
    perform the OS installation process. As disk choose the mounted in the
    DUT Hard Disk.

**Expected result**

The information about successful installation should be displayed.

## LBT003.002 Boot Debian from Hard Disk

**Test description**

This test aims to verify that Debian Stable distribution could be booted from
the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Debian 11

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the hard disk on which the system was previously
    installed.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.

## LBT004.001 Ubuntu LTS installation on Hard Disk

**Test description**

This test aims to verify that Ubuntu LTS modern distribution could be
installed on the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../../generic-test-setup#os-installer)
    perform the OS installation process. As disk choose the mounted in the
    DUT Hard Disk.

**Expected result**

The information about successful installation should be displayed.

## LBT004.002 Boot Ubuntu From Hard Disk

**Test description**

This test aims to verify that Ubuntu LTS modern distribution could be booted
from the hard disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the hard disk on which the system was previously
    installed.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.
