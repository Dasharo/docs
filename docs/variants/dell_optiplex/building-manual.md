# Dell OptiPlex 7010/9010 Dasharo - building manual

**Please read the [overview page](overview.md) first!**

## Available variants

To build Dasharo compatible with Dell OptiPlex 7010/9010, you need to decide
what is your desired configuration. The available options are as follows:

- Dasharo (coreboot + SeaBIOS)
- Dasharo (coreboot + edk2)
- Dasharo (coreboot + SeaBIOS) with
  [Intel TXT](https://doc.coreboot.org/security/intel/txt.html) support
- Dasharo (coreboot + edk2) with
  [Intel TXT](https://doc.coreboot.org/security/intel/txt.html) support

### Intel TXT

If your choice is to enable TXT support, be advised that there are proprietary
[ACM blobs](https://doc.coreboot.org/security/intel/acm.html) required for the
firmware to work properly. They are non-redistributable for the platform in
question, which means you will need to obtain/extract them yourself and patch
the result binary using `cbfstool`. The methods are covered below in the
[Include proprietary components](#include-proprietary-components) section.

    If in doubt, it is recommended to proceed with the non-TXT scenario.

## Building steps

1. Clone the coreboot repository:

    ```bash
    git clone https://github.com/dasharo/coreboot.git
    cd coreboot
    ```

    Replace `vX.Y.Z` with a valid version, eg. `v0.1.1`:

    ```bash
    git fetch --tags
    git checkout optiplex_7010_9010_vX.Y.Z
    ```

    Checkout submodules:

    ```bash
    git submodule update --init --recursive --checkout
    ```

1. Start a docker container:

     ```bash
    	docker run --rm -it \
    	   -v $PWD:/home/coreboot/coreboot \
    	   -w /home/coreboot/coreboot \
    	   coreboot/coreboot-sdk:2023-11-24_2731fa619b /bin/bash
     ```

1. Inside of the container, configure and start the build process:

    ```bash
    make distclean
    ```

    * To build `Dasharo (coreboot+SeaBIOS) v0.1.0`:

     ```bash
    	cp configs/config.dell_optiplex_9010_sff .config
     ```

    * To build `Dasharo (coreboot+UEFI) v0.1.0`:

     ```bash
    	cp configs/config.dell_optiplex_9010_sff_uefi .config
     ```

    * To build `Dasharo (coreboot+SeaBIOS) v0.1.0` **with TXT support**:

     ```bash
    	cp configs/config.dell_optiplex_9010_sff_txt .config
     ```

    * To build `Dasharo (coreboot+UEFI) v0.1.0` **with TXT support**:

     ```bash
    	cp configs/config.dell_optiplex_9010_sff_uefi_txt .config
     ```

    Finally, run:

    ```bash
    make olddefconfig
    make
    ```

    or simply:

    ```bash
    make distclean && cp configs/CONFIG_NAME .config && make olddefconfig && make
    ```

### Result

This will produce a Dasharo binary placed in `build/coreboot.rom`, which can
already be manually flashed ([initial](initial-deployment.md) or as [update](firmware-update.md)).
However for working fan control it's necessary to include the proprietary
Embedded Controller firmware and TXT support also needs [aforementioned](#intel-txt)
binary blobs.

!!! warning "Fan control"
    Without the proprietary EC firmware the fans will always run at full speed.

!!! warning "TXT support"
    Without the proprietary ACM files firmware with built-in TXT support will
    potentially refuse to start.

## Include proprietary components

To patch the Dasharo binary you need several tools. They are included in [DTS](../../dasharo-tools-suite/overview.md)
but must usually be installed on other distributions:

- binwalk
- uefi-firmware version 1.9
- cbfstool

!!! warning
    The version of uefi-firmware included in DTS fails while extracting. More
    info at issue [#1226](https://github.com/Dasharo/dasharo-issues/issues/1226).

!!! note
    In Fedora 41 for the first two it's as easy as:
    ```bash
    sudo dnf install binwalk python3-pip python3-devel gcc
    pip install uefi-firmware==1.9
    ```
    cbfstool can be built with coreboot buildsystem:
    ```bash
    make -C util/cbfstool
    ```

### Obtaining vendor firmware and patching Dasharo

1. For EC and BIOS ACM file the Dell firmware is needed

    ```bash
    wget --user-agent='Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'\
     https://dl.dell.com/FOLDER05066036M/1/O7010A29.exe
    ```

1. Extract the binary

    ```bash
    binwalk --run-as=$(whoami) -e O7010A29.exe -C .
    ```

1. Extract the UEFI components

    ```bash
    uefi-firmware-parser -e "_O7010A29.exe.extracted/65C10" -O
    ```

1. Copy and patch the needed files:

    === "EC support"
        Copy the needed blob:
        ```bash
        cp _O7010A29.exe.extracted/65C10_output/pfsobject/\
        section-7ec6c2b0-3fe3-42a0-a316-22dd0517c1e8/volume-0x50000/\
        file-d386beb8-4b54-4e69-94f5-06091f67e0d3/section0.raw sch5545_ecfw.bin
        ```
        Patch the Dasharo binary
        ```bash
        cbfstool coreboot.rom add -f sch5545_ecfw.bin -n sch5545_ecfw.bin -t raw
        ```

    === "TXT support"
        Copy the needed BIOS ACM file:
        ```bash
        cp _O7010A29.exe.extracted/65C10_output/pfsobject/\
        section-7ec6c2b0-3fe3-42a0-a316-22dd0517c1e8/volume-0x500000/\
        file-2d27c618-7dcd-41f5-bb10-21166be7e143/object-0.raw \
        IVB_BIOSAC_PRODUCTION.bin
        ```
        Get the also needed SINIT file from [3mdeb-mirror](https://dl.3mdeb.com/mirror/intel/acm/):
        ```bash
        wget https://dl.3mdeb.com/mirror/intel/acm/SNB_IVB_SINIT_20190708_PW.bin
        ```
        Patch the Dasharo binary
        ```bash
        cbfstool coreboot.rom add -f IVB_BIOSAC_PRODUCTION.bin -n \
        txt_bios_acm.bin -t raw -a 0x20000
        cbfstool coreboot.rom add -f SNB_IVB_SINIT_20190708_PW.bin -n \
        txt_sinit_acm.bin -t raw -c lzma
        ```

1. Install the prepared binary with the manual method:
    * To flash Dasharo first time refer to [initial deployment manual](initial-deployment.md).
    * To update Dasharo refer to [firmware update](firmware-update.md).
