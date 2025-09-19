# Hardware configuration matrix

## Introduction

This document describes the hardware configuration used for validation of the
coreboot port on the ASRock Rack SPC741D8-2L2T/BCM.

|         Component          |                       Description                        |
| -------------------------- | -------------------------------------------------------- |
| CPU                        | Intel Xeon Silver 4410Y                                  |
|                            | Arctic Freezer 4U-M Rev. 2                               |
| RAM                        | Micron RDIMM DDR5 16GB 1Rx8 4800MHz PC5-38400 ECC        |
| Flash memory               | Winbond W25Q512FV                                        |
| Network                    | Local network wired connection                           |
| Attached devices           | 1. Goodram 16GB USB stick                                |
|                            | 2. Kingston KC3000 512GB M.2 2280 PCI-E x4 Gen4 NVMe SSD |
|                            | 3. Samsung 990 PRO NVMe SSD                              |
| Power Supply               | SeaSonic Vertex GX 850W                                  |
| Power Control              | 1. Sonoff S20 switch                                     |
|                            | 2. Goldpin cables (RTE <-> Board connection)             |
| Remote Testing Environment | RTE `v1.1.0` (firmware `v0.7.5`) connected via RS232     |
| TPM                        | ASROCK TPM-SPI (Nuvoton NPCT750)                         |
