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
test is performed in multiple iterations - after a defined time an attempt to
read the same menu is repeated.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While booting, press `SETUP_MENU_KEY` to enter the setup menu.
1. Note the results.
1. After the specified time has elapsed, repeat the operation described in
    step 3.

**Expected result**

The platform should remain in the setup menu in every testing iteration.

## STB001.002 Verify if no reboot occurs in the OS (Ubuntu 22.04)

**Test description**

This test aims to verify that the DUT booted to the Operation System does not
reset. The test is performed in multiple iterations - after a defined time an
attempt to read the output of specific commands confirming the stability of
work is repeated.

For testing purposes, additional stability criteria are adopted:

* Whether the platform has not lost connection to the Internet.

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
    a connection with the Internet:

    ```bash
    ip link | grep -E 'enp'
    ```

1. Note the results.
1. After the specified time has elapsed, repeat the operations described in
    steps 4-7.

**Expected result**

1. Subsequent readings of the first command output should indicate that
    the platform has not undergone a reboot.

    Example output of the command after 30 minutes of working:

    ```bash
    up 30 minutes
    ```

1. Subsequent readings of the second command output should indicate that the
    platform has not lost the connection to the Internet.

    Example output of the command:

    ```bash
    2: enp46s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    ```

    If the device is connected to the Internet, a `UP` status should appear
    for at least one physical interface.

## STB001.003 Verify if no reboot occurs in the OS (Windows 11)

**Test description**

This test aims to verify that the DUT booted to the Operation System does not
reset. The test is performed in multiple iterations - after a defined time an
attempt to read the output of specific commands confirming the stability of
work is repeated.

For testing purposes, additional stability criteria are adopted:

* Whether the platform has not lost connection to the Internet.

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
1. Run PowerShell as administrator and execute the following command:

    ```powershell
    (get-date) - (gcim Win32_OperatingSystem).LastBootUpTime
    ```

1. Note the results.
1. Run the following command in PowerShell to check if the platform has
    a connection with the Internet:

    ```powershell
    Get-NetAdapter -Name "Ethernet*"
    ```

1. Note the results.
1. After the specified time has elapsed, repeat the operations described in
    steps 4-7.

**Expected result**

1. Subsequent readings of the first command output should indicate that
    the platform has not undergone a reboot.

    Example output of the command after 17 minutes of working:

    ```powershell
    Days              : 0
    Hours             : 0
    Minutes           : 17
    Seconds           : 8
    Milliseconds      : 784
    Ticks             : 10287845330
    TotalDays         : 0.0119072283912037
    TotalHours        : 0.285773481388889
    TotalMinutes      : 17.1464088833333
    TotalSeconds      : 1028.784533
    TotalMilliseconds : 1028784.533
    ```

1. Subsequent readings of the second command output should indicate that the
    platform has not lost the connection to the Internet.

    Example output of the command:

    ```powershell
    Name                      InterfaceDescription                    ifIndex Status       MacAddress             LinkSpeed
    ----                      --------------------                    ------- ------       ----------             ---------
    Ethernet                  Realtek PCIe GbE Family Controller           15 Up           D4-93-90-0C-23-A1       100 Mbps
    ```

    If the device is connected to the Internet, a `UP` status should appear
    for at least one physical interface.
