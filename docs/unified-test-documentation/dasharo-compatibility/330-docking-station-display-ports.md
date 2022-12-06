# Dasharo Compatibility: Docking station Display ports

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
1. The docking station is connected to the USB-C port.

    > If the docking station is not directly connected to the DUT, but with a
    > USB-C to USB-C cable, make sure it is full-featured cable (>=5Gbps) with
    > 5A current capability.

## DDP001.001 HDMI display (Ubuntu 22.04)

**Test description**

This test aims to verify that the display connected with the HDMI cable to the
docking station is correctly recognized by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04
1. Connect an HDMI cable to the docking station and a display.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. If using more than one display, switch the display mode between `Mirror` and
   `Join Displays`.

**Expected result**

The image should be displayed on the external HDMI-connected display in `Mirror`
and `Join Displays` modes.

## DDP001.002 HDMI display (Windows 11)

**Test description**

This test aims to verify that the display connected with the HDMI cable to the
docking station is correctly recognized by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11
1. Connect an HDMI cable to the docking station and a display.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. If using more than one display, switch the display mode between `Duplicate`
   and `Extend`.

**Expected result**

The image should be displayed on the external HDMI-connected display in
`Duplicate` and `Extend` modes.

## DDP002.001 DP display (Ubuntu 22.04)

**Test description**

This test aims to verify that the display connected with the HDMI cable to the
docking station is correctly recognized by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04
1. Connect a Display Port cable to the docking station and a display.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
4. If using more than one display, switch the display mode between `Mirror` and
   `Join Displays`.

**Expected result**

The image should be displayed on the external DisplayPort-connected display in
`Mirror` and `Join Displays` modes.

## DDP002.002 DP display (Windows 11)

**Test description**

This test aims to verify that the display connected with the DisplayPort cable
to the docking station is correctly recognized by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11
1. Connect a DisplayPort cable to the docking station and a display.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. If using more than one display, switch the display mode between `Duplicate`
   and `Extend`.

**Expected result**

The image should be displayed on the external DisplayPort-connected display in
`Duplicate` and `Extend` modes.

## DDP003.001 Triple display (Ubuntu 22.04)

**Test description**

This test aims to verify that the three display simultaneously connected to the
docking station is correctly recognized by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04
1. Connect three displays using HDMI/DisplayPort cables, depending on the
   specifications of the docking station.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Switch the display mode between `Mirror` and `Join Displays`.

**Expected result**

The image should be displayed on the three external displays in `Mirror` and
`Join Displays` modes.

## DDP003.002 Triple display (Windows 11)

**Test description**

This test aims to verify that the three display simultaneously connected to the
docking station is correctly recognized by the `OPERATING_SYSTEM`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11
1. Connect three displays using HDMI/DisplayPort cables, depending on the
   specifications of the docking station.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. If using more than one display, switch the display mode between `Duplicate`
   and `Extend`.

**Expected result**

The image should be displayed on the three external displays in `Duplicate` and
`Extend` modes.
