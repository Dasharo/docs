# Dasharo Stability: M.2 Wi-fi

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
   [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
   [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
   [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).

## SMW0001.001 Wi-fi connection after cold boot (Ubuntu 22.04)

**Test description**

This test aims to verify that the Wi-Fi card is detected and working correctly
after performing a cold boot. The test should be performed in multiple iterations.

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
1. Open a terminal window and run the following command:

    ```bash
    lspci | grep "Network Controller"
    ```

1. Open a terminal window and run the following commands:

    ```bash
    nmcli radio wifi on
    nmcli device wifi rescan
    # Wait ~5 seconds
    nmcli device wifi list
    ```

1. Disconnect the power source, and remove the battery if present.
1. Connect power and battery again.
1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lspci | grep "Network Controller"
    ```

1. Open a terminal window and run the following commands:

    ```bash
    nmcli radio wifi on
    nmcli device wifi rescan
    # Wait ~5 seconds
    nmcli device wifi list
    ```

**Expected result**

1. The output of each `lspci` command should contain information about the
   mounted on the DUT network controller. Example output:

    ```bash
    2f:00.0 Network controller: Intel Corporation Wi-Fi 6 AX201 (rev 1a)
    ```

1. The output of each `nmcli device` wifi list` command should return a list of
   available Wi-Fi networks. Example output:

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

## SMW0002.001 Wi-fi connection after warm boot (Ubuntu 22.04)

**Test description**

This test aims to verify that the Wi-Fi card is detected and working correctly
after performing a warm boot. The test is performed in multiple iterations.

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
1. Open a terminal window and run the following command:

    ```bash
    lspci | grep "Network Controller"
    ```

1. Open a terminal window and run the following commands:

    ```bash
    nmcli radio wifi on
    nmcli device wifi rescan
    # Wait ~5 seconds
    nmcli device wifi list
    ```

1. Power off the DUT using the power button.
1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lspci | grep "Network Controller"
    ```

1. Open a terminal window and run the following commands:

    ```bash
    nmcli radio wifi on
    nmcli device wifi rescan
    # Wait ~5 seconds
    nmcli device wifi list
    ```

**Expected result**

1. The output of each `lspci` command should contain information about the
   mounted on the DUT network controller. Example output:

    ```bash
    2f:00.0 Network controller: Intel Corporation Wi-Fi 6 AX201 (rev 1a)
    ```

1. The output of each `nmcli device` wifi list` command should return a list of
   available Wi-Fi networks. Example output:

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

## SMW0003.001 Wi-fi connection after reboot (Ubuntu 22.04)

**Test description**

This test aims to verify that the Wi-Fi card is detected and working correctly
after performing a reboot. The test is performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../generic-test-setup#firmware)

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lspci | grep "Network Controller"
    ```

1. Open a terminal window and run the following commands:

    ```bash
    nmcli radio wifi on
    nmcli device wifi rescan
    # Wait ~5 seconds
    nmcli device wifi list
    ```

1. Disconnect the power source, and remove the battery if present.
1. Connect power and battery again.
1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lspci | grep "Network Controller"
    ```

1. Open a terminal window and run the following commands:

    ```bash
    nmcli radio wifi on
    nmcli device wifi rescan
    # Wait ~5 seconds
    nmcli device wifi list
    ```

**Expected result**

1. The output of each `lspci` command should contain information about the
   mounted on the DUT network controller. Example output:

    ```bash
    2f:00.0 Network controller: Intel Corporation Wi-Fi 6 AX201 (rev 1a)
    ```

1. The output of each `nmcli device` wifi list` command should return a list of
   available Wi-Fi networks. Example output:

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

## SMW0004.001 Wi-fi connection after suspension (Ubuntu 22.04)

**Test description**

This test aims to verify that the Wi-Fi card is detected and working correctly
after performing suspension. The test is performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the [Firmware test suite](https://wiki.ubuntu.com/FirmwareTestSuite)
   package.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lspci | grep "Network Controller"
    ```

1. Open a terminal window and run the following commands:

    ```bash
    nmcli radio wifi on
    nmcli device wifi rescan
    # Wait ~5 seconds
    nmcli device wifi list
    ```

1. Execute the following command to suspend the system and automatically wake it
   up after 10 seconds:

    ```bash
    sudo fwts s3 --s3-sleep-delay=10
    ```

1. Open a terminal window and run the following command:

    ```bash
    lspci | grep "Network Controller"
    ```

1. Open a terminal window and run the following commands:

    ```bash
    nmcli radio wifi on
    nmcli device wifi rescan
    # Wait ~5 seconds
    nmcli device wifi list
    ```

**Expected result**

1. The output of each `lspci` command should contain information about the
   mounted on the DUT network controller. Example output:

    ```bash
    2f:00.0 Network controller: Intel Corporation Wi-Fi 6 AX201 (rev 1a)
    ```

1. The output of each `nmcli device` wifi list` command should return a list of
   available Wi-Fi networks. Example output:

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
