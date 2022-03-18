# Updating firmware using fwupd

This document describes the process of installing firmware updates from LVFS
using fwupd.

## Installing fwupd

### Using binary packages

Only `.deb` packages are provided. The procudure was verified on `Ubuntu 20.04
LTS`, but is should also apply to other Debian-based dsitributions. If you are
using different distribution, you might need to
[build from source](#building-from-source).

1. Download and extract the fwupd archive:

```bash
$ wget --content-disposition \
     https://cloud.3mdeb.com/index.php/s/peqT6xsrCn5pzRk/download \
     https://cloud.3mdeb.com/index.php/s/TPKDpzedRi7sEJJ/download \
     https://cloud.3mdeb.com/index.php/s/C58L5c5RmbjKWWz/download
$ unzip fwupd-novacustom-v1.0.0.zip
```

1. This is an example how to verify the binaries (in this case `fwupd-novacustom-v1.0.0.zip`):

```bash
$ gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc
$ gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/oss_master_key/open-source-software/3mdeb-open-source-software-master-key.asc
$ gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/novacustom/novacustom-open-source-firmware-release-1.x-key.asc

$ sha256sum -c fwupd-novacustom-v1.0.0.zip.sha256
$ gpg -v --verify fwupd-novacustom-v1.0.0.zip.sha256.sig fwupd-novacustom-v1.0.0.zip.sha256
```

1. flashrom packages are located inside `flashrom-1.2-2-3mdeb.zip`:

```bash
$ unzip flashrom-1.2-2-3mdeb.zip
$ sudo apt install ./flashrom_1.2-2_amd64.deb
$ sudo apt install ./libflashrom1_1.2-2_amd64.deb
$ sudo apt install ./libflashrom-dev_1.2-2_amd64.deb
```

1. fwupd packages are located inside `fwupd-1.7.3-3mdeb.zip`:

```bash
$ unzip fwupd-1.7.3-3mdeb.zip
$ sudo apt install ./fwupd_1.7.3+r68+gf3a5e4d1_amd64.deb \
                   ./fwupd-doc_1.7.3+r68+gf3a5e4d1_all.deb \
                   ./fwupd-tests_1.7.3+r68+gf3a5e4d1_amd64.deb \
                   ./gir1.2-fwupd-2.0_1.7.3+r68+gf3a5e4d1_amd64.deb \
                   ./gir1.2-fwupdplugin-1.0_1.7.3+r68+gf3a5e4d1_amd64.deb \
                   ./gir1.2-gusb-1.0_0.3.5-1_amd64.deb \
                   ./libfwupd2_1.7.3+r68+gf3a5e4d1_amd64.deb \
                   ./libfwupd-dev_1.7.3+r68+gf3a5e4d1_amd64.deb \
                   ./libfwupdplugin4_1.7.3+r68+gf3a5e4d1_amd64.deb \
                   ./libfwupdplugin-dev_1.7.3+r68+gf3a5e4d1_amd64.deb \
                   ./libgusb2_0.3.5-1_amd64.deb \
                   ./libgusb-dev_0.3.5-1_amd64.deb
```

### Building from source

> There is no need to do any of these steps unless you can't use the packages
> provided in [the previous step](#using-binary-packages)
> You might need to adjust the package manager commands and package names to
> your distribution.

#### Flashrom

1. Install build dependencies:

```bash
$ sudo apt update
$ sudo apt install -y build-essential pciutils libpci-dev libusb-1.0-0-dev \
    cmake meson pkg-config libftdi1-dev debhelper git wget python3-markdown \
    gcab
```

1. Obtain source code:

```bash
$ git clone https://github.com/Dasharo/flashrom.git -b v1.2.0.1
$ cd flashrom
```

1. Build and install flashrom:

```bash
$ meson build
$ ninja -C build
$ sudo ninja -C build install
```

#### fwupd

1. Obtain source code:

```bash
$ git clone https://github.com/Dasharo/fwupd.git -b v1.7.3.1
$ cd fwupd
```

1. Install build dependencies:

```bash
$ ./contrib/setup
```

1. Build and install fwupd:

```bash
$ sudo depmod
$ meson build -Ddocs=none -Dplugin_flashrom=true
$ ninja -C build
$ sudo ninja -C build install
```

## Updating firmware from LVFS

1. Use the following command to update firmware with fwupd:

    _Note: You may be asked which device to update. If you see a prompt, select
    NV4XMB,ME,MZ_

```bash
$ sudo fwupdmgr update

Selected device: NV4XMB,ME,MZ
╔══════════════════════════════════════════════════════════════════════════════╗
║ Update NV4XMB,ME,MZ to 0.5.0?                                                ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ This release adds the following features:                                    ║
║                                                                              ║
║ • vboot Verified Boot                                                        ║
║ • TPM Measured Boot                                                          ║
║ • Custom fan curve                                                           ║
║ • Microcode for Tiger Lake stepping 0x2                                      ║
║                                                                              ║
║ This release changes the following features:                                 ║
║                                                                              ║
║ • Disabled unused DPTF device                                                ║
║                                                                              ║
║ NV4XMB,ME,MZ and all connected devices may not be usable while updating.     ║
╚══════════════════════════════════════════════════════════════════════════════╝

Perform operation? [Y|n]:
Downloading…             [***************************************]
Downloading…             [***************************************]
Decompressing…           [***************************************]
Decompressing…           [***************************************]
Authenticating…          [***************************************]
Authenticating…          [***************************************]
Restarting device…       [***************************************]
Writing…                 [***************************************]
Decompressing…           [***************************************]
Writing…                 [***************************************]
Verifying…               [***************************************]
Writing…                 [***************************************]
Restarting device…       [***************************************]
Waiting…                 [***************************************]
Successfully installed firmware

An update requires the system to shutdown to complete. Shutdown now? [y|N]:
```

1. Shut down the computer when prompted, or manually later on

2. Power on the laptop again
3. Log in and run the following command to verify results:

```bash
$ sudo fwupdmgr get-results

Choose a device:
0.	Cancel
1.	4bde70ba4e39b28f9eab1628f9dd6e6244c03027 (11th Gen Intel Core™ i7-1165G7 @ 2.80GHz)
2.	5792b48846ce271fab11c4a545f7a3df0d36e00a (Display controller)
3.	073c01931cb0e9889bbfb2ea4a4c2fc558805fc6 (Display controller)
4.	dbee8bd3b1ae0316ad143336155651eedb495a0e (NV4XMB,ME,MZ)
5.	71b677ca0f1bc2c5b804fa1d59e52064ce589293 (SSD 980 PRO 1TB)
6.	c6a80ac3a22083423992a3cb15018989f37834d6 (TPM)
7.	eefcbd318bd31fc1eba6358e628b3f9dceb87206 (USB4 host controller)
```

1. Select `NV4XMB,ME,MZ` when prompted, and the results will be displayed:

```bash
NV4XMB,ME,MZ:
  Device ID:            dbee8bd3b1ae0316ad143336155651eedb495a0e
  Previous version:     0.5.0
  Update State:         Success
  Last modified:        2022-01-13 11:09
  GUID:                 230c8b18-8d9b-53ec-838b-6cfc0383493a
  Device Flags:         • Internal device
                        • Updatable
                        • System requires external power source
                        • Needs shutdown after installation
                        • Cryptographic hash verification is available
```
