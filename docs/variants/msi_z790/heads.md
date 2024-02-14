# Dasharo (coreboot + Heads) firmware variant

Heads-based variant of Dasharo firmware compatible with MSI PRO Z790-P boards
is offered as a Technology Preview Release.

Please consider to support the project financially by purchasing the
[Dasharo Entry Subscription](https://novacustom.com/product/dasharo-entry-subscription/).
With this subscription, you will get access to the
[Transition from Dasharo UEFI to Heads variant](#transition-from-dasharo-uefi-to-heads-variant)
feature in Dasharo Tools Suite and support from Dasharo directly via Matrix.
The subscription is not automatically renewed.

## Releases

Following Release Notes describe status of Dasharo (coreboot + Heads) firmware
development compatible with MSI PRO Z790-P boards.

### v0.9.0

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

This section presents the crucial steps required to build the Dasharo Heads
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
    git checkout msi_ms7e06_v0.9.0
    ```

1. Start docker container:

    ```bash
    docker run --rm -it -v $PWD:$PWD -w $PWD \
      3mdeb/heads-docker:3.0.0 /bin/bash
    ```

1. Inside of the container, start the build process:

=== "PRO Z790-P (WIFI) DDR4"

    ```bash
    BOARD=msi_z790p_ddr4 make
    ```

    This will produce a Dasharo binary placed in
    `build/x86/msi_z790p_ddr4/dasharo-msi_z790p_ddr4-*.rom`.

=== "PRO Z790-P (WIFI)"

    ```bash
    BOARD=msi_z790p_ddr5 make
    ```

    This will produce a Dasharo binary placed in
    `build/x86/msi_z790p_ddr5/dasharo-msi_z790p_ddr5-*.rom`.

## Transition from Dasharo UEFI to Heads variant

**Recommended**

Please use [Dasharo Tools Suite](../../dasharo-tools-suite/overview.md) with
Heads subscription credentials to transition to Heads.

**Manual**

Use [FlashBIOS](../../unified/msi/recovery.md#using-msi-flashbios-button)
method or flash with flashrom in OS. To transition to heads firmware, whole
binary has to be flashed:

```bash
flashrom -p internal -w <heads_fw_file>
```

> NOTE: ME has to be disabled and descriptor unlocked to flash full file. MSI
> firmware began to ship the platforms with ME and flash descriptor regions
> read-only. Unlocking the descriptor is possible using Firmware Update Mode
> on Dasharo v0.9.1.

## Logo customization

To replace the logo, one must rebuild the firmware. Other methods are not
supported as of now. You would need to replace the
`branding/Dasharo/bootsplash.jpg` in the heads repository with your own, and
proceed with the [Building manual](#building-manual).

## Initial deployment

The supported method is to follow the
[initial deployment](/unified/novacustom/initial-deployment.md), and then the
[Transition from Dasharo UEFI to Heads variant](#transition-from-dasharo-uefi-to-heads-variant).

## Firmware update

[Build](#building-manual) or download Dasharo Heads firmware, and proceed with
the official [Heads update documentation](https://osresearch.net/Updating).
