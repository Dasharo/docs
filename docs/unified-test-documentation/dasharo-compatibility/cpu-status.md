# Dasharo Compatibility: CPU Status

## Test cases

### CPU001.001 CPU works

**Test description**

Check whether the CPU mounted on the DUT works.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

1. TBD

### CPU002.001 CPU cache enabled

**Test description**

Check whether the all declared for the DUT cache levels are enabled.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Execute below command in terminal:

        getconf -a | grep CACHE

1. Note the result.

**Expected result**

1. TBD

### CPU003.001 Multiple CPU support

**Test description**

Check whether the DUT has multiple CPU support.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Execute below command in terminal:

        lscpu

1. Note the result.

**Expected result**

1. TBD

### CPU004.001 Multiple-core support

**Test description**

Check whether the DUT has multi-core support.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Execute below command in terminal:

        lscpu

1. Note the result.

**Expected result**

1. TBD

### CPU005.001 CPU not stuck on initial frequency

**Test description**

Check whether the mounted CPU does not stuck on the initial frequency.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Execute below command in terminal:

        cat /proc/cpuinfo | grep clock

1. Note the result.

**Expected result**

1. TBD
