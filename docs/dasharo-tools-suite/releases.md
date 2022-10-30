# Release Notes

Following Release Notes describe status of Open Source Software development for
Dasharo Tools Suite.

For details about our release process please read
[Dasharo Standard Release Process](../dev-proc/standard-release-process.md).

<center>
[Subscribe to Dasharo Tools Suite Newsletter]
[newsletter]{.md-button .md-button--primary .center}
</center>

[newsletter]: https://newsletter.3mdeb.com/subscription/ttzqCq9fy

## v1.1.0

### Images

* [USB bootable DTS v1.1.0 image](https://3mdeb.com/open-source-firmware/DTS/v1.1.0/dts-base-image-ce-v1.1.0.wic.gz)
* [sha256](https://3mdeb.com/open-source-firmware/DTS/v1.1.0/dts-base-image-ce-v1.1.0.wic.gz.sha256)
* [sha256.sig](https://3mdeb.com/open-source-firmware/DTS/v1.1.0/dts-base-image-ce-v1.1.0.wic.gz.sha256.sig)

  See how to verify hash and signature on [this video.](https://youtu.be/oTx2iStxXOE)

### Changelog

* Added [Dasharo zero-touch
  initial deployment](./documentation.md#dasharo-zero-touch-initial-deployment)
  for couple of supported platform
* Added multiple HCL report improvements, e.g. dump informations about TPM, ME
* Refactored Dasharo Tools Suite [documentation](./overview.md)
* Added possibility to rollback using firmware dumped in HCL report
* Added documentation about [building Dasharo Tools Suite
  image](./documentation.md#building)
* Deploying artifacts on [boot.dasharo.com](https://boot.dasharo.com/yocto/dts/)
* Sharing build cache on [cache.dasharo.com](https://cache.dasharo.com/yocto/dts/)

## v1.0.2

### Images

* [USB bootable DTS CE v1.0.2 image](https://3mdeb.com/open-source-firmware/DTS/v1.0.2/dts-base-image-ce-v1.0.2.wic.gz)
* [sha256](https://3mdeb.com/open-source-firmware/DTS/v1.0.2/dts-base-image-ce-v1.0.2.wic.gz.sha256)
* [sha256.sig](https://3mdeb.com/open-source-firmware/DTS/v1.0.2/dts-base-image-ce-v1.0.2.wic.gz.sha256.sig)

  See how to verify hash and signature on [this video.](https://youtu.be/oTx2iStxXOE)

### Changelog

* Added new vendor specific menu entry which is displayed only on supported
  platforms, for now NovaCustom menu was added for NV4x and NS50 70MU laptops
* DTS version is now printed in the main menu
* `ec_transition` script now supports NV4XMB,ME,MZ laptops and automatically
  download firmware used for transition both for NV4x and NS5x laptopts,
  [firmware transition](documentation.md#ec-transition)
  documentation is updated
* Added kernel configuration to silence terminal logs by default (change loglevel
  to 1)
* Enabled GOOGLE_MEMCONSOLE_COREBOOT kernel configuration to ease getting
  firmware logs

## v1.0.1

### Images

* [USB bootable DTS CE v1.0.1 image](https://3mdeb.com/open-source-firmware/DTS/v1.0.1/dts-base-image-ce-v1.0.1.wic.gz)
* [sha256](https://3mdeb.com/open-source-firmware/DTS/v1.0.1/dts-base-image-ce-v1.0.1.wic.gz.sha256)
* [sha256.sig](https://3mdeb.com/open-source-firmware/DTS/v1.0.1/dts-base-image-ce-v1.0.1.wic.gz.sha256.sig)

  See how to verify hash and signature on [this video.](https://youtu.be/oTx2iStxXOE)

### Changelog

* Added system76_ectool to enable Embedded Controller [firmware updating](./documentation.md#ec-update)
* Added ec_transition script which helps with full Dasharo/Embedded Controller
  [firmware transition](./documentation.md#ec-transition) for NS50 70MU and NS70
  laptops
* First public release: [meta-dts-ce](https://github.com/Dasharo/meta-dts-ce)

## v1.0.0

### Images

* [USB bootable DTS CE v1.0.0 image](https://3mdeb.com/open-source-firmware/DTS/v1.0.0/dts-base-image-ce-v1.0.0.wic.gz)
* [sha256](https://3mdeb.com/open-source-firmware/DTS/v1.0.0/dts-base-image-ce-v1.0.0.wic.gz.sha256)

  ```bash
  # assuming all files have been downloaded to the same directory without
  # changing names
  sha256sum -c [sha256 file]
  ```

### Changelog

* Auto-login functionality
* User menu
* [Dasharo HCL Report](../glossary.md#dasharo-hardware-compatibility-list-report)
  which add the ability to automatically dump device information and send it to
  3mdeb servers
* Possibility to manually [update the Dasharo
  firmware](./documentation.md#firmware-update)
* [Bootable via iPXE](./documentation.md#bootable-over-network)
* [Bootable via USB](./documentation.md#bootable-usb-stick)
* Tested on NovaCustom NV4x, Dell OptiPlex 7010/9010
