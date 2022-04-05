# Standard Release Process

Following procedure is generic description of release process of firmware for
supported hardware platforms and targets open-source firmware developers.
Precise steps and any difference from standard process are described in
platform specific documentation.

Description here is, intentionally, open-source firmware framework agnostic
and should be maintained in that way.

## Initial release

For platforms not supported by Dasharo there is need for initial release, which
consist of [Dasharo Common
Base](../../osf-trivia-list/dasharo/#what-is-dasharo-common-base). Initial
release should have established test scope defined in platform [test
matrix](../../unified-test-documentation/overview/#test-matrix) section.

1. Fetch upstream project
1. Checkout branch `<platfrom>/release`
    - `coreboot` - use most recent commit on upstream `master`
    - `edk2` - use most recent stable tag
1. Create branch `<platform>/rel_v0.1.0`
1. Cherry-pick required patches from `dasharo-common-base` branch
1. Apply all other modifications necessary to  provide initial support for
   `<platform>` according to platform test matrix scope.
1. Run platform regression test suite
1. If results are accepted merge it to `<platform>/release` branch
1. Add tag, which should trigger CI and publish binaries
1. Merge release branch to develop

## Regular release

Following procedure applies to platform for which initial release was already
published.

1. Checkout new branch `<platform>/rel_vX.Y.Z` from recent commit on
   `<platfrom>/release` - to understand versioning scheme please read
   [Versioning](versioning.md) section
2. Merge current `<platform>/develop` to `<platform>/rel_vX.Y.Z`
3. Run platform regression test suite
4. Fix all required issues and repeat point 3 until fixed - this doesn't mean
   all tests pass, this mean that approved set passed
5. If results are accepted merge it to `<platform>/release` branch
6. Add tag, which should trigger CI and publish binaries
7. Merge release branch to develop
