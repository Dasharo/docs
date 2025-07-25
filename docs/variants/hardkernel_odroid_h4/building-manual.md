# Dasharo firmware building guide

## Intro

This guide shows how to build Dasharo firmware for Hardkernel devices.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git
    + `sudo apt-get install git`

## Building

To build Dasharo (coreboot+UEFI) firmware image, first clone the coreboot repository:

```bash
git clone https://github.com/Dasharo/coreboot.git
```

then follow the steps below:

1. To build a specific version checkout to the version's tag.
    Skip this step otherwise.

    ```bash
    cd coreboot
    git checkout hardkernel_odroid_h4_<version>
    ```

    For example

    ```bash
    git checkout hardkernel_odroid_h4_v0.9.0
    ```

2. Checkout submodules:

    ```bash
    git submodule update --init --checkout
    ```

3. Build the firmware:

    ```bash
    ./build.sh odroid_h4
    ```

    The resulting coreboot image will be placed in the coreboot directory as
    `hardkernel_odroid_h4_<version>.rom`.

## Building Slim Bootloader

To build Dasharo (Slim Bootloader + UEFI) firmware image, first clone and enter
Slim Bootloader repository:

```bash
git clone https://github.com/Dasharo/slimbootloader.git -b odroid_h4_support
cd slimbootloader
```

then follow the steps below:

1. To build a specific version, checkout to the version's tag.
    Skip this step otherwise.

    ```bash
    git checkout hardkernel_odroid_h4_<version>
    ```

    For example

    ```bash
    git checkout hardkernel_odroid_h4_v0.9.0
    ```

2. Checkout submodules:

    ```bash
    git submodule update --init --checkout --recursive
    ```

3. Copy vendor image to this repository. IDF and ME regions will be taken from
   this image when stitching loader

    ```sh
    cp /path/to/ADLN-H4_B1.08/ADLN-H4_B1.08.bin image.rom
    ```

    or

    ```sh
    cp /path/to/hardkernel_odroid_h4_v0.9.0.rom image.rom
    ```

    You can skip this step and pass path to this image via `INPUT_IMAGE` variable
    instead

4. Build UEFI Payload and Slim BootLoader

    ```sh
    ./build.sh odroid_h4
    ```

    You can also pass path to vendor image via `INPUT_IMAGE` variable

    ```sh
    INPUT_IMAGE=~/Downloads/hardkernel_odroid_h4_v0.9.0.rom ./build.sh odroid_h4
    ```

    The resulting Slim Bootloader image will be placed in the Slim Bootloader
    directory as `Outputs/odroidh4/ifwi-release.bin`.

    > The UEFI payload has almost no features enabled. Passing the following
    > additional arguments: `-D VARIABLE_SUPPORT=SPI -D SECURE_BOOT_ENABLE=TRUE`
    > `-D SMM_SUPPORT=TRUE -D CRYPTO_PROTOCOL_SUPPORT=TRUE` to enable variable
    > and Secure Boot support results in a hang in the payload.
