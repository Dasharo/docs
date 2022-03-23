# Test matrix

## About

<!--
The test matrix is used to determine which of the test suites and test cases
described in this documentation are dedicated to the given platform
-->

## Test matrix - ASUS KGPE-D16

### Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | coreboot base port                                | CBP           | All                                  |
| 2.   | SMBIOS                                            | DMI           | DMI002.001, DMI003.001               |
| 3.   | coreboot fan control                              | CFN           | All                                  |
| 4.   | Custom boot menu key                              | CBK           | All                                  |
| 5.   | Debian Stable and Ubuntu LTS support              | LBT           | LBT001.002                           |
| 6.   | Network boot                                      | PXE           | All                                  |
| 7.   | USB detect                                        | USB           | All                                  |
| 8.   | USB boot                                          | UBB           | All                                  |
| 9.   | Platform suspend and resume                       | SUSP          | All                                  |
| 10.  | Flash write protection                            | FWP           | All                                  |

### Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | TPM Support                                       | TPM           | TPM001.001                           |
| 2.   | Verified Boot support                             | VBO           | VBO001.001, VBO002.001, VBO003.001   |

### Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | coreboot boot measure                             | CBMEM         | All                                  |

## Test matrix - Clevo NV41MZ

### Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | Memory HCL                                        | HCL           | All                                  |
| 2.   | UEFI compatible interface                         | EFI           | All                                  |
| 3.   | Display ports and LCD support                     | DSP           | All                                  |
| 4.   | Embedded Controller and Super I/O initialization  | ECR           | All                                  |
| 5.   | NVMe support                                      | NVM           | All                                  |
| 6.   | Custom logo                                       | CLG           | All                                  |
| 7.   | Custom boot menu key                              | CBK           | All                                  |
| 8.   | USB HID and MSC Support                           | USB           | All                                  |
| 9.   | Debian Stable and Ubuntu LTS support              | LBT           | All                                  |
| 10.  | UEFI Shell                                        | USH           | All                                  |
| 11.  | Windows 11 booting                                | WBT           | All                                  |
| 12.  | Audio subsystem                                   | AUD           | All                                  |
| 13.  | USB-C/Thunderbolt                                 | UTC           | All                                  |
| 14.  | Network boot                                      | PXE           | All                                  |
| 15.  | M.2 WiFi/Bluetooth                                | WLE           | All                                  |
| 16.  | SD card support                                   | SDC           | All                                  |
| 17.  | USB Camera verification                           | CAM           | All                                  |
| 18.  | Nvidia Graphics support                           | NVI           | All                                  |
| 19.  | Custom fan curve                                  | FAN           | All                                  |
| 20.  | SMBIOS                                            | DMI           | DMI002.001, DMI003.001, DMI005.001,  |
|      |                                                   |               | DMI006.001, DMI007.001, DMI008.001   |

### Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | TPM Support                                       | TPM           | All                                  |
| 2.   | Verified Boot support                             | VBO           | VBO001.002, VBO002.002, VBO003.001   |
| 3.   | Measured Boot support                             | MBO           | All                                  |
| 4.   | Secure Boot support                               | SBO           | All                                  |

## Test matrix - Clevo NV41MB

### Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | Memory HCL                                        | HCL           | All                                  |
| 2.   | UEFI compatible interface                         | EFI           | All                                  |
| 3.   | Display ports and LCD support                     | DSP           | All                                  |
| 4.   | Embedded Controller and Super I/O initialization  | ECR           | Whithout ECR010.001 and ECR010.002   |
| 5.   | NVMe support                                      | NVM           | All                                  |
| 6.   | Custom logo                                       | CLG           | All                                  |
| 7.   | Custom boot menu key                              | CBK           | All                                  |
| 8.   | USB HID and MSC Support                           | USB           | All                                  |
| 9.   | Debian Stable and Ubuntu LTS support              | LBT           | All                                  |
| 10.  | UEFI Shell                                        | USH           | All                                  |
| 11.  | Windows 11 booting                                | WBT           | All                                  |
| 12.  | Audio subsystem                                   | AUD           | All                                  |
| 13.  | USB-C/Thunderbolt                                 | UTC           | All                                  |
| 14.  | Network boot                                      | PXE           | All                                  |
| 15.  | M.2 WiFi/Bluetooth                                | WLE           | All                                  |
| 16.  | SD card support                                   | SDC           | All                                  |
| 17.  | USB Camera verification                           | CAM           | All                                  |
| 18.  | Custom fan curve                                  | FAN           | FAN001.001                           |
| 19.  | SMBIOS                                            | DMI           | DMI002.001, DMI003.001, DMI005.001,  |
|      |                                                   |               | DMI006.001, DMI007.001, DMI008.001   |

### Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | TPM Support                                       | TPM           | All                                  |
| 2.   | Verified Boot support                             | VBO           | VBO001.002, VBO002.002, VBO003.001   |
| 3.   | Measured Boot support                             | MBO           | All                                  |
| 4.   | Secure Boot support                               | SBO           | All                                  |

## Test matrix - Talos II

### Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | coreboot base port                                | CBP           | CBP001.001, CBP002.001, CBP004.001   |

## Test matrix - Clevo NS50

### Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:----:|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | Memory HCL                                        | HCL           | All                                  |
| 2.   | UEFI compatible interface                         | EFI           | All                                  |
| 3.   | Display ports and LCD support                     | DSP           | All                                  |
| 4.   | Embedded Controller and Super I/O initialization  | ECR           | Whithout ECR010.001 and ECR010.002   |
| 5.   | NVMe support                                      | NVM           | All                                  |
| 6.   | Custom logo                                       | CLG           | All                                  |
| 7.   | Custom boot menu key                              | CBK           | All                                  |
| 8.   | USB HID and MSC Support                           | USB           | All                                  |
| 9.   | Debian Stable and Ubuntu LTS support              | LBT           | All                                  |
| 10.  | Windows 11 booting                                | WBT           | All                                  |
| 11.  | Audio subsystem                                   | AUD           | All                                  |
| 12.  | USB-C/Thunderbolt                                 | UTC           | All                                  |
| 13.  | M.2 WiFi/Bluetooth                                | WLE           | All                                  |
| 14.  | SD card support                                   | SDC           | All                                  |
| 15.  | USB Camera verification                           | CAM           | All                                  |
| 16.  | Custom fan curve                                  | FAN           | FAN001.001                           |
| 17.  | SMBIOS                                            | DMI           | DMI002.001, DMI003.001, DMI005.001,  |
|      |                                                   |               | DMI006.001, DMI007.001, DMI008.001   |

### Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | TPM Support                                       | TPM           | All                                  |
| 2.   | Verified Boot support                             | VBO           | VBO001.002, VBO002.002               |
| 3.   | Measured Boot support                             | MBO           | All                                  |
| 4.   | Secure Boot support                               | SBO           | All                                  |
