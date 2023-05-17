# Dasharo Compatibility: Thunderbolt docking station audio

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup#os-boot-from-disk).
1. The `Thunderbolt docking station` connected to the Thunderbolt port.

## TDA001.001 Audio recognition (Ubuntu 22.04)

**Test description**

This test aims to verify that the external headset is properly recognized after
plugging in the 3.5 mm jack into the docking station.

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

## TDA001.002 Audio recognition (Windows 11)

**Test description**

This test aims to verify that the external headset is properly recognized
after plugging in the 3.5 mm jack into the docking station.

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

## TDA002.001 Audio playback (Ubuntu 22.04)

**Test description**

This test aims to verify that the audio subsystem is able to playback audio
recordings by using the external headset speakers connected to the docking
station.

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

## TDA002.002 Audio playback (Windows 11)

**Test description**

This test aims to verify that the audio subsystem is able to playback audio
recordings by using the external headset speakers connected to the docking
station.

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
1. Plug in a headset jack into the docking station.
1. Find the `Speakers` icon in the bottom right part of the screen and click
   it using the left mouse button to open volume menu.
1. After the `Which device did you plug in` menu appearing, select what type
    of external device has been connected to the laptop (headset).
1. In the volume menu, click the rightmost part of it and note the reult.

**Expected result**

Sound should be played from the external speakers.

## TDA003.001 Audio capture (Ubuntu 22.04)

**Test description**

This test aims to verify that the audio subsystem is able to capture audio
from external headset connected to the docking station.

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

## TDA003.002 Audio capture (Windows 11)

**Test description**

This test aims to verify that the audio subsystem is able to capture audio
from external headset connected to the docking station.

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
