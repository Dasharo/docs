# Dasharo firmware building guide

## Intro

This guide shows how to build Dasharo firmware compatible with ASRock Rack
SPC741D8-2L2T/BCM.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git
    + `sudo apt-get install git`

## Building

To build Dasharo (coreboot+UEFI) firmware image, first clone the coreboot
repository:

```bash
git clone https://github.com/Dasharo/coreboot.git
```

then follow the steps below:

1. To build a specific version checkout to the version's tag.
    Skip this step otherwise.

    ```bash
    cd coreboot
    git checkout asrock_spc741d8_<version>
    ```

    For example

    ```bash
    git checkout asrock_spc741d8_v0.9.0
    ```

2. Build the firmware:

    ```bash
    ./build.sh asrock_spc741d8
    ```

    The resulting coreboot image will be placed in the coreboot directory as
    `asrock_spc741d8_<version>.rom`.
