# Dasharo Compatibility: Network boot utilities

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

### NBT001.001 Netboot is available

**Test description**

This test aims to verify that the `Network Boot and Utilities` menu is
available and its content is right.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `Network Boot and Utilities` option using the arrow keys and
    press `Enter`.

**Expected result**

1. `Network Boot and Utilities` option should be present in the UEFI Boot Menu.
1. After selecting the `Network Boot and Utilities` option the following
    menu should appear:

    ```bash
       ------------------------ Network Boot and Utilities ----------------------
       ------------------------ Please Select an Option -------------------------
       OS Selection & Utilities
       iPXE Boot
       iPXE Shell
       Advanced
    ```

### NBT002.001 OS Selection & Utilities is available

**Test description**

This test aims to verify that the `OS Selection & Utilities` menu is
available and its content is right.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `Network Boot and Utilities` option using the arrow keys and press
    `Enter`.
1. Select the `OS Selection & Utilities` option using the arrow keys and press
    `Enter`.

**Expected result**

1. `OS Selection & Utilities` option should be present in the
    `Network Boot and Utilities` menu.
1. After selecting the `OS Selection & Utilities` option the following
    menu should appear:

    ```bash
     ____               __                  __    ___
    /\  _`\            /\ \__              /\ \__/\_ \    __
    \ \ \L\ \_ __   ___\ \ ,_\    __    ___\ \ ,_\//\ \  /\_\
     \ \ ,__/\`'__\/ __`\ \ \/  /'__`\ /'___\ \ \/ \ \ \ \/\ \
      \ \ \/\ \ \//\ \L\ \ \ \_/\  __//\ \__/\ \ \_ \_\ \_\ \ \
       \ \_\ \ \_\\ \____/\ \__\ \____\ \____\\ \__\/\____\\ \_\
        \/_/  \/_/ \/___/  \/__/\/____/\/____/ \/__/\/____/ \/_/

    These tools are under construction.
    Eventually, official Protectli tools and installers will be available here.

    In the meantime, check out netboot.xyz.

    Press any key to continue to netboot.xyz

    ```

### NBT003.001 iPXE boot is available

**Test description**

This test aims to verify that the `iPXE Boot` menu is available and it
content is right.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `Network Boot and Utilities` option using the arrow keys and
    press `Enter`.
1. Select the `iPXE Boot` option using the arrow keys and press `Enter`.

**Expected result**

1. `iPXE Boot` option should be present in the `Network Boot and Utilities`
    menu.
1. After selecting the `iPXE Boot` option the autoboot procedure should be
    started.

### NBT004.001 iPXE shell is available

**Test description**

This test aims to verify that the `iPXE Shell` menu is available and it
content is right.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `Network Boot and Utilities` option using the arrow keys and press
`Enter`.
1. Select the `iPXE Shell` option using the arrow keys and press `Enter`.

**Expected result**

1. `iPXE Shell` option should be present in the `Network Boot and Utilities`
    menu.
1. After selecting the `iPXE Shell` option the following menu should appear:

    ```bash
    You are now in iPXE shell. Type "exit" to go back to the main menu.
    iPXE>
    ```

### NBT005.001 iPXE shell works correctly

**Test description**

This test aims to verify that the iPXE shell works correctly by configuring
network interface and booting from selected address.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `Network Boot and Utilities` option using the arrow keys and press
    `Enter`.
1. Select the `iPXE Shell` option using the arrow keys and press `Enter`.
1. Configure communication interface by using the following command:

    ```bash
    dhcp net0
    ```

1. Connect to the DTS ipxe menu by using the following command:

    ```bash
    chain http://boot.3mdeb.com/dts.ipxe
    ```

**Expected result**

1. Communication interface configuration procedure should be successful.
1. DTS boot menu should appear.

### NBT006.001 Advanced option is available

**Test description**

This test aims to verify that the `Advanced` menu is available and its content
is right.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `Network Boot and Utilities` option using the arrow keys and press
    `Enter`.
1. Select the `Advanced` option using the arrow keys and press `Enter`.

**Expected result**

1. `Advanced` option should be present in the `Network Boot and Utilities`
    menu.
1. After selecting the `Advanced` option the following menu should appear:

    ```bash
       ------------------------ Network Boot and Utilities ----------------------
       ------------------------ Please Select an Option -------------------------
       Change Netboot iPXE Payload URL
       Exit
    ```

### NBT007.001 Change netboot URL works correctly

**Test description**

This test aims to verify that it's possible to change the netboot URL and boot
from it.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `Network Boot and Utilities` option using the arrow keys and press
    `Enter`.
1. Select the `Advanced` option using the arrow keys and press `Enter`.
1. Select the `Change Netboot iPXE Payload URL` option using the arrow keys and
    press `Enter`.
1. Select the `Change Netboot iPXE Payload URL` option **again** using the arrow
    keys and press `Enter`.
1. Replace the existing address with another iPXE payload URL address, for
    example: `http://boot.3mdeb.com/dts.ipxe`.
1. Apply changes by selecting option `Apply and Exit` and pressing `Enter`.
1. Select the `OS Selection & Utilities` option using the arrow keys and press
    `Enter`.

**Expected result**

1. Proper boot menu should appear.
