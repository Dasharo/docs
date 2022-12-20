# Dasharo menu overview

This section describes the overview of the Dasharo firmware setup menu. In the
subsections you will get to know:

* What options are available?
* How to use submenus and options?
* How the options and submenus work?

[Here](https://youtu.be/3tk0snFrZDY) you may watch a Dasharo menu walkthrough
with commentary presenting Dasharo features.

[Here](/variants/novacustom_nv4x_tgl/compatibility-check-results-ubuntu.md) you
can see checkbox results on Dasharo firmware.

## Dasharo menu guides

The main menu is entered by executing Setup application either through
[Boot Manager Menu](#boot-manager-menu) or platform-specific hotkey. You may
find the right key in the top-left corner when booting the platform (when logo
shows up), for example `DEL`:

```txt
DEL   to enter Setup
F11   to enter Boot Manager Menu
ENTER to boot directly
```

* [Setup Main Page](#main-page)
    - [User Password Management](user-passwd-mgmt.md)
    - [Device Manager](device-manager.md)
    - [Dasharo System Features](dasharo-system-features.md)
    - [One Time Boot](#one-time-boot)
    - [Boot Maintenance Manager](boot-maintenance-mgr.md)

NOTE: Some sections may still be under construction.

* [Boot Manager Menu](#boot-manager-menu) - entered with a different key than
  used for setup application. Lists all bootable options and allows one to
  override the boot path.

### Main Page

![](/images/menus/main_page.jpeg)

The page is the main view of the firmware setup application. It contains the
board model (`MS-7D25`), installed CPU and firmware version in the top-left
corner. In the top-right corner the CPU frequency and system RAM amount is
shown.

From the main page one may access all menus and submenus available in the
firmware setup. Besides the menus there is also an option to:

1. Change the language (currently only English is supported)
2. `Continue` - execute the top first boot order priority
3. `Reset` - resets the platform.

The currently available menus/submenus are as follows:

* [User Password Management](user-passwd-mgmt.md) - allows to set firmware
  setup password
* [Device Manager](device-manager.md) - allows configuring various devices and
  features like: UEFI Secure Boot, TPM device, SATA and TCG OPAL password, etc.
  It may also contain informational menus like Driver Health Manager, Network
  Device List and others.
* [Dasharo System Features](dasharo-system-features.md)- contains submenus for
  features specific to Dasharo products and Dasharo supported platforms
* [One Time Boot](#one-time-boot) - allows to choose which boot entry to
  execute. It simply lists all available boot options and allows to select one
  the same way as [Boot Manager Menu](#boot-manager-menu)
* [Boot Maintenance Manager](boot-maintenance-mgr.md) - allows to manipulate
  various UEFI standard variables responsible for console and boot options. One
  may choose which devices should be used for input and output, choose to boot
  an arbitrary file or modify the boot options and boot order.

NOTE: not all submenus may be available on your platform.
[Contact Dasharo Team](mailto:contact@dasharo.com) for more information and
possible feature extension of your platform.

### Boot Manager Menu

Boot Manager Menu is an application that lists all bootable options and allows
one to override the boot path.

Boot Manager Menu is entered with a different key than setup application. It
may be customized on your platform. The right key to use is always printed on
the screen in the top-left corner, for example `F11`:

```txt
DEL   to enter Setup
F11   to enter Boot Manager Menu
ENTER to boot directly
```

After pressing the right hotkey for Boot Manager Menu, a window should pop up:

![](/images/menus/boot_manager.jpeg)

One may use up and down arrows to move to desired position. Pressing enter will
cause the execution of selected option. Pressing ESC will cause the firmware to
boot the first boot priority according to the configured boot order.

### One Time Boot

When setup application is entered, one of the menus is called `One Time Boot`.
As the name suggests it allows to override the boot just one time (not
permanently). The usage principles are the same as for [Boot Manager Menu](#boot-manager-menu).

Example view of `One Time Boot` submenu:

![](/images/menus/one_time_boot.jpeg)

On the right side of the menu window, there is a `DevicePath` which is a
UEFI-compliant path to the device or file being executed. Depending on the
file/device type, these paths may be different:

![](/images/menus/one_time_boot.jpeg)
![](/images/menus/one_time_boot3.jpeg)

For example:

* `HD(1,GPT,CF917E4F-3AD1-4293-B4E8-C4EA7BC6FAFD,0x800,0x100000)/\EFI\ubuntu\shimx64.efi`
  means to boot a file named `\EFI\ubuntu\shimx64.efi` from GPT paritioned hard
  disk no. 1 from partition with UUID `CF917E4F-3AD1-4293-B4E8-C4EA7BC6FAFD`
* `PciRoot(0x0)/Pci(0x1D,0x0)/Pci(0x0,0x0)/NVMe(0x1,A7-6C-B1-11-B1-38-25-00)`
  means to boot from NVMe disk namespace 1 and Extended Unique Identifier (EUI)
  `A7-6C-B1-11-B1-38-25-00` which is connected to PCIe Root Port with device
  number 0x1d function 0. As there is no file name appended at the end, the
  UEFI specification automatically looks for `\EFI\BOOT\BOOTX64.EFI` file (for
  x86 64 bit architecture). Note if such file is not present on a FAT32
  partition on the disk, it will not be recognized as bootable.
* `PciRoot(0x0)/Pci(0x14,0x0)/USB(0x15,0x0)` means to boot from USB disk
  connected to USB controller at PCI device 0x14 function 0. The last part
  informs it is an USB device connected to port 0x15 (21 in decimal). As there
  is no file name appended at the end, the UEFI specification automatically
  looks for `\EFI\BOOT\BOOTX64.EFI` file (for x86 64 bit architecture).  Note
  if such file is not present on a FAT32 partition on the disk, it will not be
  recognized as bootable.
* `MemoryMapped(0xB,0x860000,0x15FFFFF)/FvFile(7C04A583-9E3E-4F1C-AD65-E05268D0B4D1)`
  points to UEFI Shell application inside the UEFI Payload binary which has
  been loaded into memory at address range (0x860000 - 0x15FFFFF). The exact
  file to be loaded is indicated by `FvFile` and the file GUID
  `7C04A583-9E3E-4F1C-AD65-E05268D0B4D1`

There are many others `DevicePaths` defined in [UEFI Specification](https://uefi.org/specifications).
If you are interested in decoding those, read through the specification
carefully.
