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

> This build procedure produces full firmware binary including blobs such as
> FSP, and ME. Currently, access to them is restricted to the OEM (Protectli) via
> a private repository.

1. Clone the coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot
    ```

1. Checkout the desired version, e.g. `v1.1.0`:

    ```bash
    cd coreboot
    git checkout protectli_vault_ehl_v1.1.0
    ```

1. Checkout submodules:

    ```bash
    git submodule update --init --checkout
    ```

1. Obtain the Protectli blobs package (only v1.1.0 or older):

    > Replace `<PROTECTLI_BLOBS_REPO>` with a a proper path to the repository
    > in a form of: `git@repo-path.git`. You should checkout to the same tag as
    > in case aof the coreboot repository.

    ```bash
    cd 3rdparty/blobs/mainboard/
    git init
    git remote add origin <PROTECTLI_BLOBS_REPO>
    git fetch origin && git checkout protectli_vault_ehl_v1.1.0
    cd -
    ```

1. Build the firmware:

    ```bash
    ./build.sh vp2420
    ```

The resulting coreboot image will be placed in the coreboot directory as
`protectli_vp2420_<version>.rom`.
