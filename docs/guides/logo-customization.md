# Boot logo replacement instructions

## Introduction

The logo displayed at boot can be customized according to the client's
preferences. For this, we have created a script that automates the process of
replacing the logo. It is part of the
[Dasharo Configuration Utility](https://github.com/Dasharo/dcu) - a tool
designed to configure Dasharo binary images.

## Procedure

=== "Dasharo"

    Use the [Dasharo Configuration Utility](https://github.com/Dasharo/dcu#usage)
    to put custom logo into a Dasharo coreboot image.

    ```bash
    ./dcu logo <dasharo_image> -l <logo_file>
    ```

    Changing logo on a fused platform requires adding more arguments to flashrom commands:

    - read only bios region

    ```bash
    flashrom -p internal --ifd -i bios -r <dasharo_image>
    ```

    - write only bios region + add noverify

    ```bash
    flashrom -p internal --ifd -i bios -w <dasharo_image> --noverify-all
    ```

=== "Dasharo (coreboot + Heads)"

    Logo customization is not supported as of now. To replace the logo,
    you must rebuild the firmware. You need to replace the
    `branding/Dasharo/bootsplash.jpg` with your own, and proceed with the
    building manual.
