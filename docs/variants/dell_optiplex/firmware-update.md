# Firmware update

**Please read the [overview page](overview.md) first!**

Following documentation describe process of Dasharo open-source firmware
distribution update.

## OS booting

For simplicity we recommend using network booted
[Dasharo Tools Suite](../../../dasharo-tools-suite/overview).

### Dasharo (coreboot+SeaBIOS) and Dasharo (coreboot+UEFI) update

* Make sure a wired network cable to the device's Ethernet port
* Perform DTS network boot
    - Dasharo (coreboot+SeaBIOS)
        * While booting enter SeaBIOS menu using ++esc++
        * Choose option `iPXE (PCI 00:19.0)`
    - Dasharo (coreboot+UEFI)
        * Press F7 and choose iPXE Network boot
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
[this issue](faq.md#cpu-was-replaced-warm-reset-required-loop)
