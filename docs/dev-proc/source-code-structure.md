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

Dasharo Release tags in git repository use format: `<platform>_vX.Y.Z`

## New platform support

Branch for new platform should be created from most recent`master` branch tag.
If there is justified need to create support for new board at arbitrary
non-tagged commit developer should mark this commit with `<platform>_v0.0.0`
tag.

## Force-pushes rules

Force-pushes to `<platform>/rel_vX.Y.Z` or `<platfrom>/<feature>` are
unconditionally forbidden.

For other branches force-pushes are forbidden with following exceptions:
* rebasing - when some other PR is merged to target branch before our does, or
  when upstream's master introduces the same fixes that our branch would
* squashing - to not produce unnecessary "fix indentation" or "add missing
  braces" commits to the history
* (re-)signing commits (both -S and -s) - shouldn't happen, but if it does
  happen it would be better to have it fixed by original author than the person
  that tries to upstream it some time later.
