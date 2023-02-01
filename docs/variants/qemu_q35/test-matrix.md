# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

Note, that the below-described test scope is used during Dasharo
Certification Procedure for tested platform:
`QEMU Q35 Machine`

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [UEFI compatible interface][EFI]                  | EFI           | All                                  |
| 2.   | [UEFI Shell][USH]                                 | USH           | All                                  |
| 3.   | [Display ports and LCD support][DSP]              | DSP           | DSP001.001      |
| 4.   | [Custom boot logo][CLG]                           | CLG           | All                                  |
| 5.  | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT001.001, LBT001.002, LBT002.001, LBT002.002, LBT003.001, LBT003.002, LBT004.001, LBT004.002|
| 6.  | [Windows booting][WBT]                            | WBT           | All                                  |
| 7.  | [Custom Boot Keys][CBK]                           | CBK           | All                                  |
| 8.  | [Qubes OS Support][QBS]                        | QBS           | QBS001.001, QBS001.002 |
| 9.  | [CPU status][CPU]                                 | CPU           | All                                  |
| 10.  | [BIOS Setup password][PSW]                        | PSW           | All                                  |

[EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
[USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[QBS]: ../../unified-test-documentation/dasharo-compatibility/309-qubesos-support.md
[CPU]: ../../unified-test-documentation/dasharo-compatibility/31T-cpu-status.md
[PSW]: ../../unified-test-documentation/dasharo-compatibility/329-bios-setup-password.md

## Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Secure Boot support][SBO]                        | SBO           | All                                  |
| 2.   | [ME neuter support][MNE]                          | MNE           | All                                  |
| 3.   | [BIOS lock support][BLS]                          | BLS           | All                                  |

[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
[MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
[BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md
