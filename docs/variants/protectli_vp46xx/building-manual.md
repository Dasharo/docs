# Building manual

## Intro

This document describes the procedure for compiling coreboot for Protectli
VP4630, VP4650 and VP4670.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git

## Build Dasharo firmware

Since version v1.0.18 VP4630 and VP4650 use different configuration file than
VP4670. Versions v1.0.17 and older do not support VP4650 and VP4670 at all.

1. Clone the coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot
    ```

2. Checkout the desired version, e.g. `v1.0.18`:

    ```bash
    cd coreboot
    git checkout protectli_vault_cml_v1.0.18
    ```

3. Checkout submodules:

    ```bash
    git submodule update --init --checkout
    ```

4. Obtain the Protectli blobs package and extract it to
   `3rdparty/blobs/mainboard` directory (or keep it as `protectli_blobs.zip`
   file in the coreboot directory, the build script will extract it if needed
   in step 5).

5. Build the firmware v1.0.18 or newer:

    + for VP4630 and VP4650

        ```bash
        ./build.sh vp4630_vp4650
        ```

    + for VP4670

        ```bash
        ./build.sh vp4670
        ```

    **NOTICE**: VP4630 and VP4650 binary will not work on VP4670 and vice versa.
    They use different FSP variants.

    Versions v1.0.17 and earlier support only VP4630 and can be built using the
    following command:

    ```bash
    ./build.sh vp46xx
    ```

    The resulting coreboot image will be placed in `build/coreboot.rom`.
