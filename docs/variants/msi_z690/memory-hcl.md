---
hide:
  - toc
---

# Memory HCL

## Contributing

Feel free to test different modules and report us your results via en
[email](mailto:contact@dasharo.com) or submit a Pull Request to
[Dasharo documentation repository](https://github.com/Dasharo/docs).

Be sure to include information about the memory:

1. If using Linux use `sudo dmidecode -t memory`.
2. If using Windows attach screenshots from CPU-Z for example.

> Currently memory profile is not selectable via BIOS setup. This feature is
> planned for future releases.

## HCL list

Memory hardware Compatibility List present the DIMM modules tested and verified
to work with Dasharo in 3mdeb laboratory.

Legend:

* Configuration 1/2/4 - means given memory module was tested in 1, 2 and 4
  DIMMs populated configuration, &#10004; means successfully tested, &#10006;
  means platform did not boot with Dasharo, e.g. &#10004;/&#10004;/&#10004;
  means all configurations work
* Type: `DDR4` or `DDR5`
* Size: DIMM capacity in GB
* Speed: `normal/XMP1/XMP2` - memory clock speed in MHz for standard and XMP
  memory profiles, `-` means not tested, &#10006; means platform did not boot
  with given profile
* Voltage: `normal/XMP1/XMP2` - memory voltage in Volts for standard and XMP
  memory profiles, `-` means not tested, &#10006; means platform did not boot
  with given profile

> NOTE: some XMP profiles may have lower speeds than other ones, but also have
> smaller CAS latency.

| DIMM vendor | Part Number | Configuration 1/2/4 | Type | Size | Speed | Voltage |
|:-----------:|:-----------:|:-------------------:|:----:|:----:|:-----:|:-------:|
| Kingston | KF3600C17D4/8GX | &#10004;/&#10004;/&#10004; | DDR4 | 8GB | 2400MHz/3467MHz/2933MHz | 1.2V/1.35V/1.35V |
