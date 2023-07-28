# Dasharo Stability: Battery thresholds

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
1. Laptop's charger connected to the power outlet.

## BTS001.001 Charging until 98% battery level (Ubuntu 22.04)

**Test description**

This test aims to verify if charging the battery stops when the battery level
reaches 98% mark.

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
1. Open a terminal window and execute following command to check current battery
    charge level percentage:

    ```bash
    cat /sys/class/power_supply/BAT0/capacity
    ```

1. Note the results.
1. If the battery level sits below 95% mark, plug the charger into the DUT.
1. If the battery level sits above 95% mark, wait until the DUT's battery
    discharges to below 95% level and then plug the charger into the DUT.
1. Wait until the DUT's battery charge level reaches 98%.
1. Open a terminal window and execute following command to confirm that the
    battery charging stops at 98% mark:

    ```bash
    cat /sys/class/power_supply/BAT0/status
    ```

1. Note the results.

**Expected result**

1. The output of the `cat /sys/class/power_supply/BAT0/capacity` command should
    contain information about the current battery charge level.
1. The output of the `cat /sys/class/power_supply/BAT0/status` command should
    contain information about the current battery charging status.
    Example output:

    ```bash
    not charging
    ```

## BTS002.001 Not charging between 95% and 98% levels (Ubuntu 22.04)

**Test description**

This test aims to verify if charging the battery does not start after plugging
in the charger into the DUT when the battery level sits between 95% and 98%.

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
1. Open a terminal window and execute following command to check current battery
    charge level percentage:

    ```bash
    cat /sys/class/power_supply/BAT0/capacity
    ```

1. Note the results.
1. If the battery level sits between 95% and 98%, plug the charger into the DUT.
1. If the battery level sits below 95%, plug the charger into the DUT, wait
    until the battery reaches the level between 95% and 98% and then unplug the
    charger and plug it back in into the DUT.
1. Open a terminal window and execute following command to confirm that the
    battery does not start charging:

    ```bash
    cat /sys/class/power_supply/BAT0/status
    ```

1. The output of the `cat /sys/class/power_supply/BAT0/capacity` command should
    contain information about the current battery charge level.
1. The output of the `cat /sys/class/power_supply/BAT0/status` command should
    contain information about the current battery charging status.
    Example output:

    ```bash
    not charging
    ```
