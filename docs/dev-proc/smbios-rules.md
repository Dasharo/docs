# Dasharo Product Guidelines: SMBIOS BIOS Information (Type 0)

2 types of devices may be supported by Dasharo:

- Those that already have a supported firmware implementation available
- Those that do not

In the first case, a device may have drivers available in Windows Update or
firmware via fwupd/LVFS. If that is the case, we want to leverage this support
in Dasharo too. Since fwupd and Windows Update identify devices by (among other
things) SMBIOS contents, we do this by matching as many SMBIOS fields as
possible.

For example, in fwupd, the following SMBIOS fields are used for generating
device GUIDs:

```bash
Computer Information
--------------------
BiosVendor: 3mdeb Embedded Systems Consulting
BiosVersion: Dasharo (coreboot+UEFI) v1.0.0
BiosMajorRelease: 1
BiosMinorRelease: 0
Manufacturer: Notebook
Family: Not Applicable
ProductName: NV4XMB,ME,MZ
ProductSku: Not Applicable
EnclosureKind: a
BaseboardManufacturer: Notebook
BaseboardProduct: NV4XMB,ME,MZ

Hardware IDs
------------
{37b192b9-4fe8-5d20-b4e7-6d00782e2a09}   <- Manufacturer + Family + ProductName + ProductSku + BiosVendor + BiosVersion + BiosMajorRelease + BiosMinorRelease
{bc90b4cf-a507-50c5-bf51-48c26863dc13}   <- Manufacturer + Family + ProductName + BiosVendor + BiosVersion + BiosMajorRelease + BiosMinorRelease
{cf004452-c518-5899-a791-d246db94c413}   <- Manufacturer + ProductName + BiosVendor + BiosVersion + BiosMajorRelease + BiosMinorRelease
{25b6ea34-8f52-598e-a27a-31e03014dbe3}   <- Manufacturer + Family + ProductName + ProductSku + BaseboardManufacturer + BaseboardProduct
{dd71301d-2915-5884-af96-498003ea55bb}   <- Manufacturer + Family + ProductName + ProductSku
{8603f686-41b8-5ea0-bbf8-d3e5cfa9c0ac}   <- Manufacturer + Family + ProductName
{17e12139-ddb8-5e43-ad90-74e69a044051}   <- Manufacturer + ProductSku + BaseboardManufacturer + BaseboardProduct
{cd9d0da1-e88d-5d36-aae5-2ba60e8d0ed6}   <- Manufacturer + ProductSku
{99192755-edd8-5f6d-8c46-e7d9e0b8be5f}   <- Manufacturer + ProductName + BaseboardManufacturer + BaseboardProduct
{0f4d8e7f-9419-5817-a8c5-aa54027c1b35}   <- Manufacturer + ProductName
{17e12139-ddb8-5e43-ad90-74e69a044051}   <- Manufacturer + Family + BaseboardManufacturer + BaseboardProduct
{cd9d0da1-e88d-5d36-aae5-2ba60e8d0ed6}   <- Manufacturer + Family
{a127c2d7-5537-5b72-8bc1-9ccd683f18e6}   <- Manufacturer + EnclosureKind
{96005f57-a38f-5b5e-a26a-50d7286811b0}   <- Manufacturer + BaseboardManufacturer + BaseboardProduct
{56bb94fc-caf1-5863-9e85-1e449a0c5a01}   <- Manufacturer
```

In this case, we set all the fields that are relevant (excluding BIOS version
and vendor) to the same values as the stock firmware.

Be aware that sometimes this means a downgrade - in the case above, it would
make more sense to set the `Manufacturer` field to a sensible value such as
`NovaCustom`, but since this field is used in several GUIDs in fwupd and
Windows Update and the OEM set it to `Notebook`, we'll do this as well.
Exceptions can be made depending on circumstances (e.g. if the field in question
is important for functionality).

In the case where the device does not have an existing supported BIOS or the
client chooses to use different SMBIOS fields (e.g. to make it easier to
differentiate devices), we want to set the fields to the most sensible values:

- `Family`: family of devices (e.g. `Clevo_tgl-u` for Clevo Tiger Lake laptops)
- `Manufacturer`: The name of the party selling the device (OEM)
- `ProductName`: The name under which the device is sold
- `BaseboardManufacturer`: The manufacturer of the device (ODM), e.g. `Clevo`
- `BaseboardProduct`: The name of the mainboard part
- `ProductSku`: Variant of the device, e.g. soldered RAM capacity or discrete
  GPU option. May be read from straps in mainboard code.

For a list of SMBIOS fields used by Windows Update, see
[Microsoft's documentation](https://docs.microsoft.com/en-us/windows-hardware/drivers/dashboard/using-chids).

# BIOS Vendor and Version fields

We use the following convention for filling in the BIOS version fields:

```bash
Dasharo ([major_framework]+[minor_framework]) v[version]
```

`major_framework` refers to the primary framework in which the firmware is
developed, e.g. `coreboot` or `TianoCore`.

`minor_framework` is the secondary framework, a supporting component for the
primary framework, e.g. a coreboot payload.

Examples:

```bash
Dasharo (coreboot+UEFI) v1.0.0    - for coreboot-based TianoCore builds
Dasharo (coreboot+SeaBIOS) v1.0.0 - for coreboot-based SeaBIOS builds
Dasharo (coreboot+Heads) v1.0.0   - for coreboot-based Heads builds
```

For the version number fields, refer to [Versioning](../versioning).
