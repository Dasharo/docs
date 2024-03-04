# Building manual

## Requirements

- Docker - you will need Docker packages from Docker's own repository
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git
    + `sudo apt-get install git`

## Building

To build Dasharo firmware image, follow the steps below:

1. Clone the coreboot repository:

    ```bash
    git clone https://github.com/Dasharo/coreboot.git -b protectli_vault_kbl/release
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
