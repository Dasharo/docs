# Capsule Updates

## Introduction

This document lists devices which support UEFI Update Capsules and
demonstrates how to use them for a firmware update.  There is [a more detailed
overview](../kb/capsule-updates-overview.md) which can be helpful in showing how
this compares to other update methods.

## Supported devices

!!! note

    Update Capsules are only supported in UEFI/EDK2 firmware versions,
    not in SeaBIOS or Heads-based firmware flavors.

The following table describes which devices support Update Capsules
and since which firmware release, if applicable.  If a particular device isn't
mentioned, it means that it doesn't support this update method.

| Manufacturer | Device     | Starting with FW version |
| ---          | ---        | ---                      |
| MSI          | Z690-A PRO | TBD                      |
| MSI          | Z790-P PRO | TBD                      |

`TBD` (to be delivered) is used as a placeholder for upcoming releases which
should have this feature enabled.

## Prerequisites

* _UEFI Shell_<br>
  UEFI Dasharo firmware has this, but won't hurt to call it out explicitly.
* _Storage device available from UEFI Shell_<br>
  Not all file-systems are available to UEFI, so not all storage devices and
  partition on them will be usable for the purpose of capsule updates.  An
  ESP (EFI System Partition, where `EFI/` directory is located) is a good choice
  because it should be always readable by UEFI.
* _`CapsuleApp.efi`_<br>
  This is a UEFI application which passes a capsule file to firmware to perform
  an update.
* _Firmware capsule_<br>
  The firmware update capsule file itself.  Should have `.cap` file extension.

## What's preserved by an update

| Type         | Notes                                      |
| ---          | ---                                        |
| SMMSTORE     | holds UEFI Variables such as [settings](../dasharo-menu-docs/dasharo-system-features.md) or [boot order](../dasharo-menu-docs/boot-maintenance-mgr.md)                  |
| ROMHOLE      | only on MSI                                |
| SMBIOS       | unique data like serial number or UUID     |
| boot logo    | [set by the user](logo-customization.md)   |

Preservation is done as a best effort. However some
 firmware changes are expected (e.g., current custom
 logo can be too large for the new firmware), thus a
 failure to move data in some cases won’t necessarily
 abort an update.

## How to use UEFI Update Capsules

!!! note

    Out of technical necessity, Intel Management Engine (Intel ME) must be
    HAP-disabled in order for firmware to process a capsule successfully.  If
    you're sure that the supplied capsule is the correct one, but you keep
    getting this error:

    ```
    CapsuleApp: failed to query capsule capability - Unsupported
    ```

    Then double-check that Intel ME is in `Disabled (HAP)` state in [the
    corresponding menu][me-menu] or switch it to that state before performing
    an update.

1. Copy `CapsuleApp.efi` and `firmware.cap` files to a partition (the shorter
   the path from the root, the easier it will be to find in the UEFI Shell).

2. See the note above about Intel ME and HAP-disable it if it's enabled or
   soft-disabled at the moment.  An update won't be initiated if this isn't
   done (`CapsuleApp.efi` will make an effort and give up, so no harm other than
   update not happening).

3. Enter [Boot Manager Menu][bmm] and select `UEFI Shell` entry.  Alternatively,
   if you're in Setup, use [One Time Boot][otb] which is a different way to do
   the same.

4. Press `Escape` to get to the prompt.  In practice pressing any key works the
   same in most cases, so no problem if you didn't make it in 5 seconds.

5. The first thing that UEFI Shell prints, even before the prompt with the
   timer, is the list of file systems and block devices (it can also be
   retrieved later by running `map` command):
   ![Top of UEFI Shell](../images/uefi-shell-top.png)
   The hard part is to find the drive with `CapsuleApp.efi` and `firmware.cap`
   among them. One way of doing it is going through `FS*` sequentially using
   `ls` command:
   ![ls command in UEFI Shell](../images/uefi-shell-ls.png)
   Once the file-system is identified, run its name to switch to it:
   ![Change file-system in UEFI Shell](../images/uefi-shell-cd-fs.png)

6. If files are in file-system's root, no need to do anything here.  Otherwise,
   use `cd` command to open a target directory to not have to enter full paths:
   ![Change directory in UEFI Shell](../images/uefi-shell-cd-dir.png)

7. Now you should be in a position to initiate a capsule update (run `ls` again
   if in doubt about current location) via `CapsuleApp.efi
   firmware.cap` (substitute `firmware.cap` with an actual file name):
   ![Initiating a capsule update](../images/uefi-shell-capsule-app-posting.png)
   A sign of success is an immediate reboot followed by a dialog of [Firmware
   Update Mode](../kb/firmware-update-mode.md):
   ![Firmware Update Mode warning](../images/fum-warning.png)
   Read the text and press the key it asks you to press if you want to proceed.

8. An ongoing firmware update looks like this:
   ![Ongoing capsule update](../images/uefi-capsule-update.png)

!!! warning

    Don't reboot or power off the device until the process is completed!

After either a successful or failed update, the machine should reboot
 automatically. After that, if everything succeeded, you should have an
 updated firmware with data migrated from the previous version.

!!! note

      Since the settings were preserved, remember to re-enable Intel Management Engine after the update.

[me-menu]: ../dasharo-menu-docs/dasharo-system-features.md#intel-management-engine-options
[bmm]: ../dasharo-menu-docs/overview.md#boot-manager-menu
[otb]: ../dasharo-menu-docs/overview.md#one-time-boot

## Version verification

Current version of the firmware can be seen in the top-left corner of the main
page of the [Setup][main-page].

![Main page](../images/menus/main_page.jpeg)

[main-page]: ../dasharo-menu-docs/overview.md#main-page

## Troubleshooting

In case the update process has aborted, one can run `CapsuleApp.efi -S` in UEFI
Shell to get basic information pointing to the reason:

![Failed update debug output](../images/uefi-capsule-update-not-ready.png)

The most interesting field is `Capsule Status:`.  The error codes there are
quite generic but still useful:

* `Security Violation` indicates an issue with capsule's signature
* `Not Ready` indicates that the capsule is unsupported by this firmware, likely
  because it isn't compatible

## Further information

* [Overview of Update Capsules](../kb/capsule-updates-overview.md)
* [Details on Update Capsules](../kb/edk2-capsule-updates.md)
  (developer-oriented)
