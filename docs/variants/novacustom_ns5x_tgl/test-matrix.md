# Test matrix

## About

The test matrix is used to determine the scope of tests to which the DUT is
subjected before the release of the new binary.

## Module: Dasharo compatibility

| No.  | Supported test suite                                   | Test suite ID | Supported test cases                 |
|:----:|:-------------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                      | HCL           | All                                  |
| 2.   | [UEFI compatible interface][EFI]                       | EFI           | All                                  |
| 3.   | [Display ports and LCD support][DSP]                   | DSP           | DSP001.001, DSP001.002, DSP001.003, DSP002.001, DSP002.002 |
| 4.   | [Embedded Controller and Super I/O initialization][ECR]| ECR           | Without ECR010.001, ECR010.002, ECR25.001, ECR26.001, ECR27.001, ECR28.001 |
| 5.   | [NVMe support][NVM]                                    | NVM           | All                                  |
| 6.   | [Custom logo][CLG]                                     | CLG           | All                                  |
| 7.   | [Custom boot menu key][CBK]                            | CBK           | All                                  |
| 8.   | [USB HID and MSC Support][USB]                         | USB           | All                                  |
| 9.   | [Debian Stable and Ubuntu LTS support][LBT]            | LBT           | LBT004.001, LBT004.002               |
| 10.  | [UEFI Shell][USH]                                      | USH           | All                                  |
| 11.  | [Windows booting][WBT]                                 | WBT           | WBT001.001                           |
| 12.  | [Audio subsystem][AUD]                                 | AUD           | All                                  |
| 13.  | [USB-C support][UTC]                                   | UTC           | All                                  |
| 14.  | [Network boot][PXE]                                    | PXE           | Without PXE007.001                   |
| 15.  | [M.2 WiFi/Bluetooth][WLE]                              | WLE           | All                                  |
| 16.  | [SD card support][SDC]                                 | SDC           | All                                  |
| 17.  | [USB Camera verification][CAM]                         | CAM           | All                                  |
| 18.  | [Fan speed measure][FAN]                               | FAN           | FAN001.001                           |
| 19.  | [SMBIOS][DMI]                                          | DMI           | Without DMI001.001                   |
| 20.  | [Firmware update using fwupd][FFW]                     | FFW           | All                                  |
| 21.  | [Dasharo Tools Suite][DTS]                             | DTS           | DTS006.001, DTS007.001               |
| 22.  | [CPU status][CPU]                                      | CPU           | All                                  |
| 23.  | [Embedded controller flashing][ECF]                    | ECF           | All                                  |
| 24.  | [Logo customization functionality][LCM]                | LCM           | LCM001.001                           |
| 25.  | [Firmware locally building and flashing][FLB]          | FLB           | All                                  |
| 26.  | [Custom Boot Order][CBO]                               | CBO           | CBO001.002                           |
| 27.  | [QubesOS support][QBS]                                 | QBS           | All                                  |
| 28.  | [Fedora support][FED]                                  | FED           | All                                  |
| 29.  | [Platform suspend and resume][SUSP]                    | SUSP          | SUSP001.001, SUSP002.001, SUSP003.001 |
| 30.  | [Sign of life][SOL]                                    | SOL           | All                                  |
| 31.  | [BIOS menu function keys][BMF]                         | BMF           | All                                  |

[HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
[EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[ECR]: ../../unified-test-documentation/dasharo-compatibility/31G-ec-and-superio.md
[NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
[WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
[AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
[UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
[WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
[SDC]: ../../unified-test-documentation/dasharo-compatibility/316-sdcard-reader.md
[CAM]: ../../unified-test-documentation/dasharo-compatibility/317-usb-camera.md
[FAN]: ../../unified-test-documentation/dasharo-compatibility/S30-fan-speed.md
[DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
[FFW]: ../../unified-test-documentation/dasharo-compatibility/320-fwupd-firmware-update.md
[DTS]: ../../unified-test-documentation/dasharo-compatibility/326-dasharo-tools-suite.md
[ECF]: ../../unified-test-documentation/dasharo-compatibility/327-embedded_controller_flashing.md
[PXE]: ../../unified-test-documentation/dasharo-compatibility/315-network-boot.md
[CPU]: ../../unified-test-documentation/dasharo-compatibility/31T-cpu-status.md
[FLB]: ../../unified-test-documentation/dasharo-compatibility/326b-firmware-building-locally.md
[LCM]: ../../unified-test-documentation/dasharo-compatibility/328-logo-customization-functionality.md
[CBO]: ../../unified-test-documentation/dasharo-compatibility/325-custom-boot-order.md
[QBS]: ../../unified-test-documentation/dasharo-compatibility/309-qubesos-support.md
[FED]: ../../unified-test-documentation/dasharo-compatibility/310-fedora-support.md
[SUSP]: ../../unified-test-documentation/dasharo-compatibility/31M-platform-suspend-and-resume.md
[SOL]: ../../unified-test-documentation/dasharo-compatibility/347-sign-of-life.md
[MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
[BMF]: ../../unified-test-documentation/dasharo-compatibility/357-bios-menu-function-keys.md
[SMS]: ../../unified-test-documentation/dasharo-compatibility/358-suspend-mechanism-switching-S0ix-S3.md

## Module: Dasharo security

| No.  | Supported test suite                         | Test suite ID | Supported test cases                 |
|:-----|:---------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                           | TPM           | Without TPM001.001 and TPM002.001    |
| 2.   | [Verified Boot support][VBO]                 | VBO           | Without VBO006.001 and VBO007.001    |
| 3.   | [Measured Boot support][MBO]                 | MBO           | All                                  |
| 4.   | [Secure Boot support][SBO]                   | SBO           | Without SBO006.001, SBO007.001 and SBO008.001 |
| 5.   | [ME disable/neuter support][MNE]             | MNE           | Without MNE006.001                   |
| 6.   | [Network Stack][NBA]                         | NBA           | All                                  |
| 7.   | [Early Boot Dma Protection][EDP]             | EDP           | All                                  |
| 8.   | [BIOS Lock][BLS]                             | BLS           | All                                  |
| 9.   | [SMM BIOS write protection][SMM]             | SMM           | All                                  |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
[MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
[MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
[NBA]: ../../unified-test-documentation/dasharo-security/20T-network-boot.md
[EDP]: ../../unified-test-documentation/dasharo-security/20L-early-boot-dma-protection.md
[BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md
[SMM]: ../../unified-test-documentation/dasharo-security/20O-SMM-bios-write-protection.md

## Module: Dasharo performance

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
| 1.   | [USB Type-A devices detection][SUD]               | SUD           | All                                  |
| 2.   | [M.2 Wi-fi][SMW]                                  | SMW           | All                                  |
| 3.   | [NVMe detection][SNV]                             | SNV           | All                                  |
| 4.   | [NET interface after coldboot/warmboot/reboot/suspend][NET] | NET | All                                  |

[SUD]: ../../unified-test-documentation/dasharo-stability/C01-usb-type-a-devices-detection.md
[SMW]: ../../unified-test-documentation/dasharo-stability/C02-m2-wi-fi.md
[SNV]: ../../unified-test-documentation/dasharo-stability/C03-nvme-detection.md
[NET]: ../../unified-test-documentation/dasharo-stability/01-net-controller-after-coldboot-warmboot-reboot-suspend.md
