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
    git clone https://github.com/Dasharo/coreboot.git \
    -b protectli_vault_glk/release
    ```

2. Check out the desired version e.g. `v1.0.0`:

    ```bash
    cd coreboot
    git checkout protectli_vault_ehl_v1.0.0
    ```

3. Start build process:

    ```bash
    ./build.sh vp2420
    ```

The resulting coreboot image will be placed in `build/coreboot.rom`.
