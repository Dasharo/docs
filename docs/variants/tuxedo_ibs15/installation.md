# Dasharo for Tuxedo IBS15 Gen6 - Installation manual

## Intro

Flashing coreboot can be done from Linux using flashrom with the internal
programmer. This document describes the process of building, installing and
running flashrom on Ubuntu 20.04.

## Build flashrom

Please follow generic guide for [Dasharo flashrom fork](../../../osf-trivia-list/deployment/#how-to-install-dasharo-flashrom-fork).

## Reading flash contents

To read from the flash and save them to a file (`dump.rom`), execute the
following command:

```bash
flashrom -p internal -r dump.rom
```

## Installing Dasharo

### Initial Installation

During the initial installation of Dasharo, you will need the supported Intel
ME version (and configuration) to be present in the Dasharo firmware image. If
you already have a Dasharo compatible ME firmware installed, then proceed with
[Updating Dasharo instructions](#updating-dasharo).

> Publicly released binaries do not contain ME binary. If you need a Dasharo
> compatible Intel ME update for your device, contact us via already
> established commercial support channel.

When flashing binaries with ME binary included, flashing of the whole chip is
required. Follow the steps below:

- Power off the laptop
- While holding the Fn+M keys, power on the laptop - This unlocks the ME and
  allows for it to be overwritten. The fans will spin at 100% speed at this
  point
- Execute the following command, replacing [path] with the path to the **full**
  firmware image (containing ME firmware and flash descriptor) you want to
  flash:

  ```bash
  flashrom -p internal -w [full_image]
  ```

- **Reboot** the laptop
- The laptop will boot into Dasharo. After Dasharo has booted, it is safe to
  shut down the laptop to silence the fans

> Note: if you shut down the laptop instead of rebooting, it may be necessary
> to hold Fn+M for it to boot the first time after flashing.

### Updating Dasharo

If Dasharo is currently installed, only the BIOS region of the flash needs to
be updated. Flash it using the following command:

```bash
flashrom -p internal -w [path] --ifd -i bios
```
