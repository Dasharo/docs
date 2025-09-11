# Supported hardware

Following is up to date list of hardware platforms supported by Dasharo
open-source firmware distribution.

## Emulation

* Following emulation targets are supported under **Dasharo Community Support**:

    - [QEMU Q35](qemu_q35/overview.md)

## Network appliance

* Following network appliances are supported under **Dasharo Support Package**:

    - [Protectli FW6](../unified/protectli/overview.md#fw6)
    - [Protectli v1000-series](../unified/protectli/overview.md#v1000-series)
    - [Protectli VP2410](../unified/protectli/overview.md#vp2410)
    - [Protectli VP2420](../unified/protectli/overview.md#vp2420)
    - [Protectli VP46XX](../unified/protectli/overview.md#vp46xx)
    - [Protectli VP66XX](../unified/protectli/overview.md#vp66xx)

* Following network appliances are supported under **Dasharo Pro Package**:

    - [Dasharo (coreboot+UEFI) Pro Package for Network Appliance](https://shop.3mdeb.com/product/1-year-dasharo-pro-package-for-network-appliance/)
        + [PC Engines APU 2/3/4/6 platforms](../variants/pc_engines/releases_uefi.md)
        + [Hardkernel Odroid H4+](../variants/hardkernel_odroid_h4/releases.md)
    - [Dasharo (coreboot+SeaBIOS) Pro Package for Network Appliance](https://shop.3mdeb.com/product/1-year-dasharo-pro-package-for-network-appliance-corebootseabios/)
        + [PC Engines APU 2/3/4/6 platforms](../variants/pc_engines/releases_seabios.md)
    - [Dasharo (Slim Bootloader+UEFI) Pro Package for Network Appliance](https://shop.3mdeb.com/product/dasharo-slim-bootloaderuefi-pro-package-for-network-appliance/)
        + [Hardkernel Odroid H4+](../variants/hardkernel_odroid_h4/releases_sbl.md)

## Laptops

* Following laptops are supported under **Dasharo Support Package**:

    - [NovaCustom V54 14th Gen](../unified/novacustom/overview.md)
    - [NovaCustom V56 14th Gen](../unified/novacustom/overview.md)
    - [NovaCustom NV4x 12th Gen](../unified/novacustom/overview.md)
    - [NovaCustom NS5x/7x 12th Gen](../unified/novacustom/overview.md)
    - [NovaCustom NV4x 11th Gen](../unified/novacustom/overview.md)
    - [NovaCustom NS5x/7x 11th Gen](../unified/novacustom/overview.md)

* Following laptops are supported under **Dasharo Pro Package**:

    - [Dasharo (coreboot+UEFI) transition to (coreboot+Heads) for Laptops](https://shop.3mdeb.com/product/dasharo-corebootuefi-pro-package-upgrade-to-corebootheads-for-laptop-users/)
        + [NovaCustom V540TU 14th Gen](https://docs.dasharo.com/variants/novacustom_v540tu/releases_heads/)
        + [NovaCustom V560TU 14th Gen](https://docs.dasharo.com/variants/novacustom_v560tu/releases_heads/)
        + [NovaCustom NV4x 12th Gen](https://docs.dasharo.com/variants/novacustom_nv4x_adl/releases_heads/)

* Following laptops are supported under **Dasharo Community Support**:

    - [Tuxedo IBS15](tuxedo_ibs15/releases.md)

## Desktop

* Following desktops are supported under **Dasharo Support Package**:

    - [NovaCustom NUC BOX 14th Gen](../unified/novacustom/overview.md)

* Following desktops are supported under **Dasharo Pro Package**:

    - [Dasharo (coreboot+UEFI) Pro Package for Desktop](https://shop.3mdeb.com/shop/dasharo-pro-package/1year-desktop/)
        + [Dell OptiPlex](dell_optiplex/overview.md)
        + [MSI PRO Z690-A](../unified/msi/overview.md)
        + [MSI PRO Z790-P](../unified/msi/overview.md)

* Following desktops are supported under **Dasharo Community Support**:

    - [MSI PRO Z690-A](../unified/msi/overview.md)
    - [MSI PRO Z790-P](../unified/msi/overview.md)

## Workstation

* Following workstations are supported under **Dasharo Community Support**:

    - [Asus KGPE-D16](asus_kgpe_d16/overview.md)
    - [Raptor CS Talos II](talos_2/overview.md)

## Servers

* Following servers are supported under **Dasharo Pro Package**:

    - [Gigabyte MZ33-AR1](gigabyte_mz33-ar1/overview.md)
    - [ASRock Rack SPC741D8-2L2T/BCM](asrock_spc741d8/overview.md)

* Following servers are supported under **Dasharo Community Support**:

    - [Supermicro X11 LGA1151 Series](supermicro_x11_lga1151_series/overview.md)

## Openness comparison

The following table shows the comparison of binary openness between Dasharo and
proprietary firmware. It was generated using the
[Dasharo Openness Score tool](../glossary.md/#dasharo-openness-score).

The table contains the following metrics:

* `Closed-source diff` (the higher negative percentage the better, ideally
  -100% is fully FOSS)
* `Data size diff` - (the amount of data stored in the firmware varies,
  no preference here)
* `Empty space diff` - (the higher positive percentage the better, more free
  space means smaller TCB)

Each metric is calculated using the formula:

```txt
(Dasharo <type> size - Proprietary <type> size) * 100 / Proprietary <type> size
```

`<type>` is replaced by `closed-source`, `data` or `empty space` accordingly.

| Platform | Dasharo Firmware file | Proprietary Firmware file | Closed-source diff [%] | Data size diff [%] | Empty space diff [%] |
| --- | --- | --- | --- | --- | --- |
| MSI MS-7D25 DDR4 | msi_ms7d25_v1.1.4_ddr4.rom | E7D25IMS.1L0 | -27.7 | 153.5 | -18.8 |
| MSI MS-7D25 DDR5 | msi_ms7d25_v1.1.4_ddr5.rom | E7D25IMS.AL0 | -27.8 | 153.4 | -18.8 |
| MSI MS-7E06 DDR4 | msi_ms7e06_v0.9.2_ddr4.rom | E7E06IMS.1F0 | -27.4 | 153.4 | -19.0 |
| MSI MS-7E06 DDR5 | msi_ms7e06_v0.9.2_ddr4.rom | E7E06IMS.AH0 | -27.4 | 149.9 | -19.0 |
| Protectli FW6 | protectli_all_fw6_vault_kbl_v1.0.14.rom | fw6_all_YKR6LV30.bin | -47.0 | 2163.8 | 116.8 |
| Protectli V1210 | protectli_v1210_v0.9.3.rom | v1210_JPL.2LAN.S4G.PCIE.6W.013.bin | -28.4 | 3595.6 | 21.9 |
| Protectli V1211 | protectli_v1211_v0.9.3.rom | v1211_JPL.2LAN.D8G.PCIE.6W.009.bin | -28.4 | 3595.6 | 21.9 |
| Protectli V1410 | protectli_v1410_v0.9.3.rom | v1410_JPL.4LAN.S8GB.PCIE.6W.007B.bin | -28.4 | 3595.6 | 22.0 |
| Protectli V1610 | protectli_v1610_v0.9.3.rom | v1610_JPL.6LAN.D16G.PCIE.007.bin | -28.4 | 3595.7 | 21.9 |
| Protectli VP2420 | protectli_vp2420_v1.2.1.rom | vp2420_YELD4L13P.bin | -25.4 | 4805.6 | -28.0 |
| Protectli VP2430 | protectli_vp2430_v0.9.0.rom | vp2430_PRALNDZ4L10.bin | -39.6 | 17376.5 | 2.1 |
| Protectli VP46XX | protectli_vp4600_v1.2.0.rom | vp4630_v2_YW6L2318.bin | -9.7 | 3790.8 | -72.9 |
| Protectli VP66XX | protectli_vp6600_v0.9.2.rom | vp6630_ADZ6L314.bin | -30.8 | 5152.2 | -28.9 |
| Odroid H4 | hardkernel_odroid_h4_v0.9.0.rom | ADLN-H4_B1.07.bin | -35.5 | 198.4 | -14.3 |
| Novacustom V540TU | novacustom_v54x_mtl_v0.9.0.rom | V5xxTU(32M).09 | -21.9 | -35.4 | -17.0 |
| Novacustom V560TU | novacustom_v56x_mtl_v0.9.0.rom | V5xxTU(32M).09 | -21.9 | -35.4 | -17.0 |
| Novacustom NV4xPZ | novacustom_nv4x_adl_v1.7.2_full.rom | NV4xPZ(32M).03 | -27.6 | -0.8 | 46.8 |
| Novacustom NV4xME_MB | novacustom_nv4x_tgl_v1.5.2.rom | NV4XBX.05 | -30.1 | 3.0 | -24.4 |
| Novacustom NSxxPU | novacustom_ns5x_adl_v1.7.2.rom | NSx0PU(32M).09 | -26.3 | -0.8 | -7.2 |
| Novacustom NS5xMU | novacustom_ns5x_tgl_v1.5.2.rom | NS50_70MU.16N | -30.6 | 2.9 | -23.4 |
