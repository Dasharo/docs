# Dasharo Openness Score

This page contains the [Dasharo Openness
Score](../../glossary.md#dasharo-openness-score) for PC Engines apu2 series
Dasharo releases. The content of the page is generated with [Dasharo Openness
Score utility](https://github.com/Dasharo/Openness-Score).

## v0.9.0

Openness Score for pcengines_apu2_v0.9.0.rom

Open-source code percentage: **85.3%**
Closed-source code percentage: **14.7%**

* Image size: 8388608 (0x800000)
* Number of regions: 12
* Number of CBFSes: 2
* Total open-source code size: 4358328 (0x4280b8)
* Total closed-source code size: 749792 (0xb70e0)
* Total data size: 359260 (0x57b5c)
* Total empty size: 2921228 (0x2c930c)

![](pcengines_apu2_v0.9.0.rom_openness_chart.png)

![](pcengines_apu2_v0.9.0.rom_openness_chart_full_image.png)

> Numbers given above already include the calculations from CBFS regions
> presented below

### FMAP regions

| FMAP region | Offset | Size | Category |
| ----------- | ------ | ---- | -------- |
| SMMSTORE | 0x0 | 0x40000 | data |
| RW_NVRAM | 0x40000 | 0x1000 | data |
| VBLOCK_A | 0x41000 | 0x2000 | data |
| RW_FWID_A | 0x3fff00 | 0x100 | data |
| FMAP | 0x400000 | 0x1000 | data |
| RO_FRID | 0x401000 | 0x100 | data |
| RO_FRID_PAD | 0x401100 | 0x700 | data |
| GBB | 0x401800 | 0x10000 | data |

### CBFS FW_MAIN_A

* CBFS size: 3919616
* Number of files: 10
* Open-source files size: 2150524 (0x20d07c)
* Closed-source files size: 0 (0x0)
* Data size: 6180 (0x1824)
* Empty size: 1762912 (0x1ae660)

> Numbers given above are already normalized (i.e. they already include size
> of metadata and possible closed-source LAN drivers included in the payload
 > which are not visible in the table below)

| CBFS filename | CBFS filetype | Size | Compression | Category |
| ------------- | ------------- | ---- | ----------- | -------- |
| fallback/payload | simple elf | 1960751 | none | open-source |
| fallback/romstage | stage | 49464 | none | open-source |
| fallback/ramstage | stage | 101300 | LZMA | open-source |
| fallback/dsdt.aml | raw | 5713 | none | open-source |
| fallback/postcar | stage | 33296 | none | open-source |
| config | raw | 3848 | LZMA | data |
| revision | raw | 854 | none | data |
| build_info | raw | 97 | none | data |
| spd.bin | spd | 256 | none | data |
| (empty) | null | 1762912 | none | empty |

### CBFS COREBOOT

* CBFS size: 4122624
* Number of files: 16
* Open-source files size: 2207804 (0x21b03c)
* Closed-source files size: 749792 (0xb70e0)
* Data size: 6712 (0x1a38)
* Empty size: 1158316 (0x11acac)

> Numbers given above are already normalized (i.e. they already include size
> of metadata and possible closed-source LAN drivers included in the payload
 > which are not visible in the table below)

| CBFS filename | CBFS filetype | Size | Compression | Category |
| ------------- | ------------- | ---- | ----------- | -------- |
| fallback/payload | simple elf | 1960751 | none | open-source |
| fallback/romstage | stage | 49464 | none | open-source |
| fallback/dsdt.aml | raw | 5713 | none | open-source |
| fallback/ramstage | stage | 101300 | LZMA | open-source |
| fallback/postcar | stage | 33296 | none | open-source |
| bootblock | bootblock | 57280 | none | open-source |
| AGESA | raw | 504032 | none | closed-source |
| cbfs_master_header | cbfs header | 28 | none | data |
| config | raw | 3848 | LZMA | data |
| revision | raw | 854 | none | data |
| build_info | raw | 97 | none | data |
| spd.bin | spd | 256 | none | data |
| (empty) | null | 3364 | none | empty |
| (empty) | null | 1064868 | none | empty |
| (empty) | null | 90084 | none | empty |
