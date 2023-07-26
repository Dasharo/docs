# NovaCustom power and battery subsystem

NovaCustom laptops equipped with Dasharo firmware provide several battery
management mechanisms to optimize user experience and further prolong the
battery's lifespan.

## Boot  block when the battery is low

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

## Charging levels

Dasharo firmware implements various battery charging level limits, which can
vastly extend the lifespan of the battery:

- plugging in the charger when the battery level sits below 95%, will result in
    charging the battery until 98% of capacity is reached. The battery status
    will then change to `not charging`

- plugging in the charger when the battery level sits between 95% and 98%, will
    result in not activating the battery charging mechanism util the battery
    level below 95% is reached.