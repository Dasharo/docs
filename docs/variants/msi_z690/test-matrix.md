# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

An up-to date test matrix used since release v1.1.3 is available
[here](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit#gid=1143764851)

Note that the test scope is used during Dasharo Certification Procedure for both
tested platforms: `MSI PRO Z690-A WiFi DDR4` and `MSI PRO Z690-A DDR5`.

> Following portion of the document contains the test matrix for releases older
> than v1.1.3 and is preserved for historical purposes.

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
| 2.   | [UEFI compatible interface][EFI]                  | EFI           | All                                  |
| 3.   | [UEFI Shell][USH]                                 | USH           | All                                  |
| 4.   | [Display ports and LCD support][DSP]              | DSP           | DSP002.201, DSP002.301, DSP002.003, DSP003.001, DSP003.002, DSP003.003 |
| 5.   | [USB HID and MSC Support][USB]                    | USB           | USB001.001, USB001.002, USB001.003, USB002.001, USB002.002 USB002.003 |
| 6.   | [SMBIOS][DMI]                                     | DMI           | All                                  |
| 7.   | [Custom boot logo][CLG]                           | CLG           | All                                  |
| 8.   | [M.2 WiFi/Bluetooth][WLE]                         | WLE           | All                                  |
| 9.   | [Audio subsystem][AUD]                            | AUD           | AUD001.201, AUD001.301, AUD004.201, AUD004.301 AUD005.201, AUD005.301 AUD006.201, AUD006.301 |
| 10.  | [NVMe support][NVM]                               | NVM           | All                                  |
| 11.  | [Network boot][PXE]                               | PXE           | Without PXE007.001                   |
| 12.  | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT004.001, LBT004.002               |
| 13.  | [Windows booting][WBT]                            | WBT           | WBT001.001                           |
| 14.  | [Custom Boot Keys][CBK]                           | CBK           | All                                  |
| 15.  | [Dasharo Tools Suite][DTS]                        | DTS           | DTS001.001, DTS002.001, DTS003.001, DTS004.001, DTS005.001, DTS006.001 |
| 16.  | [CPU status][CPU]                                 | CPU           | CNB001.201, CNB001.301               |
| 17.  | [Platform suspend and resume][SUSP]               | SUSP          | All                                  |
| 18.  | [Device power control operations][DPC]            | DPC           | All                                  |

[HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
[EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
[USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
[DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[MWL]: ../../unified-test-documentation/dasharo-compatibility/31K-minipcie-verification.md
[WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
[AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
[NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
[PXE]: ../../unified-test-documentation/dasharo-compatibility/315-network-boot.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[DTS]: ../../unified-test-documentation/dasharo-compatibility/326-dasharo-tools-suite.md
[CPU]: ../../unified-test-documentation/dasharo-compatibility/31T-cpu-status.md
[SUSP]: ../../unified-test-documentation/dasharo-compatibility/31M-platform-suspend-and-resume.md
[DPC]: ../../unified-test-documentation/dasharo-compatibility/344-power-operations.md

## Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                                | TPM           | Without TPM001.001 and TPM002.001    |
| 2.   | [Verified Boot support][VBO]                      | VBO           | Without VBO006.001, VBO007.001       |
| 3.   | [Measured Boot support][MBO]                      | MBO           | All                                  |
| 4.   | [Secure Boot support][SBO]                        | SBO           | All                                  |
| 5.   | [ME disable/neuter support][MNE]                  | MNE           | without MNE005.001                   |
| 6.   | [BIOS lock support][BLS]                          | BLS           | All                                  |
| 7.   | [SMM BIOS write protection][SMM]                  | SMM           | All                                  |
| 8.   | [Early boot DMA protection][EDP]                  | EDP           | All                                  |
| 9.   | [UEFI Setup password][PSW]                        | PSW           | All                                  |
| 10.  | [Network stack enable/disable][NBA]               | NBA           | All                                  |
| 11.  | [USB stack enable/disable][USS]                   | USS           | All                                  |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
[MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
[MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
[BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md
[SMM]: ../../unified-test-documentation/dasharo-security/20O-SMM-bios-write-protection.md
[EDP]: ../../unified-test-documentation/dasharo-security/20L-early-boot-dma-protection.md
[PSW]: ../../unified-test-documentation/dasharo-security/20R-uefi-setup-password.md
[NBA]: ../../unified-test-documentation/dasharo-security/20T-network-boot.md
[USS]: ../../unified-test-documentation/dasharo-security/20S-usb-stack.md

## Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [coreboot bring up time measurement][CBMEM]       | CBMEM         | All                                  |

[CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md

## coreboot + Heads

Please refer to the [tests results spreadsheet](https://docs.google.com/spreadsheets/d/1yWZ--zFPIsQhXZByf7nJIrasQYuRSf1yCi60lY_RGsQ/edit#gid=5649308).
