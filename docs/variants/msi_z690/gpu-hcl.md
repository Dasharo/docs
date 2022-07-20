# GPU HCL

## Contributing

Feel free to test different graphics cards and report your results via
[email](mailto:contact@dasharo.com) or submit a Pull Request to
[Dasharo documentation repository](https://github.com/Dasharo/docs) or by using
[Dasharo issues repository](https://github.com/Dasharo/dasharo-issues/issues).

If you already have reported your results and you change some hardware
configuration we would appreciate an additional HCL report.

## HCL list

GPU Hardware Compatibility List presents the GPUs tested and verified
to work with Dasharo by community. The following list does not include GPU
which is tested and verfied in 3mdeb laboratory - this information might be
found in [Hardware Matrix](hardware-matrix.md) documentation.

Legend:
* GPU name - the full name of GPU including vendor and model name.
* Memory size - total amount of GPU memory declared by vendor.
* Memory type - GPU's type of memory.
* Bandwith - GPU's bandwith.
* PCI-E Architecture - declared by producer generation of PCI-E architecture.
* Multi-Graphics Technology - information about support for Multi-Graphics
  Technology.

Information about GPU might be read from GPU package or documentation.

| GPU name         | Memory size | Memory type | Bandwidth | PCI-E Architecture | Multi-Graphics Technology | Results                |
|:----------------:|:-----------:|:-----------:|:---------:|:------------------:|:-------------------------:|:----------------------:|
| Nvidia GeForce GTX 1060 | 3072 MB | GDDR5 | x16       | Gen3               | 1                            | [Qubes HCL reports][1] |

[1]: https://forum.qubes-os.org/t/msi-pro-z690-a-wifi-ddr4-with-alder-lake-12900k/11490/6
