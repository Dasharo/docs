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

## HCL lists

=== "CPU HCL"

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

=== "Memory HCL"

    Memory hardware Compatibility List present the DIMM modules tested and verified
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
    * Size: DIMM capacity in GB
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
    
    ### HCL list - MSI PRO Z690-A DDR4

    | Manufacturer | Part Number | Size | Type | Speed | Configuration 1/2/4 | Dasharo version | Source |
    |:------------:|:-----------:|:----:|:----:|:-----:|:-------------------:|:---------------:|:------:|
    | Crucial Technology | CT8G4DFS8266.C8FJ | 8192 MB | DDR4 SDRAM | 2666 MT/s (PC4-21300) | &#10004/-/- | v1.1.0 | Dasharo HCL report |
    | Kingston | KF3600C17D4/8GX      | 8192 MB | DDR4 SDRAM | 2400 MT/s (PC4-19200) | &#10004/-/&#10004 | v1.0.0 | Dasharo HCL report |
    | Kingston | KF3600C17D4/8GX      | 8192 MB | DDR4 SDRAM | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.0 | Dasharo HCL report |
    | Patriot Memory | 4400 C19 Series | 8192 MB | DDR4 SDRAM | 2133 MT/s (PC4-17000) | &#10004/-/- | v1.0.0 | Dasharo HCL report |
    | Thermaltake Technology Co Ltd | RG26D408GX2-3600C18A | 8192 MB | DDR4 SDRAM | 2666 MT/s (PC4-21300) | &#10004/-/- | v1.1.0 | Dasharo HCL report |
    
    1) Tested in 2x2 mixed configuration

### HCL list - MSI PRO Z690-A DDR5

| DIMM vendor | Part Number | Size | SPD profile | Configuration 1/2/4 |
|:-----------:|:-----------:|:----:|:-----------:|:-------------------:|
| Kingston    | [KF556C40BB/8][6] |8GB | 5600MT/s 40-40-40 1.25V | &#10004;/&#10004;/&#10004; |
| Crucial     | [CT8G48C40U5.M4A1/8][7] |8GB | 4800MT/s 40-39-39 1.1V | &#10004;/&#10004;/&#10004; |
| ADATA       | [AD5U48008G-S][9] |8GB | 4800MT/s 40-40-40 1.1V | &#10004;/&#10004;/&#10004; |

[1]: https://www.kingston.com/dataSheets/KF436C17BBK4_32.pdf
[2]: https://www.corsair.com/eu/en/Categories/Products/Memory/VENGEANCE-LPX/p/CMK16GX4M2B3200C16
[3]: https://www.kingston.com/dataSheets/KF432C16BB1_16.pdf
[4]: https://www.pny.com/anarchy-x-ddr4-red?sku=MD16GK2D4320016AXR
[5]: https://www.kingston.com/datasheets/KF436C18BBK2_64.pdf
[6]: https://www.kingston.com/memory/gaming/kingston-fury-beast-ddr5-memory
[7]: https://www.crucial.com/memory/ddr5/ct2k16g48c40u5
[8]: https://www.kingston.com/datasheets/HX426C16FRK4_64.pdf
[9]: https://www.adata.com/us/consumer/dram-module-ddr5-4800-u-dimm
[10]: https://www.amazon.com/OLOy-Memory-288-Pin-Desktop-MD4U323216DJDA/dp/B0836NZHWR

=== "GPU HCL"

    GPU Hardware Compatibility List presents the GPUs tested and verified
    to work with Dasharo by community. The following list does not include GPU
    which is tested and verfied in 3mdeb laboratory - this information might be
    found in [Hardware Matrix](hardware-matrix.md) documentation.
    
    Legend:
    
    * GPU name: the full name of GPU including vendor and model name.
    * Memory size: total amount of GPU memory declared by vendor.
    * Memory type: GPU's type of memory.
    * Bandwidth: GPU's bandwidth.
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
    | MSI Radeon RX 6500 XT MECH 2X 4G OC | 4 GB     | GDDR6  | x4 (x16 connector) | Gen4      | 1                         | Works only on Dasharo v1.1.0 or newer |
    | MSI GeForce RTX 3060 GAMING Z TRIO LHR | 12 GB     | GDDR6  | x16   | Gen4      | 1                         | |

For details how to maintain this documentation please consult [Dasharo HCL
Maintainer documentation](../../../dev-proc/hcl-maintainer).

[1]: https://forum.qubes-os.org/t/msi-pro-z690-a-wifi-ddr4-with-alder-lake-12900k/11490/6
[2]: https://groups.google.com/g/qubes-users/c/lGOjuApLD_o/m/TBZN0PsXEgAJ
[3]: https://github.com/Dasharo/docs/pull/329
