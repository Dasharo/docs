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

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

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

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## AUD004.301 External headset recognition (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## AUD005.201 External headset audio playback (Ubuntu)

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

## AUD005.301 External headset audio playback (Windows)

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

## AUD006.201 External headset audio capture (Ubuntu)

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

## AUD006.301 External headset audio capture (Windows)

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

## AUD007.201 HDMI Audio recognition (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## AUD007.301 HDMI Audio recognition (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

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

## AUD008.201 HDMI audio playback (Ubuntu)

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

## AUD008.301 HDMI audio playback (Windows)

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
