# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

## NV41MB test matrix

### Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
| 2.   | [UEFI compatible interface][EFI]                  | EFI           | All                                  |
| 3.   | [Display ports and LCD support][DSP]              | DSP           | DSP001.001, DSP001.002, DSP001.003, DSP002.001, DSP002.002 |
| 4.   | [Embedded Controller and Super I/O initialization][ECR] | ECR     | Without ECR021.xxx - ECR024.xxx, ECR25.001, ECR26.001, ECR27.001, ECR28.001 |
| 5.   | [NVMe support][NVM]                               | NVM           | All                                  |
| 6.   | [Custom logo][CLG]                                | CLG           | All                                  |
| 7.   | [Custom boot menu key][CBK]                       | CBK           | All                                  |
| 8.   | [USB HID and MSC Support][HID]                    | USB           | All                                  |
| 9.   | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT004.001, LBT004.002               |
| 10.  | [UEFI Shell][USH]                                 | USH           | All                                  |
| 11.  | [Windows booting][WBT]                            | WBT           | WBT001.001                           |
| 12.  | [Audio subsystem][AUD]                            | AUD           | All                                  |
| 13.  | [USB-C/Thunderbolt][UTC]                          | UTC           | All                                  |
| 14.  | [Network boot][PXE]                               | PXE           | Without PXE007.001                   |
| 15.  | [M.2 WiFi/Bluetooth][WLE]                         | WLE           | All                                  |
| 16.  | [SD card support][SDC]                            | SDC           | All                                  |
| 17.  | [USB Camera verification][CAM]                    | CAM           | All                                  |
| 18.  | [Fan speed measure][FAN]                          | FAN           | FAN001.001                           |
| 19.  | [SMBIOS][DMI]                                     | DMI           | Without DMI001.001                   |
| 20.  | [USB-C docking station detect][DUD]               | DUD           | All                                  |
| 21.  | [USB-C docking station USB devices][DUB]          | DUB           | All                                  |
| 22.  | [USB-C docking station Audio][DAU]                | DAU           | All                                  |
| 23.  | [USB-C docking station Display ports][DDP]        | DDP           | All                                  |
| 24.  | [USB-C docking station NET interface][DET]        | DET           | All                                  |
| 25.  | [Firmware update using fwupd][FFW]                | FFW           | All                                  |
| 26.  | [Dasharo Tools Suite][DTS]                        | DTS           | DTS006.001, DTS007.001               |
| 27.  | [CPU status][CPU]                                 | CPU           | All                                  |
| 28.  | [Embedded controller flashing][ECF]               | ECF           | All                                  |
| 29.  | [Logo customization functionality][LCM]           | LCM           | LCM001.001                           |
| 30.  | [Firmware locally building and flashing][FLB]     | FLB           | All                                  |
| 31.  | [Custom Boot Order][CBO]                          | CBO           | CBO001.002                           |
| 32.  | [QubesOS support][QBS]                            | QBS           | All                                  |
| 33.  | [Fedora support][FED]                             | FED           | All                                  |
| 34.  | [Platform suspend and resume][SUSP]               | SUSP          | SUSP001.001, SUSP002.001, SUSP003.001 |
| 35.  | [Thunderbolt docking station detect][TDD]         | TDD           | All                                  |
| 36.  | [Thunderbolt docking station USB devices][TDU]    | TDU           | All                                  |
| 37.  | [Thunderbolt docking station Audio][TDA]          | TDA           | All                                  |
| 38.  | [Thunderbolt docking station][TDS]                | TDS           | All                                  |
| 39.  | [Thunderbolt docking station Display ports][TDP]  | TDP           | All                                  |
| 40.  | [Thunderbolt docking station NET interface][TDN]  | TDN           | All                                  |
| 41.  | [Sign of life][SOL]                               | SOL           | All                                  |
| 42.  | [ME disable/neuter support][MNE]                  | MNE           | MNE001.001                           |
| 43.  | [NVIDIA Graphics support][NVI]                    | NVI           | All                                  |
| 44.  | [USB-C docking station SD card reader][DSD]       | DSD           | All                                  |
| 45.  | [BIOS menu function keys][BMF]                    | BMF           | All                                  |
| 46.  | [Suspend mechanism switching S0ix/S3][SMS]             | SMS           | All                                  |

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
[FAN]: ../../unified-test-documentation/dasharo-compatibility/S30-fan-speed.md
[DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
[DUD]: ../../unified-test-documentation/dasharo-compatibility/323-docking-station-detect.md
[DUB]: ../../unified-test-documentation/dasharo-compatibility/324-docking-station-usb-devices.md
[DAU]: ../../unified-test-documentation/dasharo-compatibility/322-docking-station-audio.md
[FFW]: ../../unified-test-documentation/dasharo-compatibility/320-fwupd-firmware-update.md
[DTS]: ../../unified-test-documentation/dasharo-compatibility/326-dasharo-tools-suite.md
[CPU]: ../../unified-test-documentation/dasharo-compatibility/31T-cpu-status.md
[ECF]: ../../unified-test-documentation/dasharo-compatibility/327-embedded_controller_flashing.md
[FLB]: ../../unified-test-documentation/dasharo-compatibility/326b-firmware-building-locally.md
[LCM]: ../../unified-test-documentation/dasharo-compatibility/328-logo-customization-functionality.md
[CBO]: ../../unified-test-documentation/dasharo-compatibility/325-custom-boot-order.md
[QBS]: ../../unified-test-documentation/dasharo-compatibility/309-qubesos-support.md
[FED]: ../../unified-test-documentation/dasharo-compatibility/310-fedora-support.md
[DDP]: ../../unified-test-documentation/dasharo-compatibility/330-docking-station-display-ports.md
[DET]: ../../unified-test-documentation/dasharo-compatibility/340-docking-station-net-interface.md
[SUSP]: ../../unified-test-documentation/dasharo-compatibility/31M-platform-suspend-and-resume.md
[TDD]: ../../unified-test-documentation/dasharo-compatibility/352-thunderbolt-docking-station-detect.md
[TDU]: ../../unified-test-documentation/dasharo-compatibility/353-thunderbolt-docking-station-usb-devices.md
[TDA]: ../../unified-test-documentation/dasharo-compatibility/351-thunderbolt-docking-station-audio.md
[TDS]: ../../unified-test-documentation/dasharo-compatibility/350-thunderbolt-docking-station.md
[TDP]: ../../unified-test-documentation/dasharo-compatibility/354-thunderbolt-docking-station-display-ports.md
[TDN]: ../../unified-test-documentation/dasharo-compatibility/355-thunderbolt-docking-station-net-interface.md
[SOL]: ../../unified-test-documentation/dasharo-compatibility/347-sign-of-life.md
[MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
[NVI]: ../../unified-test-documentation/dasharo-compatibility/319-nvidia-graphics.md
[DSD]: ../../unified-test-documentation/dasharo-compatibility/356-docking-station-sd-card-reader.md
[BMF]: ../../unified-test-documentation/dasharo-compatibility/357-bios-menu-function-keys.md
[SMS]: ../../unified-test-documentation/dasharo-compatibility/358-suspend-mechanism-switching-S0ix-S3.md

### Module: Dasharo security

| No.  | Supported test suite                       | Test suite ID | Supported test cases                 |
|:-----|:-------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                         | TPM           | Without TPM001.001 and TPM002.001    |
| 2.   | [Verified Boot support][VBO]               | VBO           | Without VBO006.001 and VBO007.001    |
| 3.   | [Measured Boot support][MBO]               | MBO           | All                                  |
| 4.   | [Secure Boot support][SBO]                 | SBO           | Without SBO006.001, SBO007.001 and SBO008.001 |
| 5.   | [ME disable/neuter support][MNE]           | MNE           | Without MNE006.001                   |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
[MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
[MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md

### Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [coreboot boot measure][CBMEM]                    | CBMEM         | All                                  |
| 2.   | [CPU temperature measure][CPT]                    | CPT           | All                                  |
| 3.   | [CPU frequency measure][CPF]                      | CPF           | All                                  |
| 4.   | [Custom fan curve][CFC]                           | CFC           | All                                  |
| 5.   | [Platform stability][STB]                         | STB           | All                                  |

[CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
[CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
[CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
[CFC]: ../../unified-test-documentation/dasharo-performance/406-custom-fan-curve.md
[STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md

## Module: Dasharo stability

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [M.2 Wi-fi][SMW]                                  | SMW           | All                                  |

[SMW]: ../../unified-test-documentation/dasharo-stability/C02-m2-wi-fi.md

## NV41MZ test matrix

### Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
| 2.   | [UEFI compatible interface][EFI]                  | EFI           | All                                  |
| 3.   | [Display ports and LCD support][DSP]              | DSP           | DSP001.001, DSP001.002, DSP001.003, DSP002.001, DSP002.002 |
| 4.   | [Embedded Controller and Super I/O initialization][ECR] | ECR     | Without ECR021.xxx - ECR024.xxx, ECR25.001, ECR26.001, ECR27.001, ECR28.001 |
| 5.   | [NVMe support][NVM]                               | NVM           | All                                  |
| 6.   | [Custom logo][CLG]                                | CLG           | All                                  |
| 7.   | [Custom boot menu key][CBK]                       | CBK           | All                                  |
| 8.   | [USB HID and MSC Support][HID]                    | USB           | All                                  |
| 9.   | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT004.001, LBT004.002               |
| 10.  | [UEFI Shell][USH]                                 | USH           | All                                  |
| 11.  | [Windows booting][WBT]                            | WBT           | WBT001.001                           |
| 12.  | [Audio subsystem][AUD]                            | AUD           | All                                  |
| 13.  | [USB-C/Thunderbolt][UTC]                          | UTC           | All                                  |
| 14.  | [Network boot][PXE]                               | PXE           | Without PXE007.001                   |
| 15.  | [M.2 WiFi/Bluetooth][WLE]                         | WLE           | All                                  |
| 16.  | [SD card support][SDC]                            | SDC           | All                                  |
| 17.  | [USB Camera verification][CAM]                    | CAM           | All                                  |
| 18.  | [Fan speed measure][FAN]                          | FAN           | FAN001.001                           |
| 19.  | [SMBIOS][DMI]                                     | DMI           | Without DMI001.001                   |
| 20.  | [USB-C docking station detect][DUD]               | DUD           | All                                  |
| 21.  | [USB-C docking station USB devices][DUB]          | DUB           | All                                  |
| 22.  | [USB-C docking station Audio][DAU]                | DAU           | All                                  |
| 23.  | [USB-C docking station Display ports][DDP]        | DDP           | All                                  |
| 24.  | [USB-C docking station NET interface][DET]        | DET           | All                                  |
| 25.  | [Firmware update using fwupd][FFW]                | FFW           | All                                  |
| 26.  | [Dasharo Tools Suite][DTS]                        | DTS           | DTS006.001, DTS007.001               |
| 27.  | [CPU status][CPU]                                 | CPU           | All                                  |
| 28.  | [Embedded controller flashing][ECF]               | ECF           | All                                  |
| 29.  | [Logo customization functionality][LCM]           | LCM           | LCM001.001                           |
| 30.  | [Firmware locally building and flashing][FLB]     | FLB           | All                                  |
| 31.  | [Custom Boot Order][CBO]                          | CBO           | CBO001.002                           |
| 32.  | [QubesOS support][QBS]                            | QBS           | All                                  |
| 33.  | [Fedora support][FED]                             | FED           | All                                  |
| 34.  | [Platform suspend and resume][SUSP]               | SUSP          | SUSP001.001, SUSP002.001, SUSP003.001 |
| 35.  | [Thunderbolt docking station detect][TDD]         | TDD           | All                                  |
| 36.  | [Thunderbolt docking station USB devices][TDU]    | TDU           | All                                  |
| 37.  | [Thunderbolt docking station Audio][TDA]          | TDA           | All                                  |
| 38.  | [Thunderbolt docking station][TDS]                | TDS           | All                                  |
| 39.  | [Thunderbolt docking station Display ports][TDP]  | TDP           | All                                  |
| 40.  | [Thunderbolt docking station NET interface][TDN]  | TDN           | All                                  |
| 41.  | [Sign of life][SOL]                               | SOL           | All                                  |
| 42.  | [USB-C docking station SD card reader][DSD]       | DSD           | All                                  |
| 43.  | [BIOS menu function keys][BMF]                    | BMF           | All                                  |

### Module: Dasharo security

| No.  | Supported test suite                       | Test suite ID | Supported test cases                 |
|:-----|:-------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                         | TPM           | Without TPM001.001 and TPM002.001    |
| 2.   | [Verified Boot support][VBO]               | VBO           | Without VBO006.001 and VBO007.001    |
| 3.   | [Measured Boot support][MBO]               | MBO           | All                                  |
| 4.   | [Secure Boot support][SBO]                 | SBO           | Without SBO006.001, SBO007.001 and SBO008.001 |
| 5.   | [ME disable/neuter support][MNE]           | MNE           | Without MNE006.001                   |

### Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [coreboot boot measure][CBMEM]                    | CBMEM         | All                                  |
| 2.   | [CPU temperature measure][CPT]                    | CPT           | All                                  |
| 3.   | [CPU frequency measure][CPF]                      | CPF           | All                                  |
| 4.   | [Custom fan curve][CFC]                           | CFC           | All                                  |
| 5.   | [Platform stability][STB]                         | STB           | All                                  |

## Module: Dasharo stability

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [M.2 Wi-fi][SMW]                                  | SMW           | All                                  |
