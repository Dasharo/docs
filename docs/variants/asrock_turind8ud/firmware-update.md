# Firmware update

ASRock Rack TURIND8UD-2T/X550 runs Dasharo firmware with a
[LinuxBoot](https://www.linuxboot.org/) payload.

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
