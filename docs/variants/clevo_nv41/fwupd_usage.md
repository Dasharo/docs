# Updating firmware using fwupd

This document describes the process of installing firmware updates from LVFS
using fwupd.

## Installing fwupd

### Using binary packages

Only `.deb` packages are provided. The procudure was verified on `Ubuntu 20.04
LTS`, but is should also apply to other Debian-based dsitributions. If you are
using different distribution, you might need to
[build from source](#building-form-source).

1. Download fwupd archive:
```bash
$ wget --content-disposition \
     https://cloud.3mdeb.com/index.php/s/peqT6xsrCn5pzRk/download \
     https://cloud.3mdeb.com/index.php/s/TPKDpzedRi7sEJJ \
     https://cloud.3mdeb.com/index.php/s/C58L5c5RmbjKWWz \
```

2. This is an example how to verify the binaries (in this case `fwupd-novacustom-v1.0.0.zip`):
```bash
$ gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc
$ gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/oss_master_key/open-source-software/3mdeb-open-source-software-master-key.asc
$ gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc

$ sha256sum -c fwupd-novacustom-v1.0.0.zip.sha256
$ gpg -v --verify fwupd-novacustom-v1.0.0.zip.sha256.sig fwupd-novacustom-v1.0.0.zip.sha256
```

3. flashrom packages are located inside `flashrom-1.2-2-3mdeb.zip`:
```bash
$ unzip flashrom-1.2-2-3mdeb.zip
$ sudo apt install ./flashrom_1.2-2_amd64.deb
$ sudo apt install ./libflashrom1_1.2-2_amd64.deb
$ sudo apt install ./libflashrom-dev_1.2-2_amd64.deb
```

4. fwupd packages are located inside `fwupd-1.7.3-3mdeb.zip`:
```bash
$ unzip fwupd-1.7.3-3mdeb.zip
$ sudo apt install ./fwupd_1.7.3+r68+gf3a5e4d1_amd64.deb
$ sudo apt install ./fwupd-doc_1.7.3+r68+gf3a5e4d1_all.deb
$ sudo apt install ./fwupd-tests_1.7.3+r68+gf3a5e4d1_amd64.deb
$ sudo apt install ./gir1.2-fwupd-2.0_1.7.3+r68+gf3a5e4d1_amd64.deb
$ sudo apt install ./gir1.2-fwupdplugin-1.0_1.7.3+r68+gf3a5e4d1_amd64.deb
$ sudo apt install ./gir1.2-gusb-1.0_0.3.5-1_amd64.deb
$ sudo apt install ./libfwupd2_1.7.3+r68+gf3a5e4d1_amd64.deb
$ sudo apt install ./libfwupd-dev_1.7.3+r68+gf3a5e4d1_amd64.deb
$ sudo apt install ./libfwupdplugin4_1.7.3+r68+gf3a5e4d1_amd64.deb
$ sudo apt install ./libfwupdplugin-dev_1.7.3+r68+gf3a5e4d1_amd64.deb
$ sudo apt install ./libgusb2_0.3.5-1_amd64.deb
$ sudo apt install ./libgusb-dev_0.3.5-1_amd64.deb
```

### Building from source

> You might need to adjust the package manager commands and package names to
> your distribution.

#### Preperation

1. Obtain source code of `flashrom` and `fwupd`:

```bash
$ git clone https://github.com/dasharo/flashrom -b TBD
$ git clone https://github.com/dasharo/fwupd -b TBD
```

2. Install build dependencies for flashrom:

```bash
$ sudo apt install -y build-essential pciutils libpci-dev libusb-1.0-0-dev \
    cmake meson pkg-config libftdi1-dev debhelper git wget python3-markdown \
    gcab
```

3. Install fwupd dependencies

```bash
$ cd fwupd
$ ./contrib/setup
```

#### Building

TBD

#### Installing
