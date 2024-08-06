# Initial deployment

Initial flashing of Dasharo firmware can be done from Linux using flashrom with
the internal programmer. This document describes the process of building,
installing and running flashrom on Ubuntu 22.04.

## Deploy using Dasharo Tools Suite

For simplicity we recommend using
[Dasharo Tools Suite](../../dasharo-tools-suite/overview.md) to
omit all compilation steps and deploy the Dasharo firmware seamlessly.

1. Boot Dasharo Tools Suite.
2. Perform Dasharo installation.

This will flash the BIOS region only. After the successful operation, DTS will
reboot the platform.

This concludes Dasharo deployment process using DTS.

## Build flashrom

Please follow generic guide for [Dasharo flashrom fork](../../osf-trivia-list/deployment.md#how-to-install-dasharo-flashrom-fork).

## Reading flash contents

Always prepare a backup of the current firmware image. To read from the flash
and save it to a file (`dump.rom`), execute the following command:

```bash
flashrom -p internal -r dump.rom
```

## Flashing Dasharo

To flash Dasharo on the platform, execute the following command:

```bash
flashrom -p internal -w intel_minnowmax_v0.9.0_no_sb.rom
```

This will flash the whole image. After the operation is successful, power
cycle the platform.
