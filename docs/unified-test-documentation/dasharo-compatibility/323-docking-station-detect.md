# Dasharo compatibility: Docking station detect

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
1. The docking station connected to the USB-C port.

## DUD001.001 Docking station detection after coldboot (Ubuntu 22.04)

**Test description**

This test aims to verify that the DUT properly detects the docking station after
coldboot (realized by power supply cutting off then restoring back).
This test case may be re-done several times to specify the platform and
connection stability.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Cut the power off while DUT is turned on.
1. Restore power and power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**

After `lsusb` command the docking station entries should be displayed, but
output can be different depending on the model of the docking station.

Example entries signifing the docking station:

```bash
Bus 002 Device 010: Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter
Bus 002 Device 009: Prolific Technology, Inc. USB SD Card Reader
Bus 002 Device 008: VIA Labs, Inc. USB3.0 Hub
```

## DUD002.001 Docking station detection after warmboot (Ubuntu 22.04)

**Test description**

This test aims to verify that the DUT properly detects the docking station
after warmboot (realized by device turning off then turning on). This test case
may be re-done several times to specify the platform and connection stability.

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
    lsusb
    ```

1. Note the results.

**Expected result**

After `lsusb` command the docking station entries should be displayed, but
output can be different depending on the model of the docking station.

Example entries signifing the docking station:

```bash
Bus 002 Device 010: Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter
Bus 002 Device 009: Prolific Technology, Inc. USB SD Card Reader
Bus 002 Device 008: VIA Labs, Inc. USB3.0 Hub
```

## DUD003.001 Docking station detection after reboot (Ubuntu 22.04)

**Test description**

This test aims to verify that the DUT properly detects the docking station
after system reboot (performed by relevant command). This test case may be
re-done several times to specify the platform and connection stability.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    sudo reboot
    ```

1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**

After `lsusb` command the docking station entries should be displayed, but
output can be different depending on the model of the docking station.

Example entries signifing the docking station:

```bash
Bus 002 Device 010: Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter
Bus 002 Device 009: Prolific Technology, Inc. USB SD Card Reader
Bus 002 Device 008: VIA Labs, Inc. USB3.0 Hub
```
