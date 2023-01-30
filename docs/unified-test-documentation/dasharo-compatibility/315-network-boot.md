# Dasharo Compatibility: Network Boot

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Device should be connected to the Internet by using an Ethernet cable.

## PXE000.001 Enable Network Boot (Firmware)

**Test description**

This test aims to verify if Network Boot can be enabled.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `SETUP_MENU_KEY` = F2

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Dasharo System Features` menu option.
1. Enter the `Networking Options` menu option.
1. Hover on checkbox next to `Enable Network Boot` option, and make sure
    that `X` sign is present between square brackets - `[X]`. Use `Spacebar`
    to toggle.
1. Save using `F10`, and exit using `Esc`.
1. Reboot the device.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `One Time Boot` menu option.

**Expected result**

1. The `Network Boot` boot option is present.

## PXE000.002 Disable Network Boot (Firmware)

**Test description**

This test aims to verify if Network Boot can be disabled. When disabled, it
prevents loading network controller drivers and unregisters iPXE as boot option.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `SETUP_MENU_KEY` = F2

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Dasharo System Features` menu option.
1. Enter the `Networking Options` menu option.
1. Hover on checkbox next to `Enable Network Boot` option, and make sure
    that `X` sign is NOT present between square brackets - `[ ]`. Use `Spacebar`
    to toggle.
1. Save using `F10`, and exit using `Esc`.
1. Reboot the device.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `One Time Boot` menu option.

**Expected result**

1. The `Network Boot` boot option is not present.

## PXE001.001 Dasharo Network Boot is available

**Test description**

This test aims to verify, that the `iPXE Network boot` is available in the boot
menu and whether, after selecting this boot option, `Dasharo Network Boot Menu`
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

1. `Dasharo Network Boot Menu` contains all of the needed options.
1. `Dasharo Network Boot Menu` options are in order as follows:

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
1. Select the `Autoboot` option using the arrow keys, then press `Enter`.

**Expected result**

If the server assigned to the `Autoboot` option is available in the local
network, the boot menu should appear.

If the server assigned to the `Autoboot` option isn't available in the local
network, selecting this option will result in configuring the network interfaces
and return to the `Setup Menu`.

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
    [Requirements for DTS](../../../dasharo-tools-suite/documentation#running).

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `iPXE Network boot` option using the arrow keys and press `Enter`.
1. Select the `Dasharo Tools Suite` option using the arrow keys, then press
    `Enter`.

**Expected result**

After configuring the network interfaces, connecting to the server and booting,
`Dasharo Tools Suite` menu should appear.

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

After configuring the network interfaces, connecting to the server and booting,
`netboot.xyz` menu should appear.

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

1. Load `netboot.xyz` server menu by executing the following command:

    ```bash
    chain --autofree http://boot.netboot.xyz/
    ```

**Expected result**

After configuring the network interfaces, connecting to the server and booting,
`netboot.xyz` menu should appear.

## PXE007.001 iPXE network boot

**Test description**

This test aims to verify that the DUT is capable of network booting from a PXE
server.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `iPXE Network boot` option using the arrow keys and press `Enter`.
1. Press `Ctrl+B` when prompted to stop iPXE from booting automatically.
1. Type in `dhcp` to obtain an IP address.
1. Type in `chain --autofree http://boot.netboot.xyz/` to load a boot menu
1. Enter the "Live CDs" submenu using the arrow keys and Enter.
1. Select `Debian` -> `Debian Live 11 (bullseye)` -> `Debian 11 Gnome` and
    press Enter.

**Expected result**

1. The iPXE application boots successfully.
1. iPXE obtains an IP address.
1. iPXE boots an `Debian 11` from netboot.xyz.
