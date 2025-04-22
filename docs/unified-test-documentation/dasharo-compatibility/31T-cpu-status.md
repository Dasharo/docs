# Dasharo Compatibility: CPU Status

The test suite is fully automated for Windows and most Linux-based systems.
Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

If your OS is not supported by the OSFV, refer to the guide below.

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

## CPU001.0XX CPU works (Linux generic)

**Test description**

Check whether the mounted on the DUT CPU works.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` screen should be displayed.

## CPU001.010 CPU works (XCP-NG)

Follows the [generic CPU001.0XX Linux-based test case](#cpu0010xx-cpu-works-linux-generic)

## CPU001.011 CPU works (ESXI)

Follows the [generic CPU001.0XX Linux-based test case](#cpu0010xx-cpu-works-linux-generic)

## CPU002.0XX CPU cache enabled (Linux generic)

**Test description**

Check whether all declared for the DUT cache levels are enabled.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Execute below command in terminal:

    ```bash
    getconf -a | grep CACHE
    ```

1. Note the result.

**Expected result**

The output of the command should contain information about all cache levels,
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

## CPU002.010 CPU cache enabled (XCP-NG)

Follows the [generic CPU002.0XX Linux-based test case](#cpu0020xx-cpu-cache-enabled-linux-generic)

## CPU002.011 CPU cache enabled (ESXI)

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Execute below command in terminal:

```bash
esxcli hardware cpu list | grep Cache
```

1. Note the result.

**Expected result**

The output of the command should contain information about all cache levels,
their size and association. Example output:

```bash
L2 Cache Size: 2097152
L2 Cache Associativity: 16
L2 Cache Line Size: 64
L2 Cache CPU Count: 4
L3 Cache Size: 6291456
L3 Cache Associativity: 12
L3 Cache Line Size: 64
L3 Cache CPU Count: 4
```

## CPU003.0XX Multiple CPU support (Linux generic)

**Test description**

Check whether the DUT has multiple CPU support.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

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

## CPU003.010 Multiple CPU support (XCP-NG)

Follows the [generic CPU003.0XX Linux-based test case](#cpu0030xx-multiple-cpu-support-linux-generic)

## CPU003.011 Multiple CPU support (ESXI)

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Execute below command in terminal:

```bash
esxcli hardware cpu global get
```

1. Note the result.

**Expected result**

The output of the command should contain basic information about the CPU,
including the number of the `CPU Cores`. If it is greater than 1, the DUT
has multiple CPU support. Example results:

```bash
CPU Packages: 1
CPU Cores: 4
CPU Threads: 4
Hyperthreading Active: false
Hyperthreading Supported: false
Hyperthreading Enabled: true
HV Support: 3
```

## CPU004.0XX Multiple-core support (Linux generic)

**Test description**

Check whether the DUT has multi-core support.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = _Linux-based_

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

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

## CPU004.001 Multiple-core support (Ubuntu)

Follows the [generic CPU004.0XX Linux-based test case](#cpu0040xx-multiple-core-support-linux-generic)

## CPU004.010 Multiple-core support (XCP-NG)

Follows the [generic CPU004.0XX Linux-based test case](#cpu0040xx-multiple-core-support-linux-generic)

## CPU004.011 Multiple-core support (ESXI)

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Execute below command in terminal:

```bash
esxcli hardware cpu list | grep Id
```

1. Note the result.

**Expected result**

The output of the command will show a list of CPU cores on the system
along with the `Package Id:` This designates the socket to which the
core belongs.If the number of cores with the same `Package Id:`
is more than 1, the DUT has multi-core support. Example results:

```bash
Id: 0
Package Id: 0
Id: 1
Package Id: 0
Id: 2
Package Id: 0
Id: 3
Package Id: 0
```
