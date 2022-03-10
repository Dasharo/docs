# Test matrix

## About

<!--
Matryca testowa służy do określenia które z zetsawów i przypadków testych
opisanych w dokumentacji testowej dedykowane są dla danej platformy
-->

## Test matrix - ASUS KGPE-D16

### Module: dasharo-compatibility

| No.  | Supported test suite                              | Supported test cases                 |
|:----:|:-------------------------------------------------:|:------------------------------------:|
| 1.   | coreboot base port                                | All                                  |
| 2.   | SMBIOS                                            | DMI002.001, DMI003.001               |
| 3.   | coreboot fan control                              | All                                  |
| 4.   | custom boot menu key                              | All                                  |
| 5.   | Debian Stable and Ubuntu LTS support              | LBT001.002                           |
| 6.   | Network boot                                      | All                                  |
| 7.   | USB detect                                        | All                                  |
| 8.   | USB boot                                          | All                                  |

### Module: dasharo-security

| No.  | Supported test suite                              | Supported test cases                 |
|:----:|:-------------------------------------------------:|:------------------------------------:|
| 1.   | TPM Support                                       | TPM001.001                           |
| 2.   | Verified Boot support                             | VBO001.001, VBO002.001, VBO003.001   |

## Test matrix - Novacustom Clevo NV41MZ

### Module: dasharo-compatibility

| No.  | Supported test suite                              | Supported test cases                 |
|:----:|:-------------------------------------------------:|:------------------------------------:|
| 1.   | Memory HCL                                        | All                                  |
| 2.   | UEFI compatible interface                         | All                                  |
| 3.   | Display ports and LCD support                     | All                                  |
| 4.   | Embedded Controller and Super I/O initialization  | All                                  |
| 5.   | NVMe support                                      | All                                  |
| 6.   | Custom logo                                       | All                                  |
| 7.   | custom boot menu key                              | All                                  |
| 8.   | UEFI Secure Boot                                  | All                                  |
| 9.   | USB HID and MSC Support                           | All                                  |
| 10.  | Debian Stable and Ubuntu LTS support              | All                                  |
| 11.  | UEFI Shell                                        | All                                  |
| 12.  | Windows 11 booting                                | All                                  |
| 13.  | Audio subsystem                                   | All                                  |
| 14.  | USB-C/Thunderbolt                                 | All                                  |
| 15.  | Network boot                                      | All                                  |
| 16.  | M.2 WiFi/Bluetooth                                | All                                  |
| 17.  | SD card support                                   | All                                  |
| 18.  | USB Camera verification                           | All                                  |
| 19.  | Nvidia Graphics support                           | All                                  |
| 20.  | Custom fan curve                                  | All                                  |
| 21.  | SMBIOS                                            | DMI002.001, DMI003.001, DMI005.001,  |
|      |                                                   | DMI006.001, DMI007.001, DMI008.001   |

### Module: dasharo-security

| No.  | Supported test suite                              | Supported test cases                 |
|:----:|:-------------------------------------------------:|:------------------------------------:|
| 1.   | TPM Support                                       | All                                  |
| 2.   | Verified Boot support                             | VBO001.002, VBO002.002, VBO003.001   |
| 3.   | Measured Boot support                             | All                                  |
| 4.   | Secure Boot support                               | All                                  |

## Test matrix - Novacustom Clevo NV41MB

### Module: dasharo-compatibility

| No.  | Supported test suite                              | Supported test cases                 |
|:----:|:-------------------------------------------------:|:------------------------------------:|
| 1.   | Memory HCL                                        | All                                  |
| 2.   | UEFI compatible interface                         | All                                  |
| 3.   | Display ports and LCD support                     | All                                  |
| 4.   | Embedded Controller and Super I/O initialization  | All                                  |
| 5.   | NVMe support                                      | All                                  |
| 6.   | Custom logo                                       | All                                  |
| 7.   | custom boot menu key                              | All                                  |
| 8.   | UEFI Secure Boot                                  | All                                  |
| 9.   | USB HID and MSC Support                           | All                                  |
| 10.  | Debian Stable and Ubuntu LTS support              | All                                  |
| 11.  | UEFI Shell                                        | All                                  |
| 12.  | Windows 11 booting                                | All                                  |
| 13.  | Audio subsystem                                   | All                                  |
| 14.  | USB-C/Thunderbolt                                 | All                                  |
| 15.  | Network boot                                      | All                                  |
| 16.  | M.2 WiFi/Bluetooth                                | All                                  |
| 17.  | SD card support                                   | All                                  |
| 18.  | USB Camera verification                           | All                                  |
| 19.  | Custom fan curve                                  | FAN001.001                           |
| 20.  | SMBIOS                                            | DMI002.001, DMI003.001, DMI005.001,  |
|      |                                                   | DMI006.001, DMI007.001, DMI008.001   |

### Module: dasharo-security

| No.  | Supported test suite                              | Supported test cases                 |
|:----:|:-------------------------------------------------:|:------------------------------------:|
| 1.   | TPM Support                                       | All                                  |
| 2.   | Verified Boot support                             | VBO001.002, VBO002.002, VBO003.001   |
| 3.   | Measured Boot support                             | All                                  |
| 4.   | Secure Boot support                               | All                                  |

## Test matrix - Talos 2

### Module: dasharo-compatibility

| No.  | Supported test suite                  | Supported test cases                           |
|:----:|:-------------------------------------:|:----------------------------------------------:|
| 1.   | coreboot base port                    | CBP001.001, CBP002.001, CBP004.001             |

## Test matrix - Tuxedo IBS15

### Module: dasharo-compatibility

| No.  | Supported test suite                              | Supported test cases                 |
|:----:|:-------------------------------------------------:|:------------------------------------:|
| 1.   | Memory HCL                                        | All                                  |
| 2.   | UEFI compatible interface                         | All                                  |
| 3.   | Display ports and LCD support                     | All                                  |
| 4.   | Embedded Controller and Super I/O initialization  | Whithout ECR010.001 and ECR010.002   |
| 5.   | NVMe support                                      | All                                  |
| 6.   | Custom logo                                       | All                                  |
| 7.   | custom boot menu key                              | All                                  |
| 8.   | UEFI Secure Boot                                  | All                                  |
| 9.   | USB HID and MSC Support                           | All                                  |
| 10.  | Debian Stable and Ubuntu LTS support              | All                                  |
| 12.  | Windows 11 booting                                | All                                  |
| 13.  | Audio subsystem                                   | All                                  |
| 14.  | USB-C/Thunderbolt                                 | All                                  |
| 16.  | M.2 WiFi/Bluetooth                                | All                                  |
| 17.  | SD card support                                   | All                                  |
| 18.  | USB Camera verification                           | All                                  |
| 19.  | Custom fan curve                                  | FAN001.001                           |
| 20.  | SMBIOS                                            | DMI002.001, DMI003.001, DMI005.001,  |
|      |                                                   | DMI006.001, DMI007.001, DMI008.001   |

### Module: dasharo-security

| No.  | Supported test suite                              | Supported test cases                 |
|:----:|:-------------------------------------------------:|:------------------------------------:|
| 1.   | TPM Support                                       | All                                  |
| 2.   | Verified Boot support                             | VBO001.002, VBO002.002               |
| 3.   | Measured Boot support                             | All                                  |
| 4.   | Secure Boot support                               | All                                  |
