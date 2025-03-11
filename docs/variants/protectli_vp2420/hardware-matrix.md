# Hardware configuration matrix

## Introduction

This document describes the hardware configuration used for validation of the
coreboot port on the Protectli VP2420 firewall.

## Protectli VP2420

| Component              | Description                                              |
|------------------------|----------------------------------------------------------|
| **CPU**                | Intel(R) Celeron(R) J6412 @ 2.00GHz                      |
| **RAM**                | KINGSTON KVR29S21S6/8                                    |
| **Flash memory**       | Macronix MX25U6435E/F                                    |
| **SSD**                | 1. goodram SSDPR-CX400-256                               |
|                        | 2. goodram SSDPR-CL100-240-g2                            |
| **MMC drive**          | SAMSUNG 8GTF4R (on-board)                                |
| **USB pendrives**      | 1. SanDisk USB 3.2Gen1 16 GB                             |
|                        | 2. SanDisk USB 3.2Gen1 32 GB                             |
|                        | 3. USB Type-C Hub Pro UCN3286                            |
| **USB headers**        | USB Expander                                             |
| **Attached devices**   | 1. Logitech, Inc. Keyboard K120                          |
|                        | 2. Dell Mouse MS116p                                     |
|                        | 3. USB Type-C Hub Pro UCN3286                            |
| **Wireless card**      | Qualcomm Atheros QCA6174                                 |
| **Display**            | HDMI 1920x1080p, DP 1920x1080p                           |
| **Ethernet**           | 4x intel i225 (on-board)                                 |
| **Power supply**       | Channel Well Technology 12V, 5.0A 60W                    |

> Note, that in **RAM** section all used during verification procedure modules
> have been listed. Device has only one RAM mounting slot.
