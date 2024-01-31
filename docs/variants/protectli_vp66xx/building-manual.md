# Building manual

## Intro

This document describes the procedure for compiling coreboot for Protectli
VP6630/VP6650/VP6670.

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
    git checkout protectli_vault_adl_v0.9.0
    ```

3. Checkout submodules:

    ```bash
    git submodule update --init --checkout
    ```

4. Build the firmware:

    ```bash
    ./build.sh vp66xx
    ```

The resulting coreboot image will be placed in the coreboot directory as
`protectli_vp66xx.rom`.
