# Initial deployment

Initial flashing of Dasharo firmware can be done from Linux using flashrom with
the internal programmer. This document describes the process of building,
installing and running flashrom on Ubuntu 22.04.

## Build flashrom

Please follow generic guide for [Dasharo flashrom fork](../../osf-trivia-list/deployment.md#how-to-install-dasharo-flashrom-fork).

## Reading flash contents

Always prepare a backup of the current firmware image. To read from the flash
and save it to a file (`dump.rom`), execute the following command:

```bash
flashrom -p internal -r dump.rom
```

## Flashing Dasharo

=== "FW6"

    To flash Dasharo on the platform, execute the following command - replace `[path]`
    with the path to the Dasharo image you want to flash, e.g. `protectli_fw6_DF_v1.0.14.rom`.

    ```bash
    sudo flashrom -p internal -w [path] --ifd -i bios
    ```

    After successful operation reboot the platform.

=== "V1000-series"

    To flash Dasharo on the platform, execute the following command - replace
    `[path]` with the path to the Dasharo image you want to flash, e.g.
    `protectli_vault_V1210_v0.9.3.rom`.

    ```bash
    flashrom -p internal -w [path] --ifd -i bios
    ```

    This will flash the BIOS region only. After the operation is successful,
    reboot the platform.

=== "VP4630/VP4650/VP4670"

    To flash Dasharo on the platform, execute the following command -
    replace `[path]` with the path to the Dasharo image you want to flash, e.g.
    `protectli_vault_cml_v1.0.13.rom`.

    ```bash
    flashrom -p internal -w [path]
    ```

    This will flash the full image, including the Intel ME. The operation
    requires a hard reset of the platform. To perform a hard reset:

    1. Power off the platform. Note, it may not power off completely due to
        flashed ME.
    2. Disconnect power supply from the board when OS finishes all tasks after
        power off (the screen goes dark or black).
    3. Disconnect the RTC/CMOS battery OR clear the CMOS using the pin header
        located near memory slots. Wait about half a minute (unshort the pins).
    4. Connect the power supply back.
    5. The platform should power on normally now. You can connect the battery
        back if it was disconnected.

=== "VP6630/VP6650/VP6670"

    To flash Dasharo on the platform, execute the following command - replace
    `[path]` with the path to the Dasharo image you want to flash, e.g.
    `protectli_vp66xx_v0.9.0.rom`.

    ```bash
    flashrom -p internal -w [path] --ifd -i bios
    ```

    This will flash the BIOS region only. After the operation is successful,
    reboot the platform.

=== "VP2410"

    To flash Dasharo on the platform, execute the following command -
    replace `[path]` with the path to the Dasharo image you want to flash,
    e.g. `protectli_vault_glk_v1.0.15.rom`.

    If stock firmware is currently installed:

    ```bash
    flashrom -p internal -w [path]
    ```

    If Dasharo is currently installed, only the COREBOOT and IFWI partitions
    of the flash needs to be updated. Flash it using the following command:

    ```bash
    flashrom -p internal -w protectli_vault_glk_v1.0.15.rom --fmap -i COREBOOT -i IFWI
    ```

    This command also preserves Dasharo UEFI settings and the boot order.

=== "VP2420"

    To flash Dasharo on the platform, execute the following command - replace
    `[path]` with the path to the Dasharo image you want to flash, e.g.
    `protectli_vault_ehl_v1.0.0.rom`.

    If stock firmware is currently installed:

    ```bash
    flashrom -p internal -w [path] --ifd -i bios
    ```

    If Dasharo is currently installed, only the `RW_SECTION_A` partition of the
    flash needs to be updated. Flash it using the following command:

    ```bash
    flashrom -p internal -w protectli_vault_ehl_v1.x.y.rom --fmap -i RW_SECTION_A
    ```

    This command also preserves Dasharo UEFI settings and the boot order.

=== "VP2430"

    To flash Dasharo on the platform, execute the following command - replace
    `[path]` with the path to the Dasharo image you want to flash, e.g.
    `protectli_vp2430_v0.9.0.rom`.

    If stock firmware is currently installed:

    ```bash
    flashrom -p internal -w [path] --ifd -i bios
    ```

    If Dasharo is currently installed, only the `RW_SECTION_A` partition of the
    flash needs to be updated. Flash it using the following command:

    ```bash
    flashrom -p internal -w protectli_vp2430_v0.9.0.rom --fmap -i RW_SECTION_A
    ```

    This command also preserves Dasharo UEFI settings and the boot order.

=== "VP3210/VP3230"

    To flash Dasharo on the platform, execute the following command -
    replace `[path]` with the path to the Dasharo image you want to flash,
    e.g. `protectli_vp32xx_v0.9.0.rom`:

    ```bash
    flashrom -p internal -w protectli_vp32xx_v0.9.0.rom
    ```
=== "VP2440"

    To flash Dasharo on the platform, execute the following command - replace
    `[path]` with the path to the Dasharo image you want to flash, e.g.
    `protectli_vp2440_v0.9.0.rom`.

    If stock firmware is currently installed:

    ```bash
    flashrom -p internal -w [path] --ifd -i bios
    ```

    If Dasharo is currently installed, only the `RW_SECTION_A` partition of the
    flash needs to be updated. Flash it using the following command:

    ```bash
    flashrom -p internal -w protectli_vp2440_v0.9.0.rom --fmap -i RW_SECTION_A
    ```

    This command also preserves Dasharo UEFI settings and the boot order.
