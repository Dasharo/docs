# Firmware transition

=== "NUC BOX"

    The transition is currently only supported on laptops. The NUC BOX is
    currently not supported by Heads.

=== "Laptops"

    ## Introduction

    This document describes the process of transitioning from Dasharo UEFI to Heads
    and the other way around.

    > NOTE: The transition is currently only supported on laptops. The NUC BOX is
      currently not supported by Heads.

    ## Switching from Dasharo UEFI to Heads

    To change firmware branches from UEFI to Heads, because of how different the two
    firmware types are, it's required to disable some security measures before
    flashing. Follow the steps below to install Heads from an existing Dasharo UEFI
    firmware installation:

    - Hold down the ++f2++ key and press the ++power++ button to enter the UEFI
      Setup Menu
    - Enter the `Device Manager` submenu and disable `Secure Boot`
    - Enter the `Dasharo System Features` submenu
    - In the `Dasharo Security Options` submenu, disable:
        + SMM BIOS Write Protection
        + BIOS boot medium lock
    - In the `Intel Management Engine Options` submenu disable the Management Engine

    !!! tip

        For a more detailed guide on the UEFI Setup Menu options, check out the
        [Dasharo menu documentation](https://docs.dasharo.com/dasharo-menu-docs/overview).

    - [Boot into Dasharo Tools
      Suite](https://docs.dasharo.com/dasharo-tools-suite/documentation/running/)
    - Enter your DPP subscription credentials
    - Select `Update Dasharo firmware` to check for updates
    - When asked to switch to Heads firmware, press `Y`
    - Proceed with [DTS firmware
      update](https://docs.dasharo.com/dasharo-tools-suite/documentation/features/#firmware-update)
      as usual

    When the update is finished, your laptop will shut down automatically. Power it
    back on to boot into your new Heads installation!

    !!! warning "TOTP secrets warning"

        On the first boot, you will be shown a warning about TOTP secrets. This is
        normal and expected on the first boot. Run `OEM Factory Reset /
        Re-Ownership` to finish deploying Heads.

        Check out [Heads documentation](https://osresearch.net/Configuring-Keys/#oem-factory-resetre-ownership)
        for a detailed factory reset guide.

    !!! note "Note for Qubes OS users"

        After installing Qubes while Heads is installed, you will need to select
        `Reset TPM` in the Heads menu to finish the installation.

        From the main menu, enter `Options` -> `TPM/TOTP/HOTP Options` and select
        `Reset the TPM`.

        Users upgrading to Heads while Qubes is already installed are not affected.

    ## Switching from Dasharo Heads back to UEFI

    To revert back to UEFI, you will need to use Heads' built-in firmware update
    tool:

    - Prepare USB stick with UEFI firmware binary

        !!! note "Supported filesystems"
            FAT, exFAT or ext4 filesystem is recommended

    - Insert the USB stick into the laptop
    - Enter Heads main menu -> ++"Options"++ -> ++"Flash/Update the BIOS"++
    - Select ++"Flash the firmware with a new ROM, erase settings"++
    - Confirm that you have inserted the USB stick
    - Select your downloaded firmware binary on the USB stick
    - (Optional) Compare sha256 checksum with the official, signed digests available
      on the `Releases` page for your device on docs.dasharo.com
    - Select ++"Yes"++ to begin flashing
    - When the update is done, press ++enter++ to reboot your device.

    Your device should reboot into UEFI firmware.

    > When reverting to UEFI, it's not possible to restore EFI boot manager entries
    > that were added before installing Heads. Therefore, you may need to re-create
    > your boot entries manually, or find your boot loader using `Boot From File`
    > option in the UEFI setup menu.
