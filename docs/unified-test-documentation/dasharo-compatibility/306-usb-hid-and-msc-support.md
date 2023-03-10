# Dasharo compatibility: USB HID and MSC Support

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

## USB001.001 USB devices detection (firmware)

**Test description**

This test aims to verify that the external USB devices are detected
correctly by the firmware and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Connect the flash drive using the USB port.

**Test steps**

1. Power on the DUT.
1. Enter the boot menu using the `BIOS_SETUP_KEY`.
1. Select the `Boot Menu`, press `Enter` and note the result.

**Expected result**

1. Flash drive entry is listed in the boot menu.

## USB001.002 USB devices detection in OS (Ubuntu 22.04)

**Test description**

This test aims to verify that the external USB devices are detected
correctly by the `OPERATING_SYSTEM` and all basic keys work according to their
labels.

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

1. Connect external USB devices to DUT USB A port and note the result.

**Expected result**

1. After each device is connected to the USB port, a new USB device entry
    in `lsusb` command output should appear.

## USB001.003 USB devices detection in OS (Windows 11)

**Test description**

This test aims to verify that the external USB devices are detected correctly
by the `OPERATING_SYSTEM` and all basic keys work according to their labels.

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

    ```bash
    Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }
    ```

1. Note the results.

**Expected result**

1. After executing the command, a list containing all USB devices should
be displayed. All devices' status should be `OK`.

    Example output:

    ```bash
    Status     Class           FriendlyName
    ------     -----           ------------
    OK         DiskDrive       Mass Storage Device USB Device
    OK         USB             Generic USB Hub
    OK         HIDClass        USB Input Device
    OK         Bluetooth       Intel(R) Wireless Bluetooth(R)
    OK         USB             USB Root Hub (USB 3.0)
    OK         Net             TP-LINK Gigabit Ethernet USB Adapter
    OK         USB             Generic USB Hub
    OK         USB             USB Mass Storage Device
    ```

## USB002.001 USB keyboard detection (firmware)

**Test description**

This test aims to verify that the external USB keyboard is detected correctly
by the firmware and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Connect the external USB keyboard using the USB port.

**Test steps**

1. Power on the DUT
1. Enter the boot menu using the `BIOS_SETUP_KEY`.
1. Use the arrow keys, Esc key and the Enter key to navigate the menus.

**Expected result**

1. All menus can be entered using the external USB keyboard.

## USB002.002 USB keyboard detection (Ubuntu 22.04)

**Test description**

This test aims to verify that the external USB keyboard is detected correctly
by the `OPERATING_SYSTEM` and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `libinput-tools` on the DUT.
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

## USB002.003 USB keyboard detection (Windows 11)

**Test description**

This test aims to verify that the external USB keyboard is detected correctly
by the `OPERATING_SYSTEM` and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Connect the external USB keyboard using the USB port.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open PowerShell and run the following command:

    ```bash
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

1. After running the PowerShell command information about connected keyboard
    should be displayed.

    Example output:

    ```bash
    Caption                     : Enhanced (101- or 102-key)
    Description                 : USB Input Device
    InstallDate                 :
    Name                        : Enhanced (101- or 102-key)
    Status                      : OK
    Availability                :
    ConfigManagerErrorCode      : 0
    ConfigManagerUserConfig     : False
    CreationClassName           : Win32_Keyboard
    DeviceID                    : USB\VID_046D&PID_C31C&MI_00\6&26C21341&0&0000
    ErrorCleared                :
    ErrorDescription            :
    LastErrorCode               :
    PNPDeviceID                 : USB\VID_046D&PID_C31C&MI_00\6&26C21341&0&0000
    PowerManagementCapabilities :
    PowerManagementSupported    : False
    StatusInfo                  :
    SystemCreationClassName     : Win32_ComputerSystem
    SystemName                  : DESKTOP-CUR9H2J
    IsLocked                    :
    Layout                      : 00000409
    NumberOfFunctionKeys        : 12
    Password                    :
    PSComputerName              :
    ```

1. All standard keyboard keys generate correct characters
   or actions when pressed.
1. Key combinations are detected correctly.

## USB003.001 Upload 1GB file on USB storage (Ubuntu 22.04)

**Test description**

This test aims to verify that the 1GB file can be transferred from the
`OPERATING_SYSTEM` to the `USB storage`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04
1. `USB storage` - at least 1GB of free space

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

1. Plug in the `USB storage` to the USB port.
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

## USB003.002 Upload 1GB file on USB storage (Windows 11)

**Test description**

This test aims to verify that the 1GB file can be transferred from the
`OPERATING_SYSTEM` to the `USB storage`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11
1. `USB storage` - at least 1GB of free space

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

1. Plug in the `USB storage` to the USB port.
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
