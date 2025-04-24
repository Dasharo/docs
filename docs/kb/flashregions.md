# Intel Flash regions

## Introduction

In modern Intel platforms, the SPI flash is home to multiple different
firmwares, and is shared between several masters. The SPI flash is divided
into regions, each containing different firmware or configuration for a
different purpose.

This document describes the intricacies of SPI flash regions and explains when
and which regions to flash. This documentation is specific to Intel-based
platforms and may not apply to all platforms.

## Regions

### Intel Flash Descriptor

The IFD region is always located in the first sectors of the SPI flash and
contains the layout of the flash. It also describes the access permissions for
each master (which may be the host processor, Intel ME, and Intel Gigabit
Ethernet). It can be considered the "partition table" equivalent for SPI Flash.

On Dasharo platforms, this region is typically set to writable by the host
processor, to allow certain features which require modifying the flash
descriptor. Other, proprietary firmware implementations often lock this region,
in which case external flashing is required.

To enable parsing of regions described by the IFD in flashrom, append `--ifd`
to your flashrom command. This argument is required if you want to flash
specific regions described by the IFD, like BIOS, ME, GBE or the IFD itself.

To include the IFD region in a flashrom read or write operation, append `-i fd`
to your flashrom command

### Intel Gigabit Ethernet

The Gigabit Ethernet (GbE) region is present on platforms which feature the
Intel i219 series of network interfaces. This region describes the configuration
of the network adapter, including the MAC address.

This region should **not be touched unless necessary**, for example, if you're
trying to change the MAC address of the platform.

To include the GbE region in a flashrom read or write operation, append `-i gbe`
to your flashrom command.

### Intel Management Engine

The Management Engine (ME) region contains the ME's firmware and configuration.
This region is updated as part of regular BIOS updates.

On Dasharo platforms, this region is typically left writable by the host to
allow runtime firmware updates. On proprietary firmware implementations, this
region may be read and / or write protected, in which case external flashing is
required.

To include the ME region in a flashrom read or write operation, append `-i me`
to your flashrom command.

### BIOS

The BIOS region is where the host firmware resides. This region is updated as
part of regular BIOS updates.

On Dasharo firmware, the region is typically unlocked for reading and flashing,
but some parts of it may be write-protected using PRx registers.

If you have the following in your flashrom output:

```text
PR0: Warning: 0x001c0000-0x01ffffff is read-only.
```

then part of the BIOS region is protected and is not writable. On Dasharo
firmware, this lock can usually be disabled by disabling `BIOS Boot Medium Lock`
in the UEFI setup menu. On proprietary firmware implementations, look for a
similarly named option, but your mileage may vary. Otherwise, external flashing
is required.

To include the BIOS region in a flashrom read or write operation, append
`-i bios` to your flashrom command.
