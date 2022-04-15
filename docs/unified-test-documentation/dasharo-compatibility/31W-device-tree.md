# Dasharo compatibility: Device tree

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

### DVT001.001 Node with coreboot exists

**Test description**

This test aims to verify whether the node with the coreboot exists in Device
Tree.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Debian 11.0

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    xxd /sys/firmware/devicetree/base/firmware/coreboot/compatible
    ```

1. Note the result.

**Expected result**

The output of the command should contain information about memory sectors
dedicated for coreboot. 

### DVT002.001 Memory for coreboot is reserved (Ubuntu 20.04)

**Test description**

This test aims to verify that in the system exists reserved memory for
coreboot.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    xxd /sys/firmware/devicetree/base/firmware/coreboot/reg
    ```

1. Note the results.

**Expected result**

If output is diffrent from:

```bash
No such file or directory
```

test completed successfully.

Example results:

```bash
1b[?2004l
00000000: 636f 7265 626f 6f74 00 coreboot.
1b[?2004h
```
