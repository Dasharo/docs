# Firmware update

This document explains the process of updating firmware on the ASRock Rack
TURIND8UD platform.

=== "LinuxBoot"

    !!! warning "No in-band firmware update is available yet"

        There is currently **no supported method for updating the Dasharo
        firmware from the running operating system** on this platform.

        In-place firmware update support is planned and will become available once
        OpenBMC support is implemented for the platform. Once OpenBMC is in place,
        firmware will be updatable through the BMC. This page will be updated with
        the procedure when that support lands.

    ## Reflashing the firmware

    Until an in-band update method is available, the only way to change the
    firmware is to externally program the BIOS SPI flash chip. Follow the process
    described in the [Recovery](recovery.md#external-flashing) section.

=== "UEFI"

    The firmware may be updated using Dasharo Firmware Update Mode.

    1. Power on the device.
    2. While the device is booting, hold the `ESC` key to enter the UEFI Setup
        Menu.
    3. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
    4. Enter the [Dasharo Security Options](../../../dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
        submenu.
    5. Select the "Firmware Update Mode" option.
    6. Follow instructions on screen to perform the automatic update of firmware.

    For more details, see [Firmware Update Mode](../../../kb/firmware-update-mode/).
