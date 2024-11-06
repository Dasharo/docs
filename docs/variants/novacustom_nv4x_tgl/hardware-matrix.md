# Hardware configuration matrix

## Introduction

This document describes the hardware configurations used for validation of the
coreboot port on the NovaCustom NV4X laptop.

## Ports specification

### Right side view

![](../../images/novacustom_nv_ports_right_view.png)

| No.  | Description                                      |
|------|--------------------------------------------------|
| 1.   | Speaker                                          |
| 2.   | 2-In-1 Audio Jack (Headphone / Microphone)       |
| 3.   | USB 3.2 Gen 2 Type-C Port                        |
| 4.   | USB 3.2 Gen 2 Type-A Port                        |
| 5.   | HDMI-Out Port                                    |
| 6.   | Power Button                                     |
| 7.   | DC-In Jack                                       |
| 8.   | Led Indicator                                    |

### Left side view

![](../../images/novacustom_nv_ports_left_view.png)

| No.  | Description                                      |
|------|--------------------------------------------------|
| 1.   | Security Lock Slot                               |
| 2.   | RJ-45 LAN Jack                                   |
| 3.   | USB 3.2 Gen 2 Type-A Port                        |
| 4.   | SD Card Reader                                   |
| 5.   | Thunderbolt 4 Port with Power Delivery (DC-IN)   |
| 6.   | Speaker                                          |

The graphics used are from pages 17-18 of the
[official service manual](https://novacustom.stackstorage.com/s/6mFpzU01I9UR94sI/en_US)
for the NV41 platforms.

## NV41MZ

| Component                      | Description                                      |
|--------------------------------|--------------------------------------------------|
| **CPU**                        | Intel(R) Core(TM) i7-1165G7                      |
|                                | Internal Cooling                                 |
| **RAM**                        | Slot 1: KVR29S21S6/8                             |
|                                | Slot 2: KVR29S21S6/8                             |
| **SSD**                        | Samsung 980 PRO NVMe 500 GB                      |
| **Flash memory**               | GigaDevice 25B127DSIG 16 MB                      |
| **USB pendrives**              | SanDisk Ultra USB 3.0 32 GB                      |
| **USB Keyboard**               | Logitech, Inc. Keyboard K120                     |
| **Wireless card 1**            | Intel Wi-Fi 6 AX201                              |
| **Wireless card 2**            | Atheros QCNFA222                                 |
| **Display**                    | Display 1: HDMI 1920x1080p                       |
| **Network**                    | Local network wired connection                   |
| **Internal devices**           | 1. 1920x1080 14 inch screen                      |
|                                | 2. Internal keyboard with LED backlight          |
|                                | 3. Touchpad                                      |
|                                | 4. Camera                                        |
|                                | 5. Audio subsystem                               |
| **Attached devices**           | The platform is tested with every docking station/hub listed [in HCL][HCL] |
| **Power Supply**               | Chicony 19V, 3.42A, 65 W                         |

## NV41MB

| Component                      | Description                                      |
|--------------------------------|--------------------------------------------------|
| **CPU**                        | Intel(R) Core(TM) i7-1165G7                      |
|                                | Internal Cooling                                 |
| **GPU**                        | NVIDIA GeForce GTX1650 4 GB                      |
| **RAM**                        | Slot 1: KVR29S21D8/32                            |
|                                | Slot 2: KVR29S21D8/32                            |
| **SSD**                        | Samsung 980 PRO NVMe 250 GB                      |
| **Flash memory**               | GigaDevice 25B127DSIG 16 MB                      |
| **USB pendrives**              | SanDisk Ultra USB 3.0 32 GB                      |
| **USB Keyboard**               | Logitech, Inc. Keyboard K120                     |
| **Wireless card**              | Intel Wi-Fi 6 AX201                              |
| **Display**                    | Display 1: HDMI 1920x1080p                       |
| **Network**                    | Local network wired connection                   |
| **Internal devices**           | 1. 1920x1080 14 inch screen                      |
|                                | 2. Internal keyboard with LED backlight          |
|                                | 3. Touchpad                                      |
|                                | 4. Camera                                        |
|                                | 5. Audio subsystem                               |
| **Attached devices**           | The platform is tested with every docking station/hub listed [in HCL][HCL] |
| **Power Supply**               | Chicony 19V, 4.74A, 90 W                         |

[HCL]: https://docs.dasharo.com/unified/novacustom/hcl/#nv4x-11th-gen
