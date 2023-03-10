# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

Note, that the below-described test scope is used during Dasharo
Certification Procedure for both tested platforms:
`MSI PRO Z690-A WiFi DDR4` and `MSI PRO Z690-A DDR5`.

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
| 2.   | [UEFI compatible interface][EFI]                  | EFI           | All                                  |
| 3.   | [UEFI Shell][USH]                                 | USH           | All                                  |
| 4.   | [Display ports and LCD support][DSP]              | DSP           | DSP002.001, DSP002.002, DSP002.003, DSP003.001, DSP003.002, DSP003.003 |
| 5.   | [USB HID and MSC Support][USB]                    | USB           | All                                  |
| 6.   | [SMBIOS][DMI]                                     | DMI           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, DMI006.001, DMI008.001|
| 7.   | [Custom boot logo][CLG]                           | CLG           | All                                  |
| 8.   | [M.2 WiFi/Bluetooth][WLE]                         | WLE           | All                                  |
| 9.   | [Audio subsystem][AUD]                            | AUD           | AUD001.001, AUD001.002, AUD004.001, AUD004.002 AUD005.001, AUD005.002 AUD006.001, AUD006.002 |
| 10.  | [NVMe support][NVM]                               | NVM           | All                                  |
| 11.  | [Network boot][PXE]                               | PXE           | Without PXE007.001                   |
| 12.  | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
| 13.  | [Windows booting][WBT]                            | WBT           | All                                  |
| 14.  | [SD card support][SDC]                            | SDC           | All                                  |
| 15.  | [Custom Boot Keys][CBK]                           | CBK           | All                                  |
| 16.  | [Dasharo Tools Suite][DTS]                        | DTS           | DTS001.001, DTS002.001, DTS003.001, DTS004.001, DTS005.001, DTS006.001 |
| 17.  | [CPU status][CPU]                                 | CPU           | All                                  |
| 18.  | [Platform suspend and resume][SUSP]               | SUSP          | Without SUSP004.001                  |
| 19.  | [Super I/O initialization - QubesOS][PPS]         | PPS           | All                                  |
| 20.  | [Device power control operations][DPC]            | DPC           | All                                  |
| 21.  | [Display resolution - QubesOS][DSR]               | DSR           | All                                  |
| 22.  | [SATA hot-plug detection][SHT]                    | SHT           | All                                  |

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
[SDC]: ../../unified-test-documentation/dasharo-compatibility/316-sdcard-reader.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[DTS]: ../../unified-test-documentation/dasharo-compatibility/326-dasharo-tools-suite.md
[CPU]: ../../unified-test-documentation/dasharo-compatibility/31T-cpu-status.md
[SUSP]: ../../unified-test-documentation/dasharo-compatibility/31M-platform-suspend-and-resume.md
[PPS]: ../../unified-test-documentation/dasharo-compatibility/343-super-I-O-initialization-on-QubesOS.md
[DPC]: ../../unified-test-documentation/dasharo-compatibility/344-power-operations.md
[DSR]: ../../unified-test-documentation/dasharo-compatibility/345-display-resolution.md
[SHT]: ../../unified-test-documentation/dasharo-compatibility/346-SATA-hotplug-detection.md

## Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                                | TPM           | Without TPM001.001 and TPM002.001    |
| 2.   | [Verified Boot support][VBO]                      | VBO           | Without VBO006.001, VBO007.001       |
| 3.   | [Measured Boot support][MBO]                      | MBO           | All                                  |
| 4.   | [Secure Boot support][SBO]                        | SBO           | All                                  |
| 5.   | [ME neuter support][MNE]                          | MNE           | All                                  |
| 6.   | [BIOS lock support][BLS]                          | BLS           | All                                  |
| 7.   | [SMM BIOS write protection][SMM]                  | SMM           | All                                  |
| 8.   | [Early boot DMA protection][EDP]                  | EDP           | All                                  |
| 9.   | [BIOS Setup password][PSW]                        | PSW           | All                                  |
| 10.  | [Network Boot availability][NBA]                  | NBA           | All                                  |
| 11.  | [USB stack][USS]                                  | USS           | All                                  |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
[MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
[MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
[BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md
[SMM]: ../../unified-test-documentation/dasharo-security/20O-SMM-bios-write-protection.md
[EDP]: ../../unified-test-documentation/dasharo-security/20L-early-boot-dma-protection.md
[PSW]: ../../unified-test-documentation/dasharo-security/20R-bios-setup-password.md
[NBA]: ../../unified-test-documentation/dasharo-security/20T-network-boot-block.md
[USS]: ../../unified-test-documentation/dasharo-security/20S-usb-stack.md

### Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [coreboot bring up time measurement][CBMEM]       | CBMEM         | All                                  |
| 2.   | [CPU temperature measure][CPT]                    | CPT           | All                                  |
| 3.   | [CPU frequency measure][CPF]                      | CPF           | All                                  |

[CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
[CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
[CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
