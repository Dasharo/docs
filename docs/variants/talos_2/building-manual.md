# Buidling coreboot image

In order to build coreboot image, follow the steps below:

1. Clone the coreboot repository:

   ```
   git clone git@github.com:Dasharo/coreboot.git -b talos_2_support_ramstage
   # or HTTPS alternatively
   git clone git@github.com:Dasharo/coreboot.git -b talos_2_support_ramstage
   ```

    master - follows upstream project master branch
    raptor-cs_talos-2/release - contains all code releases for given <platform>, list of supported platforms is in Hardware Compatibility List section
    raptor-cs_talos-2/rel_vX.Y.Z - release branch for version X.Y.Z
    raptor-cs_talos-2/develop - contains most recent development and is periodically synced with master branch
    raptor-cs_talos-2/<feature> - tracks development of platform specific feature


2. Get the submodules:

   ```
   cd coreboot
   git submodule update --init --checkout
   ```

3. Start docker container (assuming you are already in coreboot root
   directory):

   ```
   docker run --rm -it -v $PWD:/home/coreboot/coreboot -w /home/coreboot/coreboot 3mdeb/coreboot-sdk:mkimage /bin/bash
   ```

4. When inside of the container, configure the build for Talos II:

   ```
   cp configs/config.raptor-cs-talos-2 .config
   make olddefconfig
   ```

5. Start the build process of coreboot inside the container:

   ```
   make
   ```
