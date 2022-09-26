# Dasharo Compatibility: Docking station USB-C

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

## DUC001.001 USB Type-C laptop charging (Ubuntu 22.04)

**Test description**

This test aims to verify whether the DUT can be charged using a USB Type-C PD
power supply connected to the docking station, which is connected to the
Thunderbolt 4 port.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Disconnect any charger from the DUT.
1. Connect the docking station to the Thunderbolt 4 port located on the casing
    of the DUT.
1. Connect the charger plug to the docking station.
1. Open a terminal window and run the follwing command:

    ```bash
    cat /sys/class/power_supply/BAT0/status
    ```

1. Note the results

**Expected result**

Output of the command should show one of this: `Charging` or `Full`. That means
laptop is charged properly.

Example output:

```bash
Charging
```

## DUC001.002 USB Type-C laptop charging (Windows 11)

**Test description**

This test aims to verify whether the DUT can be charged using a USB Type-C PD
power supply connected to the docking station, which is connected to the
Thunderbolt 4 port.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Connect the docking station to the Thunderbolt 4 port located on the left side
    of the laptop.
1. Connect the charger plug to the docking station.
1. Open PowerShell and and run the follwing command:

    ```powershell
    Get-WmiObject win32_battery
    ```

1. Note the results

**Expected result**

If `BatteryStatus` is equal 2, that means laptop is charged properly.

Example part of output:

```powershell
BatteryStatus               : 2
```
