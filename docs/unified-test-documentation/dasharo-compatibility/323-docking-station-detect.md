# Dasharo compatibility: Docking station detect

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
1. Connected `USB_STICK` to the USB port.

### DUD001.001 USB detection after coldboot (Ubuntu 22.04)

**Test description**

This test aims to verify that the DUT properly detects USB device after
coldboot (realized by power supply cutting off then restoring back).
This test case may be re-done several times to specify the platform and
connection stability.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Cut the power off while DUT is turned on.
1. Restore power and power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**

The `USB_STICK` is detected after coldboot.


### DUD002.001 USB detection after warmboot (Ubuntu 22.04)

**Test description**

This test aims to verify that the DUT properly detects USB device after
warmboot (realized by device turning off then turning on). This test case
may be re-done several times to specify the platform and connection stability.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**

The `USB_STICK` is detected after warmboot.

### DUD003.001 USB detection after reboot (Ubuntu 22.04)

**Test description**

This test aims to verify that the DUT properly detects USB device after system
reboot (performed by relevant command). This test case may be re-done
several times to specify the platform and connection stability.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    sudo reboot
    ```

1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    lsusb
    ```

1. Note the results.

**Expected result**

The `USB_STICK` is detected after reboot.
