# Firmware update

Following documentation describe process of Dasharo open-source firmware
update.

## OS booting

For simplicity we using network boot [netboot.xyz from USB](https://netboot.xyz/docs/booting/usb).

Boot system from USB:

* From section `Tools` choose `Utilities (64-bit)`
* Then from section `netboot.xyz tools` choose `Kernel cmdline params`
* You should see prompt `Enter kernel cmdline parameters`
* Type: `iomem=relaxed` and ++enter++
* Use ++esc++ to get back to netboot.xyz main menu
* From section `Distributions` choose `Live CDs`, then `Debian`, `Debian Live
  11 (bullseye)` and `Debian 11 (Core)`

**NOTE**: If trustworthiness of that solution is in question please note
netboot.xyz can be [self-hosted](https://netboot.xyz/docs/selfhosting).

## Get Dasharo

Download the Dell OptiPlex 7010/9010 Dasharo from [release section](releases.md#binaries)
or [build from source](building-manual.md).
