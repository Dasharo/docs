# Dasharo Compatibility: CPU Status

## Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup#os-boot-from-disk).

## CPU001.001 CPU works (Ubuntu 22.04)

**Test description**

Check whether the mounted on the DUT CPU works.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` screen should be displayed.

## CPU001.002 CPU works (Windows 11)

**Test description**

Check whether the mounted on the DUT CPU works.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` screen should be displayed.

## CPU002.001 CPU cache enabled (Ubuntu 22.04)

**Test description**

Check whether all declared for the DUT cache levels are enabled.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

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

## CPU002.002 CPU cache enabled (Windows 11)

**Test description**

Check whether all declared for the DUT cache levels are enabled.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Run PowerShell as an administrator and execute command:

    ```powershell
    Get-Wmiobject -class win32_cachememory | fl Purpose, CacheType, InstalledSize
    ```

1. Note the result.

**Expected result**

The output of the command should contain information about all cache levels,
their size and association. Example output:

```powershell
Purpose       : CACHE1
CacheType     : 4
InstalledSize : 192

Purpose       : CACHE1
CacheType     : 3
InstalledSize : 128

Purpose       : CACHE2
CacheType     : 5
InstalledSize : 5120

Purpose       : CACHE3
CacheType     : 5
InstalledSize : 8192
```

## CPU003.001 Multiple CPU support (Ubuntu 22.04)

**Test description**

Check whether the DUT has multiple CPU support.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

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

## CPU003.002 Multiple CPU support (Windows 11)

**Test description**

Check whether the DUT has multiple CPU support.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Run PowerShell as an administrator and execute command:

    ```powershell
    WMIC CPU Get NumberOfCores
    ```

1. Note the result.

**Expected result**

The output of the command should contain information about the CPUs.
Example results:

```powershell
NumberOfCores
4
```

## CPU004.001 Multiple-core support (Ubuntu 22.04)

**Test description**

Check whether the DUT has multi-core support.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

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

## CPU004.002 Multiple-core support (Windows 11)

**Test description**

Check whether the DUT has multi-core support.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot.
1. Run PowerShell as an administrator and check total CPU cores by executing
command:

    ```powershell
    WMIC CPU Get NumberOfCores
    ```

1. Note the result.
1. Check total CPU socket number by executing command:

    ```powershell
    (Get-CimInstance -ClassName Win32_ComputerSystem).NumberOfProcessors
    ```

1. Note the result.

**Expected result**

1. If number of cores is higher than number of sockets then DUT has multi-core
support. Example outputs:

- 1st command:

```powershell
NumberOfCores
4
```

- 2nd command:

```powershell
1
```
