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
sudo docker run --rm -it -v $PWD:/home/coreboot/coreboot -w /home/coreboot/coreboot -u root coreboot/coreboot-sdk:2021-09-23_b0d87f753c /bin/bash
```

1. Follow below instructions, to prepare your environment for building OVMF image.

- Setup the environment variables with the following command -

```bash
make -C BaseTools

source edksetup.sh
```

- Update the submodules in order get latest dependencies.
And avoid any build process errors while building the OVMF image.

```bash
git submodules update --init
```

## Building the firmware image

1. To build firmware image with required features set the flags with **TRUE/FLASE**.
Following is an example of SMM feature enabled,
`DEFINE SMM_REQUIRE = TRUE` in the **OvmfPkgX64.dsc** file.

 Check the following build command:

```bash
build -a IA32 -a X64 -t GCC5 -b RELEASE -p OvmfPkg/OvmfPkgX64.dsc
```

- Once the build is completed, the OVMF firmware image can be found below given path:

```bash
edk2/Build/Ovmf/DEBUG_GCC5/FV/OVMF_CODE.fd
edk2/Build/Ovmf/DEBUG_GCC5/FV/OVMF_VARS.fd
```
