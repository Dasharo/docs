# Building manual

## Intro

This document describes the procedure for compiling coreboot for Protectli
VP3630, VP4650 and VP4670.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git

## Build Dasharo BIOS firmware

The easiest way to build coreboot is to use the official Docker image.

1. Obtain the docker image:

    ```bash
    docker pull coreboot/coreboot-sdk:2021-09-23_b0d87f753c
    ```

2. Clone the coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot.git
    ```

    Navigate to the source code directory and checkout to the desired revision:

    > Replace the REVISION with:
    >
    > - `protectli_vault_cml/release` for the latest released version
    > - `protectli_vault_cml_vVERSION` (e.g. `v1.0.18`) for the given release

    ```bash
    cd coreboot
    git checkout REVISION
    git submodule update --init --recursive --checkout
    ```

3. Start the coreboot-sdk Docker container:

    ```bash
    docker run --rm -it -u $UID \
       -v $PWD:/home/coreboot/coreboot \
       -w /home/coreboot/coreboot \
       coreboot/coreboot-sdk:2021-09-23_b0d87f753c /bin/bash
    ```

4. Since version v1.0.18 VP4630 and VP4650 use
   `config.protectli_cml_vp4630_vp4650` file and run with the same binary.
   VP4670 uses `config.protectli_cml_vp4670` file. Build the firmware:

    ```bash
    # for VP4630 and VP4650
    cp configs/config.protectli_cml_vp4630_vp4650 .config
    # OR for VP4670
    cp configs/config.protectli_cml_vp4670 .config
    make olddefconfig
    make
    ```

    Versions v1.0.17 and earlier support only VP3630 and can be built using the
    following command:

    ```bash
    ./build.sh vp46xx
    ```

The resulting coreboot image will be placed in `build/coreboot.rom`.

NOTICE: VP4630 and VP4650 binary will not work on VP4670 and vice versa. They
use different FSP variants.
