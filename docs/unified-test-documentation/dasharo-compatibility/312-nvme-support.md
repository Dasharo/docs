# Dasharo Compatibility: NVMe support

## NVM001.001 NVMe support (firmware)

**Test description**

This test aims to verify that firmware is able to correctly
detect NVMe disk in the M.2 slot.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Insert a NVMe disk into the M.2 slot on the DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter
    the UEFI Boot Menu and note the result.

**Expected result**

1. The NVMe disk should be listed on the bootable devices list.

## NVM001.201 NVMe support (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## NVM001.301 NVMe support in OS (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop
