# Test matrix - Protectli VP4620

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:----:|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
| 2.   | [UEFI compatible interface][EFI]                  | EFI           | EFI001.001                           |
| 3.   | [Display ports][DSP]                              | DSP           | DSP002.001, DSP002.003, DSP003.001, DSP003.003 |
| 4.   | [Network boot][PXE]                               | PXE           | All                                  |
| 5.   | [NVMe support][NVM]                               | NVM           | NVM001.001, NVM001.002               |
| 6.   | [Custom logo][CLG]                                | CLG           | All                                  |
| 7.   | [Custom boot menu key][CBK]                       | CBK           | All                                  |
| 8.   | [USB HID and MSC Support][USB]                    | USB           | USB001.001, USB001.002, USB002.001, USB002.002 |
| 9.   | [FreeBSD support][BSD]                            | BSD           | All                                  |
| 10.  | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | All                                  |
| 11.  | [USB-C/Thunderbolt][UTC]                          | UTC           | UTC004.001                           |
| 12.  | [M.2 WiFi/Bluetooth][WLE]                         | WLE           | WLE001.001, WLE002.001, WLE003.001   |
| 13.  | [miniPCIe LTE/WiFi/Bluetooth][MWL]                | MWL           | MWL004.001                           |
| 14.  | [eMMC support][MMC]                               | MMC           | MMC001.001                           |
| 15.  | [SMBIOS][DMI]                                     | DMI           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, DMI006.001 |
| 16.  | [Custom network boot entries][CNB]                | CNB           | CNB001.002                           |
| 17.  | [M.2 automatic SATA/NVMe switching support][MSS]  | MSS           | MSS001.001                           |

[HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
[EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[PXE]: ../../unified-test-documentation/dasharo-compatibility/315-network-boot.md
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

## Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                                | TPM           | TPM001.001                           |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md

## Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Device boot measure][DBM]                        | DBM           | All                                  |

[DBM]: ../../unified-test-documentation/dasharo-performance/403-device-boot-measure.md
