# Dasharo Compatibility: UEFI Shell

## USH001.001 UEFI Shell

**Test description**

This test aims to verify that the DUT has the ability to boot into an integrated
UEFI Shell application.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Generic test setup: Firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BOOT_MENU_KEY` to enter the UEFI Boot
    Menu.
1. Select the `UEFI Shell` option using the arrow keys and press `Enter`.

**Expected result**

The DUT boots into an UEFI Shell successfully, as indicated by the example
console output shown on the screen:

```text
UEFI Interactive Shell v2.2
EDK II
UEFI v2.70 (EDK II, 0x00010000)
Mapping table
      FS0: Alias(s):HD1b:;BLK2:
      PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,9C-BB-50-01-BB-38-25-5
-4BB4-4FDD-9534-B097CD497222,0x800,0x100000)
      FS1: Alias(s):HD1c:;BLK3:
      PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,9C-BB-50-01-BB-38-25-1
-C6AB-4400-AE03-0BF2960DD525,0x100800,0x1D0C5000)
     BLK1: Alias(s):
     PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,9C-BB-50-01-BB-38-25-)
        BLK0: Alias(s):
        PciRoot(0x0)/Pci(0x14,0x0)/USB(0x0,0x2)
    Press ESC in 1 seconds to skip startup.nsh or any other key to continue.
```
