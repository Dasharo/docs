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

1. Log into the BMC GUI at `https://<BMC_IP>`.

1. Enter the `Server power operations`
   (`https://<BMC_IP>/#/server-control/power-operations`) and invoke
  `warm reboot`.

1. After rebooting the vendor firmware will be restored.
