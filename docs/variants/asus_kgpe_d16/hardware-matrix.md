# Hardware configuration matrix

The tables below contain information about current components of the testing
environment for ASUS KGPE-D16 boards available in 3mdeb testing laboratory.

## Board No. 1

<<<<<<< HEAD
| Component                      | Description                                                    | Board connection                           |
|--------------------------------|----------------------------------------------------------------|--------------------------------------------|
| **CPU**                        | AMD Opteron(TM) Processor 6282 SE                              | `CPU1` slot                                |
|                                | CPU Cooler                                                     | `CPU_FAN1` connector                       |
| **RAM**                        | DDR3 16GB Kingston KVR16R11D4/16                               | `DIMM_B2` slot                             |
| **Flash memory**               | Winbond W25Q64FV 8MB                                           | `BIOS` slot                                |
| **Network**                    | Local network wired connection                                 | `LAN1` port                                |
| **Attached devices**           | 1. Goodram 16GB USB stick                                      | `USB1` port                                |
|                                | 2. ASUS TPM-L R2.0 module (chip Infineon SLB9665 TT2.0)        | `TPM1` connector                           |
| **Power Supply**               | 700 W ATX type power supply                                    | `SSIPWR1`, `SSI12V1` connectors            |
| **Power Control**              | 1. Sonoff S20 switch                                           | N/A                                        |
|                                | 2. Goldpin cables (RTE <-> Board connection)                   | `PANEL1` connector                         |
| **Remote Testing Environment** | 1. RTE `v1.0.0` (firmware `v0.5.3`) connected via RS232        | `COM1` port                                |
|                                | 2. Goldpin cables + qspimux (RTE <-> flash memory connection)  | `BIOS` slot                                |

## Board No. 2

| Component                      | Description                                                            | Board connection                           |
|--------------------------------|------------------------------------------------------------------------|--------------------------------------------|
| **CPU**                        | AMD Opteron(TM) Processor 6282 SE                                      | `CPU1` slot                                |
|                                | CPU Cooler                                                             | `CPU_FAN1` connector                       |
| **RAM**                        | DDR3 16GB Kingston KVR16R11D4/16                                       | `DIMM_B2` slot                             |
| **Flash memory**               | Winbond W25Q128JV 16MB                                                 | `BIOS` slot                                |
| **Network**                    | Local network wired connection                                         | `LAN1` port                                |
| **Attached devices:**          | 1. Goodram 16GB USB stick                                              | `USB1` port                                |
|                                | 2. ASUS TPM 1.2 Rev 1.02h module (chip Infineon SLB9635 TT 1.2)        | `TPM1` connector                           |
|                                | 3. Post Debug Card                                                     | `PCI6` slot                                |
| **Power Supply**               | 700 W ATX type power supply                                            | `SSIPWR1`, `SSI12V1`, `SSI12V2` connectors |
| **Power Control**              | 1. Sonoff S20 switch                                                   | N/A                                        |
|                                | 2. Goldpin cables (RTE <-> Board connection)                           | `PANEL1` connector                         |
| **Remote Testing Environment** | 1. RTE `v1.0.0` (firmware `v0.5.3`) connected via RS232                | `COM1` port                                |
|                                | 2. POMONA Clip + DIP8/SOIC8 adapter (RTE <-> flash memory connection)  | `BIOS` slot                                |
=======
| Component                  | Description                                                  | Board connection                           |
|----------------------------|--------------------------------------------------------------|--------------------------------------------|
| CPU                        | AMD Opteron(TM) Processor 6282 SE                            | `CPU1` slot                                |
|                            | CPU Cooler                                                   | `CPU_FAN1` connector                       |
|                            | AMD Opteron(TM) Processor 6282 SE                            | `CPU2` slot                                |
|                            | CPU Cooler                                                   | `CPU_FAN2` connector                       |
| RAM                        | DDR3 16GB Kingston KVR16R11D4/16                             | `DIMM_B2` slot                             |
|                            | DDR3 16GB Kingston KVR16R11D4/16                             | `DIMM_F2` slot                             |
| Flash memory               | Winbond W25Q64FV 8MB                                         | `BIOS` slot                                |
| Network                    | Local network wired connection                               | `LAN1` port                                |
| Attached devices           | 1. Goodram 16GB USB stick                                    | `USB1` port                                |
|                            | 2. ASUS TPM-L R2.0 module (chip Infineon SLB9665 TT2.0)      | `TPM1` connector                           |
| Power Supply               | 700 W ATX type power supply                                  | `SSIPWR1`, `SSI12V1` connectors            |
| Power Control              | 1. Sonoff S20 switch                                         | N/A                                        |
|                            | 2. Goldpin cables (RTE <-> Board connection)                 | `PANEL1` connector                         |
| Remote Testing Environment | 1. RTE `v1.0.0` (firmware `v0.5.3`) connected via RS232      | `COM1` port                                |
|                            | 2. Goldpin cables + qspimux (RTE <-> flash memory connection)| `BIOS` slot                                |

## Board No. 2

| Component                  | Description                                                          | Board connection                           |
|----------------------------|----------------------------------------------------------------------|--------------------------------------------|
| CPU                        | AMD Opteron(TM) Processor 6282 SE                                    | `CPU1` slot                                |
|                            | CPU Cooler                                                           | `CPU_FAN1` connector                       |
| RAM                        | DDR3 16GB Kingston KVR16R11D4/16                                     | `DIMM_B2` slot                             |
| Flash memory               | Winbond W25Q128JV 16MB                                               | `BIOS` slot                                |
| Network                    | Local network wired connection                                       | `LAN1` port                                |
| Attached devices:          | 1. Goodram 16GB USB stick                                            | `USB1` port                                |
|                            | 2. ASUS TPM 1.2 Rev 1.02h module (chip Infineon SLB9635 TT 1.2)      | `TPM1` connector                           |
|                            | 3. Post Debug Card                                                   | `PCI6` slot                                |
| Power Supply               | 700 W ATX type power supply                                          | `SSIPWR1`, `SSI12V1`, `SSI12V2` connectors |
| Power Control:             | 1. Sonoff S20 switch                                                 | N/A                                        |
|                            | 2. Goldpin cables (RTE <-> Board connection)                         | `PANEL1` connector                         |
| Remote Testing Environment | 1. RTE `v1.0.0` (firmware `v0.5.3`) connected via RS232              | `COM1` port                                |
|                            | 2. POMONA Clip + DIP8/SOIC8 adapter (RTE <-> flash memory connection)| `BIOS` slot                                |
>>>>>>> 3c275ad19786fa1db6035a0197b5e5c82583814a

ASUS KGPE-D16 board ports, slots, and connectors description is available in
the manufacturer
[documentation](https://dlcdnets.asus.com/pub/ASUS/mb/SocketG34(1944)/KGPE-D16/Menual_QVL/E8847_KGPE-D16.pdf)
(page 2-7).
