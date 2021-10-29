# Insurgo Dasharo on Talos II - building manual

## Building coreboot

To build coreboot image, follow the steps below:

1. Clone the coreboot repository:

    ```bash
    $ git clone git@github.com:dasharo/coreboot.git -b raptor-cs_talos-2/release
    ```

1. Get the submodules:

    ```bash
    $ cd coreboot
    $ git submodule update --init --recursive --checkout
    ```

1. Start docker container:

    ```
    $ docker run --rm -it \
       -v $PWD:/home/coreboot/coreboot \
       -w /home/coreboot/coreboot \
       3mdeb/coreboot-sdk:mkimage /bin/bash
    ```

1. Inside of the container, configure and start the build process:

    ```
    (docker)$ cp configs/config.raptor-cs-talos-2 .config
    (docker)$ make olddefconfig
    (docker)$ make
    ```

## Building heads

1. Clone the heads repository:

    ```bash
    $ git clone git@github.com:dasharo/heads.git -b raptor-cs_talos-2/release
    ```

1. Start docker container:

    ```
    $ docker run --rm -it -v $PWD:$PWD -w $PWD 3mdeb/heads-docker:2.3.0 /bin/bash
    ```

1. Build:

    ```bash
    $ make BOARD=talos-2_server
    ```
