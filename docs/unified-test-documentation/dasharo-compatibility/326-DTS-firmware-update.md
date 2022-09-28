# Dasharo Compatibility: Firmware flashing using Dasharo Tools Suite

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Wired network connection.
1. Make yourself familiar with
    [Bootable over network](../../../common-coreboot-docs/dasharo_tools_suite/#bootable-over-network).

## FDT001.001 Flash firmware by using Dasharo Tools Suite

**Test description**

This test aims to verify whether there is the possibility to flash the DUT
firmware by using Dasharo Tools Suite (DTS).

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `{PATH}` = individual path to a specific binary.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. [Disable Secure Boot](../../unified-test-documentation/dasharo-security/206-secure-boot.md).

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the `iPXE Network Boot` option.
1. In the `Network Boot menu`, select the `iPXE Shell` option.
1. Type in `dhcp` to obtain an IP address.
1. Type in `chain  http://boot.3mdeb.com/dts.ipxe` to load DTS.
1. Wait for `Enter an option`.
1. Type 9 and click `Enter` to launch Shell.
1. Run the following command to obtain `coreboot.rom` binary:

    ```bash
    wget https://3mdeb.com/open-source-firmware/{PATH} -O /tmp/coreboot.rom
    ```

    > This is not only way to obtain binary. For example you can use `scp`.

1. Run the following command to flash firmware:

    ```bash
    flashrom -p internal -w /tmp/coreboot.rom
    ```

1. Power off the DUT.
1. Repeat steps 1-8.
1. Run the following command to check firmware version:

    ```bash
    dmidecode -t 0
    ```

1. Note the results.

**Expected result**

The output of `dmidecode` command should contain information about current
firmware. The current firmware version should be equal to the binary version,
which you were flashing.

Example output:

```bash
Version: Dasharo (coreboot+UEFI) v1.1.0
```

## FDT002.001 Firmware update using fwupd in Dasharo Tools Suite

**Test description**

This test aims to verify whether there is the possibility to update the DUT
firmware by using Dasharo Tools Suite (DTS).

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. [Disable Secure Boot](../../unified-test-documentation/dasharo-security/206-secure-boot.md).

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the `iPXE Network Boot` option.
1. In the `Network Boot menu`, select the `iPXE Shell` option.
1. Type in `dhcp` to obtain an IP address.
1. Type in `chain  http://boot.3mdeb.com/dts.ipxe` to load DTS.
1. Wait for `Enter an option`.
1. Type 9 and click `Enter` to launch into Shell.
1. Run the following commands to update firmware to the latest version:

    ```bash
    fwupdmgr refresh
    fwupdmgr update
    ```

1. Power off the DUT.
1. Repeat steps 1-8.
1. Run the following command to check firmware version:

    ```bash
    dmidecode -t 0
    ```

1. Note the results.

**Expected result**

The output of `dmidecode` command should contain information about current
firmware. The current firmware version should be equal to the binary version,
which you were flashing.

Example output:

```bash
Version: Dasharo (coreboot+UEFI) v1.1.0
```
