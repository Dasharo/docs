# NovaCustom power and battery subsystem

NovaCustom laptops equipped with Dasharo firmware provide several battery
management mechanisms to optimize user experience and further prolong the
battery's lifespan.

## Boot  blocking when the battery is low

To prevent corruption of the bootloader, which may occur due to sudden power cut
off during the OS boot process, booting the OS is blocked when the battery level
sits below 5%. When trying to boot the OS with the battery level below the
defined threshold, following message will be displayed on screen:

![](images/boot_block_popup.jpg)

## Disconnected battery warning

When the firmware encounters problems with detecting the battery, following
message will appear suggesting checking the physical connection between the
battery and mainboard:

![](images/battery_connection.jpg)

## Power information error

When the firmware encounters problems with retrieving information about AC and
battery state, following error message will be displayed:

![](images/power_error.jpg)

## Charge thresholds

Dasharo firmware implements battery charge thresholds, which aim to extend the
lifespan of the battery:

- charging will only start when the battery level is below 95%

- charging will stop once the battery level reaches 98%

Custom charge thresholds can be configured using the Dasharo setup menu or using
third-party software like [tlp](https://linrunner.de/tlp/faq/battery.html).
