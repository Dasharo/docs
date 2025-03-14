# Special features

This document describes special firmware features specific to NovaCustom
laptops.

## CPU throttling threshold

The user can set a custom temperature (in °C), above which the CPU will start
throttling itself. By default, the threshold is set to 80°C.

The available values range from TjMax - 63 to TjMax, where TjMax is the maximum
allowed temperature for a particular CPU. That is, for instance, 100°C for TGL
and ADL, and 110°C for MTL.

The option can be set in EDK2, under `Dasharo System Features >
Power Management Options > CPU Throttling Threshold`.

## Battery charge management

NovaCustom laptops equipped with Dasharo firmware provide several battery
management mechanisms to optimize the user experience and prolong the battery's
lifespan.

### Low battery boot prevention

To prevent corruption of the bootloader, which may occur due to a sudden power
loss during the OS boot process, booting the OS is blocked when the battery
level is below 5%. When trying to boot the OS with the battery level below the
defined threshold, the following message will be shown on the screen:

![boot_block_popup](../../images/battery_block_popup.jpg)

### Disconnected battery warning

When the firmware encounters problems with detecting the battery, the following
message will appear suggesting checking the physical connection between the
battery and mainboard:

![battery_connection](../../images/battery_connection.jpg)

### Power information error

When the firmware encounters problems with retrieving information about AC and
battery state, the following error message will be displayed:

![power_error](../../images/power_error.jpg)

### Charge thresholds

Dasharo firmware implements battery charge thresholds, which aim to extend the
lifespan of the battery:

- charging will only start when the battery level is below the lower threshold
(default: 95%)

- charging will stop once the battery level reaches the upper threshold
(default: 98%)

Custom charge thresholds can be configured using the Dasharo setup menu.

### Battery bypass mode

The device can be powered in three modes:

- Battery Mode - the device is powered using the battery only. This mode is
active only if the device is not connected to a power adapter.
- Charging Mode - when the device is connected to a proper power adapter
it is powered directly from the adapter and the battery is not used.
Only if the current charge level is below the lower charge threshold
will the battery start being charged. When the upper threshold
is achieved, the battery stops charging and again no current
is flowing through it, preventing excessive wear.
    + If you are using the device like a desktop computer, having it
constantly connected to the power adapter, consider lowering the
charge thresholds to about 70-80%. By keeping the battery at a lower
charge level the battery wear overtime can be reduced.
- Hybrid Power Boost mode - the device is powered from the battery and the
power adapter at the same time. This mode activates only when the power
adapter can't provide enough power to the system. The battery will start
charging only if the current charge falls below the lower charge threshold
and stop once the upper threshold is achieved.

## RGB keyboard

Some models feature an RGB backlit keyboard. Dasharo implements driverless
backlight control using only the hotkeys on the keyboard.

### Usage

The backlight can be controlled using the hotkeys on the numeric keypad:

- `Fn` + `/` - Next color
- `Fn` + `*` - Toggle On / Off
- `Fn` + `-` - Brightness down
- `Fn` + `+` - Brightness up

The backlight has the following color modes:

- White (default)
- Red
- Green
- Blue
- Yellow
- Magenta
- Cyan

## Fn Lock hotkey

By default, the `Function Keys` (++f1++ - ++f12++) must be used with a
combination of ++fn++ key to change display brightness, keyboard illumination,
etc. The `Fn lock` capability provides a way of using these actions without the
necessity of using the ++fn++ key.

### Enabling

Press the ++fn+caps-lock++ keys combination.

### Disabling

Press the ++fn+caps-lock++ keys combination again.

## Fan profiles

There are two fan profiles implemented. The profiles can be selected via the
[Power Management Options](../../dasharo-menu-docs/dasharo-system-features.md#power-management-options)
menu in the Setup Menu.

Fan profiles are defined as follows:

=== "Silent"

	Releases newer than v1.4.0 11th Gen and v1.6.0 12th Gen

	| Temperature [°C] | Fan speed [%] |
	|------------------|---------------|
	| 0                | 20            |
	| 65               | 25            |
	| 75               | 35            |
	| 85               | 100           |

	Releases v1.4.0 11th Gen and v1.6.0 12th Gen or older

	| Temperature [°C] | Fan speed [%] |
	|------------------|---------------|
	| 0                | 25            |
	| 65               | 30            |
	| 75               | 35            |
	| 100              | 100           |

=== "Performance"

	Releases newer than v1.4.0 11th Gen and v1.6.0 12th Gen

	| Temperature [°C] | Fan speed [%] |
	|------------------|---------------|
	| 0                | 25            |
	| 55               | 35            |
	| 75               | 60            |
	| 85               | 100           |

	Releases v1.4.0 11th Gen and v1.6.0 12th Gen or older

	| Temperature [°C] | Fan speed [%] |
	|------------------|---------------|
	| 0                | 25            |
	| 55               | 35            |
	| 75               | 60            |
	| 100              | 100           |

> Values in-between curve points are interpolated linearly.

## Power switch watchdog

In the rare events where the Embedded Controller experiences a crash or gets
stuck, the EC can be forcefully reset by simply holding the power button for
more than 10 seconds.

## Graphics Card Modes

The **V5xxTNX** models come equipped with multiple graphics modes,
allowing for specialized configurations tailored to different use
cases. These modes can be accessed through the `Hybrid Graphics`
setting, enabling users to optimize their system for either maximum
battery life, peak performance, or a balance between the two.

### NVIDIA Optimus (iGPU & dGPU Enabled)

**NVIDIA Optimus** is a hybrid mode that dynamically switches between
the integrated GPU (**iGPU**) and the dedicated GPU (**dGPU**)
depending on workload requirements. This allows the system to balance
**performance and power efficiency** by using the iGPU for less
demanding tasks and activating the dGPU when higher graphics
performance is needed.

#### **Benefits**

- **Convenience** – automatic switching between GPUs provides a
seamless experience without manual intervention.
- **Better battery life than dGPU Only mode** – the system primarily
relies on the iGPU for everyday tasks, reducing power consumption.
- **Full access to external ports** – unlike iGPU Only mode, HDMI and
the second USB-C DisplayPort remain functional.

#### **Limitations**

- **Increased power consumption compared to iGPU Only** – as the dGPU
still activates when needed, battery life is shorter than in iGPU Only
mode.
- **Potential performance inconsistencies** – automatic GPU switching
may introduce occasional stutters or latency in certain applications.
- **Linux compatibility issues** – Optimus can cause problems in Linux
due to driver and GPU switching limitations.

This mode is best suited for users who need **a balance between
battery life and performance** while maintaining full external display
functionality.

### iGPU Only

This mode is primarily designed to maximize battery life by utilizing
only the integrated GPU (iGPU), significantly reducing power
consumption.

While **NVIDIA Optimus** provides an all-in-one solution, it has
certain drawbacks, particularly affecting laptop performance when
running on battery.

When using **iGPU Only** mode, be aware of both its benefits and
limitations:

#### **Benefits**

- Extends battery life by up to **100%** compared to dGPU mode.

#### **Limitations**

- **No access to the HDMI port** – connecting an external display via
HDMI will not be possible.
- **Limited functionality of the second USB-C DisplayPort** – this
port will also be unavailable in this mode.

Choosing this mode requires balancing between extended battery life
and the full functionality of external ports.

### dGPU Only

In **dGPU Only** mode, the internal LCD screen is directly connected
to the dedicated GPU (dGPU), ensuring that it never switches back to
the integrated GPU (iGPU).

This setup provides **the highest possible performance**, making it
ideal for **demanding environments** such as video games and other
graphics-intensive applications. Additionally, it offers **better
compatibility with Linux**, as it eliminates issues related to GPU
switching. At the expense of the highest power consumption across all
modes.
