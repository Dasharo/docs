# Test matrix - Protectli fw6e

## About

<!--
The test matrix is used to determine which of the test suites and test cases
described in this documentation are dedicated to the given platform
-->

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
| 2.   | [UEFI compatible interface][EFI]                  | EFI           | EFI001.001                           |
| 4.   | [Display ports and LCD support][DSP]              | DSP           | DSP002.001, DSP002.002, DSP002.003, DSP003.001, DSP003.002, DSP003.003 |
| 5.   | [USB HID and MSC Support][USB]                    | USB           | USB001.001, USB001.002, USB002.001, USB002.002 |
| 6.   | [SMBIOS][DMI]                                     | DMI           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, DMI006.001, DMI008.001|
| 7.   | [Custom boot logo][CLG]                           | CLG           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, DMI006.001 |
| 8.   | [M.2 WiFi/Bluetooth][WLE]                         | WLE           | WLE001.001, WLE002.001, WLE003.001   |
| 10.  | [NVMe support][NVM]                               | NVM           | NVM001.001, NVM001.002               |
| 11.  | [Network boot][PXE]                               | PXE           | All                                  |
| 12.  | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | All                                  |
| 15.  | [Custom logo][CLG]                                | CLG           | All                                  |
| 16.  | [Custom boot menu key][CBK]                       | CBK           | All                                  |
| 10.  | [FreeBSD support][BSD]                            | BSD           | All                                  |
| 12.  | [USB-C/Thunderbolt][UTC]                          | UTC           | UTC004.001                           |
| 14.  | [miniPCIe LTE/WiFi/Bluetooth][MWL]                | MWL           | MWL004.001                           |
| 15.  | [eMMC support][MMC]                               | MMC           | MMC001.001                           |
| 17.  | [Custom network boot entries][CNB]                | CNB           | CNB001.002                           |
| 18.  | [M.2 automatic SATA/NVMe switching support][MSS]  | MSS           | MSS001.001                           |

[HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
[EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
[DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[MWL]: ../../unified-test-documentation/dasharo-compatibility/31K-minipcie-verification.md
[WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
[NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
[PXE]: ../../unified-test-documentation/dasharo-compatibility/315-network-boot.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[BSD]: ../../unified-test-documentation/dasharo-compatibility/307-freebsd-support
[UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
[MMC]: ../../unified-test-documentation/dasharo-compatibility/31M-emmc-support.md
[CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md
[MSS]: ../../unified-test-documentation/dasharo-compatibility/31I-nvme-switching.md

## Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                                | TPM           | TPM001.001                           |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
