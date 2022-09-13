# Recovery

## Vendor firmware recovery

### Prequisitions

To proceed with the recovery procedure the backup with the vendor firmware will
be necessary eg. `dump.rom`.

The backup file should be generated before making any changes in the device
flash chip according to documentation in the
[Reading flash contents](initial-deployment.md#reading-flash-contents)
section.

### Internal flashing

If the platform is booting properly it's possible to recover vendor firmware
using flashrom on Ubuntu 20.04. If the flashrom from previous operations is lost
somewhere, build it according to
[this documentation](initial-deployment.md#build-flashrom).

To restore the vendor firmware, open a terminal and run the following command:

```bash
flashrom -p internal -w dump.rom
```
