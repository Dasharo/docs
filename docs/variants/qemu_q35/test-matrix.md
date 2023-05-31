# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

Note, that the below-described test scope is used during Dasharo Certification
Procedure for tested platform: `QEMU Q35 Machine`

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [UEFI compatible interface][EFI]                  | EFI           | All                                  |
| 2.   | [UEFI Shell][USH]                                 | USH           | All                                  |
| 3.   | [Display ports and LCD support][DSP]              | DSP           | DSP001.001                           |
| 4.   | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT001.001, LBT001.002, LBT002.001, LBT002.002, LBT003.001, LBT003.002, LBT004.001, LBT004.002|
| 5.   | [Network boot][PXE]                               | PXE           | All                                  |
| 6.   | [Windows booting][WBT]                            | WBT           | All                                  |
| 7.   | [Qubes OS Support][QBS]                           | QBS           | QBS001.001, QBS001.002               |
| 8.   | [CPU status][CPU]                                 | CPU           | All                                  |
| 9.   | [BIOS Setup password][PSW]                        | PSW           | All                                  |

[EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
[USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
[QBS]: ../../unified-test-documentation/dasharo-compatibility/309-qubesos-support.md
[CPU]: ../../unified-test-documentation/dasharo-compatibility/31T-cpu-status.md
[PSW]: ../../unified-test-documentation/dasharo-compatibility/329-bios-setup-password.md
[PXE]: ../../unified-test-documentation/dasharo-compatibility/315-network-boot.md

## Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                                | TPM           | Without TPM001.001, TPM002.001 and TPM003.001    |
| 2.   | [Secure Boot support][SBO]                        | SBO           | All                                  |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
