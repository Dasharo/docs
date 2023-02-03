# CPU HCL

## Contributing

* Use [Dasharo Tools Suite HCL
  report](../../../dasharo-tools-suite/documentation/#hcl-report) to upload
  report automatically.
* Create new issue in [Dasharo issues
  repository](https://github.com/Dasharo/dasharo-issues/issues).
* Create PR directly to [Dasharo documentation
  repository](https://github.com/Dasharo/docs).
* [email](mailto:contact@dasharo.com?subject=CPU HCL report) you
  `/proc/cpuinfo` or relevant information using following template:

  ```text
  CPU model: 
  Dasharo version: 
  ```

If you already have reported your results and you change some hardware
configuration we would appreciate an update.

## HCL list

CPU Hardware Compatibility List presents the CPUs tested and verified
to work with Dasharo by community. The following list does not include CPU
which is tested and verfied in 3mdeb laboratory - this information might be
found in [Hardware Matrix](hardware-matrix.md) documentation.

Legend:

* CPU Model: Intel CPU Model name.
* Dasharo version: Dasharo version on which report was created.
  - `-` if version was not reported
* Source:
  - Link to report if it is public.
  - `Dasharo HCL report` if it was reported using DTS.

<center>

| CPU Model | Dasharo version |  Source  |
|:---------:|:----------------------:|:---------:|
| 12th Gen Intel(R) Core(TM) i5-12400F | - | [Github PR][3] |
| 12th Gen Intel(R) Core(TM) i5-12500T | v1.1.0 | Dasharo HCL report |
| 12th Gen Intel(R) Core(TM) i5-12600 | v1.1.0 | Dasharo HCL report |
| 12th Gen Intel(R) Core(TM) i5-12600K | v1.0.0 | Dasharo HCL report |
| 12th Gen Intel(R) Core(TM) i5-12600K | v1.1.0 | Dasharo HCL report |
| 12th Gen Intel(R) Core(TM) i7-12700K | v1.0.0 | Dasharo HCL report |
| 12th Gen Intel(R) Core(TM) i7-12700K | v1.0.0 | [Qubes HCL reports][2] |
| 12th Gen Intel(R) Core(TM) i9-12900K | v0.4.0 | [Qubes HCL reports][1] |

</center>

For details how to maintain this documentation please consult [Dasharo HCL
Maintainer documentation](../../../dev-proc/hcl-maintainer).

[1]: https://forum.qubes-os.org/t/msi-pro-z690-a-wifi-ddr4-with-alder-lake-12900k/11490/6
[2]: https://groups.google.com/g/qubes-users/c/lGOjuApLD_o/m/TBZN0PsXEgAJ
[3]: https://github.com/Dasharo/docs/pull/329
