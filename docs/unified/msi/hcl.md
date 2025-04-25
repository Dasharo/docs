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

=== "CPU HCL (18 Mar 2025)"

    CPU Hardware Compatibility List presents the CPUs tested and verified
    to work with Dasharo by community. The following list does not include CPU
    which is tested and verified in 3mdeb laboratory - this information might be
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
        DTS](../../dasharo-tools-suite/documentation/features.md#hcl-report).

    <center>

    === "PRO Z690-A (WIFI) (DDR4)"
        {%
            include-markdown "../../resources/hcl/cpu/pro-z690-a-wifi-ddr4.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "PRO Z790-P (WIFI) (DDR4)"
        {%
            include-markdown "../../resources/hcl/cpu/pro-z790-p-wifi-ddr4.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    </center>

=== "Memory HCL (12 Sep 2023)"

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
        {%
            include-markdown "../../resources/hcl/memory/pro-z690-a-wifi-ddr4.md"
            start="<!--start-->"
            end="<!--end-->"
        %}


    === "PRO Z690-A (WIFI)"
        {%
            include-markdown "../../resources/hcl/memory/pro-z690-a-wifi.md"
            start="<!--start-->"
            end="<!--end-->"
        %}


    === "PRO Z790-P (WIFI) DDR4"
        {%
            include-markdown "../../resources/hcl/memory/pro-z790-p-wifi-ddr4.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "PRO Z790-P (WIFI)"
        {%
            include-markdown "../../resources/hcl/memory/pro-z790-p-wifi.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    </center>

=== "GPU HCL (manual)"

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
    which is tested and verified in 3mdeb laboratory - this information might be
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

    {%
        include-markdown "../../resources/hcl/gpu/manual.md"
        start="<!--start-->"
        end="<!--end-->"
    %}

=== "GPU HCL (Z690-A automatic)"

    Hardware Compatibility List generated based on `lspci` output from Dasharo HCL Reports:

    Legend:

    * Vendor Name: vendor name as reported by `lspci`.
    * GPU Code Name: GPU code name or equivalent.
    * Model: GPU model.
    * PCI VendorID:ModelID: PCI Vendor ID and Model ID reported by `lspci`.
    * Multi-Graphics Config: If card was detected in multi-GPU configuration.
    Please note it doesn't mean heterogeous or homogeneous configuration, it just
    mean there were many VGA controllers detected in given report.

    {%
        include-markdown "../../resources/hcl/gpu/z690-a-automatic.md"
        start="<!--start-->"
        end="<!--end-->"
    %}

For details how to maintain this documentation please consult [Dasharo HCL
Maintainer documentation](../../dev-proc/hcl-maintainer.md).

[1]: https://forum.qubes-os.org/t/msi-pro-z690-a-wifi-ddr4-with-alder-lake-12900k/11490/6
[2]: https://groups.google.com/g/qubes-users/c/lGOjuApLD_o/m/TBZN0PsXEgAJ
[3]: https://github.com/Dasharo/../../pull/329
[4]: https://github.com/Dasharo/../../pull/693

## Contributing

=== "PRO Z690-A (WIFI) DDR4"
    - Use [Dasharo Tools Suite HCL report](../../dasharo-tools-suite/documentation/features.md#hcl-report)
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
    - Use [Dasharo Tools Suite HCL report](../../dasharo-tools-suite/documentation/features.md#hcl-report)
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
    - Use [Dasharo Tools Suite HCL report](../../dasharo-tools-suite/documentation/features.md#hcl-report)
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
    - Use [Dasharo Tools Suite HCL report](../../dasharo-tools-suite/documentation/features.md#hcl-report)
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
