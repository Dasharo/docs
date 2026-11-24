# Hardware Compatibility List

The following lists present hardware reported to work with Dasharo firmware.
They are generated automatically from public hardware databases and from
Dasharo HCL reports sent by the community using
[Dasharo Tools Suite](../../dasharo-tools-suite/documentation/features.md#hcl-report).
Only reports from machines running Dasharo are taken into account.

Feel free to [contact the community](https://docs.dasharo.com/#community), if
you can't find your hardware. For details on how these lists are maintained
please consult
[Dasharo HCL Maintainer documentation](../../dev-proc/hcl-maintainer.md).

<!-- dts-hw-conf-gen: begin of generated HCL tables, see data/hcl-tables.tsv -->
=== "CPU HCL (24 Nov 2026)"

    CPU Hardware Compatibility List presents the CPUs reported to work with
    Dasharo.

    Legend:

    * CPU Model: CPU model name.
    * Dasharo version: Dasharo version on which the report was created.
        - `-` if version was not reported
        - the firmware flavor is given in parentheses, unless it is
          coreboot+UEFI, e.g. `v0.9.0 (coreboot+heads)`
    * Source:
        - `Dasharo HCL Report` if it was reported using
          [DTS](../../dasharo-tools-suite/documentation/features.md#hcl-report).
        - Link to the report if it comes from a public hardware database.

    === "FW6"
        {%
            include-markdown "../../resources/hcl/cpu/protectli-fw6.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "V1000 series"
        {%
            include-markdown "../../resources/hcl/cpu/protectli-v1000-series.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "VP2410"
        {%
            include-markdown "../../resources/hcl/cpu/protectli-vp2410.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "VP2420"
        {%
            include-markdown "../../resources/hcl/cpu/protectli-vp2420.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "VP2430"
        {%
            include-markdown "../../resources/hcl/cpu/protectli-vp2430.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "VP2440"
        {%
            include-markdown "../../resources/hcl/cpu/protectli-vp2440.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "VP32XX"
        {%
            include-markdown "../../resources/hcl/cpu/protectli-vp32xx.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "VP46XX"
        {%
            include-markdown "../../resources/hcl/cpu/protectli-vp46xx.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "VP66XX"
        {%
            include-markdown "../../resources/hcl/cpu/protectli-vp66xx.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

=== "Memory HCL (24 Nov 2026)"

    Memory Hardware Compatibility List presents the memory modules reported to
    work with Dasharo.

    Legend:

    * Manufacturer, Part Number, Size, Speed: as read from the module SPD
      (`decode-dimms`) or, when unavailable, from the SMBIOS tables.
    * Configuration 1/2/4: &#10004; marks whether the report was created with
      1, 2 or 4 modules installed.
    * Dasharo version: Dasharo version on which the report was created.
        - `-` if version was not reported
        - the firmware flavor is given in parentheses, unless it is
          coreboot+UEFI, e.g. `v0.9.0 (coreboot+heads)`
    * Source:
        - `Dasharo HCL Report` if it was reported using
          [DTS](../../dasharo-tools-suite/documentation/features.md#hcl-report).
        - Link to the report if it comes from a public hardware database.

    === "FW6"
        {%
            include-markdown "../../resources/hcl/memory/protectli-fw6.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "VP2410"
        No reports yet. Help us extend this list by sending a Dasharo HCL report
        from your machine using
        [Dasharo Tools Suite](../../dasharo-tools-suite/documentation/features.md#hcl-report).

    === "VP2420"
        {%
            include-markdown "../../resources/hcl/memory/protectli-vp2420.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "VP2430"
        No reports yet. Help us extend this list by sending a Dasharo HCL report
        from your machine using
        [Dasharo Tools Suite](../../dasharo-tools-suite/documentation/features.md#hcl-report).

    === "VP2440"
        {%
            include-markdown "../../resources/hcl/memory/protectli-vp2440.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "VP32XX"
        {%
            include-markdown "../../resources/hcl/memory/protectli-vp32xx.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "VP46XX"
        {%
            include-markdown "../../resources/hcl/memory/protectli-vp46xx.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

    === "VP66XX"
        {%
            include-markdown "../../resources/hcl/memory/protectli-vp66xx.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

<!-- dts-hw-conf-gen: end of generated HCL tables -->
