# Versioning

Dasharo Releases are versioned using [Semantic Versioning](https://semver.org/)
and [Keep A Changelog](https://keepachangelog.com/en/1.0.0/) to document
changes introduced in new releases.

Major version zero (0.y.z) is for initial development or first release issued
and may not support all Dasharo Quality Criteria.

The only way to map Dasharo Version to version of Open Source Firmware
framework or other components included in Dasharo Release is through release
notes. Link to Dasharo Release Notes for your hardware platform can be found
in menu on the left side (Supported Hardware->Hardware Model->Releases).

Dasharo Releases can be divided into two categories:

* Dasharo Pro Package Releases (previous Dasharo Supporters Release for
  Dasharo Support Entrance Subscribers)
* Dasharo Community Releases

## Dasharo Pro Package Releases

Dasharo Pro Package subscribers receive firmware updates more
frequently than the community. The number of updates per year depends on the
number of Dasharo Pro Package sold and the availability of other
funding (e.g., NLNet, corporate sponsors, community donations) but is less
than 2 updates per year. Dasharo Pro Package Releases are characterized
by a changing patch version (`z`). Fixes and features introduced in Dasharo
Pro Package Releases will also be available later as Dasharo Community
Releases with public pre-built binaries in the respective release pages. In
short, being a Dasharo Subscriber gives early access to the newest features
and fixes.

[How to become Dasharo Pro Package subscriber?](../ways-you-can-help-us.md#become-a-dasharo-entry-subscription-subscriber)

## Dasharo Community Releases

Dasharo Community Releases are built and published once a year. Each Dasharo
Community Release has a zero patch version (`x.y.0`) and the only changing
number is the minor version `y`. To be up-to-date with latest Dasharo
Community Release updates, one can subscribed to free of charge mailing list
for given hardware platform, for which the link can be found in menu on the
left side (Supported Hardware->Hardware Model->Releases).

## Signing keys

In Dasharo we use following rules for keys:

* GPG RSA 4096 for signing and authentication and subkey for encryption
* There few types of naming conventions, which define `Real Name` field and
  chain of trust schemes:
    - Software:
        + Real Name: `<name> open-source software release <version> signing key`
        + Signing key: `3mdeb Open Source Software Master Key <contact@3mdeb.com>`
    - Firmware:
        + Real Name: `<name> open-source firmware release <version> signing key`
        + Signing key: `3mdeb Dasharo Master Key`
    - PC Engines (firmware exception):
        + Real Name: `PC Engines open-source firmware release <version> signing key`
        + Signing key: `3mdeb Open Source Firmware Master Key <contact@3mdeb.com>`
    - Dasharo firmware produced by 3mdeb:
        + Real Name: `Dasharo release <version> compatible with <name> signing key`
        + Signing key: `3mdeb Dasharo Master Key`
    - For Dasharo firmware produced by 3mdeb on customer's behalf:
        + Real Name: `Dasharo open-source firmware <version> for <name> signing key`
        + Signing key: `3mdeb Dasharo Master Key`

`<name>` typically is in form `<vendor> <model>` or just `<vendor>` if we
release firmware for whole line of products which can be support in one binary
e.g. PC Engines. Examples:

* `Dell OptiPlex 7010/9010`
* `ASUS KGPE-D16`
* `MSI MS7D25`
* `NovaCustom`
* `Tuxedo`

Most recent status should be reflected in
[3mdeb-secpack](https://github.com/3mdeb/3mdeb-secpack) repository.
