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

## Preparation

Follow the steps specified in [the building instructions](../building)

## Procedure

The script `build.sh` located in the coreboot directory can be used
to replace the logo. To replace the logo, run the following command:

```bash
$ ./build.sh build -l path/to/logo.bmp
```

The command will output an updated coreboot image into the directory `artifacts`.
