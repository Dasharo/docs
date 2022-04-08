# NovaCustom fwupd/LVFS support service

## Introduction

This document contains the report of the discovery of the most appropriate
fwupd/LVFS firmware update method, including potential risks and roadblocks.

### Device specification

NovaCustom NV4x system firmware

- Intel i7-1165G7 (Tiger Lake ULV platform)
- Samsung 980PRO NVMe SSD
- 2x SO-DIMM DDR4 system memory
- Optional NVIDIA discrete graphics
- Dasharo coreboot-based firmware
- Firmware stored on a SPI flash chip, flashable internally via flashrom

### Update protocol

- The device is flashable internally via flashrom
- No special unlocks necessary for flashing the required BIOS flash portions
  (only requirement is that UEFI Secure Boot is disabled while updating)

### Feasibility analysis

- Tiger Lake-U is supported in flashrom
  + Present since commit <https://github.com/flashrom/flashrom/commit/93b01904db607ef8169047e68e376dcda1bd7fbe>,
      not yet released to stable as of 14.01.2022
- flashrom is supported in fwupd
  + flashrom plugin is enabled by default in many common desktop Linux
      distributions, including Ubuntu (starting with 21.10) and Arch Linux
  + enabling a device in the flashrom plugin is a matter of adding
      device-specific entries to the plugin quirk list
- Potential risk: vboot support in fwupd
  + flashrom supports flashing vboot rw slots, which are coreboot images
      located within the BIOS partition of the flash
  + however, fwupd only implements flashing the entire BIOS region of the SPI
      flash, which includes other firmware components such as vboot keys,
      vboot recovery partition and user settings
  + the device currently has vboot partially implemented - the BIOS flash
      is not protected and the binaries are signed with (public) developer keys
  + this means we can currently update the BIOS using the traditional fwupd
      update path
  + once we decide to change the vboot keys and lock down the rest of the,
      flash, proper vboot support will need to be implemented in fwupd
  + until then, it will not be possible to enable vboot fully

### Further steps: Vboot support

- In case full vboot support in fwupd is desired, the following are currently
  missing and need to be implemented:
  + Support reading and processing VBNV (Vboot non-volatile store) data in
      fwupd:
    - this store contains information about the current vboot state,
          e.g. currently booted slot (A/B/Recovery), recovery reason, firmware
          signature verification status. This information is stored in CMOS, but
          the exact offset varies by device - so a method for determining the offset
          is also required.
    - For Google Chromebooks, this offset is exposed in a Chromebook-specific
          ACPI device which we cannot use in non-Chromebook device. An alternative
          interface or possibly a quirk in fwupd's flashrom plugin will need to be
          added (though this approach is not preferred by fwupd maintainers).
  + Support for flashing fmap regions in fwupd's flashrom plugin:
    - currently,
          fwupd only attempts to read flash layout from the Intel Flash Descriptor
          located in the flash. This only allows fwupd to flash the entire BIOS
          region, while vboot requires only a portion of the BIOS partition to be
          updated at a given time, with some of the BIOS partition being read-only.
          This means that with vboot fully enabled, updating will fail by attempting
          to write to a read-only portion of the flash.
    - Vboot partitions (slots) are a subset of the bios partition and are defined
          in FMAP (flashmap). Support for it will need to be implemented in fwupd
          (possible by utilizing libflashrom).
          Additionally, some user settings like boot order and setup options are
          stored in a separate FMAP region, so implementing FMAP support in fwupd
          will allow us to preserve them across firmware updates.
  + Vboot A/B slot support
    - In Google Chromebooks, the firmware updater
          only updates one slot at a time and if it succeeds (the device reboots
          into it successfully and works stably), then it will also update the other
          slot to the same (now confirmed good) firmware. fwupd does not currently
          support anything like this, so support for it will also need to be
          implemented.
  + Prior work:
    - <https://github.com/fwupd/fwupd/pull/1370>
    - <https://github.com/fwupd/fwupd/pull/1481>
    - <https://lkml.org/lkml/2019/11/28/291>
