# Dasharo Product Guidelines: SMBIOS Information

## Introduction

This document describes the guidelines for filling in the SMBIOS fields in
devices supported by Dasharo. It is meant to be used primarily as a reference
for Dasharo developers.

## BIOS Information (Type 0)

### Vendor field

The vendor field is always set as follows:

```
3mdeb Embedded Systems Consulting
```

### Version field

The BIOS version string is defined as follows:

```bash
Dasharo ([major_framework]+[minor_framework]) v[version]
```

- `major_framework` refers to the primary framework in which the firmware is
  developed, e.g. `coreboot` or `edk2`.

- `minor_framework` is the secondary framework, a supporting component for the
  primary framework, e.g. a coreboot payload. May not always be used, e.g. if
  `edk2` is used as the primary framework.

*For TianoCore UEFIPayload, we use the simpler and more recognizable UEFI name.*

Examples:

```bash
Dasharo (coreboot+UEFI) v1.0.0    - for coreboot-based builds with TianoCore UEFIPayload
Dasharo (coreboot+SeaBIOS) v1.0.0 - for coreboot-based builds with SeaBIOS payload
Dasharo (coreboot+Heads) v1.0.0   - for coreboot-based builds with Heads payload
Dasharo (edk2) v1.0.0             - for plain edk2-based builds
```

For the version number fields, refer to [Versioning](../versioning).

## System Information (Type 1)

### Devices with an existing BIOS implementation

In this case, set all the fields that are relevant (excluding BIOS version and
vendor) to the same values as the stock firmware.

To obtain SMBIOS values from the stock firmware, either:

- Obtain the logs from the machin from the cloud
- Run `dmidecode -t 1` on the machine itself

### Devices with no existing BIOS implementation

In the case where the device does not have an existing supported BIOS or the
client chooses to use different SMBIOS fields (e.g. to make it easier to
differentiate devices), refer to the
[SMBIOS specification](https://www.dmtf.org/sites/default/files/standards/documents/DSP0134_3.5.0.pdf).
