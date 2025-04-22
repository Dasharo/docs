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

## NVM001.0XX NVMe support (Linux generic)

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Insert a NVMe disk into the M.2 slot on the DUT.
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

```bash
sudo mount | grep 'on / '
```

**Expected result**

1. The `OPERATING_SYSTEM` has been booted from the NVMe disk correctly.
1. Output in Terminal indicates that system partition is installed on the NVMe
    disk:

```bash
/dev/nvme* on / tpe ext4 (rw,relatime,errors=remount-ro)
```

## NVM001.201 NVMe support (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## NVM001.010 NVMe support (XCP-NG)

Follows the [generic NVM001.0XX Linux-based test case](#nvm0010xx-nvme-support-linux-generic)

## NVM001.011 NVMe support (ESXI)

**Test setup**

1. Insert a NVMe disk into the M.2 slot on the DUT.
1. Install OS on the disc.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Execute the following command:

```bash
esxcli storage core nvme device list
```

**Expected result**

1. The `OPERATING_SYSTEM` has been booted from the NVMe disk correctly.
1. Output from the command contains a line `Is Boot Device: true`
indicating that the nvme drive is the system boot drive.

```bash
t10.NVMe____SSDPR2DPX7002D02T2D80______________________2710003002275A3A
   Display Name: Local NVMe Disk (t10.NVMe____SSDPR2DPX7002D02T2D80______________________2710003002275A3A)
   Has Settable Display Name: true
   Size: 1953514
   Device Type: Direct-Access
   Multipath Plugin: HPP
   Devfs Path: /vmfs/devices/disks/t10.NVMe____SSDPR2DPX7002D02T2D80______________________2710003002275A3A
   Vendor: NVMe
   Model: SSDPR-PX700-02T-80
   Sub NQN: nqn.2014-08.com.maxio:nvme:1602:M.2:G4A007172
   NVMe spec revision: 2.0
   (...)
```

## NVM001.301 NVMe support in OS (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop
