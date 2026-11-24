# MSI PRO Z790-P (WIFI) (DDR5) Dasharo Release Notes

This is a Dasharo Pro Package Release. To obtain access to the pre-built binaries,
you need to [subscribe to the Dasharo Pro Package subscriber](https://docs.dasharo.com/ways-you-can-help-us/#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our [shop](https://shop.3mdeb.com/shop/dasharo-pro-package/1year-desktop/).
As a subscriber, you will receive access to all firmware updates for the
duration of your subscription via the Dasharo Pro Package newsletter,
and gain entry to the Dasharo Premier Support invite-only live chat
on the Matrix network, enabling direct engagement with the Dasharo Team
and fellow subscribers for personalized, priority assistance.

Following Release Notes describe status of open-source firmware development for
MSI PRO Z790-P (WIFI) (DDR5)

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

For detailed information on our validation setup, please refer to the
[Hardware Configuration Matrix](hardware-matrix.md). To gain a deeper
understanding of the nomenclature reasons behind the Z690/Z790 boards, we
recommend seeing our [FAQ](../../unified/msi/faq.md).

{{ subscribe_form("b7d54f08-baae-4762-9ce2-c1df12bdca58",
"Subscribe to MSI PRO Z790-P (WIFI) (DDR5) Dasharo Release Newsletter") }}

## v0.9.6 - 2026-11-24

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/msi/ms7e06/v0.9.6-results.csv).

### Added

- USB port power configuration option
- USB wake support
- Quiet boot/Fast boot options
- Dasharo ACPI driver support for temperature and fan monitoring

### Changed

- Updated CPU microcode (see SBOM)
- New settings in Platform Setup Menu now reset to platform-default value
  instead to zero and will show those values on first boot
- Per Regulation (EU) 2024/2847, Annex I, Part I, point (2)(b), enabling
  secure configuration by default - UEFI Secure Boot, SMM BWP, DMA protection.
  Users with discrete GPUs with unsigned optionROMs or optionROMs not
  respecting DMA protection and EDKII IOMMU protocol may stop giving graphical
  output in the firmware. Other add-on cards with insecure optionROMs may also
  be affected.

### Fixed

- [Incorrect DIMM SPD size causing DDR5 XMP training failure](https://github.com/Dasharo/dasharo-issues/issues/1923)
- [OS failing to boot with iGPU and dGPU](https://github.com/Dasharo/dasharo-issues/issues/1922)
- [CPU Turbo Boost not functional](https://github.com/Dasharo/dasharo-issues/issues/1919)
- [Firmware UI not stretched to full screen resolution](https://github.com/Dasharo/dasharo-issues/issues/1914)
- [Firmware unable to detect disks](https://github.com/Dasharo/dasharo-issues/issues/1913)
- PCI Enumeration Done IPC command incorrectly sent to PMC
- Incorrect PCI ASPM and Clock PM default settings

### Known issues

- [XMP1 profile does not boot in combination with some DDR5 configurations](https://github.com/Dasharo/dasharo-issues/issues/683)
- [Cannot wake from suspend via RTC on QubesOS](https://github.com/Dasharo/dasharo-issues/issues/484)
- [Windows 11 installer unable to detect i225 Ethernet NIC](https://github.com/Dasharo/dasharo-issues/issues/482)
- [Windows 11 VBS (Virtualization-based Security) appears Not enabled on System Information](https://github.com/Dasharo/dasharo-issues/issues/539)
- [Ubuntu fails to boot with early DMA protection Enabled](https://github.com/Dasharo/dasharo-issues/issues/1869)

### Binaries

[sha256][msi_ms7e06_v0.9.6_ddr4.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.6_ddr4.cap_sig]{.md-button}
(msi_ms7e06_v0.9.6_ddr4.cap)
[sha256][msi_ms7e06_v0.9.6_ddr4.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.6_ddr4.rom_sig]{.md-button}
(msi_ms7e06_v0.9.6_ddr4.rom)
[msi_ms7e06_v0.9.6_ddr4.sbom.json][msi_ms7e06_v0.9.6_ddr4.sbom.json_file]{.md-button}
[sha256][msi_ms7e06_v0.9.6_ddr4.sbom.json_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.6_ddr4.sbom.json_sig]{.md-button}
[sha256][msi_ms7e06_v0.9.6_ddr4_dev_signed.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.6_ddr4_dev_signed.cap_sig]{.md-button}
(msi_ms7e06_v0.9.6_ddr4_dev_signed.cap)
[sha256][msi_ms7e06_v0.9.6_ddr4_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.6_ddr4_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.6_ddr4_dev_signed.rom)
[sha256][msi_ms7e06_v0.9.6_ddr5.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.6_ddr5.cap_sig]{.md-button}
(msi_ms7e06_v0.9.6_ddr5.cap)
[sha256][msi_ms7e06_v0.9.6_ddr5.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.6_ddr5.rom_sig]{.md-button}
(msi_ms7e06_v0.9.6_ddr5.rom)
[msi_ms7e06_v0.9.6_ddr5.sbom.json][msi_ms7e06_v0.9.6_ddr5.sbom.json_file]{.md-button}
[sha256][msi_ms7e06_v0.9.6_ddr5.sbom.json_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.6_ddr5.sbom.json_sig]{.md-button}
[sha256][msi_ms7e06_v0.9.6_ddr5_dev_signed.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.6_ddr5_dev_signed.cap_sig]{.md-button}
(msi_ms7e06_v0.9.6_ddr5_dev_signed.cap)
[sha256][msi_ms7e06_v0.9.6_ddr5_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.6_ddr5_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.6_ddr5_dev_signed.rom)

This is a Dasharo Pro Package release. For this platform, access to pre-built
binaries is provided exclusively through the
[Full Build for MSI PRO Z790-P (WIFI) and PRO Z790-P (WIFI) DDR4](https://shop.3mdeb.com/product/1year-desktop/),
a bundled hardware-and-firmware product available in
the 3mdeb shop. A standalone Dasharo Pro Package subscription is not offered
for this platform.

With the Full Build, you receive firmware updates for the duration of your
subscription via the Dasharo Pro Package newsletter, and gain entry to the
Dasharo Premier Support invite-only live chat on the Matrix network, enabling
direct engagement with the Dasharo Team and fellow subscribers for
personalized, priority assistance.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7e06/dasharo-release-0.x-compatible-with-msi-ms-7e06-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.12 revision 39b88850](https://github.com/Dasharo/coreboot/tree/39b88850)
    + [License](https://github.com/Dasharo/coreboot/blob/39b88850/COPYING)
- [Dasharo EDKII fork based on edk2-stable202602 revision 0cacb9d1](https://github.com/Dasharo/edk2/tree/0cacb9d1)
    + [License](https://github.com/Dasharo/edk2/blob/0cacb9d1/License.txt)
- [Dasharo EDK2-platforms fork based on 1002a59639f111a2f8178b77d1f5fde0ea8d976f revision 4db2845d](https://github.com/Dasharo/edk2-platforms/tree/4db2845d)
    + [License](https://github.com/Dasharo/edk2-platforms/blob/4db2845d/License.txt)
- [iPXE based on ad8cbcee950840547f87394179a7e712e1c3c06f revision ad8cbcee](https://github.com/Dasharo/ipxe/tree/ad8cbcee)
    + [License](https://github.com/Dasharo/ipxe/blob/ad8cbcee/COPYING.GPLv2)
- [vboot based on 3f94e2c7ed revision 3f94e2c7](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3f94e2c7/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3f94e2c7/LICENSE)
- [Intel Management Engine version v16.1.30.2307](https://github.com/Dasharo/dasharo-blobs/blob/fbe0c65c/msi/ms7e06/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.2](https://github.com/Dasharo/dasharo-blobs/blob/fbe0c65c/msi/ms7e06/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version RPL-S C.0.C8.50](https://github.com/intel/FSP/tree/7cb9638a/RaptorLakeFspBinPkg/Client/RaptorLakeS)
    + [License](https://github.com/intel/FSP/blob/7cb9638a/FSP_License.pdf)
- [Intel microcode version ADL/RPL C0/H0 0x3e 12/10/2025](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20260925/intel-ucode/06-97-05)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20260925/license)
- [Intel microcode version RPL B0 0x137 18/02/2026](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20260925/intel-ucode/06-b7-01)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20260925/license)

An [integrated SBOM](https://doc.coreboot.org/sbom/sbom.html) is also
included in the firmware images. It describes a complete set of components
and their versions used to build the firmware images. The published SBOM
artifact is in CycloneDX format and can be viewed by SBOM tools, for example
[sbom-tools](https://github.com/sbom-tool/sbom-tools).

### Measured boot provenance report

[msi_ms7e06_v0.9.6_ddr5_mbprov_report.html][msi_ms7e06_v0.9.6_ddr5_mbprov_report.html_file]{.md-button}

The measured boot provenance report presents the evidence collected from a
running Dasharo machine (its SPI image, the TCG event logs of coreboot and the
payload, the live PCR values, a TPM quote, platform registers) and matches it
against the SBOM and the reproducibly built firmware image. It exists so that
reviewers can audit the firmware and to present attestation reference.

### EU Cyber Resilience Act (CRA)

The [EU Cyber Resilience Act](https://eur-lex.europa.eu/eli/reg/2024/2847/oj)
requires manufacturers to document what their products are made of and how
they handle security issues. This release ships a Software Bill of Materials
(SBOM) that lists every firmware component. We check it against the CRA
requirements with [sbom-tools](https://github.com/sbom-tool/sbom-tools).

!!! success "EU CRA Phase 1 (2026): Compliant"

    *Vulnerability and incident reporting (Article 14): how security issues are reported to us and how we notify the authorities. Applies from 11 September 2026.*

    All mandatory requirements are met. 1 recommendation can still be improved.

    | Area | What it covers | :material-close-circle:{ style="color: #ff5252" title="Failed" } Errors | :material-alert:{ style="color: #ff9100" title="Warning" } Warnings | :material-information:{ style="color: #448aff" title="Info" } Info |
    | --- | --- | :---: | :---: | :---: |
    | **Security Information** | How to report vulnerabilities and get security updates | 0 | 0 | 4 |
    | **Integrity Information** | Checksums that prove each component is unmodified | 0 | 0 | 1 |
    | **Document Metadata** | Who made the firmware and when the SBOM was created | 0 | 1 | 0 |

    **Errors** are serious gaps. **Warnings** are smaller gaps or
    recommendations; after a phase's deadline, missing items are reported as
    warnings too. **Info** findings are for reference only.

    ??? info "Show all findings"

        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 13(7) / Annex I Part II (1): SBOM freshness** (Document Metadata): SBOM has no creation timestamp; keep the documented component inventory current when components change
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex I Part I (2)(f): Component integrity information (hash)** (Integrity Information): Component 'coreboot' missing cryptographic hash (recommended for integrity)
          *Components: coreboot*
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex I Part II (1): Documented vulnerability information** (Security Information): No vulnerability data or vulnerability assertion found; include vulnerability information or a statement of no known vulnerabilities
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Art. 13(17): Vulnerability disclosure contact** (Security Information): Security contact provided via CRA sidecar (consider adding a security-contact externalReference to the SBOM)
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Art. 13(8) / 13(19): Support period disclosure** (Security Information): Consider specifying a support end date for security updates
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Art. 14(7): ENISA single reporting platform** (Security Information): No ENISA single reporting platform identifier — track ENISA publication and add `enisaReportingPlatformId` to the CRA sidecar when available

!!! success "EU CRA Phase 2 (2027): Compliant"

    *All CRA requirements for products sold in the EU, including a complete SBOM, security updates and a support period. Applies from 11 December 2027.*

    All mandatory requirements are met. 1 recommendation can still be improved.

    | Area | What it covers | :material-close-circle:{ style="color: #ff5252" title="Failed" } Errors | :material-alert:{ style="color: #ff9100" title="Warning" } Warnings | :material-information:{ style="color: #448aff" title="Info" } Info |
    | --- | --- | :---: | :---: | :---: |
    | **Security Information** | How to report vulnerabilities and get security updates | 0 | 0 | 6 |
    | **Document Metadata** | Who made the firmware and when the SBOM was created | 0 | 1 | 1 |
    | **Integrity Information** | Checksums that prove each component is unmodified | 0 | 0 | 1 |

    **Errors** are serious gaps. **Warnings** are smaller gaps or
    recommendations; after a phase's deadline, missing items are reported as
    warnings too. **Info** findings are for reference only.

    ??? info "Show all findings"

        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 13(7) / Annex I Part II (1): SBOM freshness** (Document Metadata): SBOM has no creation timestamp; keep the documented component inventory current when components change
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex V: EU Declaration of Conformity reference** (Document Metadata): Missing reference to the EU Declaration of Conformity (attestation or certification external reference) for product class Default
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex I Part I (2)(f): Component integrity information (hash)** (Integrity Information): Component 'coreboot' missing cryptographic hash (recommended for integrity)
          *Components: coreboot*
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex I Part II (1): Documented vulnerability information** (Security Information): No vulnerability data or vulnerability assertion found; include vulnerability information or a statement of no known vulnerabilities
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex I Part II (5): Coordinated vulnerability disclosure policy** (Security Information): CVD policy URL provided via CRA sidecar (consider adding an advisories externalReference to the SBOM)
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex II (7): Component lifecycle status** (Security Information): Consider including component lifecycle/end-of-support information
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Art. 13(17): Vulnerability disclosure contact** (Security Information): Security contact provided via CRA sidecar (consider adding a security-contact externalReference to the SBOM)
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Art. 13(8) / 13(19): Support period disclosure** (Security Information): Consider specifying a support end date for security updates
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Art. 14(7): ENISA single reporting platform** (Security Information): No ENISA single reporting platform identifier — track ENISA publication and add `enisaReportingPlatformId` to the CRA sidecar when available

### Platform security (fwupd HSI)

!!! danger "HSI:0 (Insecure State)"

    Little or no firmware protection was detected.

    [fwupd](https://fwupd.org) tested this firmware on real hardware and gave
    it a Host Security ID of **HSI:0**, level 0
    on a scale from 0 (Insecure) to 4 (Secure). Higher is better. To reach a
    level, the platform must pass all of the checks at that level and at all
    of the levels below it.
    [More about HSI](https://fwupd.github.io/libfwupdplugin/hsi.html).

| Level | What it covers | Checks passed | Result |
| --- | --- | :---: | :---: |
| **HSI-1**<br>Critical | The most basic protections, considered essential. A failure here could let an attacker compromise the firmware without physical access. | 13 / 14 | :material-close-circle:{ style="color: #ff5252" title="Failed" } |
| **HSI-2**<br>Risky | Protection of the boot process against an attacker with local access. Failures here are theoretical or hard to exploit. | 6 / 8 | :material-close-circle:{ style="color: #ff5252" title="Failed" } |
| **HSI-3**<br>Protected | Out-of-band protection of the firmware, possibly including recovery. | 2 / 5 | :material-close-circle:{ style="color: #ff5252" title="Failed" } |
| **HSI-4**<br>Secure | Encryption and execution protection for the firmware. | 2 / 2 | :material-check-circle:{ style="color: #00c853" title="Passed" } |
| **Runtime (!)** | Security issues in the operating system that was running during the test, such as an unencrypted swap partition. They add a "!" to the result but never change the level. | 4 / 6 | :material-alert:{ style="color: #ff9100" title="Warning" } |

??? failure "HSI-1 Critical: 13 of 14 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **BIOS firmware updates** | Firmware updates can be installed through the standard UEFI capsule mechanism. | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **csme16 override** | The Intel Management Engine cannot be forced into debug mode. | Locked |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **csme16 v16.1.30.2307** | The Intel Management Engine firmware has no known vulnerabilities. | Valid |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Platform debugging** | Hardware debugging interfaces are disabled and locked. | Disabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **SPI write** | The firmware flash chip is locked against writes from the OS. | Disabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **SPI lock** | The firmware flash chip is locked against writes from the OS. | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **SPI BIOS region** | Only trusted firmware code (SMM) can write the flash chip. | Locked |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Supported CPU** | fwupd knows how to check the security of this processor. | Valid |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **TPM empty PCRs** | The firmware records every boot stage in the TPM. | Valid |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **TPM v2.0** | A TPM 2.0 security chip is present and usable. | Found |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **UEFI bootservice variables** | Firmware-internal UEFI variables cannot be changed from the OS. | Locked |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **UEFI platform key** | Secure Boot uses a valid, non-test platform key. | Valid |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **UEFI secure boot** | Only signed bootloaders and operating systems are allowed to start. | Enabled |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **SPI BIOS Descriptor** | The flash layout cannot be changed to unlock protected regions.<br>**Why it fails:** [issue 1](#hsi-issue-1) | Invalid |

??? failure "HSI-2 Risky: 6 of 8 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Intel BootGuard** | Intel Boot Guard, a hardware root of trust for the firmware, is enabled. | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Intel BootGuard OTP fuse** | The Boot Guard configuration is permanently burned into the chipset. | Valid |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Intel GDS mitigation** |  | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **IOMMU** | Devices are restricted to the memory they are allowed to use (blocks DMA attacks, e.g. via Thunderbolt). | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Platform debugging** | Hardware debugging interfaces are disabled and locked. | Locked |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **TPM PCR0 reconstruction** | The TPM boot measurements match the firmware event log. | Valid |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Intel BootGuard ACM protected** | The Intel Boot Guard code that verifies the firmware is itself protected.<br>**Why it fails:** [issue 4](#hsi-issue-4) | Invalid |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Intel BootGuard verified boot** | Boot Guard checks the firmware signature before running it.<br>**Why it fails:** [issue 5](#hsi-issue-5) | Invalid |

??? failure "HSI-3 Protected: 2 of 5 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **CET Platform** | Control-flow Enforcement Technology, which blocks a common class of exploits, is available. | Supported |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Pre-boot DMA protection** | Devices cannot read or write memory through DMA before the OS has started. | Enabled |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Intel BootGuard error policy** | The system refuses to boot if firmware verification fails.<br>**Why it fails:** [issue 6](#hsi-issue-6) | Invalid |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Suspend-to-idle** | The system supports modern standby, which keeps protections active while asleep.<br>**Why it fails:** [issue 2](#hsi-issue-2) | Disabled |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Suspend-to-ram** | The system does not use S3 sleep, during which memory is less protected.<br>**Why it fails:** [issue 3](#hsi-issue-3) | Enabled |

??? success "HSI-4 Secure: 2 of 2 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Encrypted RAM** | RAM contents are encrypted, protecting against cold-boot and bus snooping attacks. | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **SMAP** | The kernel is prevented from accidentally accessing user memory. | Enabled |

??? warning "Runtime: 4 of 6 checks passed"

    Security issues in the operating system that was running during the test, such as an unencrypted swap partition. They add a "!" to the result but never change the level.

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **fwupd plugins** | fwupd is running without third-party plugins. | Untainted |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Linux kernel lockdown** | The Linux kernel blocks root from modifying the running kernel. | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Linux kernel** | The Linux kernel has not loaded unsigned or proprietary modules. | Untainted |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **UEFI db** | The Secure Boot allow-list is up to date. | Valid |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **CET OS Support** | The operating system uses Control-flow Enforcement Technology to block a common class of exploits.<br>**Why it fails:** [issue 7](#hsi-issue-7) | Not supported |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Linux swap** | Swap space is encrypted, so memory contents are not written to disk in the clear.<br>**Why it fails:** [issue 8](#hsi-issue-8) | Unencrypted |

#### Why some checks fail

1. <a id="hsi-issue-1"></a>**SPI BIOS Descriptor (HSI-1):** Flash regions are
   not locked to allow ME HAP mode to be enabled. Future releases may lock the
   descriptor.
2. <a id="hsi-issue-2"></a>**Suspend-to-idle (HSI-3):** Suspend-to-idle is can
   be supported on this platform, but many PCIe cards do not work well with
   that sleep mode, thus it is not enabled yet. Future releases may enable
   this feature.
3. <a id="hsi-issue-3"></a>**Suspend-to-ram (HSI-3):** Suspend-to-ram is
   enabled by default on this platform, but can be made runtime configurable
   when Suspend-to-idle is properly supported. Future releases may add setup
   option with Suspend-to-ram disabled by default, in favor of
   Suspend-to-idle.
4. <a id="hsi-issue-4"></a>**Intel BootGuard ACM protected (HSI-2):** Intel
   Boot Guard is not possible to be enabled on this platform, as they come
   fused with Boot Guard disabled out of the box.
5. <a id="hsi-issue-5"></a>**Intel BootGuard verified boot (HSI-2):** Intel
   Boot Guard is not possible to be enabled on this platform, as they come
   fused with Boot Guard disabled out of the box.
6. <a id="hsi-issue-6"></a>**Intel BootGuard error policy (HSI-3):** Intel
   Boot Guard is not possible to be enabled on this platform, as they come
   fused with Boot Guard disabled out of the box.
7. <a id="hsi-issue-7"></a>**CET OS Support (Runtime):** [CET OS check is not
   reliable.](https://github.com/fwupd/fwupd/issues/10162)
8. <a id="hsi-issue-8"></a>**Linux swap (Runtime):** The swap partitions or
   image files are not encrypted by default on Linux.

??? abstract "Full `fwupdmgr security` output"

    ```text
    HSI-1
    ✔ BIOS firmware updates:         Enabled
    ✔ csme16 override:               Locked
    ✔ csme16 v16.1.30.2307:          Valid
    ✔ Platform debugging:            Disabled
    ✔ SPI write:                     Disabled
    ✔ SPI lock:                      Enabled
    ✔ SPI BIOS region:               Locked
    ✔ Supported CPU:                 Valid
    ✔ TPM empty PCRs:                Valid
    ✔ TPM v2.0:                      Found
    ✔ UEFI bootservice variables:    Locked
    ✔ UEFI platform key:             Valid
    ✔ UEFI secure boot:              Enabled
    ✘ SPI BIOS Descriptor:           Invalid

    HSI-2
    ✔ Intel BootGuard:               Enabled
    ✔ Intel BootGuard OTP fuse:      Valid
    ✔ Intel GDS mitigation:          Enabled
    ✔ IOMMU:                         Enabled
    ✔ Platform debugging:            Locked
    ✔ TPM PCR0 reconstruction:       Valid
    ✘ Intel BootGuard ACM protected: Invalid
    ✘ Intel BootGuard verified boot: Invalid

    HSI-3
    ✔ CET Platform:                  Supported
    ✔ Pre-boot DMA protection:       Enabled
    ✘ Intel BootGuard error policy:  Invalid
    ✘ Suspend-to-idle:               Disabled
    ✘ Suspend-to-ram:                Enabled

    HSI-4
    ✔ Encrypted RAM:                 Enabled
    ✔ SMAP:                          Enabled

    Runtime Suffix -!
    ✔ fwupd plugins:                 Untainted
    ✔ Linux kernel lockdown:         Enabled
    ✔ Linux kernel:                  Untainted
    ✔ UEFI db:                       Valid
    ✘ CET OS Support:                Not supported
    ✘ Linux swap:                    Unencrypted
    ```

[msi_ms7e06_v0.9.6_ddr5_mbprov_report.html_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr5_mbprov_report.html
[msi_ms7e06_v0.9.6_ddr4.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr4.cap.sha256
[msi_ms7e06_v0.9.6_ddr4.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr4.cap.sha256.sig
[msi_ms7e06_v0.9.6_ddr4.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr4.rom.sha256
[msi_ms7e06_v0.9.6_ddr4.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr4.rom.sha256.sig
[msi_ms7e06_v0.9.6_ddr4.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr4.sbom.json
[msi_ms7e06_v0.9.6_ddr4.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr4.sbom.json.sha256
[msi_ms7e06_v0.9.6_ddr4.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr4.sbom.json.sha256.sig
[msi_ms7e06_v0.9.6_ddr4_dev_signed.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr4_dev_signed.cap.sha256
[msi_ms7e06_v0.9.6_ddr4_dev_signed.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr4_dev_signed.cap.sha256.sig
[msi_ms7e06_v0.9.6_ddr4_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr4_dev_signed.rom.sha256
[msi_ms7e06_v0.9.6_ddr4_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr4_dev_signed.rom.sha256.sig
[msi_ms7e06_v0.9.6_ddr5.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr5.cap.sha256
[msi_ms7e06_v0.9.6_ddr5.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr5.cap.sha256.sig
[msi_ms7e06_v0.9.6_ddr5.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr5.rom.sha256
[msi_ms7e06_v0.9.6_ddr5.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr5.rom.sha256.sig
[msi_ms7e06_v0.9.6_ddr5.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr5.sbom.json
[msi_ms7e06_v0.9.6_ddr5.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr5.sbom.json.sha256
[msi_ms7e06_v0.9.6_ddr5.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr5.sbom.json.sha256.sig
[msi_ms7e06_v0.9.6_ddr5_dev_signed.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr5_dev_signed.cap.sha256
[msi_ms7e06_v0.9.6_ddr5_dev_signed.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr5_dev_signed.cap.sha256.sig
[msi_ms7e06_v0.9.6_ddr5_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr5_dev_signed.rom.sha256
[msi_ms7e06_v0.9.6_ddr5_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.6/msi_ms7e06_v0.9.6_ddr5_dev_signed.rom.sha256.sig

## v0.9.5 - 2026-08-13

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/msi/ms7e06/v0.9.5-results.csv).
This is an [Assured Dasharo release](../../dasharo-naming-convention.md#description).

### Added

- [SBOM embedded into firmware](https://github.com/Dasharo/dasharo-issues/issues/129)
- MRC cache is now preserved by capsule updates to avoid memory retraining
- [Detection of TPMs that support only a single active bank](https://github.com/Dasharo/edk2/pull/282)
- [New setup submenu with various experimental CPU and overclocking options
  under Device Manager -> Platform Setup Menu. Use at your own risk, no
  support is provided for these
  options.](https://docs.dasharo.com/dasharo-menu-docs/platform-setup-menu/)
- [New experimental RAM voltage configuration options for DDR4 variants under
  Device Manager -> Platform Setup Menu. Use at your own risk, no support is
  provided for these
  options.](https://docs.dasharo.com/dasharo-menu-docs/platform-setup-menu/)
- [Perliminary support for SMI Transfer Monitor with an option to enable it
  via setup](https://docs.dasharo.com/guides/smi-transfer-monitor/)
- [Restoring default settings with CMOS battery reset](https://github.com/Dasharo/dasharo-issues/issues/1233)
- [EZ Debug LED support](https://github.com/Dasharo/dasharo-issues/issues/1911)
- [Verification of XMP profile and profile requested voltage on DDR4
  variants](https://github.com/Dasharo/dasharo-issues/issues/605)
- [Ramping the RAM voltage per XMP profile needs on DDR4 variants (DDR5
  variants ramp the voltage inside Intel
  FSP)](https://github.com/Dasharo/dasharo-issues/issues/605#issuecomment-1891021617)

### Changed

- Updated CPU microcode (see SBOM)
- [Support extending both SHA-1 and SHA-256 PCRs for dTPM](https://github.com/Dasharo/dasharo-issues/issues/982)
- TPM log no longer uses entries of fixed size
- [Updated TPM ACPI device path (can help with Windows 11)](https://github.com/Dasharo/coreboot/pull/796)
- [Removed MMX/SSE instructions from UEFI runtime drivers (fixes efivar on
  FreeBSD)](https://github.com/Dasharo/dasharo-issues/issues/1001)
- Register serial console after VGA (affects FreeBSD)
- [XMP profile selection option moved to Device Manager -> Platform Setup Menu
  (requires enabling overclocking option
  first)](https://docs.dasharo.com/dasharo-menu-docs/platform-setup-menu/)
- [Disabled USB port power when powering off the machine](https://github.com/Dasharo/dasharo-issues/issues/1910)

### Fixed

- [Unable to apply UEFI dbx 20250902 update via fwupdmgr](https://github.com/Dasharo/dasharo-issues/issues/1691)
- [Cannot enter Firmware Update Mode twice in a row](https://github.com/Dasharo/dasharo-issues/issues/1759)
- [XMP profile option showing XMP3 profile on DDR4 platforms](https://github.com/Dasharo/dasharo-issues/issues/683#issuecomment-1907380025)

### Known issues

- [XMP1 profile does not boot in combination with some DDR5 configurations](https://github.com/Dasharo/dasharo-issues/issues/683)
- [Cannot wake from suspend via RTC on QubesOS](https://github.com/Dasharo/dasharo-issues/issues/484)
- [Windows 11 installer unable to detect i225 Ethernet NIC](https://github.com/Dasharo/dasharo-issues/issues/482)
- [Windows 11 VBS (Virtualization-based Security) appears Not enabled on
  System Information](https://github.com/Dasharo/dasharo-issues/issues/539)
- [Ubuntu fails to boot with early DMA protection Enabled](https://github.com/Dasharo/dasharo-issues/issues/1869)

### Binaries

!!! Notice

    The release binaries have been withdrawn from the storage system to avoid
    updates to the unstable firmware version.

[sha256][msi_ms7e06_v0.9.5_ddr4.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.5_ddr4.cap_sig]{.md-button}
(msi_ms7e06_v0.9.5_ddr4.cap)
[sha256][msi_ms7e06_v0.9.5_ddr4.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.5_ddr4.rom_sig]{.md-button}
(msi_ms7e06_v0.9.5_ddr4.rom)
[msi_ms7e06_v0.9.5_ddr4.sbom.json][msi_ms7e06_v0.9.5_ddr4.sbom.json_file]{.md-button}
[sha256][msi_ms7e06_v0.9.5_ddr4.sbom.json_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.5_ddr4.sbom.json_sig]{.md-button}
[sha256][msi_ms7e06_v0.9.5_ddr4_dev_signed.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.5_ddr4_dev_signed.cap_sig]{.md-button}
(msi_ms7e06_v0.9.5_ddr4_dev_signed.cap)
[sha256][msi_ms7e06_v0.9.5_ddr4_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.5_ddr4_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.5_ddr4_dev_signed.rom)
[sha256][msi_ms7e06_v0.9.5_ddr5.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.5_ddr5.cap_sig]{.md-button}
(msi_ms7e06_v0.9.5_ddr5.cap)
[sha256][msi_ms7e06_v0.9.5_ddr5.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.5_ddr5.rom_sig]{.md-button}
(msi_ms7e06_v0.9.5_ddr5.rom)
[msi_ms7e06_v0.9.5_ddr5.sbom.json][msi_ms7e06_v0.9.5_ddr5.sbom.json_file]{.md-button}
[sha256][msi_ms7e06_v0.9.5_ddr5.sbom.json_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.5_ddr5.sbom.json_sig]{.md-button}
[sha256][msi_ms7e06_v0.9.5_ddr5_dev_signed.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.5_ddr5_dev_signed.cap_sig]{.md-button}
(msi_ms7e06_v0.9.5_ddr5_dev_signed.cap)
[sha256][msi_ms7e06_v0.9.5_ddr5_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.5_ddr5_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.5_ddr5_dev_signed.rom)

This is a Dasharo Pro Package Release. To access the pre-built binaries,
you need to [subscribe to the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our
[shop](https://shop.3mdeb.com/product/1year-desktop/).
As a subscriber, you will receive access to all firmware updates for the
duration of your subscription via the Dasharo Pro Package newsletter, and
gain entry to the Dasharo Premier Support invite-only live chat on the Matrix
network, enabling direct engagement with the Dasharo Team and fellow
subscribers for personalized, priority assistance.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7e06/dasharo-release-0.x-compatible-with-msi-ms-7e06-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.12 revision b4bd89b9](https://github.com/Dasharo/coreboot/tree/b4bd89b9)
    + [License](https://github.com/Dasharo/coreboot/blob/b4bd89b9/COPYING)
- [Dasharo EDKII fork based on edk2-stable202602 revision 5dc2238e](https://github.com/Dasharo/edk2/tree/5dc2238e)
    + [License](https://github.com/Dasharo/edk2/blob/5dc2238e/License.txt)
- [Dasharo EDK2-platforms fork based on 1002a59639f111a2f8178b77d1f5fde0ea8d976f revision 1002a596](https://github.com/Dasharo/edk2-platforms/tree/1002a596)
    + [License](https://github.com/Dasharo/edk2-platforms/blob/1002a596/License.txt)
- [iPXE based on ad8cbcee950840547f87394179a7e712e1c3c06f revision ad8cbcee](https://github.com/Dasharo/ipxe/tree/ad8cbcee)
    + [License](https://github.com/Dasharo/ipxe/blob/ad8cbcee/COPYING.GPLv2)
- [vboot based on 3f94e2c7ed revision 3f94e2c7](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3f94e2c7/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3f94e2c7/LICENSE)
- [Intel Management Engine version v16.1.30.2307](https://github.com/Dasharo/dasharo-blobs/blob/0ca1dcac/msi/ms7e06/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.2](https://github.com/Dasharo/dasharo-blobs/blob/0ca1dcac/msi/ms7e06/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version RPL-S C.0.C8.50](https://github.com/intel/FSP/tree/23cf2587/RaptorLakeFspBinPkg/Client/RaptorLakeS)
    + [License](https://github.com/intel/FSP/blob/23cf2587/FSP_License.pdf)
- [Intel microcode version ADL/RPL C0/H0 0x3e 12/10/2025](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20260811/intel-ucode/06-97-05)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20260811/license)
- [Intel microcode version RPL B0 0x137 18/02/2026](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20260811/intel-ucode/06-b7-01)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20260811/license)

An [integrated SBOM](https://doc.coreboot.org/sbom/sbom.html) is also
included in the firmware images. It describes a complete set of components
and their versions used to build the firmware images. The published SBOM
artifact is in CycloneDX format and can be viewed by SBOM tools, for example
[sbom-tools](https://github.com/sbom-tool/sbom-tools).

[msi_ms7e06_v0.9.5_ddr4.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr4.cap.sha256
[msi_ms7e06_v0.9.5_ddr4.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr4.cap.sha256.sig
[msi_ms7e06_v0.9.5_ddr4.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr4.rom.sha256
[msi_ms7e06_v0.9.5_ddr4.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr4.rom.sha256.sig
[msi_ms7e06_v0.9.5_ddr4.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr4.sbom.json
[msi_ms7e06_v0.9.5_ddr4.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr4.sbom.json.sha256
[msi_ms7e06_v0.9.5_ddr4.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr4.sbom.json.sha256.sig
[msi_ms7e06_v0.9.5_ddr4_dev_signed.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr4_dev_signed.cap.sha256
[msi_ms7e06_v0.9.5_ddr4_dev_signed.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr4_dev_signed.cap.sha256.sig
[msi_ms7e06_v0.9.5_ddr4_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr4_dev_signed.rom.sha256
[msi_ms7e06_v0.9.5_ddr4_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr4_dev_signed.rom.sha256.sig
[msi_ms7e06_v0.9.5_ddr5.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr5.cap.sha256
[msi_ms7e06_v0.9.5_ddr5.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr5.cap.sha256.sig
[msi_ms7e06_v0.9.5_ddr5.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr5.rom.sha256
[msi_ms7e06_v0.9.5_ddr5.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr5.rom.sha256.sig
[msi_ms7e06_v0.9.5_ddr5.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr5.sbom.json
[msi_ms7e06_v0.9.5_ddr5.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr5.sbom.json.sha256
[msi_ms7e06_v0.9.5_ddr5.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr5.sbom.json.sha256.sig
[msi_ms7e06_v0.9.5_ddr5_dev_signed.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr5_dev_signed.cap.sha256
[msi_ms7e06_v0.9.5_ddr5_dev_signed.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr5_dev_signed.cap.sha256.sig
[msi_ms7e06_v0.9.5_ddr5_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr5_dev_signed.rom.sha256
[msi_ms7e06_v0.9.5_ddr5_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.5/msi_ms7e06_v0.9.5_ddr5_dev_signed.rom.sha256.sig

## v0.9.4 - 2025-12-01

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/msi/ms7e06/v0.9.4-results.csv).

### Changed

- Updated CPU microcode (see SBOM)

### Known issues

- [XMP1 profile does not boot in combination with some DDR5 configurations](https://github.com/Dasharo/dasharo-issues/issues/683)
- [Windows 11 installer unable to detect i225 Ethernet NIC](https://github.com/Dasharo/dasharo-issues/issues/482)
- [Cannot wake from suspend via RTC on QubesOS](https://github.com/Dasharo/dasharo-issues/issues/484)
- [Windows 11 VBS (Virtualization-based Security) appears Not enabled on System Information](https://github.com/Dasharo/dasharo-issues/issues/539)
- [Capsule update signing is not enforced](https://github.com/Dasharo/dasharo-issues/issues/1075)

### Binaries

[sha256][msi_ms7e06_v0.9.4_ddr4.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.4_ddr4.cap_sig]{.md-button}
(msi_ms7e06_v0.9.4_ddr4.cap)

[sha256][msi_ms7e06_v0.9.4_ddr4.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.4_ddr4.rom_sig]{.md-button}
(msi_ms7e06_v0.9.4_ddr4.rom)

[sha256][msi_ms7e06_v0.9.4_ddr4_dev_signed.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.4_ddr4_dev_signed.cap_sig]{.md-button}
(msi_ms7e06_v0.9.4_ddr4_dev_signed.cap)

[sha256][msi_ms7e06_v0.9.4_ddr4_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.4_ddr4_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.4_ddr4_dev_signed.rom)

[sha256][msi_ms7e06_v0.9.4_ddr5.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.4_ddr5.cap_sig]{.md-button}
(msi_ms7e06_v0.9.4_ddr5.cap)

[sha256][msi_ms7e06_v0.9.4_ddr5.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.4_ddr5.rom_sig]{.md-button}
(msi_ms7e06_v0.9.4_ddr5.rom)

[sha256][msi_ms7e06_v0.9.4_ddr5_dev_signed.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.4_ddr5_dev_signed.cap_sig]{.md-button}
(msi_ms7e06_v0.9.4_ddr5_dev_signed.cap)

[sha256][msi_ms7e06_v0.9.4_ddr5_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.4_ddr5_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.4_ddr5_dev_signed.rom)

This is a Dasharo Pro Package Release. To access the pre-built binaries,
you need to [subscribe to the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our
[shop](https://shop.3mdeb.com/product/1year-desktop/).
As a subscriber, you will receive access to all firmware updates for the
duration of your subscription via the Dasharo Pro Package newsletter, and
gain entry to the Dasharo Premier Support invite-only live chat on the Matrix
network, enabling direct engagement with the Dasharo Team and fellow
subscribers for personalized, priority assistance.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7e06/dasharo-release-0.x-compatible-with-msi-ms-7e06-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 24.12 revision a5a05f13](https://github.com/Dasharo/coreboot/tree/a5a05f13)
    + [License](https://github.com/Dasharo/coreboot/blob/a5a05f13/COPYING)
- [Dasharo EDKII fork based on edk2-stable202502 revision 1c50dad8](https://github.com/Dasharo/edk2/tree/1c50dad8)
    + [License](https://github.com/Dasharo/edk2/blob/1c50dad8/License.txt)
- [Dasharo EDK2-platforms fork based on v0.9.0 revision 1002a596](https://github.com/Dasharo/edk2-platforms/tree/1002a596)
    + [License](https://github.com/Dasharo/edk2-platforms/blob/1002a596/License.txt)
- [iPXE based on 2025.03 revision 6c7068fc](https://github.com/Dasharo/ipxe/tree/6c7068fc)
    + [License](https://github.com/Dasharo/ipxe/blob/6c7068fc/COPYING.GPLv2)
- [vboot based on f1f70f46dc revision f1f70f46](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/LICENSE)
- [Intel Management Engine version v16.1.30.2307](https://github.com/Dasharo/dasharo-blobs/blob/8dce7604/msi/ms7e06/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.2](https://github.com/Dasharo/dasharo-blobs/blob/8dce7604/msi/ms7e06/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version RPL-S C.0.C8.50](https://github.com/intel/FSP/tree/5d0424c8/RaptorLakeFspBinPkg/Client/RaptorLakeS)
    + [License](https://github.com/intel/FSP/blob/5d0424c8/FSP_License.pdf)
- [Intel microcode version ADL/RPL C0/H0 0x3d 12/10/2025](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20251111/intel-ucode/06-97-05)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20251111/license)
- [Intel microcode version RPL B0 0x132 08/10/2025](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20251111/intel-ucode/06-b7-01)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20251111/license)

[msi_ms7e06_v0.9.4_ddr4.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr4.cap.sha256
[msi_ms7e06_v0.9.4_ddr4.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr4.cap.sha256.sig
[msi_ms7e06_v0.9.4_ddr4.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr4.rom.sha256
[msi_ms7e06_v0.9.4_ddr4.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr4.rom.sha256.sig
[msi_ms7e06_v0.9.4_ddr4_dev_signed.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr4_dev_signed.cap.sha256
[msi_ms7e06_v0.9.4_ddr4_dev_signed.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr4_dev_signed.cap.sha256.sig
[msi_ms7e06_v0.9.4_ddr4_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr4_dev_signed.rom.sha256
[msi_ms7e06_v0.9.4_ddr4_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr4_dev_signed.rom.sha256.sig
[msi_ms7e06_v0.9.4_ddr5.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr5.cap.sha256
[msi_ms7e06_v0.9.4_ddr5.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr5.cap.sha256.sig
[msi_ms7e06_v0.9.4_ddr5.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr5.rom.sha256
[msi_ms7e06_v0.9.4_ddr5.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr5.rom.sha256.sig
[msi_ms7e06_v0.9.4_ddr5_dev_signed.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr5_dev_signed.cap.sha256
[msi_ms7e06_v0.9.4_ddr5_dev_signed.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr5_dev_signed.cap.sha256.sig
[msi_ms7e06_v0.9.4_ddr5_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr5_dev_signed.rom.sha256
[msi_ms7e06_v0.9.4_ddr5_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.4/msi_ms7e06_v0.9.4_ddr5_dev_signed.rom.sha256.sig

## v0.9.3 - 2025-09-18

This is a [Rapid
release](../../dasharo-naming-convention.md) and
has a reduced scope of tests.

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/msi/ms7e06/v0.9.3-results.csv).

### Added

- Improved measured boot support
- Microsoft Option ROM UEFI CA to Secure Boot DB
- Check for flash descriptor writability when exposing HAP disable option

### Changed

- Rebased coreboot repository to 24.12 (see SBOM)
- Rebased edk2 repository to edk2-stable202502 (see SBOM)
- Owner GUID of Secure Boot DB and KEK to Microsoft recommended values
- Updated DBX to 2025-06-13

### Known issues

- [XMP1 profile does not boot in combination with some DDR5 configurations](https://github.com/Dasharo/dasharo-issues/issues/683)
- [Windows 11 installer unable to detect i225 Ethernet NIC](https://github.com/Dasharo/dasharo-issues/issues/482)
- [Cannot wake from suspend via RTC on QubesOS](https://github.com/Dasharo/dasharo-issues/issues/484)
- [Windows 11 VBS (Virtualization-based Security) appears Not enabled on
  System Information](https://github.com/Dasharo/dasharo-issues/issues/539)
- [Capsule update signing is not enforced](https://github.com/Dasharo/dasharo-issues/issues/1075)

### Binaries

[sha256][msi_ms7e06_v0.9.3_ddr4.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.3_ddr4.cap_sig]{.md-button}
(msi_ms7e06_v0.9.3_ddr4.cap)

[sha256][msi_ms7e06_v0.9.3_ddr4.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.3_ddr4.rom_sig]{.md-button}
(msi_ms7e06_v0.9.3_ddr4.rom)

[sha256][msi_ms7e06_v0.9.3_ddr4_dev_signed.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.3_ddr4_dev_signed.cap_sig]{.md-button}
(msi_ms7e06_v0.9.3_ddr4_dev_signed.cap)

[sha256][msi_ms7e06_v0.9.3_ddr4_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.3_ddr4_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.3_ddr4_dev_signed.rom)

[sha256][msi_ms7e06_v0.9.3_ddr5.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.3_ddr5.cap_sig]{.md-button}
(msi_ms7e06_v0.9.3_ddr5.cap)

[sha256][msi_ms7e06_v0.9.3_ddr5.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.3_ddr5.rom_sig]{.md-button}
(msi_ms7e06_v0.9.3_ddr5.rom)

[sha256][msi_ms7e06_v0.9.3_ddr5_dev_signed.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.3_ddr5_dev_signed.cap_sig]{.md-button}
(msi_ms7e06_v0.9.3_ddr5_dev_signed.cap)

[sha256][msi_ms7e06_v0.9.3_ddr5_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.3_ddr5_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.3_ddr5_dev_signed.rom)

This is a Dasharo Pro Package Release. To access the pre-built binaries, you
need to [subscribe to the Dasharo Pro Package
subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our
[shop](https://shop.3mdeb.com/product/1year-desktop/). As a subscriber, you
will receive access to all firmware updates for the duration of your
subscription via the Dasharo Pro Package newsletter, and gain entry to the
Dasharo Premier Support invite-only live chat on the Matrix network, enabling
direct engagement with the Dasharo Team and fellow subscribers for
personalized, priority assistance.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature
verification](../../guides/signature-verification.md) using [this
key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7e06/dasharo-release-0.x-compatible-with-msi-ms-7e06-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 24.12 revision fecb8be2](https://github.com/Dasharo/coreboot/tree/fecb8be2)
    + [License](https://github.com/Dasharo/coreboot/blob/fecb8be2/COPYING)
- [Dasharo EDKII fork based on edk2-stable202502 revision 1c50dad8](https://github.com/Dasharo/edk2/tree/1c50dad8)
    + [License](https://github.com/Dasharo/edk2/blob/1c50dad8/License.txt)
- [Dasharo EDK2-platforms fork based on v0.9.0 revision 1002a596](https://github.com/Dasharo/edk2-platforms/tree/1002a596)
    + [License](https://github.com/Dasharo/edk2-platforms/blob/1002a596/License.txt)
- [iPXE based on 2025.03 revision 6c7068fc](https://github.com/Dasharo/ipxe/tree/6c7068fc)
    + [License](https://github.com/Dasharo/ipxe/blob/6c7068fc/COPYING.GPLv2)
- [vboot based on f1f70f46dc revision f1f70f46](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/f1f70f46/LICENSE)
- [Intel Management Engine version v16.1.30.2307](https://github.com/Dasharo/dasharo-blobs/blob/8dce7604/msi/ms7e06/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.2](https://github.com/Dasharo/dasharo-blobs/blob/8dce7604/msi/ms7e06/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package version RPL-S C.0.C8.50](https://github.com/intel/FSP/tree/5d0424c8/RaptorLakeFspBinPkg/Client/RaptorLakeS)
    + [License](https://github.com/intel/FSP/blob/5d0424c8/FSP_License.pdf)
- [Intel microcode based on 0x36 (for CPUIDs 00090672, 00090675, 000b06f2, 000b06f5), 0x12B (for CPUID 000b0671) revision 8dce7604](https://github.com/Dasharo/dasharo-blobs/blob/8dce7604/msi/ms7d25/microcode.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/LICENSE_UCODE_PROD.md)

[msi_ms7e06_v0.9.3_ddr4.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr4.cap.sha256
[msi_ms7e06_v0.9.3_ddr4.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr4.cap.sha256.sig
[msi_ms7e06_v0.9.3_ddr4.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr4.rom.sha256
[msi_ms7e06_v0.9.3_ddr4.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr4.rom.sha256.sig
[msi_ms7e06_v0.9.3_ddr4_dev_signed.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr4_dev_signed.cap.sha256
[msi_ms7e06_v0.9.3_ddr4_dev_signed.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr4_dev_signed.cap.sha256.sig
[msi_ms7e06_v0.9.3_ddr4_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr4_dev_signed.rom.sha256
[msi_ms7e06_v0.9.3_ddr4_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr4_dev_signed.rom.sha256.sig
[msi_ms7e06_v0.9.3_ddr5.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr5.cap.sha256
[msi_ms7e06_v0.9.3_ddr5.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr5.cap.sha256.sig
[msi_ms7e06_v0.9.3_ddr5.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr5.rom.sha256
[msi_ms7e06_v0.9.3_ddr5.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr5.rom.sha256.sig
[msi_ms7e06_v0.9.3_ddr5_dev_signed.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr5_dev_signed.cap.sha256
[msi_ms7e06_v0.9.3_ddr5_dev_signed.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr5_dev_signed.cap.sha256.sig
[msi_ms7e06_v0.9.3_ddr5_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr5_dev_signed.rom.sha256
[msi_ms7e06_v0.9.3_ddr5_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/uefi/v0.9.3/msi_ms7e06_v0.9.3_ddr5_dev_signed.rom.sha256.sig

## v0.9.2 - 2024-12-10

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/msi/ms7e06/v0.9.2-results.csv).

### Added

- [Capsule Update V1](https://github.com/Dasharo/dasharo-issues/issues/423)
- [FWUPD support](https://docs.dasharo.com/kb/fwupd/)
- [Preserve user data during a capsule update](https://github.com/Dasharo/dasharo-issues/issues/809)
- [CPU configuration menu](https://github.com/Dasharo/dasharo-issues/issues/134)
- [Update to a much newer EDKII revision](https://github.com/Dasharo/dasharo-issues/issues/432)
- [Dual TPM feature in coreboot. When ME is disabled, fTPM becomes inactive as well and chipset will route the TPM traffic to SPI bus. coreboot will now probe for all possible TPMs and initialize the one that is currently active.](https://github.com/Dasharo/dasharo-issues/issues/113)
- [Expose ESRT entry for firmware updates](https://github.com/Dasharo/dasharo-issues/issues/802)

### Changed

- Use a constant value for major BIOS version number in ROMHOLES (used by FlashBIOS)
- Updated Intel CPU microcode to 0x12B version
- [Updated Flash Descriptor to enlarge BIOS region; refer to SBOM section below](https://github.com/Dasharo/dasharo-blobs/pull/16)

### Fixed

- [No ability to change active PCR banks with TPM PPI in FW](https://github.com/Dasharo/dasharo-issues/issues/521)
- [Fix the problem where a disk with a meaningful name would appear as Non-Block Boot Device in the created OS boot options from ESP](https://github.com/Dasharo/edk2/pull/122)
- [Improve resource detection above 4 GiB](https://github.com/Dasharo/edk2/pull/161)

### Known issues

- [XMP1 profile does not boot in combination with some DDR5 configurations](https://github.com/Dasharo/dasharo-issues/issues/683)
- [Windows 11 installer unable to detect i225 Ethernet NIC](https://github.com/Dasharo/dasharo-issues/issues/482)
- [Cannot wake from suspend via RTC on QubesOS](https://github.com/Dasharo/dasharo-issues/issues/484)
- [Windows 11 VBS (Virtualization-based Security) appears Not enabled on System Information](https://github.com/Dasharo/dasharo-issues/issues/539)
- [Capsule update signing is not enforced](https://github.com/Dasharo/dasharo-issues/issues/1075)

### Binaries

[sha256][msi_ms7e06_v0.9.2_ddr4.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.2_ddr4.cap_sig]{.md-button}
(msi_ms7e06_v0.9.2_ddr4.cap)

[sha256][msi_ms7e06_v0.9.2_ddr4_dev_signed.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.2_ddr4_dev_signed.cap_sig]{.md-button}
(msi_ms7e06_v0.9.2_ddr4_dev_signed.cap)

[sha256][msi_ms7e06_v0.9.2_ddr4.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.2_ddr4.rom_sig]{.md-button}
(msi_ms7e06_v0.9.2_ddr4.rom)

[sha256][msi_ms7e06_v0.9.2_ddr4_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.2_ddr4_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.2_ddr4_dev_signed.rom)

[sha256][msi_ms7e06_v0.9.2_ddr5.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.2_ddr5.cap_sig]{.md-button}
(msi_ms7e06_v0.9.2_ddr5.cap)

[sha256][msi_ms7e06_v0.9.2_ddr5_dev_signed.cap_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.2_ddr5_dev_signed.cap_sig]{.md-button}
(msi_ms7e06_v0.9.2_ddr5_dev_signed.cap)

[sha256][msi_ms7e06_v0.9.2_ddr5.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.2_ddr5.rom_sig]{.md-button}
(msi_ms7e06_v0.9.2_ddr5.rom)

[sha256][msi_ms7e06_v0.9.2_ddr5_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.2_ddr5_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.2_ddr5_dev_signed.rom)

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7e06/dasharo-release-0.x-compatible-with-msi-ms-7e06-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 24.02.01 revision b9d6d8c7](https://github.com/Dasharo/coreboot/tree/b9d6d8c7)
    + [License](https://github.com/Dasharo/coreboot/blob/b9d6d8c7/COPYING)
- [Dasharo EDKII fork based on edk2-stable202402 revision 5b3658c0](https://github.com/Dasharo/edk2/tree/5b3658c0)
    + [License](https://github.com/Dasharo/edk2/blob/5b3658c0/License.txt)
- [Dasharo EDK2-platforms fork based on v0.9.0 revision 3323ed48](https://github.com/Dasharo/edk2-platforms/tree/3323ed48)
    + [License](https://github.com/Dasharo/edk2-platforms/blob/3323ed48/License.txt)
- [iPXE based on 2023.12 revision 35d84756](https://github.com/Dasharo/ipxe/tree/35d84756)
    + [License](https://github.com/Dasharo/ipxe/blob/35d84756/COPYING.GPLv2)
- [vboot based on 3d37d2aafe revision 3d37d2aa](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/)
    + [License](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/3d37d2aa/LICENSE)
- [Intel Management Engine based on v16.1.30.2307 revision 4f6e917d](https://github.com/Dasharo/dasharo-blobs/blob/4f6e917d/msi/ms7e06/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor based on v1.2 revision 4f6e917d](https://github.com/Dasharo/dasharo-blobs/blob/4f6e917d/msi/ms7e06/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Firmware Support Package based on RPL-S C.0.C8.50 revision 3819544e](https://github.com/intel/FSP/tree/3819544e/RaptorLakeFspBinPkg/Client/RaptorLakeS)
    + [License](https://github.com/intel/FSP/blob/3819544e/FSP_License.pdf)
- [Intel microcode based on 0x36 (for CPUIDs 00090672, 00090675, 000b06f2, 000b06f5), 0x12B (for CPUID 000b0671) revision 4f6e917d](https://github.com/Dasharo/dasharo-blobs/blob/4f6e917d/msi/ms7d25/microcode.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/INTEL_FSP_SIC_LICENSE.txt)

## v0.9.1 - 2024-01-22

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/tree/main/boards/msi/ms7e06/results.csv).

### Added

- [Automatic fan control](https://github.com/Dasharo/dasharo-issues/issues/381)
- [RAM Disk support (EXPERIMENTAL)](https://github.com/Dasharo/dasharo-issues/issues/277)
- [Memory overclocking support with XMP profiles](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#memory-configuration)
- [Compatibility with Raptor Lake Refresh CPUs](https://github.com/Dasharo/dasharo-issues/issues/534)
- [Selective Option ROM loading](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#pcipcie-configuration)
- [Serial Console Redirection option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#serial-port-configuration)
- [Power state after power fail option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Option for Resizable BARs enabling](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#pcipcie-configuration)
- [ESP partition scanning in look for grubx64.efi or shimx64.efi or Windows bootmgr](https://github.com/Dasharo/dasharo-issues/issues/94)
- Memory speed is displayed in the firmware setup main page
- [Added support for taking screenshots in the firmware](https://docs.dasharo.com/dev-proc/screenshots/#taking-screenshots)
- Microsoft and Windows 2023 UEFI Secure Boot certificates
- Disabling ME and unlocking descriptor with HMRFPO command on FUM flow

### Changed

- [This is a Dasharo Pro Package release](https://docs.dasharo.com/dev-proc/versioning/#dasharo-pro-package-releases)
- [Updated microcode to the newer version; refer to SBOM section below](https://github.com/coreboot/intel-microcode/commit/6788bb07eb5f9e9b83c31ea1364150fe898f450a)
- [Updated ME to the newer version; refer to SBOM section below](https://github.com/Dasharo/dasharo-blobs/tree/main/msi/ms7e06)
- [Updated Flash Descriptor to unlock regions; refer to SBOM section below](https://github.com/Dasharo/dasharo-blobs/tree/main/msi/ms7e06)
- [Switched to the Raptor Lake-S Client FSP; refer to SBOM section below](https://github.com/intel/FSP/tree/481ea7cf0bae0107c3e14aa746e52657647142f3/RaptorLakeFspBinPkg/Client/RaptorLakeS)
- Get SMBIOS serial number and UUID from ROMHOLE region instead of CBFS
  (ROMHOLE is preserved during FlashBIOS and updates via DTS)
- Rebased coreboot on 4.21 tag
- Reduced the amount of microcode blobs included in the build, due to
  redundancy (some blobs had the same shasum and supported the same CPUIDs)
- Enroll default UEFI Secure Boot keys on the first boot
- [Improved UEFI Secure Boot menu user experience](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#secure-boot-configuration)
- DDR4 variant SMBIOS product name to reflect MSI naming
- Scope of reset to default hotkey to global in firmware setup
- Booting DTS over iPXE via HTTPS
- Removed the i225/i226 EFI driver from the builds in favor of native iPXE
  driver
- Switched iPXE repository to Dasharo fork for the native iPXE driver for
  i225/i226

### Fixed

- [No audio playback via headset](https://github.com/Dasharo/dasharo-issues/issues/483)
- [Auto Boot Time-out is reset to 0 when F9 is pressed](https://github.com/Dasharo/dasharo-issues/issues/513)
- [Some RPL-S CPUs ( 0xB06F2 (RPL-S C0) or 0xB06F5 (RPL-S H0)) have a problem with booting on v0.9.0](https://github.com/Dasharo/dasharo-issues/issues/496)
- [Change boot order menu is confusing](https://github.com/Dasharo/dasharo-issues/issues/422)
- [The setup menu does not issue a reset, resulting in saved but unapplied settings](https://github.com/Dasharo/dasharo-issues/issues/398)
- [PCI Express Resizable BAR programming](https://github.com/Dasharo/dasharo-issues/issues/565)
- [PCI Express resource allocation for Intel ARC A750](https://github.com/Dasharo/dasharo-issues/issues/584)
- [CPU frequency not displayed on setup front page](https://github.com/Dasharo/dasharo-issues/issues/662)
- P2SB BAR not properly reserved in ACPI
- Power LED not blinking during S3 sleep
- PS/2 controller not enabled at first boot after flashing
- Incorrect C-states reported in ACPI unsupported by HW
- Incorrect first timestamp format in ACPI FPDT

### Known issues

- [XMP1 profile does not boot in combination with some DDR5 configurations](https://github.com/Dasharo/dasharo-issues/issues/683)
- [Windows 11 installer unable to detect i225 Ethernet NIC](https://github.com/Dasharo/dasharo-issues/issues/482)
- [Cannot wake from suspend via RTC on QubesOS](https://github.com/Dasharo/dasharo-issues/issues/484)
- [Windows 11 VBS (Virtualization-based Security) appears Not enabled on System Information](https://github.com/Dasharo/dasharo-issues/issues/539)
- [No ability to change active PCR banks with TPM PPI in FW](https://github.com/Dasharo/dasharo-issues/issues/521)

### Binaries

[sha256][msi_ms7e06_v0.9.1_ddr4.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.1_ddr4.rom_sig]{.md-button}
(msi_ms7e06_v0.9.1_ddr4)

[sha256][msi_ms7e06_v0.9.1_ddr4_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.1_ddr4_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.1_ddr4_dev_signed)

[sha256][msi_ms7e06_v0.9.1_ddr5.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.1_ddr5.rom_sig]{.md-button}
(msi_ms7e06_v0.9.1_ddr5)

[sha256][msi_ms7e06_v0.9.1_ddr5_dev_signed.rom_hash]{.md-button}
[sha256.sig][msi_ms7e06_v0.9.1_ddr5_dev_signed.rom_sig]{.md-button}
(msi_ms7e06_v0.9.1_ddr5_dev_signed)

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7e06/dasharo-release-0.x-compatible-with-msi-ms-7e06-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 4.21 revision 2c5426c3](https://github.com/Dasharo/coreboot/tree/2c5426c3)
- [Dasharo EDKII fork based on edk2-stable202002 revision 11746340](https://github.com/Dasharo/edk2/tree/11746340)
- [iPXE based on 2023.12 revision 838611b3](https://github.com/Dasharo/ipxe/tree/838611b3)
- [vboot based on 0c11187c75 revision 0c11187c](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/0c11187c/)
- [Intel Management Engine based on v16.1.30.2307 revision 18aab76c](https://github.com/Dasharo/dasharo-blobs/blob/18aab76c/msi/ms7e06/me.bin)
- [Intel Flash Descriptor based on v1.1 revision 18aab76c](https://github.com/Dasharo/dasharo-blobs/blob/18aab76c/msi/ms7e06/descriptor.bin)
- [Intel Firmware Support Package based on RPL-S C.0.BD.40 revision 481ea7cf](https://github.com/intel/FSP/tree/481ea7cf/RaptorLakeFspBinPkg/Client/RaptorLakeS)
- [Intel microcode based on ADL/RPL C0/H0 0x0000002e revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-97-05)
- [Intel microcode based on RPL B0 0x00000119 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-b7-01)

## v0.9.0 - 2023-08-31

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/16wokQYhtS7XA1DQC3Om7FY-IImG6SZisGK7NnzyRGVY/edit?usp=sharing).

### Added

- [MSI FLASHBIOS recovery support](https://docs.dasharo.com/unified/msi/recovery/#using-msi-flashbios-button)
- [Raptor Lake-S CPU support](https://github.com/Dasharo/dasharo-issues/issues/130)
- MSI PRO Z790-P board support with the same feature set as PRO Z690-A
- [MSI ACPI device that triggers automatic driver and utility installation manager](https://www.youtube.com/watch?v=K-v-veV_jvI)
- [Support for logo customization](https://docs.dasharo.com../../guides/logo-customization/)
- UEFI 2.8 errata C compliance in EDKII fork
- [Firmware Update Mode](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [This is a Dasharo Pro Package release](https://docs.dasharo.com/dev-proc/versioning/#dasharo-pro-package-releases)
- [Use new microcode version, refer to SBOM](https://github.com/coreboot/intel-microcode/commit/390edfb411ba7de8559ad40597c7acb6c6a1ea96)
- [Use new ME version, refer to SBOM](https://github.com/Dasharo/dasharo-blobs/tree/main/msi/ms7e06)
- [Make NVIDIA RTX 3060 spawn HD Audio device in Device Manager](https://github.com/Dasharo/dasharo-issues/issues/364)
- [Reset to defaults with F9 causes the right settings to be restored](https://github.com/Dasharo/dasharo-issues/issues/355)
- [Popup with information about recovery mode is not displayed after flashing with a valid binary](https://github.com/Dasharo/dasharo-issues/issues/269)
- Proper watchdog timeout value to avoid reset loops on DDR5 boards
  with bigger amount of RAM
- [Chipset Watchdog timeout value changes actual watchdog trigger time](https://github.com/Dasharo/dasharo-issues/issues/413)
- No missing ACPI objects errors in Linux dmesg
- Setup Password option

### Binaries

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Pro Package newsletter.

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 4.18 revision 197229de](https://github.com/Dasharo/coreboot/tree/197229de)
- [Dasharo EDKII fork based on edk2-stable202002 revision 94f562a7](https://github.com/Dasharo/edk2/tree/94f562a7)
- [iPXE based on 6ba671acd9 revision 6ba671ac](https://github.com/ipxe/ipxe/tree/6ba671ac)
- [vboot based on b76cd8c806 revision b76cd8c8](https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+/b76cd8c8/)
- [Intel Management Engine based on v16.1.30.2255 revision 2a8875ec](https://github.com/Dasharo/dasharo-blobs/blob/2a8875ec/msi/ms7e06/me.bin)
- [Intel Flash Descriptor based on v1.0 revision 2a8875ec](https://github.com/Dasharo/dasharo-blobs/blob/2a8875ec/msi/ms7e06/descriptor.bin)
- [Intel Firmware Support Package based on IoT RPL-S PV 3492_03 revision 2fea9a2f](https://github.com/intel/FSP/tree/2fea9a2f/RaptorLakeFspBinPkg/IoT/RaptorLakeS)
- [Intel microcode based on ADL C0 0x0000002c revision microcode-20230613](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230613/intel-ucode/06-97-02)
- [Intel microcode based on ADL H0 0x0000002c revision microcode-20230613](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230613/intel-ucode/06-97-05)
- [Intel microcode based on RPL B0 0x00000113 revision microcode-20230613](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230613/intel-ucode/06-b7-01)

[msi_ms7e06_v0.9.2_ddr4.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr4.cap.sha256
[msi_ms7e06_v0.9.2_ddr4.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr4.cap.sha256.sig
[msi_ms7e06_v0.9.2_ddr4_dev_signed.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr4_dev_signed.cap.sha256
[msi_ms7e06_v0.9.2_ddr4_dev_signed.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr4_dev_signed.cap.sha256.sig
[msi_ms7e06_v0.9.2_ddr4.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr4.rom.sha256
[msi_ms7e06_v0.9.2_ddr4.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr4.rom.sha256.sig
[msi_ms7e06_v0.9.2_ddr4_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr4_dev_signed.rom.sha256
[msi_ms7e06_v0.9.2_ddr4_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr4_dev_signed.rom.sha256.sig
[msi_ms7e06_v0.9.2_ddr5.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr5.cap.sha256
[msi_ms7e06_v0.9.2_ddr5.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr5.cap.sha256.sig
[msi_ms7e06_v0.9.2_ddr5_dev_signed.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr5_dev_signed.cap.sha256
[msi_ms7e06_v0.9.2_ddr5_dev_signed.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr5_dev_signed.cap.sha256.sig
[msi_ms7e06_v0.9.2_ddr5.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr5.rom.sha256
[msi_ms7e06_v0.9.2_ddr5.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr5.rom.sha256.sig
[msi_ms7e06_v0.9.2_ddr5_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr5_dev_signed.rom.sha256
[msi_ms7e06_v0.9.2_ddr5_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.2/msi_ms7e06_v0.9.2_ddr5_dev_signed.rom.sha256.sig
[msi_ms7e06_v0.9.1_ddr4.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr4.rom.sha256
[msi_ms7e06_v0.9.1_ddr4.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr4.rom.sha256.sig
[msi_ms7e06_v0.9.1_ddr4_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr4_dev_signed.rom.sha256
[msi_ms7e06_v0.9.1_ddr4_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr4_dev_signed.rom.sha256.sig
[msi_ms7e06_v0.9.1_ddr5.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr5.rom.sha256
[msi_ms7e06_v0.9.1_ddr5.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr5.rom.sha256.sig
[msi_ms7e06_v0.9.1_ddr5_dev_signed.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr5_dev_signed.rom.sha256
[msi_ms7e06_v0.9.1_ddr5_dev_signed.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7e06/v0.9.1/msi_ms7e06_v0.9.1_ddr5_dev_signed.rom.sha256.sig
