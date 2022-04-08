# Hardware configuration matrix

The tables below contain information about current components of the testing
environment for Talos II board available in 3mdeb testing laboratory.

Configuration with a single IBM POWER9 64bit CPU is supported.
Dual CPU setup not supported currently.

## Board No. 1

<<<<<<< HEAD
| Component                      | Description                                                   | Board connection                |
|--------------------------------|---------------------------------------------------------------|---------------------------------|
| **CPU**                        | TBD                                                           | `CPU1` slot                     |
|                                | TBD                                                           | `CPU2` slot                     |
|                                | CPU Cooler                                                    | `CPU_FAN1` connector            |
| **RAM**                        | TBD                                                           | `DIMM_B2` slot                  |
| **Flash memory**               | TBD                                                           | `BIOS` slot                     |
| **Network**                    | Local network wired connection                                | `LAN1` port                     |
| **Attached devices**           | 1. TBD                                                        | `USB1` port                     |
|                                | 2. TBD                                                        | `TPM1` connector                |
| **Power Supply**               | TBD W ATX type power supply                                   | `SSIPWR1`, `SSI12V1` connectors |
| **Power Control**              | 1. Sonoff S20 switch                                          | N/A                             |
|                                | 2. Goldpin cables (RTE <-> Board connection)                  | `PANEL1` connector              |
| **Remote Testing Environment** | 1. RTE `v1.0.0` (firmware `v0.5.3`) connected via RS232       | `COM1` port                     |
|                                | 2. Goldpin cables + qspimux (RTE <-> flash memory connection) | `BIOS` slot                     |

Following RAM configurations were tested and are proved to be properly
initialized.

=======
>>>>>>> 3c275ad19786fa1db6035a0197b5e5c82583814a

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
