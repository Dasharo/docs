# Dasharo compatibility: USB-C docking station USB devices

## Test cases common documentation

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
1. The `USB storage` connected to the docking station.

## DUB001.001 USB devices recognition (firmware)

**Test description**

This test aims to verify that the external USB devices connected to the docking
station are recognized correctly by the `FIRMWARE`.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Hold the `BIOS_MENU_KEY` to enter the BIOS Menu.
1. Check if the `USB storage` is available on the list.

**Expected result**

The `USB storage` is available which confirms successful recognition.

## DUB001.002 USB devices recognition (Ubuntu 22.04)

**Test description**

This test aims to verify that the external USB devices connected to the docking
station are recognized correctly by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

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

## DUB001.003 USB devices recognition (Windows 11)

**Test description**

This test aims to verify that the external USB devices connected to the docking
station are recognized correctly by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

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

## DUB002.001 USB keyboard recognition (firmware)

**Test description**

This test aims to verify that the external USB keyboard connected to the docking
station is detected correctly by the `FIRMWARE` and all basic keys work
according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The external USB keyboard connected to the docking station.

**Test steps**

1. Power on the DUT
1. Hold the `BIOS_MENU_KEY` to enter the Bios Menu.
1. Use the arrow keys, Esc key and the Enter key to navigate the menus.

**Expected result**

All menus can be entered using the external USB keyboard.

## DUB002.002 USB keyboard detection (Ubuntu 22.04)

**Test description**

This test aims to verify that the external USB keyboard connected to the docking
station is detected correctly by the `OPERATING_SYSTEM` and all basic keys work
according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `libinput-tools` package: `sudo apt install libinput-tools`.
1. The external USB keyboard connected to the docking station.

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

## DUB002.003 USB keyboard recognition (Windows 11)

**Test description**

This test aims to verify that the external USB keyboard is detected correctly
by the `OPERATING_SYSTEM` and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. The external USB keyboard connected to the docking station.

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

## DUB003.001 Upload 1GB file on USB storage (Ubuntu 22.04)

**Test description**

This test aims to verify that the 1GB file can be transferred from the
`OPERATING_SYSTEM` to the `USB storage` connected to the docking station.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
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

## DUB003.002 Upload 1GB file on USB storage (Windows 11)

**Test description**

This test aims to verify that the 1GB file can be transferred from the
`OPERATING_SYSTEM` to the `USB storage` connected to the docking station.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
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
