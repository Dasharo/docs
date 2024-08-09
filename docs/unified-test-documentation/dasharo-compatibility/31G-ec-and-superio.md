# Dasharo Compatibility: Embedded Controller and Super I/O initialization

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

## ECR001.001 Battery monitoring - charge level in OS (Ubuntu)

**Test description**

This test verifies whether the battery charge level is reported in the OS.

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
1. Locate the power menu in the upper right corner of the screen.
1. Open the power menu and locate the battery status indicator.

**Expected result**

1. The battery status indicator should show the current charge level (percentage
    left).

## ECR001.002 Battery monitoring - charge level in OS (Windows)

**Test description**

This test verifies whether the battery charge level is reported in the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Locate the power menu in the lower right corner of the screen.

**Expected result**

1. The battery status indicator should show the current charge level (percentage
    left).

## ECR001.003 Battery start charge threshold

**Test description**

The setup menu allows you to set your own threshold for the start of battery
charging, which defines the level above which the battery will not start to
charge. The aim of this test is to check that functionality.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter Dasharo Setup Menu
1. Enter **Dasharo System Features**
1. Enter **Power Management Options**
1. Set **Battery Start Charge Threshold** to e.g. 60%
1. Discharge the battery below the previously set level
1. Charge battery above the previously set level
1. Reconnect charging cable

**Expected result**

After reconnecting the charging cable, the battery should not start charging.

## ECR001.004 Battery stop charge threshold

**Test description**

The setup menu allows you to set your own threshold for the stop of battery
charging, which defines the level above which the battery will stop charging.
The aim of this test is to check that functionality.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter Dasharo Setup Menu
1. Enter **Dasharo System Features**
1. Enter **Power Management Options**
1. Set **Battery Stop Charge Threshold** to desired value
1. Wait until the battery is charged to the stop threshold.

**Expected result**

The battery should stop charging at stop threshold.

## ECR002.001 Battery monitoring - charging state in OS (Ubuntu)

**Test description**

This test verifies that the power supply state is detected correctly in the OS.

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
1. Locate the power menu in the upper right corner of the screen.
1. Open the power menu and locate the battery status indicator.
1. Note the current state.
1. Unplug the power supply and wait for the battery charge state to change to
    `Discharging`.
1. Plug in the power supply and wait for the battery charge state to change to
    `Charging`.

**Expected result**

1. The battery charge indicator should correctly show whether the power supply
    is plugged in or not.
1. The battery charge indicator should detect the AC adapter state change
    within seconds of the adapter being plugged in/out.

## ECR002.002 Battery monitoring - charging state in OS (Windows)

**Test description**

This test verifies that the power supply state is detected correctly in the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Locate the power menu in the lower right corner of the screen.
1. Open the power menu and locate the battery status indicator.
1. Note the current state.
1. Unplug the power supply and wait for the battery charge state to change to
    `on battery`.
1. Plug in the power supply and wait for the battery charge state to change to
    `plugged in`.

**Expected result**

1. The battery charge indicator should correctly show whether the power supply
   is plugged in or not.
1. The battery charge indicator should detect the AC adapter state change
   within seconds of the adapter being plugged in / out.

## ECR003.001 Touchpad in OS - (Ubuntu)

**Test description**

This test verifies that the touchpad is initialized correctly and is detected
by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `libinput-tools` on the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Verify that the cursor can be moved with the touchpad and that clicking works
    (test both clicking and tapping).
1. Run `sudo libinput debug-events` in the terminal:
    1. Verify that scrolling with 2 fingers generates a `POINTER_AXIS` event,
    1. Verify that pinching with 2 fingers generates a `GESTURE_PINCH_UPDATE` event.
1. Press `Ctrl + C` to terminate the `libinput` program.

**Expected result**

1. Moving the cursor, clicking, zooming and scrolling are detected correctly by
   the operating system.

## ECR003.002 Touchpad in OS - (Windows)

**Test description**

This test verifies that the touchpad is initialized correctly and is detected
by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Verify that the cursor can be moved with the touchpad and that clicking
    works (test both clicking and tapping).
1. Open `C:\Windows` in `Windows Explorer`
    1. Verify that scrolling with 2 fingers moves the content of the window,
    1. Verify that pinching with 2 fingers zooms in and zooms out the content.

**Expected result**

1. Moving the cursor, clicking, zooming and scrolling are detected correctly by
   the operating system.

## ECR004.001 Keyboard (standard keypad) in firmware

**Test description**

This test verifies that the keyboard is detected correctly by the firmware
and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware)

**Test steps**

1. Power on the DUT and press the `BIOS_SETUP_KEY` to enter the setup menu.
1. Use the arrow keys and the Enter key to navigate the menus.

**Expected result**

1. All menus can be entered using the internal keyboard.

## ECR004.002 Keyboard (standard keypad) in OS (Ubuntu)

**Test description**

This test verifies that the keyboard is detected correctly by the operating
system and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `libinput-tools` on the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Run `sudo libinput debug-events --show-keycodes` in the terminal.
1. Press each keyboard key and check the generated keycode.

**Expected result**

1. All standard keyboard keys generate the correct keycodes and events as per
    their labels.
1. Key combinations are detected correctly.

## ECR004.003 Keyboard (standard keypad) in OS (Windows)

**Test description**

This test verifies that the keyboard is detected correctly by the operating
system and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open `notepad`
    1. Test the alphanumeric keys and note the generated characters
    1. Test non-alphanumeric keys and verify that they generate the signs
    1. Test key combinations with the `Shift`, and `Alt` modifier keys
1. Open `On-Screen Keyboard` and press `Ctrl` key on the hardware keyboard.
   Check if `On-Screen Keyboard` correctly highlights it.
1. Open `Start menu` and press `Esc`. Check if `Start menu` is properly closed.

**Expected result**

1. All standard keyboard keys generate correct characters
   or actions when pressed.
1. Key combinations are detected correctly.

## ECR005.001 Keyboard (function key: play/pause) in OS (Ubuntu)

**Test description**

This test verifies that the play/pause hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `libinput-tools` on the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Run `sudo libinput debug-events --show-keycodes` in the terminal.
1. Verify that pressing the play/pause key generates a `KEY_PLAYPAUSE` event.

**Expected result**

1. Pressing the play/pause hotkey generates a `KEY_PLAYPAUSE` event.

## ECR005.002 Keyboard (function key: play/pause) in OS (Windows)

**Test description**

This test verifies that the play/pause hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Start `Groove Music`
1. Verify that when pressing the `play/pause` button, player menu appears
    in the upper left part of the screen for a few seconds.

**Expected result**

1. Pressing the play/pause hotkey is properly detected by the OS

## ECR006.001 Keyboard (function key: cooling mode) in OS (Ubuntu)

**Test description**

This test verifies that the cooling mode hotkey works correctly.

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
1. Press the cooling mode hotkey (Fn + 1) once and note the effect.
1. Press the cooling mode hotkey once again and note the effect.

**Expected result**

1. Pressing the hotkey once should activate the cooling mode (fans should
   spin up to their maximum speed).
1. Pressing the hotkey again should deactivate the cooling mode (fans should
   return to normal).

## ECR006.002 Keyboard (function key: cooling mode) in OS (Windows)

**Test description**

This test verifies that the cooling mode hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the cooling mode hotkey (Fn + 1) once and note the effect.
1. Press the cooling mode hotkey once again and note the effect.

**Expected result**

1. Pressing the hotkey once should activate the cooling mode (fans should
   spin up to their maximum speed).
1. Pressing the hotkey again should deactivate the cooling mode (fans should
   return to normal).

## ECR007.001 Keyboard (function key: touchpad on/off) in OS (Ubuntu)

**Test description**

This test verifies that the touchpad on/off hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Create a file `/etc/udev/hwdb.d/60-keyboard.hwdb` with the following contents:

    ```bash
    evdev:atkbd:dmi:bvn*:bvr*:svnNotebook:pnNV4XMB,ME,MZ:*
             KEYBOARD_KEY_f7=191
             KEYBOARD_KEY_f8=191
    ```

1. Execute the following commands:

```bash
sudo systemd-hwdb update
sudo udevadm trigger
```

**Test steps**

1. Press the touchpad on/off key and try to use the touchpad.
1. Press the touchpad on/off key once again and try to use the touchpad again.

**Expected result**

1. Pressing the hotkey once should deactivate the touchpad (touchpad should be
   completely inoperable).
1. Pressing the hotkey again should reactivate the touchpad.

## ECR007.002 Keyboard (function key: touchpad on/off) in OS (Windows)

**Test description**

This test verifies that the touchpad on/off hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the touchpad on/off key and try to use the touchpad.
1. Press the touchpad on/off key once again and try to use the touchpad again.

**Expected result**

1. Pressing the hotkey once should deactivate the touchpad (touchpad should be
   completely inoperable).
1. Pressing the hotkey again should reactivate the touchpad.

## ECR008.001 Keyboard (function key: display on/off) in OS (Ubuntu)

**Test description**

This test verifies that the display on/off hotkey works correctly.

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
1. Press the display on/off hotkey once and note the effect.
1. Press any key on the keyboard and note the effect.

**Expected result**

1. Pressing the hotkey once should turn the internal LCD panel off.
1. Pressing any key on the keyboard should power the internal LCD panel back on.

## ECR008.002 Keyboard (function key: display on/off) in OS (Windows)

**Test description**

This test verifies that the display on/off hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the display on/off hotkey once and note the effect.
1. Press any key on the keyboard and note the effect.

**Expected result**

1. Pressing the hotkey once should turn the internal LCD panel off.
1. Pressing any key on the keyboard should power the internal LCD panel
    back on.

## ECR009.001 Keyboard (function key: mute) in OS (Ubuntu)

**Test description**

This test verifies that the volume mute hotkey works correctly.

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
1. Press the volume mute hotkey twice and note the effect each keypress has.

**Expected result**

1. Pressing the hotkey should mute or unmute the currently enabled audio output.
1. Each keypress should cause a mute/unmute notification to appear in the middle
   of the screen.

## ECR009.002 Keyboard (function key: mute) in OS (Windows)

**Test description**

This test verifies that the mute hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the mute hotkey once and check the volume indicator in the bottom right
   part of the screen.
1. Press the mute hotkey once and check the volume indicator again.

**Expected result**

1. Pressing the hotkey once should mute the device
1. Pressing the hotkey again should re-enable the sound

## ECR010.001 Keyboard (function key: keyboard backlight) in OS (Ubuntu)

**Test description**

This test verifies that the keyboard backlight hotkey works correctly.

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
1. Press the keyboard backlight hotkey 6 times and note the effect on the
   keyboard backlight after each keypress.

**Expected result**

1. The keyboard has 6 backlight settings from 0% to 100% Each keypress should
   set the keyboard to the next mode, with the last mode wrapping back around
   to the first.

## ECR010.002 Keyboard (function key: keyboard backlight) in OS (Windows)

**Test description**

This test verifies that the keyboard backlight hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the keyboard backlight hotkey 6 times and note the effect on the
   keyboard backlight after each keypress.

**Expected result**

1. The keyboard has 6 backlight settings from 0% to 100% Each keypress should
   set the keyboard to the next mode, with the last mode wrapping back around
   to the first.

## ECR011.001 Keyboard (function key: volume down) in OS (Ubuntu)

**Test description**

This test verifies that the volume down hotkey works correctly.

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
1. Press the volume down hotkey once and note the effects.

**Expected result**

1. Pressing the hotkey should decrease the volume of the currently enabled audio
   output.
1. Each key press should cause a volume down notification to appear in the
   middle of the screen.

## ECR011.002 Keyboard (function key: volume down) in OS (Windows)

**Test description**

This test verifies that the volume down hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the volume down hotkey once and note the effects.

**Expected result**

1. Pressing the hotkey should decrease the volume of the currently enabled audio
   output.
1. Each key press should cause a volume down notification to appear in the upper
   left part of the screen.

## ECR012.001 Keyboard (function key: volume up) in OS (Ubuntu)

**Test description**

This test verifies that the volume up hotkey works correctly.

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
1. Press the volume up hotkey once and note the effects.

**Expected result**

1. Pressing the hotkey should increase the volume of the currently enabled audio
   output.
1. Each key press should cause a volume up notification to appear in the middle
   of the screen.

## ECR012.002 Keyboard (function key: volume up) in OS (Windows)

**Test description**

This test verifies that the volume up hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the volume down hotkey once and note the effects.

**Expected result**

1. Pressing the hotkey should increase the volume of the currently enabled audio
   output.
1. Each key press should cause a volume up notification to appear in the upper
   left part of the screen.

## ECR013.001 Keyboard (function key: display switch) in OS (Ubuntu)

**Test description**

This test verifies that the display switch hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `libinput-tools` on the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Run `sudo libinput debug-events --show-keycodes` in the terminal.
1. Press the display switch hotkey once and note the effect.

**Expected result**

1. Pressing the hotkey should yield the following output in the terminal:

    ```bash
    -event3   KEYBOARD_KEY     +0.000s	KEY_LEFTMETA (125) pressed
     event3   KEYBOARD_KEY     +0.004s	KEY_P (25) pressed
     event3   KEYBOARD_KEY     +0.010s	KEY_P (25) released
     event3   KEYBOARD_KEY     +0.015s	KEY_LEFTMETA (125) released
    ```

## ECR013.002 Keyboard (function key: display switch) in OS (Windows)

**Test description**

This test verifies that the display switch hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the display switch hotkey once and note the effect.

**Expected result**

1. Pressing the hotkey should cause the display settings bar to appear
    on the right part of the screen.

## ECR014.001 Keyboard (function key: brightness down) in OS (Ubuntu)

**Test description**

This test verifies that the brightness down hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test steps**

1. Press the brightness down hotkey once and note the effects.

**Expected result**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Pressing the hotkey should decrease the brightness of the internal LCD
   display.
1. Each key press should cause a brightness down notification to appear in the
   middle of the screen.

## ECR014.002 Keyboard (function key: brightness down) in OS (Windows)

**Test description**

This test verifies that the brightness down hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the brightness down hotkey once and note the effects.

**Expected result**

1. Pressing the hotkey should decrease the brightness of the internal LCD
   display.
1. Each key press should cause a brightness down notification to appear in the
   top left of the screen.

## ECR015.001 Keyboard (function key: brightness up) in OS (Ubuntu)

**Test description**

This test verifies that the brightness up hotkey works correctly.

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
1. Press the brightness up hotkey once and note the effects.

**Expected result**

1. Pressing the hotkey should increase the brightness of the internal LCD
   display.
1. Each key press should cause a brightness up notification to appear in the
   middle of the screen.

## ECR015.002 Keyboard (function key: brightness up) in OS (Windows)

**Test description**

This test verifies that the brightness down hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the brightness up hotkey once and note the effects.

**Expected result**

1. Pressing the hotkey should increase the brightness of the internal LCD
   display.
1. Each key press should cause a brightness up notification to appear in the
   top left of the screen.

## ECR016.001 Keyboard (function key: camera on/off) in OS (Ubuntu)

**Test description**

This test verifies that the camera on/off hotkey works correctly.

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
1. Open the terminal and run the command: `watch -n1 lsusb`.
1. Press the camera on/off hotkey twice and note the effect after each
    keypress.

**Expected result**

1. Pressing the hotkey once should make the
    `Chicony Electronics Co., Ltd Chicony USB2.0 Camera` device disappear
    from the output of `lsusb`.
1. Pressing the hotkey again should make the USB device reappear.

## ECR016.002 Keyboard (function key: camera on/off) in OS (Windows)

**Test description**

This test verifies that the camera on/off hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open the `Camera` app.
1. Press the camera on/off hotkey twice and note the effect after
   a few seconds after the keypress.

**Expected result**

1. Pressing the hotkey once should make the camera image disappear.
1. Pressing the hotkey again should make the camera image appear again
   after a few seconds.

## ECR017.001 Keyboard (function key: flight mode) in OS (Ubuntu)

**Test description**

This test verifies that the flight mode hotkey works correctly.

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
1. Locate and open the power menu in the upper right corner of the screen.
1. Enter Settings and navigate to the Wi-Fi panel.
1. Note the current state of the Airplane Mode switch.
1. Press the flight mode hotkey twice and note the result of each keypress.

**Expected result**

1. Pressing the hotkey once should enable airplane mode.
1. Pressing the hotkey again should disable airplane mode.

## ECR017.002 Keyboard (function key: flight mode) in OS (Windows)

**Test description**

This test verifies that the flight mode hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the camera on/off hotkey twice and note the effect after the key press.

**Expected result**

1. Pressing the hotkey once should enable airplane mode and cause
   `airplane mode on` notification to appear in the top right
   part of the screen.
1. Pressing the hotkey again should disable airplane mode and cause
   `airplane mode off` notification to appear in the top right
   part of the screen.

## ECR018.001 Keyboard (function key: sleep) in OS (Ubuntu)

**Test description**

This test verifies that the sleep hotkey works correctly.

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
1. Press the sleep hotkey once and note the result.

**Expected result**

1. The laptop should go to sleep within seconds of the hotkey being pressed.
1. The power LED should be blinking green, indicating the laptop is sleeping.

## ECR018.002 Keyboard (function key: sleep) in OS (Windows)

**Test description**

This test verifies that the sleep hotkey works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Proceed with the
    [Installing updates and drivers](/unified/clevo/post-install/#windows-11)
    section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Wait 30 seconds for the system to load fully.
1. Press the sleep hotkey once and note the result.

**Expected result**

1. The laptop should go to sleep within seconds of the hotkey being pressed.
1. The power LED should be blinking green, indicating the laptop is sleeping.

## ECR019.001 Buttons (button: power) in OS (Ubuntu)

**Test description**

This test verifies that the power button is detected correctly by the operating
system. In Ubuntu 22.04 OS the default function assigned to this key is suspend
mode.

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
1. Open the terminal and run the following command to check the power button
    action:

    ```bash
    gsettings get org.gnome.settings-daemon.plugins.power power-button-action
    ```

1. If the status is other than `suspend` run the following command to change
   the power button action:

    ```bash
    gsettings set org.gnome.settings-daemon.plugins.power power-button-action "suspend"
    ```

1. Check the power button action again by running the following command:

    ```bash
    gsettings get org.gnome.settings-daemon.plugins.power power-button-action
    ```

1. Press the power button once and note the result.
1. Press `Enter` and note the result.
1. Run the following command to check last finished operation:

    ```bash
    journalctl | grep systemd-logind | tail -1
    ```

**Expected result**

1. Pressing the button once should make laptop enter sleep mode.
1. The power LED should be blinking green, indicating the laptop is sleeping.
1. After completing the 5th step device should wake up.
1. The output of the last command should contain the line:

    ```bash
    Operation 'sleep' finished
    ```

## ECR019.002 Buttons (button: power) in OS (Windows)

**Test description**

This test verifies that the power button is detected correctly by the operating
system. In Windows 11 OS the default function assigned to this key is sleep
mode.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Proceed with the
    [Installing updates and drivers](/unified/clevo/post-install/#windows-11)
    section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Wait 30 seconds for the system to load fully.
1. Press the power button once and note the result.

**Expected result**

1. Pressing the button once should make laptop enter sleep mode.
1. The power LED should be blinking green, indicating the laptop is sleeping.

## ECR020.001 Buttons (button: lid switch) in OS (Ubuntu)

**Test description**

This test verifies that the lid switch is detected correctly by the operating
system.

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
1. Open one terminal window and run the following command:

    ```bash
    sudo systemd-inhibit --what handle-lid-switch --mode block watch echo "Inhibiting lid switch"
    ```

1. Open another terminal and run the command
    `sleep 5 && cat /proc/acpi/button/lid/LID0/state` to read the state of
    the lid while it is closed.
1. Close the lid and wait 5 seconds.
1. Open the lid and note the output of the command.
1. Run the command `cat /proc/acpi/button/lid/LID0/state` while the lid is
    open and note the output.

**Expected result**

1. The output of the second command should report that the lid is closed.
1. The output of the third command should report that the lid is open.

## ECR020.002 Buttons (button: lid switch) in OS (Windows)

**Test description**

This test verifies that the lid switch is detected correctly by the operating
system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Proceed with the
    [Installing updates and drivers](/unified/clevo/post-install/#windows-11)
    section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Wait 30 seconds for the system to load fully.
1. Close the lid and note the effect on the power LED.

**Expected result**

1. Pressing the button once should make laptop enter sleep mode.
1. The power LED should be blinking green, indicating the laptop is sleeping.

## ECR021.001 Keyboard (function key: RGB keyboard toggle) in OS (Ubuntu)

**Test description**

This test verifies that the RGB keyboard toggle hotkey is handled properly by
the operating system.

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
1. Press the RGB keyboard toggle hotkey twice and note the result each time.

**Expected result**

1. Pressing the button once should disable the keyboard backlight.
1. Pressing the button again should re-enable the keyboard backlight.

## ECR021.002 Keyboard (function key: RGB keyboard toggle) in OS (Windows)

**Test description**

This test verifies that the RGB keyboard toggle hotkey is handled properly by
the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the RGB keyboard toggle hotkey twice and note the result each time.

**Expected result**

1. Pressing the button once should disable the keyboard backlight.
1. Pressing the button again should re-enable the keyboard backlight.

## ECR022.001 RGB keyboard next color FN key in OS (Ubuntu)

**Test description**

This test verifies that the RGB keyboard's next color hotkey is handled properly
by the operating system.

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
1. Press the RGB keyboard color hotkey repeatedly until the keyboard cycles
   through all color modes.

**Expected result**

1. Pressing the button once should switch the keyboard color.
1. All color modes according to product documentation should be accessible.

## ECR022.002 RGB keyboard next color FN key in OS (Windows)

**Test description**

This test verifies that the RGB keyboard's next color hotkey is handled properly
by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the RGB keyboard color hotkey repeatedly until the keyboard cycles
   through all color modes.

**Expected result**

1. Pressing the button once should switch the keyboard color.
1. All color modes according to product documentation should be accessible.

## ECR023.001 RGB keyboard brightness down FN key in OS (Ubuntu)

**Test description**

This test verifies that the RGB keyboard brightness down hotkey is handled
properly by the operating system.

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
1. Press the RGB keyboard brightness down hotkey and note the result.

**Expected result**

1. Pressing the button once should lower the keyboard backlight

## ECR023.002 RGB keyboard brightness down FN key in OS (Windows)

**Test description**

This test verifies that the RGB keyboard brightness down hotkey is handled
properly by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the RGB keyboard brightness down hotkey and note the result.

**Expected result**

1. Pressing the button once should lower the keyboard backlight.

## ECR024.001 RGB keyboard brightness up FN key in OS (Ubuntu)

**Test description**

This test verifies that the RGB keyboard brightness up hotkey is handled
properly by the operating system.

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
1. Press the RGB keyboard brightness up hotkey and note the result.

**Expected result**

1. Pressing the button once should increase the keyboard backlight.

## ECR024.002 RGB keyboard brightness up FN key in OS (Windows)

**Test description**

This test verifies that the RGB keyboard brightness up hotkey is handled
properly by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Press the RGB keyboard brightness up hotkey and note the result.

**Expected result**

1. Pressing the button once should increase the keyboard backlight.

## ECR025.001 Permanent keyboard illumination after cold-boot (Firmware)

**Test description**

This test aims to verify that after performing cold-boot, keyboard still
illuminates in firmware.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware)

**Test steps**

1. Power on the DUT and press the `BIOS_SETUP_KEY` to enter the setup menu.
1. Set keyboard brightness and color to arbitrary settings.
1. Disconnect power source, and remove battery if present.
1. Connect power and battery again.
1. Power on the DUT again and press the `BIOS_SETUP_KEY` to enter the setup
    menu.

**Expected result**

1. After cold-boot keyboard brightness and colors settings remain the same.

## ECR025.002 Permanent keyboard illumination after cold-boot (Ubuntu)

**Test description**

This test aims to verify that after performing cold-boot, keyboard still
illuminates in Ubuntu.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the `OPERATING_SYSTEM`.
1. Log into the `OPERATING_SYSTEM` by using the proper login and password.
1. Set keyboard brightness and color to arbitrary settings.
1. Disconnect power source, and remove battery if present.
1. Connect power and battery again.
1. Power on the DUT.
1. Boot into the `OPERATING_SYSTEM`.
1. Log into the `OPERATING_SYSTEM` by using the proper login and password.

**Expected result**

1. After cold-boot keyboard brightness and colors settings remain the same.

## ECR025.003 Permanent keyboard illumination after cold-boot (Windows)

**Test description**

This test aims to verify that after performing cold-boot, keyboard still
illuminates in Windows.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the `OPERATING_SYSTEM`.
1. Log into the `OPERATING_SYSTEM` by using the proper login and password.
1. Set keyboard brightness and color to arbitrary settings.
1. Disconnect power source, and remove battery if present.
1. Connect power and battery again.
1. Power on the DUT.
1. Boot into the `OPERATING_SYSTEM`.
1. Log into the `OPERATING_SYSTEM` by using the proper login and password.

**Expected result**

1. After cold-boot keyboard brightness and colors settings remain the same.

## ECR026.001 Permanent keyboard illumination after warm-boot (Firmware)

**Test description**

This test aims to verify that after performing warm-boot, keyboard still
illuminates in firmware.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware)

**Test steps**

1. Power on the DUT and press the `BIOS_SETUP_KEY` to enter the setup menu.
1. Set keyboard brightness and color to arbitrary settings.
1. Power off the DUT using power button.
1. Power on the DUT again and press the `BIOS_SETUP_KEY` to enter the setup
    menu.

**Expected result**

1. After warm-boot keyboard brightness and colors settings remain the same.

## ECR026.002 Permanent keyboard illumination after warm-boot (Ubuntu)

**Test description**

This test aims to verify that after performing warm-boot, keyboard still
illuminates in Ubuntu.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the `OPERATING_SYSTEM`.
1. Log into the `OPERATING_SYSTEM` by using the proper login and password.
1. Set keyboard brightness and color to arbitrary settings.
1. Power off the DUT using power button.
1. Power on the DUT.
1. Boot into the `OPERATING_SYSTEM`.
1. Log into the `OPERATING_SYSTEM` by using the proper login and password.

**Expected result**

1. After warm-boot keyboard brightness and colors settings remain the same.

## ECR026.003 Permanent keyboard illumination after warm-boot (Windows)

**Test description**

This test aims to verify that after performing warm-boot, keyboard still
illuminates in Windows.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the `OPERATING_SYSTEM`.
1. Log into the `OPERATING_SYSTEM` by using the proper login and password.
1. Set keyboard brightness and color to arbitrary settings.
1. Power off the DUT using power button.
1. Power on the DUT.
1. Boot into the `OPERATING_SYSTEM`.
1. Log into the `OPERATING_SYSTEM` by using the proper login and password.

**Expected result**

1. After warm-boot keyboard brightness and colors settings remain the same.

## ECR027.001 Permanent keyboard illumination after reboot (Firmware)

**Test description**

This test aims to verify that after performing reboot, keyboard still
illuminates in firmware.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware)

**Test steps**

1. Power on the DUT and press the `BIOS_SETUP_KEY` to enter the setup menu.
1. Set keyboard brightness and color to arbitrary settings.
1. Select `Reset` option from the bottom of the list.
1. During boot press the `BIOS_SETUP_KEY` to enter the setup menu.

**Expected result**

1. After reboot keyboard brightness and colors settings remain the same.

## ECR027.002 Permanent keyboard illumination after reboot (Ubuntu)

**Test description**

This test aims to verify that after performing reboot, keyboard still
illuminates in Ubuntu

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
1. Set keyboard brightness and color to arbitrary settings.
1. Reboot the device using:

    ```bash
    sudo reboot now
    ```

**Expected result**

1. After reboot keyboard brightness and colors settings remain the same.

## ECR027.003 Permanent keyboard illumination after reboot (Windows)

**Test description**

This test aims to verify that after performing reboot, keyboard still
illuminates in Windows 11.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Set keyboard brightness and color to arbitrary settings.
1. Reboot the device executing in PowerShell:

    ```bash
    Restart-Computer
    ```

**Expected result**

1. After reboot keyboard brightness and colors settings remain the same.

## ECR028.001 Permanent keyboard illumination after suspension (Firmware)

**Test description**

This test aims to verify that after performing suspension, keyboard still
illuminates in firmware.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `SUSPEND_KEY` = `Fn + F12`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware)

**Test steps**

1. Power on the DUT and press the `BIOS_SETUP_KEY` to enter the setup menu.
1. Set keyboard brightness and color to arbitrary settings.
1. Suspend the DUT using `SUSPEND_KEY`.
1. Wake the device from suspend pressing any key on keyboard.

**Expected result**

1. After suspend keyboard brightness and colors settings remain the same.

## ECR028.002 Permanent keyboard illumination after suspension (Ubuntu)

**Test description**

This test aims to verify that after performing suspension, keyboard still
illuminates in Ubuntu

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu
1. `SUSPEND_KEY` = `Fn + F12`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Set keyboard brightness and color to arbitrary settings.
1. Suspend the DUT using `SUSPEND_KEY`.
1. Wake the device from suspend pressing any key on keyboard.

**Expected result**

1. After suspend keyboard brightness and colors settings remain the same.

## ECR028.003 Permanent keyboard illumination after suspension (Windows)

**Test description**

This test aims to verify that after performing suspension, keyboard still
illuminates in Windows.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows
1. `SUSPEND_KEY` = `Fn + F12`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Set keyboard brightness and color to arbitrary settings.
1. Suspend the DUT using `SUSPEND_KEY`.
1. Wake the device from suspend pressing any key on keyboard.

**Expected result**

1. After suspend keyboard brightness and colors settings remain the same.

## ECR029.001 FnLock Hotkey (Ubuntu)

**Test description**

This test aims to verify that FnLock hotkey functionality works properly on
Ubuntu.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu
1. `FN_LOCK_KEY` = `Fn + CapsLock`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Use `FN_LOCK_KEY` to activate Fn lock functionality.
1. Test function keys `F1` - `F12` and note the results.

**Expected result**

1. The function keys `F1` - `F12` behave as if `Fn` key is pressed.

## ECR029.002 FnLock Hotkey (Windows)

**Test description**

This test aims to verify that FnLock hotkey functionality works properly on
Windows.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows
1. `FN_LOCK_KEY` = `Fn + CapsLock`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Use `FN_LOCK_KEY` to activate Fn lock functionality.
1. Test function keys `F1` - `F12` and note the results.

**Expected result**

1. The function keys `F1` - `F12` behave as if `Fn` key is pressed.

## ECR030.001 Charging until 98% battery level (Ubuntu)

**Test description**

This test aims to verify if charging the battery stops when the battery level
reaches 98% mark.

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
1. Open a terminal window and execute following command to check current battery
    charge level percentage:

    ```bash
    cat /sys/class/power_supply/BAT0/capacity
    ```

1. Note the results.
1. If the battery level sits below 95% mark, plug the charger into the DUT.
1. If the battery level sits above 95% mark, wait until the DUT's battery
    discharges to below 95% level and then plug the charger into the DUT.
1. Wait until the DUT's battery charge level reaches 98%.
1. Open a terminal window and execute following command to confirm that the
    battery charging stops at 98% mark:

    ```bash
    cat /sys/class/power_supply/BAT0/status
    ```

1. Note the results.

**Expected result**

1. The output of the `cat /sys/class/power_supply/BAT0/capacity` command should
    contain information about the current battery charge level.
1. The output of the `cat /sys/class/power_supply/BAT0/status` command should
    contain information about the current battery charging status.
    Example output:

    ```bash
    not charging
    ```

## ECR030.001 Not charging between 95% and 98% levels (Ubuntu)

**Test description**

This test aims to verify if charging the battery does not start after plugging
in the charger into the DUT when the battery level sits between 95% and 98%.

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
1. Open a terminal window and execute following command to check current battery
    charge level percentage:

    ```bash
    cat /sys/class/power_supply/BAT0/capacity
    ```

1. Note the results.
1. If the battery level sits between 95% and 98%, plug the charger into the DUT.
1. If the battery level sits below 95%, plug the charger into the DUT, wait
    until the battery reaches the level between 95% and 98% and then unplug the
    charger and plug it back in into the DUT.
1. Open a terminal window and execute following command to confirm that the
    battery does not start charging:

    ```bash
    cat /sys/class/power_supply/BAT0/status
    ```

1. The output of the `cat /sys/class/power_supply/BAT0/capacity` command should
    contain information about the current battery charge level.
1. The output of the `cat /sys/class/power_supply/BAT0/status` command should
    contain information about the current battery charging status.
    Example output:

    ```bash
    not charging
    ```

## ECR031.001 EC firmware sync in coreboot

**Test description**

This test verifies the automatic EC firmware update / sync feature in coreboot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Downgrade to the previous firmware version (both EC and coreboot must be
   downgraded) if needed.
1. Keep AC adapter or USB-PD power supply connected for the duration of the
   test.

**Test steps**

1. Power on the DUT.
1. Proceed with the firmware update steps [as documented in the firmware update
   guide](/guides/firmware-update).
1. Reboot the DUT after updating firmware.
1. Wait until the DUT updates the EC (indicated by the fans spinning at full
   speed) and powers off.
1. Power on the DUT.
1. Note the EC firmware version displayed on the Dasharo boot screen.

**Expected result**

1. The EC version displayed on the boot screen should match the expected version
   number.
1. There should not be a pop-up indicating that the EC update failed for any
   reason.

## ECR032.001 EC firmware sync in coreboot blocked when AC not connected

**Test description**

This test verifies that the automatic EC firmware update / sync feature in
coreboot does not attempt to update the EC while an AC adapter is not connected.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Downgrade to the previous firmware version (both EC and coreboot must be
   downgraded) if needed.

**Test steps**

1. Power on the DUT.
1. Proceed with the firmware update steps [as documented in the firmware update
   guide](/guides/firmware-update).
1. Disconnect the AC adapter, if connected.
1. Reboot the DUT.
1. Note the contents of the popup displayed on the Dasharo boot screen.

**Expected result**

1. A warning message should appear, informing the user that the EC update did
   not proceed correctly, and asking them to reboot with an AC adapter
   connected.

## ECR033.001 EC power button watchdog

**Test description**

This test verifies that the EC power switch watchdog feature is functional and
can reset the EC.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Attach [EC debugger](../../transparent-validation/ec-debugger/uart-relay.md)
   to the DUT.

**Test steps**

1. Power on the DUT.
1. Hold the power button pressed for at least 10 seconds
1. Note any messages appearing on the EC debug interface.

**Expected result**

1. The debug logs should contain a message indicating that the EC was reset due
   to watchdog timeout reset, e.g.:

    ```text
    Last reset caused by PWRSW WDT Timeout!
    ```

## ECR034.001 Soft Switch Microphone Key (Ubuntu)

**Test description**

This test verifies that Fn+4 key combination for microphone soft switch works

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
1. Go to 'Settings -> Sound
1. Observe the bar above the Input Device option
1. Press the `Fn+4` combination at will

**Expected result**

1. The Fn+4 should toggle the mic ON and OFF and it should be seen on the
 aforementioned bar which state is currently active as noise made will
 make the bar go back and forth if ON and completely still if OFF

## ECR034.002 Soft Switch Microphone Key (Windows)

**Test description**

This test verifies that Fn+4 key combination for microphone soft switch works

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Go to 'Settings -> System -> Sound
1. Observe the bar located on the mic volume slider
1. Press the `Fn+4` combination at will

**Expected result**

1. The Fn+4 should toggle the mic ON and OFF and it should be seen on the
 aforementioned bar which state is currently active as the noise made will
 make the bar go back and forth if ON and completely still if OFF

## SIO001.001 PS/2 mouse in OS - (Ubuntu)

**Test description**

This test verifies that the touchpad is initialized correctly and is detected
by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Connect PS/2 mouse to the green PS/2 port on the board or the PS/2 splitter
   (if the board has a unified, black PS/2 connector)

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Verify that the cursor can be moved with the PS/2 mouse and that clicking
   works.

**Expected result**

1. Moving the cursor and clicking working correctly in the operating system.

## SIO001.002 PS/2 mouse in OS - (Windows)

**Test description**

This test verifies that the touchpad is initialized correctly and is detected
by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Connect PS/2 mouse to the green PS/2 port on the board or the PS/2 splitter
   (if the board has a unified, black PS/2 connector)

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Verify that the cursor can be moved with the PS/2 mouse and that clicking
   works.

**Expected result**

1. Moving the cursor and clicking working correctly in the operating system.

## SIO002.001 PS/2 keyboard in firmware

**Test description**

This test verifies that the keyboard is detected correctly by the firmware
and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `BIOS_SETUP_KEY` = `Esc`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware)
2. Connect PS/2 keyboard to the violet PS/2 port on the board or the PS/2
   splitter (if the board has a unified, black PS/2 connector)

**Test steps**

1. Power on the DUT and press the `BIOS_SETUP_KEY` to enter the setup menu.
2. Use the arrow keys and the Enter key to navigate the menus.

**Expected result**

1. All menus can be entered using the PS/2 keyboard.

## SIO002.002 PS/2 keyboard in OS (Ubuntu)

**Test description**

This test verifies that the keyboard is detected correctly by the operating
system and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `BIOS_SETUP_KEY` = `Esc`
3. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Connect PS/2 keyboard to the violet PS/2 port on the board or the PS/2
   splitter (if the board has a unified, black PS/2 connector)

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Run `sudo libinput debug-events --show-keycodes` in the terminal.
5. Press keyboard keys and check the generated keycode.

**Expected result**

1. All standard keyboard keys generate the correct keycodes and events as per
   their labels.
2. Key combinations are detected correctly.

## SIO002.003 PS/2 keyboard in OS (Windows)

**Test description**

This test verifies that the keyboard is detected correctly by the operating
system and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Connect PS/2 keyboard to the violet PS/2 port on the board or the PS/2
   splitter (if the board has a unified, black PS/2 connector)

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Open `notepad`
    * Test the alphanumeric keys and note the generated characters
    * Test non-alphanumeric keys and verify that they generate the signs
    * Test key combinations with the `Shift`, and `Alt` modifier keys
5. Open `On-Screen Keyboard` and press `Ctrl` key on the hardware keyboard.
   Check if `On-Screen Keyboard` correctly highlights it.
6. Open `Start menu` and press `Esc`. Check if `Start menu` is properly closed.

**Expected result**

1. All standard keyboard keys generate correct characters
   or actions when pressed.
2. Key combinations are detected correctly.

## SIO003.001 PS/2 keyboard wake in OS (Ubuntu)

**Test description**

This test verifies that the keyboard is detected correctly by the operating
system and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `BIOS_SETUP_KEY` = `Esc`
3. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Connect PS/2 keyboard to the violet PS/2 port on the board or the PS/2
   splitter (if the board has a unified, black PS/2 connector)

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Suspend the system to RAM.
5. Press a keyboard key to wake the platform.

**Expected result**

1. Platform is resuming to the OS from sleep after pressing the key.

## SIO003.002 PS/2 keyboard wake in OS (Windows)

**Test description**

This test verifies that the keyboard is detected correctly by the operating
system and all basic keys work according to their labels.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Connect PS/2 keyboard to the violet PS/2 port on the board or the PS/2
   splitter (if the board has a unified, black PS/2 connector)

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Suspend the system to RAM.
5. Press a keyboard key to wake the platform.

**Expected result**

1. Platform is resuming to the OS from sleep after pressing the key.

## SIO004.001 Serial port in firmware

**Test description**

This test verifies that the serial port is detected correctly by the firmware
and the menu can be traversed with serial console.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `BIOS_SETUP_KEY` = `Esc`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware)
2. Connect DB9 null modem cable to RS232/USB adapter and the onboard serial
   port connector.

**Test steps**

1. Open the terminal emulator, e.g. minicom, on the RS232/USB adapter.
2. Power on the DUT and press the `BIOS_SETUP_KEY` to enter the setup menu.
3. Use the arrow keys and the Enter key to navigate the menus.

**Expected result**

1. All menus can be entered using the serial console.

## SIO004.002 Serial port in OS (Ubuntu)

**Test description**

This test verifies that the serial port is detected correctly by the operating
system and can be utilized as serial console.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `BIOS_SETUP_KEY` = `Esc`
3. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Connect DB9 null modem cable to RS232/USB adapter and the onboard serial
   port connector.
3. Configure Linux kernel parameters to use serial console, e.g.
   `console=ttyS0,115200`

**Test steps**

1. Open the terminal emulator, e.g. minicom, on the RS232/USB adapter.
2. Power on the DUT.
3. Boot into the system.
4. Log into the system by using the proper login and password through serial
   console.

**Expected result**

1. Serial port can be used as Linux console to log in.
2. Serial port can be used to execute commands in bash/shell.
