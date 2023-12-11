# Hardware compatibility

## Introduction

This page contains the list of peripherals that have been verified to work with
NovaCustom laptops by the Dasharo validation team. They are tested with each
release for each laptop currently supported.

### USB-C docking stations

<div class="annotate" markdown>

* Wavlink UMD05 Pro Rev.E, Rev.C1 (USB-C DP Alternate mode)
    - 1x DP 1.4, 2x HDMI 2.0b (1)
    - Power Delivery up to 100W
    - 4x USB 3 5Gbps Type-A ports, one with BC1.2 charging
    - SD + MicroSD card reader
    - Gigabit Ethernet
    - 3.5mm combo (headphone + mic) audio jack

* Wavlink UG69PD2 Rev.A1 (DisplayLink)
    - 2x HDMI / DP ports (2)
    - Power Delivery up to 65W
    - 4x USB 3 5Gbps Type-A ports, one with BC1.2 charging
    - 2x USB 3 5Gbps Type-C ports
    - Gigabit Ethernet
    - 3.5mm headphone and mic jacks


> **Note on DisplayLink compatibility:** DisplayLink requires a driver to
> function correctly. On Windows, the driver should install automatically if
> network is connected and Windows Update is enabled. On Linux, consult your
> distribution documentation on DisplayLink compatibility.

</div>

1. DisplayPort Alt mode, Synaptics VMM5310 DP MST hub, two upstream DP 1.4
   lanes, DSC 1.2 decompression, up to 2x 4K60 + 1x 4K30 depending on source

2. DisplayLink, up to 2x 5K60 supported. OS driver required

### USB-C Hubs

<div class="annotate" markdown>

* Levin 7-in-1 USB Type-C Hub Pro
    - HDMI
    - Power delivery pass-through
    - 2x USB-A 5Gbps
    - SD, TF card reader

* Generic 7-in-1 USB Type-C Hub
    - HDMI, VGA (1)
    - Power delivery pass-through
    - 2x USB-A 5Gbps
    - SD card reader
    - Ethernet
    - 3.5mm headphone jack

</div>

1. Only one can be used simultaneously
