# Versioning

Dasharo Releases are versioned using [Semantic Versioning](https://semver.org/)
and [Keep A Changelog](https://keepachangelog.com/en/1.0.0/) to document
changes introduced in new releases.

Major version zero (0.y.z) is for initial development and may not support all
Dasharo Quality Criteria.

The only way to map Dasharo Version to version of Open Source Firmware
framework or other components included in Dasharo Release is through release
notes. Link to Dasharo Release Notes for your hardware platform can be found in
[Hardware Compatibility List](../variants/hardware-compatibility-list.md)
section.

## Signing keys

In Dasharo we use following rules for keys:

* GPG RSA 4096 for signing and authentication and subkey for encryption
* There few types of naming conventions, which define `Real Name` field and
  chain of trust schemes:
    - Software:
        - Real Name: `<name> open-source software relase <version> signing key`
        - Signing key: `3mdeb Open Source Software Master Key <contact@3mdeb.com>`
    - Firmware:
        - Real Name: `<name> open-source firmware relase <version> signing key`
        - Signing key: `3mdeb Dasharo Master Key`
    - PC Engines (firmware exception):
        - Real Name: `PC Engines open-source firmware relase <version> signing key`
        - Signing key: `3mdeb Open Source Firmware Master Key <contact@3mdeb.com>`
    - Dasharo firmware produced by 3mdeb:
        - Real Name: `Dasharo release <version> compatible with <name> signing key`
        - Signing key: `3mdeb Dasharo Master Key`
    - For Dasharo firmware produced by 3mdeb on customer's behalf:
        - Real Name: `Dasharo open-source firmware <version> for <name> signing key`
        - Signing key: `3mdeb Dasharo Master Key`

`<name>` typically is in form `<vendor> <model>` or just `<vendor>` if we
release firmware for whole line of products which can be support in one binary
e.g. PC Engines. Examples:

- `Dell OptiPlex 7010/9010`
- `ASUS KGPE-D16`
- `MSI MS7D25`
- `Novacustom`
- `Tuxedo`

Most recent status should be reflected in
[3mdeb-secpack](https://github.com/3mdeb/3mdeb-secpack) repository.

