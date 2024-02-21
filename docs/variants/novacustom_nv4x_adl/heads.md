# Dasharo (coreboot + Heads) firmware variant

For the NovaCustom NV4x 12th Gen, Heads-based variant of Dasharo firmware is
offered as a Technology Preview Release.

Please consider to support the project financially by purchasing the
[Dasharo Entry Subscription](https://novacustom.com/product/dasharo-entry-subscription/).
With this subscription, you will get access to the
[Transition from Dasharo UEFI to Heads variant](#transition-from-dasharo-uefi-to-heads-variant)
feature in Dasharo Tools Suite and support from Dasharo directly via Matrix.
The subscription is not automatically renewed.

## Releases

Following Release Notes describe status of development of Dasharo (coreboot +
Heads) firmware for NovaCustom NV4x 12th Gen.

### v0.9.1

TBD

## Hardware Configuration Matrix

Generally, the same [hardware configuration](hardware-matrix.md) as for the
UEFI variant applies.

A notable addition is usage of the
[Nitrokey 3A Mini](https://novacustom.com/product/nitrokey-3a-mini/)
USB device, which is required for Heads installation and usage.

## Test Matrix

Please refer to the [tests results spreadsheet](TBD).

## Building manual

This sectino presents the crucial steps required to build the Dasharo Heads
firmware. For more information, you may also refer to the official
[Heads building documentation](https://osresearch.net/general-building/).

### Requirements

This guide was verified on Ubuntu 22.04. In practice, any Linux distribution
with [Docker](https://www.docker.com/) support should be enough to complete it.

Make sure that you have following packages installed:

* Docker
    - follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    - follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
* Git

    ```bash
    sudo apt -y install git
    ```

* 1. Clone Dasharo Heads repository

   ```bash
    git clone https://github.com/Dasharo/heads.git
   ```

1. Navigate to the source code directory and checkout to the desired revision:

    ```bash
    cd heads
    git checkout novacustom_nv4x_adl_v0.9.1
    ```

1. Start docker container:

    ```bash
    docker run --rm -it -v $PWD:$PWD -w $PWD \
      3mdeb/heads-docker:3.0.0 /bin/bash
    ```

1. Inside of the container, start the build process:

    ```bash
    BOARD=nitropad-nv41 make
    ```

This will produce a Dasharo binary placed in
`build/x86/nitropad-nv41/dasharo-nitropad-nv41-*.rom`.

## Transition from Dasharo UEFI to Heads variant

To change firmware branches from UEFI to Heads, because of how different the two
firmware types are, it's required to disable some security measures before
flashing. Follow the steps below to install Heads from an existing Dasharo UEFI
firmware installation:

* Enter UEFI Setup Menu and disable:
    - UEFI Secure Boot
    - SMM BIOS Write Protection
    - BIOS boot medium lock
    - Intel Management Engine
* [Boot into Dasharo Tools Suite](https://docs.dasharo.com/dasharo-tools-suite/documentation/#running)
* Enter your DES credentials in DTS
* Select `Update Dasharo firmware` to check for updates
* When asked to switch to Heads firmware, press `Y`
* Proceed with the update steps as usual

When the update is finished, your laptop with shut down automatically. Power it
back on to boot into your new Heads installation!

> On the first boot, you will be shown a warning about TOTP secrets. This is
> normal and expected on the first boot. Run `OEM Factory Reset / Re-Ownership`
> to finish deploying Heads.

## Logo customization

To replace the logo, one must rebuild the firmware. Other methods are not
supported as of now. You would need to replace the
`branding/Dasharo/bootsplash.jpg` with your own, and proceed with the
[Building manual](#building-manual).

## Initial deployment

The supported method is to follow the
[initial deployment](/unified/novacustom/initial-deployment.md), and then the
[Transition from Dasharo UEFI to Heads variant](#transition-from-dasharo-uefi-to-heads-variant).

## Firmware update

[Build](#building-manual) or download Dasharo Heads firmware, and proceed with
the official [Heads update documentation](https://osresearch.net/Updating).
