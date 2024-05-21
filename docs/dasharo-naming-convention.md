# Dasharo Product Naming Convention

Following documentation is results of [RFC](https://github.com/Dasharo/dasharo-issues/issues/762).

## Synopsis

```plain
Dasharo (firmware_framework[+payload]) Entry Package [customer_type] for
market_segment
```

## Description

Dasharo's naming scheme is crafted to convey the essential details of each
firmware package. It includes the base firmware framework, an optional payload,
the targeted market segment, and the customer type. This structure assists in
identifying the most suitable package for specific technological needs, market
segments, and customer categories.

Components of the naming scheme:

```plain
Dasharo (firmware_framework[+payload]) Entry Package [customer_type] for
market_segment
```

- `firmware_framework`: Mandatory. Specifies the base firmware framework used
  in the package. Options include:
  ```plain
  coreboot | UEFI
  ```
  `UEFI` signifies EDK II reference implementation of the UEFI Specification.

- `payload` (optional): Details the additional software loaded by the firmware.
  Options are:
  ```plain
  none | UEFI | SeaBIOS | Heads
  ```
  The omission of this component implies no additional payload.

- `market_segment`: Indicates the target market segment for the package.
  Possible segments:
  ```plain
  Network Appliance/Embedded | Laptop | Desktop | Workstation | Server
  ```

- `customer_type`: Specifies whether the package is aimed at professional
  retail customers or enterprise business customers. Options are:
  ```plain
  Pro | Enterprise
  ```

This naming convention aims to provide clarity and precision, facilitating ease
of understanding across Dasharo's firmware offerings.

## Examples

```plain
Dasharo (coreboot+Heads) Entry Package Pro for Laptop
```

A package aimed at professional retail customers with laptops, incorporating
coreboot with the Heads payload.

```plain
Dasharo (UEFI) Entry Package Enterprise for Desktop
```

A package for enterprise business customers for desktops, employing UEFI with
no additional payload specified.
