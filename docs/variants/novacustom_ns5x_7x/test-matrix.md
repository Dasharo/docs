# Test matrix - NovaCustom NS5x/7x

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

## Module: Dasharo compatibility

| No.  | Supported test suite                                   | Test suite ID | Supported test cases                 |
|:----:|:-------------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                      | HCL           | All                                  |
| 2.   | [UEFI compatible interface][EFI]                       | EFI           | All                                  |
| 3.   | [Display ports and LCD support][DSP]                   | DSP           | DSP001.001, DSP001.002, DSP001.003, DSP002.001, DSP002.002, DSP002.003 |
| 4.   | [Embedded Controller and Super I/O initialization][ECR]| ECR           | Whithout ECR010.001 and ECR010.002   |
| 5.   | [NVMe support][NVM]                                    | NVM           | All                                  |
| 6.   | [Custom logo][CLG]                                     | CLG           | All                                  |
| 7.   | [Custom boot menu key][CBK]                            | CBK           | All                                  |
| 8.   | [USB HID and MSC Support][USB]                         | USB           | All                                  |
| 9.   | [Debian Stable and Ubuntu LTS support][LBT]            | LBT           | All                                  |
| 10.  | [Windows booting][WBT]                                 | WBT           | WBT001.001                           |
| 11.  | [Audio subsystem][AUD]                                 | AUD           | All                                  |
| 12.  | [USB-C/Thunderbolt][UTC]                               | UTC           | All                                  |
| 13.  | [M.2 WiFi/Bluetooth][WLE]                              | WLE           | All                                  |
| 14.  | [SD card support][SDC]                                 | SDC           | All                                  |
| 15.  | [USB Camera verification][CAM]                         | CAM           | All                                  |
| 16.  | [Custom fan curve][FAN]                                | FAN           | FAN001.001                           |
| 17.  | [SMBIOS][DMI]                                          | DMI           | DMI002.001, DMI003.001, DMI005.001, DMI006.001, DMI007.001, DMI008.001  |
| 18.  | [Docking station detect][DUD]                          | DUD           | All                                  |
| 19.  | [Docking station USB devices][DUB]                     | DUB           | All                                  |
| 20.  | [Docking station Audio][DAU]                           | DAU           | All                                  |
| 21.  | [Docking station USB-C][DUC]                           | DUC           | All                                  |
| 22.  | [Firmware update using fwupd][FFW]                     | FFW           | All                                  |
| 23.  | [Firmware update using Dasharo Tools Suite][FDT]       | FDT           | All                                  |

[HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
[EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[ECR]: ../../unified-test-documentation/dasharo-compatibility/31G-ec-and-superio.md
[NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
[AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
[UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
[WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
[SDC]: ../../unified-test-documentation/dasharo-compatibility/316-sdcard-reader.md
[CAM]: ../../unified-test-documentation/dasharo-compatibility/317-usb-camera.md
[FAN]: ../../unified-test-documentation/dasharo-compatibility/S30-fan-control.md
[DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
[DUD]: ../../unified-test-documentation/dasharo-compatibility/323-docking-station-detect.md
[DUB]: ../../unified-test-documentation/dasharo-compatibility/324-docking-station-usb-devices.md
[DAU]: ../../unified-test-documentation/dasharo-compatibility/322-docking-station-audio.md
[DUC]: ../../unified-test-documentation/dasharo-compatibility/321-docking-station-usb-c.md
[FFW]: ../../unified-test-documentation/dasharo-compatibility/320-fwupd-firmware-update.md
[FDT]: ../../unified-test-documentation/dasharo-compatibility/326-DTS-firmware-update.md

## Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                                | TPM           | All                                  |
| 2.   | [Measured Boot support][MBO]                      | MBO           | All                                  |
| 3.   | [Secure Boot support][SBO]                        | SBO           | All                                  |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
[MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md

## Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [CPU frequency measure][CPF]       | CPF         | All                                  |

[CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
