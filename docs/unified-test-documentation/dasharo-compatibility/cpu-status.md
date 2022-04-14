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

The `OPERATING_SYSTEM` screen should be displayed.

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

```bash
getconf -a | grep CACHE
```

1. Note the result.

**Expected result**

Example results:

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

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Execute below command in terminal:

```bash
lscpu
```

1. Note the result.

**Expected result**

Example results:

```bash
Architecture:                    ppc64le
Byte Order:                      Little Endian
CPU(s):                          32
On-line CPU(s) list:             0-31
Thread(s) per core:              4
Core(s) per socket:              4
Socket(s):                       2
NUMA node(s):                    2
...
```

If `CPU(s)` are more than 1, DUT has multiple CPU support.

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

```bash
lscpu
```

1. Note the result.

**Expected result**

Example results:

```bash
Architecture:                    ppc64le
Byte Order:                      Little Endian
CPU(s):                          32
On-line CPU(s) list:             0-31
Thread(s) per core:              4
Core(s) per socket:              4
Socket(s):                       2
NUMA node(s):                    2
...
```

If `Core(s) per socket` are more than 1, DUT has multi-core support.

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

```bash
cat /proc/cpuinfo | grep clock
```

1. Note the result.

**Expected result**

Example unwanted results:

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

The values of clock should be diffrent than `2700.000000MHz`.
