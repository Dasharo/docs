# Supermicro X11 LGA1151 Series - building manual

**Please read the [overview page](../overview) first!**

To build Dasharo compatible with Supermicro X11 LGA1151 Series, follow the
steps below:

1. Clone the coreboot repository:

    ```bash
    git clone https://github.com/dasharo/coreboot.git
    ```

    ```bash
    cd coreboot
    ```

    Replace vX.Y.Z with valid version:

    ```bash
    git checkout supermicro_x11_lga1151_series_vX.Y.Z
    ```

    Checkout submodules:

    ```bash
    git submodule update --init --recursive --checkout
    ```

1. Start docker container:

    * To build `Dasharo (coreboot+UEFI) v0.1.0`:

     ```bash
    	docker run --rm -it \
    	   -v $PWD:/home/coreboot/coreboot \
    	   -w /home/coreboot/coreboot \
    	   coreboot/coreboot-sdk:2022-12-18_3b32af950d /bin/bash
     ```

     To understand difference between versions please read [FAQ](faq.md).

1. Inside of the container, configure and start the build process. 

     * Please choose correct config for your platform:

        * `config.supermicro_x11ssh_t` for X11SSH-T mainboard model
        * `config.supermicro_x11ssh_tf` for X11SSH-TF mainboard model

        ```bash
        export CONFIG_NAME=config.supermicro_x11ssh_<model>
        ```

     * Make sure build environment is clean:

        ```bash
        make distclean
        ```

    * To build `Dasharo (coreboot+UEFI) v0.1.0`

      ```bash
       cp configs/$CONFIG_NAME .config
      ```

    * To build `Dasharo (coreboot+UEFI) v0.1.0` debug version (very verbose logging).

      ```bash
       cp configs/$CONFIG_NAME.debug .config
      ```

      ```bash
      make olddefconfig
      ```

      ```bash
      make
      ```

    or simply:

      ```bash
      make distclean && cp configs/$CONFIG_NAME .config && make olddefconfig && make
      ```

This will produce a Dasharo binary placed in `build/coreboot.rom`, which can be
flashed in following ways, depending on your situation:

* To flash Dasharo first time refer to [initial deployment manual](initial-deployment.md).
* To update Dashro refer [firmware update](firmware-update.md).
