# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update. The update process may be different, depending on which
firmware version is currently installed on your device. The currently installed
firmware version can be checked with the following command in a Linux
environment:

```shell
sudo dmidecode -t bios | grep Version
```

Alternatively, it can be checked in the `BIOS Setup Menu`.

## Version v1.2.0 or older

You should update to the [v1.3.0 version](../releases/#v130-2022-09-01) first,
by following
[this procedure](../../../common-coreboot-docs/dasharo_tools_suite/#dasharo-ec-transition).

## Version v1.3.0 or newer

### Update using flashrom

* Boot into
  [Dasharo Tools Suite](../../../common-coreboot-docs/dasharo_tools_suite/#running)

* Flash the `RW_SECTION_A` partition using the following command:

  ```bash
  flashrom -p internal -w [path] --fmap -i RW_SECTION_A
  ```

> This command also preserves UEFI settings and the boot order.

### Update using fwupd

To update the firmware using fwupd follow
[this documentation](../../common-coreboot-docs/fwupd_usage.md).
