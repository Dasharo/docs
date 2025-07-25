# Initial deployment

Initial flashing of Dasharo firmware can be done from Linux using flashrom with
the internal programmer.

 This document describes the process of building, installing and running
flashrom on Ubuntu 24.04.

## Build flashrom

Please follow generic guide for [Dasharo flashrom fork](../../osf-trivia-list/deployment.md#how-to-install-dasharo-flashrom-fork).

## Reading flash contents

Always prepare a backup of the current firmware image. To read from the flash
and save it to a file (`dump.rom`), execute the following command:

```bash
flashrom -p internal -r dump.rom
```

## Flashing Dasharo

To flash Dasharo on the platform, execute the following command - replace `[path]`
with the path to the Dasharo image you want to flash, e.g. `novacustom_nuc_box_v0.9.0.rom`.

```bash
sudo flashrom -p internal -w [path]
```

After successful operation, power off the platform, unplug power from the
platform, plug it back in and power the platform back on.
