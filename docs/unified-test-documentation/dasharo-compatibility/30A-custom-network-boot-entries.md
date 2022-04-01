# Dasharo Compatibility: Custom Network Boot entries

## Test cases

### CNB001.002 Only one iPXE in boot menu

**Test description**

This test aims to verify that thenetwork boot option with iPXE appears only
once in the boot option list.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Check the iPXE is listed only once on the boot option list.

**Expected result**

1. There is only one iPXE entry on the boot option list.
