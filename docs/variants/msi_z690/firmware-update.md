# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update. The update process may be different, depending on which
firmware version is currently installed on your device. The currently installed
firmware version can be checked with the following command in a Linux
environment:

```bash
sudo dmidecode -t bios | grep Version
```

Alternatively, it can be checked in the `BIOS Setup Menu`.

## Version v1.0.0 or newer

Only the `RW_SECTION_A` partition of the flash needs to be updated. Flash it
using the following command:

```bash
flashrom -p internal -w [path] --fmap -i RW_SECTION_A
```

> This command also preserves Dasharo UEFI settings and the boot order.

## Version older than v1.0.0

In this case, the whole `bios` region must be updated.

```bash
flashrom -p internal -w [path] --ifd -i bios
```
