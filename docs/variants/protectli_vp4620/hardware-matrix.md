# Hardware configuration matrix - Protectli VP4620

## Introduction

This document describes the hardware configuration used for validation of the
coreboot port on the Protectli VP4620 firewall.

## Protectli VP4620 Dasharo v1.0.13

| Component              | Description                                              |
|------------------------|----------------------------------------------------------|
| **CPU**                | Intel Core i7-10510U                                     |
| **SSD**                | M.2 SSD SATA: Hoodisk SSL032GTTC7-S9A-2S                 |
|                        | M.2 SSD PCIE4X: Samsung MZVLB256HBHQ-00000               |
|                        | external SATA 2.5 inch: Goodram SSDPR-CL100-240-G2 240GB |
| **RAM**                | CRUCIAL CT4G4SFS824A                                     |
|                        | SAMSUNG M471A4G43MB1-CTD                                 |
|                        | SAMSUNG M471A1K43CB1-CTD                                 |
|                        | SAMSUNG M471A5244BB0-CRC                                 |
|                        | KINGSTON KVR24S17S8/8                                    |
|                        | KINGSTON KVR26S19S8/16                                   |
| **Wireless card**      | Intel Wi-Fi 6 AX201                                      |
| **LTE miniPCIe card**  | Quectel EC-20                                            |
| **Display**            | HDMI 1920x1080p, DP 1920x1080p                           |
| **Ethernet**           | 6x intel i225 (on-board)                                 |
| **Attached devices**   | 1. SanDisk USB 3.2Gen1 16 GB                             |
|                        | 2. SanDisk USB 3.2Gen1 16 GB                             |
|                        | 3. SanDisk USB 3.2Gen1 16 GB                             |
|                        | 4. USB Type-C Hub Pro UCN3286                            |
| **USB Keyboard**       | DELL KB216                                               |
| **MMC drive**          | SAMSUNG KLM8G1GETF-B041 (on-board)                       |
| **TPM**                | PC Engines TPM1A LPC TPM                                 |
| **Power supply**       | Channel Well Technology 12V, 7.5A 90W                    |

> Note, that in **RAM** section all used during verification procedure
    modules have been listed. Device has only two RAM mounting slots.
