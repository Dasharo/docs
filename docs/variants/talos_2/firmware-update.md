# Firmware update

The following documentation describes the process of Dasharo open-source firmware
update.

1. Copy the binaries to the BMC:

    ```bash
    scp build/bootblock.signed.ecc root@<BMC_IP>:/tmp/bootblock.signed.ecc
    scp build/coreboot.rom.signed.ecc root@<BMC_IP>:/tmp/coreboot.rom.signed.ecc
    ```

1. Flash the binaries by replacing the HBB partition (execute from BMC):

    ```bash
    pflash -e -P HBB -p /tmp/bootblock.signed.ecc
    pflash -e -P HBI -p /tmp/coreboot.rom.signed.ecc
    ```

1. Log into the BMC GUI at `https://<BMC_IP>`.

1. Enter the `Server power operations`
   (`https://<BMC_IP>/#/server-control/power-operations`) and invoke
  `warm reboot`.

1. Go to `Serial over LAN remote console` (`https://<BMC_IP>/#/server-control/remote-console`).

1. Enjoy the updated firmware running on Talos II.
