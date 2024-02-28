# Dasharo APU Configuration

The Dasharo APU Configuration menu is an exclusive menu for PC Engines apu
platforms. This menu is intended to provide equivalent runtime configuration
capabilities as [PC Engines sortbootorder](https://github.com/pcengines/sortbootorder).

> Not all sortbootorder options may be currently available. They may be added
> in the future.

## Dasharo APU Configuration menu options

When entering the `Dasharo APU Configuration` menu, one may see the
following options to appear:

![](/images/menus/apu_config.jpeg){ class="center" }

### Core Performance Boost

This option enables AMD Core Performance Boost (aka CPU Turbo). When enabled
firmware will make 2 additional boosted P-states available. Core Performance
Boost is able to raise a single core frequency from 1000MHz up to 1400MHz if
other cores are pretty much inactive.

Disable this option if you notice system unstabilities.

### Watchdog

`Enable watchdog` option controls whether the AMD FCH watchdog will be enabled
during boot. When selected, the `Watchdog timeout value` will appear, where
one can specify the watchdog expiration timeout in seconds.

The watchdog is useful when a platform hangs and needs to be reset
automatically, which will happen if watchdog timer expires. Minimum timeout is
60s to let the OS take control over the watchdog (e.g. sp5100_tco watchdog
driver for Linux) and keep reloading it to avoid resets.

### PCI Express power management features

When enabled, the firmware will attempt to enable Clock Power Management, ASPM
L0s and L1 on PCI Express ports. Enabling these options may result in [PCI
Express device performance
reduction](https://github.com/pcengines/coreboot/issues/387) at the cost of
better power savings.
