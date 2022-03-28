# Dasharo Compatibility: FreeBSD support

## Test cases

### Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).

### LBT001.001 Debian Stable installation and boot

**Test description**

This test verifies that FreeBSD distribution could be installed on 
the DUT and works properly.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = FreeBSD 13

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.