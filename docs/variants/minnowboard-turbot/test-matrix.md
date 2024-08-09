# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary compatible with
MinnowBoard Turbot.

## Module: Dasharo compatibility

| No. | Supported test suite                  | Test suite ID | Supported test cases                 |
|:---:|:--------------------------------------|:-------------:|:-------------------------------------|
| 1.  | [UEFI compatible interface][EFI]      | EFI           | All                                  |
| 2.  | [Display ports][DSP]                  | DSP           | DSP002.001, DSP002.003               |
| 3.  | [Network boot][PXE]                   | PXE           | All                                  |
| 4.  | [Custom logo][CLG]                    | CLG           | All                                  |
| 5.  | [Custom Boot Keys][CBK]               | CBK           | All                                  |
| 6.  | [USB HID and MSC Support][USB]        | USB           | USB001.xxx and USB002.xxx            |
| 7.  | [Debian Stable and Ubuntu LTS support][LBT]  | LBT    | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
| 8.  | [SMBIOS][DMI]                         | DMI           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, DMI006.001 |
| 9.  | [Custom network boot entries][CNB]    | CNB           | CNB001.002                           |
| 10. | [Audio subsystem][AUD]                | AUD           | AUD007.001, AUD008.001               |
| 11. | [UEFI Shell][USH]                     | USH           | All                                  |
| 12. | [USB detection][UDT]                  | UDT           | All                                  |
| 13. | [USB booting][UBT]                    | UBT           | All                                  |
| 14. | [Dasharo Tools Suite][DTS]            | DTS           | DTS001.001, DTS002.001, DTS003.001, DTS004.001, DTS005.001, DTS006.001 |
| 15. | [CPU status][CPU]                     | CPU           | CPU001.001, CPU001.002               |

[EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[NBT]: ../../unified-test-documentation/dasharo-compatibility/315b-netboot-utilities.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[PXE]: ../../unified-test-documentation/dasharo-compatibility/315-network-boot.md
[CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md
[USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
[DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
[AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
[UDT]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
[UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md
[CPU]: ../../unified-test-documentation/dasharo-compatibility/31T-cpu-status.md
[DTS]: ../../unified-test-documentation/dasharo-compatibility/326-dasharo-tools-suite.md

## Module: Dasharo security

| No. | Supported test suite                  | Test suite ID | Supported test cases                 |
|:----|:--------------------------------------|:-------------:|:-------------------------------------|
| 1.  | [Secure Boot support][SBO]            | SBO           | All                                  |
| 2.  | [BIOS lock support][BLS]              | BLS           | All                                  |
| 3.  | [SMM BIOS write protection][SMM]      | SMM           | All                                  |
| 4.  | [UEFI Setup password][PSW]            | PSW           | All                                  |
| 5.  | [Network stack enable/disable][NBA]   | NBA           | All                                  |
| 6.  | [USB stack enable/disable][USS]       | USS           | All                                  |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
[BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md
[SMM]: ../../unified-test-documentation/dasharo-security/20O-SMM-bios-write-protection.md
[PSW]: ../../unified-test-documentation/dasharo-security/20R-uefi-setup-password.md
[NBA]: ../../unified-test-documentation/dasharo-security/20T-network-boot.md
[USS]: ../../unified-test-documentation/dasharo-security/20S-usb-stack.md

## Module: Dasharo performance

| No. | Supported test suite                  | Test suite ID | Supported test cases                 |
|:----|:--------------------------------------|:-------------:|:-------------------------------------|
| 1.  | [coreboot bring up time measurement][CBMEM] | CBMEM         | All                            |
| 2.  | [CPU temperature measure][CPT]        | CPT           | All                                  |
| 3.  | [CPU frequency measure][CPF]          | CPF           | Without CPU003.XXX and CPU005.XXX    |
| 4.  | [Platform stability][STB]             | STB           | All                                  |

[CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
[CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
[CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
[STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md
[BUB]: ../../unified-test-documentation/dasharo-performance/407-ubuntu-booting-performance-test.md
[BDE]: ../../unified-test-documentation/dasharo-performance/408-debian-booting-performance-test.md
