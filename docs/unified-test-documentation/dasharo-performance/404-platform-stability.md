# Dasharo Performance: Platform stability

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

## STB001.001 Verify if no reboot occurs in the firmware

**Test description**

This test aims to verify that the DUT booted to the BIOS does not reset. The
test is performed in multiple iterations - this means that after a certain time
an attempt to read the same menu is repeated.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter setup menu.
1. Note the results.
1. After the specified time has elapsed, repeat the operation described in
    step 3.

**Expected result**

Platform should remain in the setup menu in every testing iteration.

## STB001.002 Verify if no reboot occurs in the OS (Ubuntu 22.04)

**Test description**

This test aims to verify that the DUT booted to the Operation System does not
reset. The test is performed in multiple iterations - this means that after a
certain time an attempt to read the same menu is repeated.

For the testing purposes, additional stability criteria are adopted:

* whether the platform has not lost connection to the Internet.

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
    uptime -p
    ```

1. Note the results.
1. Run the following command in the terminal to check if the platform has
    connection with the Internet:

    ```bash
    ip link | grep -E 'enp'
    ```

1. Note the results.
1. After the specified time has elapsed, repeat the operations described in
    steps 4-7.

**Expected result**

1. Subsequent readings of the `uptime -p` command output should indicate that
    the platform has not undergone a reboot.

    Example output of the command after 30 minutes of woroking

    ```bash
    up 30 minutes
    ```

1. Subsequent readings of the `ip link | grep -E 'enp'` command output should
    indicate that the platform has not lost connection to the Internet.

    Example output of the command:

    ```bash
    2: enp46s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    ```

    The `UP` in the output indicates that network interface is up and running.

## STB001.002 Verify if no reboot occurs in the OS (Windows 11)

**Test description**

This test aims to verify that the DUT booted to the Operation System does not
reset. The test is performed in multiple iterations - this means that after a
certain time an attempt to read the same menu is repeated.

For the testing purposes, additional stability criteria are adopted:

* whether the platform has not lost connection to the Internet.

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
1. Observe if platform is not resetting on its own.
1. Note the results.

**Expected result**

Platform should remain in system without rebooting during whole observation.
