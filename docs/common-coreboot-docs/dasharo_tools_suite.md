# Dasharo Tools Suite

## Introduction

Dasharo Tools Suite (DTS) is a set of tools running in a minimal Linux
environment, with a goal of deploying, updating and maintaining firmware on
Dasharo supported devices. For example, it can be used to update the firmware
on a device, even when no OS is currently installed.

## DTS flavors

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

The following documentation describes how to otain and use Community Edition
version. To obtain OEM version conatct us by using
[email](mailto:contact@dasharo.com).

## DTS CE distribution methods

It can be distributed in various ways. Currently, there are two distribution
options:

* bootable USB stick image.
* bootable over network (iPXE),

### Bootable USB stick

This documentation is compatible with the `v0.3.0` version of the DTS.

### Requirements

* USB stick (at least 1GB)
* Wired network connection
* Secure Boot disabled
* [DTS CE v0.3.0 downloaded](https://cloud.3mdeb.com/index.php/s/Q7pAppm4gnRCef9/download)

### Launching DTS

* Flash the downloaded `dts-base-image-ce-v0.3.0.wic.gz` image onto USB stick.
    - you can use cross-platform GUI installer - [Etcher](https://www.balena.io/etcher/)
    - you can also use `dd` to flash from command line

```bash
gzip -cdk dts-base-image-ce-v0.3.0.wic.gz | sudo dd of=/dev/sdX bs=16M status=progress conv=fdatasync
```

* Insert the USB stick to a USB in your device

* Boot from the USB stick

### Using DTS

* A menu should appear

* Enter `1` to dump logs with hardware from your device

![](../images/dts-hcl-run.png)

## Bootable over network

This documentation is compatible with the `v0.1.0` version of the DTS.

### Requirements

* Dasharo device with DTS functionality integrated
* Wired network connection
* Secure Boot disabled

### Launching DTS

To access Dasharo Tools Suite:

* Attach a wired network cable to the device's Ethernet port
* Power on the device, holding down the Boot Menu entry key
* In the Boot Menu, select the `iPXE Network Boot` option
* In the Network Boot menu, select the `Dasharo Tools Suite` option
* Login as `root` (no password)

The DTS shell will now appear.

### Using DTS

Within DTS, you may use the `flashrom` and `fwupdmgr` utilities to update,
downgrade, or reinstall your firmware.

To update your firmware to the latest version:

```bash
fwupdmgr refresh
fwupdmgr update
```
