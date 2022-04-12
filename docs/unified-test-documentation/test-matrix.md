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
| 11.  | Display ports and LCD support                     | DSP           | DSP004.001, DSP004.003               |

### Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | TPM Support                                       | TPM           | TPM001.001                           |
| 2.   | Verified Boot support                             | VBO           | VBO001.001, VBO002.001, VBO003.001   |

### Module: Dasharo performance

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | coreboot bring up time measurement                | CBMEM         | All                                  |

## Test matrix - Clevo NV41MZ

### Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | Memory HCL                                        | HCL           | All                                  |
| 2.   | UEFI compatible interface                         | EFI           | All                                  |
| 3.   | Display ports and LCD support                     | DSP           | DSP001.001, DSP001.002, DSP001.003,  |
|      |                                                   |               | DSP002.001, DSP002.002, DSP002.003   |
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
| 3.   | Display ports and LCD support                     | DSP           | DSP001.001, DSP001.002, DSP001.003,  |
|      |                                                   |               | DSP002.001, DSP002.002, DSP002.003   |
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

## Test matrix - Clevo NS50

### Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:----:|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | Memory HCL                                        | HCL           | All                                  |
| 2.   | UEFI compatible interface                         | EFI           | All                                  |
| 3.   | Display ports and LCD support                     | DSP           | DSP001.001, DSP001.002, DSP001.003,  |
|      |                                                   |               | DSP002.001, DSP002.002, DSP002.003   |
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

## Test matrix - Protectli VP4620

### Module: Dasharo compatibility

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:----:|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | Memory HCL                                        | HCL           | All                                  |
| 2.   | UEFI compatible interface                         | EFI           | EFI001.001                           |
| 3.   | Display ports                                     | DSP           | DSP002.001, DSP002.003, DSP003.001,  |
|      |                                                   |               | DSP003.003                           |
| 4.   | Network boot                                      | PXE           | All                                  |
| 5.   | NVMe support                                      | NVM           | NVM001.001, NVM001.002               |
| 7.   | Custom logo                                       | CLG           | All                                  |
| 8.   | Custom boot menu key                              | CBK           | All                                  |
| 9.   | USB HID and MSC Support                           | USB           | USB001.001, USB001.002, USB002.001, USB002.002 |
| 10.  | FreeBSD support                                   | BSD           | All                                  |
| 11.  | Debian Stable and Ubuntu LTS support              | LBT           | All                                  |
| 12.  | USB-C/Thunderbolt                                 | UTC           | UTC004.001                           |
| 13.  | M.2 WiFi/Bluetooth                                | WLE           | WLE001.001, WLE002.001, WLE003.001   |
| 14.  | miniPCIe LTE/WiFi/Bluetooth                       | MWL           | MWL004.001                           |
| 15.  | eMMC support                                      | MMC           | MMC001.001                           |
| 16.  | SMBIOS                                            | DMI           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, DMI006.001 |
| 17.  | Custom network boot entries                       | CNB           | CNB001.002                           |
| 18.  | M.2 automatic SATA/NVMe switching support         | MSS           | MSS001.001                           |

### Module: Dasharo security

| No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
|:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
| 1.   | TPM Support                                       | TPM           | TPM001.001                           |
