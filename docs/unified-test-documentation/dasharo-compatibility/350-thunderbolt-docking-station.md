# Dasharo Compatibility: Thunderbolt docking station

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
1. The docking station connected to the Thunderbolt port.

## TDS001.001 Thunderbolt laptop charging (Ubuntu 22.04)

**Test description**

This test aims to verify whether the DUT can be charged using a PD power supply
connected to the docking station, which is connected to the Thunderbolt port.

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
1. Disconnect any charger from the DUT.
1. Connect the charger plug to the docking station.
1. Open a terminal window and run the following command:

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

## TDS001.002 Thunderbolt laptop charging (Windows 11)

**Test description**

This test aims to verify whether the DUT can be charged using a PD power supply
connected to the docking station, which is connected to the Thunderbolt port.

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
1. Disconnect any charger from the DUT.
1. Connect the charger plug to the docking station.
1. Open PowerShell and and run the following command:

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
