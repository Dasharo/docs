# Dell OptiPlex 7010/9010 Dasharo - building manual

**Please read the [overview page](overview.md) first!**

## Available variants

To build Dasharo compatible with Dell OptiPlex 7010/9010, you need to decide
what is your desired configuration. The available options are as follows:

- Dasharo (coreboot + SeaBIOS)
- Dasharo (coreboot + edk2)
- Dasharo (coreboot + SeaBIOS) with
  [Intel TXT](https://doc.coreboot.org/security/intel/txt.html) support
- Dasharo (coreboot + edk2) with
  [Intel TXT](https://doc.coreboot.org/security/intel/txt.html) support

### Intel TXT

If your choice is to enable TXT support, be advised that there are proprietary
[ACM blobs](https://doc.coreboot.org/security/intel/acm.html) required for the
firmware to work properly. They are non-redistributable for the platform in
question, which means you will need to obtain/extract them yourself and patch
the result binary using `cbfstool`. The methods are covered later on in the
[initial deployment guide](initial-deployment.md#firmware-preparation)

    If in doubt, it is recommended to proceed with the non-TXT scenario.

## Building steps

1. Clone the coreboot repository:

    ```bash
    git clone https://github.com/dasharo/coreboot.git
    cd coreboot
    ```

    Replace `vX.Y.Z` with a valid version, eg. `v0.1.1`:

    ```bash
    git fetch --tags
    git checkout optiplex_7010_9010_vX.Y.Z
    ```

    Checkout submodules:

    ```bash
    git submodule update --init --recursive --checkout
    ```

1. Start a docker container:

     ```bash
    	docker run --rm -it \
    	   -v $PWD:/home/coreboot/coreboot \
    	   -w /home/coreboot/coreboot \
    	   coreboot/coreboot-sdk:2023-11-24_2731fa619b /bin/bash
     ```

1. Inside of the container, configure and start the build process:

    ```bash
    make distclean
    ```

    * To build `Dasharo (coreboot+SeaBIOS) v0.1.0`:

     ```bash
    	cp configs/config.dell_optiplex_9010_sff .config
     ```

    * To build `Dasharo (coreboot+UEFI) v0.1.0`:

     ```bash
    	cp configs/config.dell_optiplex_9010_sff_uefi .config
     ```

    * To build `Dasharo (coreboot+SeaBIOS) v0.1.0` **with TXT support**:

     ```bash
    	cp configs/config.dell_optiplex_9010_sff_txt .config
     ```

    * To build `Dasharo (coreboot+UEFI) v0.1.0` **with TXT support**:

     ```bash
    	cp configs/config.dell_optiplex_9010_sff_uefi_txt .config
     ```

    Finally, run:

    ```bash
    make olddefconfig
    make
    ```

    or simply:

    ```bash
    make distclean && cp configs/CONFIG_NAME .config && make olddefconfig && make
    ```

This will produce a Dasharo binary placed in `build/coreboot.rom`, which can be
flashed in following ways, depending on your situation:

- To flash Dasharo first time refer to [initial deployment manual](initial-deployment.md).
- To update Dashro refer to [firmware update](firmware-update.md).
