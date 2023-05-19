# Building manual

## Intro

This document describes the procedure for compiling coreboot for Protectli
VP2420.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git

## Build Dasharo BIOS firmware

1. Clone the coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot
    ```

1. Checkout the desired version, e.g. `v1.0.0`:

    ```bash
    cd coreboot
    git checkout protectli_vault_ehl_v1.0.0
    ```

1. Checkout submodules:

    ```bash
    git submodule update --init --checkout
    ```

1. Obtain the Protectli blobs package, extract it and copy just `protectli`
   directory to `3rdparty/blobs/mainboard` directory.

1. Build the firmware v1.0.0 or newer:

    ```bash
    ./build.sh vp2420
    ```

The resulting coreboot image will be placed in the coreboot directory as
`protectli_vp2420_<version>.rom`.
