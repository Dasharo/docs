# Dasharo Compatibility: Network Boot

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Device should be connected to the Internet by using an Ethernet cable.

## PXE001.001 Dasharo Network Boot is available

**Test description**

This test aims to verify, that the `iPXE Network boot` is available in the boot
menu and whether, after selecting this boot option `Dasharo Network Boot Menu`
is displayed.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `iPXE Network boot` option using the arrow keys and press `Enter`.

**Expected result**

1. The `iPXE Network boot` option is available.
1. After selecting the `iPXE Network boot`, the `Dasharo Network Boot Menu`
    should be displayed.

## PXE002.001 Dasharo network boot menu boot options order is correct

**Test description**

This test aims to verify that `Dasharo Network Boot Menu` contains all of the
needed options which are in the correct order.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `iPXE Network boot` option using the arrow keys and press `Enter`.

**Expected result**

`Dasharo Network Boot Menu` contains all of the needed options which are in the
following order:

```bash
Autoboot
Dasharo Tools Suite
OS installation
iPXE Shell
```

## PXE003.001 Autoboot option is available and works correctly

**Test description**

This test aims to verify that the `Autoboot` option in
`Dasharo Network Boot Menu` works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `iPXE Network boot` option using the arrow keys and press `Enter`.
1. Select the `Autoboot` option using the arrow keys and press `Enter`.

**Expected result**

If the server assigned to the `Autoboot` option is available in the local
network after a while menu should appear.

If the server assigned to the `Autoboot` option isn't available in the local
network, selecting this option will result in configuring the network interfaces
and in the case of no access to the server, return to the setup menu.

## PXE004.001 DTS option is available and works correctly

**Test description**

This test aims to verify that the `Dasharo Tools Suite` option in
`Dasharo Network Boot Menu` allows booting into DTS.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Proceed with the
    [Requirements for DTS](https://docs.dasharo.com/common-coreboot-docs/dasharo_tools_suite/#requirements).

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `iPXE Network boot` option using the arrow keys and press `Enter`.
1. Select the `Dasharo Tools Suite` option using the arrow keys and press
    `Enter`.

**Expected result**

After connecting to the server and booting into DTS, the DTS menu should appear.

## PXE005.001 OS installation option is available and works correctly

**Test description**

This test aims to verify that the `OS installation` option in
`Dasharo Network Boot Menu` allows booting into netboot.xyz server.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `iPXE Network boot` option using the arrow keys and press `Enter`.
1. Select the `OS installation` option using the arrow keys and press `Enter`.

**Expected result**

After a while netboot.xyz server menu should appear. You should be able to move
in the menu using the arrow keys and select the option using `Enter`.

## PXE006.001 iPXE shell option is available and works correctly

**Test description**

This test aims to verify that the `iPXE Shell` option in
`Dasharo Network Boot Menu` works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the boot menu.
1. Select the `iPXE Network boot` option using the arrow keys and press `Enter`.
1. Select the `iPXE Shell` option using the arrow keys and press `Enter`.
1. Obtain an IP address by executing the following command:

    ```bash
    dhcp
    ```

1. Load a netboot.xyz server menu by executing the following command:

    ```bash
    chain --autofree http://boot.netboot.xyz/
    ```

**Expected result**

After a while netboot.xyz server menu should appear. You should be able to move
in the menu using the arrow keys and select the option using `Enter`.
