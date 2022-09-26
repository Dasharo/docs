# Dasharo Compatibility: miniPCIe slot verification

## Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup#os-boot-from-disk).

## MWL001.001 Wireless card detection (Ubuntu 22.04)

**Test description**

This test aims to verify that the Wi-Fi/Bluetooth card is enumerated correctly
and can be detected from the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

```bash
lspci | grep Network controller
```

**Expected result**

The output of the command should contain the line:

```bash
2f:00.0 Network controller: Intel Corporation Wi-Fi 6 AX200 (rev 1a)
```

The exact name and revision may be different depending on hardware
configuration.

## MWL001.002 Wireless card detection (Windows 11)

**Test description**

This test aims to verify that the Wi-Fi/Bluetooth card is enumerated correctly
and can be detected from the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open PowerShell and execute following command:

```powershell
Get-PnpDevice -PresentOnly | Select-String -Pattern "Wi-Fi"
```

1. Note the result.

**Expected result**

The output of the command should contain a line starting with:

```bash
Intel(R) Wi-Fi 6AX200 160MHz
```

or a line starting with:

```bash
Intel(R) Wi-Fi 6AX201 160MHz
```

## MWL002.001 Wi-Fi scanning (Ubuntu 22.04)

**Test description**

This test aims to verify that the Wi-Fi functionality of card is initialized
correctly and can be used from within the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.
1. Make sure to have any Wi-Fi signal available.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following commands as root:

```bash
nmcli radio wifi on
nmcli device wifi rescan
# Wait ~5 seconds
nmcli device wifi list
```

**Expected result**

The output of the last command should return a list of available Wi-Fi networks,
for example:

```bash
IN-USE  BSSID              SSID                    MODE   CHAN  RATE        SIGNAL  BARS  SECURITY
        XX:XX:XX:XX:XX:XX  DIRECT-ny               Infra  6     65 Mbit/s   75      ▂▄▆_  WPA2
*       XX:XX:XX:XX:XX:XX  3mdeb_abr_5GHz          Infra  48    405 Mbit/s  72      ▂▄▆_  WPA2
        XX:XX:XX:XX:XX:XX  3mdeb_abr               Infra  11    54 Mbit/s   69      ▂▄▆_  WPA2
        XX:XX:XX:XX:XX:XX  FunBox2-F9BF_2.4GHz     Infra  1     130 Mbit/s  50      ▂▄__  WPA1 WPA2
        XX:XX:XX:XX:XX:XX  H_Office                Infra  2     270 Mbit/s  35      ▂▄__  WPA2
        XX:XX:XX:XX:XX:XX  DIRECT-xpPhaser 3330    Infra  1     65 Mbit/s   34      ▂▄__  WPA2
        XX:XX:XX:XX:XX:XX  Orange_Swiatlowod_A79A  Infra  108   540 Mbit/s  32      ▂▄__  WPA2
        XX:XX:XX:XX:XX:XX  DIRECT-KRM288x Series   Infra  11    54 Mbit/s   22      ▂___  WPA2
        XX:XX:XX:XX:XX:XX  Orange_Swiatlowod_A79A  Infra  11    130 Mbit/s  20      ▂___  WPA2
        XX:XX:XX:XX:XX:XX  DIRECT-ejPhaser 3330    Infra  1     65 Mbit/s   17      ▂___  WPA2
        XX:XX:XX:XX:XX:XX  NED-WIFI                Infra  11    270 Mbit/s  17      ▂___  WPA2
```

## MWL002.002 Wi-Fi scanning (Windows 11)

**Test description**

This test aims to verify that the Wi-Fi functionality of card is initialized
correctly and can be used from within the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.
1. Make sure to have any Wi-Fi signal available

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open PowerShell and execute following command:

```powershell
netsh wlan show network
```

1. Note the result.

**Expected result**

1. Output should contain `3mdeb_abr` and/or `3mdeb_abr_5GHz`.
1. Example output:

```powershell
SSID 1 : 3mdeb_abr
    Network type            : Infrastructure
    Authentication          : WPA2-Personal
    Encryption              : CCMP

SSID 2 : Sonoff1 192.168.4.208 Hotspot
    Network type            : Infrastructure
    Authentication          : WPA2-Personal
    Encryption              : CCMP

SSID 3 : Orange_Swiatlowod_F1A0
    Network type            : Infrastructure
    Authentication          : WPA2-Personal
    Encryption              : CCMP

SSID 4 : Sonoff1 Fallback Hotspot
    Network type            : Infrastructure
    Authentication          : WPA2-Personal
    Encryption              : CCMP

SSID 5 : DIRECT-KRM288x Series
    Network type            : Infrastructure
    Authentication          : WPA2-Personal
    Encryption              : CCMP
```

## MWL003.001 Bluetooth scanning (Ubuntu 22.04)

**Test description**

This test aims to verify that the Bluetooth functionality of card is initialized
correctly and can be used from within the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.
1. Enable Bluetooth and make it discoverable in any device nearby DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following commands:

```bash
bluetoothctl
power on
scan on
# Wait ~5 seconds
devices
```

**Expected result**

The output of the last command should return a list of detectable Bluetooth
devices, for example:

```bash
Device XX:XX:XX:XX:XX:XX Device 1
Device XX:XX:XX:XX:XX:XX Wojtek N
Device XX:XX:XX:XX:XX:XX Mi Smart Band 4
Device XX:XX:XX:XX:XX:XX Galaxy Watch4 Classic (PHLM)
Device XX:XX:XX:XX:XX:XX Galaxy Watch4 Classic (PHLM)
Device XX:XX:XX:XX:XX:XX Device 2
Device XX:XX:XX:XX:XX:XX [Signage] Samsung QMR Series
Device XX:XX:XX:XX:XX:XX [Signage] Samsung QMR Series
Device XX:XX:XX:XX:XX:XX Device 3
Device XX:XX:XX:XX:XX:XX Device 4
Device XX:XX:XX:XX:XX:XX Device 5
Device XX:XX:XX:XX:XX:XX Device 6
```

## MWL003.002 Bluetooth scanning (Windows 11)

**Test description**

This test aims to verify that the Bluetooth functionality of card is initialized
correctly and can be used from within the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.
1. Enable Bluetooth and make it discoverable in any device nearby DUT

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Enter `Notification Center` in the bottom right part of the screen.
1. Using right mouse button click on the Bluetooth icon.
1. In shown drop-down menu click `Go to settings`.
1. Click the `+` icon described as `Add Bluetooth or other device`.
1. In the `Add a device` menu click `Bluetooth`.
1. Wait a few moments until DUT scans for nearby Bluetooth devices and note
   the result.

**Expected result**

Available Bluetooth devices should appear in the `Add a device` window.

## MWL004.001 LTE card detection (Ubuntu 22.04)

**Test description**

This test aims to verify that the LTE card is detected correctly in the
operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.
2. Plug the LTE card into miniPCIe slot.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute `lsusb`

**Expected result**

The output of the command should return a list of USB devices including LTE
module, for example:

```bash
Bus 001 Device 004: ID 05c6:9215 Qualcomm, Inc. Quectel EC20 LTE modem
```

<!-- TODO: add connection initiation with SIM card -->
