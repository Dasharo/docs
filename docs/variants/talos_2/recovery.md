# Recovery

## Prequisitions

To proceed with the recovery procedure the backup with the vendor firmware will
be necessary eg. `talos.pnor`.

The backup file should be generated before making any changes in the device flash
chip according to documentation in the first step in
[Testing firmware images without flashing](initial-deployment.md#testing-firmware-images-without-flashing)
section.

## Flashing using BMC

Flash firmware by executing the following commands on BMC:

```bash
pflash -E -p /tmp/talos.pnor
```

1. Log into the BMC GUI at `https://<BMC_IP>`.

1. Enter the `Server power operations`
   (`https://<BMC_IP>/#/server-control/power-operations`) and invoke
  `warm reboot`.

1. After rebooting the vendor firmware will be restored.

## Restore Petitboot

If you want to use Petitboot, and you have already installed system Heads,
follow this procedure:

1. Download the newest `PNOR` package from
    [raptor wiki](https://wiki.raptorcs.com/wiki/Talos_II/Firmware).

1. Unzip downloaded file and find the `talos.pnor` file.

1. Copy the file to the BMC:

```bash
scp talos.pnor root@<BMC_IP>:/tmp/talos.pnor
```

1. Modify partitions by executing the following commands on BMC
    (this is not necessary):

```bash
pflash -P HBB -p /tmp/bootblock.signed.ecc -F /tmp/talos.pnor
pflash -P HBI -p /tmp/coreboot.rom.signed.ecc -F /tmp/talos.pnor
```

1. Flash firmware:

```bash
pflash -E -p /tmp/talos.pnor
```

1. Log into the BMC GUI at `https://<BMC_IP>`.

1. Enter the `Server power operations`
   (`https://<BMC_IP>/#/server-control/power-operations`) and invoke
  `warm reboot`.

1. Enjoy the Petitboot running on Talos II.
