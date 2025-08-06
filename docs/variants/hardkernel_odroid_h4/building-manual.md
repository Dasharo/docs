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
git clone https://github.com/Dasharo/slimbootloader.git
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

2. Build UEFI Payload and Slim BootLoader

    ```sh
    ./build.sh odroid_h4
    ```

!!! note

    If you wish to build Slim Bootloader with your own keys, run
    `SBL_KEY_DIR=<path_to_keys> ./build.sh odroid_h4` instead, where the
    `<path_to_keys>` is the path to the directory with keys generated with
    `python BootloaderCorePkg\Tools\GenerateKeys.py -k <path_to_keys>` from the
    clone Slim Bootloader directory. `<path_to_keys>` may be an absolute path
    or path relative to Slim Bootloader repository directory.

The resulting Slim Bootloader image will be placed in the Slim Bootloader
directory as `Outputs/odroid_h4/ifwi-release.bin`.
