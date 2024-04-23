# Overview

The Vault is a small form network appliance built for use as a firewall /
router, virtualization platform, a daily-driven personal computer, and more.
The VP6630/VP6650/VP6670 feature an Intel Alder Lake-P CPU, 2x DDR5 SODIMM
memory, Intel i225-V/i226-V 2.5G Ethernet ports, 2x SFP Intel X710, 4x USB-A
ports (1x 3.1, 3x 2.0), one internal USB-A 3.1, 1x USB-C with PD, PCIe NVMe
storage, M.2 WIFI and WWAN slots, 2x serial console over USB-C and RJ45, SPI
TPM, 2 CPU fans.

* VP6630 - Intel® Core™ i3 -1215U
* VP6650 - Intel® Core™ i5 -1235U
* VP6670 - Intel® Core™ i7 -1255U

> On VP66xx Intel ME (Management Engine) is disabled by using the
> [HAP bit](../../osf-trivia-list/me.md#hap-altmedisable-bit-aka-disabling-me).

## Documentation sections

* [Releases](releases.md) - groups information about all releases.
* [Building manual](building-manual.md) - describes how to build Dasharo for
  Protectli VP6630/VP6650/VP6670.
* [Initial deployment](initial-deployment.md) - describes initial Dasharo
  deployment methods (i. e. flashing new firmware) for Protectli
  VP6630/VP6650/VP6670.
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
