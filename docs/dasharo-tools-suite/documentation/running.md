# Running

The Dasharo Tools Suite can be started in various ways. Currently, there are
two options:

* bootable over a network (iPXE),
* bootable USB stick image.

The first one should always be preferred if possible, as it is the easiest one
to use.

## Bootable over a network

This section describes how to boot DTS using iPXE.

### Requirements

Below are the requirements that must be met to run DTS over a network on the
platform:

* Dasharo device with DTS functionality integrated,
* wired network connection,
* [Secure Boot disabled](../../dasharo-menu-docs/device-manager.md#secure-boot-configuration),
* If device if flashed with Dasharo and support following functionality
    + disabled BIOS lock feature,
    + disabled SMM BIOS write protection feature.

### Launching DTS

To access Dasharo Tools Suite:

* attach a wired network cable to the device's Ethernet port,
* power on the device, holding down the Boot Menu entry key,
* in the Boot Menu, select the `iPXE Network Boot` option,
* in the Network Boot menu, select the `Dasharo Tools Suite` option, or enter
  iPXE shell and type by hand:

    ```bash
    dhcp net0
    chain https://boot.dasharo.com/dts/dts.ipxe
    ```

    !!! warning

        Because of misconfigured iPXE on some firmware releases, booting over
        HTTPS is impossible, and the above command will fail. In that case, we
        recommend downloading the DTS image to USB. If you feel there is no
        risk of an MITM attack, you can proceed with
        `http://boot.dasharo.com/dts/dts.ipxe` at your own risk.

* the DTS menu will now appear.

### Launching DTS nightly builds

!!! warning

    Nightly builds are for developers and for those who want to use the latest
    DTS without waiting for release. Hence, nightly builds are not tested and
    should be launched at your own risk!

The DTS nightly builds are updated automatically every Saturday. The builds use
the latest commit from the [`meta-dts`
repository](https://github.com/Dasharo/meta-dts) `develop` branch and the
[`dts-scripts` repository](https://github.com/Dasharo/dts-scripts) `main`
branch. The used commits could be checked in [`nightly.ipxe`
file](http://boot.dasharo.com/dts/nightly.ipxe).

To access Dasharo Tools Suite nightly build, use the following commands in the
iPXE shell, instead of  the commands described in [the chapter
above](#launching-dts):

```ipxe
dhcp
chain https://boot.dasharo.com/dts/nightly.ipxe
```

!!! warning

    Because of misconfigured iPXE on some firmware releases, booting over
    HTTPS is impossible, and the above command will fail. In that case, we
    recommend downloading the DTS image to USB. If you feel there is no
    risk of an MITM attack, you can proceed with
    `http://boot.dasharo.com/dts/nightly.ipxe` at your own risk.

## Bootable USB stick

This section describes how to boot DTS using a USB stick.

### Requirements

Below are the requirements that must be met to run DTS from a USB device on the
platform:

* USB stick (at least 2GB),
* Latest image from [releases](https://github.com/Dasharo/meta-dts/releases)
  section.
* Wired network connection,
* [Secure Boot disabled](../../dasharo-menu-docs/device-manager.md#secure-boot-configuration),
* If device if flashed with Dasharo and support following functionality
    + disabled BIOS lock feature,
    + disabled SMM BIOS write protection feature.

### Launching DTS

To access Dasharo Tools Suite:

* flash the downloaded image onto USB stick,
    + you can use a cross-platform GUI installer - [Etcher](https://www.balena.io/etcher/)
    + you can also use `dd` to flash from the command line

```bash
gzip -cdk dts-base-image-v1.1.0.wic.gz | \
sudo dd of=/dev/sdX bs=16M status=progress conv=fdatasync
```

!!! note "Notes"

    * this is an example done on the v1.1.0 image.
    * replace "sdX" with the letter of your USB disk device. For example: sda,
      sdb, sdc. It should not be partition number (for example, not sda1
      or sda2).

* insert the USB stick into a USB in your device,
* boot from the USB stick,
* the DTS menu will now appear.
