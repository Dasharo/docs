# Firmware update

**Please read the [overview page](overview.md) first!**

Following documentation describe process of Dasharo open-source firmware
update.

## OS booting

For simplicity we using network booted 
[Dasharo Tools Suite](../../../common-coreboot-docs/dasharo_tools_suite).

### Dasharo (coreboot+SeaBIOS) update

* Attach a wired network cable to the device's Ethernet port
* Power on the device, holding down the Boot Menu entry key (ESC)
* In the Boot Menu, select the `iPXE` option
* In the Network Boot menu, select the `ipxe shell` option
* Obtain address through DHCP or configure network connection in other way:
```console
dhcp net0
```

* Chainload Dasharo Tools Suite:
```console
chain http://boot.3mdeb.com/dts.ipxe
```

* Login as `root` (no password)
* Download the Dell OptiPlex 7010/9010 Dasharo from [release
  section](releases.md#binaries) or [build from source](building-manual.md).
* Flash it using:
```console
sudo flashrom -p internal --ifd -i bios -i me -w <dasharo_optiplex_9010_firmware>
```

Please note that not using `-i bios -i me` may lead to 
[this issue](faq/#cpu-was-replace-warm-reset-required-loop).
