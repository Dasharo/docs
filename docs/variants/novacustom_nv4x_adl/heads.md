# Dasharo (coreboot + heads) firmware variant

For the NovaCustom NV4x 12th Gen, heads-based variant of Dasharo firmware is
offered as a Technology Preview Release.

## Releases

Following Release Notes describe status of Dasharo (coreboot + heads)firmware
development for NovaCustom NV4x 12th Gen.

### v0.9.0

TBD

## Hardware Configuration Matrix

Generally, the same [hardware configuration](hardware-matrix.md) as for the
UEFI varuant applies.

A notable addition is usage of the
[Nitrokey 3A](https://shop.nitrokey.com/shop/nk3an-nitrokey-3a-nfc-14)
USB device, which is required for heads installation and usage.

## Test Matrix

Please refer to the [tests results spreadsheet](TBD).

## Building manual

This sectino presents the crucial steps required to build the Dasharo heads
firmware. For more information, you may also refer to the official
[heads building documentation](https://osresearch.net/general-building/).

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

* 1. Clone Dasharo heads repository

   ```bash
    git clone https://github.com/Dasharo/heads.git
   ```

1. Navigate to the source code directory and checkout to the desired revision:

    ```bash
    cd heads
    git checkout novacustom_nv4x_adl_v0.9.0-rc1
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

## Transition from Dasharo UEFI to heads variant

TBD

## Logo customization

To replace the logo, one must rebuild the firmware. Other methods are not
supported as of now. You would need to replace the
`branding/Dasharo/bootsplash.jpg` with your own, and proceed with the
[Building manual](#building-manual).

## Initial deployment

The supported method is to follow the
[initial deployment](/unified/novacustom/initial-deployment.md), and then the
[Transition from Dasharo UEFI to heads variant](#transition-from-dasharo-uefi-to-heads-variant).

## Firmware update

[Build](#building-manual) or download Dasharo heads firmware, and proceed with
the official [heads update documentation](https://osresearch.net/Updating).
