# ASRock Rack SPC741D8-2L2T/BCM Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development
for ASRock Rack SPC741D8-2L2T/BCM.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

We gratefully acknowledge the [https://os.itec.kit.edu](https://os.itec.kit.edu)
(Operating Systems Group) at Karlsruhe Institute of Technology (Fabian Meyer,
Felix Zimmer, Yussuf Khalil) for their contribution in initiating the coreboot
port for this platform and supporting open-source firmware development.

{{ subscribe_form("5c8e048b-0cc1-4ae0-95c2-5e27c7453849",
"Subscribe to ASRock Rack SPC741D8-2L2T/BCM Dasharo Release Newsletter") }}

Motherboards with Dasharo preinstalled can be purchased
[here](https://shop.3mdeb.com/product/asrock-spc741d8-2l2t-bcm-dasharo-pro/).
Full server builds can be purchased
[here](https://shop.3mdeb.com/product/asrock-spc741d8-2l2t-bcm-dasharo-pro-full-build/).

## v0.9.1 - 2026-10-14

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/ASRock/SPC741D8-2L2T-BCM/).

### Added

- [Intel TXT](https://docs.dasharo.com/guides/intel-txt/)
- Intel Emerald Rapids CPU Support
- [PCIe Bifurcation](https://docs.dasharo.com/dasharo-menu-docs/platform-setup-menu/#pcie-bifurcation)
- [Intel SMI Transfer Monitor (STM)](https://docs.dasharo.com/guides/smi-transfer-monitor/)
- Embedded Software Bill of Materials (SBoM)

### Fixed

- [DCU custom boot logo is not displayed](https://github.com/Dasharo/dasharo-issues/issues/1629)
- [TPM PPI does not work](https://github.com/Dasharo/dasharo-issues/issues/1602)
- [Long boot time](https://github.com/Dasharo/dasharo-issues/issues/1585)

### Known issues

- [Intruder switch significantly slows platform down when active](https://github.com/Dasharo/dasharo-issues/issues/1933)
- [TXT HEAP and SINIT memory ranges not reserved](https://github.com/Dasharo/dasharo-issues/issues/1936)
- [USB mass storage devices not detected after warmboot or reboot](https://github.com/Dasharo/dasharo-issues/issues/1935)
- [SINIT ACM does not perform a measurement of an STM](https://github.com/Dasharo/dasharo-issues/issues/1934)
- [Errors and unexpected messages printed during boot](https://github.com/Dasharo/dasharo-issues/issues/1609)
- [Invalid PCR 1, 2, 7 reconstruction](https://github.com/Dasharo/dasharo-issues/issues/1608)
- [Immediate BSOD trying to boot Windows](https://github.com/Dasharo/dasharo-issues/issues/1598)
- [Large ME region size](https://github.com/Dasharo/dasharo-issues/issues/1586)
- [STB002.001 encounters unlisted error](https://github.com/Dasharo/dasharo-issues/issues/1013)

### Binaries

[sha256][asrock_spc741d8_v0.9.1.rom_hash]{.md-button}
[sha256.sig][asrock_spc741d8_v0.9.1.rom_sig]{.md-button}
(asrock_spc741d8_v0.9.1.rom)
[asrock_spc741d8_v0.9.1.sbom.json][asrock_spc741d8_v0.9.1.sbom.json_file]{.md-button}
[sha256][asrock_spc741d8_v0.9.1.sbom.json_hash]{.md-button}
[sha256.sig][asrock_spc741d8_v0.9.1.sbom.json_sig]{.md-button}
[sha256][asrock_spc741d8_v0.9.1_btg_devel.rom_hash]{.md-button}
[sha256.sig][asrock_spc741d8_v0.9.1_btg_devel.rom_sig]{.md-button}
(asrock_spc741d8_v0.9.1_btg_devel.rom)
[sha256][asrock_spc741d8_v0.9.1_txt.rom_hash]{.md-button}
[sha256.sig][asrock_spc741d8_v0.9.1_txt.rom_sig]{.md-button}
(asrock_spc741d8_v0.9.1_txt.rom)

This is a Dasharo Pro Package release. For this platform, access to pre-built
binaries is provided exclusively through the
[Full Build for ASRock Rack SPC741D8-2L2T/BCM](https://shop.3mdeb.com/product/dasharo-corebootuefi-pro-package-for-servers/),
a bundled hardware-and-firmware product available in
the 3mdeb shop. A standalone Dasharo Pro Package subscription is not offered
for this platform.

With the Full Build, you receive firmware updates for the duration of your
subscription via the Dasharo Pro Package newsletter, and gain entry to the
Dasharo Premier Support invite-only live chat on the Matrix network, enabling
direct engagement with the Dasharo Team and fellow subscribers for
personalized, priority assistance.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/refs/heads/master/dasharo/asrock_spc741d8/dasharo-release-0.x-compatible-with-asrock-spc741d8-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.12 revision 62592a4f](https://github.com/Dasharo/coreboot/tree/62592a4f)
- [Dasharo EDKII fork based on edk2-stable202502 revision bdb92c0e](https://github.com/Dasharo/edk2/tree/bdb92c0e)
- [Dasharo iPXE fork based on 2025.03 revision ad8cbcee](https://github.com/Dasharo/ipxe/tree/ad8cbcee)
    + [License](https://github.com/Dasharo/ipxe/blob/ad8cbcee/COPYING.GPLv2)
- [Intel Firmware Support Package for Eagle Stream version 0115.D.05](https://github.com/intel/FSP/tree/7cb9638a/EagleStreamFspBinPkg)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Server Platform Services version v6.1.4.89.0](https://github.com/Dasharo/dasharo-blobs/blob/69f6817e/asrock/spc741d8/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/69f6817e/asrock/spc741d8/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel microcode version SPR-HBM 0x2c000435 02/03/2026](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20250812/intel-ucode/06-8f-08)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20250812/license)
- [Intel microcode version SPR-SP 0x210002f4 02/03/2026](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20250812/intel-ucode/06-cf-02)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20250812/license)

An [integrated SBOM](https://doc.coreboot.org/sbom/sbom.html) is also
included in the firmware images. It describes a complete set of components
and their versions used to build the firmware images. The published SBOM
artifact is in CycloneDX format and can be viewed by SBOM tools, for example
[sbom-tools](https://github.com/sbom-tool/sbom-tools).

### CRA compliance

CRA compliance status generated with [sbom-tools](https://github.com/sbom-tool/sbom-tools)

#### Phase 2

```text
EU CRA Phase 2 (2029)
COMPLIANT — With warnings
Security  █████████████████████████░░░░░░░░░░░░░░░     5 (62.5%)
Doc Meta  ██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     2 (25.0%)
Integrity █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     1 (12.5%)
```

[asrock_spc741d8_v0.9.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.1/asrock_spc741d8_v0.9.1.rom.sha256
[asrock_spc741d8_v0.9.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.1/asrock_spc741d8_v0.9.1.rom.sha256.sig
[asrock_spc741d8_v0.9.1.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.1/asrock_spc741d8_v0.9.1.sbom.json
[asrock_spc741d8_v0.9.1.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.1/asrock_spc741d8_v0.9.1.sbom.json.sha256
[asrock_spc741d8_v0.9.1.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.1/asrock_spc741d8_v0.9.1.sbom.json.sha256.sig
[asrock_spc741d8_v0.9.1_btg_devel.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.1/asrock_spc741d8_v0.9.1_btg_devel.rom.sha256
[asrock_spc741d8_v0.9.1_btg_devel.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.1/asrock_spc741d8_v0.9.1_btg_devel.rom.sha256.sig
[asrock_spc741d8_v0.9.1_txt.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.1/asrock_spc741d8_v0.9.1_txt.rom.sha256
[asrock_spc741d8_v0.9.1_txt.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.1/asrock_spc741d8_v0.9.1_txt.rom.sha256.sig

## v0.9.0 - 2025-09-18

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/ASRock/SPC741D8-2L2T-BCM/).

### Added

- Initial support for the ASRock Rack SPC741D8-2L2T/BCM platform
- [UEFI compatible interface](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface/)
- [Support for discrete TPM](https://docs.dasharo.com/unified-test-documentation/dasharo-security/200-tpm-support/)
- [UEFI Secure Boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [Boot logo customization support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/328-logo-customization-functionality/)
- [USB boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31N-usb-boot/)
- [NVMe boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/312-nvme-support/)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [Network boot](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/315b-netboot-utilities/)
- [Ubuntu LTS booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support/)
- [Serial port console redirection](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31G-ec-and-superio/#sio004001-serial-port-in-firmware)
- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#user-password-management)
- [SMM BIOS write protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Network stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#networking-options)
- [SED/OPAL disk password support](https://www.github.com/dasharo/dasharo-issues/issues/161)

### Known issues

- [Large ME region size](https://github.com/Dasharo/dasharo-issues/issues/1586)
- [Long boot time](https://github.com/Dasharo/dasharo-issues/issues/1585)
- [STB002.001 encounters unlisted error](https://github.com/Dasharo/dasharo-issues/issues/1013)
- [Invalid PCR reconstruction](https://github.com/Dasharo/dasharo-issues/issues/1608)
- [Immediate BSOD trying to boot Windows](https://github.com/Dasharo/dasharo-issues/issues/1598)
- [Errors and unexpected messages printed during boot](https://github.com/Dasharo/dasharo-issues/issues/1609)
- [SecureBoot can't boot file signed with custom PK](https://github.com/Dasharo/dasharo-issues/issues/1610)
- [TPM PPI does not work](https://github.com/Dasharo/dasharo-issues/issues/1602)
- [DCU custom boot logo is not displayed](https://github.com/Dasharo/dasharo-issues/issues/1629)

### Binaries

[sha256][asrock_spc741d8_v0.9.0.rom_hash]{.md-button}
[sha256.sig][asrock_spc741d8_v0.9.0.rom_sig]{.md-button}
(asrock_spc741d8_v0.9.0.rom)

This is a Dasharo Pro Package Release. To access the pre-built binaries,
you need to [subscribe to the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our
[shop](https://shop.3mdeb.com/product/asrock-spc741d8-2l2t-bcm-dasharo-pro-full-build/).
As a subscriber, you will receive access to all firmware updates for the
duration of your subscription via the Dasharo Pro Package newsletter, and
gain entry to the Dasharo Premier Support invite-only live chat on the Matrix
network, enabling direct engagement with the Dasharo Team and fellow
subscribers for personalized, priority assistance.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/refs/heads/master/dasharo/asrock_spc741d8/dasharo-release-0.x-compatible-with-asrock-spc741d8-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.03 revision cee8ddf3](https://github.com/Dasharo/coreboot/tree/cee8ddf3)
- [Dasharo EDKII fork based on edk2-stable202502 revision 22333c9e](https://github.com/Dasharo/edk2/tree/22333c9e)
- [Dasharo iPXE fork based on 2025.03 revision 6c7068fc](https://github.com/Dasharo/ipxe/tree/6c7068fc)
    + [License](https://github.com/Dasharo/ipxe/blob/6c7068fc/COPYING.GPLv2)
- [Intel Firmware Support Package for Eagle Stream version 0115.D.05](https://github.com/intel/FSP/tree/5d0424c8/EagleStreamFspBinPkg)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Server Platform Services version v6.1.4.89.0](https://github.com/Dasharo/dasharo-blobs/blob/8dce7604/asrock/spc741d8/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/8dce7604/asrock/spc741d8/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel microcode version SPR-HBM 0x2c000401 08/04/2025](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20250812/intel-ucode/06-8f-08)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20250812/license)
- [Intel microcode version SPR-SP 0x210002b3 15/04/2025](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20250812/intel-ucode/06-cf-02)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20250812/license)

[asrock_spc741d8_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.0/asrock_spc741d8_v0.9.0.rom.sha256
[asrock_spc741d8_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.0/asrock_spc741d8_v0.9.0.rom.sha256.sig
