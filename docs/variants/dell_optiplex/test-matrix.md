# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
| 2.   | [UEFI compatible interface][EFI]                  | EFI           | All                                  |
| 3.   | [UEFI Shell][USH]                                 | USH           | All                                  |
| 2.   | [Display ports and LCD support][DSP]              | DSP           | DSP003.201, DSP003.003, DSP004.201, DSP004.003 |
| 3.   | [USB HID and MSC Support][USB]                    | USB           | All                                  |
| 4.   | [SMBIOS][DMI]                                     | DMI           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, DMI006.001|
| 5.   | [Custom boot logo][CLG]                           | CLG           | All                                  |
| 6.   | [Audio subsystem][AUD]                            | AUD           | AUD001.201, AUD004.201, AUD005.201, AUD006.201 |
| 7.   | [NVMe support][NVM]&sup1;                         | NVM           | NVM001.001, NVM001.002               |
| 8.   | [Network boot][PXE]                               | PXE           | Without PXE007.001                   |
| 9.   | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
| 13.  | [Windows booting][WBT]                            | WBT           | WBT001.001                           |
| 10.  | [Custom boot menu key][CBK]                       | CBK           | All                                  |
| 15.  | [Dasharo Tools Suite][DTS]                        | DTS           | DTS001.001, DTS002.001, DTS003.001, DTS004.001, DTS005.001, DTS006.001 |
| 11.  | [PCI Express ports support][PEX]                  | PEX           | PEX001.001                           |
| 16.  | [CPU status][CPU]                                 | CPU           | CPU001.201, CPU001.301               |
| 17.  | [Platform suspend and resume][SUSP]               | SUSP          | All                                  |
| 12.  | [EC and Super I/O initialization][ECR]            | SIO           | SIO001.001, SIO002.001, SIO002.002, SIO003.001, SIO004.001, SIO004.002|
| 13.  | [Fan control][FAN]                                | FAN           | FAN001.002&sup2;                     |

1) Requires a PCIe x4 to M.2 adapter
2) Fans have to be checked manually. No support for reading the fan speed.
   There is also no W83795G HWM on this machine.

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
[PEX]: ../../unified-test-documentation/dasharo-compatibility/31R-pcie-ports.md
[ECR]: ../../unified-test-documentation/dasharo-compatibility/31G-ec-and-superio.md
[FAN]: ../../unified-test-documentation/dasharo-compatibility/S31-coreboot-fan-control.md

## Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [TPM Support][TPM]                                | TPM           | TPM001.002                           |
| 2.   | [Measured Boot support][MBO]                      | MBO           | All                                  |
| 4.   | [Secure Boot support][SBO]                        | SBO           | All                                  |
| 9.   | [UEFI Setup password][PSW]                        | PSW           | All                                  |
| 10.  | [Network stack enable/disable][NBA]               | NBA           | All                                  |
| 11.  | [USB stack enable/disable][USS]                   | USS           | All                                  |

[TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
[MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
[SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
[NBA]: ../../unified-test-documentation/dasharo-security/20T-network-boot.md
[USS]: ../../unified-test-documentation/dasharo-security/20S-usb-stack.md
[PSW]: ../../unified-test-documentation/dasharo-security/20R-uefi-setup-password.md

### Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [coreboot bring up time measurement][CBMEM]       | CBMEM         | All                                  |
| 2.   | [CPU temperature measure][CPT]        | CPT           | All                                  |
| 3.   | [CPU frequency measure][CPF]          | CPF           | Without CPU003.XXX and CPU005.XXX    |
| 4.   | [Platform stability][STB]             | STB           | All                                  |

[CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
[CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
[CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
[STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md
