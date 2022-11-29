# Test matrix

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
| 5.   | [USB detection][UDT]                              | UDT           | All                                  |
| 6.   | [USB booting][UBT]                                | UBT           | All                                  |
| 7.   | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT001.002                           |
| 8.   | [CPU status][CPU]                                 | CPU           | All                                  |
| 9.   | [USB HID and MSC Support][USB]                    | USB           | USB001.001, USB001.002, USB002.001, USB002.002 |
| 10.  | [NVMe support][NVM]                               | NVM           | NVM001.001, NVM001.002               |
| 11.  | [Display ports and LCD support][DSP]              | DSP           | DSP004.001, DSP004.003               |

[CBP]: ../../unified-test-documentation/dasharo-compatibility/100-coreboot-base-port.md
[PBT]: ../../unified-test-documentation/dasharo-compatibility/31V-petitboot-payload-support.md
[HDS]: ../../unified-test-documentation/dasharo-compatibility/31U-heads-bootloader-support.md
[DVT]: ../../unified-test-documentation/dasharo-compatibility/31W-device-tree.md
[UDT]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
[UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[CPU]: ../../unified-test-documentation/dasharo-compatibility/31T-cpu-status.md
[USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support/
[NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support/
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd/

## Module: Dasharo security

| No.  | Supported test suite                         | Test suite ID | Supported test cases                 |
|:-----|:---------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                           | TPM           | TPM001.001 and TPM002.001            |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md

## Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [coreboot bring up time measurement][CBMEM]       | CBMEM         | All                                  |
| 2.   | [CPU frequency measure][CPF]                      | CPF           | CPF001.001                           |

[CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
[CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
