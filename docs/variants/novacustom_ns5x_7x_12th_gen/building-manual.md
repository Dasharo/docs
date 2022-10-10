# Building manual

## Intro

This document describes the procedure for compiling coreboot for NovaCustom
NS5xPU/NS7xPU.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git

## Procedure

The easiest way to build coreboot is to use the official Docker image.

1. Obtain the image:

    ```bash
    docker pull coreboot/coreboot-sdk:2021-09-23_b0d87f753c
    ```

1. Clone the coreboot repository:

    ```bash
    git clone https://review.coreboot.org/coreboot.git
    ```

1. Checkout to the desired Dasharo revision:

    > Replace the REVISION with one of the:
    > - `clevo/release-adl-p` for the latest released version
    > - `novacustom_ns5xpu_ns7xpu_vVERSION` (e.g. `v1.0.0`) for the given release

    ```bash
    cd coreboot
    git remote add dasharo https://github.com/dasharo/coreboot.git
    git submodule update --init --recursive --checkout
    git fetch dasharo
    git checkout REVISION
    ```

1. Run the coreboot-sdk container:

    ```bash
     docker run --rm -it \
        -v $PWD:/home/coreboot/coreboot \
        -w /home/coreboot/coreboot \
        coreboot/coreboot-sdk:2021-09-23_b0d87f753c /bin/bash
    ```

1. Build the firmware:

    ```bash
    cp configs.config.clevo_ns5xpu_ns7xpu .config
    make oldddefconfig
    make
    ```

This will produce a Dasharo binary placed in `build/coreboot.rom`, which can be
flashed in following ways, depending on your situation:

- To flash Dasharo first time refer to [initial deployment manual](initial-deployment.md).
- To update Dasharo refer [firmware update](firmware-update.md).
