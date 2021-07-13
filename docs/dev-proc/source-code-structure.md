# Source code structure

Every repository forked and maintained by Dasharo Release Team has following
branch structure:

* `master` - follows upstream project master branch
* `<platform>/release` - contains all code releases for given `<platform>`,
  list of supported platforms is in [Hardware Compatibility List](../variants/hardware-compatibility-list.md) section
* `<platform>/rel_vX.Y.Z` - release branch for version X.Y.Z
* `<platform>/develop` - contains most recent development and is periodically
  synced with `master` branch
* `<platform>/<feature>` - tracks development of platform specific feature

`<platform> = <coreboot_mainboard_vendor>_<coreboot_mainboard_model>` if
platform is supported by coreboot, otherwise we use common sense and available
information about hardware.

## Tags

Dasharo Release tags in git repository use format: `<platform>_vx.y.z`

