# Building manual

## Building coreboot

To build coreboot image, follow the steps below:

1. Clone the coreboot repository:

    ```bash
    git clone --depth=1 https://github.com/Dasharo/coreboot.git -b raptor-cs_talos-2/rel_v0.7.0
    ```

1. Get the submodules:

    ```bash
    cd coreboot
    git submodule update --init --recursive --checkout
    ```

1. Start docker container:

    ```bash
    docker run --rm -it \
       -v $PWD:/home/coreboot/coreboot \
       -w /home/coreboot/coreboot \
       -u "$(id -u):$(id -g)" \
       coreboot/coreboot-sdk:0ad5fbd48d /bin/bash
    ```

1. Inside of the container, configure and start the build process:

    ```bash
    (docker)cp configs/config.raptor-cs-talos-2 .config
    (docker)make olddefconfig
    (docker)make
    ```

## Building heads

1. Clone the heads repository:

    ```bash
    git clone --depth=1 https://github.com/Dasharo/heads.git -b raptor-cs_talos-2/release
    ```

1. Start docker container:

    ```bash
    cd heads
    docker run --rm -it -v $PWD:$PWD -w $PWD -u "$(id -u):$(id -g)" 3mdeb/heads-docker:2.4.0 /bin/bash
    ```

1. Build:

    ```bash
    make BOARD=talos-2
    ```
