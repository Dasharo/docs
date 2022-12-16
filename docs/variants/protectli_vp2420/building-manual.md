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

2. Checkout the desired version, e.g. `v1.0.0`:

    ```bash
    cd coreboot
    git checkout protectli_vault_ehl_v1.0.0
    ```

3. Checkout submodules:

    ```bash
    git submodule update --init --checkout
    ```

4. Obtain the Protectli blobs package and extract it to
   `3rdparty/blobs/mainboard` directory (or keep it as `protectli_blobs.zip`
   file in the coreboot directory, the build script will extract it if needed
   in step 5).

5. Build the firmware v1.0.0 or newer:

    ```bash
    ./build.sh vp2420
    ```

The resulting coreboot image will be placed in `build/coreboot.rom`.
