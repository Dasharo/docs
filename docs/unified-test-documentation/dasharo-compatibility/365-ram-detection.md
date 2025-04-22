# Dasharo compatibility: RAM Detection

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

## MEM001.0XX Expected RAM size detected in OS (Linux generic)

**Test description**

This test verifies that the installed physical memory (RAM) is properly
detected and reported by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_
1. Expected RAM: (e.g. 8192 MB)

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Confirm in advance the expected amount of physical memory installed on the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Run the following command:

    ```bash
    cat /proc/meminfo | grep MemTotal
    ```

1. Note the reported total memory value and compare it to the expected amount.

**Expected result**

1. The output shows the total usable memory in kilobytes.
1. The value should closely match the expected amount of installed RAM
(allowing for small OS/kernel reservations).

Example output for 8GB RAM:

```text
MemTotal:        8012348 kB
```

## MEM001.001 Expected RAM size detected in OS (Ubuntu)

Follows the [generic MEM001.0XX Linux-based test case](#mem0010xx-expected-ram-size-detected-in-os-linux-generic)

## MEM001.010 Expected RAM size detected in OS (XCP-NG)

Follows the [generic MEM001.0XX Linux-based test case](#mem0010xx-expected-ram-size-detected-in-os-linux-generic)

### MEM001.011 Expected RAM Size Detected (ESXi)

**Test description**

Verifies that the installed RAM is correctly recognized by ESXi.

**Test setup**

Know the expected amount of installed memory on the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into ESXi.
1. Log in via SSH or DCUI.
1. Run:

    ```bash
    esxcli hardware memory get
    ```

**Expected result**

The total memory reported matches the installed amount (allowing small
variations due to reserved space).

Example output for 8GB RAM:

```text
Physical Memory: 8192 MB
```
