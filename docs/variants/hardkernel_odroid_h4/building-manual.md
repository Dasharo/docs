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

## Slim Bootloader

### Building UEFI Payload

To build Dasharo (Slim Bootloader + UEFI) firmware image, first clone the EDK2
repository to build UEFI Payload (Universal Payload variant):

```bash
git clone https://github.com/tianocore/edk2.git
```

1. Checkout latest stable version and submodule:

    ```bash
    cd edk2
    git checkout edk2-stable202505\
    git submodule update --init --checkout --recursive
    ```

2. Prepare build environment:

    ```bash
    source edk_setup.sh
    make -C BaseTools
    ```

3. Build the payload:

    ```bash
    python ./UefiPayloadPkg/UniversalPayloadBuild.py -t GCC5 -o Dasharo \
        -D CRYPTO_PROTOCOL_SUPPORT=TRUE -D SIO_BUS_ENABLE=TRUE \
        -D PERFORMANCE_MEASUREMENT_ENABLE=TRUE \
        -D MULTIPLE_DEBUG_PORT_SUPPORT=TRUE -D BOOTSPLASH_IMAGE=TRUE \
        -D BOOT_MANAGER_ESCAPE=TRUE -b RELEASE
    ```

> The payload has almost no features enabled. Passing the following additional
> arguments: `-D VARIABLE_SUPPORT=SPI -D SECURE_BOOT_ENABLE=TRUE`
> `-D SMM_SUPPORT=TRUE -D CRYPTO_PROTOCOL_SUPPORT=TRUE` to enable variable and
> Secure Boot support results in a hang in the payload.

### Building Slim Bootloader

When the payload is built, proceed with cloning Slim Bootloader repository:

```bash
git clone https://github.com/Dasahro/slimbootloader.git -b odroid_h4_support
```

then follow the steps below:

1. To build a specific version checkout to the version's tag.
    Skip this step otherwise.

    ```bash
    cd cd slimbootloader
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

3. Copy the UEFI Payload:

    ```bash
    mkdir -p PayloadPkg/PayloadBins/
    cp path/to/edk2/Build/UefiPayloadPkgX64/UniversalPayload.elf PayloadPkg/PayloadBins/
    ```

4. Generate keys (do it only once):

    ```bash
    export SBL_KEY_DIR=${PWD}/SblKeys
    python BootloaderCorePkg/Tools/GenerateKeys.py -k $SBL_KEY_DIR
    ```

5. Start Slim Bootloader build:

    ```bash
    python BuildLoader.py build odroidh4 -r \
        -p "OsLoader.efi:LLDR:Lz4;UniversalPayload.elf:UEFI:Lzma"
    ```

6. Stitch the loader with IFD and ME from vendor image:

    ```bash
    python Platform/AlderlakeBoardPkg/Script/StitchLoader.py \
        -i path/to/ADLN-H4_B1.08/ADLN-H4_B1.08.bin \
        -s Outputs/odroidh4/SlimBootloader.bin \
        -o Outputs/odroidh4/ifwi-release.bin \
        -p 0xAAFFFF0C
    ```

    OR from Dasharo image:

    ```bash
    python Platform/AlderlakeBoardPkg/Script/StitchLoader.py \
        -i path/to/hardkernel_odroid_h4_v0.9.0.rom \
        -s Outputs/odroidh4/SlimBootloader.bin \
        -o Outputs/odroidh4/ifwi-release.bin \
        -p 0xAAFFFF0C
    ```

    The resulting Slim Bootloader image will be placed in the Slim Bootloader
    directory as `Outputs/odroidh4/ifwi-release.bin`.
