# Dasharo Compatibility: USB-C/Thunderbolt support with charging and display

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

## UTC001.001 USB Type-A charging capability

**Test description**

This test verifies that the USB-A ports are able to provide charging to a
connected smartphone.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

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

## UTC002.001 Thunderbolt 4 USB Type-C charging capability

**Test description**

This test verifies that the Thunderbolt 4 port is able to provide charging to
a connected smartphone.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect a phone to the Thunderbolt 4 USB Type-C port located on the left side
    of the laptop using a USB cable.
1. Note the charging status on the phone screen.

**Expected result**

1. The smartphone should indicate that it's charging.

## UTC003.001 USB Type-C PD laptop charging (Ubuntu 22.04)

**Test description**

This test verifies that the laptop can be charged using a USB Type-C PD power
supply connected to the Thunderbolt 4 port.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect the charger plug to the Thunderbolt 4 USB Type-C port located on the
    left side of the laptop.
1. Observe the battery indicator located in the top right corner of the screen.

**Expected result**

1. The battery indicator should indicate that the laptop is currently charging.

## UTC003.002 USB Type-C PD laptop charging (Windows 11)

**Test description**

This test verifies that the laptop can be charged using a USB Type-C PD power
supply connected to the Thunderbolt 4 port.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect the charger plug to the Thunderbolt 4 USB Type-C port located on the
    left side of the laptop.
1. Observe the battery indicator located in the bottom right corner of the
    screen.

**Expected result**

1. The battery indicator should indicate that the laptop is currently charging.

## UTC004.001 USB Type-C Display output (Ubuntu 22.04)

**Test description**

This test verifies that the laptop can output video to a display connected via
the Thunderbolt 4 USB Type-C port.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect a display to the Thunderbolt 4 USB Type-C port located on the left
    side of the laptop using the USB Type-C hub.
1. Open the Settings application and select the Displays panel in the left menu.
1. Verify that the attached external monitor can be selected.
1. Select and enable the monitor.

**Expected result**

1. The monitor connected to the laptop via the Thunderbolt 4 port should power
   on and display video from the laptop.

## UTC004.002 USB Type-C Display output (Windows 11)

**Test description**

This test verifies that the laptop can output video to a display connected via
the Thunderbolt 4 USB Type-C port.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect a display to the Thunderbolt 4 USB Type-C port located on the left.
    side of the laptop using a USB Type-C hub.
1. Right click on the desktop to open the desktop context menu.
1. Select `Display Settings` to open the display settings window.
1. Verify that the attached external monitor can be selected.
1. Select and enable the monitor.

**Expected result**

1. The monitor connected to the laptop via the Thunderbolt 4 port should power
   on and display video from the laptop.
