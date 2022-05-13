# Protectli Dasharo on FW6 - installation manual

Flashing coreboot can be done from Linux using flashrom with the internal
programmer. This document describes the process of building, installing and
running flashrom on Ubuntu 20.04.

## Installing flashrom

Your distribution will need at least flashrom v1.0.

```bash
sudo apt install flashrom
```

## Reading flash contents

Always prepare a backup of the current firmware image. To read from the flash
and save them to a file (`dump.rom`), execute the following command:

```bash
sudo flashrom -p internal -r dump.rom
```

## Flashing Dasharo

```bash
flashrom -p internal -w [path] --ifd -i bios
```

To flash Dasharo on the platform, execute the following command - replace `[path]`
with the path to the Dasharo image you want to flash, e.g. `protectli_fw6_DF_v1.0.14.rom`.

```bash
sudo flashrom -p internal -w protectli_fw6_DF_v1.0.14.rom --ifd -i bios
```

After successful operation reboot the platform.
