# Dasharo for Asus KGPE-D16 - building manual

## Building coreboot

To build coreboot image, follow the steps below:

1. Clone the coreboot repository:

    ```bash
    $ git clone git@github.com:dasharo/coreboot.git -b asus_kgpe_d16/develop
    ```

2. Get the submodules:

    ```bash
    $ cd coreboot
    $ git submodule update --init --recursive --checkout
    ```

3. Start docker container:

    ```
    $ docker run --rm -it \
       -v $PWD:/home/coreboot/coreboot \
       -w /home/coreboot/coreboot \
       coreboot/coreboot-sdk:0ad5fbd48d /bin/bash
    ```

4. Inside of the container, configure and start the build process:

    ```
    (docker)$ cp configs/config.asus_kgpe_d16 .config
    (docker)$ make olddefconfig
    (docker)$ make
    ```

This will produce a debug binary placed in `build/coreboot.rom`. To flash
coreboot refer to [Flashing section in the hardware setup page.](setup.md#flashing)
