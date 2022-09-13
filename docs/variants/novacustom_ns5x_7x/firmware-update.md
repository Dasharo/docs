# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update.

## Update using DTS

It is a method of updating not only the firmware but also the EC firmware. If
you are interested in version v1.3.0 or higher, this is the only recommended
method, not using specialized equipment. Follow this instruction:
[Dasharo EC Transition](../../../common-coreboot-docs/dasharo_tools_suite/#dasharo-ec-transition).

If this is your first experience with DTS, first read its
[documentation](https://docs.dasharo.com/common-coreboot-docs/dasharo_tools_suite/).
We recommend using DTS with the
[Bootable over network](https://docs.dasharo.com/common-coreboot-docs/dasharo_tools_suite/#bootable-over-network)
method which is less time-consuming and just easier than DTS on the USB Stick.

## Update using flashrom

If Dasharo is currently installed, only the RW_SECTION_A partition of the flash
needs to be updated. Before executing the command, make sure that the firmware
you want to flash the chip is compatible with the current EC firmware on your
device. If not, you should follow [Update using DTS](#update-using-dts).

Flash the RW_SECTION_A partition using the following command:

```bash
flashrom -p internal -w [path] --fmap -i RW_SECTION_A
```

This command also preserves UEFI settings and the boot order.

## Update using fwupd

To update the firmware using fwupd follow
[this documentation](../../common-coreboot-docs/fwupd_usage.md).

> Due to change the EC firmware, update using fwupd isn't supported from v1.2.0
    firmware version.
