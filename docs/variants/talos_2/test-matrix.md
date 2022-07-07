# Test matrix - Talos II

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [coreboot base port][CBP]                         | CBP           | CBP001.001, CBP002.001, CBP004.001   |
| 2.   | [Petitboot payload support][PBT]                  | PBT           | All                                  |
| 3.   | [Heads bootloader support][HDS]                   | HDS           | All                                  |
| 4.   | [Device Tree][DVT]                                | DVT           | All                                  |
| 5.   | [USB detection][USB]                              | USB           | All                                  |
| 6.   | [USB booting][UBT]                                | UBT           | All                                  |
| 7.   | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT002.001                           |
| 8.   | [CPU status][CPU]                                 | CPU           | All                                  |

[CBP]: ../../unified-test-documentation/dasharo-compatibility/100-coreboot-base-port.md
[PBT]: ../../unified-test-documentation/dasharo-compatibility/31V-petitboot-payload-support.md
[HDS]: ../../unified-test-documentation/dasharo-compatibility/31U-heads-bootloader-support.md
[DVT]: ../../unified-test-documentation/dasharo-compatibility/31W-device-tree.md
[USB]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
[UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[CPU]: ../../unified-test-documentation/dasharo-compatibility/31T-cpu-status.md

## Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [coreboot bring up time measurement][CBMEM]       | CBMEM         | All                                  |

[CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
