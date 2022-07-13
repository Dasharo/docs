
# Dasharo Compatibility: ME neuter

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup#os-boot-from-disk).

### MNE001.001 ME neuter support (Ubuntu 22.04)

**Test description**

This test aims to verify that ME neuter function works correctly.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the follwing command:

    ```bash
    lspci | grep Management Engine
    ```

1. Note teh results.

**Expected result**

1. The output of the command should not contain the information about
    Management Engine Interface.

Example of unwanted output:

```bash
Intel Corporation Comet Lake Management Engine Interface 
```
