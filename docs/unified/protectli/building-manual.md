# Building manual

## Intro

This document describes the procedure for building coreboot for all Protectli
devices.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git
    + `sudo apt-get install git`

Alternatively Fedora can be used instead of Ubuntu by following the same steps except:
[Install Docker Engine on Fedora](https://docs.docker.com/engine/install/fedora/)

## Building

To build Dasharo firmware image, first clone the coreboot repository:
    ```bash
    git clone https://github.com/Dasharo/coreboot.git
    ```
then follow the steps below:

=== "FW6"

    1. Checkout to the device's branch:
        ```bash
        cd coreboot
        git checkout protectli_vault_kbl/release
        ```

    To build a specific version replace `protectli_vault_kbl/release` to
    `protectli_vault_kbl_v1.0.x` where `x` is the version number.

    2. Start build process (note it requires certain blobs to proceed):

        ```bash
        cd coreboot
        git submodule update --init --checkout
        # you will need to obtain the ZIP with blobs at this point
        unzip protectli_blobs.zip -d 3rdparty/blobs/mainboard
        ./build.sh fw6
        ```

=== "V1000-series"

    1. Checkout the desired version, e.g. `v0.9.3`:

        ```bash
        cd coreboot
        git checkout protectli_vault_jsl_v0.9.3
        ```

    2. Checkout submodules:

        ```bash
        git submodule update --init --checkout
        ```

    3. Obtain the Protectli blobs package (only for versions v0.9.0 and v0.9.1):

        > Replace `<PROTECTLI_BLOBS_REPO>` with a a proper path to the repository
        > in a form of: `git@repo-path.git`. You should checkout to the same tag as
        > in case of the coreboot repository.

        ```bash
        cd 3rdparty/blobs/mainboard/
        git init
        git remote add origin <PROTECTLI_BLOBS_REPO>
        git fetch origin && git checkout protectli_vault_jsl_v0.9.0
        cd -
        ```

    4. Build the firmware:

        + for V1210

            ```bash
            ./build.sh V1210
            ```

        + for V1211

            ```bash
            ./build.sh V1211
            ```

        + for V1410

            ```bash
            ./build.sh V1410
            ```

        + for V1610

            ```bash
            ./build.sh V1610
            ```

    The resulting coreboot image will be placed in the coreboot directory as
    `protectli_V1210.rom`, `protectli_V1410.rom` or `protectli_V1610.rom`
    respectvely.

=== "VP4630/VP4650/VP4670"

    Since version v1.0.18 VP4630 and VP4650 use different configuration file than
    VP4670. Versions v1.0.17 and older do not support VP4650 and VP4670 at all.

    Versions v1.1.1 and newer support all variants with a single binary.

    1. Checkout the desired version, e.g. `v1.1.0`:

        ```bash
        cd coreboot
        git checkout protectli_vault_cml_v1.1.0
        ```

    2. Checkout submodules:

        ```bash
        git submodule update --init --checkout
        ```

    3. Obtain the Protectli blobs package (only for version v1.1.0 and older):

        > Replace `<PROTECTLI_BLOBS_REPO>` with a a proper path to the repository
        > in a form of: `git@repo-path.git`. You should checkout to the same tag as
        > in case of the coreboot repository.

        ```bash
        cd 3rdparty/blobs/mainboard/
        git init
        git remote add origin <PROTECTLI_BLOBS_REPO>
        git fetch origin && git checkout protectli_vault_cml_v1.1.0
        cd -
        ```

    4. Build the firmware:

        === "v1.1.1 or newer"

            ```bash
            ./build.sh vp46xx
            ```

            The resulting coreboot image will be placed in the coreboot directory as
            `protectli_vault_cml_<version>_vp46xx.rom`.

        === "V1.1.0 or older"

            === "VP4630 and VP4650"

                ```bash
                ./build.sh vp4630_vp4650
                ```

                The resulting coreboot image will be placed in the coreboot
                directory as `protectli_vault_cml_<version>_vp4630_vp4650.rom`.

            === "VP4670"

                ```bash
                ./build.sh vp4670
                ```

                The resulting coreboot image will be placed in the coreboot
                directory as `protectli_vault_cml_<version>_vp4670.rom`.

=== "VP6630/VP6650/VP6670"

    1. Checkout the desired version, e.g. `v0.9.0`:

        ```bash
        cd coreboot
        git checkout protectli_vault_adl_v0.9.0
        ```

    2. Checkout submodules:

        ```bash
        git submodule update --init --checkout
        ```

    3. Build the firmware:

        ```bash
        ./build.sh vp66xx
        ```

    The resulting coreboot image will be placed in the coreboot directory as
    `protectli_vp66xx.rom`.

=== "VP2410"

    1. Checkout the desired version, e.g. `v1.0.15`:

        ```bash
        cd coreboot
        git checkout protectli_vault_glk_v1.0.15
        ```

    2. Checkout submodules:

        ```bash
        git submodule update --init --checkout
        ```

    3. Obtain the Protectli blobs package (only for v1.0.15 or older):

        > Replace `<PROTECTLI_BLOBS_REPO>` with a a proper path to the repository
        > in a form of: `git@repo-path.git`. You should checkout to the same tag as
        > in case of the coreboot repository.

        ```bash
        cd 3rdparty/blobs/mainboard/
        git init
        git remote add origin <PROTECTLI_BLOBS_REPO>
        git fetch origin && git checkout protectli_vault_glk_v1.0.15
        cd -
        ln -s ../blobs/mainboard/protectli/vault_glk/GeminilakeFspBinPkg/ 3rdparty/fsp/GeminilakeFspBinPkg
        ```

    4. Build the firmware:

        ```bash
        ./build.sh vp2410
        ```

    The resulting coreboot image will be placed in the coreboot directory as
    `protectli_vp2410_<version>.rom`.

=== "VP2420"

    1. Checkout the desired version, e.g. `v1.1.0`:

        ```bash
        cd coreboot
        git checkout protectli_vault_ehl_v1.1.0
        ```

    2. Checkout submodules:

        ```bash
        git submodule update --init --checkout
        ```

    3. Obtain the Protectli blobs package (only v1.1.0 or older):

        > Replace `<PROTECTLI_BLOBS_REPO>` with a a proper path to the repository
        > in a form of: `git@repo-path.git`. You should checkout to the same tag as
        > in case of the coreboot repository.

        ```bash
        cd 3rdparty/blobs/mainboard/
        git init
        git remote add origin <PROTECTLI_BLOBS_REPO>
        git fetch origin && git checkout protectli_vault_ehl_v1.1.0
        cd -
        ```

    4. Build the firmware:

        ```bash
        ./build.sh vp2420
        ```

    The resulting coreboot image will be placed in the coreboot directory as
    `protectli_vp2420_<version>.rom`.

=== "VP2430"

    1. Checkout the desired version, e.g. `v0.9.0`:

        ```bash
        cd coreboot
        git checkout protectli_vp2430_v0.9.0
        ```

    2. Checkout submodules:

        ```bash
        git submodule update --init --checkout
        ```

    3. Build the firmware:

        ```bash
        ./build.sh vp2430
        ```

    The resulting coreboot image will be placed in the coreboot directory as
    `protectli_vp2430_<version>.rom`.

=== "VP3210/VP3230"

    1. Checkout the desired version, e.g. `v0.9.0`:

        ```bash
        cd coreboot
        git checkout protectli_vault_adln_v0.9.0
        ```

    2. Checkout submodules:

        ```bash
        git submodule update --init --checkout
        ```

    3. Build the firmware:

        ```bash
        ./build.sh vp32xx
        ```

    The resulting coreboot image will be placed in the coreboot directory as
    `protectli_vp32xx_<version>.rom`.

=== "VP2440"

    1. Checkout the desired version, e.g. `v0.9.0`:

        ```bash
        cd coreboot
        git checkout protectli_vp2440_v0.9.0
        ```

    2. Checkout submodules:

        ```bash
        git submodule update --init --checkout
        ```

    3. Build the firmware:

        ```bash
        ./build.sh vp2440
        ```

    The resulting coreboot image will be placed in the coreboot directory as
    `protectli_vp2440_<version>.rom`.
