# Building manual

## Intro

This document describes the procedure for compiling coreboot for Protectli
VP2410.

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

1. Checkout the desired version, e.g. `v1.0.15`:

    ```bash
    cd coreboot
    git checkout protectli_vault_glk_v1.0.15
    ```

1. Checkout submodules:

    ```bash
    git submodule update --init --checkout
    ```

1. Obtain the Protectli blobs package:

    > Replace `<PROTECTLI_BLOBS_REPO>` with a a proper path to the repository
    > in a form of: `git@repo-path.git`. You should checkout to the same tag as
    > in case aof the coreboot repository.

    ```bash
    cd 3rdparty/blobs/mainboard/
    git init
    git remote add origin <PROTECTLI_BLOBS_REPO>
    git fetch origin && git checkout protectli_vault_glk_v1.0.15
    cd -
    ln -s ../blobs/mainboard/protectli/vault_glk/GeminilakeFspBinPkg/ 3rdparty/fsp/GeminilakeFspBinPkg
    ```

1. Build the firmware v1.0.15 or newer:

    ```bash
    ./build.sh vp2410
    ```

The resulting coreboot image will be placed in the coreboot directory as
`protectli_vp2410_<version>.rom`.
