# Dasharo Compatibility: Audio subsystem

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
1. For the audio tests you need to connect monitor with speakers via HDMI.

## AUD001.201 Audio subsystem detection (Ubuntu)

**Test description**

This test aims to verify that the audio subsystem is initialized correctly
and can be detected from the operating system.

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
1. Open a terminal window and execute the following command:

    ```bash
    cat /sys/class/sound/card0/hwC0D*/chip_name
    ```

**Expected result**

The output of the command should return a list of detected audio devices.
Depending on mounted devices, the output might be different.

Example output:

```bash
ALC293
Tigerlake HDMI
```

## AUD001.301 Audio subsystem detection (Windows)

**Test description**

This test aims to verify that the audio subsystem is initialized correctly
and can be detected from the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install package `AudioDeviceCmdlets`:

    ```powershell
    Install-PackageProvider -Name NuGet -Force
    ```

    ```powershell
    Install-Module -Name AudioDeviceCmdlets -Force
    ```

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Run PowerShell as administrator and execute the following command:

    ```powershell
    Get-AudioDevice -list  | ft Index, Default, Type, Name
    ```

**Expected result**

`Microphone (Realtek(R) Audio)` and `Speakers (Realtek(R) Audio)` should be
listed in the output:

```powershell
Index Default Type      Name
----- ------- ----      ----
    1    True Playback  Speakers (Realtek(R) Audio)
    2    True Recording Microphone (Realtek(R) Audio)
```

## AUD002.201 Audio playback (Ubuntu)

**Test description**

This test aims to verify that the audio subsystem is able to playback audio
recordings.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `alsa-utils` package:
    `sudo apt install alsa-utils`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

    ```bash
    pactl set-sink-mute alsa_output.pci-0000_00_1f.3.analog-stereo  0
    pactl set-sink-volume alsa_output.pci-0000_00_1f.3.analog-stereo 65535
    speaker-test
    ```

**Expected result**

Sound should be played from the integrated speakers.

## AUD002.301 Audio playback (Windows)

**Test description**

This test aims to verify that the audio subsystem is able to playback audio
recordings.

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
1. Find the `Speakers` icon in the bottom right part of the screen and click
    it using the left mouse button to open the volume menu.
1. In the volume menu, click the rightmost part of it and note the result.

**Expected result**

Sound should be played from the integrated speakers.

## AUD003.201 Audio capture (Ubuntu)

**Test description**

This test aims to verify that the audio subsystem is able to capture audio.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `alsa-utils` package:
    `sudo apt install alsa-utils`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

    ```bash
    arecord -f S16_LE -d 10 -r 16000 /tmp/test-mic.wav
    ```

1. Make some noise around DUT. For example, say something.
1. Execute the following command:

    ```bash
    aplay /tmp/test-mic.wav
    ```

**Expected result**

The recorded audio clip is recorded correctly and played back.

## AUD003.301 Audio capture (Windows)

**Test description**

This test aims to verify that the audio subsystem is able to capture audio.

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

## AUD004.201 External headset recognition (Ubuntu)

**Test description**

This test aims to verify that the external headset is properly recognized
after plugging the 3.5 mm jack into the slot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `alsa-utils` package:
    `sudo apt install alsa-utils`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug a headset jack into a micro jack slot located on the right side of
    the laptop.
1. When the `Select Audio Device` menu appears, select what type of external
    device has been connected to the laptop (headset).
1. Open a terminal window and execute the following command:

    ```bash
    amixer -c 0 contents | grep -A 2 'Front Headphone Jack'
    ```

1. Disconnect the headset from the laptop.
1. Execute the following command again:

    ```bash
    amixer -c 0 contents | grep -A 2 'Front Headphone Jack'
    ```

**Expected result**

1. The output of the first command should not be empty and contains the line:

    ```text
    : values=on
    ```

1. The output of the second command should not be empty and contains the line:

    ```text
    : values=off
    ```

## AUD004.301 External headset recognition (Windows)

**Test description**

This test aims to verify that the external headset is properly recognized
after plugging the 3.5 mm jack into the slot.

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
1. Plug a headset jack into a micro jack slot located on the right side of
    the laptop.
1. After the `Which device did you plug` in menu appears, select what type of
    external device has been connected to the laptop (headset).
1. Find the `Speakers` icon in the bottom right part of the screen and click it
    using the right mouse button then using the left mouse button click
    `Sound Settings`.
1. Locate the `More sound settings` bar and click on it.
1. Click on the `Speakers` bar using the right mouse button then using the left
    mouse button click `Properties`.
1. Locate in `General` the section field named `Jack Information`.
1. Close the windows `Speakers Properties` and `Sound`.
1. Disconnect a headset from the laptop.
1. Repeat steps 7-9.

**Expected result**

1. `Jack Information` field in the first case should show the position
    `Front Panel 3.5 mm Jack`.
1. After disconnecting a headset from the laptop and checking again field
    `Jack Information` should not contain the phrase `Front Panel 3.5 mm Jack`.

## AUD005.001 External headset audio playback (Ubuntu)

**Test description**

This test aims to verify that the audio subsystem is able to playback audio
recordings by using the external headset speakers.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `alsa-utils` package:
    `sudo apt install alsa-utils`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug a headset jack into a micro jack slot located on the right side of the
    laptop.
1. Open a terminal window and execute the following command:

    ```bash
    pactl set-sink-mute alsa_output.pci-0000_00_1f.3.analog-stereo  0
    pactl set-sink-volume alsa_output.pci-0000_00_1f.3.analog-stereo 65535
    speaker-test
    ```

**Expected result**

Sound should be played from external speakers.

## AUD005.002 External headset audio playback (Windows)

**Test description**

This test aims to verify that the audio subsystem is able to playback audio
recordings by using the external headset speakers.

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
1. Plug a headset jack into a micro jack slot located on the right side of the
    laptop.
1. Find the `Speakers` icon in the bottom right part of the screen and click
   it using the left mouse button to open the volume menu.
1. In the volume menu, click the rightmost part of it and note the result.

**Expected result**

Sound should be played from external speakers.

## AUD006.001 External headset audio capture (Ubuntu)

**Test description**

This test aims to verify that the audio subsystem is able to capture audio from
an external headset.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `alsa-utils` package:
    `sudo apt install alsa-utils`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug a headset jack into a micro jack slot located on the right side of the
    laptop.
1. Open a terminal window and execute the following command:

    ```bash
    arecord -f S16_LE -d 10 -r 16000 /tmp/test-mic.wav
    ```

1. Make some noise for the headset. For example, say something.
1. Execute the following command:

    ```bash
    aplay /tmp/test-mic.wav
    ```

1. Execute the following command:

    ```bash
    arecord -f S16_LE -d 10 -r 16000 /tmp/test-mic-1.wav
    ```

1. Make some noise for the DUT. For example, tap a few times in the laptop
    casing.
1. Execute the following command:

    ```bash
    aplay /tmp/test-mic.wav
    ```

**Expected result**

1. During playback of the first recording, all noise that was made for the
    headset should be clearly heard.
1. During playback of the second recording, all noise that was made for DUT
    should be quiet or not heard.

## AUD006.002 External headset audio capture (Windows)

**Test description**

This test aims to verify that the audio subsystem is able to capture audio from
an external headset.

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
1. Plug a headset jack into a micro jack slot located on the right side of the
    laptop.
1. Find the `Speakers` icon in the bottom right part of the screen and click
    it using the right mouse button then using the left mouse button click
    `Sound Settings`.
1. Locate the `All sound devices` bar and click on it.
1. Select the `Microphone` position in the `Input devices` section.
1. Click on the `Start Test` bar in the `Input settings` section.
1. Create some noise for the headset to capture and note the result.
    For example, say something.
1. Create some noise for the DUT. For example, tap a few times in the laptop
    casing.
1. Click on the `Stop Test` bar.

**Expected result**

1. The `Input volume` bar located in the `Input settings` section should raise
    when some noise has been created for the headset.
1. The `Input volume` bar located in the `Input settings` section should not
    raise when some noise has been created for the DUT.
1. The result of the test after clicking the `Stop Test` bar should be more than
    0% of the total volume.

## AUD007.001 HDMI Audio recognition (Ubuntu)

**Test description**

This test aims to verify that the output audio is properly assigned after
connecting the external display using the HDMI cable.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `alsa-utils` package:
    `sudo apt install alsa-utils`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect the external display to the HDMI slot.
1. Open a terminal window and execute the following command:

    ```bash
    pactl list cards | grep "hdmi-output" | grep -v "not available"
    ```

1. Disconnect the headset from the laptop.
1. Execute the following command again:

    ```bash
    pactl list cards | grep "hdmi-output" | grep -v "not available"
    ```

**Expected result**

1. The output of the first command should not be empty and contains the line:

    ```text
    : hdmi-output-0: HDMI / DisplayPort (type: HDMI, priority: 5900, latency
     offset: 0 usec, availability group: Legacy 4, available)
    ```

1. The output of the second command should be empty

## AUD007.002 HDMI Audio recognition (Windows)

**Test description**

This test aims to verify that the output audio is properly assigned after
connecting the external display using the HDMI cable.

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
1. Find the `Speakers` icon in the bottom right part of the screen and click it
    using the right mouse button then using the left mouse button click
    `Sound Settings`.
1. Locate the `All sound devices` bar and click on it.
1. Locate the `Output devices` and `Input devices` section.
1. Connect the external display to the HDMI slot.

**Expected result**

The connected display should appear in the `Output devices` section.

## AUD008.001 HDMI audio playback (Ubuntu)

**Test description**

This test aims to verify that the audio subsystem is able to playback audio
recordings by using the external display connected to the HDMI slot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `alsa-utils` package:
    `sudo apt install alsa-utils`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect the external display to the HDMI slot.

1. Open a terminal window and execute the following commands:

    ```bash
    pacmd set-card-profile 0 output:hdmi-stereo
    pactl set-sink-mute alsa_output.pci-0000_00_1f.3.analog-stereo  0
    pactl set-sink-volume alsa_output.pci-0000_00_1f.3.analog-stereo 65535
    speaker-test
    ```

**Expected result**

Sound should be played from the external display.

## AUD008.002 HDMI audio playback (Windows)

**Test description**

This test aims to verify that the audio subsystem is able to playback audio
recordings by using the external display connected to the HDMI slot.

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
1. Connect the external display to the HDMI slot.
1. Find the `Speakers` icon in the bottom right part of the screen and click it
    using the right mouse button then using the left mouse button click
    `Sound Settings`.
1. Locate the `All sound devices` bar and click on it.
1. Select the external display position in the `Output devices` section.
1. Click on the `Test` bar in the `Output settings` section.

**Expected result**

Sound should be played from the external display.
