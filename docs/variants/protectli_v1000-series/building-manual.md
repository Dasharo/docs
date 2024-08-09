# Building manual

## Intro

This document describes the procedure for compiling coreboot for Protectli
V1210, V1410 and V1610.

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

2. Checkout the desired version, e.g. `v0.9.2`:

    ```bash
    cd coreboot
    git checkout protectli_vault_jsl_v0.9.2
    ```

3. Checkout submodules:

    ```bash
    git submodule update --init --checkout
    ```

4. Obtain the Protectli blobs package (only for versions v0.9.0 and v0.9.1):

    > Replace `<PROTECTLI_BLOBS_REPO>` with a a proper path to the repository
    > in a form of: `git@repo-path.git`. You should checkout to the same tag as
    > in case of the coreboot repository.

    ```bash
    cd 3rdparty/blobs/mainboard/
    git init
    git remote add origin <PROTECTLI_BLOBS_REPO>
    git fetch origin && git checkout protectli_vault_jsl_v0.9.0
    cd -
    ```

5. Build the firmware:

    + for V1210

        ```bash
        ./build.sh V1210
        ```

    + for V1410

        ```bash
        ./build.sh V1410
        ```

    + for V1610

        ```bash
        ./build.sh V1610
        ```

The resulting coreboot image will be placed in the coreboot directory as
`protectli_V1210.rom`, `protectli_V1410.rom` or `protectli_V1610.rom`
respectvely.
