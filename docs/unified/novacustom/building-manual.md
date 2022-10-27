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

1. Refer to the table below to set the `SDK`, `REVISION`, and `CONFIG` variables
   based on your device and preference:
    - using release branch will always result in the latest released version,
    - using tag you can specify the exact version to build.

| Device        | SDK version             | release branch | tag format                 | config |
|---------------|-------------------------|----------------|----------------------------|---------------------|
| NV4X TGL      | coreboot-sdk:0ad5fbd48d | clevo/release  | novacustom_nv4x_vX.Y.Z     | novacustom_nv4x_tgl |
| NS5X/7X TGL   | coreboot-sdk:0ad5fbd48d | clevo/release  | novacustom_ns5x_vX.Y.Z     | novacustom_ns5x_tgl |
| NS5X/NS7X ADL | coreboot-sdk:0ad5fbd48d | clevo/release  | novacustom_ns5x_adl_vX.Y.Z | novacustom_nv4x_adl |
| NV4X ADL      | coreboot-sdk:0ad5fbd48d | clevo/release  | novacustom_nv4x_adl_vX.Y.Z | novacustom_ns4x_adl |

1. Export variables:

    ```bash
    export SDK="<SDK>"
    export REVISION="<BRANCH_OR_TAG>"
    export CONFIG="<CONFIG>"
    ```

    For example, if you want to build `v1.3.0` firmware for the `NS5X ADL`, you
    should set:

    ```bash
    export SDK="coreboot-sdk:0ad5fbd48d"
    ```

    ```bash
    export REVISION="novacustom_ns5x_adl_v1.3.0"
    ```

    ```bash
    export CONFIG="config.novacustom_ns5x_adl.3.0"
    ```

1. Clone the Dasharo coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot.git
    ```

1. Navigate to the source code directory and checkout to the desired revision:

    ```bash
    cd coreboot
    ```

    ```bash
    git checkout $REVISION
    ```

    ```bash
    git submodule update --init --recursive --checkout
    ```

1. Start docker container:


    ```bash
    docker run --rm -it -u $UID \
       -v $PWD:/home/coreboot/coreboot \
       -w /home/coreboot/coreboot \
       $SDK /bin/bash
    ```

1. Inside of the container, configure and start the build process:

    ```bash
    cp configs/config.$CONFIG .config
    ```

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
