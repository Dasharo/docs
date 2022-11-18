# Dasharo firmware building guide

## Intro

This guide shows how to build Dasharo firmware for Samsung Chromebook 3
devices.

## Requirements

This guide was verified on Ubuntu 22.04. In practice, any Linux distribution
with [Docker](https://www.docker.com/) support should be enough to complete it.

Make sure that you have following packages installed:

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git

    ```bash
    sudo apt -y install git
    ```

## Build Dasharo BIOS firmware

1. Clone the Dasharo coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot.git
    ```

1. Navigate to the source code directory and checkout to the desired revision:

    ```bash
    cd coreboot
    ```

    > Replace `X.Y.Z` with a valid version

    ```bash
    git checkout google_celes_vX.Y.Z
    ```

1. Checkout submodules:

    ```bash
    git submodule update --init --recursive --checkout
    ```

1. Start docker container:

   ```bash
   docker run --rm -it -u $UID \
      -v $PWD:/home/coreboot/coreboot \
      -w /home/coreboot/coreboot \
      coreboot/coreboot-sdk:2021-09-23_b0d87f753c /bin/bash
   ```

1. Inside of the container, configure the build process:

    ```bash
    make distclean && cp configs/bsw/config.celes.uefi .config
    ```

1. Start the build process:

    ```bash
    make olddefconfig && make
    ```

This will produce a Dasharo binary placed in `build/coreboot.rom`.

## Install Dasharo firmware

The Dasharo firmware can be flashed in following ways, depending on your
situation:

- To flash Dasharo for the first time, refer to the
  [initial deployment guide](initial-deployment.md).
- To update Dasharo, refer to the [firmware update guide](firmware-update.md).
