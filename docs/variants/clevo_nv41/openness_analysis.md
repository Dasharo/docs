# Intro

This document aims to compare the openness of Dasharo Firmware and Insyde BIOS.

There is an [ongoing discussion](https://github.com/Dasharo/dasharo-issues/issues/43) about the methodology of the openness metric.

## BIOS versions used in the analysis

* [Dasharo coreboot v0.5.0](https://cloud.3mdeb.com/index.php/s/xM8FcCsMc8kfmKB)
* [Insyde BIOS](https://cloud.3mdeb.com/index.php/s/6Pte9F9nefxQEMN)

## Insyde BIOS

In the case of the Insyde bios, the entire image should be considered
proprietary. There are several parts of the image that have a well-known
structure or make use of a public standard. However, to decode these structures,
one needs to employ reverse-engineering tools and techniques to know what
structures are present.

## Dasharo BIOS

### CBFS

| image                  | size (bytes) | Is it open-source? |
| ---                    | ---:         | ---                |
| cbfs master header     | 20h          | Yes                |
| fallback/romstage      | 14770h       | Yes                |
| cpu_microcode_blob.bin | 31C00h       | No                 |
| intel_fit              | 50h          | Yes                |
| fallback/ramstage      | 1E626h       | Yes                |
| config                 | 579h         | Yes                |
| revision               | 351h         | Yes                |
| build_info             | 5Dh          | Yes                |
| fallback/dsdt.aml      | 6233h        | Yes                |
| vbt.bin                | 51Ch         | Yes                |
| (empty)                | 1E4h         | N/A                |
| fspm.bin               | 9F000h       | No                 |
| cmos_layout.bin        | 22Ch         | Yes                |
| (empty)                | D24h         | N/A                |
| fsps.bin               | 43676h       | No                 |
| fallback/postcar       | 8F24h        | Yes                |
| fallback/payload       | 1771C5h      | Yes                |
| fallback/verstage      | 12C80h       | Yes                |
| (empty)                | 10E5E4h      | N/A                |
| bootblock              | 74C0h        | Yes                |
| **Summary**            | 3F7A33h      | **In 62.9%**       |

Open and closed source images are in the table below.

| type                 | summarised size | Percent |
| ---                  | ---:            | ---:    |
| open-source          | 1D42D1h         | 62.9%   |
| closed-source        | 114276h         | 37.1%   |
| empty (not included) | 10F4ECh         |         |

### Whole flash image

| region      | size     | open-source percent (bytes) |
| ---         | ---:     | ---:                        |
| descriptor  | 1000h    | 0%                          |
| ME          | 4FF000h  | 0%                          |
| BIOS        | B00000h  | 62.9%                       |
| **Summary** | 1000000h | **43.2%**                   |

## Summary

| image   | open-source percent (bytes) |
| ---     | ---:                        |
| Insyde  | 0%                          |
| Dasharo | 43.2%                       |
