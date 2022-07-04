# Dasharo Compatibility: Firmware update using Dasharo Tools Suite

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Wired network connection.
1. Make yourself familiar with
    [Bootable over network](../../../common-coreboot-docs/dasharo_tools_suite/#bootable-over-network)

### FDT001.001 Flash firmware by using Dasharo Tools Suite

**Test description**

This test aims to verify whether there is the possibility to flash the DUT
firmware by using Dasharo Tools Suite (DTS).

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.
1. [Disable Secure Boot](../../unified-test-documentation/dasharo-security/206-secure-boot.md).
1. Obtain `coreboot.rom` binary.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the `iPXE Network Boot` option.
1. In the `Network Boot menu`, select the `Dasharo Tools Suite` option.
1. Login as root (no password required).
1. Type 9 and click `Enter` to launch into Shell.
1. Run the following commands to update firmware to the latest version:

    ```bash
    flashrom -p internal -w /tmp/coreboot.rom
    ```

1. Reboot the DUT.
1. Press `SETUP_MENU_KEY` to enter the setup menu.
1. Note the results.

**Expected result**

In the `Setup menu` information about the current firmware version should be
displayed.

Example output:

```bash
Dasharo (coreboot+UEFI) v1.2.0
```

### FDT002.001 Firmware update by using Dasharo Tools Suite

**Test description**

This test aims to verify whether there is the possibility to update the DUT
firmware by using Dasharo Tools Suite (DTS).

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.
1. [Disable Secure Boot](../../unified-test-documentation/dasharo-security/206-secure-boot.md).

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the `iPXE Network Boot` option.
1. In the `Network Boot menu`, select the `Dasharo Tools Suite` option.
1. Login as root (no password required).
1. Type 9 and click `Enter` to launch into Shell.
1. Run the following commands to update firmware to the latest version:

    ```bash
    fwupdmgr refresh
    fwupdmgr update
    ```

1. Reboot the DUT.
1. Press `SETUP_MENU_KEY` to enter the setup menu.
1. Note the results.

**Expected result**

In the `Setup menu` information about the current firmware version should be
displayed.

Example output:

```bash
Dasharo (coreboot+UEFI) v1.2.0
```
