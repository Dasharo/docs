# Dasharo Compatibility: M.2 WiFi/Bluetooth

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).

### WLE001.001 Wireless card detection (Ubuntu 20.04)

**Test description**

This test aims to verify that the Wi-Fi/Bluetooth card is enumerated correctly
and can be detected from the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
1. Open a terminal window and execute the following command:

```
lspci | grep AX20
```

**Expected result**

The output of the command should contain the line:

```
2f:00.0 Network controller: Intel Corporation Wi-Fi 6 AX200 (rev 1a)
```

The exact name and revision may be different depending on hardware configuration.

### WLE001.002 Wireless card detection (Windows 11)

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
1. Log into system by using the proper login and password.
1. Open PowerShell and execute following command:

```
Get-PnpDevice -PresentOnly | Select-String -Pattern "Wi-Fi"
```

1. Note the result.

**Expected result**

The output of the command should contain a line starting with:

```
Intel(R) Wi-Fi 6AX200 160MHz
```

or a line starting with:

```
Intel(R) Wi-Fi 6AX201 160MHz
```

### WLE002.001 Wi-Fi scanning (Ubuntu 20.04)

**Test description**

This test aims to verify that the Wi-Fi functionality of card is initialized
correctly and can be used from within the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the [Common](#common) section.
1. Make sure to have any Wi-Fi signal available.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
1. Open a terminal window and execute the following commands as root:

```
nmcli radio wifi on
nmcli device wifi rescan
# Wait ~5 seconds
nmcli device wifi list
```

**Expected result**

The output of the last command should return a list of available Wi-Fi networks,
for example:

```
IN-USE  BSSID              SSID                    MODE   CHAN  RATE        SIGNAL  BARS  SECURITY
        36:78:EE:05:03:45  DIRECT-ny               Infra  6     65 Mbit/s   75      ▂▄▆_  WPA2
*       60:38:E0:D6:46:9A  3mdeb_abr_5GHz          Infra  48    405 Mbit/s  72      ▂▄▆_  WPA2
        60:38:E0:D6:46:99  3mdeb_abr               Infra  11    54 Mbit/s   69      ▂▄▆_  WPA2
        D8:D7:75:02:F9:BF  FunBox2-F9BF_2.4GHz     Infra  1     130 Mbit/s  50      ▂▄__  WPA1 WPA2
        30:5A:3A:A1:46:B0  H_Office                Infra  2     270 Mbit/s  35      ▂▄__  WPA2
        9E:93:4E:74:C0:3F  DIRECT-xpPhaser 3330    Infra  1     65 Mbit/s   34      ▂▄__  WPA2
        D8:A7:56:D9:A7:9F  Orange_Swiatlowod_A79A  Infra  108   540 Mbit/s  32      ▂▄__  WPA2
        86:25:19:05:D4:A0  DIRECT-KRM288x Series   Infra  11    54 Mbit/s   22      ▂___  WPA2
        D8:A7:56:D9:A7:9A  Orange_Swiatlowod_A79A  Infra  11    130 Mbit/s  20      ▂___  WPA2
        9E:93:4E:74:C0:57  DIRECT-ejPhaser 3330    Infra  1     65 Mbit/s   17      ▂___  WPA2
        B0:BE:76:06:9F:22  NED-WIFI                Infra  11    270 Mbit/s  17      ▂___  WPA2
```

### WLE002.002 Wi-Fi scanning (Windows 11)

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
1. Log into system by using the proper login and password.
1. Locate in the bottom right corner of the screen `Internet access`
   icon and click it.
1. Enable Wi-Fi and note the result.

**Expected result**

After enabling Wi-Fi available networks should appear
in the `Internet access` menu.

### WLE003.001 Bluetooth scanning (Ubuntu 20.04)

**Test description**

This test aims to verify that the Bluetooth functionality of card is initialized
correctly and can be used from within the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the [Common](#common) section.
1. Enable Bluetooth and make it discoverable in any device nearby DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
1. Open a terminal window and execute the following commands:

```
bluetoothctl
power on
scan on
# Wait ~5 seconds
devices
```

**Expected result**

The output of the last command should return a list of detectable Bluetooth
devices, for example:

```
Device 48:24:57:E0:61:74 48-24-57-E0-61-74
Device 88:BD:45:74:FA:A5 Wojtek N
Device CE:9E:7B:BF:69:F2 Mi Smart Band 4
Device 56:62:93:8B:1A:F9 Galaxy Watch4 Classic (PHLM)
Device 64:F2:FD:1E:26:BC Galaxy Watch4 Classic (PHLM)
Device 0F:18:A1:D9:23:F6 0F-18-A1-D9-23-F6
Device 8C:EA:48:B1:59:B3 [Signage] Samsung QMR Series
Device 8C:EA:48:B1:57:EB [Signage] Samsung QMR Series
Device 76:C7:FD:86:9B:0E 76-C7-FD-86-9B-0E
Device 40:5E:96:43:3A:6A 40-5E-96-43-3A-6A
Device 4C:58:3B:C1:37:90 4C-58-3B-C1-37-90
Device 6A:93:A2:6A:E5:20 6A-93-A2-6A-E5-20
```

### WLE003.002 Bluetooth scanning (Windows 10)

**Test description**

This test aims to verify that the Bluetooth functionality of card is initialized
correctly and can be used from within the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 10

**Test setup**

1. Proceed with the [Common](#common) section.
1. Enable Bluetooth and make it discoverable in any device nearby DUT

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
1. Enter `Notification Center` in the bottom right part of the screen.
1. Using right mouse button click on the Bluetooth icon.
1. In shown drop-down menu click `Go to settings`.
1. Click the `+` icon described as `Add Bluetooth or other device`.
1. In the `Add a device` menu click `Bluetooth`.
1. Wait a few moments until DUT scans for nearby Bluetooth devices and note
   the result.

**Expected result**

Available Bluetooth devices should appear in the `Add a device` window.
