# Dasharo Compatibility: NET controller after coldboot/warmboot/reboot/suspend

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../generic-test-setup.md#os-boot-from-disk).
1. The `Thunderbolt docking station` connected to the Thunderbolt port.

## NET001.001 201 controller after coldboot (Ubuntu)

**Test description**

This test aims to verify that the network controller works and the platform
is able to connect to the network after coldboot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a Ethernet cable with internet connection to the platform.
1. Wait for internet connection to initialize.
1. Open a terminal window and execute following command to list available
    network interfaces:

    ```bash
    ip a
    ```

1. Determine the name of the ethernet controller. It typically is `ethX` or
    `enpXsY`, where `X` and `Y`  are numbers.
1. Then, execute following command to check if the network interface is working
    correctly:

    ```bash
    cat /sys/class/net/<interface_name>/operstate
    ```

1. Perform coldboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the command mentioned in point 8.

**Expected result**

1. The `ip a` command should return information about available NET
    interfaces. The list should contain the ethernet network interface, which is
    typically identified as `ethX` or `enpXsY`, where `X` and `Y`  are numbers.
    Example output:

    ```bash
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
    2: enp46s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether d4:93:90:16:92:f8 brd ff:ff:ff:ff:ff:ff
    inet 192.168.4.85/24 brd 192.168.4.255 scope global dynamic noprefixroute enp46s0
       valid_lft 40276sec preferred_lft 40276sec
    inet6 fe80::8317:79e3:81ec:a1f4/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
    3: wlp0s20f3: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
    link/ether 14:18:c3:7d:77:06 brd ff:ff:ff:ff:ff:ff
    ```

1. The `cat /sys/class/net/<interface_name>/operstate` command should return
    information indicating if the network interface works correctly (`up`) or
    not (`down`). Example output:

    ```bash
    up
    ```

## NET002.201 NET controller after warmboot (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## NET003.201 NET controller after reboot (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## NET004.201 NET controller after suspend (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop
