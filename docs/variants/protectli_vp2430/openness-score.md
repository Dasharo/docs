# Dasharo Openness Score

This page contains the [Dasharo Openness
Score](../../glossary.md#dasharo-openness-score) for Protectli VP2430 Dasharo
releases. The content of the page is generated with [Dasharo Openness Score
utility](https://github.com/Dasharo/Openness-Score).

## v0.9.0

Report has been generated with Openness Score utility version v0.2

Openness Score for protectli_vp2430_v0.9.0.rom

Open-source code percentage: **33.8%**
Closed-source code percentage: **66.2%**

* Image size: 16777216 (0x1000000)
* Number of regions: 24
* Number of CBFSes: 3
* Total open-source code size: 3414850 (0x341b42)
* Total closed-source code size: 6694310 (0x6625a6)
* Total data size: 866832 (0xd3a10)
* Total empty size: 5801224 (0x588508)

![](protectli_vp2430_v0.9.0.rom_openness_chart.png)

![](protectli_vp2430_v0.9.0.rom_openness_chart_full_image.png)

> Numbers given above already include the calculations from CBFS regions
> presented below

### FMAP regions

| FMAP region | Offset | Size | Category |
| ----------- | ------ | ---- | -------- |
| SMMSTORE | 0x500000 | 0x40000 | data |
| RECOVERY_MRC_CACHE | 0x540000 | 0x20000 | data |
| RW_MRC_CACHE | 0x560000 | 0x20000 | data |
| RW_VPD | 0x580000 | 0x2000 | data |
| RW_NVRAM | 0x582000 | 0x6000 | data |
| VBLOCK_A | 0x608000 | 0x10000 | data |
| RW_FWID_A | 0xafff00 | 0x100 | data |
| RO_VPD | 0xb00000 | 0x4000 | data |
| FMAP | 0xb04000 | 0x800 | data |
| RO_FRID | 0xb04800 | 0x100 | data |
| RO_FRID_PAD | 0xb04900 | 0x700 | data |
| GBB | 0xb05000 | 0x3000 | data |

### IFD regions

| IFD region | Start | End | Size | Category |
| -------------- | ----- | --- | ---- | -------- |
| Intel ME | 0x00001000 | 0x00413fff | 0x413000 | closed-source |
| Flash Descriptor | 0x00000000 | 0x00000fff | 0x1000 | data |
| Device Exp2 | 0x00414000 | 0x004fffff | 0xec000 | empty |

### CBFS BOOTSPLASH

* CBFS size: 524288
* Number of files: 2
* Open-source files size: 0 (0x0)
* Closed-source files size: 0 (0x0)
* Data size: 188768 (0x2e160)
* Empty size: 335520 (0x51ea0)

> Numbers given above are already normalized (i.e. they already include size
> of metadata and possible closed-source LAN drivers included in the payload
> which are not visible in the table below)

| CBFS filename | CBFS filetype | Size | Compression | Category |
| ------------- | ------------- | ---- | ----------- | -------- |
| logo.bmp | raw | 188663 | LZMA | data |
| (empty) | null | 335520 | none | empty |

### CBFS FW_MAIN_A

* CBFS size: 5144320
* Number of files: 13
* Open-source files size: 1663265 (0x196121)
* Closed-source files size: 1211091 (0x127ad3)
* Data size: 8940 (0x22ec)
* Empty size: 2261024 (0x228020)

> Numbers given above are already normalized (i.e. they already include size
> of metadata and possible closed-source LAN drivers included in the payload
> which are not visible in the table below)

| CBFS filename | CBFS filetype | Size | Compression | Category |
| ------------- | ------------- | ---- | ----------- | -------- |
| fallback/payload | simple elf | 1362458 | none | open-source |
| fallback/romstage | stage | 98064 | none | open-source |
| fallback/ramstage | stage | 145019 | LZMA | open-source |
| fallback/dsdt.aml | raw | 19448 | none | open-source |
| fallback/postcar | stage | 38276 | none | open-source |
| cpu_microcode_blob.bin | microcode | 138240 | none | closed-source |
| fspm.bin | fsp | 786432 | none | closed-source |
| fsps.bin | fsp | 286419 | LZ4 | closed-source |
| config | raw | 5586 | LZMA | data |
| revision | raw | 876 | none | data |
| build_info | raw | 120 | none | data |
| vbt.bin | raw | 1274 | LZMA | data |
| (empty) | null | 1508 | none | empty |

### CBFS COREBOOT

* CBFS size: 5210112
* Number of files: 17
* Open-source files size: 1751585 (0x1aba21)
* Closed-source files size: 1211091 (0x127ad3)
* Data size: 9412 (0x24c4)
* Empty size: 2238024 (0x222648)

> Numbers given above are already normalized (i.e. they already include size
> of metadata and possible closed-source LAN drivers included in the payload
> which are not visible in the table below)

| CBFS filename | CBFS filetype | Size | Compression | Category |
| ------------- | ------------- | ---- | ----------- | -------- |
| fallback/payload | simple elf | 1362458 | none | open-source |
| fallback/romstage | stage | 98064 | none | open-source |
| fallback/ramstage | stage | 145019 | LZMA | open-source |
| fallback/dsdt.aml | raw | 19448 | none | open-source |
| fallback/postcar | stage | 38276 | none | open-source |
| bootblock | bootblock | 88320 | none | open-source |
| cpu_microcode_blob.bin | microcode | 138240 | none | closed-source |
| fspm.bin | fsp | 786432 | none | closed-source |
| fsps.bin | fsp | 286419 | LZ4 | closed-source |
| cbfs_master_header | cbfs header | 32 | none | data |
| intel_fit | intel_fit | 80 | none | data |
| config | raw | 5586 | LZMA | data |
| revision | raw | 876 | none | data |
| build_info | raw | 120 | none | data |
| vbt.bin | raw | 1274 | LZMA | data |
| (empty) | null | 1252 | none | empty |
| (empty) | null | 2236772 | none | empty |
