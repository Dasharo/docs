# Dasharo image customization

## Introduction

Sometimes it is necessary to customize the image by changing the logo
displayed on boot or to set a unique UUID or Serial Number for SMBIOS.
[coreboot_customizer](https://github.com/Dasharo/meta-dts/blob/3da0807f10b46f496e23fff97c61ed49861cb475/meta-dts-distro/recipes-dts/dts/dts/coreboot_customizer)
is a simple script that help with these tasks.

## Prerequisites

Following packages must be installed:

* `imagemagick` (for `convert` command)
* `util-linux` (for `uuidparse` command)

The script will exit with an error if any of above are not present.

Additionally the script makes use of [coreboot's
cbfstool](https://github.com/coreboot/coreboot/tree/master/util/cbfstool) to
modify the images, so it is required to be available to the script. The script
will try to find the `cbfstool`` installed in the system. If not found, then
it searches for cbfstool in the current directory. If not found, then it tries
to download the cbfstool from [3mdeb's
FTP](https://dl.3mdeb.com/open-source-firmware/utilities/cbfstool) (compiled
using instructions in [Compiling cbfstool](#compiling-cbfstool)). If that
fails, the script will exit with an error.

## Usage

```txt
Usage: coreboot_customizer OPTIONS coreboot.rom

  coreboot.rom  - Dasharo coreboot file to modify

  OPTIONS:
    -u | --uuid <UUID>              - UUID in RFC4122 format to be set in SMBIOS type 1 structure
    -s | --serial-number <SERIAL>   - Serial number to be set in SMBIOS type 1 and type 2 structure
    -l | --logo <LOGO>              - Custom logo in BMP/PNG/JPG/SVG format to be displayed on boot

  Examples:
    ./coreboot_customizer -u 96bcfa1a-42b4-6717-a44c-d8bbc18cbea4 -s D07229051 -l ~/logo.svg coreboot.rom

    ./coreboot_customizer -u `dmidecode -s system-uuid` -s `dmidecode -s baseboard-serial-number` coreboot.rom
      Above command will obtain the current SMBIOS UUID and Serial Number
      from the system and patch the coreboot binary.
```

`coreboot_customizer` can be used as a standalone script (paired with
cbfstool) and is also available in [Dasharo Tools
Suite](../dasharo-tools-suite/overview.md).

The script will save the UUID and Serial Number to the COREBOOT region and the
logo to BOOTSPLASH region.

NOTE: Not all Dasharo platform support such customizations.

NOTE: if you update the firmware by rewriting whole BIOS region, the data will
be lost. To avoid data loss during the COREBOOT region update, Dasharo
firmware will keep the copies of Serial Number and UUID in the UEFI variables
on normal boot, so that in the potential firmware update in the future, the
data will be kept (as long as UEFI variables are not erased).

## Error codes

* 0 - no error
* 1 - unknown argument/option
* 2 - `uuidparse` not found
* 3 - `convert` not found
* 4 - coreboot image not found or invalid path
* 5 - `cbfstool` not found
* 6 - failed to extract coreboot configuration file from coreboot image
* 7 - configurable UUID not supported by given coreboot image
* 8 - invalid UUID format
* 9 - failed to set the UUID (more detailed error information in the script
      output)
* 10 - configurable Serial Number not supported by given coreboot image
* 11 - failed to set the Serial Number (more detailed error information in the
       script output)
* 12 - logo file not found or invalid path
* 13 - unsupported logo file format
* 14 - customizable logo not supported by given coreboot image
* 15 - logo file too big to fit in given coreboot image
* 16 - failed to set the logo (more detailed error information in the script
       output)

## Compiling cbfstool

```bash
git clone https://review.coreboot.org/coreboot.git
cd coreboot
TOOLLDFLAGS=-static make -C util/cbfstool
strip --strip-unneeded util/cbfstool/cbfstool
```

Copy the `util/cbfstool/cbfstool` to the directory where `coreboot_customizer`
is saved. Alternatively you make install `cbfstool` to your system:
`TOOLLDFLAGS=-static sudo make -C util/cbfstool install`.

<!--Empty pixel to avoid orphaned pages when overview is hidden-->
[![empty-pixel](../../images/empty_pixel.png)](logo-customization.md)
