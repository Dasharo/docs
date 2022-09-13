# Dell OptiPlex 7010/9010 Dasharo - building manual

**Please read the [overview page](overview.md) first!**

## Building coreboot

To build release image of Dasharo compatible with Dell OptiPlex 7010/9010,
follow the steps below:

1. Clone the coreboot repository:

    ```bash
    git clone https://github.com/dasharo/coreboot.git
    ```

    ```bash
    cd coreboot
    ```

    Replace vX.Y.Z with valid version:

    ```bash
    git checkout dell_optiplex_9010_vX.Y.Z
    ```

    Checkout submodules:

    ```bash
    git submodule update --init --recursive --checkout
    ```

1. Start docker container:

    ```bash
    docker run --rm -it \
       -v $PWD:/home/coreboot/coreboot \
       -w /home/coreboot/coreboot \
       coreboot/coreboot-sdk:VERSION /bin/bash
    ```

    * `VERSION` should be replaced according to version you building:
      - `v0.1.0` - `2022-04-04_9a8d0a03db`

1. Inside of the container, configure and start the build process:

    ```bash
    make distclean
    ```

    ```bash
    cp configs/config.dell_optiplex_9010 .config
    ```

    ```bash
    make olddefconfig
    ```

    ```bash
    make
    ```

    or simply:

    ```bash
    make distclean && cp configs/config.dell_optiplex_9010 .config && make olddefconfig && make
    ```

This will produce a release binary placed in `build/coreboot.rom`. To flash
Dasharo refer to [initial deployment manual](initial-deployment.md).

## Debug build

1. Clone the coreboot repository:

    ```bash
    git clone https://github.com/dasharo/coreboot.git
    ```

    ```bash
    cd coreboot
    ```

    Replace vX.Y.Z with a valid version:

    ```bash
    git checkout dell_optiplex_9010_vX.Y.Z
    ```

    Checkout submodules:

    ```bash
    git submodule update --init --recursive --checkout
    ```

1. Start docker container:

    ```bash
    docker run --rm -it \
       -v $PWD:/home/coreboot/coreboot \
       -w /home/coreboot/coreboot \
       coreboot/coreboot-sdk:VERSION /bin/bash
    ```

    * `VERSION` should be replaced according to version you building:
      - `v0.1.0` - `2022-04-04_9a8d0a03db`

1. Inside of the container, configure and start the build process:

    ```bash
    make distclean
    ```

    ```bash
    cp configs/config.dell_optiplex_9010.debug .config
    ```

    ```bash
    make olddefconfig && make
    ```

This will produce a debug binary placed in `build/coreboot.rom`. To flash
Dasharo refer to [initial deployment manual](initial-deployment.md).
