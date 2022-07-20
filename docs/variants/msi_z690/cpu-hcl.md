# CPU HCL

## Contributing

Feel free to test different processors and report your results via
[email](mailto:contact@dasharo.com) or submit a Pull Request to
[Dasharo documentation repository](https://github.com/Dasharo/docs) or by using
[Dasharo issues repository](https://github.com/Dasharo/dasharo-issues/issues).

If you already have reported your results and you change some hardware
configuration we would appreciate an additional HCL report.

## HCL list

CPU Hardware Compatibility List presents the CPUs tested and verified
to work with Dasharo by community. The following list does not include CPU
which is tested and verfied in 3mdeb laboratory - this information might be
found in [Hardware Matrix](hardware-matrix.md) documentation.

Legend:
* Processor name - the full name of processor including vendor, brand and
    CPU number.
* Core name - CPU core codename.
* CPU base speed - based CPU speed.
* CPU boost speed - boosted CPU speed.
* Wattage - declared by producer processor wattage.
* GPU - information about embedded graphics processing unit.
* Results - link to measurement results.

Information about processor name, core name and speed might be read from OS
(Linux systems - command `lscpu`, Windows systems - `System information` menu).
Rest of the information might be read from CPU package or documentation.

| Processor name       | Core name   | CPU base speed | CPU boost speed | Wattage | GPU             | Results                |
|:--------------------:|:-----------:|:--------------:|:---------------:|:-------:|:---------------:|:----------------------:|
| Intel Core i9-12900K | Alder Lake  | 3.2 GHz        | 5.3 GHz         | 125     | UHDGraphics710  | [Qubes HCL reports][1] |
| Intel Core i7-12700K | Alder Lake  | 3.6 GHz        | 5.0 GHz         | 125     | UHDGraphics770  | [Qubes HCL reports][2] |

[1]: <https://forum.qubes-os.org/t/msi-pro-z690-a-wifi-ddr4-with-alder-lake-12900k/11490/6>
[2]: <https://www.qubes-os.org/hcl/#msi_ms-7d25_i7-12700k_alder-lake_integrated-graphics-uhd-770-geforce-gtx-1080-ti>
