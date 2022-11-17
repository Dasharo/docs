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

## Version v1.1.0 or newer

> Version v1.1.0 had to change the flashmap layout and requires usage of the
> [procedure below](#version-older-than-v110) when migrating from v1.0.0 or
> older.

Only the `RW_SECTION_A` and `RW_SECTION_B` partitions of the flash needs to be
updated. Flash it using the following command:

```bash
flashrom -p internal -w [path] --fmap -i RW_SECTION_A -i RW_SECTION_B
```

> To flash newer firmware the command described in the
[section below](#version-older-than-v110) might be also used. But remember,
in that case, all Dasharo UEFI settings will be lost. Also, the memory training
procedure will have to be carried out again.

## Version older than v1.1.0

In this case, the whole `bios` region must be updated.

```bash
flashrom -p internal -w [path] --ifd -i bios
```
