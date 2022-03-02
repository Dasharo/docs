# Dell OptiPlex 7010/9010 Dasharo - building manual

## Building coreboot

To build coreboot image, follow the steps below:

1. Clone the coreboot repository:

    ```bash
    $ git clone https://review.coreboot.org/coreboot.git
    ```

2. Get the submodules:

    ```bash
    $ cd coreboot
    $ git submodule update --init --recursive --checkout
    ```

3. Checkout Dasharo branch for OptiPlex 7010/9010 (replace vX.Y.Z with valid
   version):

    ```bash
    $ git remote add dasharo https://github.com/dasharo/coreboot.git
    $ git fetch dasharo
    $ git checkout dell_optiplex_9010_vX.Y.Z
    ```

4. Start docker container:

    ```bash
    $ docker run --rm -it \
       -v $PWD:/home/coreboot/coreboot \
       -w /home/coreboot/coreboot \
       coreboot/coreboot-sdk:0ad5fbd48d /bin/bash
    ```

5. Inside of the container, configure and start the build process:

    ```bash
    (docker)$ make distclean
    (docker)$ cp configs/config.dell_optiplex_9010_sff .config
    (docker)$ make olddefconfig
    (docker)$ make
    ```

    or simply:

    ```bash
    (docker)$ make distclean && cp configs/config.dell_optiplex_9010_sff .config && make olddefconfig && make
    ```

6. Container can be closed safely with `exit` Release Dasharo binary compatible
   with Dell OptiPlex 7010/9010 SFF can be found in `build/coreboot.rom`.

In case of flashing Dasharo first time please continue using [initial deployment manual](initial-deployment.md). 
To perform update from older Dasharo version please continue using [firmware update](firmware-update.md).
