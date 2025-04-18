# OS installation

The following document contains information about supported operating systems
installation process on Protectli hardware. This includes official
resources from the OS vendor and some tips that we found during testing.

## FreeBSD

### Installation documentation

Official documentation can be found
[here](https://docs.freebsd.org/en/books/handbook/bsdinstall/).

### Installation images

Installer images can be downloaded from the official
[website](https://www.freebsd.org/where/).

## Debian

### Installation documentation

Official documentation can be found
[here](https://www.debian.org/releases/stable/amd64/).

### Installation images

Installer images can be downloaded from the official
[website](https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/)

## pfSense

### Installation documentation

Official documentation can be found
[here](https://docs.netgate.com/pfsense/en/latest/install/index.html).

### Installation images

Installer images can be downloaded from the official
[website](https://atxfiles.netgate.com/mirror/downloads/).

!!! note "Installation using only serial port"

    If you want to install pfSense using only a serial connection you
    have to download `pfSense-CE-memstick-serial-*` image.
    Please also note that pfSense only uses serial 0 during the installation.

## Ubuntu Server

### Installation documentation

Official documentation can be found
[here](https://ubuntu.com/tutorials/install-ubuntu-server#1-overview).

### Installation images

Installer images can be downloaded from the official
[website](https://ubuntu.com/download/server).

## Proxmox Virtual Environment

### Installation documentation

Official documentation can be found
[here](https://proxmox.com/en/products/proxmox-virtual-environment/get-started).

### Installation images

Installer images can be downloaded from the official
[website](https://proxmox.com/en/downloads/proxmox-virtual-environment/iso).

## OPNsense

### Installation documentation

Official documentation can be found
[here](https://docs.opnsense.org/manual/install.html).

!!! Note

    When you boot the installer's live environment to start installation
    you have to log in as **installer** with password **opnsense**.

### Installation images

Installer images can be downloaded from the official
[website](https://opnsense.org/download/).

## XCP-NG

### Installation documentation

Official documentation can be found
[here](https://docs.xcp-ng.org/installation/install-xcp-ng/).

### Installation images

Installer images can be downloaded from the official
[website](https://updates.xcp-ng.org/isos/).

## ESXI

### Installation documentation

Official documentation can be found
[here](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/esxi-installation-and-setup-7-0/installing-and-setting-up-esxi/installing-esxi/installing-esxi-interactively/install-esxi-interactivelly.html)

!!! note "Installation using only serial port"

    Current versions of ESXI (8.0.3) do not support installing using
    only serial console.

### Installation images

Guide on how to download the installer image can be found on Brodacom's
[website](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/6-7/esxi-installation-and-setup-6-7/installing-and-setting-up-esxi-install/before-you-install-esxi-install/download-the-esxi-installer-install.html).
