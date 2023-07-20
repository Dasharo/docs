# Dasharo Compatibility: Proxmox support

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).

## PVE001.001 Proxmox Virtual Environment stable installation on Hard Disk

**Test description**

This test aims to verify that Proxmox VE stable could be installed on the hard
disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Proxmox VE stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. According to the [Documentation](../generic-test-setup.md#os-installer)
   perform the OS installation process.

**Expected result**

The information about successful installation should be displayed.

## PVE001.002 Boot Proxmox Virtual Environment stable from Hard Disk

**Test description**

This test aims to verify that Proxmox VE stable could be booted from the hard
disk on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Proxmox VE stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the device on which the system was previously
   installed.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.
