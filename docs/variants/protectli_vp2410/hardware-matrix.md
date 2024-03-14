# Hardware configuration matrix

## Introduction

This document describes the hardware configuration used for validation of the
coreboot port on the Protectli VP2410 firewall.

## Protectli VP2410

| Component              | Description                                              |
|------------------------|----------------------------------------------------------|
| **CPU**                | Intel Celeron J4125 @ 2.70GHz                            |
| **RAM**                | CRUCIAL CT4G4SFS824A                                     |
|                        | SAMSUNG M471A4G43MB1-CTD                                 |
|                        | SAMSUNG M471A1K43CB1-CTD                                 |
|                        | SAMSUNG M471A5244BB0-CRC                                 |
|                        | KINGSTON KVR24S17S8/8                                    |
|                        | KINGSTON KVR26S19S8/16                                   |
|                        | KINGSTON KVR26S21S6/8                                    |
| **Flash memory**       | Macronix MX25U6473F                                      |
| **SSD**                | CRUCIAL CT500MX500SSD1                                   |
| **MMC drive**          | SAMSUNG 8GTF4R (on-board)                                |
| **USB pendrives**      | 1. SanDisk USB 3.2Gen1 16 GB                             |
|                        | 2. SanDisk USB 3.2Gen1 16 GB                             |
|                        | 3. USB Type-C Hub Pro UCN3286                            |
| **Attached devices**   | 1. Logitech, Inc. Keyboard K120                          |
|                        | 2. Dell Mouse MS116p                                     |
|                        | 3. USB Type-C Hub Pro UCN3286                            |
| **LTE miniPCIe card**  | Quectel EC-20                                            |
| **Wireless card**      | Intel Wi-Fi 6 AX200                                      |
| **Display**            | HDMI 1920x1080p, DP 1920x1080p                           |
| **Ethernet**           | 4x intel i211 (on-board)                                 |
| **TPM**                | PC Engines TPM1A LPC TPM                                 |
| **Power supply**       | Channel Well Technology 12V, 5.0A 60W                    |

> Note, that in **RAM** section all used during verification procedure modules
> have been listed. Device has only one RAM mounting slot.
