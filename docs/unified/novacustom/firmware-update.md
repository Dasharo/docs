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

    ## Prerequisites

    Your firmware version can be checked by entering the
    [Dasharo Setup Menu](../../dasharo-menu-docs/overview.md#dasharo-menu-guides)
    using the ++f2++ key while booting.

    !!! note "Please note"

        Before updating, it is recommended to set the Intel Management Engine to
        Disabled (HAP) in [Dasharo System Features](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#intel-management-engine-options).

    > Advanced users can also [build](./building-manual.md) and/or flash the
    > binaries themselves by following the steps under the [Manual
    > update](#manual-update) section.

    ### Capsule Update via fwupd

    Using fwupd is the recommended and simplest way to perform Dasharo
    firmware updates on supported devices.

    To check which firmware versions support fwupd updates, check
    [Firmware Update Guide](../../guides/firmware-update.md#fwupd--lvfs).

    For instructions on how to use fwupd and update the firmware, follow the
    [Dasharo fwupd documentation](../../kb/fwupd.md#update-instructions).

    === "Laptops"

        ### Firmware Update Mode

        Firmware Update Mode is available on the following versions:

        | Generation |    Version    |                         Note                         |
        | ---------- | ------------- | ---------------------------------------------------- |
        | 11th       | > 1.5.0       |                                                      |
        | 12th       | > 1.7.0       |                                                      |
        | 14th       | 0.9.0 - 0.9.1 | On newer versions, please use fwupd directly instead |

        To update using Firmware Update Mode, follow the
        [Generic Firmware Update Documentation](../../guides/firmware-update.md#firmware-update-mode).

        Check out our [YouTube video](https://www.youtube.com/watch?v=muWjhrQ7bQk)
        for a demonstration of Firmware Update Mode.

    === "NUC BOX"

    ### Updating via DTS

    1. First, ensure that [UEFI Secure Boot](../../dasharo-menu-docs/device-manager.md#custom-mode-and-key-management)
       has been disabled and that [Network Boot](../../dasharo-menu-docs/dasharo-system-features.md#networking-options)
       has been enabled.

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

    Ensure that the firmware protections are disabled:

    * in [Dasharo Security Options](../../dasharo-menu-docs/dasharo-system-features.md) both `BIOS boot medium lock` and `Enable SMM BIOS write protection` should be unchecked.
    * [UEFI Secure Boot](../../dasharo-menu-docs/device-manager.md#secure-boot-configuration) must be disabled (uncheck `Attempt Secure Boot` if `Current Secure Boot State` does not say `Disabled`).
    * the Intel Management Engine must be set to `Disabled (HAP)` in [Dasharo System Features](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#intel-management-engine-options).

    To apply changes, you will need to reboot.

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

    !!! warning "PLEASE NOTE:"
        As of the Heads releases **v0.9.1 for V5x0TU** and **v0.9.3 for
        NV4xPZ**, a **barrel jack power supply** needs to be plugged in during
        the update. The reboot triggered by the EC update resets the USB-PD
        controller, which does not come back up in time for the EC update's
        AC adapter check, causing it to fail. A barrel jack supply bypasses
        this issue.

        Furthermore, please make sure that you have followed our
        [Initial deployment](https://docs.dasharo.com/unified/novacustom/initial-deployment/#apt-package-manager_1)
        guide beforehand, specifically the section on EC firmware installation.
