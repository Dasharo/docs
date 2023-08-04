# Dasharo Product Guidelines: SMBIOS Information

## Introduction

This document describes the guidelines for filling in the SMBIOS fields in
devices supported by Dasharo. It is meant to be used primarily as a reference
for Dasharo developers.

## BIOS Information (Type 0)

### Vendor field

The Vendor field, for firmware with release date after 13 January 2022,
is set as follows:

```bash
3mdeb
```

For firmware with release date before 13 January 2022:

```bash
3mdeb Embedded Systems Consulting
```

### BIOS Version field

The BIOS Version string is defined as follows:

```bash
Dasharo ([major_framework]+[minor_framework]) v[version]
```

- `major_framework` refers to the primary framework in which the firmware is
  developed, e.g. `coreboot` or `UEFI`.
- `minor_framework` is the secondary framework, a supporting component for the
  primary framework, e.g. a coreboot payload. May not always be used, e.g. if
  `edk2` is used as the primary framework.
- `version` means version according to official
  [Dasharo Versioning](versioning.md) documentation.

_For [TianoCore UEFIPayloadPkg](https://github.com/Dasharo/edk2/tree/dasharo/UefiPayloadPkg),
we use the simpler and more recognizable UEFI name._

Examples:

- `Dasharo (coreboot+UEFI) v1.0.0` - for coreboot-based builds with TianoCore UEFIPayload
- `Dasharo (coreboot+SeaBIOS) v1.0.0` - for coreboot-based builds with SeaBIOS payload
- `Dasharo (coreboot+Heads) v1.0.0` - for coreboot-based builds with Heads payload
- `Dasharo (UEFI) v1.0.0` - for plain edk2-based builds

## System Information (Type 1)

### Devices with an existing BIOS implementation

In this case, set all the fields that are relevant (excluding BIOS version and
vendor) to the same values as the stock firmware.

To obtain SMBIOS values from the stock firmware, either:

- Obtain the `fwdump-docker` logs from 3mdeb cloud
- Run `dmidecode -t 1` on the machine itself

### Devices with no existing BIOS implementation

In the case where the device does not have an existing supported BIOS or the
client chooses to use different SMBIOS fields (e.g. to make it easier to
differentiate devices), refer to the
[SMBIOS specification v3.5.0](https://www.dmtf.org/sites/default/files/standards/documents/DSP0134_3.5.0.pdf).
