# Building manual

## Intro

This document describes the procedure for compiling coreboot for NovaCustom
NS5x/7x.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git

## Build Dasharo BIOS firmware

The easiest way to build coreboot is to use the official Docker image.

1. Obtain the image:

    ```bash
    docker pull coreboot/coreboot-sdk:0ad5fbd48d
    ```

1. Clone the coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot.git
    ```

    Navigate to the source code directory and checkout to the desired revision:

    > Replace the REVISION with:
    >
    > - `clevo/release` for the latest released version
    > - `novacustom_ns5x_vVERSION` (e.g. `v1.3.0`) for the given release

    ```bash
    cd coreboot
    git checkout REVISION
    git submodule update --init --recursive --checkout
    ```

1. Start the coreboot-sdk Docker container:

    ```bash
    docker run --rm -it -u $UID \
       -v $PWD:/home/coreboot/coreboot \
       -w /home/coreboot/coreboot \
       coreboot/coreboot-sdk:0ad5fbd48d /bin/bash
    ```

1. Build the firmware:

    ```bash
    cp configs/config.novacustom_ns5x .config
    make olddefconfig
    make
    ```

The resulting coreboot image will be placed in
`build/coreboot.rom`.

## Build EC firmware

1. Clone the ec repository:

    ```bash
    git clone https://github.com/Dasharo/ec.git
    ```

    Navigate to the source code directory and checkout to the desired revision:

    > Replace the REVISION with:
    >
    > - `release` for the latest released version
    > - `novacustom_ns5x_vVERSION` (e.g. `v1.3.0`) for the given release

    ```bash
    cd ec
    git checkout REVISION
    ```

1. Build the firmware:

    ```bash
    cd ec
    EC_BOARD_VENDOR=clevo EC_BOARD_MODEL=ns50mu ./build.sh
    ```

The resulting image will be placed in: `clevo_ns50mu_ec.rom`
