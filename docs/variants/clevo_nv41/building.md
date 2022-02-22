# coreboot building

## Intro

This documents describes the procedure for compiling coreboot for Clevo NV41MZ.

## Requirements

- Docker
  - follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
  - follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git

## Procedure

The easiest way to build coreboot is to use the official Docker image.

Obtain the image:

```bash
$ docker pull coreboot/coreboot-sdk:0ad5fbd48d
```

Obtain coreboot source code for Clevo NV41:

```bash
$ git clone https://github.com/Dasharo/coreboot.git
```

Navigate to the source code directory and checkout to the desired revision:

> Replace the REVISION with one of the:
> - `clevo_nv41mz/release` for the latest released version
> - `clevo_nv41mz/vVERSION` (e.g. `v0.1.1`) for the given release

```bash
$ cd coreboot
$ git checkout REVISION
$ git submodule update --init --recursive --checkout
```

Enter the Docker container:

```bash
$ docker run -u $UID --rm -it -v $PWD:/home/coreboot/coreboot -w /home/coreboot/coreboot \
    coreboot/coreboot-sdk:0ad5fbd48d /bin/bash
```

*Warning: Do not run `docker` as root. This command should be executed as your
current user. If you're having trouble running `docker` on your user account,
follow the steps outlined in [Requirements](#requirements).*

You should be inside the Docker container. Now run following script to build
the image:

```bash
$ ./build.sh build
```

The resulting coreboot image will be placed in
`artifacts/dasharo_clevo_nv41mz_VERSION.rom`.
