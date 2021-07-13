# Source code structure

Every repository forked and maintained by Dasharo Release Team has following
branch structure:

* `master` - follows upstream project master branch
* `<platform>/release` - contains all code releases for given `<platform>`,
  list of supported platforms is in [Hardware Compatibility List](../variants/hardware-compatibility-list.md) section
* `<platform>/develop` - contains most recent development and is periodically
  synced with `master` branch
* `<platform>/<feature>` - tracks development of platform specific feature

