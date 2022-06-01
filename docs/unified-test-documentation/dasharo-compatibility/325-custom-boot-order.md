# Dasharo Compatibility: Custom Boot Order (SSD, USB)

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

### CBO001.001 Custom boot order

**Test description**

This test aims to verify that the DUT boot from the suitable source, with the
posibility to boot from other sources.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT
1. Press `BOOT_MENU_KEY` key to display boot menu.
1. Compare the listed devices with the desired boot order.

**Expected result**

When there is a possibility for the platform to boot from different sources:

1. Priority will be given to the system booted from SSD connected by mSATA.
1. If above-mentioned SSD does not include system, it will be booted from USB.
1. If it either not include system, it will be booted from SSD connected by
SATA 2.5

If there is only one bootable medium the platform shall boot from it.

Example boot menu:

```bash
Select boot device:

1. AHCI/0: SATA SSD ATA-11 Hard-Disk (15272 MiBytes)
2. USB MSC Drive  USB Flash Memory PMAP
3. USB MSC Drive SanDisk Ultra 1.00
4. USB MSC Drive Generic Flash Disk 8.07
5. AHCI/1: TOSHIBA MK2561GSYN ATA-8 Hard-Disk (232 GiBytes)
6. iPXE
7. Payload [memtest]
```
