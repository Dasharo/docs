# Dasharo Compatibility: USB-C/Thunderbolt support with charging and display

## Test cases common documentation

The test suite is mostly fully automated. Only manual test cases are documented.
Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS preparation](../generic-test-setup.md#os-preparation).
1. Proceed with the
   [Generic test setup: OS post installation steps](../generic-test-setup.md#post-installation).

## UTC001.001 USB Type-A charging capability

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

## UTC001.002 USB Type-A charging capability with ME disabled

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

## UTC002.001 Thunderbolt 4 USB Type-C power output

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
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect a phone to the Thunderbolt 4 USB Type-C port located on the left side
    of the laptop using a USB cable.
1. Note the charging status on the phone screen.

**Expected result**

1. The smartphone should indicate that it's charging.

## UTC002.002 Thunderbolt 4 USB Type-C power output with ME disabled

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

## UTC007.001 USB Type-C docking station Triple display (Ubuntu)

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
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Switch the display mode between `Mirror` and `Join Displays`.

**Expected result**

The image should be displayed on the three external displays in `Mirror` and
`Join Displays` modes.

## UTC007.002 USB Type-C docking station Triple display (Windows)

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
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. If using more than one display, switch the display mode between `Duplicate`
   and `Extend`.

**Expected result**

The image should be displayed on the three external displays in `Duplicate` and
`Extend` modes.

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

## UTC007.006 USB Type-C docking station Triple display with ME disabled(Windows)

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

## UTC011.001 USB Type-C docking station USB devices recognition (firmware)

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
1. Hold the `BIOS_MENU_KEY` to enter the BIOS Menu.
1. Check if the `USB storage` is available on the list.

**Expected result**

The `USB storage` is available which confirms successful recognition.

## UTC011.004 USB Type-C docking station USB devices recognition ME disabled (firmware)

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

## UTC012.001 USB Type-C docking station USB keyboard (firmware)

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

1. Power on the DUT
1. Hold the `BIOS_MENU_KEY` to enter the Bios Menu.
1. Use the arrow keys, Esc key and the Enter key to navigate the menus.

**Expected result**

All menus can be entered using the external USB keyboard.

## UTC013.001 USB Type-C docking station upload 1GB file on USB storage (Ubuntu)

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

## UTC013.002 USB Type-C docking station upload 1GB file on USB storage(Windows)

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

## UTC013.003 USB Type-C docking station upload 1GB file on USB storage with ME disabled(Ubuntu)

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

## UTC013.004 USB Type-C docking station upload 1GB file on USB storage with ME disabled(Windows)

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

## UTC016.001 USB Type-C docking station audio playback (Ubuntu)

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

## UTC016.002 USB Type-C docking station audio playback (Windows)

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
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a headset jack into the docking station.
1. Find the `Speakers` icon in the bottom right part of the screen and click
   it using the left mouse button to open volume menu.
1. After the `Which device did you plug in` menu appearing, select what type
    of external device has been connected to the laptop (headset).
1. In the volume menu, click the rightmost part of it and note the result.

**Expected result**

Sound should be played from the external speakers.

## UTC016.003 USB Type-C docking station audio playback with ME disabled(Ubuntu)

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

## UTC016.004 USB Type-C docking station audio playback with ME disabled(Windows)

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
1. In the volume menu, click the rightmost part of it and note the result.

**Expected result**

Sound should be played from the external speakers.

## UTC017.001 USB Type-C docking station audio capture (Ubuntu)

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

## UTC017.002 USB Type-C docking station audio capture (Windows)

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
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a headset jack into the docking station.
1. After the `Which device did you plug in` menu appearing, select what type
    of external device has been connected to the laptop (headset).
1. Find the `Speakers` icon in the bottom right part of the screen and click
    it using the right mouse button then using the left mouse button
    click `Sound Settings`.
1. Locate the `All sound devices` bar and click on it.
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

## UTC017.003 USB Type-C docking station audio capture with ME disabled(Ubuntu)

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

## UTC017.004 USB Type-C docking station audio capture with ME disabled(Windows)

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
1. Locate the `All sound devices` bar and click on it.
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

## UTC020.002 USB Type-C PD current limiting (Windows)

**Test description**

This test aims to verify that the power draw from a USB-C PD power supply does
not exceed the limits of the power supply's specifications.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test steps**
1. Power on the DUT.
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

## UTC020.003 USB Type-C PD current limiting with ME disabled (Ubuntu)

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

## UTC020.004 USB Type-C PD current limiting with ME disabled (Windows)

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
