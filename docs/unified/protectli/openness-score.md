# Dasharo Openness Score

This page contains the [Dasharo Openness
Score](../../glossary.md#dasharo-openness-score) for Protectli Dasharo
releases. The content of the page is generated with [Dasharo Openness Score
utility](https://github.com/Dasharo/Openness-Score).

=== "vp46xx"

    ## v1.2.0

    Openness Score for protectli_vp46xx_v1.2.0.rom

    Open-source code percentage: **32.3%**
    Closed-source code percentage: **67.7%**

    * Image size: 16777216 (0x1000000)
    * Number of regions: 25
    * Number of CBFSes: 3
    * Total open-source code size: 4751528 (0x4880a8)
    * Total closed-source code size: 9978470 (0x984266)
    * Total data size: 497394 (0x796f2)
    * Total empty size: 1549824 (0x17a600)

    ![](protectli_vp46xx_v1.2.0.rom_openness_chart.png)

    ![](protectli_vp46xx_v1.2.0.rom_openness_chart_full_image.png)

    > Numbers given above already include the calculations from CBFS regions
    > presented below

    ### FMAP regions

    | FMAP region | Offset | Size | Category |
    | ----------- | ------ | ---- | -------- |
    | SI_ME | 0x1000 | 0x5ff000 | closed-source |
    | SI_DESC | 0x0 | 0x1000 | data |
    | RECOVERY_MRC_CACHE | 0x600000 | 0x10000 | data |
    | RW_MRC_CACHE | 0x610000 | 0x10000 | data |
    | SMMSTORE | 0x620000 | 0x40000 | data |
    | SHARED_DATA | 0x660000 | 0x2000 | data |
    | VBLOCK_DEV | 0x662000 | 0x2000 | data |
    | RW_NVRAM | 0x664000 | 0x6000 | data |
    | VBLOCK_A | 0x6ea000 | 0x2000 | data |
    | RW_FWID_A | 0xb7ff00 | 0x100 | data |
    | RO_VPD | 0xb80000 | 0x4000 | data |
    | FMAP | 0xb84000 | 0x800 | data |
    | RO_FRID | 0xb84800 | 0x100 | data |
    | RO_FRID_PAD | 0xb84900 | 0x700 | data |
    | GBB | 0xb85000 | 0x3000 | data |

    ### CBFS BOOTSPLASH

    * CBFS size: 524288
    * Number of files: 1
    * Open-source files size: 0 (0x0)
    * Closed-source files size: 0 (0x0)
    * Data size: 28 (0x1c)
    * Empty size: 524260 (0x7ffe4)

    > Numbers given above are already normalized (i.e. they already include size
    > of metadata and possible closed-source LAN drivers included in the payload
    > which are not visible in the table below)

    | CBFS filename | CBFS filetype | Size | Compression | Category |
    | ------------- | ------------- | ---- | ----------- | -------- |
    | (empty) | null | 524260 | none | empty |

    ### CBFS FW_MAIN_A

    * CBFS size: 4800256
    * Number of files: 16
    * Open-source files size: 2325656 (0x237c98)
    * Closed-source files size: 1845555 (0x1c2933)
    * Data size: 8261 (0x2045)
    * Empty size: 620784 (0x978f0)

    > Numbers given above are already normalized (i.e. they already include size
    > of metadata and possible closed-source LAN drivers included in the payload
    > which are not visible in the table below)

    | CBFS filename | CBFS filetype | Size | Compression | Category |
    | ------------- | ------------- | ---- | ----------- | -------- |
    | fallback/romstage | stage | 71104 | none | open-source |
    | fallback/ramstage | stage | 132189 | LZMA | open-source |
    | fallback/dsdt.aml | raw | 8831 | none | open-source |
    | fallback/postcar | stage | 31588 | none | open-source |
    | fallback/payload | simple elf | 2081944 | none | open-source |
    | cpu_microcode_blob.bin | microcode | 300032 | none | closed-source |
    | fspm.bin | fsp | 581632 | none | closed-source |
    | fspm_2.bin | fsp | 581632 | none | closed-source |
    | fsps.bin | fsp | 191132 | LZMA | closed-source |
    | fsps_2.bin | fsp | 191127 | LZMA | closed-source |
    | config | raw | 4993 | LZMA | data |
    | revision | raw | 859 | none | data |
    | build_info | raw | 103 | none | data |
    | vbt.bin | raw | 1183 | LZMA | data |
    | (empty) | null | 164 | none | empty |
    | (empty) | null | 4004 | none | empty |

    ### CBFS COREBOOT

    * CBFS size: 4685824
    * Number of files: 22
    * Open-source files size: 2425872 (0x250410)
    * Closed-source files size: 1845555 (0x1c2933)
    * Data size: 9617 (0x2591)
    * Empty size: 404780 (0x62d2c)

    > Numbers given above are already normalized (i.e. they already include size
    > of metadata and possible closed-source LAN drivers included in the payload
    > which are not visible in the table below)

    | CBFS filename | CBFS filetype | Size | Compression | Category |
    | ------------- | ------------- | ---- | ----------- | -------- |
    | fallback/romstage | stage | 71104 | none | open-source |
    | fallback/ramstage | stage | 132189 | LZMA | open-source |
    | fallback/dsdt.aml | raw | 8831 | none | open-source |
    | fallback/postcar | stage | 31588 | none | open-source |
    | fallback/payload | simple elf | 2081944 | none | open-source |
    | fallback/verstage | stage | 61752 | none | open-source |
    | bootblock | bootblock | 38464 | none | open-source |
    | cpu_microcode_blob.bin | microcode | 300032 | none | closed-source |
    | fspm.bin | fsp | 581632 | none | closed-source |
    | fspm_2.bin | fsp | 581632 | none | closed-source |
    | fsps.bin | fsp | 191132 | LZMA | closed-source |
    | fsps_2.bin | fsp | 191127 | LZMA | closed-source |
    | cbfs_master_header | cbfs header | 28 | none | data |
    | intel_fit | intel_fit | 80 | none | data |
    | config | raw | 4993 | LZMA | data |
    | revision | raw | 859 | none | data |
    | build_info | raw | 103 | none | data |
    | cmos_layout.bin | cmos_layout | 708 | none | data |
    | vbt.bin | raw | 1183 | LZMA | data |
    | (empty) | null | 420 | none | empty |
    | (empty) | null | 2724 | none | empty |
    | (empty) | null | 401636 | none | empty |

=== "vp2410"

# Dasharo Openness Score

    ## v1.1.0

    Openness Score for protectli_vp2410_v1.1.0.rom

    Open-source code percentage: **31.7%**
    Closed-source code percentage: **68.3%**

    * Image size: 8388608 (0x800000)
    * Number of regions: 17
    * Number of CBFSes: 2
    * Total open-source code size: 2313343 (0x234c7f)
    * Total closed-source code size: 4983646 (0x4c0b5e)
    * Total data size: 409627 (0x6401b)
    * Total empty size: 681992 (0xa6808)

    ![](protectli_vp2410_v1.1.0.rom_openness_chart.png)

    ![](protectli_vp2410_v1.1.0.rom_openness_chart_full_image.png)

    > Numbers given above already include the calculations from CBFS regions
    > presented below

    ### FMAP regions

    | FMAP region | Offset | Size | Category |
    | ----------- | ------ | ---- | -------- |
    | IFWI | 0x1000 | 0x2ff000 | closed-source |
    | SI_DESC | 0x0 | 0x1000 | data |
    | RECOVERY_MRC_CACHE | 0x300000 | 0x10000 | data |
    | RW_MRC_CACHE | 0x310000 | 0x10000 | data |
    | FMAP | 0x3a1000 | 0x1000 | data |
    | SMMSTORE | 0x67f000 | 0x40000 | data |

    ### CBFS BOOTSPLASH

    * CBFS size: 524288
    * Number of files: 1
    * Open-source files size: 0 (0x0)
    * Closed-source files size: 0 (0x0)
    * Data size: 28 (0x1c)
    * Empty size: 524260 (0x7ffe4)

    > Numbers given above are already normalized (i.e. they already include size
    > of metadata and possible closed-source LAN drivers included in the payload
    > which are not visible in the table below)

    | CBFS filename | CBFS filetype | Size | Compression | Category |
    | ------------- | ------------- | ---- | ----------- | -------- |
    | (empty) | null | 524260 | none | empty |

    ### CBFS COREBOOT

    * CBFS size: 3002368
    * Number of files: 17
    * Open-source files size: 2313343 (0x234c7f)
    * Closed-source files size: 523102 (0x7fb5e)
    * Data size: 8191 (0x1fff)
    * Empty size: 157732 (0x26824)

    > Numbers given above are already normalized (i.e. they already include size
    > of metadata and possible closed-source LAN drivers included in the payload
    > which are not visible in the table below)

    | CBFS filename | CBFS filetype | Size | Compression | Category |
    | ------------- | ------------- | ---- | ----------- | -------- |
    | fallback/payload | simple elf | 2080815 | none | open-source |
    | fallback/romstage | stage | 47192 | LZ4 | open-source |
    | fallback/ramstage | stage | 125678 | LZMA | open-source |
    | fallback/dsdt.aml | raw | 7126 | none | open-source |
    | pt | raw | 20480 | none | open-source |
    | pdpt | raw | 32 | none | open-source |
    | fallback/postcar | stage | 32020 | none | open-source |
    | cpu_microcode_blob.bin | microcode | 152576 | none | closed-source |
    | fspm.bin | fsp | 178014 | LZ4 | closed-source |
    | fsps.bin | fsp | 192512 | none | closed-source |
    | cbfs_master_header | cbfs header | 28 | none | data |
    | config | raw | 4505 | LZMA | data |
    | revision | raw | 859 | none | data |
    | build_info | raw | 103 | none | data |
    | vbt.bin | raw | 1271 | LZMA | data |
    | header_pointer | cbfs header | 4 | none | data |
    | (empty) | null | 157732 | none | empty |

=== "vp2420"

    ## v1.2.0

    Openness Score for protectli_vp2420_v1.2.0.rom

    Open-source code percentage: **35.3%**
    Closed-source code percentage: **64.7%**

    * Image size: 16777216 (0x1000000)
    * Number of regions: 26
    * Number of CBFSes: 3
    * Total open-source code size: 4806882 (0x4958e2)
    * Total closed-source code size: 8800924 (0x864a9c)
    * Total data size: 627958 (0x994f6)
    * Total empty size: 2541452 (0x26c78c)

    ![](protectli_vp2420_v1.2.0.rom_openness_chart.png)

    ![](protectli_vp2420_v1.2.0.rom_openness_chart_full_image.png)

    > Numbers given above already include the calculations from CBFS regions
    > presented below

    ### FMAP regions

    | FMAP region | Offset | Size | Category |
    | ----------- | ------ | ---- | -------- |
    | SI_ME | 0x1000 | 0x6ff000 | closed-source |
    | SI_DESC | 0x0 | 0x1000 | data |
    | RECOVERY_MRC_CACHE | 0x700000 | 0x10000 | data |
    | RW_MRC_CACHE | 0x710000 | 0x10000 | data |
    | SMMSTORE | 0x720000 | 0x40000 | data |
    | SHARED_DATA | 0x760000 | 0x2000 | data |
    | VBLOCK_DEV | 0x762000 | 0x2000 | data |
    | RW_NVRAM | 0x764000 | 0x6000 | data |
    | CONSOLE | 0x76a000 | 0x20000 | data |
    | VBLOCK_A | 0x88a000 | 0x2000 | data |
    | RW_FWID_A | 0xbfff00 | 0x100 | data |
    | RO_VPD | 0xc00000 | 0x4000 | data |
    | FMAP | 0xc04000 | 0x800 | data |
    | RO_FRID | 0xc04800 | 0x100 | data |
    | RO_FRID_PAD | 0xc04900 | 0x700 | data |
    | GBB | 0xc05000 | 0x3000 | data |

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

    ### CBFS FW_MAIN_A

    * CBFS size: 3620608
    * Number of files: 13
    * Open-source files size: 2365521 (0x241851)
    * Closed-source files size: 732494 (0xb2d4e)
    * Data size: 8513 (0x2141)
    * Empty size: 514080 (0x7d820)

    > Numbers given above are already normalized (i.e. they already include size
    > of metadata and possible closed-source LAN drivers included in the payload
    > which are not visible in the table below)

    | CBFS filename | CBFS filetype | Size | Compression | Category |
    | ------------- | ------------- | ---- | ----------- | -------- |
    | fallback/payload | simple elf | 2081638 | none | open-source |
    | fallback/romstage | stage | 85520 | none | open-source |
    | fallback/ramstage | stage | 129116 | LZMA | open-source |
    | fallback/dsdt.aml | raw | 9759 | none | open-source |
    | fallback/postcar | stage | 59488 | none | open-source |
    | cpu_microcode_blob.bin | microcode | 20480 | none | closed-source |
    | fspm.bin | fsp | 495616 | none | closed-source |
    | fsps.bin | fsp | 216398 | LZ4 | closed-source |
    | config | raw | 4815 | LZMA | data |
    | revision | raw | 859 | none | data |
    | build_info | raw | 103 | none | data |
    | vbt.bin | raw | 1200 | LZMA | data |
    | (empty) | null | 514080 | none | empty |

    ### CBFS COREBOOT

    * CBFS size: 4161536
    * Number of files: 17
    * Open-source files size: 2441361 (0x254091)
    * Closed-source files size: 732494 (0xb2d4e)
    * Data size: 8857 (0x2299)
    * Empty size: 978824 (0xeef88)

    > Numbers given above are already normalized (i.e. they already include size
    > of metadata and possible closed-source LAN drivers included in the payload
    > which are not visible in the table below)

    | CBFS filename | CBFS filetype | Size | Compression | Category |
    | ------------- | ------------- | ---- | ----------- | -------- |
    | fallback/payload | simple elf | 2081638 | none | open-source |
    | fallback/romstage | stage | 85520 | none | open-source |
    | fallback/ramstage | stage | 129116 | LZMA | open-source |
    | fallback/dsdt.aml | raw | 9759 | none | open-source |
    | fallback/postcar | stage | 59488 | none | open-source |
    | bootblock | bootblock | 75840 | none | open-source |
    | cpu_microcode_blob.bin | microcode | 20480 | none | closed-source |
    | fspm.bin | fsp | 495616 | none | closed-source |
    | fsps.bin | fsp | 216398 | LZ4 | closed-source |
    | cbfs_master_header | cbfs header | 28 | none | data |
    | intel_fit | intel_fit | 80 | none | data |
    | config | raw | 4815 | LZMA | data |
    | revision | raw | 859 | none | data |
    | build_info | raw | 103 | none | data |
    | vbt.bin | raw | 1200 | LZMA | data |
    | (empty) | null | 1060 | none | empty |
    | (empty) | null | 977764 | none | empty |
