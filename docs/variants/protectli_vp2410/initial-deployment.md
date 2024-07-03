# Initial deployment

Initial flashing of Dasharo firmware can be done from Linux using flashrom with
the internal programmer. This document describes the process of building,
installing and running flashrom on Ubuntu 22.04.

## Build flashrom

Please follow generic guide for [Dasharo flashrom fork](../../osf-trivia-list/deployment.md#how-to-install-dasharo-flashrom-fork).

## Reading flash contents

Always prepare a backup of the current firmware image. To read from the flash
and save them to a file (`dump.rom`), execute the following command:

```bash
flashrom -p internal -r dump.rom
```

Keep the backup for later recovery if needed.

## Flashing Dasharo

To flash Dasharo on the platform, execute the following command - replace `[path]`
with the path to the Dasharo image you want to flash, e.g. `protectli_vault_glk_v1.0.15.rom`.

If stock firmware is currently installed:

```bash
flashrom -p internal -w [path]
```

If Dasharo is currently installed, only the COREBOOT and IFWI partitions of the
flash needs to be updated. Flash it using the following command:

```bash
flashrom -p internal -w protectli_vault_glk_v1.0.15.rom --fmap -i COREBOOT -i IFWI
```

This command also preserves Dasharo UEFI settings and the boot order.
