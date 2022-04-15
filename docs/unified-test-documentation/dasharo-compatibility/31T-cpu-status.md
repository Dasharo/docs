# Dasharo Compatibility: CPU Status

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

### CPU001.001 CPU works

**Test description**

Check whether the mounted on the DUT CPU works.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Debian 11.0

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` screen should be displayed.

### CPU002.001 CPU cache enabled

**Test description**

Check whether all declared for the DUT cache levels are enabled.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Debian 11.0

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Execute below command in terminal:

    ```bash
    getconf -a | grep CACHE
    ```

1. Note the result.

**Expected result**

The utput of the command should contain information about all cache levels,
their size and association. Example output:

    ```bash
    LEVEL1_ICACHE_SIZE                 32768
    LEVEL1_ICACHE_ASSOC                32
    LEVEL1_ICACHE_LINESIZE             128
    LEVEL1_DCACHE_SIZE                 32768
    LEVEL1_DCACHE_ASSOC                32
    LEVEL1_DCACHE_LINESIZE             128
    LEVEL2_CACHE_SIZE                  524288
    LEVEL2_CACHE_ASSOC                 2048
    LEVEL2_CACHE_LINESIZE              32
    LEVEL3_CACHE_SIZE                  10485760
    LEVEL3_CACHE_ASSOC                 40960
    LEVEL3_CACHE_LINESIZE              32
    LEVEL4_CACHE_SIZE                  0
    LEVEL4_CACHE_ASSOC                 0
    LEVEL4_CACHE_LINESIZE              0
    ```

### CPU003.001 Multiple CPU support

**Test description**

Check whether the DUT has multiple CPU support.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Debian 11.0

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Execute below command in terminal:

    ```bash
    lscpu
    ```

1. Note the result.

**Expected result**

The output of the command should contain basic information about the CPU,
including the number of the `CPU (s)`. If `CPU(s)` are more than 1, the DUT
has multiple CPU support. Example results:

    ```bash
    Architecture:                    ppc64le
    Byte Order:                      Little Endian
    CPU(s):                          32
    On-line CPU(s) list:             0-31
    Thread(s) per core:              4
    Core(s) per socket:              4
    Socket(s):                       2
    NUMA node(s):                    2
    ```

### CPU004.001 Multiple-core support

**Test description**

Check whether the DUT has multi-core support.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Debian 11.0

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Execute below command in terminal:

    ```bash
    lscpu
    ```

1. Note the result.

**Expected result**

The output of the command should contain basic information about the CPU,
including the number of the `Core(s) per socket`. If `Core(s) per socket`
are more than 1, the DUT has multi-core support. Example results:

    ```bash
    Architecture:                    ppc64le
    Byte Order:                      Little Endian
    CPU(s):                          32
    On-line CPU(s) list:             0-31
    Thread(s) per core:              4
    Core(s) per socket:              4
    Socket(s):                       2
    NUMA node(s):                    2
    ```

### CPU005.001 CPU not stuck on initial frequency

**Test description**

Check whether the mounted CPU does not stuck on the initial frequency.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Debian 11.0

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Execute below command in terminal:

    ```bash
    cat /proc/cpuinfo | grep clock
    ```

1. Note the result.

**Expected result**

The output of the command should contain information about the current clock
frequency of each CPU. If the clock frequency for any clocks are the same or
current frequency is the same as initial frequency, the test should be
considered as failed.

Example of unwanted results:

    ```bash
    clock		: 2700.000000MHz
    clock		: 2700.000000MHz
    clock		: 2700.000000MHz
    clock		: 2700.000000MHz
    clock		: 2700.000000MHz
    clock		: 2700.000000MHz
    clock		: 2700.000000MHz
    clock		: 2700.000000MHz
    clock		: 2700.000000MHz
    clock		: 2700.000000MHz
    clock		: 2700.000000MHz
    clock		: 2700.000000MHz
    clock		: 2700.000000MHz
    clock		: 2700.000000MHz
    ```
