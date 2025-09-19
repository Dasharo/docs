# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update. The update process may be different, depending on which
firmware version is currently installed on your device.

!!! question "Boot time after update"
    The first boot after updating firmware may take a longer time than usual,
    due to memory being re-trained. Generally, first boot time increases
    according to the amount of installed RAM in the system. A system with 96 GB
    of RAM may take over 2 minutes to boot.

    After first boot, memory training settings are cached, and subsequent boot
    times should be much lower.

=== "Dasharo (UEFI)"

    === "Laptops"

        ## Prerequisites

        Your firmware version can be checked by entering the
        [Dasharo Setup Menu](../../dasharo-menu-docs/overview.md#dasharo-menu-guides)
        using the ++f2++ key while booting.

        > Advanced users can also [build](./building-manual.md) and/or flash the
        > binaries themselves by following the steps under the [Manual
        > update](#manual-update) section.

        ### Capsule Update via fwupd

        fwupd and Capsule Update are available starting with the following versions:

        | Generation | Version |
        | ---------- | ------- |
        | 11th       | 1.6.0   |
        | 12th       | 1.8.0   |
        | 14th       | 1.0.0   |

        !!! note

            Capsule updates are only available when Intel ME is HAP-Disabled and the
            AC adapter is connected to the laptop

            See [this Knowledge Base article](../../dasharo-menu-docs/dasharo-system-features.md#intel-management-engine-options)
            for information about disabling the ME, or [Issue #1302](https://github.com/Dasharo/dasharo-issues/issues/1302)
            for more context.

        To update your firmware, run the following commands:

        ```bash
        $ sudo fwupdtool refresh
        $ sudo fwupdtool update
        ```

        or use any other fwupd front-end of your choice, like GNOME Firmware Update.
        Then, reboot your machine to apply the update.

        !!! warning
            Powering off instead of rebooting as instructed by fwupd will result in
            aborting the update.

        ### Firmware Update Mode

        Firmware Update Mode is available starting with the following versions:

        | Generation | Version |
        | ---------- | ------- |
        | 11th       | 1.5.0   |
        | 12th       | 1.7.0   |
        | 14th       | Any     |

        To update using Firmware Update Mode, follow the
        [generic Firmware Update documentation](../../guides/firmware-update.md#firmware-update-mode).

        Check out our [YouTube video](https://www.youtube.com/watch?v=muWjhrQ7bQk)
        for a demonstration of Firmware Update Mode.

        ### Updating older versions

        1. First, ensure that [UEFI Secure Boot](../../dasharo-menu-docs/device-manager.md#custom-mode-and-key-management)
           has been disabled.

        2. Boot to the [Dasharo Tools Suite](../../dasharo-tools-suite/documentation/running.md#bootable-over-a-network).
           We recommend the network boot option.

        3. In the main menu of Dasharo Tools Suite, select option `5` to proceed with
           the installation of the firmware update.

        4. In case you want to know more about the firmware update option in Dasharo
           Tools Suite, please check out the
           [features section](../../dasharo-tools-suite/documentation/features.md#firmware-update)
           of the dedicated Dasharo Tools Suite documentation page.

        ### Manual update

        This update method is for advanced users only and is not recommended for
        regular end users.

        > Please make sure you that you update the BIOS firmware and the EC firmware
        > respectively, as the laptop will power off after the EC firmware flash.

    === "NUC BOX"

        ### Manual update

        Currently, the NUC BOX only supports updating the firmware manually via DTS.

    Ensure that the firmware protections are disabled (1) in
    [Dasharo Security Options](../../dasharo-menu-docs/dasharo-system-features.md).
    Both `BIOS boot medium lock` and `Enable SMM BIOS write protection` should
    be unchecked. [UEFI Secure Boot](../../dasharo-menu-docs/device-manager.md#secure-boot-configuration)
    must be disabled as well (uncheck `Attempt Secure Boot` if
    `Current Secure Boot State` does not say `Disabled`). To apply changes, you
    will need to reboot.
    { .annotate }

    1. These options were introduced in v1.5.0 for TGL models and v1.7.0 for ADL
       models. You can skip these steps if you are using an older firmware version.

    Follow the local firmware update procedure described in the [DTS firmware update
    documentation](../../dasharo-tools-suite/documentation/features.md#local-firmware-update).

    > Please note that
    > [network boot must be enabled](../../dasharo-menu-docs/dasharo-system-features.md#networking-options)
    > if you want to boot to the Dasharo Tools Suite over a network connection.

=== "Dasharo (coreboot + Heads)"

    ## Firmware update

    [Build](building-manual.md#dasharo-coreboot--heads) or
    download Dasharo Heads firmware, and proceed with
    the official [Heads update documentation](https://osresearch.net/Updating).
