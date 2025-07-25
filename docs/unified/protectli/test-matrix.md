# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

=== "FW6"

    ## Module: Dasharo compatibility

    | No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
    | 2.   | [Display ports and LCD support][DSP]              | DSP           | DSP002.201, DSP002.003               |
    | 3.   | [USB HID and MSC Support][USB]                    | USB           | USB001.001, USB001.002, USB002.001, USB002.002 |
    | 4.   | [SMBIOS][DMI]                                     | DMI           | DMI002.201, DMI003.201, DMI004.201, DMI005.001, DMI006.001 |
    | 5.   | [Custom boot logo][CLG]                           | CLG           | DMI002.201, DMI003.201, DMI004.201, DMI005.001, DMI006.001 |
    | 6.   | [M.2 WiFi/Bluetooth][WLE]                         | WLE           | WLE001.001, WLE002.001, WLE003.001   |
    | 7.   | [Network boot][PXE]                               | PXE           | PXE007.001                           |
    | 8.   | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
    | 9.   | [Custom boot menu key][CBK]                       | CBK           | All                                  |
    | 10.  | [FreeBSD support][BSD]                            | BSD           | All                                  |
    | 11.  | [miniPCIe LTE/WiFi/Bluetooth][MWL]                | MWL           | MWL004.201                           |
    | 12.  | [Custom network boot entries][CNB]                | CNB           | CNB001.201                           |

    [HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
    [DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
    [USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
    [DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
    [CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
    [MWL]: ../../unified-test-documentation/dasharo-compatibility/31K-minipcie-verification.md
    [WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
    [PXE]: ../../unified-test-documentation/dasharo-compatibility/315-network-boot.md
    [LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
    [CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
    [BSD]: ../../unified-test-documentation/dasharo-compatibility/307-freebsd-support.md
    [CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md

    ## Module: Dasharo performance

    | No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [CPU temperature][CPT]                            | CPT           | All                                  |

    [CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md

=== "V1000-series"

    ## Module: Dasharo compatibility

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:----:|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [UEFI compatible interface][EFI]      | EFI           | All                                  |
    | 2.   | [Display ports][DSP]                  | DSP           | DSP002.201, DSP002.301, DSP002.003   |
    | 3.   | [Network boot utilities][NBT]         | NBT           | All                                  |
    | 4.   | [NVMe support][NVM]                   | NVM           | All                                  |
    | 5.   | [Custom logo][CLG]                    | CLG           | All                                  |
    | 6.   | [Custom Boot Keys][CBK]               | CBK           | All                                  |
    | 7.   | [USB HID and MSC Support][USB]        | USB           | USB001.xxx and USB002.xxx            |
    | 8.   | [Debian Stable and Ubuntu LTS support][LBT]  | LBT    | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
    | 9.   | [miniPCIe LTE/WiFi/Bluetooth][MWL]    | MWL           | MWL004.201                           |
    | 10.  | [M.2 WiFi/Bluetooth][WLE]             | WLE           | All                                  |
    | 11.  | [eMMC support][MMC]                   | MMC           | All                                  |
    | 12.  | [SMBIOS][DMI]                         | DMI           | DMI002.201, DMI003.201, DMI004.201, DMI005.001, DMI006.001 |
    | 13.  | [Custom network boot entries][CNB]    | CNB           | CNB001.201                           |
    | 14.  | [Audio subsystem][AUD]                | AUD           | AUD007.xxx, AUD008.xxx               |
    | 15.  | [UEFI Shell][USH]                     | USH           | All                                  |
    | 16.  | [USB detection][UDT]                  | UDT           | All                                  |
    | 17.  | [USB booting][UBT]                    | UBT           | All                                  |
    | 18.  | [Windows booting][WBT]                | WBT           | WBT001.001                           |

    [EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
    [DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
    [NBT]: ../../unified-test-documentation/dasharo-compatibility/315b-netboot-utilities.md
    [NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
    [CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
    [CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
    [USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
    [BSD]: ../../unified-test-documentation/dasharo-compatibility/307-freebsd-support.md
    [LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
    [UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
    [WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
    [MWL]: ../../unified-test-documentation/dasharo-compatibility/31K-minipcie-verification.md
    [MMC]: ../../unified-test-documentation/dasharo-compatibility/31M-emmc-support.md
    [DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
    [CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md
    [MSS]: ../../unified-test-documentation/dasharo-compatibility/31I-nvme-switching.md
    [WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
    [AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
    [USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
    [UDT]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
    [UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md
    [PFS]: ../../unified-test-documentation/dasharo-compatibility/341-pfSense-support.md
    [OPN]: ../../unified-test-documentation/dasharo-compatibility/342-OPNsense-support.md
    [PVE]: ../../unified-test-documentation/dasharo-compatibility/348-proxmox-support.md
    [USS]: ../../unified-test-documentation/dasharo-compatibility/349-ubuntu-server-support.md

    ## Module: Dasharo security

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [TPM Support][TPM]                    | TPM           | TPM001.201, TPM001.301, TPM002.201, TPM002.301, TPM003.201, TPM003.301 |
    | 2.   | [Secure Boot support][SBO]            | SBO           | All                                  |

    [TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
    [SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md

    ## Module: Dasharo performance

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [coreboot bring up time measurement][CBMEM] | CBMEM         | All                            |
    | 2.   | [CPU temperature measure][CPT]        | CPT           | All                                  |
    | 3.   | [CPU frequency measure][CPF]          | CPF           | Without CPU003.XXX and CPU005.XXX    |
    | 4.   | [Platform stability][STB]             | STB           | All                                  |

    [CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
    [CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
    [CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
    [STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md
    [BUB]: ../../unified-test-documentation/dasharo-performance/407-ubuntu-booting-performance-test.md
    [BDE]: ../../unified-test-documentation/dasharo-performance/408-debian-booting-performance-test.md
    [BFB]: ../../unified-test-documentation/dasharo-performance/409-freebsd-booting-performance-test.md
    [BPM]: ../../unified-test-documentation/dasharo-performance/410-proxmox-booting-performance-test.md
    [BUS]: ../../unified-test-documentation/dasharo-performance/411-ubuntu-server-booting-performance-test.md
    [BOS]: ../../unified-test-documentation/dasharo-performance/412-opnsense-serial-booting-performance-test.md
    [BOV]: ../../unified-test-documentation/dasharo-performance/413-opnsense-vga-booting-performance-test.md
    [BPS]: ../../unified-test-documentation/dasharo-performance/414-pfsense-serial-booting-performance-test.md
    [BPV]: ../../unified-test-documentation/dasharo-performance/415-pfsense-vga-booting-performance-test.md

=== "VP4630/VP4650/VP4670"

    ## Module: Dasharo compatibility

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:----:|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [Memory HCL][HCL]                     | HCL           | All                                  |
    | 2.   | [UEFI compatible interface][EFI]      | EFI           | All                                  |
    | 3.   | [Display ports][DSP]                  | DSP           | DSP002.201, DSP002.301, DSP002.003, DSP003.201, DSP003.301, DSP003.003 |
    | 4.   | [Network boot utilities][NBT]         | NBT           | All                                  |
    | 5.   | [NVMe support][NVM]                   | NVM           | All                                  |
    | 6.   | [Custom logo][CLG]                    | CLG           | All                                  |
    | 7.   | [Custom boot menu key][CBK]           | CBK           | All                                  |
    | 8.   | [USB HID and MSC Support][USB]        | USB           | USB001.XXX and USB002.XXX            |
    | 9.   | [FreeBSD support][BSD]                | BSD           | All                                  |
    | 10.  | [Debian Stable and Ubuntu LTS support][LBT]  | LBT         | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
    | 11.  | [USB-C support][UTC]                  | UTC           | UTC004.001, UTC004.002               |
    | 12.  | [M.2 WiFi/Bluetooth][WLE]             | WLE           | ALL                                  |
    | 13.  | [eMMC support][MMC]                   | MMC           | MMC001.001                           |
    | 14.  | [SMBIOS][DMI]                         | DMI           | DMI002.201, DMI003.201, DMI004.201, DMI005.001, DMI006.001 |
    | 15.  | [Custom network boot entries][CNB]    | CNB           | CNB001.201                           |
    | 16.  | [M.2 automatic SATA/NVMe switching support][MSS]  | MSS           | MSS001.001                           |
    | 17.  | [Windows booting][WBT]                | WBT           | WBT001.001                           |
    | 18.  | [Audio subsystem][AUD]                | AUD           | AUD001.201, AUD001.301, AUD002.201, AUD002.301, AUD003.201, AUD003.301, AUD004.201, AUD004.301, AUD005.201, AUD005.301, AUD006.201, AUD006.301 |
    | 19.  | [UEFI Shell][USH]                     | USH           | All                                  |
    | 20.  | [USB detection][UDT]                  | UDT           | All                                  |
    | 21.  | [USB booting][UBT]                    | UBT           | All                                  |
    | 22.  | [pfSense support][PFS]                | PFS           | All                                  |
    | 23.  | [OPNsense support][OPN]               | OPN           | All                                  |
    | 24.  | [Proxmox support][PVE]                | PVE           | All                                  |
    | 25.  | [Ubuntu Server support][USS]          | USS           | All                                  |

    [HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
    [EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
    [DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
    [NBT]: ../../unified-test-documentation/dasharo-compatibility/315b-netboot-utilities.md
    [NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
    [CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
    [CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
    [USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
    [BSD]: ../../unified-test-documentation/dasharo-compatibility/307-freebsd-support.md
    [LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
    [UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
    [WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
    [MWL]: ../../unified-test-documentation/dasharo-compatibility/31K-minipcie-verification.md
    [MMC]: ../../unified-test-documentation/dasharo-compatibility/31M-emmc-support.md
    [DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
    [CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md
    [MSS]: ../../unified-test-documentation/dasharo-compatibility/31I-nvme-switching.md
    [WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
    [AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
    [USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
    [UDT]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
    [UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md
    [PFS]: ../../unified-test-documentation/dasharo-compatibility/341-pfSense-support.md
    [OPN]: ../../unified-test-documentation/dasharo-compatibility/342-OPNsense-support.md
    [PVE]: ../../unified-test-documentation/dasharo-compatibility/348-proxmox-support.md
    [USS]: ../../unified-test-documentation/dasharo-compatibility/349-ubuntu-server-support.md

    ## Module: Dasharo security

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [TPM Support][TPM]            | TPM           | Without TPM001.001,TPM002.001 and TPM003.001 |
    | 2.   | [Verified Boot support][VBO]          | VBO           | Without VBO006.001 and VBO007.001    |
    | 3.   | [Measured Boot support][MBO]          | MBO           | All                                  |
    | 4.   | [Secure Boot support][SBO]            | SBO           | All                                  |
    | 5.   | [ME disable/neuter support][MNE]      | MNE           | MNE006.201                           |
    | 6.   | [BIOS lock support][BLS]              | BLS           | All                                  |
    | 7.   | [USB stack enable/disable][USS]       | USS           | All                                  |
    | 8.   | [SMM BIOS write protection][SMM]      | SMM           | All                                  |

    > Note: in Dasharo compatible with Protectli VP46xx ME is soft-disabled by
    > default - no additional option for ME disabling is available in the Setup
    > Menu.

    [TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
    [VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
    [MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
    [SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
    [MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
    [BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md
    [USS]: ../../unified-test-documentation/dasharo-security/20S-usb-stack.md
    [SMM]: ../../unified-test-documentation/dasharo-security/20O-SMM-bios-write-protection.md

    ## Module: Dasharo performance

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [coreboot bring up time measurement][CBMEM] | CBMEM         | All                            |
    | 2.   | [CPU temperature measure][CPT]        | CPT           | All                                  |
    | 3.   | [CPU frequency measure][CPF]          | CPF           | Without CPU003.XXX and CPU005.XXX    |
    | 4.   | [Platform stability][STB]             | STB           | All                                  |
    | 5.   | [Ubuntu booting performance test][BUB] | BUB           | All                                 |
    | 6.   | [Debian booting performance test][BDE] | BDE           | All                                 |
    | 7.   | [FreeBSD booting performance test][BFB] | BFB           | All                                |
    | 8.   | [Proxmox booting performance test][BPM] | BPM           | All                                |
    | 9.   | [Ubuntu Server booting performance test][BUS] | BUS           | All                          |
    | 10.  | [OPNsense (serial output) booting performance test][BOS] | BOS           | All               |
    | 11.  | [OPNsense (VGA output) booting performance test][BOV]    | BOV           | All               |
    | 12.  | [pfSense (serial output) booting performance test][BPS]  | BPS           | All               |
    | 13.  | [pfSense (VGA output) booting performance test][BPV]     | BPV           | All               |

    [CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
    [CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
    [CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
    [STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md
    [BUB]: ../../unified-test-documentation/dasharo-performance/407-ubuntu-booting-performance-test.md
    [BDE]: ../../unified-test-documentation/dasharo-performance/408-debian-booting-performance-test.md
    [BFB]: ../../unified-test-documentation/dasharo-performance/409-freebsd-booting-performance-test.md
    [BPM]: ../../unified-test-documentation/dasharo-performance/410-proxmox-booting-performance-test.md
    [BUS]: ../../unified-test-documentation/dasharo-performance/411-ubuntu-server-booting-performance-test.md
    [BOS]: ../../unified-test-documentation/dasharo-performance/412-opnsense-serial-booting-performance-test.md
    [BOV]: ../../unified-test-documentation/dasharo-performance/413-opnsense-vga-booting-performance-test.md
    [BPS]: ../../unified-test-documentation/dasharo-performance/414-pfsense-serial-booting-performance-test.md
    [BPV]: ../../unified-test-documentation/dasharo-performance/415-pfsense-vga-booting-performance-test.md

=== "VP6630/VP6650/VP6670"

    ## Module: Dasharo compatibility

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:----:|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [Memory HCL][HCL]                     | HCL           | All                                  |
    | 2.   | [UEFI compatible interface][EFI]      | EFI           | All                                  |
    | 3.   | [Display ports][DSP]                  | DSP           | DSP002.201, DSP002.301, DSP002.003, DSP003.201, DSP003.301, DSP003.003 |
    | 4.   | [Network boot utilities][NBT]         | NBT           | All                                  |
    | 5.   | [NVMe support][NVM]                   | NVM           | All                                  |
    | 6.   | [Custom logo][CLG]                    | CLG           | All                                  |
    | 7.   | [Custom boot menu key][CBK]           | CBK           | All                                  |
    | 8.   | [USB HID and MSC Support][USB]        | USB           | USB001.XXX and USB002.XXX            |
    | 9.   | [FreeBSD support][BSD]                | BSD           | All                                  |
    | 10.  | [Debian Stable and Ubuntu LTS support][LBT]  | LBT         | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
    | 11.  | [USB-C support][UTC]                  | UTC           | UTC004.001, UTC004.002               |
    | 12.  | [M.2 WiFi/Bluetooth][WLE]             | WLE           | ALL                                  |
    | 14.  | [SMBIOS][DMI]                         | DMI           | DMI002.201, DMI003.201, DMI004.201, DMI005.001, DMI006.001 |
    | 15.  | [Custom network boot entries][CNB]    | CNB           | CNB001.201                           |
    | 17.  | [Windows booting][WBT]                | WBT           | WBT001.001                           |
    | 18.  | [Audio subsystem][AUD]                | AUD           | AUD001.201, AUD001.301, AUD002.201, AUD002.301, AUD003.201, AUD003.301, AUD004.201, AUD004.301, AUD005.201, AUD005.301, AUD006.201, AUD006.301 |
    | 19.  | [UEFI Shell][USH]                     | USH           | All                                  |
    | 20.  | [USB detection][UDT]                  | UDT           | All                                  |
    | 21.  | [USB booting][UBT]                    | UBT           | All                                  |
    | 22.  | [pfSense support][PFS]                | PFS           | All                                  |
    | 23.  | [OPNsense support][OPN]               | OPN           | All                                  |
    | 24.  | [Proxmox support][PVE]                | PVE           | All                                  |
    | 25.  | [Ubuntu Server support][USS]          | USS           | All                                  |

    [HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
    [EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
    [DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
    [NBT]: ../../unified-test-documentation/dasharo-compatibility/315b-netboot-utilities.md
    [NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
    [CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
    [CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
    [USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
    [BSD]: ../../unified-test-documentation/dasharo-compatibility/307-freebsd-support.md
    [LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
    [UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
    [WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
    [MWL]: ../../unified-test-documentation/dasharo-compatibility/31K-minipcie-verification.md
    [DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
    [CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md
    [WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
    [AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
    [USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
    [UDT]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
    [UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md
    [PFS]: ../../unified-test-documentation/dasharo-compatibility/341-pfSense-support.md
    [OPN]: ../../unified-test-documentation/dasharo-compatibility/342-OPNsense-support.md
    [PVE]: ../../unified-test-documentation/dasharo-compatibility/348-proxmox-support.md
    [USS]: ../../unified-test-documentation/dasharo-compatibility/349-ubuntu-server-support.md

    ## Module: Dasharo security

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [TPM Support][TPM]            | TPM           | Without TPM001.001,TPM002.001 and TPM003.001 |
    | 2.   | [Verified Boot support][VBO]          | VBO           | Without VBO006.001 and VBO007.001    |
    | 3.   | [Measured Boot support][MBO]          | MBO           | All                                  |
    | 4.   | [Secure Boot support][SBO]            | SBO           | All                                  |
    | 5.   | [ME disable/neuter support][MNE]      | MNE           | MNE006.201                           |
    | 6.   | [BIOS lock support][BLS]              | BLS           | All                                  |
    | 7.   | [USB stack enable/disable][USS]       | USS           | All                                  |
    | 8.   | [SMM BIOS write protection][SMM]      | SMM           | All                                  |

    > Note: in Dasharo for Protectli VP66XX ME is HAP disabled by default - no
    > additional option for ME disabling is available in the Setup Menu.

    [TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
    [VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
    [MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
    [SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
    [MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
    [BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md
    [USS]: ../../unified-test-documentation/dasharo-security/20S-usb-stack.md
    [SMM]: ../../unified-test-documentation/dasharo-security/20O-SMM-bios-write-protection.md

    ## Module: Dasharo performance

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [coreboot bring up time measurement][CBMEM] | CBMEM         | All                            |
    | 2.   | [CPU temperature measure][CPT]        | CPT           | All                                  |
    | 3.   | [CPU frequency measure][CPF]          | CPF           | Without CPU003.XXX and CPU005.XXX    |
    | 4.   | [Platform stability][STB]             | STB           | All                                  |
    | 5.   | [Ubuntu booting performance test][BUB] | BUB           | All                                 |
    | 6.   | [Debian booting performance test][BDE] | BDE           | All                                 |
    | 7.   | [FreeBSD booting performance test][BFB] | BFB           | All                                |
    | 8.   | [Proxmox booting performance test][BPM] | BPM           | All                                |
    | 9.   | [Ubuntu Server booting performance test][BUS] | BUS           | All                          |
    | 10.  | [OPNsense (serial output) booting performance test][BOS] | BOS           | All               |
    | 11.  | [OPNsense (VGA output) booting performance test][BOV]    | BOV           | All               |
    | 12.  | [pfSense (serial output) booting performance test][BPS]  | BPS           | All               |
    | 13.  | [pfSense (VGA output) booting performance test][BPV]     | BPV           | All               |

    [CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
    [CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
    [CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
    [STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md
    [BUB]: ../../unified-test-documentation/dasharo-performance/407-ubuntu-booting-performance-test.md
    [BDE]: ../../unified-test-documentation/dasharo-performance/408-debian-booting-performance-test.md
    [BFB]: ../../unified-test-documentation/dasharo-performance/409-freebsd-booting-performance-test.md
    [BPM]: ../../unified-test-documentation/dasharo-performance/410-proxmox-booting-performance-test.md
    [BUS]: ../../unified-test-documentation/dasharo-performance/411-ubuntu-server-booting-performance-test.md
    [BOS]: ../../unified-test-documentation/dasharo-performance/412-opnsense-serial-booting-performance-test.md
    [BOV]: ../../unified-test-documentation/dasharo-performance/413-opnsense-vga-booting-performance-test.md
    [BPS]: ../../unified-test-documentation/dasharo-performance/414-pfsense-serial-booting-performance-test.md
    [BPV]: ../../unified-test-documentation/dasharo-performance/415-pfsense-vga-booting-performance-test.md

=== "VP2410"

    ## Module: Dasharo compatibility

    | No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
    |:----:|:--------------------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
    | 2.   | [UEFI compatible interface][EFI]                  | EFI           | All                                  |
    | 3.   | [Display ports][DSP]                              | DSP           | DSP002.201, DSP002.301, DSP002.003, DSP003.201, DSP003.301, DSP003.003 |
    | 4.   | [Network boot utilities][NBT]                     | NBT           | All                                  |
    | 5.   | [NVMe support][NVM]                               | NVM           | All                                  |
    | 6.   | [Custom logo][CLG]                                | CLG           | All                                  |
    | 7.   | [Custom boot menu key][CBK]                       | CBK           | All                                  |
    | 8.   | [USB HID and MSC Support][USB]                    | USB           | All                                  |
    | 9.   | [FreeBSD support][BSD]                            | BSD           | All                                  |
    | 10.  | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
    | 11.  | [USB-C support][UTC]                              | UTC           | UTC004.001, UTC004.001               |
    | 12.  | [M.2 WiFi/Bluetooth][WLE]                         | WLE           | ALL                                  |
    | 13.  | [eMMC support][MMC]                               | MMC           | MMC001.001                           |
    | 14.  | [SMBIOS][DMI]                                     | DMI           | DMI002.201, DMI003.201, DMI004.201, DMI005.001, DMI006.001 |
    | 15.  | [Custom network boot entries][CNB]                | CNB           | CNB001.201                           |
    | 16.  | [M.2 automatic SATA/NVMe switching support][MSS]  | MSS           | MSS001.001                           |
    | 17.  | [Windows booting][WBT]                            | WBT           | WBT001.001                           |
    | 18.  | [Audio subsystem][AUD]                            | AUD           | AUD001.201, AUD001.301, AUD002.201, AUD002.301, AUD003.201, AUD003.301, AUD004.201, AUD004.301, AUD005.201, AUD005.301, AUD006.201, AUD006.301 |
    | 19.  | [UEFI Shell][USH]                                 | USH           | All                                  |
    | 20.  | [USB detection][UDT]                              | UDT           | All                                  |
    | 21.  | [USB booting][UBT]                                | UBT           | All                                  |

    [HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
    [EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
    [DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
    [NBT]: ../../unified-test-documentation/dasharo-compatibility/315b-netboot-utilities.md
    [NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
    [CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
    [CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
    [USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
    [BSD]: ../../unified-test-documentation/dasharo-compatibility/307-freebsd-support.md
    [LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
    [UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
    [WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
    [MWL]: ../../unified-test-documentation/dasharo-compatibility/31K-minipcie-verification.md
    [MMC]: ../../unified-test-documentation/dasharo-compatibility/31M-emmc-support.md
    [DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
    [CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md
    [MSS]: ../../unified-test-documentation/dasharo-compatibility/31I-nvme-switching.md
    [WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
    [AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
    [USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
    [UDT]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
    [UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md

    ## Module: Dasharo security

    | No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [TPM Support][TPM]                                | TPM           | Without TPM001.001 and TPM002.001    |
    | 2.   | [Verified Boot support][VBO]                      | VBO           | VBO006.002, VBO007.002, VBO008.001   |
    | 3.   | [Measured Boot support][MBO]                      | MBO           | All                                  |
    | 4.   | [Secure Boot support][SBO]                        | SBO           | All                                  |
    | 5.   | [BIOS lock support][BLS]                          | BLS           | All                                  |

    [TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
    [VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
    [MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
    [SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
    [MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
    [BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md

    ## Module: Dasharo performance

    | No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [coreboot bring up time measurement][CBMEM]       | CBMEM         | All                                  |
    | 2.   | [CPU temperature measure][CPT]                    | CPT           | All                                  |
    | 3.   | [CPU frequency measure][CPF]                      | CPF           | All                                  |
    | 4.   | [Platform stability][STB]                         | STB           | All                                  |

    [CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
    [CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
    [CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
    [STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md

=== "VP2420"

    ## Module: Dasharo compatibility

    | No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
    |:----:|:--------------------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [Memory HCL][HCL]                                 | HCL           | All                                  |
    | 2.   | [UEFI compatible interface][EFI]                  | EFI           | All                                  |
    | 3.   | [Display ports][DSP]                              | DSP           | DSP002.201, DSP002.301, DSP002.003, DSP003.201, DSP003.301, DSP003.003 |
    | 4.   | [Network boot utilities][NBT]                     | NBT           | All                                  |
    | 6.   | [Custom logo][CLG]                                | CLG           | All                                  |
    | 7.   | [Custom boot menu key][CBK]                       | CBK           | All                                  |
    | 8.   | [USB HID and MSC Support][USB]                    | USB           | USB001.XXX and USB002.XXX            |
    | 9.   | [FreeBSD support][BSD]                            | BSD           | All                                  |
    | 10.  | [Debian Stable and Ubuntu LTS support][LBT]       | LBT           | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
    | 11.  | [USB-C support][UTC]                              | UTC           | UTC004.001, UTC004.002               |
    | 12.  | [M.2 WiFi/Bluetooth][WLE]                         | WLE           | ALL                                  |
    | 13.  | [eMMC support][MMC]                               | MMC           | MMC001.001                           |
    | 14.  | [SMBIOS][DMI]                                     | DMI           | DMI002.201, DMI003.201, DMI004.201, DMI005.001, DMI006.001 |
    | 15.  | [Custom network boot entries][CNB]                | CNB           | CNB001.201                           |
    | 17.  | [Windows booting][WBT]                            | WBT           | WBT001.001                           |
    | 18.  | [UEFI Shell][USH]                                 | USH           | All                                  |
    | 19.  | [USB detection][UDT]                              | UDT           | All                                  |
    | 20.  | [USB booting][UBT]                                | UBT           | All                                  |
    | 21.  | [pfSense support][PFS]                            | PFS           | All                                  |
    | 22.  | [OPNsense support][OPN]                           | OPN           | All                                  |
    | 23.  | [Proxmox support][PVE]                            | PVE           | All                                  |
    | 24.  | [Ubuntu Server support][USS]                      | USS           | All                                  |

    [HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
    [EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
    [DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
    [NBT]: ../../unified-test-documentation/dasharo-compatibility/315b-netboot-utilities.md
    [NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
    [CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
    [CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
    [USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
    [BSD]: ../../unified-test-documentation/dasharo-compatibility/307-freebsd-support.md
    [LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
    [UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
    [WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
    [MWL]: ../../unified-test-documentation/dasharo-compatibility/31K-minipcie-verification.md
    [MMC]: ../../unified-test-documentation/dasharo-compatibility/31M-emmc-support.md
    [DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
    [CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md
    [MSS]: ../../unified-test-documentation/dasharo-compatibility/31I-nvme-switching.md
    [WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
    [AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
    [USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
    [UDT]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
    [UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md
    [PFS]: ../../unified-test-documentation/dasharo-compatibility/341-pfSense-support.md
    [OPN]: ../../unified-test-documentation/dasharo-compatibility/342-OPNsense-support.md
    [PVE]: ../../unified-test-documentation/dasharo-compatibility/348-proxmox-support.md
    [USS]: ../../unified-test-documentation/dasharo-compatibility/349-ubuntu-server-support.md

    ## Module: Dasharo security

    | No.  | Supported test suite                              | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [TPM Support][TPM]                                | TPM           | TPM001.201 and TPM001.301            |
    | 2.   | [Verified Boot support][VBO]                      | VBO           | Without VBO006.001 and VBO007.001    |
    | 3.   | [Measured Boot support][MBO]                      | MBO           | All                                  |
    | 4.   | [Secure Boot support][SBO]                        | SBO           | All                                  |
    | 5.   | [BIOS lock support][BLS]                          | BLS           | All                                  |
    | 6.   | [USB stack enable/disable][USS]                   | USS           | All                                  |
    | 7.   | [SMM BIOS write protection][SMM]                  | SMM           | All                                  |

    [TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
    [VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
    [MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
    [SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
    [BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md
    [USS]: ../../unified-test-documentation/dasharo-security/20S-usb-stack.md
    [SMM]: ../../unified-test-documentation/dasharo-security/20O-SMM-bios-write-protection.md

    ## Module: Dasharo performance

    | No.  | Supported test suite                                     | Test suite ID | Supported test cases                 |
    |:-----|:---------------------------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [coreboot bring up time measurement][CBMEM]              | CBMEM         | All                                  |
    | 2.   | [CPU temperature measure][CPT]                           | CPT           | All                                  |
    | 3.   | [CPU frequency measure][CPF]                             | CPF           | Without CPU003.XXX and CPU005.XXX    |
    | 4.   | [Platform stability][STB]                                | STB           | All                                  |
    | 5.   | [Ubuntu booting performance test][BUB]                   | BUB           | All                                  |
    | 6.   | [Debian booting performance test][BDE]                   | BDE           | All                                  |
    | 7.   | [FreeBSD booting performance test][BFB]                  | BFB           | All                                  |
    | 8.   | [Proxmox booting performance test][BPM]                  | BPM           | All                                  |
    | 9.   | [Ubuntu Server booting performance test][BUS]            | BUS           | All                                  |
    | 10.  | [OPNsense (serial output) booting performance test][BOS] | BOS           | All                                  |
    | 11.  | [OPNsense (VGA output) booting performance test][BOV]    | BOV           | All                                  |
    | 12.  | [pfSense (serial output) booting performance test][BPS]  | BPS           | All                                  |
    | 13.  | [pfSense (VGA output) booting performance test][BPV]     | BPV           | All                                  |

    [CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
    [CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
    [CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
    [STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md
    [BUB]: ../../unified-test-documentation/dasharo-performance/407-ubuntu-booting-performance-test.md
    [BDE]: ../../unified-test-documentation/dasharo-performance/408-debian-booting-performance-test.md
    [BFB]: ../../unified-test-documentation/dasharo-performance/409-freebsd-booting-performance-test.md
    [BPM]: ../../unified-test-documentation/dasharo-performance/410-proxmox-booting-performance-test.md
    [BUS]: ../../unified-test-documentation/dasharo-performance/411-ubuntu-server-booting-performance-test.md
    [BOS]: ../../unified-test-documentation/dasharo-performance/412-opnsense-serial-booting-performance-test.md
    [BOV]: ../../unified-test-documentation/dasharo-performance/413-opnsense-vga-booting-performance-test.md
    [BPS]: ../../unified-test-documentation/dasharo-performance/414-pfsense-serial-booting-performance-test.md
    [BPV]: ../../unified-test-documentation/dasharo-performance/415-pfsense-vga-booting-performance-test.md

=== "VP2430"

    ## Module: Dasharo compatibility

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:----:|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [Memory HCL][HCL]                     | HCL           | All                                  |
    | 2.   | [UEFI compatible interface][EFI]      | EFI           | All                                  |
    | 3.   | [Display ports][DSP]                  | DSP           | DSP002.001, DSP002.002, DSP002.003, DSP003.001, DSP003.002, DSP003.003 |
    | 4.   | [Network boot utilities][NBT]         | NBT           | All                                  |
    | 5.   | [NVMe support][NVM]                   | NVM           | All                                  |
    | 6.   | [Custom logo][CLG]                    | CLG           | All                                  |
    | 7.   | [Custom boot menu key][CBK]           | CBK           | All                                  |
    | 8.   | [USB HID and MSC Support][USB]        | USB           | USB001.XXX and USB002.XXX            |
    | 9.   | [FreeBSD support][BSD]                | BSD           | All                                  |
    | 10.  | [Debian Stable and Ubuntu LTS support][LBT]  | LBT         | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
    | 11.  | [USB-C support][UTC]                  | UTC           | UTC004.001, UTC004.002               |
    | 12.  | [M.2 WiFi/Bluetooth][WLE]             | WLE           | ALL                                  |
    | 14.  | [SMBIOS][DMI]                         | DMI           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, DMI006.001 |
    | 15.  | [Custom network boot entries][CNB]    | CNB           | CNB001.002                           |
    | 17.  | [Windows booting][WBT]                | WBT           | WBT001.001                           |
    | 18.  | [Audio subsystem][AUD]                | AUD           | AUD001.001, AUD001.002, AUD002.001, AUD002.002, AUD003.001, AUD003.002, AUD004.001, AUD004.002, AUD005.001, AUD005.002, AUD006.001, AUD006.002 |
    | 20.  | [USB detection][UDT]                  | UDT           | All                                  |
    | 21.  | [USB booting][UBT]                    | UBT           | All                                  |
    | 22.  | [pfSense support][PFS]                | PFS           | All                                  |
    | 23.  | [OPNsense support][OPN]               | OPN           | All                                  |
    | 24.  | [Proxmox support][PVE]                | PVE           | All                                  |
    | 25.  | [Ubuntu Server support][USS]          | USS           | All                                  |
    | 26. | [Auto boot time-out][BMM]             | BMM           | All                                  |
    | 27. | [CPU status][CPU]                     | CPU           | CPU001.001, CPU002.001, CPU003.001, CPU004.001|
    | 28. | [ESP scanning][ESP]                   | ESP           | All                                  |
    | 29. | [Reset to defaults][RTD]              | RTD           | RTD001.001, RTD002.001, RTD003.001, RTD004.001, RTD006.001 |
    | 30. | [Ethernet interface][NET]             | NET           | All                                  |
    | 31. | [Dasharo Configuration Utility][NET]  | DCU           | DCU001.001, DCU002.001, DCU003.001   |
    | 33. | [Sleep mode][SUSP]                    | SUSP          | SUSP001.001, SUSP002.001, SUSP003.001, SUSP005.001|

    [HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
    [EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
    [DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
    [NBT]: ../../unified-test-documentation/dasharo-compatibility/315b-netboot-utilities.md
    [NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
    [CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
    [CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
    [USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
    [BSD]: ../../unified-test-documentation/dasharo-compatibility/307-freebsd-support.md
    [LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
    [UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
    [WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
    [MWL]: ../../unified-test-documentation/dasharo-compatibility/31K-minipcie-verification.md
    [DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
    [CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md
    [WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
    [AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
    [USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
    [UDT]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
    [UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md
    [PFS]: ../../unified-test-documentation/dasharo-compatibility/341-pfSense-support.md
    [OPN]: ../../unified-test-documentation/dasharo-compatibility/342-OPNsense-support.md
    [PVE]: ../../unified-test-documentation/dasharo-compatibility/348-proxmox-support.md
    [USS]: ../../unified-test-documentation/dasharo-compatibility/349-ubuntu-server-support.md
    [CPU]: ../../unified-test-documentation/dasharo-compatibility/31T-cpu-status.md
    [BMM]: ../../dasharo-menu-docs/boot-maintenance-mgr.md#boot-maintenance-manager
    [ESP]: ../../unified-test-documentation/dasharo-compatibility/361-esp-scanning.md
    [RTD]: ../../dasharo-menu-docs/overview.md#f9-reset-to-defaults
    [NET]: ../../unified-test-documentation/dasharo-stability/01-net-controller-after-coldboot-warmboot-reboot-suspend.md
    [DCU]: ../../unified-test-documentation/dasharo-compatibility/362-dcu.md
    [SUSP]: ../../unified-test-documentation/dasharo-compatibility/31M-platform-suspend-and-resume.md
    [LCM]: ../../unified-test-documentation/dasharo-compatibility/328-logo-customization-functionality.md

    ## Module: Dasharo security

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [TPM Support][TPM]            | TPM           | Without TPM001.001,TPM002.001 and TPM003.001 |
    | 2.   | [Verified Boot support][VBO]          | VBO           | Without VBO006.001 and VBO007.001    |
    | 3.   | [Measured Boot support][MBO]          | MBO           | All                                  |
    | 4.   | [Secure Boot support][SBO]            | SBO           | All                                  |
    | 5.   | [ME disable/neuter support][MNE]      | MNE           | MNE004.001                           |
    | 6.   | [BIOS lock support][BLS]              | BLS           | All                                  |
    | 7.   | [USB stack enable/disable][USS]       | USS           | All                                  |
    | 8.   | [SMM BIOS write protection][SMM]      | SMM           | All                                  |
    | 9.  | [UEFI Setup password][PSW]            | PSW           | All                                  |
    | 10. | [TPM2 Commands][TPMCMD]               | TPMCMD        | All                                  |

    [TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
    [VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
    [MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
    [SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
    [MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
    [BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md
    [USS]: ../../unified-test-documentation/dasharo-security/20S-usb-stack.md
    [SMM]: ../../unified-test-documentation/dasharo-security/20O-SMM-bios-write-protection.md
    [PSW]: ../../unified-test-documentation/dasharo-security/20R-uefi-setup-password.md
    [TPMCMD]: ../../unified-test-documentation/dasharo-security/200-tpm2-commands.md

    ## Module: Dasharo performance

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [coreboot bring up time measurement][CBMEM] | CBMEM         | All                            |
    | 2.   | [CPU temperature measure][CPT]        | CPT           | All                                  |
    | 3.   | [CPU frequency measure][CPF]          | CPF           | Without CPU003.XXX and CPU005.XXX    |
    | 4.   | [Platform stability][STB]             | STB           | All                                  |
    | 5.   | [Ubuntu booting performance test][BUB] | BUB           | All                                 |
    | 6.   | [Debian booting performance test][BDE] | BDE           | All                                 |
    | 7.   | [FreeBSD booting performance test][BFB] | BFB           | All                                |
    | 8.   | [Proxmox booting performance test][BPM] | BPM           | All                                |
    | 9.   | [Ubuntu Server booting performance test][BUS] | BUS           | All                          |
    | 10.  | [OPNsense (serial output) booting performance test][BOS] | BOS           | All               |
    | 11.  | [OPNsense (VGA output) booting performance test][BOV]    | BOV           | All               |
    | 12.  | [pfSense (serial output) booting performance test][BPS]  | BPS           | All               |
    | 13.  | [pfSense (VGA output) booting performance test][BPV]     | BPV           | All               |

    [CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
    [CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
    [CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
    [STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md
    [BUB]: ../../unified-test-documentation/dasharo-performance/407-ubuntu-booting-performance-test.md
    [BDE]: ../../unified-test-documentation/dasharo-performance/408-debian-booting-performance-test.md
    [BFB]: ../../unified-test-documentation/dasharo-performance/409-freebsd-booting-performance-test.md
    [BPM]: ../../unified-test-documentation/dasharo-performance/410-proxmox-booting-performance-test.md
    [BUS]: ../../unified-test-documentation/dasharo-performance/411-ubuntu-server-booting-performance-test.md
    [BOS]: ../../unified-test-documentation/dasharo-performance/412-opnsense-serial-booting-performance-test.md
    [BOV]: ../../unified-test-documentation/dasharo-performance/413-opnsense-vga-booting-performance-test.md
    [BPS]: ../../unified-test-documentation/dasharo-performance/414-pfsense-serial-booting-performance-test.md
    [BPV]: ../../unified-test-documentation/dasharo-performance/415-pfsense-vga-booting-performance-test.md

=== "VP3210/VP3230"

    ## Module: Dasharo compatibility

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:----:|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [Memory HCL][HCL]                     | HCL           | All                                  |
    | 2.   | [UEFI compatible interface][EFI]      | EFI           | All                                  |
    | 3.   | [Display ports][DSP]                  | DSP           | DSP002.001, DSP002.002, DSP002.003, DSP003.001,SP003.002, DSP003.003 |
    | 4.   | [Network boot utilities][NBT]         | NBT           | All                                  |
    | 5.   | [NVMe support][NVM]                   | NVM           | All                                  |
    | 6.   | [Custom logo][CLG]                    | CLG           | All                                  |
    | 7.   | [Custom boot menu key][CBK]           | CBK           | All                                  |
    | 8.   | [USB HID and MSC Support][USB]        | USB           | USB001.XXX and USB002.XXX            |
    | 9.   | [FreeBSD support][BSD]                | BSD           | All                                  |
    | 10.  | [Debian Stable and Ubuntu LTS support][LBT] | LBT     | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
    | 11.  | [USB-C support][UTC]                  | UTC           | UTC004.001, UTC004.002               |
    | 12.  | [M.2 WiFi/Bluetooth][WLE]             | WLE           | ALL                                  |
    | 14.  | [SMBIOS][DMI]                         | DMI           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, MI006.001 |
    | 15.  | [Custom network boot entries][CNB]    | CNB           | CNB001.002                           |
    | 17.  | [Windows booting][WBT]                | WBT           | WBT001.001                           |
    | 18.  | [Audio subsystem][AUD]                | AUD           | AUD001.001, AUD001.002, AUD002.001, AUD002.002, UD003.001, AUD003.002, AUD004.001, AUD004.002, AUD005.001, AUD005.002, AUD006.001, AUD006.002 |
    | 19.  | [UEFI Shell][USH]                     | USH           | All                                  |
    | 20.  | [USB detection][UDT]                  | UDT           | All                                  |
    | 21.  | [USB booting][UBT]                    | UBT           | All                                  |
    | 22.  | [pfSense support][PFS]                | PFS           | All                                  |
    | 23.  | [OPNsense support][OPN]               | OPN           | All                                  |
    | 24.  | [Proxmox support][PVE]                | PVE           | All                                  |
    | 25.  | [Ubuntu Server support][USS]          | USS           | All                                  |

    [HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
    [EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
    [DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
    [NBT]: ../../unified-test-documentation/dasharo-compatibility/315b-netboot-utilities.md
    [NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
    [CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
    [CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
    [USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
    [BSD]: ../../unified-test-documentation/dasharo-compatibility/307-freebsd-support.md
    [LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
    [UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
    [WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
    [MWL]: ../../unified-test-documentation/dasharo-compatibility/31K-minipcie-verification.md
    [DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
    [CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md
    [WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
    [AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
    [USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
    [UDT]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
    [UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md
    [PFS]: ../../unified-test-documentation/dasharo-compatibility/341-pfSense-support.md
    [OPN]: ../../unified-test-documentation/dasharo-compatibility/342-OPNsense-support.md
    [PVE]: ../../unified-test-documentation/dasharo-compatibility/348-proxmox-support.md
    [USS]: ../../unified-test-documentation/dasharo-compatibility/349-ubuntu-server-support.md

    ## Module: Dasharo security

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [TPM Support][TPM]                    | TPM           | Without TPM001.001,TPM002.001 and TPM003.001 |
    | 2.   | [Verified Boot support][VBO]          | VBO           | Without VBO006.001 and VBO007.001    |
    | 3.   | [Measured Boot support][MBO]          | MBO           | All                                  |
    | 4.   | [Secure Boot support][SBO]            | SBO           | All                                  |
    | 5.   | [ME disable/neuter support][MNE]      | MNE           | MNE004.001                           |
    | 6.   | [BIOS lock support][BLS]              | BLS           | All                                  |
    | 7.   | [USB stack enable/disable][USS]       | USS           | All                                  |
    | 8.   | [SMM BIOS write protection][SMM]      | SMM           | All                                  |

    > Note: in Dasharo for Protectli VP66XX ME is HAP disabled by default - no
    > additional option for ME disabling is available in the Setup Menu.

    [TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
    [VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
    [MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
    [SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
    [MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
    [BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md
    [USS]: ../../unified-test-documentation/dasharo-security/20S-usb-stack.md
    [SMM]: ../../unified-test-documentation/dasharo-security/20O-SMM-bios-write-protection.md

    ## Module: Dasharo performance

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [coreboot bring up time measurement][CBMEM] | CBMEM         | All                            |
    | 2.   | [CPU temperature measure][CPT]        | CPT           | All                                  |
    | 3.   | [CPU frequency measure][CPF]          | CPF           | Without CPU003.XXX and CPU005.XXX    |
    | 4.   | [Platform stability][STB]             | STB           | All                                  |
    | 5.   | [Ubuntu booting performance test][BUB] | BUB           | All                                 |
    | 6.   | [Debian booting performance test][BDE] | BDE           | All                                 |
    | 7.   | [FreeBSD booting performance test][BFB] | BFB           | All                                |
    | 8.   | [Proxmox booting performance test][BPM] | BPM           | All                                |
    | 9.   | [Ubuntu Server booting performance test][BUS] | BUS           | All                          |
    | 10.  | [OPNsense (serial output) booting performance test][BOS] | BOS           | All               |
    | 11.  | [OPNsense (VGA output) booting performance test][BOV]    | BOV           | All               |
    | 12.  | [pfSense (serial output) booting performance test][BPS]  | BPS           | All               |
    | 13.  | [pfSense (VGA output) booting performance test][BPV]     | BPV           | All               |

    [CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
    [CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
    [CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
    [STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md
    [BUB]: ../../unified-test-documentation/dasharo-performance/407-ubuntu-booting-performance-test.md
    [BDE]: ../../unified-test-documentation/dasharo-performance/408-debian-booting-performance-test.md
    [BFB]: ../../unified-test-documentation/dasharo-performance/409-freebsd-booting-performance-test.md
    [BPM]: ../../unified-test-documentation/dasharo-performance/410-proxmox-booting-performance-test.md
    [BUS]: ../../unified-test-documentation/dasharo-performance/411-ubuntu-server-booting-performance-test.md
    [BOS]: ../../unified-test-documentation/dasharo-performance/412-opnsense-serial-booting-performance-test.md
    [BOV]: ../../unified-test-documentation/dasharo-performance/413-opnsense-vga-booting-performance-test.md
    [BPS]: ../../unified-test-documentation/dasharo-performance/414-pfsense-serial-booting-performance-test.md
    [BPV]: ../../unified-test-documentation/dasharo-performance/415-pfsense-vga-booting-performance-test.md

=== "VP2440"

    ## Module: Dasharo compatibility

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:----:|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [Memory HCL][HCL]                     | HCL           | All                                  |
    | 2.   | [UEFI compatible interface][EFI]      | EFI           | All                                  |
    | 3.   | [Display ports][DSP]                  | DSP           | DSP002.001, DSP002.002, DSP002.003, DSP003.001, DSP003.002, DSP003.003 |
    | 4.   | [Network boot utilities][NBT]         | NBT           | All                                  |
    | 5.   | [NVMe support][NVM]                   | NVM           | All                                  |
    | 6.   | [Custom logo][CLG]                    | CLG           | All                                  |
    | 7.   | [Custom boot menu key][CBK]           | CBK           | All                                  |
    | 8.   | [USB HID and MSC Support][USB]        | USB           | USB001.XXX and USB002.XXX            |
    | 9.   | [FreeBSD support][BSD]                | BSD           | All                                  |
    | 10.  | [Debian Stable and Ubuntu LTS support][LBT]  | LBT         | LBT003.001, LBT003.002, LBT004.001, LBT004.002|
    | 11.  | [USB-C support][UTC]                  | UTC           | UTC004.001, UTC004.002               |
    | 12.  | [M.2 WiFi/Bluetooth][WLE]             | WLE           | ALL                                  |
    | 14.  | [SMBIOS][DMI]                         | DMI           | DMI002.001, DMI003.001, DMI004.001, DMI005.001, DMI006.001 |
    | 15.  | [Custom network boot entries][CNB]    | CNB           | CNB001.002                           |
    | 17.  | [Windows booting][WBT]                | WBT           | WBT001.001                           |
    | 18.  | [Audio subsystem][AUD]                | AUD           | AUD001.001, AUD001.002, AUD002.001, AUD002.002, AUD003.001, AUD003.002, AUD004.001, AUD004.002, AUD005.001, AUD005.002, AUD006.001, AUD006.002 |
    | 20.  | [USB detection][UDT]                  | UDT           | All                                  |
    | 21.  | [USB booting][UBT]                    | UBT           | All                                  |
    | 22.  | [pfSense support][PFS]                | PFS           | All                                  |
    | 23.  | [OPNsense support][OPN]               | OPN           | All                                  |
    | 24.  | [Proxmox support][PVE]                | PVE           | All                                  |
    | 25.  | [Ubuntu Server support][USS]          | USS           | All                                  |
    | 26. | [Auto boot time-out][BMM]             | BMM           | All                                  |
    | 27. | [CPU status][CPU]                     | CPU           | CPU001.001, CPU002.001, CPU003.001, CPU004.001|
    | 28. | [ESP scanning][ESP]                   | ESP           | All                                  |
    | 29. | [Reset to defaults][RTD]              | RTD           | RTD001.001, RTD002.001, RTD003.001, RTD004.001, RTD006.001 |
    | 30. | [Ethernet interface][NET]             | NET           | All                                  |
    | 31. | [Dasharo Configuration Utility][NET]  | DCU           | DCU001.001, DCU002.001, DCU003.001   |
    | 33. | [Sleep mode][SUSP]                    | SUSP          | SUSP001.001, SUSP002.001, SUSP003.001, SUSP005.001|

    [HCL]: ../../unified-test-documentation/dasharo-compatibility/301-memory-hcl.md
    [EFI]: ../../unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface.md
    [DSP]: ../../unified-test-documentation/dasharo-compatibility/31E-display-ports-and-lcd.md
    [NBT]: ../../unified-test-documentation/dasharo-compatibility/315b-netboot-utilities.md
    [NVM]: ../../unified-test-documentation/dasharo-compatibility/312-nvme-support.md
    [CLG]: ../../unified-test-documentation/dasharo-compatibility/304-custom-logo.md
    [CBK]: ../../unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key.md
    [USB]: ../../unified-test-documentation/dasharo-compatibility/306-usb-hid-and-msc-support.md
    [BSD]: ../../unified-test-documentation/dasharo-compatibility/307-freebsd-support.md
    [LBT]: ../../unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support.md
    [UTC]: ../../unified-test-documentation/dasharo-compatibility/31H-usb-type-c.md
    [WLE]: ../../unified-test-documentation/dasharo-compatibility/318-m2-wifi-bluetooth.md
    [MWL]: ../../unified-test-documentation/dasharo-compatibility/31K-minipcie-verification.md
    [DMI]: ../../unified-test-documentation/dasharo-compatibility/31L-smbios.md
    [CNB]: ../../unified-test-documentation/dasharo-compatibility/30A-custom-network-boot-entries.md
    [WBT]: ../../unified-test-documentation/dasharo-compatibility/31A-windows-booting.md
    [AUD]: ../../unified-test-documentation/dasharo-compatibility/31F-audio-subsystem.md
    [USH]: ../../unified-test-documentation/dasharo-compatibility/30P-uefi-shell.md
    [UDT]: ../../unified-test-documentation/dasharo-compatibility/31O-usb-detect.md
    [UBT]: ../../unified-test-documentation/dasharo-compatibility/31N-usb-boot.md
    [PFS]: ../../unified-test-documentation/dasharo-compatibility/341-pfSense-support.md
    [OPN]: ../../unified-test-documentation/dasharo-compatibility/342-OPNsense-support.md
    [PVE]: ../../unified-test-documentation/dasharo-compatibility/348-proxmox-support.md
    [USS]: ../../unified-test-documentation/dasharo-compatibility/349-ubuntu-server-support.md
    [CPU]: ../../unified-test-documentation/dasharo-compatibility/31T-cpu-status.md
    [BMM]: ../../dasharo-menu-docs/boot-maintenance-mgr.md#boot-maintenance-manager
    [ESP]: ../../unified-test-documentation/dasharo-compatibility/361-esp-scanning.md
    [RTD]: ../../dasharo-menu-docs/overview.md#f9-reset-to-defaults
    [NET]: ../../unified-test-documentation/dasharo-stability/01-net-controller-after-coldboot-warmboot-reboot-suspend.md
    [DCU]: ../../unified-test-documentation/dasharo-compatibility/362-dcu.md
    [SUSP]: ../../unified-test-documentation/dasharo-compatibility/31M-platform-suspend-and-resume.md
    [LCM]: ../../unified-test-documentation/dasharo-compatibility/328-logo-customization-functionality.md

    ## Module: Dasharo security

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [TPM Support][TPM]            | TPM           | Without TPM001.001,TPM002.001 and TPM003.001 |
    | 2.   | [Verified Boot support][VBO]          | VBO           | Without VBO006.001 and VBO007.001    |
    | 3.   | [Measured Boot support][MBO]          | MBO           | All                                  |
    | 4.   | [Secure Boot support][SBO]            | SBO           | All                                  |
    | 5.   | [ME disable/neuter support][MNE]      | MNE           | MNE004.001                           |
    | 6.   | [BIOS lock support][BLS]              | BLS           | All                                  |
    | 7.   | [USB stack enable/disable][USS]       | USS           | All                                  |
    | 8.   | [SMM BIOS write protection][SMM]      | SMM           | All                                  |
    | 9.  | [UEFI Setup password][PSW]            | PSW           | All                                  |
    | 10. | [TPM2 Commands][TPMCMD]               | TPMCMD        | All                                  |

    [TPM]: ../../unified-test-documentation/dasharo-security/200-tpm-support.md
    [VBO]: ../../unified-test-documentation/dasharo-security/201-verified-boot.md
    [MBO]: ../../unified-test-documentation/dasharo-security/203-measured-boot.md
    [SBO]: ../../unified-test-documentation/dasharo-security/206-secure-boot.md
    [MNE]: ../../unified-test-documentation/dasharo-security/20F-me-neuter.md
    [BLS]: ../../unified-test-documentation/dasharo-security/20J-bios-lock-support.md
    [USS]: ../../unified-test-documentation/dasharo-security/20S-usb-stack.md
    [SMM]: ../../unified-test-documentation/dasharo-security/20O-SMM-bios-write-protection.md
    [PSW]: ../../unified-test-documentation/dasharo-security/20R-uefi-setup-password.md
    [TPMCMD]: ../../unified-test-documentation/dasharo-security/200-tpm2-commands.md

    ## Module: Dasharo performance

    | No.  | Supported test suite                  | Test suite ID | Supported test cases                 |
    |:-----|:--------------------------------------|:-------------:|:-------------------------------------|
    | 1.   | [coreboot bring up time measurement][CBMEM] | CBMEM         | All                            |
    | 2.   | [CPU temperature measure][CPT]        | CPT           | All                                  |
    | 3.   | [CPU frequency measure][CPF]          | CPF           | Without CPU003.XXX and CPU005.XXX    |
    | 4.   | [Platform stability][STB]             | STB           | All                                  |
    | 5.   | [Ubuntu booting performance test][BUB] | BUB           | All                                 |
    | 6.   | [Debian booting performance test][BDE] | BDE           | All                                 |
    | 7.   | [FreeBSD booting performance test][BFB] | BFB           | All                                |
    | 8.   | [Proxmox booting performance test][BPM] | BPM           | All                                |
    | 9.   | [Ubuntu Server booting performance test][BUS] | BUS           | All                          |
    | 10.  | [OPNsense (serial output) booting performance test][BOS] | BOS           | All               |
    | 11.  | [OPNsense (VGA output) booting performance test][BOV]    | BOV           | All               |
    | 12.  | [pfSense (serial output) booting performance test][BPS]  | BPS           | All               |
    | 13.  | [pfSense (VGA output) booting performance test][BPV]     | BPV           | All               |

    [CBMEM]: ../../unified-test-documentation/dasharo-performance/400-coreboot-boot-measure.md
    [CPT]: ../../unified-test-documentation/dasharo-performance/401-cpu-temperature.md
    [CPF]: ../../unified-test-documentation/dasharo-performance/402-cpu-frequency.md
    [STB]: ../../unified-test-documentation/dasharo-performance/404-platform-stability.md
    [BUB]: ../../unified-test-documentation/dasharo-performance/407-ubuntu-booting-performance-test.md
    [BDE]: ../../unified-test-documentation/dasharo-performance/408-debian-booting-performance-test.md
    [BFB]: ../../unified-test-documentation/dasharo-performance/409-freebsd-booting-performance-test.md
    [BPM]: ../../unified-test-documentation/dasharo-performance/410-proxmox-booting-performance-test.md
    [BUS]: ../../unified-test-documentation/dasharo-performance/411-ubuntu-server-booting-performance-test.md
    [BOS]: ../../unified-test-documentation/dasharo-performance/412-opnsense-serial-booting-performance-test.md
    [BOV]: ../../unified-test-documentation/dasharo-performance/413-opnsense-vga-booting-performance-test.md
    [BPS]: ../../unified-test-documentation/dasharo-performance/414-pfsense-serial-booting-performance-test.md
    [BPV]: ../../unified-test-documentation/dasharo-performance/415-pfsense-vga-booting-performance-test.md
