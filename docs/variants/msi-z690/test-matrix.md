# Test matrix - MSI-Z960

## About

<!--
The test matrix is used to determine which of the test suites and test cases
described in this documentation are dedicated to the given platform
-->

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | [UEFI compatible interface][EFI]                  | EFI           | EFI001.001                           |
| 2.   | [UEFI Shell][USH]                                 | USH           | All                                  |
| 3.   | [Display ports and LCD support][DSP]              | DSP           | DSP002.001, DSP002.003, DSP003.001, DSP003.003 |
| 4.   | [USB HID and MSC Support][USB]                    | USB           | USB001.001, USB001.002, USB002.001, USB002.002 |

[EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
[USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md

<!--
## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | SMBIOS                                            | DMI           | DMI002.001, DMI003.001, DMI004.001, DMI006.001, DMI007.001, DMI008.001|
| 2.   | Memory HCL                                        | HCL           | All                                  |
| 3.   | UEFI compatible interface                         | EFI           | All                                  |
| 4.   | UEFI Shell                                        | USH           | All                                  |
| 5.   | Display ports and LCD support                     | DSP           | DSP002.001, DSP002.002 DSP002.003, DSP003.001, DSP003.002 DSP003.003 |
| 6.   | USB HID and MSC Support                           | USB           | All                                  |
| 7.   | miniPCIe slot verification                        | MWL           | All                                  |
| 8.   | M.2 WiFi/Bluetooth                                | WLE           | All                                  |
| 9.   | Audio subsystem                                   | AUD           | All                                  |
| 10.  | NVMe support                                      | NVM           | All                                  |
| 11.  | Network boot                                      | PXE           | All                                  |
| 12.  | Debian Stable and Ubuntu LTS support              | LBT           | All                                  |
| 13.  | SD card support                                   | SDC           | All                                  |
| 14.  | Windows 11 booting                                | WBT           | All                                  |
| 15.  | Custom logo                                       | CLG           | All                                  |
| 16.  | Custom boot menu key                              | CBK           | All                                  |

## Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | TPM Support                                       | TPM           | All                                  |
| 2.   | Verified Boot support                             | VBO           | VBO001.002, VBO002.002, VBO003.001   |
| 3.   | Measured Boot support                             | MBO           | All                                  |
| 4.   | Secure Boot support                               | SBO           | All                                  |

### Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | coreboot bring up time measurement                | CBMEM         | All                                  |
-->
