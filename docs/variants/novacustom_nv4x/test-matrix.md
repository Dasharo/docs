# Test matrix - NovaCustom NV41

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

## Test matrix - NovaCustom NV41MZ

### Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
| 2.   | [UEFI compatible interface][EFI]                  | EFI           | All                                  |
| 3.   | [Display ports and LCD support][DSP]              | DSP           | DSP001.001, DSP001.002, DSP001.003, DSP002.001, DSP002.002, DSP002.003 |
| 4.   | [Embedded Controller and Super I/O initialization][ECR] | ECR     | Without ECR021.xxx - ECR024.xxx      |
| 5.   | [NVMe support][NVM]                               | NVM           | All                                  |
| 6.   | [Custom logo][CLG]                                | CLG           | All                                  |
| 7.   | [Custom boot menu key][CBK]                       | CBK           | All                                  |
| 8.   | [USB HID and MSC Support][HID]                    | USB           | All                                  |
| 9.   | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
| 10.  | [UEFI Shell][USH]                                 | USH           | All                                  |
| 11.  | [Windows booting][WBT]                            | WBT           | WBT001.001                           |
| 12.  | [Audio subsystem][AUD]                            | AUD           | All                                  |
| 13.  | [USB-C/Thunderbolt][UTC]                          | UTC           | All                                  |
| 14.  | [Network boot][PXE]                               | PXE           | without PXE007.001                   |
| 15.  | [M.2 WiFi/Bluetooth][WLE]                         | WLE           | All                                  |
| 16.  | [SD card support][SDC]                            | SDC           | All                                  |
| 17.  | [USB Camera verification][CAM]                    | CAM           | All                                  |
| 18.  | [Nvidia Graphics support][NVI]                    | NVI           | All                                  |
| 19.  | [Custom fan curve][FAN]                           | FAN           | FAN001.001                           |
| 20.  | [SMBIOS][DMI]                                     | DMI           | DMI002.001, DMI003.001, DMI005.001, DMI006.001, DMI007.001, DMI008.001 |
| 21.  | [Docking station detect][DUD]                     | DUD           | All                                  |
| 22.  | [Docking station USB devices][DUB]                | DUB           | All                                  |
| 23.  | [Docking station Audio][DAU]                      | DAU           | All                                  |
| 24.  | [Docking station USB-C][DUC]                      | DUC           | All                                  |
| 25.  | [Firmware update using fwupd][FFW]                | FFW           | All                                  |
| 26.  | [Firmware update using Dasharo Tools Suite][FDT]  | FDT           | All                                  |
| 27.  | [Firmware locally building and flashing][FLB]     | FLB           | All                                  |
| 28.  | [Logo customization functionality][LCM]           | LCM           | All                                  |

[HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
[EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[ECR]: ../../unified-test-documentation/dasharo-compatibility/31G-ec-and-superio.md
[NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[HID]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
[WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
[AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
[UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
[PXE]: ../../unified-test-documentation/dasharo-compatibility/315-network-boot.md
[WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
[SDC]: ../../unified-test-documentation/dasharo-compatibility/316-sdcard-reader.md
[CAM]: ../../unified-test-documentation/dasharo-compatibility/317-usb-camera.md
[NVI]: ../../unified-test-documentation/dasharo-compatibility/319-nvidia-graphics.md
[FAN]: ../../unified-test-documentation/dasharo-compatibility/S30-fan-control.md
[DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
[DUD]: ../../unified-test-documentation/dasharo-compatibility/323-docking-station-detect.md
[DUB]: ../../unified-test-documentation/dasharo-compatibility/324-docking-station-usb-devices.md
[DAU]: ../../unified-test-documentation/dasharo-compatibility/322-docking-station-audio.md
[DUC]: ../../unified-test-documentation/dasharo-compatibility/321-docking-station-usb-c.md
[FFW]: ../../unified-test-documentation/dasharo-compatibility/320-fwupd-firmware-update.md
[FDT]: ../../unified-test-documentation/dasharo-compatibility/326-DTS-firmware-update.md
[FLB]: ../../unified-test-documentation/dasharo-compatibility/326b-firmware-building-locally.md
[LCM]: ../../unified-test-documentation/dasharo-compatibility/328-logo-customization-functionality.md

### Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                                | TPM           | All                                  |
| 2.   | [Verified Boot support][VBO]                      | VBO           | VBO001.002, VBO002.002, VBO003.001, VBO004.001, VBO005.001 |
| 3.   | [Measured Boot support][MBO]                      | MBO           | All                                  |
| 4.   | [Secure Boot support][SBO]                        | SBO           | All                                  |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
[MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md

## Test matrix - NovaCustom NV41MB

### Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
| 2.   | [UEFI compatible interface][EFI]                  | EFI           | All                                  |
| 3.   | [Display ports and LCD support][DSP]              | DSP           | DSP001.001, DSP001.002, DSP001.003, DSP002.001, DSP002.002, DSP002.003 |
| 4.   | [Embedded Controller and Super I/O initialization][ECR] | ECR     | Without ECR021.xxx - ECR024.xxx      |
| 5.   | [NVMe support][NVM]                               | NVM           | All                                  |
| 6.   | [Custom logo][CLG]                                | CLG           | All                                  |
| 7.   | [Custom boot menu key][CBK]                       | CBK           | All                                  |
| 8.   | [USB HID and MSC Support][HID]                    | USB           | All                                  |
| 9.   | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | All                                  |
| 10.  | [UEFI Shell][USH]                                 | USH           | All                                  |
| 11.  | [Windows booting][WBT]                            | WBT           | WBT001.001                           |
| 12.  | [Audio subsystem][AUD]                            | AUD           | All                                  |
| 13.  | [USB-C/Thunderbolt][UTC]                          | UTC           | All                                  |
| 14.  | [Network boot][PXE]                               | PXE           | All                                  |
| 15.  | [M.2 WiFi/Bluetooth][WLE]                         | WLE           | All                                  |
| 16.  | [SD card support][SDC]                            | SDC           | All                                  |
| 17.  | [USB Camera verification][CAM]                    | CAM           | All                                  |
| 18.  | [Custom fan curve][FAN]                           | FAN           | All                                  |
| 19.  | [SMBIOS][DMI]                                     | DMI           | DMI002.001, DMI003.001, DMI005.001, DMI006.001, DMI007.001, DMI008.001 |
| 20.  | [Docking station detect][DUD]                     | DUD           | All                                  |
| 21.  | [Docking station USB devices][DUB]                | DUB           | All                                  |
| 22.  | [Docking station Audio][DAU]                      | DAU           | All                                  |
| 23.  | [Docking station USB-C][DUC]                      | DUC           | All                                  |
| 24.  | [Firmware update using fwupd][FFW]                | FFW           | All                                  |
| 25.  | [Firmware update using Dasharo Tools Suite][FDT]  | FDT           | All                                  |
| 26.  | [Firmware locally building and flashing][FLB]     | FLB           | All                                  |
| 27.  | [Logo customization functionality][LCM]           | LCM           | All                                  |

[HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
[EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[ECR]: ../../unified-test-documentation/dasharo-compatibility/31G-ec-and-superio.md
[NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[HID]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
[WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
[AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
[UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
[PXE]: ../../unified-test-documentation/dasharo-compatibility/315-network-boot.md
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
[FLB]: ../../unified-test-documentation/dasharo-compatibility/326b-firmware-building-locally.md
[LCM]: ../../unified-test-documentation/dasharo-compatibility/328-logo-customization-functionality.md

### Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                                | TPM           | All                                  |
| 2.   | [Verified Boot support][VBO]                      | VBO           | Without VBO001.001 and VBO002.001    |
| 3.   | [Measured Boot support][MBO]                      | MBO           | All                                  |
| 4.   | [Secure Boot support][SBO]                        | SBO           | All                                  |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
[MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
