# Overview

The Vault Pro is a small form network appliance built for use as a firewall
/ router, virtualization platform, a daily-driven personal computer,
and more. The VP2410 is based on a 4 network port design that leverages
a low power, but versatile Intel Celeron J4125 CPU.

![](/images/VP2410.png)

The VP2410 can accommodate up to 16GB DDR4 RAM and 2TB m.2 SATA SSD
storage drive. The built-in 8GB eMMC module can be used for booting a
light-weight OS for example, or for use as optional storage.

VP2410 specification:

* Intel Celeron® J4125 Quad Core at 2 GHz (Burst up to 2.7 GHz)
* 4 Intel® Gigabit Ethernet NIC ports
* 8GB eMMC module on board
* Intel® AES-NI support
* Fanless and Silent
* Included 12v Power Supply, VESA mount kit, Serial Console Cable,
SATA data and power cables for internal SSD, Quick Start Guide

> On VP2410 Intel ME (Management Engine) is not supported by coreboot causing
> Intel ME to enter recovery mode giving similar results to disabled ME.

For more information please refer to the references below.

## References

* [Protectli knowledge base](https://kb.protectli.com/)
* [Buy VP2410 in Protectli shop](https://eu.protectli.com/product/vp2410)

## Documentation sections

* [Releases](releases.md) - groups information about all releases.
* [Building manual](building-manual.md) - describes how to build Dasharo for
    Protecli 2410.
* [Initial deployment](initial-deployment.md) - describes initial Dasharo
    deployment methods (i. e. flashing new firmware) for Protectli VP2410.
* [Recovery](recovery.md) - gathers information on how to recover the platform
    from potential failure.
* [Hardware configuration matrix](hardware-matrix.md) - describes the
    platform's hardware configuration used during the Dasharo firmware
    validation procedure.
* [Test matrix](test-matrix.md) - describes validation scope used during
    Dasharo firmware validation procedure.
