# Dasharo compatibility: Docking station USB devices

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).
1. The docking station connected to the USB-C port.
1. The `USB_STICK` connected to the docking station.

### DUB001.001 USB devices recognition (firmware)

**Test description**

This test aims to verify that the external USB devices connected to the docking
station are recognized correctly by the `FIRMWARE`.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BIOS_MENU_KEY` to enter the BIOS Menu.
1. Check if the `USB_STICK` is available on the list.

**Expected result**

The `USB_STICK` is available which confirms successful recognition.

### DUB001.002 USB devices recognition (Ubuntu 22.04)

**Test description**

This test aims to verify that the external USB devices connected to the docking
station are recognized correctly by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
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

### DUB001.003 USB devices recognition (Windows 11)

**Test description**

This test aims to verify that the external USB devices connected to the docking
station are recognized correctly by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open PowerShell and and run the following command:

    ```powershell
    Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }
    ```

1. Note the results.

**Expected result**

1. After executing the command, a list containing all USB devices should
be displayed. The list should contain the `USB_STICK`, which is plug in.

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

### DUB002.001 USB keyboard recognition (firmware)

**Test description**

This test aims to verify that the external USB keyboard connected to the docking
station is detected correctly by the `FIRMWARE` and all basic keys work
according to their labels.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the [Common](#common) section.
1. The external USB keyboard connected to the docking station.

**Test steps**

1. Power on the DUT
1. Hold the `BIOS_MENU_KEY` to enter the Bios Menu.
1. Use the arrow keys, Esc key and the Enter key to navigate the menus.

**Expected result**

1. All menus can be entered using the external USB keyboard.

### DUB002.002 USB keyboard detection (Ubuntu 22.04)

**Test description**

This test aims to verify that the external USB keyboard connected to the docking
station is detected correctly by the `OPERATING_SYSTEM` and all basic keys work
according to their labels.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.
1. Install the `libinput-tools` package: `sudo apt install libinput-tools`.
1. Connect the external USB keyboard using the USB port.

**Test steps**

1. Power on the DUT.
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

### DUB002.003 USB keyboard recognition (Windows 11)

**Test description**

This test aims to verify that the external USB keyboard is detected correctly
by the `OPERATING_SYSTEM` and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.
1. Connect the external USB keyboard using the USB port.

**Test steps**

1. Power on the DUT.
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
