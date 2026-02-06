# Building

We choose [Yocto Project](https://www.yoctoproject.org/) to prepare Dasharo
Tools Suite system. DTS image can be built using publicly available sources.
Thanks to publishing the build cache on
[cache.dasharo.com](https://cache.dasharo.com/yocto/dts/) the time needed to
finish the process should be significantly decreased.

## Prerequisites

The following must be met to build DTS:

* Linux PC (tested on `Ubuntu 20.04 LTS`),
* [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) installed,
* [kas-container 4.2](https://raw.githubusercontent.com/siemens/kas/4.2/kas-container)
  script downloaded and available in [PATH](https://en.wikipedia.org/wiki/PATH_(variable)),

```bash
wget -O ~/bin/kas-container https://raw.githubusercontent.com/siemens/kas/4.2/kas-container
```

```bash
chmod +x ~/bin/kas-container
```

* `meta-dts` repository cloned.

```bash
mkdir yocto && cd yocto
```

```bash
git clone https://github.com/Dasharo/meta-dts.git
```

## Build

From `yocto` directory, run:

```shell
SHELL=/bin/bash kas-container build meta-dts/kas.yml
```

Image build takes time, so be patient, and the build's finished, you should see
something similar to (tasks number may differ):

```shell
Initialising tasks: 100% |###########################################################################################| Time: 0:00:01
Sstate summary: Wanted 2 Found 0 Missed 2 Current 931 (0% match, 99% complete)
NOTE: Executing Tasks
NOTE: Tasks Summary: Attempted 2532 tasks of which 2524 didn't need to be rerun and all succeeded.
```

Using the cache is enabled in `kas/cache.yml` file and can be disabled by
removing content of that file.

```bash
cat kas/cache.yml
```

output:

```bash
---
header:
  version: 11

local_conf_header:
  yocto-cache: |
    SSTATE_MIRRORS ?= "file://.* http://${LOCAL_PREMIRROR_SERVER}/${PROJECT_NAME}/sstate-cache/PATH"
    SOURCE_MIRROR_URL ?= "http://${LOCAL_PREMIRROR_SERVER}/${PROJECT_NAME}/downloads"
    INHERIT += "own-mirrors"
    LOCAL_PREMIRROR_SERVER ?= "cache.dasharo.com"
    PROJECT_NAME ?= "yocto/dts"
```

### Build image with UEFI Secure Boot support

From `yocto` directory run:

```shell
SHELL=/bin/bash kas-container build meta-dts/kas-uefi-sb.yml
```

Image build takes time, so be patient and after build's finish you should see
something similar to (the exact tasks numbers may differ):

```shell
Initialising tasks: 100% |###########################################################################################| Time: 0:00:04
Checking sstate mirror object availability: 100% |###################################################################| Time: 0:00:03
Sstate summary: Wanted 892 Local 672 Mirrors 212 Missed 8 Current 1560 (99% match, 99% complete)
NOTE: Executing Tasks
NOTE: Tasks Summary: Attempted 5860 tasks of which 5841 didn't need to be rerun and all succeeded.
```

Image created with `kas-uefi-sb.yml` configuration file enable integration of
UEFI Secure Boot into DTS using
[meta-secure-core](https://github.com/jiazhang0/meta-secure-core/). Building the
image allow to prepare a PoC version with [uses sample
keys](https://github.com/jiazhang0/meta-secure-core/tree/master/meta-efi-secure-boot#sample-keys)
which by no mean should used in production. For user keys the script
[create-user-key-store.sh](https://github.com/jiazhang0/meta-secure-core/blob/master/meta-signing-key/scripts/create-user-key-store.sh)
can be used but it was not tested yet. Quick start with instructions on how to
use image are described in
[meta-efi-secure-boot](https://github.com/jiazhang0/meta-secure-core/tree/master/meta-efi-secure-boot#quick-start-for-the-first-boot).

## Flash

* Find out your device name.

```shell
fdisk -l
```

output:

```shell
(...)
Device     Boot  Start    End Sectors  Size Id Type
/dev/sdx1  *      8192 131433  123242 60,2M  c W95 FAT32 (LBA)
/dev/sdx2       139264 186667   47404 23,2M 83 Linux
```

In this case the device name is `/dev/sdx`, **but be aware, in the next steps,
replace `/dev/sdx` with the right device name on your platform, or else you can
damage your system!**

* From where you ran image build type.

```shell
sudo umount /dev/sdx*
```

```shell
cd build/tmp/deploy/images/genericx86-64
```

Here the file `dts-base-image-genericx86-64.wic.gz` should be available, which
is the image of DTS. To flash image, you can use the same command shown in
[running section](#launching-dts_1). Just change the file name.

* Boot the platform.
