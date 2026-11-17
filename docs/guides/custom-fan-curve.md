# Custom fan curve instructions

## Introduction

The fan curve can be customised according to the user's needs using the
`Custom` mode which enables configuration of the 4 point fan curve. Fans
can be controlled from the firmware settings as well as from Linux, provided
the dasharo-acpi-dkms driver is installed.

## Configuration in firmware

1. Enter the setup menu and navigate through the following menus:
   - Dasharo System Features
   - Power Management Settings

2. Set the `Fan profile` to `Custom` for the `Custom fan curve` menu to appear

### Custom fan curve menu

In the `Custom fan curve` menu the 4 point custom curve can be configured.
`Temperature` corresponds to the X axis, and `Fan duty` corresponds to the Y axis.

To apply the changes they have to be saved before exiting the menu.

!!! note
    For each point, the `Temperature` and `Fan duty` values must be higher than for
    the previous point, and must be in range 0-100. Any invalid characters will be
    blocked on input.

    The order of the points is checked on saving so the curve can be edited in
    any order.

## Configuration in Linux

A custom fan curve can also be configured from Linux, however this path requires
installing the `dasharo-acpi-dkms` driver. It is available on
[GitHub](https://github.com/Dasharo/dasharo-acpi-dkms/releases/latest).

### Installing dasharo-acpi-dkms driver

=== "Debian/Ubuntu"
    Install dependencies:

    ```bash
    sudo apt install dkms
    ```

    Install driver:

    ```bash
    sudo apt install ./dasharo-acpi-dkms_*.deb
    ```

    To load the driver, reboot or run:

    ```bash
    sudo modprobe dasharo-acpi
    ```

=== "Fedora"
    Install dependencies:

    ```bash
    sudo dnf install dkms kernel-headers
    ```

    Install driver:

    ```bash
    sudo dnf install ./dasharo-acpi-dkms_*.rpm
    ```

    To load the driver, reboot or run:

    ```bash
    sudo modprobe dasharo-acpi
    ```

### Setting the custom fan curve

Before setting the custom fan curve it is required to know the hwmon
number for the PWM controls. Substitute HWMON_NUM for the result of
the following command:

```bash
ls /sys/devices/platform/DSHR0001\:00/hwmon
```

A custom fan curve can be set in Linux using the following commands:

- Setting fan duty to 100% on point X for fan A. The value is in range 0-255.

```bash
echo 255 | sudo tee /sys/class/hwmon/HWMON_NUM/pwmA_auto_pointX_pwm
```

- Setting temperature to 50C on point X for fan A

```bash
echo 50000 | sudo tee /sys/class/hwmon/HWMON_NUM/pwmA_auto_pointX_temp
```

!!! note

    As in the setup menu, for each point the `Temperature` and `Fan duty` values
    must be higher than for the previous point.

    Each write must result in a valid state of the whole curve. Unlike
    in the setup menu, where the check for the correct order happens on
    saving the settings, any writes of values, causing the curve to become
    invalid, will be rejected.
