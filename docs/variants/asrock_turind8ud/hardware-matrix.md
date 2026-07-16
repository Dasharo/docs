# Hardware configuration matrix

## Introduction

This document describes the hardware configuration used for validation of the
coreboot port on the ASRock Rack TURIND8UD-2T/X550.

### Main components

|         Component          |                                 Description                                 |
| -------------------------- | --------------------------------------------------------------------------- |
| CPU                        | AMD EPYC 9115                                                               |
| CPU cooler                 | ARCTIC Freezer 4U-SP5 (single tower, AMD SP5)                               |
| RAM                        | Kingston 16GB ECC Registered DDR5 1Rx8 5600MHz                              |
|                            | PC5-44800 RDIMM (KSM56R46BS8PMI-16HAI)                                      |
| BIOS Flash memory          | Winbond W25Q256JVFQ                                                         |
| BMC Flash memory           | Macronix MX25L51245G                                                        |
| Network                    | Local network wired connection                                              |
| Storage                    | Kingston KC3000 512GB M.2 2280 PCIe Gen4 x4 NVMe SSD                        |
| Power Supply               | Seasonic VERTEX GX-750 (750W, 80 Plus Gold)                                 |
| Power Control              | NOUS A1T smart outlet                                                       |
| Case                       | NZXT H5 Flow (2024) Tempered Glass, White                                   |
| Remote Testing Environment | RTE `v1.1.0` (firmware `v0.7.5`) connected via RS232                        |
| TPM                        | ASRock TPM-SPI module (Infineon)                                            |

### Miscellaneous components

|                                  Component                                  | Description (if applicable) |
| --------------------------------------------------------------------------- | --------------------------- |
| IDC to RS232 adapter                                                        | StarTech                    |
| DuPont 2.0mm to 2.54mm pitch cables                                         |                             |
| 2x5 1.27mm pitch header to individual 2.54mm female DuPont connector cables |                             |
| RTE mount with base                                                         | 3D Printed                  |
| RS232 null modem cable                                                      |                             |
| RTE hat with mux                                                            |                             |
| PCIe x1 I/O shield with 2x keystone                                         | 3D Printed                  |
| USB-A to USB micro-B cable                                                  |                             |
| RJ45 Ethernet cable                                                         |                             |
| USB-A to USB micro-B keystone                                               |                             |
| RJ45 to RJ45 keystone                                                       |                             |
| RTE power supply                                                            |                             |
