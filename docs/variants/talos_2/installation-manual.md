# Running the coreboot on Talos II

1. Copy the binaries to the BMC
   (assuming in the coreboot root directory):

   ```
   scp build/bootblock.signed.ecc root@<BMC_IP>:/tmp/bootblock.signed.ecc
   scp build/coreboot.rom.signed.ecc root@<BMC_IP>:/tmp/coreboot.rom.signed.ecc
   ```
   > If that file is not present, use `coreboot.rom` instead

2. Backup the HBB partition (for faster later recovery) by invoking this
   command on BMC:

   ```
   pflash -P HBB -r /tmp/hbb.bin
   ```

3. Flash the binaries by replacing HBB partition (execute from BMC):

   ```
   pflash -e -P HBB -p /tmp/bootblock.signed.ecc
   pflash -e -P HBI -p /tmp/coreboot.rom.signed.ecc
   ```
   > Again, if that file is not present, use `coreboot.rom` instead

   Answer yes to the prompt and wait for the process to finish.

4. Log into the BMC GUI again at https://\<BMC_IP\>/. Enter the Server power
   operations (https://\<BMC_IP\>/#/server-control/power-operations) and invoke
   warm reboot. Then move to Serial over LAN remote console
   (https://\<BMC_IP\>/#/server-control/remote-console)

   Wait for a while until coreboot shows up:

   [![asciicast](https://asciinema.org/a/zkQV1KhxY4n6IrlzssuvFHHS5.svg)](https://asciinema.org/a/zkQV1KhxY4n6IrlzssuvFHHS5)

5. Enjoy the coreboot running on Talos II.

> **Optional:** In order to recovery the platform quickly to healthy state, flash
> the HBB partition back with: \
> `pflash -e -P HBB -p /tmp/hbb.bin`
