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
=== "CPU HCL (26 Oct 2026)"

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

    === "ODROID H4"
        {%
            include-markdown "../../resources/hcl/cpu/hardkernel-odroid-h4.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

=== "Memory HCL (26 Oct 2026)"

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
        - `Dasharo HCL report` if it was reported using
          [DTS](../../dasharo-tools-suite/documentation/features.md#hcl-report).
        - Link to the report if it comes from a public hardware database.

    === "ODROID H4"
        {%
            include-markdown "../../resources/hcl/memory/hardkernel-odroid-h4.md"
            start="<!--start-->"
            end="<!--end-->"
        %}

<!-- dts-hw-conf-gen: end of generated HCL tables -->
