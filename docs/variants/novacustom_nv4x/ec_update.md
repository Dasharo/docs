# EC firmware update

coreboot has been developed and tested in combination with Embedded Controller
firmware version 1.07.05 and 1.07.08. Therefore, before flashing coreboot, it's
necessary to first check and update/downgrade the EC firmware to one of these
versions.

At the moment, the EC firmware version can only be checked while running stock
Insyde BIOS firmware.

## Check EC firmware version

To check the current EC firmware version while running stock Insyde BIOS, run
the following command:

```bash
dmidecode -t 0 | grep 'Firmware Revision'

Firmware Revision: 7.5
```

The line `Firmware Revision: 7.5` indicates that the EC is running firmware
version 1.07.05, which is one of the supported versions. If the version is
different, it is necessary to upgrade (or downgrade) the EC firmware to a
supported version.

## Update EC firmware

Updating the EC is performed with the `EcFlash` EFI application.

- Download [EC firmware 1.07.05](https://cloud.3mdeb.com/index.php/s/HFGjcEfz5i75JRr)
- Format a USB stick to FAT32
- Extract the update to root directory of the USB stick
- Plug the stick into the laptop
- Boot the laptop into the UEFI shell
- Open the USB stick, e.g. by running the command `FS0:` - one of the
  filesystems in the FS list will be the USB stick
- Run the command `EcFlash.NSH` to update the EC

The laptop will update the EC and reboot automatically. `EcFlash` can also be
used while running `coreboot`.
