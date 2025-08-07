# Initial deployment

Initial flashing of Dasharo firmware can be done from Linux using flashrom with
the internal programmer or using the Dasharo Tools Suite included in the Dasharo
Pro Package subscription (formerly Dasharo Entry Subscription). An instruction
on how to use the DTS can be found in the [DTS documentation](../../dasharo-tools-suite/documentation/features.md#dasharo-zero-touch-initial-deployment)

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

To flash Dasharo on the platform, it is only possible with an external
programmer currently. Follow the same process as in [recovery
section](recovery.md).
