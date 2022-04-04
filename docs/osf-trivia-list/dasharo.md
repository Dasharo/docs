# Dasharo

## What is Dasharo?

Dasharo is open-source firmware distribution focusing on clean and simple code,
long-term maintenance, transparent validation, privacy-respecting
implementation, liberty for the owners, and trustworthiness for all.

Dasharo aims to be to open-source firmware ecosystem what Debian/Ubuntu is for
Linux. We develop, validate, maintain and release open-source firmware binaries
for various hardware targets.

## What is Dasharo Common Base?

It is set of patches creating foundation for further integration of Dasharo
features. Common base can vary depending on the supported hardware target, but
it may consist of:

* Fixes required to build [Dasharo/edk2](https://github.com/Dasharo/edk2) as
  coreboot payload
* Fixes introducing Dasharo SMBIOS/DMI tables format according to [Dasharo
  Product Guidelines](../../dev-proc/smbios-rules)
* Fixes for submodules building
