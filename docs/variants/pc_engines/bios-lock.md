# BIOS Lock

This document describes the firmware write protect functionality integrated
into Dasharo (coreboot + UEFI) firmware for PC Engines platforms.

## Implementation

The option `Lock the BIOS Boot Medium` controls the flash protection feature
of the BIOS boot flash. If enabled, pins 1-2 on header J2 (apu2) / J3 (apu3,4,6)
can be shorted to prevent writes to the BIOS bootblock and recovery regions.

When the option is enabled and the WP header is set, firmware write protection
**cannot** be disabled until the header is physically unshorted, even by
disabling the lock in the UEFI setup menu.

!!! note

    User-updatable firmware regions remain writable while BIOS Lock is enabled
    to support non-volatile EFI variables and other features.

## Enabling BIOS Write Protection

To enable BIOS write protection:

- Enter UEFI Setup Menu
- Enter Dasharo System Features -> Dasharo Security Options
- Set the option to enable write protection
- Save and reboot
- Power off the platform
- Bridge pins 1 and 2 on header J2 (apu2) / J3 (apu3,4,6)

The firmware is now write protected. Protection is guaranteed as long as the
jumper is set.

## Disabling BIOS Write Protection

To disable BIOS write protection:

- Unbridge the WP pins
- Power on the platform and enter UEFI Setup Menu
- Enter Dasharo System Features -> Dasharo Security Options
- Unset the option to enable write protection
- Save and reboot
- Boot into a Linux OS. You can now re-flash your firmware by e.g.:

    ```bash
    sudo flashrom -p internal -c "W25Q64JV-.Q" -w pcengines_apu2_v0.9.0.rom
    ```

!!! note

    Firmware write protection is not disabled until you actually attempt to
    write to the flash. Flashrom will automatically disable block write
    protection when attempting to write to the flash.

    See [issue #754](https://github.com/Dasharo/dasharo-issues/issues/754) for
    more information.
