# Overview

The Vault is a small form network appliance built for use as a firewall /
router, virtualization platform, a daily-driven personal computer, and more.
The VP46XX is the second platform of the Vault Pro series with higher
performance and newer technology than the original FW6 series.

![](/images/VP4630_banner-1.jpg)

The VP46XX features an Intel 10th Generation CPU, 2x DDR4 DIMM modules, 6x
Intel i225-V 2.5G Ethernet ports, PCIe x4/SATA NVMe storage, LPC TPM, M.2 WIFI
and WWAN slots.

* VP4630 - Intel Core i3-10110U
* VP4650 - Intel Core i5-10210U
* VP4670 - Intel Core i7-10810U (both v1 and v2 versions, see the
  [Intel FSP repo for details](https://github.com/intel/FSP/tree/master/CometLakeFspBinPkg#differentiating-cometlake1-and-cometlake2))

> Starting with Dasharo [v1.0.19](releases.md#v1019-2022-12-08) Intel ME
> (Management Engine) is
> [soft-disabled](../../osf-trivia-list/me.md#soft-disabling-me).

For more information please refer to the references below.

## References

* [Buy VP4630 in Protectli shop](https://protectli.com/product/vp4630/)

## Documentation sections

* [Releases](releases.md) - groups information about all releases.
* [Building manual](building-manual.md) - describes how to build Dasharo for
    NovaCustom NV4x.
* [Initial deployment](initial-deployment.md) - describes initial Dasharo
    deployment methods (i. e. flashing new firmware) for Protectli VP46xx.
* [Firmware update](firmware-update.md) - explains supported Dasharo
    open-source firmware update methods.
* [Recovery](recovery.md) - gathers information on how to recover the platform
    from potential failure.
* [Hardware configuration matrix](hardware-matrix.md) - describes the
    platform's hardware configuration used during the Dasharo firmware
    validation procedure.
* [Test matrix](test-matrix.md) - describes validation scope used during
    Dasharo firmware validation procedure.
* [Post-installation setup](../protectli-post-install.md)
