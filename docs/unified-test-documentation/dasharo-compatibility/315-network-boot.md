# Dasharo Compatibility: Network Boot

## Test cases

### PXE001.001 iPXE network boot

**Test description**

This test aims to verify that the DUT is capable of network booting from a PXE
server.

**Test configuration data**

1. `FIRMWARE` = coreboot

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
