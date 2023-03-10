# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
| 2.   | [Display ports and LCD support][DSP]              | DSP           | DSP002.001, DSP002.003               |
| 3.   | [USB HID and MSC Support][USB]                    | USB           | USB001.001, USB001.002, USB002.001, USB002.002 |
| 4.   | [SMBIOS][DMI]                                     | DMI           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, DMI006.001 |
| 5.   | [Custom boot logo][CLG]                           | CLG           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, DMI006.001 |
| 6.   | [M.2 WiFi/Bluetooth][WLE]                         | WLE           | WLE001.001, WLE002.001, WLE003.001   |
| 7.   | [Network boot][PXE]                               | PXE           | PXE007.001                           |
| 8.   | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
| 9.   | [Custom boot menu key][CBK]                       | CBK           | All                                  |
| 10.  | [FreeBSD support][BSD]                            | BSD           | All                                  |
| 11.  | [miniPCIe LTE/WiFi/Bluetooth][MWL]                | MWL           | MWL004.001                           |
| 12.  | [Custom network boot entries][CNB]                | CNB           | CNB001.002                           |

[HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
[DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[MWL]: ../../unified-test-documentation/dasharo-compatibility/31K-minipcie-verification.md
[WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
[PXE]: ../../unified-test-documentation/dasharo-compatibility/315-network-boot.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[BSD]: ../../unified-test-documentation/dasharo-compatibility/307-freebsd-support.md
[CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md

## Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [CPU temperature][CPT]                            | CPT           | All                                  |

[CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
