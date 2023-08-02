# Building manual

## Intro

This document describes the procedure for compiling coreboot for Protectli
PT201, PT401 and PT601.

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

2. Checkout the desired version, e.g. `v0.9.0`:

    ```bash
    cd coreboot
    git checkout protectli_vault_jsl_v0.9.0
    ```

3. Checkout submodules:

    ```bash
    git submodule update --init --checkout
    ```

4. Obtain the Protectli blobs package:

    > Replace `<PROTECTLI_BLOBS_REPO>` with a a proper path to the repository
    > in a form of: `git@repo-path.git`. You should checkout to the same tag as
    > in case aof the coreboot repository.

    ```bash
    cd 3rdparty/blobs/mainboard/
    git init
    git remote add origin <PROTECTLI_BLOBS_REPO>
    git fetch origin && git checkout protectli_vault_jsl_v0.9.0
    cd -
    ```

5. Build the firmware v1.0.19 or newer:

    + for PT201

        ```bash
        ./build.sh pt201
        ```

    + for PT401

        ```bash
        ./build.sh pt401
        ```

    + for PT601

        ```bash
        ./build.sh pt601
        ```

The resulting coreboot image will be placed in the coreboot directory as
`protectli_pt201.rom`, `protectli_pt401.rom` or `protectli_pt601.rom`
respectvely.
