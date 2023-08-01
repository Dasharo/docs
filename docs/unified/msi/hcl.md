# Hardware Compatibility Lists

Following compatibility list is compiled thanks to community contribution and
Dasharo Team work. Please note there are other good sources of information
about compatibility like:

- [OpenBenchmarking.org](https://openbenchmarking.org)
- [linux-hardware.org](https://linux-hardware.org)
- [bsd-hardwre.info](https://bsd-hardware.info/)

Feel free to refer to above sources or [contact
community](https://docs.dasharo.com/#community), if you can't find your
hardware.

=== "CPU HCL (20 Jul 2023)"

    CPU Hardware Compatibility List presents the CPUs tested and verified
    to work with Dasharo by community. The following list does not include CPU
    which is tested and verfied in 3mdeb laboratory - this information might be
    found in [MSI PRO Z690-A Hardware Matrix](../../variants/msi_z690/hardware-matrix.md)
    and [MSI PRO Z790-P Hardware Matrix](../../variants/msi_z790/hardware-matrix.md)
    documentation.

    Legend:

    * CPU Model: CPU Model name.
    * Dasharo version: Dasharo version on which report was created.
        - `-` if version was not reported
    * Source:
        - Link to report if it is public.
        - `Dasharo HCL report` if it was [reported using
        DTS](../../../dasharo-tools-suite/documentation/#hcl-report).

    <center>

    === "PRO Z690-A (WIFI) DDR4"
        | CPU Model | Dasharo version |  Source  |
        |:---------:|:----------------------:|:---------:|
        | 12th Gen Intel(R) Core(TM) i5-12400F | - | [Github PR][3] |
        | 12th Gen Intel(R) Core(TM) i5-12400F | v1.1.0 | Dasharo HCL Report |
        | 12th Gen Intel(R) Core(TM) i5-12500T | v1.1.0 | Dasharo HCL Report |
        | 12th Gen Intel(R) Core(TM) i5-12500T | v1.1.0 | Dasharo HCL report |
        | 12th Gen Intel(R) Core(TM) i5-12600 | v1.1.0 | Dasharo HCL Report |
        | 12th Gen Intel(R) Core(TM) i5-12600 | v1.1.0 | Dasharo HCL report |
        | 12th Gen Intel(R) Core(TM) i5-12600K | v1.0.0 | Dasharo HCL Report |
        | 12th Gen Intel(R) Core(TM) i5-12600K | v1.0.0 | Dasharo HCL report |
        | 12th Gen Intel(R) Core(TM) i5-12600K | v1.1.0 | Dasharo HCL Report |
        | 12th Gen Intel(R) Core(TM) i5-12600K | v1.1.0 | Dasharo HCL report |
        | 12th Gen Intel(R) Core(TM) i5-12600K | v1.1.1 | Dasharo HCL Report |
        | 12th Gen Intel(R) Core(TM) i5-12600K | v1.1.1-rc4 | Dasharo HCL Report |
        | 12th Gen Intel(R) Core(TM) i7-12700K | v1.0.0 | Dasharo HCL Report |
        | 12th Gen Intel(R) Core(TM) i7-12700K | v1.0.0 | Dasharo HCL report |
        | 12th Gen Intel(R) Core(TM) i7-12700K | v1.0.0 | [Qubes HCL reports][2] |
        | 12th Gen Intel(R) Core(TM) i7-12700K | v1.1.0 | Dasharo HCL Report |
        | 12th Gen Intel(R) Core(TM) i7-12700K | v1.1.1 | Dasharo HCL Report |
        | 12th Gen Intel(R) Core(TM) i9-12900K | v0.4.0 | [Qubes HCL reports][1] |
        | 12th Gen Intel(R) Core(TM) i9-12900K | v1.1.0 | Dasharo HCL Report |
    		| 12th Gen Intel(R) Core(TM) i9-12900K | v1.1.1 | Dasharo HCL Report |
        | 12th Gen Intel(R) Core(TM) i9-12900KS | v1.1.1 | Dasharo HCL Report |
        | 12th Gen Intel(R) Core(TM) i9-12900T | v1.1.0 | Dasharo HCL Report |

        [1]: https://forum.qubes-os.org/t/msi-pro-z690-a-wifi-ddr4-with-alder-lake-12900k/11490/6
        [2]: https://groups.google.com/g/qubes-users/c/lGOjuApLD_o/m/TBZN0PsXEgAJ

    === "PRO Z690-A (WIFI)"
        | CPU Model | Dasharo version |  Source  |
        |:---------:|:----------------------:|:---------:|
        | | | |

    === "PRO Z790-P (WIFI) DDR4"
        | CPU Model | Dasharo version |  Source  |
        |:---------:|:----------------------:|:---------:|
        | | | |

    === "PRO Z790-P (WIFI)"
        | CPU Model | Dasharo version |  Source  |
        |:---------:|:----------------------:|:---------:|
        | | | |

    </center>

=== "Memory HCL (20 Jul 2023)"

    Memory hardware Compatibility List presents the DIMM modules tested and verified
    to work with Dasharo in 3mdeb laboratory.

    Memory Modules are tested in 1, 2 and 4 modules configurations. These follow
    the DIMM population procedures as stated in the Board Manual: 1 module in
    DIMMA2 Slot (Single Channel), 2 by adding another module in DIMMB2 (Dual
    Channel), and 4 by populating all 4 slots. Testing is defined as passing
    firmware POST and booting an OS, since what is being tested is that the Intel
    FSP (Firmware Support Package) component is initializing the Memory Modules. We
    don't stress test them for stability. Each SPD Profile is tested, so each
    Memory Module can have from 1 to 4 entries. You may also check out
    [Intel memory validation results](https://www.intel.com/content/www/us/en/platform-memory/platform-memory.html)
    page and see the results for DDR4 UDIMM testing. Maximum ratings for Alder Lake
    S CPUs is also available in the [CPU datasheet](https://edc.intel.com/content/www/us/en/design/ipla/software-development-platforms/client/platforms/alder-lake-desktop/12th-generation-intel-core-processors-datasheet-volume-1-of-2/001/processor-sku-support-matrix/).

    Legend:

    * Configuration 1/2/4 - means given memory module was tested in 1, 2 and 4
      DIMMs populated configuration, &#10004; means successfully tested, &#10006;
      means platform did not boot with Dasharo, e.g. &#10004;/&#10004;/&#10004;
      means all configurations work, `-` means not tested
    * Size: DIMM capacity in MB
    * SPD profile: can be one of JEDEC(Standard) / XMP Profile #1 / XMP Profile #2.
      Profile data:
        - Type/speed: for example DDR4-2400 means DDR4 module clocked at max 2400MHz
        for given profile
        - Timings: for example CL17-17-17 means CAS Latency 17, tRCD 17, tRP 17
        (numbers expressed in clock cycles) for given memory profile
        - Voltage: memory voltage in Volts for given memory profile

    > NOTE: some XMP profiles may have lower speeds than other ones, but also have
    > smaller CAS latency. Also the memory frequency configured in the memory
    > controller and reported by DMI/SMBIOS may be slightly lower than advertised
    > in the module specifications. This can vary based on the board design, CPU
    > and many other factors.

    <center>

    === "PRO Z690-A (WIFI) DDR4"
        | Manufacturer | Part Number | Size | Speed | Configuration 1/2/4 | Dasharo version | Source |
        |:------------:|:-----------:|:----:|:-----:|:-------------------:|:---------------:|:------:|
        | Corsair | CMK16GX4M2B3200C16 | 16384 MB | 2133 MT/s (PC4-17000) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
        | Corsair | CMK16GX4M2B3200C16 | 16384 MB | 2133 MT/s (PC4-17000) | -/-/&#10004 | v1.1.0 | Dasharo HCL report |
        | Corsair | CMK16GX4M2B3200C16 | 32768 MB | 2133 MT/s (PC4-17000) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
        | Crucial Technology | BL16G32C16U4B.16FE | 16384 MB | 2666 MT/s (PC4-21300) | &#10004/-/- | v1.1.0 | Dasharo HCL report |
        | Crucial Technology | BL16G32C16U4B.16FE | 16384 MB | 2666 MT/s (PC4-21300) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
        | Crucial Technology | CT8G4DFS8266.C8FJ | 8192 MB | 2666 MT/s (PC4-21300) | &#10004/-/- | v1.1.0 | Dasharo HCL report |
        | Kingston | KF3200C16D4/16GX | 16384 MB | 2400 MT/s (PC4-19200) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
        | Kingston | KF3200C16D4/16GX | 16384 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.1 | Dasharo HCL report |
        | Kingston | KF3200C16D4/32GX | 32768 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.0 | Dasharo HCL report |
        | Kingston | KF3200C16D4/32GX | 32768 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.1 | Dasharo HCL report |
        | Kingston | KF3600C17D4/8GX | 8192 MB | 2400 MT/s (PC4-19200) | &#10004/-/- | v1.0.0 | Dasharo HCL report |
        | Kingston | KF3600C17D4/8GX | 8192 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.0.0 | Dasharo HCL report |
        | Kingston | KF3600C17D4/8GX | 8192 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.0 | Dasharo HCL report |
        | Kingston | KF3600C17D4/8GX | 8192 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.1 | Dasharo HCL report |
        | Kingston | KF3600C17D4/8GX | 8192 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.1-rc4 | Dasharo HCL report |
        | Patriot Memory | 4400 C19 Series | 8192 MB | 2133 MT/s (PC4-17000) | &#10004/-/- | v1.0.0 | Dasharo HCL report |
        | Thermaltake Technology Co Ltd | RG26D408GX2-3600C18A | 8192 MB | 2666 MT/s (PC4-21300) | &#10004/-/- | v1.1.0 | Dasharo HCL report |

    === "PRO Z690-A (WIFI)"

        | DIMM vendor | Part Number | Size | SPD profile | Configuration 1/2/4 |
        |:-----------:|:-----------:|:----:|:-----------:|:-------------------:|
        | Kingston    | KF556C40BB/8 |8GB | 5600MT/s 40-40-40 1.25V | &#10004;/&#10004;/&#10004; |
        | Crucial     | CT8G48C40U5.M4A1/8 |8GB | 4800MT/s 40-39-39 1.1V | &#10004;/&#10004;/&#10004; |
        | ADATA       | AD5U48008G-S |8GB | 4800MT/s 40-40-40 1.1V | &#10004;/&#10004;/&#10004; |

    === "PRO Z790-P (WIFI) DDR4"
        | DIMM vendor | Part Number | Size | SPD profile | Configuration 1/2/4 |
        |:-----------:|:-----------:|:----:|:-----------:|:-------------------:|
        | | | | | |

    === "PRO Z790-P (WIFI)"
        | DIMM vendor | Part Number | Size | SPD profile | Configuration 1/2/4 |
        |:-----------:|:-----------:|:----:|:-----------:|:-------------------:|
        | | | | | |

    </center>

=== "GPU HCL"

    __NOTE__: Since we cannot extend following list based on automatic Dasharo
    HCL reports parsing until [this
    issue](https://github.com/Dasharo/dasharo-issues/issues/462) would be
    addressed we decided to not update GPU HCL ourselves. We will merge PRs to
    GPU HCL, if following criteria would be addressed:

    * Card has to be installed on main metal 16x slot, and there shouldn't be
      any other GPU except Intel integrated one if non-F CPU.
    * Confirmation than Dasharo splash screen and Firmware menus were working.
    * Actual GPU chip (PCI Vendor ID / Device ID).
    * Video Card model (Subsystem Vendor ID / Device ID).
    * Option ROM version.
    * Secure Boot status (Enabled/Disabled, in case than there are Option ROM
      signing issues. This also means than the VBIOS should NOT be modded, factory
      original versions only)

    GPU Hardware Compatibility List presents the GPUs tested and verified
    to work with Dasharo by community. The following list does not include GPU
    which is tested and verfied in 3mdeb laboratory - this information might be
    found in [MSI PRO Z690-A Hardware Matrix](../../variants/msi_z690/hardware-matrix.md)
    and [MSI PRO Z790-P Hardware Matrix](../../variants/msi_z790/hardware-matrix.md)
    documentation.

    Legend:

    * GPU name: the full name of GPU including vendor and model name.
    * Memory size: total amount of GPU memory declared by vendor.
    * Memory type: GPU's type of memory.
    * Bandwidth: GPU's memory bandwidth.
    * PCI-E Architecture: declared by producer generation of PCI-E architecture.
    * Multi-Graphics Technology: information about support for Multi-Graphics
        Technology.

    Information about GPU might be read from GPU package or documentation.

    | GPU name         | Memory size | Memory type  | Bandwidth | PCI-E Gen | Multi-Graphics Technology | Results                |
    |:----------------:|:-----------:|:------------:|:---------:|:---------:|:-------------------------:|:----------------------:|
    | Nvidia GeForce GTX 1060   | 3072 MB  | GDDR5  | 192GB/s   | Gen3      | 1                         | [Qubes HCL reports][1] |
    | MSI Radeon RX 6950 XT     | 16 GB    | GDDR6  | 576GB/s   | Gen4      | 1                         | |
    | EVGA NVidia RTX 2080      | 8 GB     | GDDR6  | 448GB/s   | Gen3      | 1                         | |
    | PNY NVidia RTX A5000      | 24 GB    | GDDR6  | 768GB/s   | Gen4      | 1                         | |
    | Nvidia GeForce GTX 1080TI | 11264 MB | GDDR5X | x16       | Gen3      | 1                         | [Qubes HCL reports][2] |
    | MSI Radeon RX 6500 XT MECH 2X 4G OC | 4 GB     | GDDR6  | 180GB/s   | Gen4      | 1                         | Works only on Dasharo v1.1.0 or newer |
    | MSI GeForce RTX 3060 GAMING Z TRIO LHR | 12 GB     | GDDR6  | 358GB/s   | Gen4      | 1                         | |

For details how to maintain this documentation please consult [Dasharo HCL
Maintainer documentation](../../../dev-proc/hcl-maintainer).

[1]: https://forum.qubes-os.org/t/msi-pro-z690-a-wifi-ddr4-with-alder-lake-12900k/11490/6
[2]: https://groups.google.com/g/qubes-users/c/lGOjuApLD_o/m/TBZN0PsXEgAJ
[3]: https://github.com/Dasharo/docs/pull/329

## Contributing

=== "PRO Z690-A (WIFI) DDR4"
    - Use [Dasharo Tools Suite HCL report](../../../dasharo-tools-suite/documentation/#hcl-report)
      to upload report automatically.
    - Create new issue in [Dasharo issues repository](https://github.com/Dasharo/dasharo-issues/issues/new?assignees=&labels=P%3A+default%2C+T%3A+hcl&template=hcl-report.md&title=CPU+HCL+report+for+msi_z690).
    - Create PR directly to [Dasharo documentation repository](https://github.com/Dasharo/docs).

    - [CPU HCL email](mailto:contact@dasharo.com?subject=CPU HCL report for msi_z690)
      your `/proc/cpuinfo` or relevant information using following template:

      ```text
      CPU model:
      Dasharo version:
      ```

    - [Memory HCL email](mailto:contact@dasharo.com?subject=Memory HCL report for msi_z690)
      as attachments outputs of following command:

      ```bash
      decode-dimms > decode-dimms.log 2> decode-dimms.err.log
      ```

      In email please include Dasharo version.

      ```text
      Dasharo version:
      ```

=== "PRO Z690-A (WIFI)"
    - Use [Dasharo Tools Suite HCL report](../../../dasharo-tools-suite/documentation/#hcl-report)
      to upload report automatically.
    - Create new issue in [Dasharo issues repository](https://github.com/Dasharo/dasharo-issues/issues/new?assignees=&labels=P%3A+default%2C+T%3A+hcl&template=hcl-report.md&title=CPU+HCL+report+for+msi_z690).
    - Create PR directly to [Dasharo documentation repository](https://github.com/Dasharo/docs).

    - [CPU HCL email](mailto:contact@dasharo.com?subject=CPU HCL report for msi_z690)
      your `/proc/cpuinfo` or relevant information using following template:

      ```text
      CPU model:
      Dasharo version:
      ```

    - [Memory HCL email](mailto:contact@dasharo.com?subject=Memory HCL report for msi_z690)
      as attachments outputs of following command:

      ```bash
      decode-dimms > decode-dimms.log 2> decode-dimms.err.log
      ```

      In email please include Dasharo version.

      ```text
      Dasharo version:
      ```

=== "PRO Z790-P (WIFI) DDR4"
    - Use [Dasharo Tools Suite HCL report](../../../dasharo-tools-suite/documentation/#hcl-report)
      to upload report automatically.
    - Create new issue in [Dasharo issues repository](https://github.com/Dasharo/dasharo-issues/issues/new?assignees=&labels=P%3A+default%2C+T%3A+hcl&template=hcl-report.md&title=CPU+HCL+report+for+msi_z790).
    - Create PR directly to [Dasharo documentation repository](https://github.com/Dasharo/docs).

    - [CPU HCL email](mailto:contact@dasharo.com?subject=CPU HCL report for msi_z790)
      your `/proc/cpuinfo` or relevant information using following template:

      ```text
      CPU model:
      Dasharo version:
      ```

    - [Memory HCL email](mailto:contact@dasharo.com?subject=Memory HCL report for msi_z790)
      as attachments outputs of following command:

      ```bash
      decode-dimms > decode-dimms.log 2> decode-dimms.err.log
      ```

      In email please include Dasharo version.

      ```text
      Dasharo version:
      ```

=== "PRO Z790-P (WIFI)"
    - Use [Dasharo Tools Suite HCL report](../../../dasharo-tools-suite/documentation/#hcl-report)
      to upload report automatically.
    - Create new issue in [Dasharo issues repository](https://github.com/Dasharo/dasharo-issues/issues/new?assignees=&labels=P%3A+default%2C+T%3A+hcl&template=hcl-report.md&title=CPU+HCL+report+for+msi_z790).
    - Create PR directly to [Dasharo documentation repository](https://github.com/Dasharo/docs).

    - [CPU HCL email](mailto:contact@dasharo.com?subject=CPU HCL report for msi_z790)
      your `/proc/cpuinfo` or relevant information using following template:

      ```text
      CPU model:
      Dasharo version:
      ```

    - [Memory HCL email](mailto:contact@dasharo.com?subject=Memory HCL report for msi_z790)
      as attachments outputs of following command:

      ```bash
      decode-dimms > decode-dimms.log 2> decode-dimms.err.log
      ```

      In email please include Dasharo version.

      ```text
      Dasharo version:
      ```

If you already have reported your results and you change some hardware
configuration we would appreciate an update.
