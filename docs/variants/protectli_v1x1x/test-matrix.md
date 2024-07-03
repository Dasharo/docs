# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary. The test scope is the same
for all platforms of the V1210/V1410/V1610 family.

## Module: Dasharo compatibility

| No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
|:----:|:--------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [UEFI compatible interface][EFI]      | EFI           | All                                  |
| 2.   | [Display ports][DSP]                  | DSP           | DSP002.001, DSP002.002, DSP002.003   |
| 3.   | [Network boot utilities][NBT]         | NBT           | All                                  |
| 4.   | [NVMe support][NVM]                   | NVM           | All                                  |
| 5.   | [Custom logo][CLG]                    | CLG           | All                                  |
| 6.   | [Custom Boot Keys][CBK]               | CBK           | All                                  |
| 7.   | [USB HID and MSC Support][USB]        | USB           | USB001.xxx and USB002.xxx            |
| 8.   | [Debian Stable and Ubuntu LTS support][LBT]  | LBT    | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
| 9.   | [miniPCIe LTE/WiFi/Bluetooth][MWL]    | MWL           | MWL004.001                           |
| 10.  | [M.2 WiFi/Bluetooth][WLE]             | WLE           | All                                  |
| 11.  | [eMMC support][MMC]                   | MMC           | All                                  |
| 12.  | [SMBIOS][DMI]                         | DMI           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, DMI006.001 |
| 13.  | [Custom network boot entries][CNB]    | CNB           | CNB001.002                           |
| 14.  | [Audio subsystem][AUD]                | AUD           | AUD007.xxx, AUD008.xxx               |
| 15.  | [UEFI Shell][USH]                     | USH           | All                                  |
| 16.  | [USB detection][UDT]                  | UDT           | All                                  |
| 17.  | [USB booting][UBT]                    | UBT           | All                                  |
| 18.  | [Windows booting][WBT]                | WBT           | WBT001.001                           |

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
[PFS]: ../../unified-test-documentation/dasharo-compatibility/341-pfSense-support.md
[OPN]: ../../unified-test-documentation/dasharo-compatibility/342-OPNsense-support.md
[PVE]: ../../unified-test-documentation/dasharo-compatibility/348-proxmox-support.md
[USS]: ../../unified-test-documentation/dasharo-compatibility/349-ubuntu-server-support.md

## Module: Dasharo security

| No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                    | TPM           | TPM001.002, TPM001.003, TPM002.002, TPM002.003, TPM003.002, TPM003.003 |
| 2.   | [Secure Boot support][SBO]            | SBO           | All                                  |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md

## Module: Dasharo performance

| No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [coreboot bring up time measurement][CBMEM] | CBMEM         | All                            |
| 2.   | [CPU temperature measure][CPT]        | CPT           | All                                  |
| 3.   | [CPU frequency measure][CPF]          | CPF           | Without CPU003.XXX and CPU005.XXX    |
| 4.   | [Platform stability][STB]             | STB           | All                                  |

[CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
[CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
[CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
[STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md
[BUB]: ../../unified-test-documentation/dasharo-performance/407-ubuntu-booting-performance-test.md
[BDE]: ../../unified-test-documentation/dasharo-performance/408-debian-booting-performance-test.md
[BFB]: ../../unified-test-documentation/dasharo-performance/409-freebsd-booting-performance-test.md
[BPM]: ../../unified-test-documentation/dasharo-performance/410-proxmox-booting-performance-test.md
[BUS]: ../../unified-test-documentation/dasharo-performance/411-ubuntu-server-booting-performance-test.md
[BOS]: ../../unified-test-documentation/dasharo-performance/412-opnsense-serial-booting-performance-test.md
[BOV]: ../../unified-test-documentation/dasharo-performance/413-opnsense-vga-booting-performance-test.md
[BPS]: ../../unified-test-documentation/dasharo-performance/414-pfsense-serial-booting-performance-test.md
[BPV]: ../../unified-test-documentation/dasharo-performance/415-pfsense-vga-booting-performance-test.md
