# Test matrix - MSI-Z960

## About

<!--
The test matrix is used to determine which of the test suites and test cases
described in this documentation are dedicated to the given platform
-->

## Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | SMBIOS                                            | DMI           | All                                  |
| 2.   | Memory HCL                                        | HCL           | All                                  |
| 3.   | UEFI compatible interface                         | EFI           | All                                  |
| 4.   | UEFI Shell                                        | USH           | All                                  |
| 5.   | Display ports and LCD support                     | DSP           | All                                  |
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
| 2.   | Verified Boot support                             | VBO           | All                                  |
| 3.   | Measured Boot support                             | MBO           | All                                  |
| 4.   | Secure Boot support                               | SBO           | All                                  |

### Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | coreboot bring up time measurement                | CBMEM         | All                                  |
