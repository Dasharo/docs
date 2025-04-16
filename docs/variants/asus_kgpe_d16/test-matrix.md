# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [coreboot base port][CBP]                         | CBP           | All                                  |
| 2.   | [SMBIOS][DMI]                                     | DMI           | DMI001.001, DMI002.001, DMI003.001, DMI004.001|
| 3.   | [coreboot fan control][FAN]                       | FAN           | All                                  |
| 4.   | [Custom boot menu key][CBK]                       | CBK           | All                                  |
| 5.   | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT001.001, LBT001.002, LBT002.001, LBT002.002|
| 6.   | [Network boot][PXE]                               | PXE           | PXE007.001                           |
| 7.   | [USB detection][UDT]                              | UDT           | All                                  |
| 8.   | [USB booting][UBT]                                | UBT           | All                                  |
| 9.   | [Platform suspend and resume][SUSP]               | SUSP          | SUSP001.001                          |
| 10.  | [Flash write protection][HWP]                     | HWP           | All                                  |
| 11.  | [Display ports and LCD support][DSP]              | DSP           | DSP004.201, DSP004.301               |

[CBP]: ../../unified-test-documentation/dasharo-compatibility/100-coreboot-base-port.md
[DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
[FAN]: ../../unified-test-documentation/dasharo-compatibility/S31-coreboot-fan-control.md
[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[PXE]: ../../unified-test-documentation/dasharo-compatibility/315-network-boot.md
[UDT]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
[UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md
[SUSP]: ../../unified-test-documentation/dasharo-compatibility/31M-platform-suspend-and-resume.md
[HWP]: ../../unified-test-documentation/dasharo-compatibility/31P-flash-write-protection.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md

## Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                                | TPM           | TPM001.002                           |
| 2.   | [Verified Boot support][VBO]                      | VBO           | VBO006.001, VBO007.001, VBO008.001   |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md

## Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [coreboot bring up time measurement][CBMEM]       | CBMEM         | All                                  |
| 2.   | [Fan control measure][FNM]                        | FNM           | All                                  |

[CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
[FNM]: ../../unified-test-documentation/dasharo-performance/405-fan-control-measure.md
