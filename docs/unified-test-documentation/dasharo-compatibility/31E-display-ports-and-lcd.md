# Dasharo Compatibility: Display ports and LCD support

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

## DSP001.001 Internal LCD in firmware

**Test description**

This test aims to verify initialization of the laptop's embedded LCD screen
during firmware execution phase.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. Observe the internal LCD during firmware execution phase.
1. Power off the DUT.

**Expected result**

1. Logo appears on the screen during firmware execution phase.

## DSP001.0XX Internal LCD in OS (Linux generic)
**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Observe the internal LCD after the `OPERATING_SYSTEM` has booted.

**Expected result**

1. Either the login screen or the `OPERATING_SYSTEM` installer appears on the
    internal LCD.

## DSP001.201 Internal LCD in OS (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## DSP001.301 Internal LCD in OS (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop


## DSP002.2XX External HDMI display in OS (Linux generic)

**Test description**

This test aims to verify initialization of the external HDMI display in the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Connect an HDMI cable to the DUT and a display.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log in by using the proper login and password.
1. If using more than one display, switch the display mode between `Mirror` and
    `Join Displays`.

**Expected result**

1. The image should be displayed on the external HDMI display in `Mirror` and
    `Join Displays` modes.

## DSP002.201 External HDMI display in OS (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## DSP002.301 External HDMI display in OS (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## DSP002.010 External HDMI display in OS (XCP-NG)

Follows the [generic DSP002.0XX Linux-based test case](#dsp002003-external-hdmi-display-in-firmware)
Only the output on a single monitor needs to observed; skip the OS
menu-specific steps.

## DSP002.011 External HDMI display in OS (ESXI)

Follows the [generic DSP002.0XX Linux-based test case](#dsp002003-external-hdmi-display-in-firmware)
Only the output on a single monitor needs to observed; skip the OS
menu-specific steps.

## DSP002.003 External HDMI display in firmware

This test aims to verify initialization of the external HDMI display
during firmware execution phase.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
2. Connect an HDMI cable to the DUT and a display.

**Test steps**

1. Power on the DUT.
1. Observe the external HDMI display during firmware execution phase.
1. Power off the DUT.

**Expected result**

1. Logo appears on the screen during firmware execution phase.

## DSP003.0XX External DP display in OS (Linux generic)

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Connect a Display Port cable to the DUT and a display.

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log in by using the proper login and password.
4. If using more than one display, switch the display mode between `Mirror` and
    `Join Displays`.

**Expected result**

1. The image should be displayed on the external Display Port connected display
    in `Mirror` and `Join Displays` modes.


## DSP003.201 External DP display in OS (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## DSP003.301 External DP display in OS (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## DSP003.010 External DP display in OS (XCP-NG)

Follows the [generic DSP003.0XX Linux-based test case](#dsp0030xx-external-dp-display-in-os-linux-generic)
Only the output on a single monitor needs to observed; skip the OS
menu-specific steps.

## DSP003.011 External DP display in OS (ESXI)

Follows the [generic DSP003.0XX Linux-based test case](#dsp0030xx-external-dp-display-in-os-linux-generic)
Only the output on a single monitor needs to observed; skip the OS
menu-specific steps.

## DSP003.003 External DP display in firmware

This test aims to verify initialization of the external Display Port connected
display during firmware execution phase.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
2. Connect a Display Port cable to the DUT and a display.

**Test steps**

1. Power on the DUT.
2. Observe the external Display Port connected display during firmware
   execution phase.
3. Power off the DUT.

**Expected result**

1. Logo appears on the screen during firmware execution phase.

## DSP004.201 External VGA display in OS (Ubuntu)

**Test description**

This test aims to verify initialization of the external VGA in the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Connect a video input connector to the VGA and a display.

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log the  by using the proper login and password.
4. If using more than one display, switch the display mode between `Mirror` and
    `Join Displays`.

**Expected result**

1. The image should be displayed on the external VGA connected display in
    `Mirror` and `Join Displays` modes.

## DSP004.301 External VGA display in OS (Windows)

**Test description**

This test aims to verify initialization of the external VGA in the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Connect a video input connector to the VGA and a display.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log the  by using the proper login and password.
1. If using more than one display, switch the display mode between `Duplicate`
    and `Extend`.

**Expected result**

1. The image should be displayed on the external Display Port connected display
    in `Duplicate` and `Extend` modes.

## DSP004.003 External VGA display in firmware

This test aims to verify initialization of the external VGA during firmware
execution phase.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
2. Connect a video input connector to the VGA and a display.

**Test steps**

1. Power on the DUT.
2. During boot, press `BOOT MENU KEY`.
3. Observe the external VGA connected display during firmware execution phase.
4. Power off the DUT.

**Expected result**

1. Boot menu appears on the screen during firmware execution phase.
