# Special features

This document describes special firmware features specific to NovaCustom
laptops.

## Battery charge management

NovaCustom laptops equipped with Dasharo firmware provide several battery
management mechanisms to optimize user experience and further prolong the
battery's lifespan.

### Low battery boot prevention

To prevent corruption of the bootloader, which may occur due to a sudden power
loss during the OS boot process, booting the OS is blocked when the battery
level is below 5%. When trying to boot the OS with the battery level below the
defined threshold, following message will be displayed on screen:

![boot_block_popup](../../images/battery_block_popup.jpg)

### Disconnected battery warning

When the firmware encounters problems with detecting the battery, following
message will appear suggesting checking the physical connection between the
battery and mainboard:

![battery_connection](../../images/battery_connection.jpg)

### Power information error

When the firmware encounters problems with retrieving information about AC and
battery state, following error message will be displayed:

![power_error](../../images/power_error.jpg)

### Charge thresholds

Dasharo firmware implements battery charge thresholds, which aim to extend the
lifespan of the battery:

- charging will only start when the battery level is below 95%

- charging will stop once the battery level reaches 98%

Custom charge thresholds can be configured using the Dasharo setup menu.

## RGB keyboard

Some models featuree an RGB backlit keyboard. Dasharo implements full driverless
backlight control using only the hotkeys on the keyboard.

### Usage

The backlight can be operated using the hotkeys on the numpad:

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
[Power Management Options](/dasharo-menu-docs/dasharo-system-features/#power-management-options)
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

In the rare event the Embedded Controller experiences a crash or gets stuck,
the EC can be forcefully reset by simply holding the power button for more than
10 seconds.
