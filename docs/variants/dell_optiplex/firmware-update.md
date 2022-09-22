# Firmware update

**Please read the [overview page](overview.md) first!**

Following documentation describe process of Dasharo open-source firmware
distribution update.

## OS booting

For simplicity we recommend using network booted
[Dasharo Tools Suite](../../../common-coreboot-docs/dasharo_tools_suite).

### Dasharo (coreboot+SeaBIOS) update

* Make sure a wired network cable to the device's Ethernet port
* Boot platform and from SeaBIOS menu choose Dasharo Network Boot Menu
* In the Dasharo Network Boot Menu, select the `Dasharo Tools Suite` option
* Enter shell using option `9)`
* Download the Dell OptiPlex 7010/9010 Dasharo from
  [release section](releases.md#binaries) or
  [build from source](building-manual.md).
* Flash it using:

```console
flashrom -p internal --ifd -i bios -w <dasharo_optiplex_9010_firmware>
```

Please note that not using `-i bios` may lead to
[this issue](faq.md#cpu-was-replace-warm-reset-required-loop)
