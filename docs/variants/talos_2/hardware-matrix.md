# Hardware configuration matrix - Talos II

## Introduction

This document describes the hardware configuration used for validation of the
coreboot port on the Talos II platform.

## Board No. 1

| Component                      | Description                                                   |
|--------------------------------|---------------------------------------------------------------|
| **CPU**                        | TBD                                                           |
|                                | TBD                                                           |
|                                | CPU Cooler                                                    |
| **RAM**                        | TBD                                                           |
| **Flash memory**               | TBD                                                           |
| **Network**                    | Local network wired connection                                |
| **Attached devices**           | 1. TBD                                                        |
|                                | 2. TBD                                                        |
| **Power Supply**               | TBD W ATX type power supply                                   |
| **Power Control**              | 1. Sonoff S20 switch                                          |
|                                | 2. Goldpin cables (RTE <-> Board connection)                  |
| **Remote Testing Environment** | 1. RTE `v1.0.0` (firmware `v0.5.3`) connected via RS232       |
|                                | 2. Goldpin cables + qspimux (RTE <-> flash memory connection) |

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
