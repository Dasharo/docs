# Building manual

## Intro

This document describes the procedure for compiling coreboot for NovaCustom
NS5x/7x.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git

## Procedure

The easiest way to build coreboot is to use the official Docker image.

1. Obtain the image:

    ```bash
    docker pull coreboot/coreboot-sdk:0ad5fbd48d
    ```

1. Clone the coreboot repository:

    ```bash
    git clone https://review.coreboot.org/coreboot.git
    ```

1. Checkout to the desired Dasharo revision:

    > Replace the REVISION with:
    >
    > - `clevo/release` for the latest released version
    > - `novacustom_ns5x_vVERSION` (e.g. `v1.3.0`) for the given release

    ```bash
    cd coreboot
    git remote add dasharo https://github.com/dasharo/coreboot.git
    git submodule update --init --recursive --checkout
    git fetch dasharo
    git checkout REVISION
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

**Warning:** Do not run `./build.``sh` as root. This command uses docker and
should be executed as your current user. If you're having trouble running
`build.sh` on your user account, follow the `Docker` instructions outlined in
[Requirements](#requirements).
