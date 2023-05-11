# Building manual

## Intro

This document describes the procedure for compiling coreboot for Protectli
VP2420. The procedure requires access to Protectli blobs, which are not
available to all users.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git
- Access to [protectli-blobs](https://github.com/Dasharo/protectli-blobs)

## Build Dasharo BIOS firmware

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

1. Obtain the Protectli blobs package by downloading the zip file from the 
   [newest tag](https://github.com/Dasharo/protectli-blobs/tags).
1. Extract it from coreboot repository to the `3rdparty/blobs/mainboard`
   directory and customize the folder name:

    ```bash
    unzip protectli_blobs.zip -d 3rdparty/blobs/mainboard
    mv 3rdparty/blobs/mainboard/protectli-blobs-1.0.18 3rdparty/blobs/mainboard/protectli
    ```

1. Build the firmware v1.0.0 or newer:

    ```bash
    ./build.sh vp2420
    ```

The resulting coreboot image will be placed in the coreboot directory as
`protectli_vp2420_<version>.rom`.
