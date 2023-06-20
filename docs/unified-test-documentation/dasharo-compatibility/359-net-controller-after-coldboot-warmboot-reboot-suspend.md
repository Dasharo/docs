# Dasharo Compatibility: NET controller after coldboot/warmboot/reboot/suspend

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
1. The `Thunderbolt docking station` connected to the Thunderbolt port.

## NET001.001 NET controller after coldboot (Ubuntu 22.04)

**Test description**

This test aims to verify that the network controller works and the platform
is able to connect to the network after coldboot.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a Ethernet cable with internet connection to the platform.
1. Wait for internet connection to initialize.
1. Open a terminal window and execute following command to list avaliable
    network interfaces:

    ```
    ip a
    ```

1. Determine te name of the ethernet controller. It typically is `ethX` or
    `enpXsY`, where `X` and `Y`  are numbers.
1. Then, execute following command to check if the network interface is working
    correctly:

    ```
    cat /sys/class/net/<interface_name>/operstate
    ```

1. Perform coldboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the command mentioned in point 8.

**Expected result**

1. Command from point 6. should return information about avaliable NET
    interfaces. Example output:

    ```
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

1. Command from points 8. and 12. should return information indicating if the
    network interface works correctly (`up`) or not (`down`). Example output:

    ```
    up
    ```

## NET002.001 NET controller after warmboot (Ubuntu 22.04)

**Test description**

This test aims to verify that the network controller works and the platform
is able to connect to the network after warmboot.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a Ethernet cable with internet connection to the platform.
1. Wait for internet connection to initialize.
1. Open a terminal window and execute following command to list avaliable
    network interfaces:

    ```
    ip a
    ```

1. Determine te name of the ethernet controller. It typically is `ethX` or
    `enpXsY`, where `X` and `Y`  are numbers.
1. Then, execute following command to check if the network interface is working
    correctly:

    ```
    cat /sys/class/net/<interface_name>/operstate
    ```

1. Perform warmboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the command mentioned in point 8.

**Expected result**

1. Command from point 6. should return information about avaliable NET
    interfaces. Example output:

    ```
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

1. Command from points 8. and 12. should return information indicating if the
    network interface works correctly (`up`) or not (`down`). Example output:

    ```
    up
    ```

## NET003.001 NET controller after reboot (Ubuntu 22.04)

**Test description**

This test aims to verify that the network controller works and the platform
is able to connect to the network after coldboot.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a Ethernet cable with internet connection to the platform.
1. Wait for internet connection to initialize.
1. Open a terminal window and execute following command to list avaliable
    network interfaces:

    ```
    ip a
    ```

1. Determine te name of the ethernet controller. It typically is `ethX` or
    `enpXsY`, where `X` and `Y`  are numbers.
1. Then, execute following command to check if the network interface is working
    correctly:

    ```
    cat /sys/class/net/<interface_name>/operstate
    ```

1. Reboot the system.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the command mentioned in point 8.

**Expected result**

1. Command from point 6. should return information about avaliable NET
    interfaces. Example output:

    ```
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

1. Command from points 8. and 12. should return information indicating if the
    network interface works correctly (`up`) or not (`down`). Example output:

    ```
    up
    ```

## NET004.001 NET controller after suspend (Ubuntu 22.04)

**Test description**

This test aims to verify that the network controller works and the platform
is able to connect to the network after suspend.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Plug in a Ethernet cable with internet connection to the platform.
1. Wait for internet connection to initialize.
1. Open a terminal window and execute following command to list avaliable
    network interfaces:

    ```
    ip a
    ```

1. Determine te name of the ethernet controller. It typically is `ethX` or
    `enpXsY`, where `X` and `Y`  are numbers.
1. Then, execute following command to check if the network interface is working
    correctly:

    ```
    cat /sys/class/net/<interface_name>/operstate
    ```

1. Execute following command to suspend the system and automatically wake it
    up after 10 seconds:

    ```
    sudo fwts s3 --s3-sleep-delay=10
    ```

1. After the system wakes up, log into the system and execute the command mentioned in point 8.

**Expected result**

1. Command from point 6. should return information about avaliable NET
    interfaces. Example output:

    ```
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

1. Command from points 8. and 10. should return information indicating if the
    network interface works correctly (`up`) or not (`down`). Example output:

    ```
    up
    ```
