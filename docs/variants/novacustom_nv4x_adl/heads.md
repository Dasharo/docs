# Dasharo (coreboot + Heads) firmware variant

For the NovaCustom NV4x 12th Gen, Heads-based variant of Dasharo firmware is
offered as a Technology Preview Release.

Please consider supporting the project financially by purchasing the
[Dasharo Entry Subscription](https://novacustom.com/product/dasharo-entry-subscription/).
With this subscription, you get access to the
[Transition from Dasharo UEFI to Heads variant](#transition-from-dasharo-uefi-to-heads-variant)
feature in Dasharo Tools Suite and support from Dasharo directly via Matrix.
The subscription is not automatically renewed.

Following Release Notes describe status of development of Dasharo (coreboot +
Heads) firmware for NovaCustom NV4x 12th Gen.

## v0.9.0

### Added

* Initial release supporting Heads payload
* coreboot revision [3a9aa3a4](https://github.com/Dasharo/coreboot/commits/3a9aa3a4692f3dd49732f5b4e3ec54be385f0969/)
  based on upstream version [v4.21](https://doc.coreboot.org/releases/coreboot-4.21-relnotes.html)

### Known issues

* [Power button does not work in Qubes](https://github.com/Dasharo/dasharo-issues/issues/710)
* [Heads shuts down instead of rebooting](https://github.com/Dasharo/dasharo-issues/issues/711)
* [Existing Qubes installation is not bootable after transition back to EDK2](https://github.com/Dasharo/dasharo-issues/issues/713)

### SBOM (Software Bill of Materials)

* [Dasharo coreboot fork rev 3a9aa3a4 based on upstream version 4.21](https://github.com/Dasharo/coreboot/tree/3a9aa3a4)
* [Dasharo Heads fork rev ccf49703 based on upstream rev 25066e5f](https://github.com/Dasharo/heads/tree/ccf49703)

## Hardware Configuration Matrix

Generally, the same [hardware configuration](hardware-matrix.md) as for the
UEFI variant applies.

A notable addition is usage of the
[Nitrokey 3A Mini](https://novacustom.com/product/nitrokey-3a-mini/)
USB device, which is required for Heads installation and usage.

## Test Matrix

Please refer to the [tests results spreadsheet](https://docs.google.com/spreadsheets/d/1yWZ--zFPIsQhXZByf7nJIrasQYuRSf1yCi60lY_RGsQ).

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

### Building

1. Clone Dasharo Heads repository:

    ```bash
    git clone https://github.com/Dasharo/heads.git
    ```

1. Navigate to the source code directory and checkout to the desired revision:

    ```bash
    cd heads
    git checkout novacustom_nv4x_adl_v0.9.0
    ```

1. Start the build inside the docker container:

    ```bash
    docker run --rm -it -v $PWD:$PWD -w $PWD \
      3mdeb/heads-docker:3.0.1 make BOARD=nitropad-nv41
    ```

This will produce a Dasharo binary placed in
`build/x86/nitropad-nv41/dasharo-nitropad-nv41-*.rom`.

## Switching from Dasharo UEFI to Heads

To change firmware branches from UEFI to Heads, because of how different the two
firmware types are, it's required to disable some security measures before
flashing. Follow the steps below to install Heads from an existing Dasharo UEFI
firmware installation:

* Hold down the ++f2++ key and press the ++power++ button to enter the UEFI
  Setup Menu
* Enter the `Device Manager` submenu and disable `Secure Boot`
* Enter the `Dasharo System Features` submenu
* In the `Dasharo Security Options` submenu, disable:
    - SMM BIOS Write Protection
    - BIOS boot medium lock
* In the `Intel Management Engine Options` submenu disable the Management Engine

!!! tip

    For a more detailed guide on the UEFI Setup Menu options, check out the
    [Dasharo menu documentation](https://docs.dasharo.com/dasharo-menu-docs/).

* [Boot into Dasharo Tools Suite](https://docs.dasharo.com/dasharo-tools-suite/documentation/#running)
* Enter your DES subscription credentials
* Select `Update Dasharo firmware` to check for updates
* When asked to switch to Heads firmware, press `Y`
* Proceed with the update steps as usual

When the update is finished, your laptop will shut down automatically. Power it
back on to boot into your new Heads installation!

!!! warning "TOTP secrets warning"

    On the first boot, you will be shown a warning about TOTP secrets. This is
    normal and expected on the first boot. Run `OEM Factory Reset /
    Re-Ownership` to finish deploying Heads.

    Check out [Heads documentation](https://osresearch.net/Configuring-Keys/#oem-factory-resetre-ownership)
    for a detailed factory reset guide.

!!! note "Note for Qubes OS users"

    After installing Qubes while Heads is installed, you will need to select
    `Reset TPM` in the Heads menu to finish the installation.

    From the main menu, enter `Options` -> `TPM/TOTP/HOTP Options` and select
    `Reset the TPM`.

    Users upgrading to Heads while Qubes is already installed are not affected.

## Switching from Dasharo Heads back to UEFI

To revert back to UEFI, you will need to boot into DTS from a USB stick.

* Follow the [Dasharo Tools Suite documentation](https://docs.dasharo.com/dasharo-tools-suite/documentation/#running)
  to boot DTS from a USB stick
* In the DTS main menu, select `Update Dasharo firmware` to check for available
  updates.
* When prompted to revert back to UEFI, press `Y`
* Proceed with the firmware update process as usual.

Once finished, your laptop will shut down automatically. Power it back on to
boot into your UEFI firmware.

> When reverting to UEFI, it's not possible to restore EFI boot manager entries
> that were added before installing Heads. Therefore, you may need to re-create
> your boot entries manually, or find your boot loader using `Boot From File`
> option in the UEFI setup menu.

## Logo customization

To replace the logo, one must rebuild the firmware. Other methods are not
supported as of now. You would need to replace the
`branding/Dasharo/bootsplash.jpg` with your own, and proceed with the
[Building manual](#building-manual).

## Initial deployment

The supported method is to follow the
[initial deployment](/unified/novacustom/initial-deployment.md), and then the
[Transition from Dasharo UEFI to Heads variant](#switching-from-dasharo-uefi-to-heads).

## Firmware update

[Build](#building-manual) or download Dasharo Heads firmware, and proceed with
the official [Heads update documentation](https://osresearch.net/Updating).
