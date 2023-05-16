# Dasharo Compatibility: Thunderbolt docking station NET interface

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

## TDN001.001 Ethernet connection (Ubuntu 22.04)

**Test description**

This test aims to verify that the connection to internet via docking station's
Ethernet port can be obtained on Ubuntu 22.04.

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
1. Connect docking station to power source.
1. Connect DUT and docking station with `USBc - USBc` cable.
1. Plug in a Ethernet cable with internet connection to docking station.
1. Wait for internet connection to initialize.
1. Ping `3mdeb.com` using command in terminal:

    ```bash
    ping 3mdeb.com
    ```

**Expected result**

1. Command should return ping info:

    ```bash
    PING 3mdeb.com (178.32.205.96) 56(84) bytes of data.
    64 bytes from cluster026.hosting.ovh.net (178.32.205.96): icmp_seq=1 ttl=50 time=44.3 ms
    64 bytes from cluster026.hosting.ovh.net (178.32.205.96): icmp_seq=2 ttl=50 time=47.7 ms
    64 bytes from cluster026.hosting.ovh.net (178.32.205.96): icmp_seq=3 ttl=50 time=41.1 ms
    ...
    ```

1. Log should not contain phrase information that host is unreachable.

    Failed ping for Ubuntu 22.04:

    ```bash
    ping: connect: Network is unreachable
    ```

## TDN001.002 Ethernet connection (Windows 11)

**Test description**

This test aims to verify that the connection to internet via docking station's
Ethernet port can be obtained on Windows 11.

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
1. Connect docking station to power source.
1. Connect DUT and docking station with `USBc - USBc` cable.
1. Plug in a Ethernet cable with internet connection to docking station.
1. Wait for internet connection to initialize.
1. Ping `3mdeb.com` using command in PowerShell:

    ```PowerShell
    ping 3mdeb.com
    ```

**Expected result**

1. Command should return ping info:

    ```PowerShell
    Pinging 3mdeb.com [178.32.205.96] with 32 bytes of data:
    Reply from 178.32.205.96: bytes=32 time=50ms TTL=50
    Reply from 178.32.205.96: bytes=32 time=47ms TTL=50
    Reply from 178.32.205.96: bytes=32 time=46ms TTL=50
    ```

1. Log should not contain phrase information that host is unreachable.

    Failed ping for Windows 11:

    ```powershell
    Ping request could not find host 3mdeb.com. Please check the name and try again.
    ```
