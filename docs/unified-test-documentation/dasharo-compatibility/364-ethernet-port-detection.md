# Dasharo compatibility: Ethernet Port Detection

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

## ETH001.0XX All Expected NET Controllers Detected (Linux generic)

**Test description**

This test verifies that all expected onboard or add-in Ethernet network
controllers are correctly detected by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Know in advance how many and which Ethernet controllers are expected on the
DUT.
1. Make sure the DUT has reliable network connection for querying the PCI
database.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Run the following command:

    ```bash
    lspci -QQ | grep -i ethernet
    ```

1. Compare the output with the expected Ethernet controller list for the DUT.

**Expected result**

1. The output of the command contains a separate entry for each expected
Ethernet controller.
1. Each line corresponds to a known and expected device.

Example output:

```text
02:00.0 Ethernet controller: Intel Corporation Device 125c (rev 04)
03:00.0 Ethernet controller: Intel Corporation Device 125c (rev 04)
04:00.0 Ethernet controller: Intel Corporation Device 125c (rev 04)
05:00.0 Ethernet controller: Intel Corporation Device 125c (rev 04)
````

## ETH001.001 All Expected NET Controllers Detected (Ubuntu)

Follows the [generic ETH001.0XX Linux-based test case](#eth0010xx-all-expected-net-controllers-detected-linux-generic)

## ETH001.010 All Expected NET Controllers Detected (XCP-NG)

Follows the [generic ETH001.0XX Linux-based test case](#eth0010xx-all-expected-net-controllers-detected-linux-generic)

## ETH001.011 All Expected NET Controllers Detected (ESXi)

**Test description**

This test verifies that all expected onboard or add-in Ethernet network
controllers are correctly detected by ESXi.

**Test setup**

1. Know the expected number and models of Ethernet controllers in the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into ESXi.
1. Log into the system via SSH or DCUI.
1. Run the following command:

    ```bash
    esxcli network nic list
    ```

1. Compare the output against the expected list of Ethernet devices.

**Expected result**

1. Each expected Ethernet controller appears in the list.
1. Devices show a valid driver, link status, and MAC address.

Example output:

```text
Name    PCI Device    Driver      Link Speed    Duplex  MAC Address
vmnic0  0000:02:00.0  ixgbe       Up   10000Mbps Full    00:1b:21:bb:aa:cc
vmnic1  0000:03:00.0  ixgbe       Up   10000Mbps Full    00:1b:21:bb:aa:cd
```

## ETH002.0XX All Expected SFP Controllers Detected (Linux generic)

**Test description**

This test verifies that all expected onboard SFP network controllers are
correctly detected by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Know in advance how many and which SFP controllers are expected on the DUT.
1. Make sure the DUT has reliable network connection for querying the PCI
database.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Run the following command:

    ```bash
    lspci -QQ | grep -i SFP
    ```

1. Compare the output with the expected SFP controller list for the DUT.

**Expected result**

1. The output of the command contains a separate entry for each expected SFP controller.
1. Each line corresponds to a known and expected device.

Example output:

```text
01:00.0 Ethernet controller: Intel Corporation Ethernet Controller X710 for 10GbE SFP+ (rev 02)
01:00.1 Ethernet controller: Intel Corporation Ethernet Controller X710 for 10GbE SFP+ (rev 02)
````

## ETH002.010 All Expected SFP Controllers Detected (Ubuntu)

Follows the [generic ETH002.0XX Linux-based test case](#eth0020xx-all-expected-sfp-controllers-detected-linux-generic)

## ETH002.010 All Expected SFP Controllers Detected (XCP-NG)

Follows the [generic ETH002.0XX Linux-based test case](#eth0020xx-all-expected-sfp-controllers-detected-linux-generic)
