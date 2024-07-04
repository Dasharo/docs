# Release Notes

=== "fw6"
    Following Release Notes describe status of Open Source Firmware development for
    Protectli FW6.

    For details about our release process please read
    [Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

    <center>
    [Subscribe to Protectli FW6 Dasharo Release Newsletter]
    [newsletter]{.md-button .md-button--primary .center}
    </center>

    Test results for this platform can be found
    [here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit?usp=sharing).

    ## v1.0.14 - 2022-05-13

    ### Changed

    - Throttling temperature to 75 Celsius degrees

    ### Known issues

    - Samsung memory modules do not work properly on older FW6A/B/C (SKU6LAV20)

    ### Binaries

    [protectli_vault_kbl_v1.0.14.rom][v1.0.14_rom]{.md-button}
    [sha256][v1.0.14_hash]{.md-button}
    [sha256.sig][v1.0.14_sig]{.md-button}

    To verify binary integrity with hash and signature please follow the
    instructions in [Dasharo release signature verification](/guides/signature-verification)
    using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/protectli-dasharo-firewall-release-1.0-key.asc)

    ### SBOM (Software Bill of Materials)

    - [coreboot based on 87f9fc85 revision e04b0ac8](https://github.com/Dasharo/coreboot/commits/e04b0ac8)
    - [seabios based on v1.0.6 revision 03bcdcaf](https://github.com/Dasharo/SeaBIOS/commits/03bcdcaf)
    - [ipxe based on 2019.3 stable revision ebf2eaf5](https://github.com/ipxe/ipxe/commits/ebf2eaf5)
    - [memtest based on v002 revision dd5b4ff2](https://review.coreboot.org/admin/repos/memtest86plus,general)
    - Management Engine: ME 11.8.50.3399,
    SHA256: e1ce735139b6d9ebb81d7f6db288b0a896c39e4b1e606324b915bec949b6aca6
    - microcode:
        + CPU signature: 0x0406E3, Date: 03.10.2019, Revision: 0xD6
        + CPU signature: 0x0806E9, Date: 27.04.2020, Revision: 0xD6
        + CPU signature: 0x0806E9, Date: 27.04.2020, Revision: 0xD6
        + CPU signature: 0x0806EA, Date: 27.04.2020, Revision: 0xD6
    - VBIOS:
        + VBIOS blob for FW6A/B/C,
        SHA256: 470d3faefb09432bea00d637ec6b3ff51854e6cff0ee56627c0773acaffa4830
        + VBIOS blob for FW6D/E,
        SHA256: d1c746127e5288942efae65907739e18ff395fab70925b44dbafafd9e7b30cd7

    [newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
    [v1.0.14_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_kbl/v1.0.14/protectli_vault_kbl_v1.0.14.rom
    [v1.0.14_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_kbl/v1.0.14/protectli_vault_kbl_v1.0.14.rom.sha256
    [v1.0.14_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_kbl/v1.0.14/protectli_vault_kbl_v1.0.14.rom.sha256.sig

=== "v1x1x"
    Following Release Notes describe status of Open Source Firmware development
    for Protectli V1210/V1410/V1610

    For details about our release process please read
    [Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

    <center>
    [Subscribe to Protectli V1210/V1410/V1610 Dasharo Release Newsletter]
    [newsletter]{.md-button .md-button--primary .center}
    </center>

    Test results for this platform can be found
    [here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit#gid=1316498194).

    [newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL

    <!--Empty pixel to avoid orphaned pages when overview is hidden-->
    [![empty-pixel](../../images/empty_pixel.png)](overview.md)

=== "vp46xx"
    Following Release Notes describe status of Open Source Firmware development for
    Protectli VP46xx

    For details about our release process please read
    [Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

    <center>
    [Subscribe to Protectli VP46xx Dasharo Release Newsletter]
    [newsletter]{.md-button .md-button--primary .center}
    </center>

    Test results for this platform can be found
    [here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit?usp=sharing).

    ## v1.2.0 - 2024-03-25

    Test results for this release can be found
    [here](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit#gid=2016830329).

    ### Added

    - [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
    - [Serial port console redirection option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#serial-port-configuration)
    - [Customizable Serial Number and UUID via CBFS support](https://github.com/Dasharo/dcu)
    - [Customizable boot logo support](https://github.com/Dasharo/dcu)
    - [Support for taking screenshots in the firmware](https://docs.dasharo.com/dev-proc/screenshots/#taking-screenshots)
    - [ESP partition scanning in look for grubx64.efi or shimx64.efi or Windows bootmgr](https://github.com/Dasharo/dasharo-issues/issues/94)
    - Microsoft and Windows 2023 UEFI Secure Boot certificates
    - UEFI 2.8 errata C compliance in EDKII fork

    ### Changed

    - Rebased to coreboot 4.21
    - Enroll default UEFI Secure Boot keys on the first boot
    - [Improved UEFI Secure Boot menu user experience](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
    - Scope of reset to defaults hotkey to global in firmware setup
    - Updated microcode to the newer version; refer to SBOM section below
    - Updated ME to the newer version; refer to SBOM section below
    - Prepared unified support for v1 and v2 CPUs resulting in a single binary for
    all 3 board variants

    ### Fixed

    - [Auto Boot Time-out is reset to 0 when F9 is pressed](https://github.com/Dasharo/dasharo-issues/issues/513)
    - [Reset to defaults with F9 causes the wrong settings to be restored](https://github.com/Dasharo/dasharo-issues/issues/355)
    - [RTC time and date resetting to the coreboot build date on 29th February](https://review.coreboot.org/c/coreboot/+/80790)

    ### Known issues

    - [Unexpected errors in dmesg on VP4670 v2 with 1.2.0](https://github.com/Dasharo/dasharo-issues/issues/746)
    - [Maximum reported frequency is base frequency, not turbo frequency (Windows 11)](https://github.com/Dasharo/dasharo-issues/issues/522)
    - [No ability to change active PCR banks with TPM PPI in FW](https://github.com/Dasharo/dasharo-issues/issues/521)
    - [DisplayPort output does not work with 16:10 (1920x1200) monitors](https://github.com/Dasharo/dasharo-issues/issues/531)

    ### Binaries

    [protectli_vp46xx_v1.2.0.rom][protectli_vp46xx_v1.2.0.rom_file]{.md-button}
    [sha256][protectli_vp46xx_v1.2.0.rom_hash]{.md-button}
    [sha256.sig][protectli_vp46xx_v1.2.0.rom_sig]{.md-button}

    [protectli_vp46xx_v1.2.0_dev_signed.rom][protectli_vp46xx_v1.2.0_dev_signed.rom_file]{.md-button}
    [sha256][protectli_vp46xx_v1.2.0_dev_signed.rom_hash]{.md-button}
    [sha256.sig][protectli_vp46xx_v1.2.0_dev_signed.rom_sig]{.md-button}

    To verify binary integrity with hash and signature please follow the
    instructions in [Dasharo release signature verification](/guides/signature-verification)
    using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/dasharo-release-1.2.x-for-protectli-signing-key.asc)

    ### SBOM (Software Bill of Materials)

    - [Dasharo coreboot fork based on 4.21 revision add9d720](https://github.com/Dasharo/coreboot/tree/add9d720)
    - [Dasharo EDKII fork based on edk2-stable202002 revision 2a15268b](https://github.com/Dasharo/edk2/tree/2a15268b)
    - [iPXE based on 2023.12 revision 838611b3](https://github.com/Dasharo/ipxe/tree/838611b3)
    - [vboot based on 0c11187c75 revision 0c11187c](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/0c11187c/)
    - [Intel Management Engine based on v14.0.47.1558 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/protectli/vault_cml/me.bin)
    - [Intel Flash Descriptor based on v1.0 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/protectli/vault_cml/descriptor.bin)
    - [Intel Firmware Support Package based on CometLake1 9.0.7B.20 revision 481ea7cf](https://github.com/intel/FSP/tree/481ea7cf/CometLakeFspBinPkg/CometLake1)
    - [Intel Firmware Support Package based on CometLake2 9.2.7B.20 revision 481ea7cf](https://github.com/intel/FSP/tree/481ea7cf/CometLakeFspBinPkg/CometLake2)
    - [Intel microcode based on CML-U42 V0 0x000000f8 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-8e-0c)
    - [Intel microcode based on CML-U62 V1 A0 0x000000f8 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-a6-00)
    - [Intel microcode based on CML-U62 V2 K1 0x000000f8 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-a6-01)

    [protectli_vp46xx_v1.2.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.2.0/protectli_vp46xx_v1.2.0.rom
    [protectli_vp46xx_v1.2.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.2.0/protectli_vp46xx_v1.2.0.rom.sha256
    [protectli_vp46xx_v1.2.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.2.0/protectli_vp46xx_v1.2.0.rom.sha256.sig
    [protectli_vp46xx_v1.2.0_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.2.0/protectli_vp46xx_v1.2.0_dev_signed.rom
    [protectli_vp46xx_v1.2.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.2.0/protectli_vp46xx_v1.2.0_dev_signed.rom.sha256
    [protectli_vp46xx_v1.2.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.2.0/protectli_vp46xx_v1.2.0_dev_signed.rom.sha256.sig

    ## v1.1.0 - 2023-06-05

    Release version v1.1.0 is currently only available for the VP4670 platform.

    ### Added

    - [USB stack and mass storage enable/disable option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
    - [SMM BIOS write protection enable/disable option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)

    ### Changed

    - Reverted to use FSP GOP for graphics initialization as it caused problems with
    Windows 11 display on VP4670
    - Switched to use driver for IT8784E Super I/O, which is present on the boards
    - CPU power limits increased from baseline to performance
    - [Updating from v1.0.x requires flashing the WP_RO recovery partition](https://docs.dasharo.com/variants/protectli_vp46xx/firmware-update/#updating-to-dasharo-v1018-or-v1019-or-v110)
    - [Firmware version v1.1.x are signed with a new key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/dasharo-release-1.1.x-for-protectli-signing-key.asc)

    ### Fixed

    - [Booting problems with Ubuntu 22.04](https://github.com/Dasharo/dasharo-issues/issues/370)
    - [Low CPU frequency values](https://github.com/Dasharo/dasharo-issues/issues/369)
    - Disabled C states deeper than C1 on VP4670 to fix Proxmox booting issue
    - [Protectli VP4670 - windows crashes after installing updates](https://github.com/Dasharo/dasharo-issues/issues/302)
    - [The inconvenience of using external headsets VP46XX](https://github.com/Dasharo/dasharo-issues/issues/167)

    ### Known issues

    - [Popup with information about recovery mode is still displayed after flashing with a valid binary](https://github.com/Dasharo/dasharo-issues/issues/320)

    ### Binaries

    [protectli_vp4670_v1.1.0.rom][protectli_vp4670_v1.1.0.rom_file]{.md-button}
    [sha256][protectli_vp4670_v1.1.0.rom_hash]{.md-button}
    [sha256.sig][protectli_vp4670_v1.1.0.rom_sig]{.md-button}

    To verify binary integrity with hash and signature please follow the
    instructions in [Dasharo release signature verification](/guides/signature-verification)
    using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/dasharo-release-1.1.x-for-protectli-signing-key.asc)

    ### SBOM (Software Bill of Materials)

    - [coreboot based on c6ee1509da revision dcc5f2e2](https://github.com/Dasharo/coreboot/tree/dcc5f2e2)
    - [edk2 based on 7f90b9cd revision 19bf14b4](https://github.com/Dasharo/edk2/tree/19bf14b4)
    - [iPXE based on 6ba671ac revision 6ba671ac](https://github.com/ipxe/ipxe/tree/6ba671ac)

    [newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
    [protectli_vp4670_v1.1.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.1.0/protectli_vp4670_v1.1.0.rom
    [protectli_vp4670_v1.1.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.1.0/protectli_vp4670_v1.1.0.rom.sha256
    [protectli_vp4670_v1.1.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.1.0/protectli_vp4670_v1.1.0.rom.sha256.sig

    ## v1.0.19 - 2022-12-08

    ### Changed

    - ME is now disabled by default (ME soft-disable)
    - vboot is now run as separate verstage (previously was run inside bootblock)
    - increased pre-RAM console buffer to fit more early cbmem logs

    ### Binaries

    [protectli_vp4630_vp4650_v1.0.19.rom][protectli_vp4630_vp4650_v1.0.19.rom_file]{.md-button}
    [sha256][protectli_vp4630_vp4650_v1.0.19.rom_hash]{.md-button}
    [sha256.sig][protectli_vp4630_vp4650_v1.0.19.rom_sig]{.md-button}

    [protectli_vp4670_v1.0.19.rom][protectli_vp4670_v1.0.19.rom_file]{.md-button}
    [sha256][protectli_vp4670_v1.0.19.rom_hash]{.md-button}
    [sha256.sig][protectli_vp4670_v1.0.19.rom_sig]{.md-button}

    To verify binary integrity with hash and signature please follow the
    instructions in [Dasharo release signature verification](/guides/signature-verification)
    using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/protectli-dasharo-firewall-release-1.0-key.asc)

    ### SBOM (Software Bill of Materials)

    - [coreboot based on c6ee1509da revision 9034fb12](https://github.com/Dasharo/coreboot/tree/9034fb12)
    - [edk2 based on 7f90b9cd revision e31b7a71](https://github.com/Dasharo/edk2/tree/e31b7a71)
    - [iPXE for EFI revision 988d2](https://github.com/ipxe/ipxe/tree/988d2c13cdf0f0b4140685af35ced70ac5b3283c)
    - VP4670: [Cometlake1 FSP 9.0.7B.20](https://github.com/intel/FSP/tree/12160fe64bc1caaba3c2d6be44da0cd8787a2561/CometLakeFspBinPkg/CometLake1)
    - VP4630 and VP4650: [Cometlake2 FSP 9.2.7B.20](https://github.com/intel/FSP/tree/12160fe64bc1caaba3c2d6be44da0cd8787a2561/CometLakeFspBinPkg/CometLake2)
    - Intel i225 EFI driver version 0.10.4,
    SHA256: 2d234ecf629fc10dc0c291a1390de3d27a05c6ecbd935628b6ff154f386d061e
    - Management Engine: Custom image based on ME 14.0.47.1558,
    SHA256: 7fa37e108176c9a2d0df60c93b10b3ad9c7725f1f82b87197a2991208c4cffec
    - microcode:
        + CPU signature: 0x0806EC, Date: 17.11.2021, Revision: 0xF0
        + CPU signature: 0x0A0660, Date: 15.11.2021, Revision: 0xF0
        + CPU signature: 0x0A0661, Date: 16.11.2021, Revision: 0xF0

    ## v1.0.18 - 2022-11-16

    Test results for this release can be found
    [here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit#gid=1613384145).

    ### Added

    - Support for VP4650 and VP4670 platforms
    - Platform will beep 12 times and blink HDD led on critical firmware errors

    ### Changed

    - Disabled Intel PTT (fTPM)
    - [Removed workaround for graphics power management as the issue no longer reproduces on newer revision of the hardware](https://github.com/Dasharo/dasharo-issues/issues/26)
    - Binaries are built with coreboot-sdk 2021-09-23_b0d87f753c (was 0ad5fbd48d)
    - Open-source graphics initialization with libgfxinit instead of proprietary and
    closed FSP GOP driver

    ### Binaries

    [protectli_vp4630_vp4650_v1.0.18.rom][protectli_vp4630_vp4650_v1.0.18.rom_file]{.md-button}
    [sha256][protectli_vp4630_vp4650_v1.0.18.rom_hash]{.md-button}
    [sha256.sig][protectli_vp4630_vp4650_v1.0.18.rom_sig]{.md-button}

    [protectli_vp4670_v1.0.18.rom][protectli_vp4670_v1.0.18.rom_file]{.md-button}
    [sha256][protectli_vp4670_v1.0.18.rom_hash]{.md-button}
    [sha256.sig][protectli_vp4670_v1.0.18.rom_sig]{.md-button}

    To verify binary integrity with hash and signature please follow the
    instructions in [Dasharo release signature verification](/guides/signature-verification)
    using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/protectli-dasharo-firewall-release-1.0-key.asc)

    ### SBOM (Software Bill of Materials)

    - [coreboot based on c6ee1509da revision ed9f6fe0](https://github.com/Dasharo/coreboot/tree/ed9f6fe0)
    - [edk2 based on 7f90b9cd revision e31b7a71](https://github.com/Dasharo/edk2/tree/e31b7a71)
    - [iPXE for EFI revision 988d2](https://github.com/ipxe/ipxe/tree/988d2c13cdf0f0b4140685af35ced70ac5b3283c)
    - VP4670: [Cometlake1 FSP 9.0.7B.20](https://github.com/intel/FSP/tree/12160fe64bc1caaba3c2d6be44da0cd8787a2561/CometLakeFspBinPkg/CometLake1)
    - VP4630 and VP4650: [Cometlake2 FSP 9.2.7B.20](https://github.com/intel/FSP/tree/12160fe64bc1caaba3c2d6be44da0cd8787a2561/CometLakeFspBinPkg/CometLake2)
    - Intel i225 EFI driver version 0.10.4,
    SHA256: 2d234ecf629fc10dc0c291a1390de3d27a05c6ecbd935628b6ff154f386d061e
    - Management Engine: Custom image based on ME 14.0.47.1558,
    SHA256: 7fa37e108176c9a2d0df60c93b10b3ad9c7725f1f82b87197a2991208c4cffec
    - microcode:
        + CPU signature: 0x0806EC, Date: 17.11.2021, Revision: 0xF0
        + CPU signature: 0x0A0660, Date: 15.11.2021, Revision: 0xF0
        + CPU signature: 0x0A0661, Date: 16.11.2021, Revision: 0xF0

    ## v1.0.17 - 2022-08-17

    Test results for this release can be found
    [here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit#gid=1613384145).

    ### Added

    - [Tools for resigning Vboot images with one RW partition](https://docs.dasharo.com/guides/vboot-signing/)

    ### Changed

    - Set thermal throttling temperature to 80 degrees
    - Disabled UEFI Secure Boot by default

    ### Fixed

    - Platform rebooting every 56 minutes
    - Incorrect menu labels displayed in network boot menu
    - Built-in audio jack does not work

    ### Binaries

    [protectli_vault_cml_v1.0.17.rom_file][protectli_vault_cml_v1.0.17.rom_file]{.md-button}
    [protectli_vault_cml_v1.0.17.rom_hash][protectli_vault_cml_v1.0.17.rom_hash]{.md-button}
    [protectli_vault_cml_v1.0.17.rom_sig][protectli_vault_cml_v1.0.17.rom_sig]{.md-button}

    To verify binary integrity with hash and signature please follow the
    instructions in [Dasharo release signature verification](/guides/signature-verification)
    using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/protectli-dasharo-firewall-release-1.0-key.asc)

    ### SBOM (Software Bill of Materials)

    - [coreboot based on 4.16 revision d662831d](https://github.com/Dasharo/coreboot/tree/d662831d)
    - [edk2 based on 7f90b9cd revision 576aa6a4](https://github.com/Dasharo/edk2/tree/576aa6a4)
    - [iPXE for EFI revision 988d2](https://github.com/ipxe/ipxe/tree/988d2c13cdf0f0b4140685af35ced70ac5b3283c)
    - [Cometlake2 FSP 9.2.7B.20](https://github.com/intel/FSP/tree/10eae55b8eb0febfa2dfabf4017701b072866170/CometLakeFspBinPkg/CometLake2)
    - Intel i225 EFI driver version 0.10.4,
    SHA256: 2d234ecf629fc10dc0c291a1390de3d27a05c6ecbd935628b6ff154f386d061e
    - Management Engine: Custom image based on ME 14.0.47.1558,
    SHA256: 7fa37e108176c9a2d0df60c93b10b3ad9c7725f1f82b87197a2991208c4cffec
    - microcode:
        + CPU signature: 0x0806EC, Date: 28.04.2021, Revision: 0xEC
        + CPU signature: 0x0A0660, Date: 28.04.2021, Revision: 0xEA
        + CPU signature: 0x0A0661, Date: 29.04.2021, Revision: 0xEC

    ## v1.0.16 - 2022-07-13

    Test results for this release can be found
    [here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit#gid=1613384145).

    ### Added

    - [Vboot Verified Boot](https://docs.dasharo.com/guides/vboot-signing/)
    - [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
    - [Vboot recovery notification in UEFI Payload](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)
    - [UEFI Shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
    - [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
    - [Intel ME soft disable](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20F-me-neuter/)
    - [BIOS flash protection for Vboot recovery region](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20J-bios-lock-support/)

    ### Changed

    - [Changed supported CPUs to Comet Lake stepping 2](https://github.com/intel/FSP/tree/master/CometLakeFspBinPkg#comet-lake-binary-differences)

    ### Fixed

    - [i225 network controller initialization takes too much time](https://github.com/Dasharo/dasharo-issues/issues/65)
    - [CVE-2022-29264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-29264)

    ### Binaries

    [protectli_vault_cml_v1.0.16.rom][v1.0.16_rom]{.md-button}
    [sha256][v1.0.16_hash]{.md-button}
    [sha256.sig][v1.0.16_sig]{.md-button}

    To verify binary integrity with hash and signature please follow the
    instructions in [Dasharo release signature verification](/guides/signature-verification)
    using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/protectli-dasharo-firewall-release-1.0-key.asc)

    ### SBOM (Software Bill of Materials)

    - [coreboot based on 4.16 revision dfaaf44d](https://github.com/Dasharo/coreboot/tree/dfaaf44d)
    - [edk2 based on 7f90b9cd revision 5345a611](https://github.com/Dasharo/edk2/tree/5345a611)
    - [iPXE for EFI revision 988d2](https://github.com/ipxe/ipxe/tree/988d2c13cdf0f0b4140685af35ced70ac5b3283c)
    - [Cometlake2 FSP 9.2.7B.20](https://github.com/intel/FSP/tree/10eae55b8eb0febfa2dfabf4017701b072866170/CometLakeFspBinPkg/CometLake2)
    - Intel i225 EFI driver version 0.10.4,
    SHA256: 2d234ecf629fc10dc0c291a1390de3d27a05c6ecbd935628b6ff154f386d061e
    - Management Engine: Custom image based on ME 14.0.47.1558,
    SHA256: 7fa37e108176c9a2d0df60c93b10b3ad9c7725f1f82b87197a2991208c4cffec
    - microcode:
        + CPU signature: 0x0806EC, Date: 28.04.2021, Revision: 0xEC
        + CPU signature: 0x0A0660, Date: 28.04.2021, Revision: 0xEA
        + CPU signature: 0x0A0661, Date: 29.04.2021, Revision: 0xEC

    ## v1.0.13 - 2022-03-22

    ### Added

    - UEFI boot support
    - i225 network controller network boot support
    - Customized boot menu keys
    - Customized setup menu keys
    - Configurable boot order
    - Configurable boot options

    ### Changed

    - ME version to 14.0.47.1558

    ### Known issues

    - [i225 network controller initialization takes too much time](https://github.com/Dasharo/dasharo-issues/issues/65)

    ### Binaries

    [protectli_vault_cml_v1.0.13.rom][v1.0.13_rom]{.md-button}
    [sha256][v1.0.13_hash]{.md-button}
    [sha256.sig][v1.0.13_sig]{.md-button}

    To verify binary integrity with hash and signature please follow the
    instructions in [Dasharo release signature verification](/guides/signature-verification)
    using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/protectli-dasharo-firewall-release-1.0-key.asc)

    ### SBOM (Software Bill of Materials)

    - [coreboot based on 4.16 revision 546e1c86](https://github.com/Dasharo/coreboot/tree/546e1c86)
    - [edk2 based on 7f90b9cd revision 7f90b9cd](https://github.com/Dasharo/edk2/tree/7f90b9cd)
    - [iPXE for EFI revision 988d2](https://github.com/ipxe/ipxe/tree/988d2c13cdf0f0b4140685af35ced70ac5b3283c)
    - [Cometlake1 FSP 9.0.7B.20](https://github.com/intel/FSP/tree/10eae55b8eb0febfa2dfabf4017701b072866170/CometLakeFspBinPkg/CometLake1)
    - Intel i225 EFI driver version 0.9.03,
    SHA256: 63e77b237dc9a8aacdd7465675ee88afc01dad3204156a91a0976a4ad1ed5b00
    - Management Engine: Custom image based on ME 14.0.47.1558,
    SHA256: 7fa37e108176c9a2d0df60c93b10b3ad9c7725f1f82b87197a2991208c4cffec
    - microcode:
        + CPU signature: 0x0806EC, Date: 28.04.2021, Revision: 0xEC
        + CPU signature: 0x0A0660, Date: 28.04.2021, Revision: 0xEA

    [newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
    [protectli_vp4630_vp4650_v1.0.19.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.19/protectli_vp4630_vp4650_v1.0.19.rom
    [protectli_vp4630_vp4650_v1.0.19.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.19/protectli_vp4630_vp4650_v1.0.19.rom.sha256
    [protectli_vp4630_vp4650_v1.0.19.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.19/protectli_vp4630_vp4650_v1.0.19.rom.sha256.sig
    [protectli_vp4670_v1.0.19.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.19/protectli_vp4670_v1.0.19.rom
    [protectli_vp4670_v1.0.19.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.19/protectli_vp4670_v1.0.19.rom.sha256
    [protectli_vp4670_v1.0.19.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.19/protectli_vp4670_v1.0.19.rom.sha256.sig
    [protectli_vp4630_vp4650_v1.0.18.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.18/protectli_vp4630_vp4650_v1.0.18.rom
    [protectli_vp4630_vp4650_v1.0.18.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.18/protectli_vp4630_vp4650_v1.0.18.rom.sha256
    [protectli_vp4630_vp4650_v1.0.18.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.18/protectli_vp4630_vp4650_v1.0.18.rom.sha256.sig
    [protectli_vp4670_v1.0.18.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.18/protectli_vp4670_v1.0.18.rom
    [protectli_vp4670_v1.0.18.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.18/protectli_vp4670_v1.0.18.rom.sha256
    [protectli_vp4670_v1.0.18.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.18/protectli_vp4670_v1.0.18.rom.sha256.sig
    [protectli_vault_cml_v1.0.17.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.17/protectli_vault_cml_v1.0.17.rom
    [protectli_vault_cml_v1.0.17.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.17/protectli_vault_cml_v1.0.17.rom.sha256
    [protectli_vault_cml_v1.0.17.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.17/protectli_vault_cml_v1.0.17.rom.sha256.sig
    [v1.0.16_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.16/protectli_vault_cml_v1.0.16.rom
    [v1.0.16_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.16/protectli_vault_cml_v1.0.16.rom.sha256
    [v1.0.16_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/v1.0.16/protectli_vault_cml_v1.0.16.rom.sha256.sig
    [v1.0.13_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.13.rom
    [v1.0.13_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.13.rom.sha256
    [v1.0.13_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_cml/protectli_vault_cml_v1.0.13.rom.sha256.sig

=== "vp66xx"
    Following Release Notes describe status of Open Source Firmware development
    for Protectli VP6630/VP6650/VP6670

    For details about our release process please read
    [Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

    <center>
    [Subscribe to Protectli VP6630/VP6650/VP6670 Dasharo Release Newsletter]
    [newsletter]{.md-button .md-button--primary .center}
    </center>

    Test results for this platform can be found
    [here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit#gid=1316498194).

    [newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL

    <!--Empty pixel to avoid orphaned pages when overview is hidden-->
    [![empty-pixel](../../images/empty_pixel.png)](overview.md)

=== "vp2410"
    Following Release Notes describe status of open-source firmware development for
    Protectli VP2410 family.

    For details about our release process please read
    [Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

    <center>
    [Subscribe to Protectli VP2410 Dasharo Release Newsletter]
    [newsletter]{.md-button .md-button--primary .center}
    </center>

    Test results for this platform can be found
    [here](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit#gid=1033426620).

    ## v1.1.0 - 2024-05-16

    ### Added

    - [SMM BIOS write protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
    - [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
    - [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
    - [Serial port console redirection option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#serial-port-configuration)
    - [Customizable Serial Number and UUID via CBFS support](https://github.com/Dasharo/dcu)
    - [Customizable boot logo support](https://github.com/Dasharo/dcu)
    - [Support for taking screenshots in the firmware](https://docs.dasharo.com/dev-proc/screenshots/#taking-screenshots)
    - [ESP partition scanning in look for grubx64.efi or shimx64.efi or Windows bootmgr](https://github.com/Dasharo/dasharo-issues/issues/94)
    - Microsoft and Windows 2023 UEFI Secure Boot certificates
    - UEFI 2.8 errata C compliance in EDKII fork

    ### Changed

    - Rebased to coreboot 4.21
    - Enroll default UEFI Secure Boot keys on the first boot
    - [Improved UEFI Secure Boot menu user experience](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
    - Scope of reset to defaults hotkey to global in firmware setup
    - Updated microcode to the newer version; refer to SBOM section below
    - Updated ME/TXE to the newer version; refer to SBOM section below
    - Updated FSP to the newer version; refer to SBOM section below

    ### Fixed

    - [Auto Boot Time-out is reset to 0 when F9 is pressed](https://github.com/Dasharo/dasharo-issues/issues/513)
    - [Reset to defaults with F9 causes the wrong settings to be restored](https://github.com/Dasharo/dasharo-issues/issues/355)
    - RAM memory capacity not reported in firmware Setup Menu
    - [RTC time and date resetting to the coreboot build date on 29th February](https://review.coreboot.org/c/coreboot/+/80790)

    ### Known issues

    - [VP2410 does not power on after shutting down with power button 4s override](https://github.com/Dasharo/dasharo-issues/issues/643)
    - [USB 2.0 sticks not detected on VP2410](https://github.com/Dasharo/dasharo-issues/issues/99)
    - [S3 resume does not work in Geminilake FSP](https://github.com/Dasharo/dasharo-issues/issues/27)

    ### Binaries

    [protectli_vp2410_v1.1.0.rom][protectli_vp2410_v1.1.0.rom_file]{.md-button}
    [sha256][protectli_vp2410_v1.1.0.rom_hash]{.md-button}
    [sha256.sig][protectli_vp2410_v1.1.0.rom_sig]{.md-button}

    To verify binary integrity with hash and signature please follow the
    instructions in [Dasharo release signature verification](/guides/signature-verification)
    using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/dasharo-release-1.1.x-for-protectli-signing-key.asc)

    ### SBOM (Software Bill of Materials)

    - [Dasharo coreboot fork based on 4.21 revision 2d96eeb7](https://github.com/Dasharo/coreboot/tree/2d96eeb7)
    - [Dasharo EDKII fork based on edk2-stable202002 revision ae0ce3e2](https://github.com/Dasharo/edk2/tree/ae0ce3e2)
    - [iPXE based on 2023.12 revision 838611b3](https://github.com/Dasharo/ipxe/tree/838611b3)
    - [vboot based on 0c11187c75 revision 0c11187c](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/0c11187c/)
    - [Intel Management Engine/Trusted Execution Engine based on v4.0.50.2083 revision 06bbd2a0](https://github.com/Dasharo/dasharo-blobs/blob/06bbd2a0/protectli/vault_glk/ifwi.bin)
    - [Intel Flash Descriptor based on v1.0 revision 06bbd2a0](https://github.com/Dasharo/dasharo-blobs/blob/06bbd2a0/protectli/vault_glk/descriptor.bin)
    - [Intel Firmware Support Package based on GLK v2.2.1.3.2 revision 06bbd2a0](https://github.com/Dasharo/dasharo-blobs/blob/06bbd2a0/protectli/vault_glk/GeminilakeFspBinPkg)
    - [Intel microcode based on GLK B0 0x0000003e revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-7a-01)
    - [Intel microcode based on GLK R0 0x00000022 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-7a-08)

    [newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
    [protectli_vp2410_v1.1.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.1.0/protectli_vp2410_v1.1.0.rom
    [protectli_vp2410_v1.1.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.1.0/protectli_vp2410_v1.1.0.rom.sha256
    [protectli_vp2410_v1.1.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.1.0/protectli_vp2410_v1.1.0.rom.sha256.sig

    ## v1.0.15 - 2022-05-31

    ### Changed

    - Customized Network boot menu and strings

    ### Fixed

    - SMBIOS memory information showing 0 MB DRAM in setup

    ### Known issues

    - [USB 2.0 sticks not detected on VP2410](https://github.com/Dasharo/dasharo-issues/issues/99)
    - [S3 resume does not work in Geminilake FSP](https://github.com/Dasharo/dasharo-issues/issues/27)

    ### Binaries

    [protectli_VP2410_DF_v1.0.15.rom][v1.0.15_rom]{.md-button}
    [sha256][v1.0.15_hash]{.md-button}
    [sha256.sig][v1.0.15_sig]{.md-button}

    To verify binary integrity with hash and signature please follow the
    instructions in [Dasharo release signature verification](/guides/signature-verification)
    using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/protectli-dasharo-firewall-release-1.0-key.asc)

    ### SBOM (Software Bill of Materials)

    - [coreboot based on b77cf229 revision f59b1ec9](https://github.com/Dasharo/coreboot/tree/f59b1ec9)
    - [edk2 based on 7f90b9cd revision 90364638](https://github.com/Dasharo/edk2/tree/90364638)
    - [iPXE for EFI revision 988d2](https://github.com/ipxe/ipxe/tree/988d2c13cdf0f0b4140685af35ced70ac5b3283c)
    - FSP: Custom version based on Intel GeminiLake FSP 2.2.1.3
    - Management Engine: Custom image based on CSE 4.0.30.1392
    - microcode:
        + CPU signature: 0x0706A8, Date: 09.06.2020, Revision: 0x18
        + CPU signature: 0x0706A0, Date: 12.07.2017, Revision: 0x26
        + CPU signature: 0x0706A1, Date: 09.06.2020, Revision: 0x34

    [newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
    [v1.0.15_rom]: https:/3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.0.15/protectli_vault_glk_v1.0.15.rom
    [v1.0.15_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.0.15/protectli_vault_glk_v1.0.15.rom.sha256
    [v1.0.15_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.0.15/protectli_vault_glk_v1.0.15.rom.sha256.sig

=== "vp2420"
    Following Release Notes describe status of open-source firmware development for
    Protectli VP2420 family.

    For details about our release process please read
    [Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

    <center>
    [Subscribe to Protectli VP2420 Dasharo Release Newsletter]
    [newsletter]{.md-button .md-button--primary .center}
    </center>

    Test results for this platform can be found
    [here](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit#gid=270990532).

    ## v1.2.0 - 2024-05-16

    ### Added

    - [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
    - [Serial port console redirection option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#serial-port-configuration)
    - [Customizable Serial Number and UUID via CBFS support](https://github.com/Dasharo/dcu)
    - [Customizable boot logo support](https://github.com/Dasharo/dcu)
    - [Support for taking screenshots in the firmware](https://docs.dasharo.com/dev-proc/screenshots/#taking-screenshots)
    - [ESP partition scanning in look for grubx64.efi or shimx64.efi or Windows bootmgr](https://github.com/Dasharo/dasharo-issues/issues/94)
    - Microsoft and Windows 2023 UEFI Secure Boot certificates
    - UEFI 2.8 errata C compliance in EDKII fork

    ### Changed

    - Rebased to coreboot 4.21
    - Enroll default UEFI Secure Boot keys on the first boot
    - [Improved UEFI Secure Boot menu user experience](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
    - Scope of reset to defaults hotkey to global in firmware setup
    - Updated microcode to the newer version; refer to SBOM section below
    - Updated ME to the newer version; refer to SBOM section below

    ### Fixed

    - [Auto Boot Time-out is reset to 0 when F9 is pressed](https://github.com/Dasharo/dasharo-issues/issues/513)
    - [Reset to defaults with F9 causes the wrong settings to be restored](https://github.com/Dasharo/dasharo-issues/issues/355)
    - [RTC time and date resetting to the coreboot build date on 29th February](https://review.coreboot.org/c/coreboot/+/80790)
    - [Cannot set custom bootsplash in firmware via DCU nor cbfstool](https://github.com/Dasharo/dasharo-issues/issues/759)

    ### Binaries

    [protectli_vp2420_v1.2.0.rom][protectli_vp2420_v1.2.0.rom_file]{.md-button}
    [sha256][protectli_vp2420_v1.2.0.rom_hash]{.md-button}
    [sha256.sig][protectli_vp2420_v1.2.0.rom_sig]{.md-button}

    [protectli_vp2420_v1.2.0_dev_signed.rom][protectli_vp2420_v1.2.0_dev_signed.rom_file]{.md-button}
    [sha256][protectli_vp2420_v1.2.0_dev_signed.rom_hash]{.md-button}
    [sha256.sig][protectli_vp2420_v1.2.0_dev_signed.rom_sig]{.md-button}

    To verify binary integrity with hash and signature please follow the
    instructions in [Dasharo release signature verification](/guides/signature-verification)
    using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/dasharo-release-1.2.x-for-protectli-signing-key.asc)

    ### SBOM (Software Bill of Materials)

    - [Dasharo coreboot fork based on 4.21 revision 7c2c79e8](https://github.com/Dasharo/coreboot/tree/7c2c79e8)
    - [Dasharo EDKII fork based on edk2-stable202002 revision ae0ce3e2](https://github.com/Dasharo/edk2/tree/ae0ce3e2)
    - [iPXE based on 2023.12 revision 838611b3](https://github.com/Dasharo/ipxe/tree/838611b3)
    - [vboot based on 0c11187c75 revision 0c11187c](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/0c11187c/)
    - [Intel Management Engine based on v15.40.32.2910 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/protectli/vault_ehl/me.bin)
    - [Intel Flash Descriptor based on v1.0 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/protectli/vault_ehl/descriptor.bin)
    - [Intel Firmware Support Package based on Elkhart Lake MR6 revision 481ea7cf](https://github.com/intel/FSP/tree/481ea7cf/ElkhartLakeFspBinPkg/)
    - [Intel microcode based on EHL B1 0x00000016 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-96-01)

    [protectli_vp2420_v1.2.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.0/protectli_vp2420_v1.2.0.rom
    [protectli_vp2420_v1.2.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.0/protectli_vp2420_v1.2.0.rom.sha256
    [protectli_vp2420_v1.2.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.0/protectli_vp2420_v1.2.0.rom.sha256.sig
    [protectli_vp2420_v1.2.0_dev_signed.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.0/protectli_vp2420_v1.2.0_dev_signed.rom
    [protectli_vp2420_v1.2.0_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.0/protectli_vp2420_v1.2.0_dev_signed.rom.sha256
    [protectli_vp2420_v1.2.0_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.2.0/protectli_vp2420_v1.2.0_dev_signed.rom.sha256.sig

    ## v1.1.0 - 2023-04-20

    ### Added

    - [USB stack and mass storage enable/disable option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
    - [SMM BIOS write protection enable/disable option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)

    ### Changed

    - [Updating from v1.0.x requires flashing the WP_RO recovery partition](../protectli_vp2420/firmware-update.md#updating-minor-versions-v1xy)
    - [Firmware version v1.1.x are signed with a new key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/dasharo-release-1.1.x-for-protectli-signing-key.asc)
    - [Keys must be provisioned prior enabling Secure Boot](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)

    ### Fixed

    - [VP2420 memory issues and incorrectly reported memory capacity](https://github.com/Dasharo/dasharo-issues/issues/397)
    - [Popup with information about recovery mode is still displayed after flashing with a valid binary](https://github.com/Dasharo/dasharo-issues/issues/320)

    ### Known issues

    - [pfSense boot time](https://github.com/Dasharo/dasharo-issues/issues/318)
    - [Double characters in pfSense initial boot phase](https://github.com/Dasharo/dasharo-issues/issues/319)

    ### Binaries

    [protectli_vp2420_v1.1.0.rom][protectli_vp2420_v1.1.0.rom_file]{.md-button}
    [sha256][protectli_vp2420_v1.1.0.rom_hash]{.md-button}
    [sha256.sig][protectli_vp2420_v1.1.0.rom_sig]{.md-button}

    To verify binary integrity with hash and signature please follow the
    instructions in [Dasharo release signature verification](/guides/signature-verification)
    using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/dasharo-release-1.1.x-for-protectli-signing-key.asc)

    ### SBOM (Software Bill of Materials)

    - [coreboot based on c86c926 revision e36a117d](https://github.com/Dasharo/coreboot/tree/e36a117d)
    - [edk2 based on 7f90b9cd revision 19bf14b4](https://github.com/Dasharo/edk2/tree/19bf14b4)

    [newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
    [protectli_vp2420_v1.1.0.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.1.0/protectli_vp2420_v1.1.0.rom
    [protectli_vp2420_v1.1.0.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.1.0/protectli_vp2420_v1.1.0.rom.sha256
    [protectli_vp2420_v1.1.0.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.1.0/protectli_vp2420_v1.1.0.rom.sha256.sig

    ## v1.0.1 - 2023-02-02

    ### Added

    - [TPM 2.0 support over SPI interface](https://docs.dasharo.com/unified-test-documentation/dasharo-security/200-tpm-support/#test-cases-common-documentation)
    - [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)

    ### Changed

    - Downgrade edk2 Secure Boot driver to achieve consistent user experience as on
    the VP46XX v1.0.19 release

    ### Fixed

    - [Dasharo BIOS lock menu is missing](https://github.com/Dasharo/dasharo-issues/issues/291)
    - [iPXE entry doesn't occur in setup menu](https://github.com/Dasharo/dasharo-issues/issues/289)
    - [Impossibility of pfSense/OPNsense console versions installation](https://github.com/Dasharo/dasharo-issues/issues/289)

    ### Known issues

    - [Popup with information about recovery mode is still displayed after flashing with a valid binary](https://github.com/Dasharo/dasharo-issues/issues/320)
    - [pfSense boot time](https://github.com/Dasharo/dasharo-issues/issues/318)
    - [Double characters in pfSense initial boot phase](https://github.com/Dasharo/dasharo-issues/issues/319)

    ### Binaries

    [protectli_vp2420_v1.0.1.rom][protectli_vp2420_v1.0.1.rom_file]{.md-button}
    [sha256][protectli_vp2420_v1.0.1.rom_hash]{.md-button}
    [sha256.sig][protectli_vp2420_v1.0.1.rom_sig]{.md-button}

    To verify binary integrity with hash and signature please follow the
    instructions in [Dasharo release signature verification](/guides/signature-verification)
    using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/protectli-dasharo-firewall-release-1.0-key.asc)

    ### SBOM (Software Bill of Materials)

    - [coreboot based on c86c926 revision 54cbbc5b](https://github.com/Dasharo/coreboot/tree/54cbbc5b)
    - [edk2 based on 7f90b9cd revision e31b7a71](https://github.com/Dasharo/edk2/tree/e31b7a71)

    [newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
    [protectli_vp2420_v1.0.1.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.1/protectli_vp2420_v1.0.1.rom
    [protectli_vp2420_v1.0.1.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.1/protectli_vp2420_v1.0.1.rom.sha256
    [protectli_vp2420_v1.0.1.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.1/protectli_vp2420_v1.0.1.rom.sha256.sig

    ## v1.0.0 - 2022-12-22

    ### Added

    - Support for VP2420 platform
    - [Vboot Verified Boot](https://docs.dasharo.com/guides/vboot-signing/)
    - [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
    - [Vboot recovery notification in UEFI Payload](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)
    - [UEFI Shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
    - [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
    - [BIOS flash protection for Vboot recovery region](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20J-bios-lock-support/)
    - UEFI boot support
    - Intel i225 controller network boot support
    - Customized boot menu keys
    - Customized setup menu keys
    - Configurable boot order
    - Configurable boot options

    ### Binaries

    [protectli_VP2420_v1.0.0.rom][v1.0.0_rom]{.md-button}
    [sha256][v1.0.0_hash]{.md-button}
    [sha256.sig][v1.0.0_sig]{.md-button}

    How to verify signatures:

    ```bash
    wget https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom
    wget https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256
    wget https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256.sig
    gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc
    gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/3mdeb-dasharo-master-key.asc
    gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/protectli-dasharo-firewall-release-1.0-key.asc
    gpg --list-sigs "3mdeb Master Key" "3mdeb Dasharo Master Key" "Protectli Dasharo Firewall Release 1.0 Signing Key"
    sha256sum -c protectli_vp2420_v1.0.0.rom.sha256
    gpg -v --verify protectli_vp2420_v1.0.0.rom.sha256.sig protectli_vp2420_v1.0.0.rom.sha256
    ```

    ### SBOM (Software Bill of Materials)

    - [coreboot based on c492b427 revision c86c9266](https://github.com/Dasharo/coreboot/tree/c86c9266)
    - [edk2 based on e461f08 revision 7948a20](https://github.com/Dasharo/edk2/tree/7948a20)
    - [iPXE for EFI revision 988d2](https://github.com/ipxe/ipxe/tree/988d2c13cdf0f0b4140685af35ced70ac5b3283c)

    [newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
    [v1.0.0_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom
    [v1.0.0_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256
    [v1.0.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256.sig
