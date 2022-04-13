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

## Testing firmware images without flashing

It is possible to test new firmware images without flashing the physical flash
device. This makes testing and switching between two versions (e.g. Hostboot and
coreboot) much faster and safer. There are two ways of doing so, one is
described on [Raptor's wiki](https://wiki.raptorcs.com/wiki/Compiling_Firmware#Running_the_firmware_temporarily)
and requires starting `mboxd` manually, the second one is described below.
v2.00+ BMC firmware requirement still applies.

1. Read original flash:

    For earlier versions of coreboot port it is required to read from system
    that booted at least once, since some of the partitions are modified on the
    first boot. this is no longer necessary since v0.5.0.

    ```shell
    root@talos:~# pflash -r /tmp/talos.pnor
    ```

    This file may also be copied out of BMC to a secure place and serve as a
    backup of whole flash contents.

    > Keep in mind that tmpfs size is limited and exceeding that limit may
    > result in unresponsive BMC, which in most severe cases requires hard power
    > cycle.

1. "Flashing" modified partition(s):

    This is similar to flashing real device with two changes: no need to erase
    the flash and target file must be specified. New command looks like this:

    ```shell
    root@talos:~# pflash -P <partition> -p <partition>.bin -F /tmp/talos.pnor
    ```

    For partition and file names check previous sections. Since the real flash
    device is not used, backup can be skipped.

1. Mount the file as flash device:

    ```shell
    root@talos:~# mboxctl --backend file:/tmp/flash.pnor
    ```

    Sometimes this command fails with timeout, in that case repeat it until it
    succeeds. Optionally, success can be tested with:

    ```shell
    root@talos:~# mboxctl --lpc-state
    LPC Bus Maps: BMC Memory
    ```

    `BMC Memory` tells that emulated flash is used instead of real one. Host
    doesn't see any difference (except maybe different access times and erase
    block size), it still reads and writes PNOR the same way as with physical
    device.

1. Start the platform as described in previous sections and test it.

1. To get back to using real PNOR:

    ```shell
    root@talos:~# mboxctl --backend vpnor
    Failed to post message: Connection timed out
    root@talos:~# mboxctl --lpc-state
    LPC Bus Maps: Flash Device
    ```

    Even though that command reports failure, it maps LPC back to flash device.
    This can be tested with `mboxctl --lpc-state`.

1. (Optional) Flash tested image to permanent storage:

    ```shell
    root@talos:~# pflash -E -p /tmp/talos.pnor
    ```
