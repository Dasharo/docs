# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

Note, that the below-described test scope is used during Dasharo Certification
Procedure for tested platform: `QEMU Q35 Machine`

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Custom Boot Keys][CBK]                           | CBK           | All                                  |
| 2.   | [UEFI Shell][USH]                                 | USH           | All                                  |
| 3.   | [Network boot][PXE]                               | PXE           | Without PXE004.001                   |
| 4.   | [SMBIOS][DMI]                                     | DMI           | Without DMI001.201 and DMI007.001    |

[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
[PXE]: ../../unified-test-documentation/dasharo-compatibility/315-network-boot.md
[DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md

## Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Network stack enable/disable][NBA]               | NBA           | All                                  |
| 2.   | [Secure Boot][SBO]                                | SBO           | Without SBO002.002                   |
| 3.   | [Measured boot][MBO]                              | MBO           | All                                  |
| 4.   | [UEFI Setup password][PSW]                        | PSW           | All                                  |

[NBA]: ../../unified-test-documentation/dasharo-security/20T-network-boot.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
[MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
[PSW]: ../../unified-test-documentation/dasharo-security/20R-uefi-setup-password.md
