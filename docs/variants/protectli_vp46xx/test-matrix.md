# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary. The test scope is the same
for all platforms of the VP46XX family.

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:----:|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
| 2.   | [UEFI compatible interface][EFI]                  | EFI           | All                                  |
| 3.   | [Display ports][DSP]                              | DSP           | DSP002.001, DSP002.002, DSP002.003, DSP003.001, DSP003.002, DSP003.003 |
| 4.   | [Network boot utilities][NBT]                     | NBT           | All                                  |
| 5.   | [NVMe support][NVM]                               | NVM           | All                                  |
| 6.   | [Custom logo][CLG]                                | CLG           | All                                  |
| 7.   | [Custom boot menu key][CBK]                       | CBK           | All                                  |
| 8.   | [USB HID and MSC Support][USB]                    | USB           | All                                  |
| 9.   | [FreeBSD support][BSD]                            | BSD           | All                                  |
| 10.  | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
| 11.  | [USB-C/Thunderbolt][UTC]                          | UTC           | UTC004.001, UTC004.001               |
| 12.  | [M.2 WiFi/Bluetooth][WLE]                         | WLE           | ALL                                  |
| 13.  | [eMMC support][MMC]                               | MMC           | MMC001.001                           |
| 14.  | [SMBIOS][DMI]                                     | DMI           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, DMI006.001 |
| 15.  | [Custom network boot entries][CNB]                | CNB           | CNB001.002                           |
| 16.  | [M.2 automatic SATA/NVMe switching support][MSS]  | MSS           | MSS001.001                           |
| 17.  | [Windows booting][WBT]                            | WBT           | WBT001.001                           |
| 18.  | [Audio subsystem][AUD]                            | AUD           | AUD001.001, AUD001.002, AUD002.001, AUD002.002, AUD003.001, AUD003.002, AUD004.001, AUD004.002, AUD005.001, AUD005.002, AUD006.001, AUD006.002 |
| 19.  | [UEFI Shell][USH]                                 | USH           | All                                  |
| 20.  | [USB detection][UDT]                              | UDT           | All                                  |
| 21.  | [USB booting][UBT]                                | UBT           | All                                  |

[HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
[EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[NBT]: ../../unified-test-documentation/dasharo-compatibility/315b-netboot-utilities.md
[NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
[BSD]: ../../unified-test-documentation/dasharo-compatibility/307-freebsd-support.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
[WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
[MWL]: ../../unified-test-documentation/dasharo-compatibility/31K-minipcie-verification.md
[MMC]: ../../unified-test-documentation/dasharo-compatibility/31M-emmc-support.md
[DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
[CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md
[MSS]: ../../unified-test-documentation/dasharo-compatibility/31I-nvme-switching.md
[WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
[AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
[USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
[UDT]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
[UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md

## Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                                | TPM           | Without TPM001.001 and TPM002.001    |
| 2.   | [Verified Boot support][VBO]                      | VBO           | All                                  |
| 3.   | [Measured Boot support][MBO]                      | MBO           | All                                  |
| 4.   | [Secure Boot support][SBO]                        | SBO           | All                                  |
| 5.   | [ME neuter support][MNE]                          | MNE           | MNE003.001                           |
| 6.   | [BIOS lock support][BLS]                          | BLS           | All                                  |

> Note: in Dasharo compatible with Protectli VP46xx ME neuter support relies
on the default blocking of this functionality - no additional option for ME
neuter setting is available in the Setup Menu.

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
[MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
[MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
[BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md

## Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [coreboot bring up time measurement][CBMEM]       | CBMEM         | All                                  |
| 2.   | [CPU temperature measure][CPT]                    | CPT           | All                                  |
| 3.   | [CPU frequency measure][CPF]                      | CPF           | All                                  |
| 4.   | [Platform stability][STB]                         | STB           | All                                  |

[CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
[CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
[CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
[STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md
