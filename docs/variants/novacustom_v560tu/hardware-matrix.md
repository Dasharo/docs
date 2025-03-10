# Hardware configuration matrix

## Introduction

This document describes the hardware configurations used for validation of the
coreboot port on the NovaCustom V560TU laptop.

## Ports specification

### Front & Rear Views

![](../../images/novacustom_v560tu_ports_front_rear_view.png)

| No.  | Description                                      |
|------|--------------------------------------------------|
| 1.   | LED Indicators                                   |
| 2.   | RJ-45 LAN Jack                                   |
| 3.   | HDMI-Out Port                                    |
| 4.   | Vent/Fan Intake/Outlet                           |

### Left side view

![](../../images/novacustom_v560tu_ports_left_view.png)

| No.  | Description                                      |
|------|--------------------------------------------------|
| 1.   | Security Lock Slot                               |
| 2.   | MicroSD Push-Push Card Reader                    |
| 3.   | USB 3.2 Gen 1 Type A Port                        |
| 4.   | 2-In-1 Audio Jack (Headphone/Microphone)         |
| 5.   | Speaker                                          |

### Right side view

![](../../images/novacustom_v560tu_ports_right_view.png)

| No. |                            Description                             |
| --- | ------------------------------------------------------------------ |
| 1.  | Speaker                                                            |
| 2.  | USB 3.2 Gen 2 Port (Type C) with PD DC-in and [Always On USB][aou] |
| 3.  | Thunderbolt™ 4 (Type C) with PD DC-in and [Always On USB][aou]     |
| 4.  | USB 3.2 Gen 2 Port (Type A) with [Always On USB][aou]              |
| 5.  | DC-In Jack                                                         |

[aou]: ../../dasharo-menu-docs/dasharo-system-features.md#power-management-options

The graphics used are from pages 43-47 of the official end user manual for the
V546TU platforms.

## V560TU

| Component                      | Description                                      |
|--------------------------------|--------------------------------------------------|
| **CPU**                        | Intel(R) Core(TM) Ultra 7 155H                   |
|                                | Internal Cooling                                 |
| **RAM**                        | Slot 1: W-NM56S516G                              |
| **SSD**                        | Goodram PX700 2TB                                |
| **SSD**                        | Goodram PX600 250GB                              |
| **Flash memory**               | XMC 25QU256CXIQ                                  |
| **USB pendrives**              | SanDisk Ultra USB 3.0 32 GB                      |
| **USB Keyboard**               | Logitech, Inc. Keyboard K120                     |
| **Wireless card 1**            | Intel Wi-Fi 6E AX211                             |
| **Wireless card 2**            | Intel Wi-Fi 7 BE200                              |
| **Display**                    | Display 1: HDMI 1920x1080p                       |
| **Network**                    | Local network wired connection                   |
| **Internal devices**           | 1. 1920x1200 16 inch screen                      |
|                                | 2. Internal ANSI keyboard                        |
|                                | 3. Touchpad                                      |
|                                | 4. Camera                                        |
|                                | 5. Audio subsystem                               |
| **Attached devices**           | The platform is tested with every docking station/hub listed [in HCL][HCL] |
| **Power Supply**               | Chicony 19V, 4.74A, 90 W                         |

[HCL]: https://docs.dasharo.com/unified/novacustom/hcl/#v56-series
