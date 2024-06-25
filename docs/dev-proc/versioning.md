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

- Dasharo Pro/Enterprise Package (formerly Dasharo Entry Subscription) Releases
- Dasharo Community Releases

## Dasharo Pro/Enterprise Package Releases

Dasharo Pro/Enterprise Package (formerly Dasharo Entry Subscription)
subscribers receive firmware updates more frequently than the community. The
number of updates per year depends on the number of Dasharo Pro/Enterprise
Package (formerly Dasharo Entry Subscription) sold and the availability of
other funding (e.g., NLNet, corporate sponsors, community donations) but one or
more per year. Dasharo Pro/Enterprise Package (formerly Dasharo Entry
Subscription) Releases are characterized by a changing patch version (`z`).
Fixes and features introduced in Dasharo Entry Subscription Releases will also
be available later as Dasharo Community Releases with public pre-built binaries
in the respective release pages. In short, being a Dasharo Subscriber gives
early access to the newest features and fixes.

[How to become Dasharo Entry Subscription subscriber?](../ways-you-can-help-us.md#become-a-dasharo-entry-subscription-subscriber)

## Dasharo Community Releases

Timeline for Dasharo Community Releases is communicated in [Dasharo
Roadmap](https://github.com/Dasharo/presentations/blob/main/dasharo_roadmap.md)
presentations during [Dasharo User
Group](https://docs.dasharo.com/#events-calendar) events. Each Dasharo
Community Release has a zero patch version (`x.y.0`) and the only changing
number is the minor version `y`. To be up-to-date with latest Dasharo Community
Release updates, one can subscribed to free of charge mailing list for given
hardware platform, for which the link can be found in menu on the left side
(Supported Hardware->Hardware Model->Releases).

## PC Engines releases and its exceptional versioning scheme

Dasharo (coreboot+SeaBIOS) for PC Engines does not adhere to the typical
versioning scheme used by Dasharo, which is semantic versioning. This is due to
a couple of reasons:

- We want to convey that this series of releases is a direct continuation of
  past efforts sponsored by PC Engines and published
  [here](https://pcengines.github.io/). By sticking to that versioning scheme, we
  do not deviate from the agreed pattern and what users are accustomed to.
- We have utilized the same infrastructure, and maintaining versioning
  according to the pattern used by us since 2017 has helped us minimize changes.

The general rule for versioning pattern is as follows: `<coreboot_rel_ver>{.00.}<dasharo_rel_num>`

- `<coreboot_rel_ver>` - changed in February 2024, from x.y.z to YY.MM{.FF},
  where `YY` represents the year, `MM` represents the month, and optional `{.FF}`
  represents the patch number if any hotfix for the given release is created.
- `{.00.}` - if no hotfix exists for the given coreboot release, we add `.00.`
  to reserve space for a potential hotfix on that version.
- `<dasharo_rel_num>` - indicates the number of versions released by the
  Dasharo Team on top of the given coreboot release, starting from `01`, where
  version `00` means no changes were applied on top of the coreboot release.

## Signing keys

In Dasharo we use following rules for keys:

- GPG RSA 4096 for signing and authentication and subkey for encryption
- There few types of naming conventions, which define `Real Name` field and
  chain of trust schemes:
    + Software:
        * Real Name: `<name> open-source software release <version> signing key`
        * Signing key: `3mdeb Open Source Software Master Key <contact@3mdeb.com>`
    + Firmware:
        * Real Name: `<name> open-source firmware release <version> signing key`
        * Signing key: `3mdeb Dasharo Master Key`
    + PC Engines (firmware exception):
        * Real Name: `PC Engines open-source firmware release <version> signing key`
        * Signing key: `3mdeb Open Source Firmware Master Key <contact@3mdeb.com>`
    + Dasharo firmware produced by 3mdeb:
        * Real Name: `Dasharo release <version> compatible with <name> signing key`
        * Signing key: `3mdeb Dasharo Master Key`
    + For Dasharo firmware produced by 3mdeb on customer's behalf:
        * Real Name: `Dasharo open-source firmware <version> for <name> signing key`
        * Signing key: `3mdeb Dasharo Master Key`

`<name>` typically is in form `<vendor> <model>` or just `<vendor>` if we
release firmware for whole line of products which can be support in one binary
e.g. PC Engines. Examples:

- `Dell OptiPlex 7010/9010`
- `ASUS KGPE-D16`
- `MSI MS7D25`
- `NovaCustom`
- `Tuxedo`

Most recent status should be reflected in
[3mdeb-secpack](https://github.com/3mdeb/3mdeb-secpack) repository.
