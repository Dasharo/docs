# Test matrix

## About

The test matrix is used to determine the scope of tests to which the DUT is
subjected before the release of the new binary.

## Module: Dasharo compatibility

| No.  | Supported test suite                                   | Test suite ID | Supported test cases                 |
|:----:|:-------------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                      | HCL           | All                                  |
| 2.   | [UEFI compatible interface][EFI]                       | EFI           | All                                  |
| 3.   | [Display ports and LCD support][DSP]                   | DSP           | DSP001.001, DSP001.201, DSP001.301, DSP002.201, DSP002.301 |
| 4.   | [Embedded Controller and Super I/O initialization][ECR]| ECR           | All                                  |
| 5.   | [NVMe support][NVM]                                    | NVM           | All                                  |
| 6.   | [Custom logo][CLG]                                     | CLG           | All                                  |
| 7.   | [Custom boot keys][CBK]                                | CBK           | All                                  |
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
| 19.  | [SMBIOS][DMI]                                          | DMI           | Without DMI001.201                   |
| 20.  | [Firmware update using fwupd][FFW]                     | FFW           | All                                  |
| 21.  | [Dasharo Tools Suite][DTS]                             | DTS           | DTS006.001, DTS007.001               |
| 22.  | [CPU status][CPU]                                      | CPU           | All                                  |
| 23.  | [Embedded controller flashing][ECF]                    | ECF           | All                                  |
| 24.  | [Logo customization functionality][LCM]                | LCM           | LCM001.001                           |
| 25.  | [Firmware locally building and flashing][FLB]          | FLB           | All                                  |
| 26.  | [Custom Boot Order][CBO]                               | CBO           | CBO001.002                           |
| 27.  | [QubesOS support][QBS]                                 | QBS           | All                                  |
| 28.  | [Fedora support][FED]                                  | FED           | All                                  |
| 29.  | [Platform suspend and resume][SUSP]                    | SUSP          | Without SUSP004 and SUSP006          |
| 30.  | [Boot blocking][BBB]                                   | BBB           | All                                  |
| 31.  | [Reset to defaults][RTD]                               | RTD           | All                                  |
| 32.  | [Suspend mechanism switching (S0ix/S3)][SMS]           | SMS           | All                                  |
| 33.  | [Platform hibernation and resume][HBN]                 | HBN           | All                                  |
| 34.  | [Sign of life][SOL]                                    | SOL           | All                                  |
| 35.  | [Power after fail][PSF]                                | PSF           | All                                  |

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
[BBB]: ../../unified-test-documentation/dasharo-compatibility/359-boot-blocking.md
[SMS]: ../../unified-test-documentation/dasharo-compatibility/358-suspend-mechanism-switching-S0ix-S3.md
[SOL]: ../../unified-test-documentation/dasharo-compatibility/347-sign-of-life.md

## Module: Dasharo security

| No.  | Supported test suite                         | Test suite ID | Supported test cases                 |
|:-----|:---------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                           | TPM           | Without TPM001.001 and TPM002.001    |
| 2.   | [Verified Boot support][VBO]                 | VBO           | Without VBO006.001 and VBO007.001    |
| 3.   | [Measured Boot support][MBO]                 | MBO           | All                                  |
| 4.   | [Secure Boot support][SBO]                   | SBO           | Without SBO006.001, SBO007.001 and SBO008.001 |
| 5.   | [ME disable/neuter support][MNE]             | MNE           | Without MNE005.201                   |
| 6.   | [USB stack][USS]                             | USS           | All                                  |
| 7.   | [Network boot availability][PXE]             | PXE           | All                                  |
| 8.   | [BIOS lock support][BLS]                     | BLS           | All                                  |
| 9.   | [Early boot DMA protection][EDP]             | EDP           | All                                  |
| 10.  | [SMM BIOS write protection][SMM]             | SMM           | All                                  |
| 11.  | [UEFI Setup password][PSW]                   | PSW           | All                                  |
| 12.  | [Wi-Fi / Bluetooth switch][WBS]              | WBS           | All                                  |
| 13.  | [Camera switch][CHS]                         | CHS           | All                                  |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
[MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
[BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md
[MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
[USS]: ../../unified-test-documentation/dasharo-security/20S-usb-stack.md
[PXE]: ../../unified-test-documentation/dasharo-security/20T-network-boot.md
[BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md
[EDP]: ../../unified-test-documentation/dasharo-security/20L-early-boot-dma-protection.md
[SMM]: ../../unified-test-documentation/dasharo-security/20O-SMM-bios-write-protection.md
[PSW]: ../../unified-test-documentation/dasharo-security/20R-uefi-setup-password.md

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
| 4.   | [NET interface detection][NET]                    | NET           | All                                  |
| 5.   | [TPM detection][TPD]                              | TPD           | TPD003.201, TPD003.202, TPD004.201, TPD004.202 |

[SUD]: ../../unified-test-documentation/dasharo-stability/C01-usb-type-a-devices-detection.md
[SMW]: ../../unified-test-documentation/dasharo-stability/C02-m2-wi-fi.md
[SNV]: ../../unified-test-documentation/dasharo-stability/C03-nvme-detection.md
[NET]: ../../unified-test-documentation/dasharo-stability/01-net-controller-after-coldboot-warmboot-reboot-suspend.md
