# Hardware configuration matrix

This document describes the hardware configurations used for validation of the
coreboot port on ASUS KGPE-D16 platforms.

## ASUS KGPE-D16 8MB

| Component                  | Description                                                  |
|----------------------------|--------------------------------------------------------------|
| Board revision             | 1.03G                                                        |
| CPU                        | AMD Opteron(TM) Processor 6282 SE                            |
|                            | CPU Cooler                                                   |
|                            | AMD Opteron(TM) Processor 6282 SE                            |
|                            | CPU Cooler                                                   |
| RAM                        | DDR3 16GB Kingston KVR16R11D4/16                             |
|                            | DDR3 16GB Kingston KVR16R11D4/16                             |
| Flash memory               | Winbond W25Q64FV 8MB                                         |
| Network                    | Local network wired connection                               |
| Attached devices           | 1. Goodram 16GB USB stick                                    |
|                            | 2. ASUS TPM-L R2.0 module (chip Infineon SLB9665 TT2.0)      |
| Power Supply               | 700 W ATX type power supply                                  |
| Power Control              | 1. Sonoff S20 switch                                         |
|                            | 2. Goldpin cables (RTE <-> Board connection)                 |
| Remote Testing Environment | 1. RTE `v1.0.0` (firmware `v0.5.3`) connected via RS232      |
|                            | 2. Goldpin cables + qspimux (RTE <-> flash memory connection)|
| TPM                        | Infineon SLB9665 TT2.0                                       |

> Standard testing procedure is performed on setup without TPM module.

## ASUS KGPE-D16 16MB

| Component                  | Description                                                          |
|----------------------------|----------------------------------------------------------------------|
| Board revision             | 1.03G                                                                |
| CPU                        | AMD Opteron(TM) Processor 6282 SE                                    |
|                            | CPU Cooler                                                           |
| RAM                        | DDR3 16GB Kingston KVR16R11D4/16                                     |
| Flash memory               | Winbond W25Q128JV 16MB                                               |
| Network                    | Local network wired connection                                       |
| Attached devices:          | 1. Goodram 16GB USB stick                                            |
|                            | 2. ASUS TPM 1.2 Rev 1.02h module (chip Infineon SLB9635 TT 1.2)      |
|                            | 3. Post Debug Card                                                   |
| Power Supply               | 700 W ATX type power supply                                          |
| Power Control:             | 1. Sonoff S20 switch                                                 |
|                            | 2. Goldpin cables (RTE <-> Board connection)                         |
| Remote Testing Environment | 1. RTE `v1.0.0` (firmware `v0.5.3`) connected via RS232              |
|                            | 2. POMONA Clip + DIP8/SOIC8 adapter (RTE <-> flash memory connection)|
| TPM                        | Infineon SLB9635 TT1.2                                               |

> Standard testing procedure is performed on setup without TPM module.

ASUS KGPE-D16 board ports, slots, and connectors description is available in
the manufacturer
[documentation](https://dlcdnets.asus.com/pub/ASUS/mb/SocketG34(1944)/KGPE-D16/Menual_QVL/E8847_KGPE-D16.pdf)
(page 2-7).
