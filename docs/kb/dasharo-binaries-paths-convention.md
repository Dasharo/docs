# Dasharo Binaries Paths Convention

Dasharo firmware binaries are available to download on [dl.3mdeb.com][dl.3mdeb.com]
and [dlui.dasharo.com][dlui.dasharo.com]. These sources are being managed
- manually
- using semi-manual automation
- fully automated CI

The objective of this document is to describe a standard convention of the
directory tree and binary names used in Dasharo sources. It will make it easier
to navigate them and find the releases one is in interested in.

## Directories Convention

The standardised path to a release directory is as follows:

`/<vendor>/<model>/<framework>[_payload]/<version>/`

where:
- `<vendor>` - hardware vendor, like `novacustom`, `protectli`, `hardkernel`,
  `pcengines`
- `<model>` - Precise device model, like `v540tu`, `vp6670`, `odroid-h4`,
  `apu4`
- `<framework>` - firmware framework, like `coreboot`, `slimbootloader`, `heads`
- `[_payload]` - optional, firmware payload, like `_uefi`, `_heads`, `_seabios`
- `<version>` - Dasharo version, like `v0.9.0`, `v1.7.2-rc1`

Example, path to the v1.0.0 release binaries for Novacustom V540TU laptop:
- `/novacustom/v540tu/coreboot_uefi/1.0.0/`

### Motivation

#### <framework>[_payload]

Historically, the firmware framework and payload were generally not present in
the paths, which looked like `/<platform_family>/<version>/`.
When the support for new frameworks and payloads appeared, new directories
started to appear, like `/<platform_family>/heads/<version>/` or
`/<platform_family>/slimbootloader/<version>/` which made the paths
inconsistent with the older releases.

To fix this inconsistency issue the framework and (optional) payload will
always be there, even if a platform has only support for a single
framework/payload combination to reduce the ambiguity.

#### <vendor>/<model>

The idea to separate the `<platform_family>` into the vendor and specific models
has a couple reasons behind it:
1. the number of combinations of vendor, microarchitecture and model family
   resulted in too many directories on a single level
1. knowing just a model name it could be not that obvious which family
   it is supposed to belong to
1. the firmware binaries for all the models from a family could be, or not be
   compatible with the whole family, it could also change with releases and
   require changing the directory structure
1. it was not clear how to release the firmware for just one device from a
   family

By separating the `vendor` and `model` into independent fields all the issues
above are solved. An additional bonus is that the user searching for the
binaries doesn't need to know technical details like the microarchitecture
of their CPU, just the name of the producer and the model of the device.

[dl.3mdeb.com]: https://dl.3mdeb.com
[dlui.dasharo.com]: https://dlui.dasharo.com

## Binary Names Convention

To reduce the confusion and risk of mixing up binaries and allow for creating
multiple variants of a single binary without inconsistencies, the name of the
binary is also being standardised, and looks like:

`<vendor>_<model>_<framework>[_<payload>]_<version>[_extra].<extension>`

where:
- `<vendor>` - hardware vendor, like `novacustom`, `protectli`, `hardkernel`,
  `pcengines`
- `<model>` - Precise device model, like `v540tu`, `vp6670`, `odroid-h4`,
  `apu4`
- `<framework>` - firmware framework, like `coreboot`, `slimbootloader`, `heads`
- `[_payload]` - optional, firmware payload, like `_uefi`, `_heads`, `_seabios`
- `<version>` - Dasharo version, like `v0.9.0`, `v1.7.2-rc1`
- `[_extra]` - optional additional info, like `_dev_signed`, `_btg_provisioned`,
  `_eom`
- `<extension>` - `rom` for normal binaries, `cap` for UEFI Capsules, `cab` for
  FWUPD cabinets etc.

### Motivation

This is especially important for the 3mdeb employees or users which flash their
devices often. Every binary should contain all the information required to
distinguish it from any other binary to reduce the risk of bricking the device
or other mishaps during flashing.
