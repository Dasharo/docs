# Hardware configuration matrix - Talos II

## Introduction

This document describes the hardware configuration used for validation of the
coreboot port on the Talos II platform.

## Talos II

| Component                      | Description                                                   |
|--------------------------------|---------------------------------------------------------------|
| **CPU**                        | IBM POWER9 “Sforza”                                           |
|                                | CPU Cooler                                                    |
| **RAM**                        | Crucial CT8G4RF88266                                          |
| **Flash memory**               | Micron MT25QL512ABB8ESF-0SIT                                  |
| **Network**                    | Local network wired connection                                |
| **Attached devices**           | SanDisk USB 3.2Gen1 16 GB                                     |
| **Ethernet**                   | 2x Broadcom BCM5719                                           |
| **Power Supply**               | Corsair TX550M                                                |
| **Power Control**              | Sonoff S20 switch                                             |
| **Remote Control**             | OpenBMC                                                       |

Following RAM configurations were tested and are proved to be properly
initialized.

```bash
MCS0, MCA0
   DIMM0: 1Rx4 16GB PC4-2666V-RC2-12-PA0
   DIMM1: not installed
MCS0, MCA1
   DIMM0: 1Rx8 8GB PC4-2666V-RD1-12
   DIMM1: not installed
MCS1, MCA0
   DIMM0: 2Rx4 32GB PC4-2666V-RB2-12-MA0
   DIMM1: not installed
MCS1, MCA1
   DIMM0: 2Rx8 16GB PC4-2666V-RE2-12
   DIMM1: not installed
```

All 3 major DRAM vendors are supported, namely Samsung, Micron and Hynix.
