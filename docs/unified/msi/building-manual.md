# Building manual

=== "Dasharo (UEFI)"

    ## Intro

    This documents describes the procedure for compiling Dasharo firmware
    compatible with MSI PRO Z690-A and MSI PRO Z790-P.

    ## Requirements

    * `Ubuntu 20.04/21.04/22.04` as a host OS was tested
    * Internet connection
    * Docker installed
        - follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
        - follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
    * Git, wget, unzip installed

    ```bash
    sudo apt install git unzip wget
    ```

    * UEFIExtract installed
        - this tool is used in the `build.sh` script to extract CPU microcode from
          the original MSI firmware

    ```bash
    sudo apt install wget
    wget https://github.com/LongSoft/UEFITool/releases/download/A59/UEFIExtract_NE_A59_linux_x86_64.zip
    unzip UEFIExtract_NE_A59_linux_x86_64.zip
    sudo cp ./UEFIExtract /usr/local/bin
    ```

    ## Procedure

    Obtain Dasharo source code:

    === "PRO Z690-A (WIFI) DDR4"
        > Replace the `REVISION` with one of the:
        >
        > - `msi_ms7d25_vVERSION` tag for the given release `VERSION`
        >   (e.g. `msi_ms7d25_v1.1.3`), **RECOMMENDED**
        > - `dasharo` branch for a development version with unreleased changes past
        >   most recent release version
        > - `msi_ms7d25/release` branch for the release versions up to v1.1.2

    === "PRO Z690-A (WIFI)"
        > Replace the `REVISION` with one of the:
        >
        > - `msi_ms7d25_vVERSION` tag for the given release `VERSION`
        >   (e.g. `msi_ms7d25_v1.1.3`), **RECOMMENDED**
        > - `dasharo` branch for a development version with unreleased changes past
        >   most recent release version
        > - `msi_ms7d25/release` branch for the release versions up to v1.1.2

    === "PRO Z790-P (WIFI) DDR4"
        > Replace the `REVISION` with one of the:
        >
        > - `msi_ms7e06_vVERSION` tag for the given release `VERSION`
        >   (e.g. `msi_ms7e06_v0.9.1`), **RECOMMENDED**
        > - `dasharo` branch for a development version with unreleased changes past
        >   most recent release version
        > - `msi_ms7d25/release` branch for the release versions up to v0.9.0

    === "PRO Z790-P (WIFI)"
        > Replace the `REVISION` with one of the:
        >
        > - `msi_ms7e06_vVERSION` tag for the given release `VERSION`
        >   (e.g. `msi_ms7e06_v0.9.1`), **RECOMMENDED**
        > - `dasharo` branch for a development version with unreleased changes past
        >   most recent release version
        > - `msi_ms7d25/release` branch for the release versions up to v0.9.0

    ```bash
    git clone https://github.com/Dasharo/coreboot.git -b REVISION
    cd coreboot
    ```

    Start the build process:

    === "PRO Z690-A (WIFI) DDR4"
        For v1.1.1 and older:

        ```bash
        ./build.sh ddr4
        ```

        For v1.1.2 and newer:

        ```bash
        ./build.sh z690a_ddr4
        ```

        The resulting Dasharo firmware image will be placed at `$PWD/msi_ms7d25_VERSION_ddr4.rom`.

    === "PRO Z690-A (WIFI)"
        For v1.1.1 and older:

        ```bash
        ./build.sh ddr5
        ```

        For v1.1.2 and newer:

        ```bash
        ./build.sh z690a_ddr5
        ```

        The resulting Dasharo firmware image will be placed at `$PWD/msi_ms7d25_VERSION_ddr5.rom`.

    === "PRO Z790-P (WIFI) DDR4"
        ```bash
        ./build.sh z790p_ddr4
        ```

        The resulting Dasharo firmware image will be placed at `$PWD/msi_ms7e06_VERSION_ddr4.rom`.

    === "PRO Z790-P (WIFI)"
        ```bash
        ./build.sh z790p_ddr5
        ```

        The resulting Dasharo firmware image will be placed at `$PWD/msi_ms7e06_VERSION_ddr4.rom`.

=== "Dasharo (coreboot + Heads)"

    # Intro

    This section presents the crucial steps required to build the Dasharo Heads
    firmware. For more information, you may also refer to the official
    [Heads building documentation](https://osresearch.net/general-building/).

    ## Requirements

    This guide was verified on Ubuntu 22.04. In practice, any Linux distribution
    with [Docker](https://www.docker.com/) support should be enough to complete it.

    Make sure that you have following packages installed:

    - Docker
        + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
        + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
    - Git

        ```bash
        sudo apt -y install git
        ```

    ## Building

    1. Clone Dasharo Heads repository

        ```bash
         git clone https://github.com/Dasharo/heads.git
        ```

    2. Navigate to the source code directory and checkout to the desired revision:

    === "PRO Z690-A"

        ```bash
        cd heads
        git checkout msi_ms7d25_v0.9.0
        ```

    === "PRO Z790-P"

        ```bash
        cd heads
        git checkout msi_ms7e06_v0.9.0
        ```

    3. Start docker container:

        ```bash
        docker run --rm -it -v $PWD:$PWD -w $PWD \
          3mdeb/heads-docker:3.0.0 /bin/bash
        ```

    4. Inside of the container, start the build process:

    === "PRO Z690-A (WIFI) DDR4"

        ```bash
        BOARD=msi_z690a_ddr4 make
        ```

        This will produce a Dasharo binary placed in
        `build/x86/msi_z690a_ddr4/dasharo-msi_z690a_ddr4-*.rom`.

    === "PRO Z690-A (WIFI)"

        ```bash
        BOARD=msi_z690a_ddr5 make
        ```

        This will produce a Dasharo binary placed in
        `build/x86/msi_z690a_ddr5/dasharo-msi_z690a_ddr5-*.rom`.

    === "PRO Z790-P (WIFI) DDR4"

        ```bash
        BOARD=msi_z790p_ddr4 make
        ```

        This will produce a Dasharo binary placed in
        `build/x86/msi_z790p_ddr4/dasharo-msi_z790p_ddr4-*.rom`.

    === "PRO Z790-P (WIFI)"

        ```bash
        BOARD=msi_z790p_ddr5 make
        ```

        This will produce a Dasharo binary placed in
        `build/x86/msi_z790p_ddr5/dasharo-msi_z790p_ddr5-*.rom`.
