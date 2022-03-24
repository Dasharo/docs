# Dasharo Tools Suite

## Introduction

Dasharo Tools Suite (DTS) is a set of tools for deploying, updating and
maintaining firmware on Dasharo supported devices. DTS is integrated into the
firmware in Dasharo supported devices and can be used to update the firmware
even when no OS is installed.

## Requirements

- Dasharo device with DTS functionality integrated
- Wired network connection
- Secure Boot disabled

## Launching DTS

To access Dasharo Tools Suite:

- Attach a wired network cable to the device's Ethernet port
- Power on the device, holding down the Boot Menu entry key
- In the Boot Menu, select the `iPXE Network Boot` option
- In the Network Boot menu, select the Dasharo Tools Suite option
- In the DTS menu, select the Dasharo Tools Suite again

The DTS shell will now appear.

## Using DTS

Within DTS, you may use the `flashrom` and `fwupdmgr` utilities to update,
downgrade, or reinstall your firmware.

To update your firmware to the latest version:

```bash
fwupdmgr update
```
