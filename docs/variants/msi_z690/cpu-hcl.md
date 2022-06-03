# CPU HCL

## Contributing

Feel free to test different processors and report your results via
[email](mailto:contact@dasharo.com) or submit a Pull Request to
[Dasharo documentation repository](https://github.com/Dasharo/docs) or by using
[Dasharo issues repository](https://github.com/Dasharo/dasharo-issues/issues).

## HCL list

CPU Hardware Compatibility List presents the CPUs tested and verified
to work with Dasharo by community. The following list does not include CPU
which is tested and verfied in 3mdeb laboratory - this information might be
found in [Hardware Matrix](../hardware-matrix.md) documentation.

Legend:
* Processor name - the full name of processor including vendor, brand and
    CPU number.
* Core name - CPU core codename.
* CPU base speed - based CPU speed.
* CPU boost spped - boosted CPU speed.
* Wattage - declared by producer processor wattage.
* GPU - information about embedded graphics processing unit.
* Results - link to measurement results.

Information about processor name, core name and speed might be read from OS
(Linux systems - command `lscpu`, Windows systems - `System information` menu).
Rest of the information might be read from CPU package or documentation.

| Processor name       | Core name   | CPU base speed | CPU boost speed | Wattage | GPU             | Results       |
|:--------------------:|:-----------:|:--------------:|:---------------:|:-------:|:---------------:|:-------------:|
| Intel Core i9-12900K | Alder Lake  | 3.2 GHz        | 5.3 GHz         | 125     | UHDGraphics710  | [link][1]     |

[1]: https://cloud.3mdeb.com/index.php/s/JRYxxxAe7fcCczx
