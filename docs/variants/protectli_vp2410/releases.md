# Protectli VP2410 Dasharo Release Notes

Following Release Notes describe status of open-source firmware development
for Protectli VP2410.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("49abc4a2-0807-4720-aef2-b150ef701b30",
"Subscribe to Protectli Dasharo Release Newsletter") }}

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit#gid=1033426620).

> The missing versions before v1.0.15 were assigned to different platforms
> interchangeably. See [Protectli FW6 releases](../protectli_fw6/releases.md)
> and [Protectli VP46XX releases](../protectli_vp46xx/releases.md).

## v1.1.1 - 2025-01-23

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/Protectli/VP2410/v1.1.1-results.csv).

### Added

- [CPU throttling option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Power state after AC loss option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)

### Changed

- Rebased coreboot to 24.02
- Rebased edk2 to edk2-stable202405

### Known issues

- [VP2410 does not power on after shutting down with power button 4s override](https://github.com/Dasharo/dasharo-issues/issues/643)
- [USB 2.0 sticks not detected on VP2410](https://github.com/Dasharo/dasharo-issues/issues/99)
- [S3 resume does not work in Geminilake FSP](https://github.com/Dasharo/dasharo-issues/issues/27)

### Binaries

[protectli_vp2410_v1.1.1.rom][protectli_vp2410_v1.1.1.rom_file]{.md-button}
[sha256][protectli_vp2410_v1.1.1.rom_hash]{.md-button}
[sha256.sig][protectli_vp2410_v1.1.1.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/dasharo-release-1.1.x-for-protectli-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 24.02 revision 001d6f77](https://github.com/Dasharo/coreboot/tree/001d6f77)
    + [License](https://github.com/Dasharo/coreboot/blob/001d6f77/COPYING)
- [Dasharo EDKII fork based on edk2-stable202405 revision 8a9fd05f](https://github.com/Dasharo/edk2/tree/8a9fd05f)
    + [License](https://github.com/Dasharo/edk2/blob/8a9fd05f/License.txt)
- [iPXE based on 2023.12 revision 35d84756](https://github.com/Dasharo/ipxe/tree/35d84756)
    + [License](https://github.com/Dasharo/ipxe/blob/35d84756/COPYING.GPLv2)
- [vboot based on 3d37d2aafe revision 3d37d2aa](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/LICENSE)
- [Intel Management Engine/Trusted Execution Engine version v4.0.50.2083](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/protectli/vault_glk/ifwi.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/protectli/vault_glk/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version GLK v2.2.1.3.2](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/protectli/vault_glk/GeminilakeFspBinPkg)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/cc9465c1/licenses/INTEL_FSP_SIC_LICENSE.txt)
- [Intel microcode version GLK B0 0x42 19/04/2024](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240531/intel-ucode/06-7a-01)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240531/license)
- [Intel microcode version GLK R0 0x24 25/08/2023](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20240531/intel-ucode/06-7a-08)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20240531/license)

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
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
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

## v1.0.15 - 2022-05-31

### Added

- Initial support for the Protectli VP2410 platform
- TPM2 support
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [UEFI compatibility](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface/)
- [Protectli boot logo](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/304-custom-logo/)
- [UEFI shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
- Customized Network boot menu and strings
- [Dasharo SMBIOS compatibility](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31L-smbios/)
- [USB 2.0 sticks support](https://github.com/Dasharo/dasharo-issues/issues/99)
- [S3 resume](https://github.com/Dasharo/dasharo-issues/issues/27)

### Binaries

[protectli_VP2410_DF_v1.0.15.rom][v1.0.15_rom]{.md-button}
[sha256][v1.0.15_hash]{.md-button}
[sha256.sig][v1.0.15_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
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

[protectli_vp2410_v1.1.1.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.1.1/protectli_vp2410_v1.1.1.rom
[protectli_vp2410_v1.1.1.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.1.1/protectli_vp2410_v1.1.1.rom.sha256
[protectli_vp2410_v1.1.1.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.1.1/protectli_vp2410_v1.1.1.rom.sha256.sig
[protectli_vp2410_v1.1.0.rom_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.1.0/protectli_vp2410_v1.1.0.rom
[protectli_vp2410_v1.1.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.1.0/protectli_vp2410_v1.1.0.rom.sha256
[protectli_vp2410_v1.1.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.1.0/protectli_vp2410_v1.1.0.rom.sha256.sig
[v1.0.15_rom]: https:/3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.0.15/protectli_vault_glk_v1.0.15.rom
[v1.0.15_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.0.15/protectli_vault_glk_v1.0.15.rom.sha256
[v1.0.15_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.0.15/protectli_vault_glk_v1.0.15.rom.sha256.sig

## v1.0.10 - 2021-09-29

### Changed

- Update ME image to fix VR issues

### SBOM (Software Bill of Materials)

- [coreboot based on 4.13 revision a4cd9117](https://github.com/Dasharo/coreboot/compare/a4cd9117...protectli_vault_glk_v1.0.10)
- [Dasharo UEFI based on TianoCore EDK2 edk2-stable202011](https://github.com/Dasharo/edk2/compare/dd7523b5b123de6f0730f2f2abb207f2a5c1ccd4...615f9f4b67876df08dcf872d311dd73884a449e3)
- [EFI iPXE 1.20.1+ (g9b25)](https://github.com/ipxe/ipxe/commit/9b25f6e5cf517f426de80ede618398ef01e385f9)

## v1.0.9 - 2021-07-20

### Changed

- SMBIOS Product name to VP2410
- UEFI Setup key changed to DEL

### Fixed

- USB detection issues

### SBOM (Software Bill of Materials)

- [coreboot based on 4.13 revision a4cd9117](https://github.com/Dasharo/coreboot/compare/a4cd9117...protectli_vault_glk_v1.0.9)
- [Dasharo UEFI based on TianoCore EDK2 edk2-stable202011](https://github.com/Dasharo/edk2/compare/dd7523b5b123de6f0730f2f2abb207f2a5c1ccd4...615f9f4b67876df08dcf872d311dd73884a449e3)
- [EFI iPXE 1.20.1+ (g9b25)](https://github.com/ipxe/ipxe/commit/9b25f6e5cf517f426de80ede618398ef01e385f9)

## v1.0.8 - 2021-05-28

### Added

- UEFI compatible interface
- iPXE network boot
- UEFI Shell
- TPM2 menu
- UEFI Measured Boot
- Persistent boot options

### Fixed

- [The VGA text mode console does not work in SeaBIOS.](https://github.com/Dasharo/dasharo-issues/issues/13)
  UEFI graphics works well.
- [VT-d (IOMMU) is not being correctly configured by FSP.](https://github.com/Dasharo/dasharo-issues/issues/14)
- Flashrom did not support Geminilake chipset. The upstream support is already there.
- [Fastboot is not yet working.](https://github.com/Dasharo/dasharo-issues/issues/15)
  FSP fastboot has been fixed to work with coreboot
- [Display does not work in FreeBSD and other BSD systems](https://github.com/Dasharo/dasharo-issues/issues/16)
  UEFI graphics works in FreeBSD.
- [Linux reports non-working TPM interrupt.](https://github.com/Dasharo/dasharo-issues/issues/12)

### Known issues

- USB keyboard cannot wake platform from S3 suspend. This s a limitation of the
  hardware design which routes only 5V power supply available in full powered
  state. Waking the platform from S3 state is only possible with power button
  and Wake-on-LAN.
- [S3 resume does not work in FSP](https://github.com/Dasharo/dasharo-issues/issues/27).
  For power saving it is recommended to use modern S0 idle states, aka s2idle
  as explained in the [Linux kernel documentation](https://www.kernel.org/doc/html/v5.0/admin-guide/pm/sleep-states.html).
  S0 idle is known to be more efficient in saving power. Additionally the
  keyboard can wake the platform from s2idle state since the power is not cut
  off from USB devices in this state.

### SBOM (Software Bill of Materials)

- [coreboot based on 4.13 revision a4cd9117](https://github.com/Dasharo/coreboot/compare/a4cd9117...protectli-firewall-1.0.8)
- [Dasharo UEFI based on TianoCore EDK2 edk2-stable202011](https://github.com/Dasharo/edk2/compare/dd7523b5b123de6f0730f2f2abb207f2a5c1ccd4...615f9f4b67876df08dcf872d311dd73884a449e3)
- [EFI iPXE 1.20.1+ (g9b25)](https://github.com/ipxe/ipxe/commit/9b25f6e5cf517f426de80ede618398ef01e385f9)

## 1.0.3-rc1 - 2021-03-19 (Engineering release)

### Added

- Initial support for Protectli Vault FW4 Geminilake platform

### Fixed

- SeaBIOS: change handling the CBFS pointer to correctly detect CBFS location
  on Apollolake and Geminilake platforms

### Known issues

- [The VGA text mode console does not work in SeaBIOS.](https://github.com/Dasharo/dasharo-issues/issues/13)
  SeaBIOS does not print boot menu prompt and boot options. Only serial console
  redirection and graphical logo works.
- [VT-d (IOMMU) is not being correctly configured by FSP.](https://github.com/Dasharo/dasharo-issues/issues/14)
- Flashrom does not support Geminilake chipset.
- [Fastboot is not yet working.](https://github.com/Dasharo/dasharo-issues/issues/15)
  It makes the boot process longer due to full memory training on each boot.
- [Since VGA text mode console doesn't yet work.](https://github.com/Dasharo/dasharo-issues/issues/16)
  FreeBSD can only be accessed on serial console.
- [Linux reports non-working TPM interrupt.](https://github.com/Dasharo/dasharo-issues/issues/12)

### SBOM (Software Bill of Materials)

- [coreboot based on 4.13 revision a4cd9117](https://github.com/Dasharo/coreboot/compare/a4cd9117...protectli-firewall-1.0.3-rc1)
- [SeaBIOS v1.0.8 based on rel-1.12.1 revision 171fc897](https://github.com/Dasharo/SeaBIOS/compare/171fc897...v1.0.8)
- [iPXE 2019.3 stable revision ebf2eaf5](https://github.com/ipxe/ipxe/commits/ebf2eaf5)
