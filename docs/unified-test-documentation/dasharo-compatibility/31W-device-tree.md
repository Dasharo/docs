# Dasharo compatibility: Device tree

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS preparation](../generic-test-setup.md#os-preparation).
1. Proceed with the
   [Generic test setup: OS post installation steps](../generic-test-setup.md#post-installation).

## DVT001.001 Node with coreboot exists

**Test description**

This test aims to verify whether the node with the coreboot exists in the Device
Tree.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Debian

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    xxd /sys/firmware/devicetree/base/firmware/coreboot/compatible
    ```

1. Note the result.

**Expected result**

The output of the command should contain information about memory sectors
dedicated for coreboot. Example output:

```bash
00000000: 636f 7265 626f 6f74 00                   coreboot
```

## DVT002.001 Memory for coreboot is reserved (Ubuntu)

**Test description**

This test aims to verify that in the system exists reserved memory for
coreboot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Debian

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    xxd /sys/firmware/devicetree/base/firmware/coreboot/reg
    ```

1. Note the results.
1. Run the following command in the terminal:

    ```bash
     xxd /sys/firmware/devicetree/base/reserved-memory/ranges
    ```

**Expected result**

1. Output of the first command should contain information about memory ranges
    for corebotot.
1. Output of the second command should contain information about reserved
    ranges.
1. All memory range for coreboot (output from command 1) should be reserved
    (output from command 2).
