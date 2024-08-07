# Dasharo Compatibility: USB-C/Thunderbolt support with charging and display

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../generic-test-setup.md#os-boot-from-disk).

## TMD001.001 USB Type-A charging capability with ME disabled

**Test description**

This test verifies that the USB-A ports are able to provide charging to a
connected smartphone.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
 Disable (Soft) - if not, using the arrow keys and Enter, choose option
 Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect a phone to the USB Type-A port located on the left side of the laptop
    using a USB cable.
1. Note the charging status on the phone screen.
1. Connect a phone to the USB Type-A port located on the right side of the laptop
    using a USB cable.
1. Note the charging status on the phone screen.

**Expected result**

1. The smartphone should indicate that it's charging when connected to either
    USB Type-A port.

## TMD002.001 Thunderbolt 4 USB Type-C power output with ME disabled

**Test description**

This test verifies that the Thunderbolt 4 port is able to provide charging to a
USB Type-C accessory.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect a phone to the Thunderbolt 4 USB Type-C port located on the left side
    of the laptop using a USB cable.
1. Note the charging status on the phone screen.

**Expected result**

1. The smartphone should indicate that it's charging.

## TMD003.001 USB Type-C PD power input with ME disabled(Ubuntu)

**Test description**

This test verifies that the device can sink power from a USB-PD power supply
connected to the Thunderbolt 4 port.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Disconnect any charger from the DUT.
1. Connect the charger plug to the docking station.
1. Open a terminal window and run the following command:

    ```bash
    cat /sys/class/power_supply/BAT0/status
    ```

**Expected result**

Output of the command should show one of this: `Charging` or `Full`. That means
laptop is charged properly.

## TMD003.002 USB Type-C PD power input with ME disabled(Windows)

**Test description**

This test verifies that the device can sink power from a USB-PD power supply
connected to the Thunderbolt 4 port.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Disconnect any charger from the DUT.
1. Connect the charger plug to the docking station.
1. Open PowerShell and and run the following command:

    ```powershell
    Get-WmiObject win32_battery
    ```

**Expected result**

If `BatteryStatus` is equal 2, that means laptop is charged properly.

Example part of output:

```powershell
BatteryStatus               : 2
```

## TMD004.001 USB Type-C Display output with ME disabled(Ubuntu)

**Test description**

This test verifies that DUT output video to a display connected via
the Thunderbolt 4 USB Type-C port.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect a display to the Thunderbolt 4 USB Type-C port using
    a USB Type-C hub
1. Open the Settings application and select the Displays panel in the left menu.
1. Verify that the attached external monitor can be selected.
1. Select and enable the monitor.

**Expected result**

1. The monitor connected to the laptop via the Thunderbolt 4 port should power
   on and display video from the laptop.

## TMD004.002 USB Type-C Display output with ME disabled(Windows)

**Test description**

This test verifies that DUT output video to a display connected via
the Thunderbolt 4 USB Type-C port.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect a display to the Thunderbolt 4 USB Type-C port using
    a USB Type-C hub.
1. Right click on the desktop to open the desktop context menu.
1. Select `Display Settings` to open the display settings window.
1. Verify that the attached external monitor can be selected.
1. Select and enable the monitor.

**Expected result**

1. The monitor connected to the laptop via the Thunderbolt 4 port should power
   on and display video from the laptop.

## TMD005.001 USB Type-C docking station HDMI display with ME disabled(Ubuntu)

**Test description**

This test aims to verify that the display connected with the HDMI cable to the
docking station is correctly recognized by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Connect an HDMI cable to the docking station and a display.
1. The `USB-C docking station` connected to the USB-C port.

    > If the docking station is not directly connected to the DUT, but with a
    > USB-C to USB-C cable, make sure it is full-featured cable (>=5Gbps) with
    > 5A current capability.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. If using more than one display, switch the display mode between `Mirror` and
   `Join Displays`.

**Expected result**

The image should be displayed on the external HDMI-connected display in `Mirror`
and `Join Displays` modes.

## TMD005.002 USB Type-C docking station HDMI display with ME disabled(Windows)

**Test description**

This test aims to verify that the display connected with the HDMI cable to the
docking station is correctly recognized by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Connect an HDMI cable to the docking station and a display.
1. The `USB-C docking station` connected to the USB-C port.

    > If the docking station is not directly connected to the DUT, but with a
    > USB-C to USB-C cable, make sure it is full-featured cable (>=5Gbps) with
    > 5A current capability.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. If using more than one display, switch the display mode between `Duplicate`
   and `Extend`.

**Expected result**

The image should be displayed on the external HDMI-connected display in
`Duplicate` and `Extend` modes.

## TMD006.001 USB Type-C docking station DP display with ME disabled(Ubuntu)

**Test description**

This test aims to verify that the display connected with the HDMI cable to the
docking station is correctly recognized by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Connect a Display Port cable to the docking station and a display.
1. The `USB-C docking station` connected to the USB-C port.

    > If the docking station is not directly connected to the DUT, but with a
    > USB-C to USB-C cable, make sure it is full-featured cable (>=5Gbps) with
    > 5A current capability.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. If using more than one display, switch the display mode between `Mirror` and
   `Join Displays`.

**Expected result**

The image should be displayed on the external DisplayPort-connected display in
`Mirror` and `Join Displays` modes.

## TMD006.002 USB Type-C docking station DP display with ME disabled(Windows)

**Test description**

This test aims to verify that the display connected with the DisplayPort cable
to the docking station is correctly recognized by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Connect a DisplayPort cable to the docking station and a display.
1. The `USB-C docking station` connected to the USB-C port.

    > If the docking station is not directly connected to the DUT, but with a
    > USB-C to USB-C cable, make sure it is full-featured cable (>=5Gbps) with
    > 5A current capability.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. If using more than one display, switch the display mode between `Duplicate`
   and `Extend`.

**Expected result**

The image should be displayed on the external DisplayPort-connected display in
`Duplicate` and `Extend` modes.

## TMD007.001 USB Type-C docking station Triple display with ME disabled(Ubuntu)

**Test description**

This test aims to verify that the three display simultaneously connected to the
docking station is correctly recognized by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Connect three displays using HDMI/DisplayPort cables, depending on the
   specifications of the docking station.
1. The `USB-C docking station` connected to the USB-C port.

    > If the docking station is not directly connected to the DUT, but with a
    > USB-C to USB-C cable, make sure it is full-featured cable (>=5Gbps) with
    > 5A current capability.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Switch the display mode between `Mirror` and `Join Displays`.

**Expected result**

The image should be displayed on the three external displays in `Mirror` and
`Join Displays` modes.

## TMD007.002 USB Type-C docking station Triple display with ME disabled(Windows)

**Test description**

This test aims to verify that the three display simultaneously connected to the
docking station is correctly recognized by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Connect three displays using HDMI/DisplayPort cables, depending on the
   specifications of the docking station.
1. The `USB-C docking station` connected to the USB-C port.

    > If the docking station is not directly connected to the DUT, but with a
    > USB-C to USB-C cable, make sure it is full-featured cable (>=5Gbps) with
    > 5A current capability.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. If using more than one display, switch the display mode between `Duplicate`
   and `Extend`.

**Expected result**

The image should be displayed on the three external displays in `Duplicate` and
`Extend` modes.

## TMD008.001 USB Type-C docking station detection after coldboot with ME disabled(Ubuntu)

**Test description**

This test aims to verify that the DUT properly detects the docking station after
coldboot (realized by power supply cutting off then restoring back).
This test case may be re-done several times to specify the platform and
connection stability.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.

**Test steps**
1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Cut the power off while DUT is turned on.
1. Restore power and power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**

After `lsusb` command the docking station entries should be displayed, but
output can be different depending on the model of the docking station.

Example entries signifing the docking station:

```bash
Bus 002 Device 010: Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter
Bus 002 Device 009: Prolific Technology, Inc. USB SD Card Reader
Bus 002 Device 008: VIA Labs, Inc. USB3.0 Hub
```

## TMD009.001  USB Type-C docking station detection after warmboot with ME disabled(Ubuntu)

**Test description**

This test aims to verify that the DUT properly detects the docking station
after warmboot (realized by device turning off then turning on). This test case
may be re-done several times to specify the platform and connection stability.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**

After `lsusb` command the docking station entries should be displayed, but
output can be different depending on the model of the docking station.

Example entries signifing the docking station:

```bash
Bus 002 Device 010: Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter
Bus 002 Device 009: Prolific Technology, Inc. USB SD Card Reader
Bus 002 Device 008: VIA Labs, Inc. USB3.0 Hub
```

# TMD010.001 USB Type-C docking station detection after reboot ME disabled (Ubuntu)

**Test description**

This test aims to verify that the DUT properly detects the docking station
after system reboot (performed by relevant command). This test case may be
re-done several times to specify the platform and connection stability.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. The `USB-C docking station` connected to the USB-C port.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option D
isable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    sudo reboot
    ```

1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**

After `lsusb` command the docking station entries should be displayed, but
output can be different depending on the model of the docking station.

Example entries signifing the docking station:

```bash
Bus 002 Device 010: Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter
Bus 002 Device 009: Prolific Technology, Inc. USB SD Card Reader
Bus 002 Device 008: VIA Labs, Inc. USB3.0 Hub
```

## TMD011.001 USB Type-C docking station USB devices recognition ME disabled (firmware)

**Test description**

This test aims to verify that the external USB devices connected to the docking
station are recognized correctly by the `FIRMWARE`.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.
1. The `USB storage` connected to the `USB-C docking station`.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Hold the `BIOS_MENU_KEY` to enter the BIOS Menu.
1. Check if the `USB storage` is available on the list.

**Expected result**

The `USB storage` is available which confirms successful recognition.

## TMD011.002 USB Type-C docking station USB devices recognition with ME disabled(Ubuntu)

**Test description**

This test aims to verify that the external USB devices connected to the docking
station are recognized correctly by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.
1. The `USB storage` connected to the `USB-C docking station`.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    watch -n1 lsusb
    ```

1. Connect(or Disconnect) external USB devices to the USB ports on the docking
    station and note the result.

**Expected result**

1. After each device is connected to the USB port, a new USB device entry
    in `lsusb` command output should appear.
1. After each device is disconnected from the USB port, a USB device entry
    in `lsusb` command output should disappear.

## TMD011.003 USB Type-C docking station USB devices recognition with ME disabled(Windows)

**Test description**

This test aims to verify that the external USB devices connected to the docking
station are recognized correctly by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.
1. The `USB storage` connected to the `USB-C docking station`.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open PowerShell and and run the following command:

    ```powershell
    Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }
    ```

1. Note the results.

**Expected result**

After executing the command, a list containing all USB devices should be
displayed. The list should contain the `USB storage`, which is plug in.

    Example output:

    ```bash
        Status     Class           FriendlyName
        ------     -----           ------------
        OK         DiskDrive       Mass Storage Device USB Device
        OK         USB             Generic USB Hub
        OK         HIDClass        USB Input Device
        OK         Bluetooth       Intel(R) Wireless Bluetooth(R)
        OK         DiskDrive       USB SanDisk 3.2Gen1 USB Device
        OK         USB             USB Root Hub (USB 3.0)
        OK         Net             TP-LINK Gigabit Ethernet USB Adapter
        OK         USB             Generic USB Hub
        OK         USB             USB Mass Storage Device
    ```

## TMD012.001 USB Type-C docking station USB keyboard with ME disabled(firmware)

**Test description**

This test aims to verify that the external USB keyboard connected to the docking
station is detected correctly by the `FIRMWARE` and all basic keys work
according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.
1. The `external USB keyboard` connected to the docking station.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_MENU_KEY` to enter the Bios Menu.
1. Use the arrow keys, Esc key and the Enter key to navigate the menus.

**Expected result**

All menus can be entered using the external USB keyboard.

## TMD012.002 USB Type-C docking station USB keyboard with ME disabled(Ubuntu)

**Test description**

This test aims to verify that the external USB keyboard connected to the docking
station is detected correctly by the `OPERATING_SYSTEM` and all basic keys work
according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `libinput-tools` package: `sudo apt install libinput-tools`.
1. The `USB-C docking station` connected to the USB-C port.
1. The `external USB keyboard` connected to the docking station.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Run the following command in the terminal:

    ```bash
    libinput debug-events --show-keycodes
    ```

1. Test the alphanumeric keys and note the generated keycodes.
1. Test non-alphanumeric keys and verify that they generate the correct
    keycodes.
1. Test key combinations with the `Shift`, `Ctrl` and `Alt` modifier keys
    (this tests 2-key rollover).

**Expected result**

1. The external USB keyboard is detected in OS.
1. All standard keyboard keys generate the correct keycodes and events as per
   their labels.
1. Key combinations are detected correctly.

## TMD012.003 USB Type-C docking station USB keyboard with ME disabled(Windows)

**Test description**

This test aims to verify that the external USB keyboard is detected correctly
by the `OPERATING_SYSTEM` and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.
1. The external USB keyboard connected to the docking station.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open PowerShell and and run the following command:

    ```powershell
    Get-CimInstance win32_KEYBOARD
    ```

1. Note the results.
1. Open `notepad`.
1. Test the alphanumeric keys and note the generated characters.
1. Test non-alphanumeric keys and verify that they generate the signs.
1. Test key combinations with the `Shift`, and `Alt` modifier keys.
1. Open `On-Screen Keyboard` and press `Ctrl` key on the hardware keyboard.
   Check if `On-Screen Keyboard` correctly highlights it.
1. Open `Start menu` and press `Esc`. Check if `Start menu` is properly closed.

**Expected result**

1. After running the PowerShell command information about connected keyboards
    should be displayed.

    One of keyboard should have identical part of output:

    ```powershell
    Description                 : USB Input Device
    ```

1. All standard keyboard keys generate correct characters
   or actions when pressed.
1. Key combinations are detected correctly.

## TMD013.001 USB Type-C docking station upload 1GB file on USB storage with ME disabled(Ubuntu)

**Test description**

This test aims to verify that the 1GB file can be transferred from the
`OPERATING_SYSTEM` to the `USB storage` connected to the docking station.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.
1. The `USB storage` connected to the `USB-C docking station`.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command to generate 1GB file:

    ```bash
    openssl rand -out test_file.txt -base64 $(( 2**30 * 3/4 ))
    ```

1. Read the path to the `USB storage` by running the following command:

    ```bash
    lsblk
    ```

1. Copy the generated file to the `USB storage` by running the following
   command:

    ```bash
    cp test_file.txt {path_to_usb_storage}
    ```

1. Verify that the files are the same by running the following command:

    ```bash
    sha256sum test_file.txt {path_to_usb_storage}/test_file.txt
    ```

**Expected result**

The output from the last command should contain 2 identical checksums:

```bash
f46597c0c63a1eefb200d40edf654e52f10c3d5d21565886ad603fabaf8d39fb  test_file.txt
f46597c0c63a1eefb200d40edf654e52f10c3d5d21565886ad603fabaf8d39fb  {path_to_usb_storage}/test_file.txt
```

## TMD013.002 USB Type-C docking station upload 1GB file on USB storage with ME disabled(Windows)

**Test description**

This test aims to verify that the 1GB file can be transferred from the
`OPERATING_SYSTEM` to the `USB storage` connected to the docking station.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.
1. The `USB storage` connected to the `USB-C docking station`.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open powershell as administrator and run the following command to generate
   1GB file:

    ```powershell
    fsutil file createnew test_file.txt 1073741824
    ```

1. Read the drive letter assigned to the `USB storage` by running the following
   command:

    ```powershell
    (Get-Volume | where drivetype -eq removable).driveletter
    ```

1. Copy the generated file to the `USB storage` by running the following
   command:

    ```powershell
    Copy-Item -Path C:\Windows\system32\test_file.txt {drive_letter}:
    ```

1. Verify that the files are the same by running the following commands:

    ```powershell
    Get-FileHash test_file.txt
    Get-FileHash {drive_letter}:\test_file.txt
    ```

**Expected result**

The output from the last commands should have equal hash:

```powershell
Algorithm       Hash                                                              Path
---------       ----                                                              ----
SHA256          F46597C0C63A1EEFB200D40EDF654E52F10C3D5D21565886AD603FABAF8D39FB  C\Windows\system3...
```

```powershell
Algorithm       Hash                                                              Path
---------       ----                                                              ----
SHA256          F46597C0C63A1EEFB200D40EDF654E52F10C3D5D21565886AD603FABAF8D39FB  E:\test_file.txt
```

## TMD014.001 USB Type-C docking station Ethernet connection with ME disabled(Ubuntu)

**Test description**

This test aims to verify that the connection to internet via docking station's
Ethernet port can be obtained on Ubuntu.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a Ethernet cable with internet connection to docking station.
1. Wait for internet connection to initialize.
1. Ping `3mdeb.com` using command in terminal:

    ```bash
    ping 3mdeb.com
    ```

**Expected result**

1. Command should return ping info:

    ```bash
    PING 3mdeb.com (178.32.205.96) 56(84) bytes of data.
    64 bytes from cluster026.hosting.ovh.net (178.32.205.96): icmp_seq=1 ttl=50 time=44.3 ms
    64 bytes from cluster026.hosting.ovh.net (178.32.205.96): icmp_seq=2 ttl=50 time=47.7 ms
    64 bytes from cluster026.hosting.ovh.net (178.32.205.96): icmp_seq=3 ttl=50 time=41.1 ms
    ...
    ```

1. Log should not contain phrase information that host is unreachable.

    Failed ping for Ubuntu 22.04:

    ```bash
    ping: connect: Network is unreachable
    ```

## TMD014.002 USB Type-C docking station Ethernet connection with ME disabled(Windows)

**Test description**

This test aims to verify that the connection to internet via docking station's
Ethernet port can be obtained on Windows.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a Ethernet cable with internet connection to docking station.
1. Wait for internet connection to initialize.
1. Ping `3mdeb.com` using command in PowerShell:

    ```PowerShell
    ping 3mdeb.com
    ```

**Expected result**

1. Command should return ping info:

    ```PowerShell
    Pinging 3mdeb.com [178.32.205.96] with 32 bytes of data:
    Reply from 178.32.205.96: bytes=32 time=50ms TTL=50
    Reply from 178.32.205.96: bytes=32 time=47ms TTL=50
    Reply from 178.32.205.96: bytes=32 time=46ms TTL=50
    ```

1. Log should not contain phrase information that host is unreachable.

    Failed ping for Windows 11:

    ```powershell
    Ping request could not find host 3mdeb.com. Please check the name and try again.
    ```

## TMD015.001 USB Type-C docking station audio recognition with ME disabled(Ubuntu)

**Test description**

This test aims to verify that the external headset is properly recognized after
plugging in the 3.5 mm jack into the docking station.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a headset jack into the docking station.
1. When the `Select Audio Device` menu appears, select what type of external
    device has been connected to the laptop (headset).
1. Open a terminal window and run the following command:

    ```bash
    watch -n1 lsusb
    ```

1. Connect(or Disconnect) external headset to the 3.5 mm jack on the docking
    station and note the result.

**Expected result**

1. After connecting the external headset to the 3.5 mm jack, a new entry in
    `lsusb` command output should appear.
1. After disconnecting the external headset from the 3.5 mm jack, a headset
    entry in `lsusb` command output should disappear.

## TMD015.002 USB Type-C docking station audio recognition with ME disabled(Windows)

**Test description**

This test aims to verify that the external headset is properly recognized
after plugging in the 3.5 mm jack into the docking station.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a headset jack into the docking station
1. After the `Which device did you plug in` menu appearing, select what type
    of external device has been connected to the laptop (headset).
1. Find the `Speakers` icon in the bottom right part of the screen and click
    it using the right mouse button then using the left mouse button
    click `Sound Settings`.
1. Locate the `All sound device` bar and click on it.
1. Connect(or Disconnect) external headset to the 3.5 mm jack on the docking
    station and note the result.

**Expected result**

1. After connecting the external headset to the 3.5 mm jack, new entries
   regarding the connected headphones should appear in the `Output devices` and
   `Input devices` sections.
1. After disconnecting the external headset from the 3.5 mm jack, the entries
   for connected headset should disappear from the `Output devices` and
   `Input devices` sections.

## TMD016.001 USB Type-C docking station audio playback with ME disabled(Ubuntu)

**Test description**

This test aims to verify that the audio subsystem is able to playback audio
recordings by using the external headset speakers connected to the docking
station.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a headset jack into the docking station.
1. When the `Select Audio Device` menu appears, select what type of external
    device has been connected to the laptop (headset).
1. Open a terminal window and execute the following command:

    ```bash
    pactl set-sink-mute alsa_output.pci-0000_00_1f.3.analog-stereo  0
    pactl set-sink-volume alsa_output.pci-0000_00_1f.3.analog-stereo 65535
    speaker-test
    ```

**Expected result**

Sound should be played from the external speakers.

## TMD016.002 USB Type-C docking station audio playback with ME disabled(Windows)

**Test description**

This test aims to verify that the audio subsystem is able to playback audio
recordings by using the external headset speakers connected to the docking
station.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a headset jack into the docking station.
1. Find the `Speakers` icon in the bottom right part of the screen and click
   it using the left mouse button to open volume menu.
1. After the `Which device did you plug in` menu appearing, select what type
    of external device has been connected to the laptop (headset).
1. In the volume menu, click the rightmost part of it and note the reult.

**Expected result**

Sound should be played from the external speakers.

## TMD017.001 USB Type-C docking station audio capture with ME disabled(Ubuntu)

**Test description**

This test aims to verify that the audio subsystem is able to capture audio
from external headset connected to the docking station.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a headset jack into the docking station.
1. When the `Select Audio Device` menu appears, select what type of external
    device has been connected to the laptop (headset).
1. Open a terminal window and execute the following command:

    ```bash
    arecord -f S16_LE -d 10 -r 16000 /tmp/test-mic.wav
    ```

1. Make some noise for the headset. For example, say something.
1. Execute the following command:

    ```bash
    aplay /tmp/test-mic.wav
    ```

**Expected result**

The recorded audio clip is recorded correctly and played back.

## TMD017.002 USB Type-C docking station audio capture with ME disabled(Windows)

**Test description**

This test aims to verify that the audio subsystem is able to capture audio
from external headset connected to the docking station.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a headset jack into the docking station.
1. After the `Which device did you plug in` menu appearing, select what type
    of external device has been connected to the laptop (headset).
1. Find the `Speakers` icon in the bottom right part of the screen and click
    it using the right mouse button then using the left mouse button
    click `Sound Settings`.
1. Locate the `All sound device` bar and click on it.
1. Select the `Microphone` position in the `Input devices` section.
1. Click on the `Start Test` bar in the `Input settings` section.
1. Create some noise for the DUT to capture and note the result.
    For example, say something.
1. Click on the `Stop Test` bar.

**Expected result**

1. The `Input volume` bar located in the `Input settings` section should raise when
    some noise is being created.
1. The result of the test after clicking the `Stop Test` bar should be more than
    0% of the total volume.

## TMD018.001 USB Type-C docking station SD Card reader detection ME disabled (Ubuntu)

**Test description**

This test aims to verify that the SD Card reader built into the docking station
is enumerated correctly and might be detected by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.
1. The `SD card` put into the slot on the `USB-C docking station`.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

```bash
lsusb | grep "Card Reader"
```

1. Note the result.

**Expected result**

The output from the command should contain information about the connected USB
SD Card Reader.

Example output:

```bash
Bus 002 Device 007: ID 067b:2733 Prolific Technology, Inc. USB SD Card Reader
```

## TMD018.002 USB Type-C docking station SD Card reader detection ME disabled (Windows)

**Test description**

This test aims to verify that the SD Card reader built into the docking station
is enumerated correctly and can be detected by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.
1. The `SD card` put into the slot on the `USB-C docking station`.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open PowerShell and execute the following command:

    ```PowerShell
    Get-PnpDevice -Status "OK" -Class "DiskDrive"
    ```

1. Note the result.

**Expected result**

The output from the command should contain information about the connected USB
SD Card Reader.

Example output:

```powershell
    OK         DiskDrive       SD Card Reader USB Device
```

## TMD019.001 USB Type-C docking station SD Card read/write with ME disabled (Ubuntu)

**Test description**

This test aims to verify that the SD Card reader is initialized correctly and
can be used from the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.
1. The `SD card` put into the slot on the `USB-C docking station`.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following commands to identify the SD
    card mounting point:

    ```bash
    lsblk | grep "sd"
    ```

1. Execute the following commands for generating, copying and comparing
    generated file:

    ```bash
    dd if=/dev/urandom of=/tmp/in.bin bs=4K count=100
    dd if=/tmp/in.bin of=/dev/sda bs=4K count=100
    dd if=/dev/sda of=/tmp/out.bin bs=4K count=100
    sha256sum /tmp/in.bin /tmp/out.bin
    ```

1. Note the result.

**Expected result**

1. The output from the command to identify the SD card mounting point should
    return information about the SD card mounting location.

    Example output:

    ```bash
    sda           8:0    1  29,5G  0 disk
    └─sda1        8:1    1  29,5G  0 part /media/user/DCB0-C7E8
    sdb           8:16   1     0B  0 disk
    ```

1. The output from the last command should contain 2 identical checksums.

    Example output

    ```bash
    2083776668ed0c8095a9ac42188153c02f360e116c14b36d2ef5c98665d75dcb  /tmp/in.bin
    2083776668ed0c8095a9ac42188153c02f360e116c14b36d2ef5c98665d75dcb  /tmp/out.bin
    ```

## TMD019.002 USB Type-C docking station SD Card read/write with ME disabled (Windows)

**Test description**

This test aims to verify that the SD Card reader is initialized correctly and
can be used from the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The `USB-C docking station` connected to the USB-C port.
1. The `SD card` put into the slot on the `USB-C docking station`.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Determine the localization of the mounted SD card.
1. Open PowerShell and execute the following commands:

    ```powershell
    New-Item -Path "${drive_location}:\" -Name "testfile.txt" -ItemType "file" -Value "This is a test string."
    Get-Content -Path "${drive_location}:\testfile.txt"
    ```

1. Note the result.

**Expected result**

The last command should return the following message: `This is a test string.`

## TMD020.001 USB Type-C PD current limiting with ME disabled (Ubuntu)

**Test description**

This test aims to verify that the power draw from a USB-C PD power supply does
not exceed the limits of the power supply's specifications.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test steps**
1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Attach a 65W USB-C power supply, with the power meter between the power
    supply and the laptop's Thunderbolt 4 port.
1. Open a terminal window and run the following command, while observing the
    power meter's display:

    ```bash
    stress-ng -c 20 -t 5
    ```

1. Repeat the step above 5 times, noting the maximum power draw shown on the
    power meter each time.

**Expected result**

The power draw does not exceed more than 105% of the power supply's nominal
power. The power meter's display stays lit all the time, indicating that the
power supply's over-current protection was not triggered.

## TMD020.002 USB Type-C PD current limiting with ME disabled (Windows)

**Test description**

This test aims to verify that the power draw from a USB-C PD power supply does
not exceed the limits of the power supply's specifications.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test steps**
1. Power on the DUT.
1. While the DUT is booting, hold the BIOS_SETUP_KEY to enter the UEFI Setup Menu.
1. Enter the Dasharo System Features menu using the arrow keys and Enter.
1. Enter the Intel Management Engine Options submenu.
1. Verify that the Intel ME mode option is in state Disable (HAP) or
Disable (Soft) - if not, using the arrow keys and Enter, choose option
Disable (HAP) or Disable (Soft).
1. Press F10 to save the changes.
1. If necessary - press Y to confirm saving the changes.
1. Go back to the main menu using the ESC key.
1. Select the Reset option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Download and install [ThrottleStop](https://www.techpowerup.com/download/techpowerup-throttlestop/)
1. Attach a 65W USB-C power supply, with the power meter between the power
    supply and the laptop's Thunderbolt 4 port.
1. Open ThrottleStop.
1. Click the `Limits` button to open a window displaying current throttle status
    and reasons.
1. Click the `TS Bench` button to open the benchmark window.
1. Start a benchmark with the default parameters (Normal, 16 threads, 120M,
    Fixed MHz), while observing the power meter's display.
1. Repeat the step above 5 times, noting the maximum power draw shown on the
    power meter each time.

**Expected result**

The power draw does not exceed more than 105% of the power supply's nominal
power. The power meter's display stays lit all the time, indicating that the
power supply's over-current protection was not triggered. When the power draw
approaches or exceeds 100% of the AC adapter's rating (65W), the field
`EDP Other` in the ThrottleStop Limit Reasons window is colored red.
