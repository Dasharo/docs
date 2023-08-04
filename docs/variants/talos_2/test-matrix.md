# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [coreboot base port][CBP]                         | CBP           | CBP001.001, CBP002.001, CBP004.001   |
| 2.   | [Heads bootloader support][HDS]                   | HDS           | HDS001.001, HDS001.002               |
| 3.   | [Device Tree][DVT]                                | DVT           | DVT001.001, DVT002.001               |

[CBP]: https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/100-coreboot-base-port
[PBT]: https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31V-petitboot-payload-support
[HDS]: https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31U-heads-bootloader-support
[DVT]: https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31W-device-tree
[UDT]: https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31O-usb-detect
[UBT]: https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31N-usb-boot
[LBT]: https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support
[CPU]: https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31T-cpu-status
[USB]: https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support
[NVM]: https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/312-nvme-support
[DSP]: https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd

## Module: Dasharo security

| No.  | Supported test suite                         | Test suite ID | Supported test cases                 |
|:-----|:---------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                           | TPM           | TPM001.001 and TPM002.001            |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md

## Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [CPU frequency measure][CPF]                      | CPF           | CPF001.003                           |

[CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
