# Overview

The Vault Pro is a small form network appliance built for use as a firewall
/ router, virtualization platform, a daily-driven personal computer,
and more. The VP2420 is based on a 4 x 2.5 G network port design that leverages
a low power, but versatile Intel Celeron J6412 CPU.

![](/images/VP2420.png)

The VP2420 can accommodate up to 32 GB DDR4 RAM and 2 TB M.2 SATA SSD
storage drive (Note: The VP2420 supports M.2 SATA drives, not NVMe
drives). The built-in 8 GB eMMC module can be used for booting a
light-weight OS for example, or for use as optional storage.

VP2410 specification:

* Intel Celeron® J6412 Quad Core at 2 GHz (Burst up to 2.6 GHz)
* 4 Intel® 2.5 Gigabit Ethernet NIC ports
* M.2 SATA SSD Slot (Note: This device does not support NVMe drives)
* 8 GB eMMC module on board
* Intel® AES-NI support
* Fanless and Silent
* Included 12v Power Supply, VESA mount kit, Serial Console Cable,
SATA data and power cables for internal SSD, Quick Start Guide

> Starting with Dasharo [v1.2.0](releases.md#v120-2024-05-16), Intel ME
> (Management Engine) is [soft-disabled](../../osf-trivia-list/me.md#soft-disabling-me)
> by default.

For more information please refer to the references below.

## References

* [Protectli knowledge base](https://kb.protectli.com/)
* [Buy VP2420 in Protectli shop](https://eu.protectli.com/product/vp2420/)

## Documentation sections

* [Releases](releases.md) - groups information about all releases.
* [Building manual](building-manual.md) - describes how to build Dasharo for
    Protecli 2420.
* [Initial deployment](initial-deployment.md) - describes initial Dasharo
    deployment methods (i. e. flashing new firmware) for Protectli VP2420.
* [Recovery](recovery.md) - gathers information on how to recover the platform
    from potential failure.
* [Hardware configuration matrix](hardware-matrix.md) - describes the
    platform's hardware configuration used during the Dasharo firmware
    validation procedure.
* [Test matrix](test-matrix.md) - describes validation scope used during
    Dasharo firmware validation procedure.
