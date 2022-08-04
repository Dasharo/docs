# Recovery

---

## Prequisitions

To proceed with the recovery procedure the backup with the vendor firmware will
be necessary, in this case, they are two files `hbb.bin` and `hbi.bin`.

Backup files should be generated before making any changes in the device flash
chip according to documentation in the second step in
[coreboot installation](initial-deployment.md#coreboot-installation)
section.

---

## Flashing using BMC

Flash firmware by executing the following commands on BMC:

```bash
pflash -e -P HBB -p /tmp/hbb.bin
pflash -e -P HBI -p /tmp/hbi.bin
```
