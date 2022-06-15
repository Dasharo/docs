# Boot logo replacement instructions

## Introduction

The logo displayed at boot can be customized according to the client's
preferences. For this, we have created a script that automates the process of
replacing the logo.

## Prerequisites

The image file must fulfill a number of requirements:

- Bitmap (BMP file)
- up to 577×432 resolution
- indexed or 24bit RGB colors
- uncompressed
- preferably containing a simple logo on a black background with no additional padding.

## Replace logo in an existing image

For devices supporting persistent bootlogo, it's possible to replace the logo
without rebuilding firmware from scratch. You only need the firmware image
and `cbfstool`.

1. Obtain cbfstool source code (skip if you've already cloned the coreboot
   source):

    ```bash
    git clone https://review.coreboot.org/coreboot.git
    ```

1. Build and install cbfstool:

    ```bash
    cd coreboot/util/cbfstool
    make
    sudo make install
    ```

1. Remove the existing logo from the firmware image (replace `[path]` with the
   path to your firmware binary):

    ```bash
    cbfstool [path] remove -r BOOTSPLASH -n logo.bmp
    ```

1. Add your desired bootlogo to the firmware image (replace `[path]` with the
   path to your firmware image and `[logo]` with the path to the logo):

    ```bash
    cbfstool [path] add -f [logo] -r BOOTSPLASH -n logo.bmp -t raw -c lzma
    ```

1. Now you can flash the updated firmware image as usual. If you're not
   updating firmware and just changing the logo, only the BOOTSPLASH region
   needs to be updated. For example:

    ```bash
    sudo flashrom -p internal --fmap -i BOOTSPLASH -w [path]
    ```

## Build image with custom logo

Preparation: Follow the steps specified in [the building instructions](../building)

The script `build.sh` located in the coreboot directory can be used to replace
the logo at build time. To replace the logo, run the following command:

```bash
./build.sh build -l path/to/logo.bmp
```

The command will output an updated coreboot image into the directory `artifacts`.
