# Dasharo (UEFI) v0.1.0 for QEMU Q35 - Building Manual

Follow below steps to create the "Dasharo (UEFI) OVMF image for QEMU Q35" from EDK2:

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)

## Procedure

Easiest way to build OVMF for QEMU Q35 is to use coreboot Docker image.
As some dependencies maybe missing in given local instance.

Obtain the docker image:

```bash
docker pull coreboot/coreboot-sdk:2021-09-23_b0d87f753c
```

Clone official Dasharo EDK2 repository to your docker instance,
with git or downloading the source code from github.

```bash
git clone https://github.com/Dasharo/edk2.git
```

Start the instance of the docker image under the Dasharo/edk2 repository:

```bash
sudo docker run --rm -it -v $PWD:/home/coreboot/coreboot \
    -w /home/coreboot/coreboot coreboot/coreboot-sdk:2021-09-23_b0d87f753c \
    /bin/bash
```

Follow below instructions, to prepare your environment for building OVMF
image.

- Setup the environment variables with the following command

```bash
make -C BaseTools
source edksetup.sh
```

- Update the submodules in order get latest dependencies.

```bash
git submodule update --init --checkout
```

- Clone the edk2-platforms repository for additional packages

```bash
git clone https://github.com/Dasharo/edk2-platforms.git && \
cd edk2-platforms && \
git checkout 3323ed481d35096fb6a7eae7b49f35eff00f86cf && \
cd -
```

- Update the PACKAGES_PATH variable

```bash
export EDK2_PLATFORMS_PATH="$WORKSPACE/edk2-platforms"
export PACKAGES_PATH="$WORKSPACE:\
$EDK2_PLATFORMS_PATH/Platform/Intel:\
$EDK2_PLATFORMS_PATH/Silicon/Intel:\
$EDK2_PLATFORMS_PATH/Features/Intel:\
$EDK2_PLATFORMS_PATH/Features/Intel/Debugging:\
$EDK2_PLATFORMS_PATH/Features/Intel/Network:\
$EDK2_PLATFORMS_PATH/Features/Intel/OutOfBandManagement:\
$EDK2_PLATFORMS_PATH/Features/Intel/PowerManagement:\
$EDK2_PLATFORMS_PATH/Features/Intel/SystemInformation:\
$EDK2_PLATFORMS_PATH/Features/Intel/UserInterface"
```

## Building the firmware image

To build the image simply invoke the following command

```bash
build -a IA32 -a X64 -t GCC5 -b RELEASE -p OvmfPkg/OvmfPkgX64.dsc
```

You can also enable additional options, for example CSM with by adding
`-D CSM_ENABLE`:

```bash
build -a IA32 -a X64 -t GCC5 -b RELEASE -p OvmfPkg/OvmfPkgX64.dsc -D CSM_ENABLE
```

Once the build is completed, the OVMF firmware image can be found below given
path:

```bash
edk2/Build/Ovmfx64/RELEASE_GCC5/FV/OVMF_CODE.fd
edk2/Build/Ovmfx64/RELEASE_GCC5/FV/OVMF_VARS.fd
```

For debug build use:

```bash
build -a IA32 -a X64 -t GCC5 -b DEBUG -p OvmfPkg/OvmfPkgX64.dsc
```

Then the resulting files will be placed in:

```bash
edk2/Build/Ovmfx64/DEBUG_GCC5/FV/OVMF_CODE.fd
edk2/Build/Ovmfx64/DEBUG_GCC5/FV/OVMF_VARS.fd
```
