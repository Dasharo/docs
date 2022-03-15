# Insurgo Dasharo on Talos II - installation manual

## coreboot installation

1. Copy the binaries to the BMC
   (assuming in the coreboot root directory):

    ```bash
    $ scp build/bootblock.signed.ecc root@<BMC_IP>:/tmp/bootblock.signed.ecc
    $ scp build/coreboot.rom.signed.ecc root@<BMC_IP>:/tmp/coreboot.rom.signed.ecc
    ```

    > If that file is not present, use `coreboot.rom` instead

1. Backup the HBB partition (for faster later recovery) by invoking this
   command on BMC:

    ```bash
    # pflash -P HBB -r /tmp/hbb.bin
    # pflash -P HBI -r /tmp/hbi.bin
    ```

1. Flash the binaries by replacing HBB partition (execute from BMC):

    ```bash
    # pflash -e -P HBB -p /tmp/bootblock.signed.ecc
    # pflash -e -P HBI -p /tmp/coreboot.rom.signed.ecc
    ```

    > Again, if that file is not present, use `coreboot.rom` instead

    Answer yes to the prompt and wait for the process to finish.

1. Log into the BMC GUI again at `https://<BMC_IP>.`

1. Enter the `Server power operations`
   (`https://<BMC_IP>/#/server-control/power-operations`) and invoke
  `warm reboot`.

1. Go to `Serial over LAN remote console` (`https://<BMC_IP>/#/server-control/remote-console`)

1. Wait for a while until coreboot shows up:

    [![asciicast](https://asciinema.org/a/zkQV1KhxY4n6IrlzssuvFHHS5.svg)](https://asciinema.org/a/zkQV1KhxY4n6IrlzssuvFHHS5)

1. Enjoy the coreboot running on Talos II.

> **Optional:** In order to recovery the platform quickly to healthy state, flash
> the HBB partition back with:
> `pflash -e -P HBB -p /tmp/hbb.bin`
> `pflash -e -P HBI -p /tmp/hbi.bin`

## heads installation

1. Copy the heads binary to the BMC (assuming in the heads root directory):

    ```bash
    $ scp build/zImage.bundled root@<BMC_IP>:/tmp/zImage.bundled
    ```

1. Log in to the BMC

    ```bash
    $ ssh root@<BMC_IP>
    ```

1. Flash the `BOOTKERNEL` partition with heads:

    ```bash
    # pflash -E -p /tmp/flash.pnor
    # pflash -e -P BOOTKERNEL -p /tmp/zImage.bundled
    ```

    Answer yes to the prompt and wait for the process to finish.

1. Log into the BMC GUI at `https://<BMC_IP>/`.

1. Enter the `Server power operations`
   (`https://<BMC_IP>/#/server-control/power-operations`) and invoke
  `warm reboot`.

1. Go to `Serial over LAN remote console` (`https://<BMC_IP>/#/server-control/remote-console`)

1. Wait for a while until heads shows up:

   [![asciicast](https://asciinema.org/a/VYszHn2aslY4GdAVBvsgbWb3d.svg)](https://asciinema.org/a/VYszHn2aslY4GdAVBvsgbWb3d)

1. Enjoy the heads running on Talos II.
