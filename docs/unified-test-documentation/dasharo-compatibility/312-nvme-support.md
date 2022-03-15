# Dasharo Compatibility: NVMe support

## Test cases

### NVM001.001 NVMe support (firmware)

**Test description**

This test aims to verify that firmware is able to correctly
detect NVMe disk in the M.2 slot.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Insert a NVMe disk into the M.2 slot on the DUT.
1. Power on the DUT.
1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter
    the UEFI Boot Menu and note the result.

**Expected result**

1. The NVMe disk should be listed on the bootable devices list.

### NVM001.002 NVMe support (Ubuntu 20.04)

**Test description**

This test aims to verify booting the Operating System from NVMe disk in
the M.2 slot.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Insert a NVMe disk into the M.2 slot on the DUT.
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
1. Open a terminal window and execute the follwing command:

```
sudo mount | grep 'on / '
```

**Expected result**

1. The `OPERATING_SYSTEM` has been booted from the NVMe disk correctly.
1. Output in Terminal indicates that system partition is installed on the NVMe
    disk:

```
/dev/nvme* on / tpe ext4 (rw,relatime,errors=remount-ro)
```

### NVM001.003 NVMe support in OS (Windows 11)

**Test description**

This test aims to verify booting the Operating System from NVMe disk in the
M.2 slot.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Insert a NVMe disk into the M.2 slot on the DUT.
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
1. Open device manager.
1. Select `Disk drives` option and find correct drive.
1. Right click the drive entry and select `Properties` option
1. Go to `Details` tab.
1. In the `Property` menu select `Hardware Ids` option.
1. Find the `Value` window and note the result.

**Expected result**

1. The `OPERATING_SYSTEM` booting from the NVMe disk
1. `NVMe` text found in the `Hardware Ids` `Values` window
