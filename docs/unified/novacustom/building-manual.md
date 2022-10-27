# Dasharo firmware building guide

## Intro

This guide shows how to build Dasharo firmware for NovaCustom devices.

## Requirements

This guide was verified on Ubuntu 22.04. In practice, any Linux distribution
with [Docker](https://www.docker.com/) support should be enough to complete it.

Make sure that you have following packages installed:

* Docker
    - follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    - follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
* Git

    ```bash
    sudo apt -y install git
    ```

## Build Dasharo BIOS firmware

1. Export variables:

1. Clone the Dasharo coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot.git
    cd coreboot
    ```

1. Checkout to the latest version:

    === "NS5x ADL v1.3.0"

        ```bash
        git checkout novacustom_ns5x_adl_v1.3.0
        ```

    === "NV4x ADL v1.3.0"

        ```bash
        git checkout novacustom_nv4x_adl_v1.3.0
        ```

    === "NS5x TGL v1.3.0"

        ```bash
        git checkout novacustom_ns5x_v1.3.0
        ```

    === "NV4x TGL v1.3.0"

        ```bash
        git checkout novacustom_nv4x_v1.3.0
        ```

    ```bash
    git submodule update --init --recursive --checkout
    ```

1. Start docker container:

    ```bash
    docker run --rm -it -u $UID \
       -v $PWD:/home/coreboot/coreboot \
       -w /home/coreboot/coreboot \
       coreboot-sdk:0ad5fbd48d /bin/bash
    ```

1. Inside of the container, configure the build process:

    === "NS5x ADL v1.3.0"

        ```bash
        cp configs/config.novacustom_ns5x_adl .config
        ```

    === "NV4x ADL v1.3.0"

        ```bash
        cp configs/config.novacustom_nv4x_adl .config
        ```

    === "NS5x TGL v1.3.0"

        ```bash
        cp configs/config.novacustom_ns5x_tgl .config
        ```

    === "NV4x TGL v1.3.0"

        ```bash
        cp configs/config.novacustom_nv4x_tgl .config
        ```


1. Start the build process:

    ```bash
    make olddefconfig
    ```

    ```bash
    make
    ```

This will produce a Dasharo binary placed in `build/coreboot.rom`, which can be
flashed in following ways, depending on your situation:

* To flash Dasharo for the first time, refer to the
  [initial deployment guide](initial-deployment.md).
* To update Dasharo, refer to the [firmware update guide](firmware-update.md).

## Build Dasharo EC firmware

1. Refer to the table below to set the `EC_BOARD_MODEL`, and `REVISION` based
   on your device and preference:
    - using `release ` branch will always result in the latest released version,
    - using tag you can specify the exact version to build.

| Device        | model    | tag format                 |
|---------------|----------|----------------------------|
| NV4X TGL      | nv4x_tgl | novacustom_nv4x_vX.Y.Z     |
| NS5X/7X TGL   | ns5x_tgl | novacustom_ns5x_vX.Y.Z     |
| NV4X ADL      | nv4x_tgl | novacustom_nv4x_adl_vX.Y.Z |
| NS5X/NS7X ADL | ns5x_adl | novacustom_ns5x_adl_vX.Y.Z |

1. Export variables:

    ```bash
    export EC_BOARD_MODEL="<MODEL>"
    export REVISION="<REVISION>"
    ```

    For example, if you want to build `v1.3.0` firmware for the `NS5X ADL`, you
    should set:

    ```bash
    export REVISION="novacustom_ns5x_adl_v1.3.0"
    ```

    ```bash
    export EC_BOARD_MODEL="novacustom_ns5x_adl"
    ```

1. Clone the Dasharo ec repository:

    ```bash
    git clone https://github.com/Dasharo/ec.git
    ```

1. Navigate to the source code directory and checkout to the desired revision:

    ```bash
    cd ec
    ```

    ```bash
    git checkout $REVISION
    ```

1. Build the firmware:

    ```bash
    EC_BOARD_VENDOR=novacustom ./build.sh
    ```

The resulting image will be placed in: `novacustom_$EC_BOARD_MODEL.rom`, which
can be flashed in following ways, depending on your situation:

* To flash Dasharo for the first time, refer to the
  [initial deployment guide](initial-deployment.md).
* To update Dasharo, refer to the [firmware update guide](firmware-update.md).
