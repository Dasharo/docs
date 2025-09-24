# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update. The update process may be different, depending on which
firmware version is currently installed on your device. The currently installed
firmware version can be checked with the following command in a Linux
environment:

```bash
sudo dmidecode -t bios | grep Version
```

Alternatively, it can be checked in the `BIOS Setup Menu`.

=== "Dasharo (UEFI)"

    ## Prerequisites

    Depending on firmware version (1) there may be manual steps required to ensure that
    the firmware can be updated.
    { .annotate }

    1. v0.9.0 for Z790-P and v1.1.2 for Z690-A introduced support for Firmware
       Update Mode

    ### Firmware Update Mode

    If the currently installed Dasharo version supports Firmware Update Mode, follow
    the steps outlined in
    [generic Firmware Update documentation](../../guides/firmware-update.md#firmware-update-mode).

    ### Manual

    Ensure that the firmware protections are disabled in
    [Dasharo Security Options](../../dasharo-menu-docs/dasharo-system-features.md).
    Both `BIOS boot medium lock` and `Enable SMM BIOS write protection` should
    be unchecked. [UEFI Secure Boot](../../dasharo-menu-docs/device-manager.md#secure-boot-configuration)
    must be disabled as well (uncheck `Attempt Secure Boot` if
    `Current Secure Boot State` does not say `Disabled`). To apply changes you
    will need to reboot.

    Please use one of the following environments to perform Dasharo update:

    * [Dasharo Tools Suite (DTS)](#dasharo-tools-suite)
    * [Linux distribution of your choice](#linux-distribution-of-your-choice)

    We recommend using DTS for updating firmware.

    ### Dasharo Tools Suite

    The DTS allows performing automatic firmware update process, which is the
    recommended method. To update your firmware, follow below steps.

    1. Boot [DTS using iPXE](../../dasharo-tools-suite/documentation/running.md#bootable-over-a-network)
       on your platform.
    2. Follow [firmware update](../../dasharo-tools-suite/documentation/features.md#firmware-update)
       procedure described in DTS documentation.

    ### Linux distribution of your choice

    Linux distributions may not yet have the support for the newest chipsets in
    flashrom installed via package manager so building the flashrom from source
    may be inevitable. You may check if your flashrom supports the Z690 and Z790
    chipset by doing a dry run without firmware binary:

    ```bash
    sudo flashrom -p internal
    ```

    Example output of undetected chipset:

    ```txt
    flashrom v1.2 on Linux 5.19.0-32-generic (x86_64)
    flashrom is free software, get the source code at https://flashrom.org

    Using clock_gettime for delay loops (clk_id: 1, resolution: 1ns).
    Cannot open file stream for /dev/mtd0
    No DMI table found.
    WARNING: No chipset found. Flash detection will most likely fail.
    ========================================================================
    You may be running flashrom on an unknown laptop. We could not
    detect this for sure because your vendor has not set up the SMBIOS
    tables correctly. Some internal buses have been disabled for
    safety reasons. You can enforce using all buses by adding
      -p internal:laptop=this_is_not_a_laptop
    to the command line, but please read the following warning if you
    are not sure.

    Laptops, notebooks and netbooks are difficult to support and we
    recommend to use the vendor flashing utility. The embedded controller
    (EC) in these machines often interacts badly with flashing.
    See the manpage and https://flashrom.org/Laptops for details.

    If flash is shared with the EC, erase is guaranteed to brick your laptop
    and write may brick your laptop.
    Read and probe may irritate your EC and cause fan failure, backlight
    failure and sudden poweroff.
    You have been warned.
    ========================================================================
    No EEPROM/flash device found.
    Note: flashrom can never write if the flash chip isn't found automatically.
    ```

    It means you cannot proceed with this flashrom version and you have to remove
    it using your package manager. Then follow the procedure for building the right
    flashrom is described in `Build flashrom` section in the
    [Initial deployment documentation](./initial-deployment.md#initial-deployment-manually)
    (note the procedure describes Ubuntu case only, your package manager and
    package names to install may be slightly different). We recommend to use
    [Dasharo Tools Suite](#dasharo-tools-suite).

    Example of good output:

    ```txt
    flashrom v1.2-1031-g6b2061b on Linux 5.19.0-32-generic (x86_64)
    flashrom is free software, get the source code at https://flashrom.org

    Using clock_gettime for delay loops (clk_id: 1, resolution: 1ns).
    No DMI table found.
    Found chipset "Intel Z690".
    Enabling flash write... SPI Configuration is locked down.
    FREG0: Flash Descriptor region (0x00000000-0x00000fff) is read-write.
    FREG1: BIOS region (0x01000000-0x01ffffff) is read-write.
    FREG2: Management Engine region (0x00001000-0x003d8fff) is read-write.
    Enabling hardware sequencing because some important opcode is locked.
    OK.
    Found Programmer flash chip "Opaque flash chip" (32768 kB, Programmer-specific) on internal.
    No operations were specified.
    ```

    That means you are good to go.

    #### Migrating SMBIOS unique data (optional)

    Before flashing you may migrate your serial number and UUID as
    described in [Initial deployment](./initial-deployment.md#migrating-smbios-unique-data).
    Applicable to Dasharo v1.1.0 (PRO Z690-A) / v0.9.0 (PRO Z790-P) and later.

    #### Flashing using flashrom

    === "PRO Z690-A boards"

        ##### Version v1.1.0 or newer

        > Version v1.1.0 and v1.1.2 had to change the flashmap layout and requires
        > usage of the [procedure below](#version-older-than-v110) when migrating from
        > v1.0.0 or older.

        Only the `RW_SECTION_A` and `RW_SECTION_B` partitions of the flash needs to be
        updated. Flash it using the following command:

        ```bash
        flashrom -p internal -w [path] --fmap -i RW_SECTION_A -i RW_SECTION_B
        ```

        > To flash newer firmware the command described in the [section below](#version-older-than-v110)
        > might be also used. But remember, in that case, all Dasharo UEFI settings
        > will be lost. Also, the memory training procedure will have to be carried out
        > again.

        ##### Version older than v1.1.0

        In this case, the whole `bios` region must be updated.

        ```bash
        flashrom -p internal -w [path] --ifd -i bios
        ```

    === "PRO Z790-P boards"

        There is only one version available for now. Please follow instructions
        described in [Initial deployment](./initial-deployment.md) to deploy the
        Dasharo.

        If updating firmware using custom builds without changing the flashmap,
        only the `RW_SECTION_A` and `RW_SECTION_B` partitions of the flash needs to be
        updated. Flash it using the following command:

        ```bash
        flashrom -p internal -w [path] --fmap -i RW_SECTION_A -i RW_SECTION_B
        ```

    #### Troubleshooting

    Possible errors are described in the
    [Generic deployment problems with flashrom](../../osf-trivia-list/deployment.md#flashrom)

=== "Dasharo (coreboot + Heads)"

    [Build](./building-manual.md#dasharo-coreboot--heads) or download Dasharo
    Heads firmware, and proceed with
    the official [Heads update documentation](https://osresearch.net/Updating).
