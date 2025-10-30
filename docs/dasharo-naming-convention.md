# Dasharo Product Naming Convention

Following documentation is v2 of naming convention following results of
[RFC](https://github.com/Dasharo/dasharo-issues/issues/762).

## Synopsis

```plain
Dasharo (framework[+payload]) [edition] [release] Package for [platform]
```

## Description

Dasharo's naming scheme is crafted to convey the essential details of each
firmware package. It includes the base firmware framework, an optional payload,
the target `platform`, and the `edition`. This structure helps identify the
most suitable package for `platform`-specific needs and customer categories.

Components of the naming scheme:

- `framework`: Mandatory. Specifies the base firmware framework used in the
package. Available options:

    + `coreboot` - Dasharo downstream of coreboot open source project.
    + `UEFI` - Dasharo downstream of Tianocore EDK II reference implementation of
  the UEFI Specification.
    + `Slim Bootloader` - upstream or downstream version of Slim Bootloader.

- `payload` (optional): Details the additional software loaded by the firmware.
Available options:

    + `UEFI` - Dasharo downstream of EDK II.
    + `SeaBIOS` - upstream or downstream version of SeaBIOS.
    + `Heads` - upstream or downstream version of Heads.
    + `U-Boot` - upstream or downstream version of U-Boot.

  The omission of this component implies no additional payload.

- `platform`: Indicates the target platform for the package. Platform is
mandatory in public names. Platform name should follow [supported hardware
list](/variants/overview).
- `edition`: Community | Pro | Enterprise (edition codes: DCP, DPP, DEP)

- `release`: Rapid | Assured | LTS. Defines QA scope and support cadence. Codes
are for internal use in filenames; public names spell out the release tier.
    + `Rapid` - minimal regression only, scope depends on target hardware and
  configuration, so that it can be 3 or 10 tests, it is very likely <=10% of
  LTS,
    + `Assured` in between Rapid and LTS, adding to `Rapid` only tests which
  validate areas of firmware that experience change,s e.g., USB
  improvements/fixes leads to test USB, measured boot changes then only TPM and
  measured boot,
    + `LTS` - full scope, typically once a year unless budget is available.

This naming convention aims to provide clarity and precision, facilitating ease
of understanding across Dasharo's firmware offerings.

## Examples

```plain
Dasharo (coreboot+Heads) Pro Rapid Package for Novacustom NV4x 12th Gen
```

A package aimed at professional retail customers with laptops, incorporating
coreboot with the Heads payload.

```plain
Dasharo (Slim Bootloader+UEFI) Pro Assured Package for Hardkernel ODROID-H4
```

A package that uses Slim Bootloader with UEFI payload on Hardkernel ODROID-H4.

```plain
Dasharo (UEFI) Enterprise LTS Package for MSI PRO Z690-A
```

A package for enterprise business customers for MSI PRO Z690-A, employing UEFI
as framework with no additional payload.
