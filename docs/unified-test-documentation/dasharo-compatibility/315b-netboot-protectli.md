# Dasharo Compatibility: Netboot Protectli VP4620

## Test cases

### NBT001.001 Netboot is available

**Test description**

This test aims to verify that the `Network Boot and Utilities` option exist, and
if after selection proper menu apperas.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `Network Boot and Utilities` option using the arrow keys and press
`Enter`.

**Expected result**

1. Menu with below contents should appear:

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

This test aims to verify that the `OS Selection & Utilities` option is available
and if after selection proper menu apperas.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `Network Boot and Utilities` option using the arrow keys and press
`Enter`.
1. Select the `OS Selection & Utilities` option using the arrow keys and press
`Enter`.

**Expected result**

1. Menu with below contents should appear:

```bash
Configuring (net0 00:e0:97:1b:99:50)...... ok
https://netboot.protectli.com/menu.ipxe.... ok
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

This test aims to verify that the `iPXE Boot` is available, and if after
selection iPXE menu appears.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `Network Boot and Utilities` option using the arrow keys and press
`Enter`.
1. Select the `iPXE Boot` option using the arrow keys and press `Enter`.

**Expected result**

1. Menu with below contents should appear:

```bash
???? Work In Progress - NOT WORKING
```

### NBT004.001 iPXE shell is available

**Test description**

This test aims to verify that the `iPXE shell` option is available, and if after
selection iPXE shell appears.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `Network Boot and Utilities` option using the arrow keys and press
`Enter`.
1. Select the `iPXE Shell` option using the arrow keys and press `Enter`.

**Expected result**

1. Menu with below contents should appear:

```bash
You are now in iPXE shell. Type "exit" to go back to the main menu.
iPXE>
```

### NBT005.001 iPXE shell works correctly

**Test description**

This test aims to verify that the iPXE shell works correctly by configuring
network interface and booting to selected adress.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `Network Boot and Utilities` option using the arrow keys and press
`Enter`.
1. Select the `iPXE Shell` option using the arrow keys and press `Enter`.
1. Configure ethernet port, and connect to iPXE menu using:

```powershell
dhcp net0
```

```powershell
chain http://boot.3mdeb.com/dts.ipxe
```

**Expected result**

1. DTS menu should appear.

### NBT006.001 Advanced option is available

**Test description**

This test aims to verify that the `Advanced` option is available, and if after
selection proper menu apperas.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the `Network Boot and Utilities` option using the arrow keys and press
`Enter`.
1. Select the `Advanced` option using the arrow keys and press `Enter`.

**Expected result**

1. Menu with below contents should appear:

```bash
   ------------------------ Network Boot and Utilities ----------------------
   ------------------------ Please Select an Option -------------------------
   Change Netboot iPXE Payload URL
   Exit
```

### NBT007.001 Change netboot url works correctly

**Test description**

This test aims to verify that it's possible to change netboot url, and boot to
it.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

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
1. Replace existing adress with for example: `http://boot.3mdeb.com/dts.ipxe`
1. Apply changes selecting `Apply and Exit`
1. Select the `OS Selection & Utilities` option using the arrow keys and press
`Enter`.

**Expected result**

1. DTS menu should appear.
