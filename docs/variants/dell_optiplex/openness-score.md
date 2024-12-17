# Dasharo Openness Score

This page contains the [Dasharo Openness
Score](../../glossary.md#dasharo-openness-score) for Dasharo releases
compatible with Dell OptiPlex 7010/9010. The content of the page is generated
with [Dasharo Openness Score
utility](https://github.com/Dasharo/Openness-Score).

## v0.1.1

Openness Score for dell_optiplex_7010_9010_v0.1.1.rom

Open-source code percentage: **24.6%**
Closed-source code percentage: **75.4%**

* Image size: 12582912 (0xc00000)
* Number of regions: 13
* Number of CBFSes: 1
* Total open-source code size: 2056924 (0x1f62dc)
* Total closed-source code size: 6313984 (0x605800)
* Total data size: 408256 (0x63ac0)
* Total empty size: 3803748 (0x3a0a64)

![](dell_optiplex_7010_9010_v0.1.1.rom_openness_chart.png)

![](dell_optiplex_7010_9010_v0.1.1.rom_openness_chart_full_image.png)

> Numbers given above already include the calculations from CBFS regions
> presented below

### FMAP regions

| FMAP region | Offset | Size | Category |
| ----------- | ------ | ---- | -------- |
| SI_ME | 0x5000 | 0x5fb000 | closed-source |
| SI_DESC | 0x0 | 0x1000 | data |
| SMMSTORE | 0x800000 | 0x40000 | data |
| RW_MRC_CACHE | 0x840000 | 0x10000 | data |
| RW_ELOG | 0x850000 | 0x10000 | data |
| FMAP | 0x860000 | 0x800 | data |
| UNUSED | 0x600000 | 0x200000 | empty |

### CBFS COREBOOT

* CBFS size: 3799040
* Number of files: 14
* Open-source files size: 2056924 (0x1f62dc)
* Closed-source files size: 26624 (0x6800)
* Data size: 8896 (0x22c0)
* Empty size: 1706596 (0x1a0a64)

> Numbers given above are already normalized (i.e. they already include size
> of metadata and possible closed-source LAN drivers included in the payload
> which are not visible in the table below)

| CBFS filename | CBFS filetype | Size | Compression | Category |
| ------------- | ------------- | ---- | ----------- | -------- |
| fallback/payload | simple elf | 1729914 | none | open-source |
| fallback/romstage | stage | 105808 | none | open-source |
| fallback/ramstage | stage | 137635 | LZMA | open-source |
| fallback/dsdt.aml | raw | 14827 | none | open-source |
| fallback/postcar | stage | 34820 | none | open-source |
| bootblock | bootblock | 33920 | none | open-source |
| cpu_microcode_blob.bin | microcode | 26624 | none | closed-source |
| cbfs_master_header | cbfs header | 32 | none | data |
| config | raw | 4040 | LZMA | data |
| revision | raw | 863 | none | data |
| build_info | raw | 114 | none | data |
| vbt.bin | raw | 1438 | LZMA | data |
| cmos_layout.bin | cmos_layout | 1204 | none | data |
| (empty) | null | 1706596 | none | empty |
