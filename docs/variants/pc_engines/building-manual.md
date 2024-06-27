# Building manual

## Intro

This document describes the procedure for compiling Dasharo for PC Engines
apu2/3/4/6 platform.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git

## Build Dasharo firmware

=== "(coreboot+UEFI) firmware"

    1. Clone the coreboot repository:

        ```bash
        git clone https://github.com/Dasharo/coreboot
        ```

    2. Checkout the desired version:

        > Replace VERSION with desired version number, e.g. `v0.9.0`:
        > `git checkout pcengines_apu2_v0.9.0`

        ```bash
        cd coreboot
        git checkout pcengines_apu2_VERSION
        ```

    3. Checkout submodules:

        ```bash
        git submodule update --init --checkout
        ```

    4. Build the firmware:

        > Replace X with correct apu platform, e.g. 2, 3, 4, 6 (apu5 is not
        > supported by UEFI builds).

         ```bash
         ./build.sh apuX
         ```

    The resulting coreboot image will be placed in the coreboot directory as
    `pcengines_apuX_v0.9.rom`, `protectli_V1410.rom` or `protectli_V1610.rom`
    respectvely.

=== "(coreboot+SeaBIOS) firmware"

    This release is built using the Dasharo Patchqueue Initiative, which is a proof
    of concept of a new approach to Dasharo coreboot downstream maintenance. Please
    follow the [dasharo-pq](https://github.com/Dasharo/dasharo-pq/) and
    [pce-fw-builder](https://github.com/pcengines/pce-fw-builder) documentation to
    build the release version of Dasharo (coreboot+SeaBIOS) for PC Engines
    apu2/3/4/6.
