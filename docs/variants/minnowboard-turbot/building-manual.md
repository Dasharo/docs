# Building manual

## Intro

This document describes the procedure for compiling coreboot compatible with
MinnowBoard Turbot.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git

## Build Dasharo BIOS firmware

1. Clone the coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot
    ```

2. Checkout the desired version, e.g. `v0.9.0`:

    ```bash
    cd coreboot
    git checkout intel_minnowmax_v0.9.0
    ```

3. Checkout submodules:

    ```bash
    git submodule update --init --checkout
    ```

4. Build the firmware:

    ```bash
    ./build.sh minnow_no_sb
    ```

The resulting coreboot image will be placed in the coreboot directory as
`intel_minnowmax_v0.9.0_no_sb.rom` or `intel_minnowmax_v0.9.0_sb.rom`
respectvely.
