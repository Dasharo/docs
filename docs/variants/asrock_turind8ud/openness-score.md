# Dasharo Openness Score

This page contains the [Dasharo Openness
Score](../../glossary.md#dasharo-openness-score) for ASRock Rack
TURIND8UD-2T/X550 Dasharo releases. The content of the page is generated with
[Dasharo Openness Score utility](https://github.com/Dasharo/Openness-Score).

=== "LinuxBoot"

    ## v0.9.0

    Report has been generated with Openness Score utility version v0.2-3-gb68f58db8217

    Openness Score for asrock_turind8ud_v0.9.0.rom

    Open-source code percentage: **76.0%**
    Closed-source code percentage: **24.0%**

    * Image size: 33554432 (0x2000000)
    * Number of regions: 9
    * Number of CBFSes: 1
    * Total open-source code size: 8604191 (0x834a1f)
    * Total closed-source code size: 2715840 (0x2970c0)
    * Total data size: 1620633 (0x18ba99)
    * Total empty size: 20613768 (0x13a8a88)

    ![](asrock_turind8ud_linuxboot_v0.9.0.rom_openness_chart.png)

    ![](asrock_turind8ud_linuxboot_v0.9.0.rom_openness_chart_full_image.png)

    > Numbers given above already include the calculations from CBFS regions
    > presented below

    ### FMAP regions

    | FMAP region | Offset | Size | Category |
    | ----------- | ------ | ---- | -------- |
    | HUBRIS_NVRAM | 0x0 | 0x10000 | data |
    | CONSOLE | 0xe87000 | 0x20000 | data |
    | FMAP | 0xea7000 | 0x1000 | data |
    | PSP_SEV_NVRAM | 0xea8000 | 0x8000 | data |
    | SMMSTORE | 0xeb0000 | 0x80000 | data |
    | RW_MRC_CACHE | 0xf30000 | 0xd0000 | data |
    | PAD | 0x1000000 | 0x1000000 | empty |

    ### CBFS COREBOOT

    * CBFS size: 15167488
    * Number of files: 20
    * Open-source files size: 8604191 (0x834a1f)
    * Closed-source files size: 2715840 (0x2970c0)
    * Data size: 10905 (0x2a99)
    * Empty size: 3836552 (0x3a8a88)

    > Numbers given above are already normalized (i.e. they already include size
    > of metadata and possible closed-source LAN drivers included in the payload
    > which are not visible in the table below)

    | CBFS filename | CBFS filetype | Size | Compression | Category |
    | ------------- | ------------- | ---- | ----------- | -------- |
    | fallback/payload | simple elf | 8332127 | none | open-source |
    | fallback/romstage | stage | 33001 | LZ4 | open-source |
    | fallback/ramstage | stage | 220490 | LZMA | open-source |
    | fallback/dsdt.aml | raw | 18573 | none | open-source |
    | cpu_microcode_b100.bin | microcode | 14368 | none | closed-source |
    | cpu_microcode_b110.bin | microcode | 14368 | none | closed-source |
    | cpu_microcode_b000.bin | microcode | 14368 | none | closed-source |
    | cpu_microcode_b010.bin | microcode | 14368 | none | closed-source |
    | apu/amdfw | amdfw | 2629632 | none | closed-source |
    | cpu_microcode_b020.bin | microcode | 14368 | none | closed-source |
    | cpu_microcode_b021.bin | microcode | 14368 | none | closed-source |
    | cbfs_master_header | cbfs header | 32 | none | data |
    | config | raw | 4108 | LZMA | data |
    | revision | raw | 919 | none | data |
    | build_info | raw | 118 | none | data |
    | cmos_layout.bin | cmos_layout | 864 | none | data |
    | sbom | raw | 3339 | none | data |
    | header_pointer | cbfs header | 4 | none | data |
    | (empty) | null | 1188 | none | empty |
    | (empty) | null | 3835364 | none | empty |

=== "UEFI"

    ## v0.9.0

    Report has been generated with Openness Score utility version v0.2-3-gb68f58db8217

    Openness Score for asrock_turind8ud_v0.9.0.rom

    Open-source code percentage: **24.3%**
    Closed-source code percentage: **75.7%**

    * Image size: 33554432 (0x2000000)
    * Number of regions: 10
    * Number of CBFSes: 2
    * Total open-source code size: 1642930 (0x1911b2)
    * Total closed-source code size: 5124288 (0x4e30c0)
    * Total data size: 1660770 (0x195762)
    * Total empty size: 25126444 (0x17f662c)

    ![](asrock_turind8ud_uefi_v0.9.0.rom_openness_chart.png)

    ![](asrock_turind8ud_uefi_v0.9.0.rom_openness_chart_full_image.png)

    > Numbers given above already include the calculations from CBFS regions
    > presented below

    ### FMAP regions

    | FMAP region | Offset | Size | Category |
    | ----------- | ------ | ---- | -------- |
    | HUBRIS_NVRAM | 0x0 | 0x10000 | data |
    | CONSOLE | 0xd87000 | 0x20000 | data |
    | FMAP | 0xda7000 | 0x1000 | data |
    | PSP_SEV_NVRAM | 0xea8000 | 0x8000 | data |
    | SMMSTORE | 0xeb0000 | 0x80000 | data |
    | RW_MRC_CACHE | 0xf30000 | 0xd0000 | data |
    | PAD | 0x1000000 | 0x1000000 | empty |

    ### CBFS COREBOOT

    * CBFS size: 14118912
    * Number of files: 21
    * Open-source files size: 1642930 (0x1911b2)
    * Closed-source files size: 5124288 (0x4e30c0)
    * Data size: 51014 (0xc746)
    * Empty size: 7300680 (0x6f6648)

    > Numbers given above are already normalized (i.e. they already include size
    > of metadata and possible closed-source LAN drivers included in the payload
    > which are not visible in the table below)

    | CBFS filename | CBFS filetype | Size | Compression | Category |
    | ------------- | ------------- | ---- | ----------- | -------- |
    | fallback/payload | simple elf | 1339419 | none | open-source |
    | fallback/romstage | stage | 33464 | LZ4 | open-source |
    | fallback/ramstage | stage | 251474 | LZMA | open-source |
    | fallback/dsdt.aml | raw | 18573 | none | open-source |
    | cpu_microcode_b100.bin | microcode | 14368 | none | closed-source |
    | cpu_microcode_b110.bin | microcode | 14368 | none | closed-source |
    | cpu_microcode_b000.bin | microcode | 14368 | none | closed-source |
    | cpu_microcode_b010.bin | microcode | 14368 | none | closed-source |
    | apu/amdfw | amdfw | 5038080 | none | closed-source |
    | cpu_microcode_b020.bin | microcode | 14368 | none | closed-source |
    | cpu_microcode_b021.bin | microcode | 14368 | none | closed-source |
    | cbfs_master_header | cbfs header | 32 | none | data |
    | config | raw | 4665 | LZMA | data |
    | revision | raw | 914 | none | data |
    | build_info | raw | 113 | none | data |
    | cmos_layout.bin | cmos_layout | 864 | none | data |
    | logo.bmp | raw | 11977 | LZMA | data |
    | sbom | raw | 30810 | none | data |
    | header_pointer | cbfs header | 4 | none | data |
    | (empty) | null | 612 | none | empty |
    | (empty) | null | 7300068 | none | empty |

    ### CBFS BOOTSPLASH

    * CBFS size: 1048576
    * Number of files: 1
    * Open-source files size: 0 (0x0)
    * Closed-source files size: 0 (0x0)
    * Data size: 28 (0x1c)
    * Empty size: 1048548 (0xfffe4)

    > Numbers given above are already normalized (i.e. they already include size
    > of metadata and possible closed-source LAN drivers included in the payload
    > which are not visible in the table below)

    | CBFS filename | CBFS filetype | Size | Compression | Category |
    | ------------- | ------------- | ---- | ----------- | -------- |
    | (empty) | null | 1048548 | none | empty |
