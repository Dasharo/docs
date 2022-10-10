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

1. Build the firmware:

    ```bash
    ./build.sh build
    ```

    The resulting coreboot image will be placed in
    `artifacts/dasharo_novacustom_ns5xz_VERSION.rom`.

**Warning:** Do not run `./build.``sh` as root. This command uses docker and
should be executed as your current user. If you're having trouble running
`build.sh` on your user account, follow the `Docker` instructions outlined in
[Requirements](#requirements).
