# Intro

This document aims to compare the openness of Dasharo firmware and AMI BIOS.

There is an
[ongoing discussion](https://github.com/Dasharo/dasharo-issues/issues/43)
about the methodology of the openness metric.

## BIOS versions used in the analysis

* [Dasharo v1.0.0](https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.0.0/msi_ms7d25_v1.0.0.rom)
* [AMI BIOS v1.0](https://download.msi.com/bos_exe/mb/7D25v10.zip)

## MSI original BIOS from AMI

In the case of the AMI BIOS, the entire image should be considered
proprietary. There are several parts of the image that have a well-known
structure or make use of a public standard. However, to decode these structures,
one needs to employ reverse-engineering tools and techniques to know what
structures are present.

## Dasharo BIOS

### CBFS regions

The below table shows only a single FMAP region COREBOOT. There are also two RW
vboot partitions containing copies of the same components from COREBOOT region
(except the verstage, bootblock and cbfs master header). Note that there are
other regions to store non-volatile data like MRC cache, UEFI variables or
vboot state backup.

Region COREBOOT:

| File                   | Size (bytes)   | Is it open-source?         |
| ---                    | ---:           | ---                        |
| cbfs master header     | 32             | &#10004;                   |
| fallback/romstage      | 95152          | &#10004;                   |
| cpu_microcode_blob.bin | 944144         | &#10006;                   |
| intel_fit              | 80             | &#10004;                   |
| fallback/ramstage      | 127231(LZMA)   | &#10004;                   |
| config                 | 1378           | &#10004;                   |
| revision               | 842            | &#10004;                   |
| build_info             | 142            | &#10004;                   |
| fallback/dsdt.aml      | 9973           | &#10004;                   |
| vbt.bin                | 1254 (LZMA)    | &#10004;                   |
| (empty)                | 2596           | N/A                        |
| fspm.bin               | 720896         | &#10006;                   |
| fsps.bin               | 290481 (LZ4)   | &#10006;                   |
| fallback/postcar       | 37504          | &#10004;                   |
| fallback/payload       | 1813047 (LZMA) | &#10004; (with exceptions) |
| fallback/verstage      | 77008          | &#10004;                   |
| (empty)                | 1055076        | N/A                        |
| bootblock              | 31808          | &#10004;                   |

The payload used is Tianocore EDK2 UEFIPayload. In order to support network
boot over i225 Ethernet, an i225 EFI driver is included in the payload. The
driver is 154064 bytes in size uncompressed (63445 LZMA compressed). The 63445
bytes will be added to closed source pool and removed from the payload size in
the calculations.

Note that UEFIPayload has support for Option ROM loading, for example to
support external graphics card output during POST. It is an additional
closed-source code which depends on the hardware configuration and is not
included in the calculations.

| Type                      | Total size (bytes) | Percent    |
| ---                       | ---:               | ---:       |
| COREBOOT region           | 5208644            | N/A        |
| empty (not included)      | 1057672            | N/A        |
| code size (open + closed) | 4150972            | N/A        |
| open-source               | 2132006            | **51.36%** |
| closed-source             | 2018966            | 48.64%     |

Region FW_MAIN_A/FW_MAIN_B:

| File                   | Size (bytes)   | Is it open-source?         |
| ---                    | ---:           | ---                        |
| fallback/romstage      | 95152          | &#10004;                   |
| cpu_microcode_blob.bin | 944144         | &#10006;                   |
| fallback/ramstage      | 127231(LZMA)   | &#10004;                   |
| config                 | 1378           | &#10004;                   |
| revision               | 842            | &#10004;                   |
| build_info             | 142            | &#10004;                   |
| fallback/dsdt.aml      | 9973           | &#10004;                   |
| (empty)                | 100            | N/A                        |
| fspm.bin               | 720896         | &#10006;                   |
| fsps.bin               | 290481 (LZ4)   | &#10006;                   |
| vbt.bin                | 1254 (LZMA)    | &#10004;                   |
| fallback/postcar       | 37504          | &#10004;                   |
| fallback/payload       | 1813047 (LZMA) | &#10004; (with exceptions) |

| Type                      | Total size (bytes) | Percent    |
| ---                       | ---:               | ---:       |
| FW_MAIN_A/B region        | 5340928            | N/A        |
| empty (not included)      | 1298884            | N/A        |
| code size (open + closed) | 4042044            | N/A        |
| open-source               | 2023078            | **50.05%** |
| closed-source             | 2018966            | 49.95%     |

COREBOOT has slightly higher open-source code percentage due to verstage and
bootblock not being present in FW_MAIN_A/B regions.

### Whole flash image

To get the overall BIOS region and full image percentage of open source code we
ignore unused space or FMAP regions which do not have CBFS and are merely data
generated during build process or boot process. The BIOS region percentage is
calculated as follows:

`(COREBOOT region open-source size + FW_MAIN_A/B open-source size * 2) * 100`
divided by `(COREBOOT region code size + FW_MAIN_A/B code size * 2)`.

Full image percentage is calculated as follows:

`(COREBOOT region open-source size + FW_MAIN_A/B open-source size * 2) * 100`
divided by
`(ME + descriptor + COREBOOT region code size + FW_MAIN_A/B code size * 2)`.

| Region      | Size (bytes) | Open-source percent (bytes) |
| ---         | ---:         | ---:                        |
| descriptor  | 0x1000       | 0%                          |
| ME          | 0x3D9000     | 0%                          |
| unused hole | 0xC26000     | N/A                         |
| BIOS        | 0x1000000    | **50.5%**                   |
| **Summary** | 0x2000000    | **37%**                     |

![](/images/openness_msi_bios.png)

![](/images/openness_msi_bios_full.png)

## Summary

| Image    | Open-source percent (bytes) |
| ---      | ---:                        |
| AMI BIOS | 0%                          |
| Dasharo  | **37%**                     |

![](/images/openness_msi.png)

![](/images/openness_msi_full.png)