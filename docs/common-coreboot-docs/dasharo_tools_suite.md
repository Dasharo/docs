# Dasharo Tools Suite

![](../images/dts-logo.png)

## Introduction

Dasharo Tools Suite (DTS) is a set of tools running in a minimal Linux
environment, with a goal of deploying, updating and maintaining firmware on
Dasharo supported devices. For example, it can be used to update the firmware
on a device, even when no OS is currently installed.

## Flavors

There is a common base, but there might be multiple flavors of the DTS images.
Currently, there are:

* CE - Community Edition
    - `Dasharo HCL Report` - generates a package with logs containing hardware
      information
    - flashrom, fwupd, and many more useful tools
    - can drop to shell to update the firmware manually
* OEM
    - on top of that, provides tools for automatic firmware deployment and
      rollback (switching to Dasharo back and forth)

## Releases

This section provide links and changelogs of DTS CE version started from release
v1.0.0.

### v1.0.2

#### Images

* [USB bootable DTS CE v1.0.2 image](https://3mdeb.com/open-source-firmware/DTS/v1.0.2/dts-base-image-ce-v1.0.2.wic.gz)
* [sha256](https://3mdeb.com/open-source-firmware/DTS/v1.0.2/dts-base-image-ce-v1.0.2.wic.gz.sha256)
* [sha256.sig](https://3mdeb.com/open-source-firmware/DTS/v1.0.2/dts-base-image-ce-v1.0.2.wic.gz.sha256.sig)

  See how to verify hash and signature on [this video.](TBD-https://youtu.be/oTx2iStxXOE)

#### Changelog

* Added system76_ectool to enable Embedded Controller [firmware updating](#dasharo-ec-update)
* Added ec_transition script which helps with full Dasharo/Embedded Controller
  [firmware transition](#dasharo-ec-transition) for NS50 70MU and NS70 laptops
* First public release: [meta-dts-ce](https://github.com/Dasharo/meta-dts-ce)

### v1.0.1

#### Images

* [USB bootable DTS CE v1.0.1 image](https://3mdeb.com/open-source-firmware/DTS/v1.0.1/dts-base-image-ce-v1.0.1.wic.gz)
* [sha256](https://3mdeb.com/open-source-firmware/DTS/v1.0.1/dts-base-image-ce-v1.0.1.wic.gz.sha256)
* [sha256.sig](https://3mdeb.com/open-source-firmware/DTS/v1.0.1/dts-base-image-ce-v1.0.1.wic.gz.sha256.sig)

  See how to verify hash and signature on [this video.](https://youtu.be/oTx2iStxXOE)

#### Changelog

* Added system76_ectool to enable Embedded Controller [firmware updating](#dasharo-ec-update)
* Added ec_transition script which helps with full Dasharo/Embedded Controller
  [firmware transition](#dasharo-ec-transition) for NS50 70MU and NS70 laptops
* First public release: [meta-dts-ce](https://github.com/Dasharo/meta-dts-ce)

### v1.0.0

#### Images

* [USB bootable DTS CE v1.0.0 image](https://3mdeb.com/open-source-firmware/DTS/v1.0.0/dts-base-image-ce-v1.0.0.wic.gz)
* [sha256](https://3mdeb.com/open-source-firmware/DTS/v1.0.0/dts-base-image-ce-v1.0.0.wic.gz.sha256)

  ```bash
  # assuming all files have been downloaded to the same directory without
  # changing names
  sha256sum -c [sha256 file]
  ```

#### Changelog

* Auto-login functionality
* User menu
* [Dasharo HCL Report](#dasharo-hcl-report) - the ability to automatically dump
  device information and send it to 3mdeb servers
* Possibility to manually [update the Dasharo firmware](#dasharo-firmware-update)
* [Bootable via iPXE](#bootable-over-network)
* [Bootable via USB](#bootable-usb-stick)
* Tested on NovaCustom NV4x, Dell OptiPlex 7010/9010

## Disabling Secure Boot

Any procedure which affects the firmware flashing should be preceded by
controlling the Secure Boot status and if it is turned on, turning it off. The
enabled Secure Boot will not only prevent you from operating on the firmware,
but you will also not be able to launch DTS.

To check the Secure Boot state:

1. Turn off the station, on which you want to test the Dasharo firmware.
1. Turn the station on and go to the next step immediately.
1. Hold the `BIOS SETUP KEY` to enter the `BIOS MENU`.
1. Localize and enter the `Secure Boot` menu using the arrow keys and Enter.
1. Verify that the `Secure Boot Status` field says `Disabled` - if not,
  deselect the `Enforce Secure Boot` option using the arrow keys and Enter.
1. Change the setting of Secure Boot to `Disabled` and press Enter.
1. Press the `F10` key to open the dialog box.
1. Press `Enter` to confirm changes and exit from the menu.

After completing the steps described above, Secure Boot should be disabled.
You could confirm that by repeating steps 3 - 5.

## Running

The Dasharo Tools Suite can be started in various ways. Currently, there are
two options:

* bootable over network (iPXE),
* bootable USB stick image.

The first one should be always preferred if possible, as it the easiest one to
use.

### Bootable over network

This section describes how to boot DTS using iPXE.

#### Requirements

* Dasharo device with DTS functionality integrated
* Wired network connection
* [Secure Boot disabled](#disabling-secure-boot)

#### Launching DTS

To access Dasharo Tools Suite:

* attach a wired network cable to the device's Ethernet port,
* power on the device, holding down the Boot Menu entry key,
* in the Boot Menu, select the `iPXE Network Boot` option,
* in the Network Boot menu, select the `Dasharo Tools Suite` option,
* the DTS menu will now appear.

### Bootable USB stick

This section describes how to boot DTS using USB stick.

#### Requirements

* USB stick (at least 2GB)
* Wired network connection
* [Secure Boot disabled](#disabling-secure-boot)
* Latest image from [releases](#releases) section

#### Launching DTS

To access Dasharo Tools Suite:

* flash the downloaded image onto USB stick,
    - you can use cross-platform GUI installer - [Etcher](https://www.balena.io/etcher/)
    - you can also use `dd` to flash from command line

```bash
gzip -cdk dts-base-image-ce-v1.0.0.wic.gz | \
sudo dd of=/dev/sdX bs=16M status=progress conv=fdatasync
```

> Note: this is an example for v1.0.0 image.

* insert the USB stick to a USB in your device,
* boot from the USB stick,
* the DTS menu will now appear.

## DTS CE functionality

This section describes functionality of Dasharo Tools Suite in Community
Edition. These are:

* Dasharo HCL Report,
* Dasharo firmware update,
* Dasharo EC Transition,
* Dasharo EC update

## Dasharo HCL Report

DTS allows to generate a package with logs containing hardware information. To
create one, choose option number 1 and check out the disclaimer. If you would
like to send the report to our servers, please remember about connecting the
ethernet cable.

![](../images/dts-hcl-run.png)

## Dasharo firmware update

Within DTS, you may use the `flashrom` and `fwupdmgr` utilities to update,
downgrade, or reinstall your firmware.

To update your firmware to the latest version first choose option number 9 to
drop to Shell and run:

```bash
fwupdmgr refresh
fwupdmgr update
```

## Dasharo EC Transition

DTS allows to perform full Embedded Controller firmware transition from the
proprietary vendor EC firmware, to the open-source Dasharo EC firmware.
Currently, this functionality is supported on the
[NovaCustom NS5x/NS7x](../variants/novacustom_ns5x_7x/overview.md)) and
[NovaCustom NV4x](../variants/novacustom_nv4x/overview.md) only.

To perform EC transition, make sure you are
[running DTS version v1.0.2 or higher](#running) and follow these steps:

* After boot, choose option number 6 open custom vendor submenu
* Plug in power supply (without it, flashing EC is not possible as losing power
  may result in firmware corruption)
* Choose option number 1 to perform full EC transition
  > Note: below is an example output from Embedded Controller transition on
    NovaCustom NS50MU laptop.

  ```bash
  Attempting to perform full EC transition
  Checking for opensource firmware
  Waiting for network connection ...
  --2022-09-20 14:00:50--
  https://cloud.3mdeb.com/index.php/s/GK2KbXaYprkCCWM/download
  Resolving cloud.3mdeb.com... 84.10.27.202
  Connecting to cloud.3mdeb.com|84.10.27.202|:443... connected.
  HTTP request sent, awaiting response... 200 OK
  Length: 131072 (128K) [application/octet-stream]
  Saving to: '/tmp/ecupdate.rom'

  /tmp/ecupdate.rom      100%[========>] 128.00K  --.-KB/s    in 0.02s

  2022-09-20 14:00:51 (6.00 MB/s) - '/tmp/ecupdate.rom'
  saved [131072/131072]

  --2022-09-20 14:00:51--
  https://cloud.3mdeb.com/index.php/s/SKpqSNzfFNY7AbK/download
  Resolving cloud.3mdeb.com... 84.10.27.202
  Connecting to cloud.3mdeb.com|84.10.27.202|:443... connected.
  HTTP request sent, awaiting response... 200 OK
  Length: 16777216 (16M) [application/octet-stream]
  Saving to: '/tmp/biosupdate.rom'

  /tmp/biosupdate.rom      100%[========>]  16.00M  5.49MB/s    in 2.9s

  2022-09-20 14:00:54 (5.49 MB/s) - '/tmp/biosupdate.rom'
  saved [16777216/16777216]

  Successfully downloaded EC and FW files.
  /tmp/biosupdate.rom: OK
  Found PCI subsystem match for device CLEVO NS50MU/NS51MU
  EC version: 1.07.07 is not supported, update required
  /tmp/ecupdate.rom: OK
  Updating EC...
  flashrom v1.2-575-g5618d82 on Linux 5.15.36-yocto-standard (x86_64)
  flashrom is free software, get the source code at https://flashrom.org

  Using clock_gettime for delay loops (clk_id: 1, resolution: 1ns).
  Found PCI subsystem match for device CLEVO NS50MU/NS51MU
  Mainboard EC Project: NS50MU
  Mainboard EC Version: 1.07.07
  Flash Part ID: ef 00 00
  Found unknown Winbond flash chip
  Found Programmer flash chip "Opaque flash chip" (128 kB,
  Programmer-specific) on ite_ec.
  Reading old flash chip contents... done.
  Erasing and writing flash chip... Erase/write done.
  Verifying flash... VERIFIED.
  Successfully updated EC firmware
  Installing Dasharo firmware...
  flashrom v1.2-575-g5618d82 on Linux 5.15.36-yocto-standard (x86_64)
  flashrom is free software, get the source code at https://flashrom.org

  Using clock_gettime for delay loops (clk_id: 1, resolution: 1ns).
  coreboot table found at 0x76a64000.
  Found chipset "Intel Tiger Lake U Premium".
  Enabling flash write...
  Warning: Setting BIOS Control at 0xdc from 0x8b to 0x89 failed.
  New value is 0x8b.
  SPI Configuration is locked down.
  OK.
  Found Programmer flash chip "Opaque flash chip" (16384 kB,
  Programmer-specific) mapped at physical address 0x0000000000000000.
  Reading ich descriptor... done.
  Using region: "bios".
  Reading old flash chip contents... done.
  Erasing and writing flash chip... Erase/write done.
  Verifying flash... VERIFIED.
  Successfully installed Dasharo firmware
  Powering off
  Syncing disks... Done.
  The computer will shut down automatically in 5 seconds
  ```

* Computer will shut down automatically.
* Power on your computer. Booting process may take a while.
* After boot, choose option number 9 to drop to Shell.
* Your firmware is correctly installed. You can retrieve EC firmware information
  using:

  ```bash
  system76_ectool info
  ```

  The output of the above command should contain information about
  the version of flashed firmware:

    - on `NovaCustom NS5x/NS7x`

  ```bash
  board: clevo/ns50mu
  version: 2022-08-31_cbff21b
  ```

    - on `NovaCustom NV4x`

  ```bash
  board: clevo/nv40mz
  version: 2022-10-07_c662165
  ```

## Dasharo EC update

DTS allows to update open-source Embedded Controller firmware to the newer
version. To properly update it, follow these steps:

* Retrieve information about your current EC

  ```bash
  system76_ectool info
  ```

  The output of the above-described command should contain information about
  the version of flashed firmware:

  ```bash
  board: clevo/ns50mu
  version: 2022-08-16_c12ff1a
  ```

* Download the newest version of Embedded Controller firmware.
* Plug in power supply, without it, flashing EC is not possible as losing power
  may cause in damaged firmware.
* Flash Embedded Controller firmware internally:

  ```bash
  system76_ectool flash ec_file.rom
  ```

  The output of the above-described command should look as follows:

  ```bash
  file board: Ok("clevo/ns50mu")
  file version: Ok("2022-08-16_c12ff1a")
  ec board: Ok("clevo/ns50mu")
  ec version: Ok("2022-08-31_cbff21b")
  Waiting 5 seconds for all keys to be released
  Sync
  SPI Read 128K
  Saving ROM to backup.rom
  SPI Write 128K
  SPI Read 128K
  Successfully programmed SPI ROM
  Result: Ok(())
  Sync
  System will shut off in 5 seconds
  Sync
  ```

  > Note: this is example output, versions may differ

* Retrieve information about your updated EC

  ```bash
  system76_ectool info
  ```

  The output of the above-described command should contain information about
  the version of flashed firmware:

  ```bash
  board: clevo/ns50mu
  version: 2022-08-31_cbff21b
  ```

## Reporting issues

Thank you for using Dasharo Tools Suite Community Edition. If you have
encountered any problems with this version, or would like to provide feedback
for us - please open an issue on [Dasharo
issues](https://github.com/Dasharo/dasharo-issues).
