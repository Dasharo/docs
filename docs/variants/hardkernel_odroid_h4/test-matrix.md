# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary compatible with
Hardkernel devices.

## Module: Dasharo compatibility

| No. | Supported test suite                  | Test suite ID | Supported test cases                 |
|:---:|:--------------------------------------|:-------------:|:-------------------------------------|
| 1.  | [Custom boot order][CBO]              | CBO           | CBO001.002                           |
| 2.  | [Custom Boot Keys][CBK]               | CBK           | All                                  |
| 3.  | [Custom logo][CLG]                    | CLG           | All                                  |
| 4.  | [USB HID and MSC Support][USB]        | USB           | USB001.0001, USB001.002, USB002.001, USB002.002|
| 5.  | [Custom network boot entries][CNB]    | CNB           | CNB001.002                           |
| 6.  | [UEFI compatible interface][EFI]      | EFI           | EFI001.001                           |
| 7.  | [UEFI Shell][USH]                     | USH           | All                                  |
| 8.  | [NVMe support][NVM]                   | NVM           | NVM001.001, NVM001.002               |
| 9.  | [Network boot][PXE]                   | PXE           | All                                  |
| 10. | [Display ports][DSP]                  | DSP           | DSP002.001, DSP003.001               |
| 11. | [Audio subsystem][AUD]                | AUD           | AUD007.001, AUD008.001               |
| 12. | [Sleep mode][SUSP]                    | SUSP          | SUSP001.001, SUSP002.001, SUSP003.001, SUSP005.001|
| 13. | [SMBIOS verification][DMI]            | DMI           | All                                  |
| 14. | [eMMC support][MMC]                  | MMC           | All                                  |
| 15. | <!--[SATA support][SATA]--> Sata support           |               | All                                  |
| 16. | [Sign of life][SOL]                   | SOL           | All                                  |
| 17. | [Persistent Boot Splash][LCM]         | LCM           | All                                  |
| 18. | [Debian Stable and Ubuntu LTS support][LBT] | LBT     | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
| 19. | [Power state after power fail][PSF]    | PSF           | All                                  |
| 20. | [Dasharo Tools Suite][DTS]            | DTS           | DTS001.001, DTS002.001, DTS003.001, DTS004.001, DTS005.001, DTS006.001 |
| 21. | [Reset to defaults][RTD]              | RTD           | RTD001.001, RTD002.001, RTD003.001, RTD004.001, RTD006.001 |
| 22. | [Ethernet interface][NET]             | NET           | All                                  |
| 23. | [Dasharo Configuration Utility][NET]  | DCU           | DCU001.001, DCU002.001, DCU003.001   |
| 24. | [ESP scanning][ESP]                   | ESP           | All                                  |
| 25. | [Network Boot Utilities][NBT]          | NBT           | All                                  |
| 26. | [USB detection][UDT]                  | UDT           | All                                  |
| 27. | [USB booting][UBT]                    | UBT           | All                                  |
| 28. | <!--[Setup Menu information][SET]-->  Setup Menu information        | SET           | All                                  |
| 29. | [Ubuntu booting performance test][BUB]| BUB           | All                                  |
| 30. | [CPU status][CPU]                     | CPU           | CPU001.001, CPU002.001, CPU003.001, CPU004.001|
| 31. | [Auto boot time-out][BMM]             | BMM           | All                                  |

[CBO]: ../../unified-test-documentation/dasharo-compatibility/325-custom-boot-order.md
[CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
[CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
[USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
[CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md
[EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
[USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
[NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
[PXE]: ../../unified-test-documentation/dasharo-compatibility/315-network-boot.md
[DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
[AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
[SUSP]: ../../unified-test-documentation/dasharo-compatibility/31M-platform-suspend-and-resume.md
[DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
[MMC]: ../../unified-test-documentation/dasharo-compatibility/31M-emmc-support.md
<!--[SATA]: .-->
[SOL]: ../../unified-test-documentation/dasharo-compatibility/347-sign-of-life.md
[LCM]: ../../unified-test-documentation/dasharo-compatibility/328-logo-customization-functionality.md
[LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
[PSF]: ../../unified-test-documentation/dasharo-compatibility/360-power-after-fail.md
[DTS]: ../../unified-test-documentation/dasharo-compatibility/326-dasharo-tools-suite.md
[RTD]: ../../dasharo-menu-docs/overview.md#f9-reset-to-defaults
[NET]: ../../unified-test-documentation/dasharo-stability/01-net-controller-after-coldboot-warmboot-reboot-suspend.md
[DCU]: ../../unified-test-documentation/dasharo-compatibility/362-dcu.md
[ESP]: ../../unified-test-documentation/dasharo-compatibility/361-esp-scanning.md
[NBT]: ../../unified-test-documentation/dasharo-compatibility/315b-netboot-utilities.md
[UDT]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
[UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md
<!--[SET]:-->
[BUB]: ../../unified-test-documentation/dasharo-performance/407-ubuntu-booting-performance-test.md
[CPU]: ../../unified-test-documentation/dasharo-compatibility/31T-cpu-status.md
[BMM]: ../../dasharo-menu-docs/boot-maintenance-mgr.md#boot-maintenance-manager

<!--
    Test cases copied from spreadsheet using a script, may be a good reference
    but need refactoring, adding links and manual check
-->
<!--
    ## Module: Dasharo Security

    | No. | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:---:|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.  | [TPM Support][TPM]                    | TPM           | TPM001.002,TPM002.001,TPM002.002,TPM003.001,TPM003.002,TPM003.004, |
    | 2.  | [Verified Boot Integration][VBO]      | VBO           | All                                  |
    | 3.  | [BIOS lock support][BLS]              | BLS           | BLS001.001,BLS002.001,               |
    | 4.  | [Measured boot integration][MBO] | MBO | MBO001.001, |
    | 5.  | [UEFI Secure Boot integration][SBO] | SBO | SBO001.001,SBO002.001,SBO003.001,SBO004.001,SBO005.001,SBO006.001,SBO007.001,SBO008.001, |
    | 6.  | [UEFI Setup password][PSW] | PSW | PSW001.001,PSW002.001,PSW003.001,PSW004.001,PSW005.001,PSW006.001,PSW007.001,PSW008.001, |
    | 7.  | [Early Boot DMA Protection][EDP] | EDP | EDP001.001,EDP002.001, |
    | 8.  | [USB stack enable/disable][USS] | USS | USS001.001,USS002.001,USS003.001,USS004.001, |
    | 9.  | [Network stack enable/disable][NBA] | NBA | NBA001.001,NBA002.001, |
    | 10. | [SMM BIOS write protection][SMM] | SMM | SMM001.001,SMM002.001, |
    | 11. | [TPM2 Commands][TPMCMD] | TPMCMD | TPMCMD001.001,TPMCMD002.001,TPMCMD003.001,TPMCMD003.002,TPMCMD004.001,TPMCMD005.001,TPMCMD006.001,TPMCMD007.001,TPMCMD007.002,TPMCMD008.001,TPMCMD009.001,TPMCMD010.001,TPMCMD011.001, |

    ## Module: Dasharo Stability

    | No. | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:---:|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1. | [TPM Support][TPD] | TPD | TPD003.001,TPD004.001,TPD003.001,TPD004.001, |
    | 2. | [USB support][] |  | SUD0001.001,SUD0002.001,SUD0003.001,SUD0004.001, |

    ## Module: Dasharo Performance

    | No. | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:---:|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1. | [Serial Boot Measure][CBMEM] | CBMEM | CBMEM001.001,CBMEM002.001,CBMEM003.001, |
    | 2. | [CPU][CPT] | CPT | CPT001.001,CPT002.001, |
    | 3. | [CPU][CPF] | CPF | CPF001.001,CPF002.001,CPF004.001, |
    | 4. | [Platform stability][STB] | STB | STB001.001,STB001.002,STB002.001, |
    | 5. | [Ubuntu booting performance test][BUB] | BUB | BUB001.001,BUB002.001,BUB003.001, |
-->

<!-- turbot test matrix, reference -->
<!--
    ## Module: Dasharo security

    | No. | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.  | [Secure Boot support][SBO]            | SBO           | All                                  |
    | 2.  | [BIOS lock support][BLS]              | BLS           | All                                  |
    | 3.  | [SMM BIOS write protection][SMM]      | SMM           | All                                  |
    | 4.  | [UEFI Setup password][PSW]            | PSW           | All                                  |
    | 5.  | [Network stack enable/disable][NBA]   | NBA           | All                                  |
    | 6.  | [USB stack enable/disable][USS]       | USS           | All                                  |

    ## Module: Dasharo performance

    | No. | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.  | [coreboot bring up time measurement][CBMEM] | CBMEM         | All                            |
    | 2.  | [CPU temperature measure][CPT]        | CPT           | All                                  |
    | 3.  | [CPU frequency measure][CPF]          | CPF           | Without CPU003.XXX and CPU005.XXX    |
    | 4.  | [Platform stability][STB]             | STB           | All                                  |

    [CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
    [CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
    [CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
    [STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md
    [BUB]: ../../unified-test-documentation/dasharo-performance/407-ubuntu-booting-performance-test.md
    [BDE]: ../../unified-test-documentation/dasharo-performance/408-debian-booting-performance-test.md
-->
