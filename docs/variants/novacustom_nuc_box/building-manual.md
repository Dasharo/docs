# Dasharo firmware building guide

## Intro

This guide shows how to build Dasharo firmware for the NovaCustom NUC BOX.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git
    + `sudo apt-get install git`

## Building

To build Dasharo firmware image, first clone the coreboot repository:

```bash
git clone https://github.com/Dasharo/coreboot.git
```

then follow the steps below:

1. To build a specific version checkout to the version's tag.
    Skip this step otherwise.

    ```bash
    cd coreboot
    git checkout novacustom_nuc_box<version>
    ```

    For example

    ```bash
    git checkout novacustom_nuc_box_v0.9.0
    ```

2. Checkout submodules:

    ```bash
    git submodule update --init --checkout
    ```

3. Build the firmware:

    ```bash
    ./build.sh novacustom_nuc_box
    ```

    The resulting coreboot image will be placed in the coreboot directory as
    `novacustom_nuc_box_<version>.rom`.
