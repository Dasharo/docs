# Release Notes

This is a Dasharo Pro Package Release. To obtain access to the pre-built binaries,
you need to [subscribe to the Dasharo Pro Package subscriber](https://docs.dasharo.com/ways-you-can-help-us/#become-a-dasharo-pro-package-subscriber).
You can do this by purchasing a Dasharo Pro Package product from our [shop](https://shop.3mdeb.com/product/1-year-dasharo-pro-package-for-network-appliance-corebootseabios/).
As a subscriber, you will receive access to all firmware updates for the
duration of your subscription via the Dasharo Pro Package newsletter,
and gain entry to the Dasharo Premier Support invite-only live chat
on the Matrix network, enabling direct engagement with the Dasharo Team
and fellow subscribers for personalized, priority assistance.

Following Release Notes describe status of Dasharo (coreboot+SeaBIOS) variant
of open-source firmware development for PC Engines apu2/3/4/6 platform.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("667a3af1-424e-439e-9144-57bfcf921ca4",
"Subscribe to Dasharo for PC Engines Release Notification Newsletter") }}

## v26.09.00.01 - 2026-11-09

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit?usp=sharing).

### Added

- [Rebased with official coreboot repository commit 8b0e34f (tag 26.09)](https://doc.coreboot.org/releases/coreboot-26.09-relnotes.html)
- SBOM generation for all firmware components
- Enabled measured boot
- Missing IOMMU device in ACPI with interrupt routing information
- Generation of unique SMBIOS System UUID from the NIC MAC address

### Changed

- [sortbootorder update to v26.09.00.01](https://github.com/pcengines/sortbootorder/compare/v24.08.00.01...v26.09.00.01)
- [SeaBIOS update to rel-1.16.3.2](https://github.com/pcengines/seabios/compare/rel-1.16.3.1...rel-1.16.3.2)
- [Builds are no longer TIMELESS. Reproduibility preserved through updated code preparation and git patch apply process](https://github.com/dasharo/dasharo-pq#prepare-code-base)
- Reworked IOMMU IVRS table generation to cover whole PCI root bridge
- cbmem console size increaed to 1MB to fit debug logs from SeaBIOS

### Fixed

- Enabled IOMMU guest APIC feature without HW support for guest AVIC causing
  Linux freezes
- Switching to IOAPIC mode on GNB IOAPIC moved to ACPI _PIC method
- CC6 save state area memory not being reserved
- Incorrect reserved bits cleared in the ECC register

### Known issues

- [apuled driver doesn't work in FreeBSD. Check the GPIOs document for workaround.](https://github.com/pcengines/coreboot/issues/329)
- [Some PCIe cards are not detected on certain OSes and/or in certain mPCIe
  slots. Check the mPCIe modules document for solution/workaround.](https://github.com/pcengines/apu2-documentation/issues/115)
- [Booting with 2 USB 3.x sticks plugged in apu4 sometimes results in detecting only 1 stick](https://github.com/pcengines/seabios/issues/30)
- [Certain USB 3.x sticks happen to not appear in boot menu](https://github.com/pcengines/seabios/issues/29)
- [Booting Xen 4.8 is unstable](https://github.com/pcengines/apu2-documentation/issues/109)

### Binaries

[sha256][pcengines_apu2_seabios_v26.09.00.01.rom_hash]{.md-button}
[sha256.sig][pcengines_apu2_seabios_v26.09.00.01.rom_sig]{.md-button}
(pcengines_apu2_seabios_v26.09.00.01.rom)
[pcengines_apu2_seabios_v26.09.00.01.sbom.json][pcengines_apu2_seabios_v26.09.00.01.sbom.json_file]{.md-button}
[sha256][pcengines_apu2_seabios_v26.09.00.01.sbom.json_hash]{.md-button}
[sha256.sig][pcengines_apu2_seabios_v26.09.00.01.sbom.json_sig]{.md-button}
[sha256][pcengines_apu3_seabios_v26.09.00.01.rom_hash]{.md-button}
[sha256.sig][pcengines_apu3_seabios_v26.09.00.01.rom_sig]{.md-button}
(pcengines_apu3_seabios_v26.09.00.01.rom)
[pcengines_apu3_seabios_v26.09.00.01.sbom.json][pcengines_apu3_seabios_v26.09.00.01.sbom.json_file]{.md-button}
[sha256][pcengines_apu3_seabios_v26.09.00.01.sbom.json_hash]{.md-button}
[sha256.sig][pcengines_apu3_seabios_v26.09.00.01.sbom.json_sig]{.md-button}
[sha256][pcengines_apu4_seabios_v26.09.00.01.rom_hash]{.md-button}
[sha256.sig][pcengines_apu4_seabios_v26.09.00.01.rom_sig]{.md-button}
(pcengines_apu4_seabios_v26.09.00.01.rom)
[pcengines_apu4_seabios_v26.09.00.01.sbom.json][pcengines_apu4_seabios_v26.09.00.01.sbom.json_file]{.md-button}
[sha256][pcengines_apu4_seabios_v26.09.00.01.sbom.json_hash]{.md-button}
[sha256.sig][pcengines_apu4_seabios_v26.09.00.01.sbom.json_sig]{.md-button}
[sha256][pcengines_apu6_seabios_v26.09.00.01.rom_hash]{.md-button}
[sha256.sig][pcengines_apu6_seabios_v26.09.00.01.rom_sig]{.md-button}
(pcengines_apu6_seabios_v26.09.00.01.rom)
[pcengines_apu6_seabios_v26.09.00.01.sbom.json][pcengines_apu6_seabios_v26.09.00.01.sbom.json_file]{.md-button}
[sha256][pcengines_apu6_seabios_v26.09.00.01.sbom.json_hash]{.md-button}
[sha256.sig][pcengines_apu6_seabios_v26.09.00.01.sbom.json_sig]{.md-button}

This is a Dasharo Pro Package release. For this platform, access to pre-built
binaries is provided exclusively through the
[Full Build for PC Engines apu2](https://shop.3mdeb.com/shop/dasharo-pro-package/1-year-dasharo-pro-package-for-network-appliance/),
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
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/pcengines_apu2/dasharo-release-24.08.00.x-for-pc-engines-signing-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 26.09 revision 33ea3953](https://github.com/coreboot/coreboot/tree/26.09)
    + [License](https://github.com/coreboot/coreboot/blob/26.09/COPYING)
- [Dasharo Patchqueue Initiative based on 26.09.00.01 revision 3eccce44](https://github.com/Dasharo/dasharo-pq/tree/3eccce44)
    + [License](https://github.com/Dasharo/dasharo-pq/blob/3eccce44/LICENSE)
- [SeaBIOS based on rel-1.16.3.2 revision 1140b280](https://github.com/pcengines/seabios/tree/1140b280)
    + [License](https://github.com/pcengines/seabios/blob/1140b280/COPYING)
- [sortbootorder based on v26.09.00.01 revision 3a159692](https://github.com/pcengines/sortbootorder/tree/3a159692)
    + [License](https://github.com/pcengines/sortbootorder/blob/3a159692/LICENSE)
- [iPXE based on 2025.12 revision 7c39c04a](https://github.com/ipxe/ipxe/tree/7c39c04a)
    + [License](https://github.com/ipxe/ipxe/blob/7c39c04a/COPYING.GPLv2)
- [Memtest86+ based on v002 revision 0bd34c22](https://review.coreboot.org/admin/repos/memtest86plus,general)
    + [License](https://review.coreboot.org/admin/repos/memtest86plus,general)
- [AMD AGESA Binary Platform Initialization version MullinsPI 1.0.0.A](https://github.com/coreboot/blobs/tree/6f42f0f3/mainboard/pcengines/apu2/AGESA.bin)
    + [License](https://github.com/coreboot/blobs/tree/6f42f0f3/pi/amd/00730F01/FT3b/license.txt)
- [AMD Platform Security Processor bootloader version D.1.1.4D](https://github.com/coreboot/blobs/tree/6f42f0f3/southbridge/amd/avalon/PSP/PspBootLoader.Bypass.sbin)
    + [License](https://github.com/coreboot/blobs/blob/6f42f0f3/southbridge/amd/avalon/PSP/license.txt)
- [AMD Platform Security Processor firmware public key version v1.0](https://github.com/coreboot/blobs/tree/6f42f0f3/southbridge/amd/avalon/PSP/AmdPubKey.bin)
    + [License](https://github.com/coreboot/blobs/blob/6f42f0f3/southbridge/amd/avalon/PSP/license.txt)
- [AMD System Management Unit firmware version 14.33](https://github.com/coreboot/blobs/tree/6f42f0f3/southbridge/amd/avalon/PSP/SmuFirmware.sbin)
    + [License](https://github.com/coreboot/blobs/blob/6f42f0f3/southbridge/amd/avalon/PSP/license.txt)
- [AMD System Management Unit - Software Configuration Settings binary version !SCS MullinsPI V0.0.0.1](https://github.com/coreboot/blobs/tree/6f42f0f3/southbridge/amd/avalon/PSP/SmuScs.bin)
    + [License](https://github.com/coreboot/blobs/blob/6f42f0f3/southbridge/amd/avalon/PSP/license.txt)
- [AMD Hudson xHCI firmware version 1.1.0.0068](https://github.com/coreboot/blobs/tree/6f42f0f3/southbridge/amd/avalon/xhci.bin)
    + [License](https://github.com/coreboot/blobs/blob/6f42f0f3/southbridge/amd/avalon/license.txt)

An [integrated SBOM](https://doc.coreboot.org/sbom/sbom.html) is also
included in the firmware images. It describes a complete set of components
and their versions used to build the firmware images. The published SBOM
artifact is in CycloneDX format and can be viewed by SBOM tools, for example
[sbom-tools](https://github.com/sbom-tool/sbom-tools).

### Measured boot provenance report

[pcengines_apu2_v26.09.00.01_mbprov_report.html][pcengines_apu2_v26.09.00.01_mbprov_report.html_file]{.md-button}

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
| **HSI-1**<br>Critical | The most basic protections, considered essential. A failure here could let an attacker compromise the firmware without physical access. | 3 / 6 | :material-close-circle:{ style="color: #ff5252" title="Failed" } |
| **HSI-2**<br>Risky | Protection of the boot process against an attacker with local access. Failures here are theoretical or hard to exploit. | 1 / 5 | :material-close-circle:{ style="color: #ff5252" title="Failed" } |
| **HSI-3**<br>Protected | Out-of-band protection of the firmware, possibly including recovery. | 1 / 5 | :material-close-circle:{ style="color: #ff5252" title="Failed" } |
| **HSI-4**<br>Secure | Encryption and execution protection for the firmware. | 0 / 3 | :material-close-circle:{ style="color: #ff5252" title="Failed" } |
| **Runtime (!)** | Security issues in the operating system that was running during the test, such as an unencrypted swap partition. They add a "!" to the result but never change the level. | 2 / 5 | :material-alert:{ style="color: #ff9100" title="Warning" } |

??? failure "HSI-1 Critical: 3 of 6 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **TPM empty PCRs** | The firmware records every boot stage in the TPM. | Valid |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **TPM v2.0** | A TPM 2.0 security chip is present and usable. | Found |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **UEFI bootservice variables** | Firmware-internal UEFI variables cannot be changed from the OS. | Locked |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **SMM locked down** | System Management Mode, the most privileged CPU mode, is locked down.<br>**Why it fails:** [issue 1](#hsi-issue-1) | Unlocked |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Fused platform** | The chipset is in its locked, production configuration.<br>**Why it fails:** [issue 2](#hsi-issue-2) | Unknown |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Supported CPU** | fwupd knows how to check the security of this processor.<br>**Why it fails:** [issue 3](#hsi-issue-3) | Unknown |

??? failure "HSI-2 Risky: 1 of 5 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **TPM PCR0 reconstruction** | The TPM boot measurements match the firmware event log. | Valid |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Platform secure boot** | The processor only runs firmware signed with the platform vendor's key (AMD PSB).<br>**Why it fails:** [issue 4](#hsi-issue-4) | Unknown |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **SPI write protection** | The firmware flash chip is locked against writes from the OS.<br>**Why it fails:** [issue 5](#hsi-issue-5) | Unknown |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **IOMMU** | Devices are restricted to the memory they are allowed to use (blocks DMA attacks, e.g. via Thunderbolt).<br>**Why it fails:** [issue 6](#hsi-issue-6) | Not found |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Platform debugging** | Hardware debugging interfaces are disabled and locked.<br>**Why it fails:** [issue 7](#hsi-issue-7) | Unknown |

??? failure "HSI-3 Protected: 1 of 5 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Suspend-to-ram** | The system does not use S3 sleep, during which memory is less protected. | Disabled |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **SPI replay protection** | The flash chip rejects replayed writes, so old firmware cannot be written back.<br>**Why it fails:** [issue 8](#hsi-issue-8) | Unknown |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **CET Platform** | Control-flow Enforcement Technology, which blocks a common class of exploits, is available.<br>**Why it fails:** [issue 9](#hsi-issue-9) | Not supported |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Pre-boot DMA protection** | Devices cannot read or write memory through DMA before the OS has started.<br>**Why it fails:** [issue 10](#hsi-issue-10) | Invalid |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Suspend-to-idle** | The system supports modern standby, which keeps protections active while asleep.<br>**Why it fails:** [issue 11](#hsi-issue-11) | Disabled |

??? failure "HSI-4 Secure: 0 of 3 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Processor rollback protection** | The platform refuses to run older, possibly vulnerable firmware.<br>**Why it fails:** [issue 12](#hsi-issue-12) | Unknown |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Encrypted RAM** | RAM contents are encrypted, protecting against cold-boot and bus snooping attacks.<br>**Why it fails:** [issue 13](#hsi-issue-13) | Unknown |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **SMAP** | The kernel is prevented from accidentally accessing user memory.<br>**Why it fails:** [issue 14](#hsi-issue-14) | Not supported |

??? warning "Runtime: 2 of 5 checks passed"

    Security issues in the operating system that was running during the test, such as an unencrypted swap partition. They add a "!" to the result but never change the level.

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **fwupd plugins** | fwupd is running without third-party plugins. | Untainted |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Linux kernel** | The Linux kernel has not loaded unsigned or proprietary modules. | Untainted |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Linux kernel lockdown** | The Linux kernel blocks root from modifying the running kernel.<br>**Why it fails:** [issue 15](#hsi-issue-15) | Disabled |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Linux swap** | Swap space is encrypted, so memory contents are not written to disk in the clear.<br>**Why it fails:** [issue 16](#hsi-issue-16) | Unencrypted |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **UEFI secure boot** | Only signed bootloaders and operating systems are allowed to start.<br>**Why it fails:** [issue 17](#hsi-issue-17) | Disabled |

#### Why some checks fail

1. <a id="hsi-issue-1"></a>**SMM locked down (HSI-1):** The test checks if two
   SMM lock bits are present. If Any of them is not set, the test fails. The
   processor present on PC Engines apu2 has only one SMM lock bit implemented
   in hardware. Thus the test can never pass as is. Despite that the SMM is
   locked with the available lock bit.
2. <a id="hsi-issue-2"></a>**Fused platform (HSI-1):** The PSP on PC Engines
   apu2 processor predates the PSP HSTI capabilities introduced in Zen
   microarchitecture. Thus Linux PSP/CCP driver does not expose the HSTI
   attributes and fwupd cannot determine the security state.
3. <a id="hsi-issue-3"></a>**Supported CPU (HSI-1):** The PSP on PC Engines
   apu2 processor predates the PSP HSTI capabilities introduced in Zen
   microarchitecture. Thus Linux PSP/CCP driver does not expose the HSTI
   attributes and fwupd cannot determine the security state.
4. <a id="hsi-issue-4"></a>**Platform secure boot (HSI-2):** The PSP on PC
   Engines apu2 processor predates the PSP HSTI capabilities introduced in Zen
   microarchitecture. Thus Linux PSP/CCP driver does not expose the HSTI
   attributes and fwupd cannot determine the security state. Also the
   published PSP blobs contain a PSP bootloader with PSB flow bypassed, which
   makes PSB not secure on these processors.
5. <a id="hsi-issue-5"></a>**SPI write protection (HSI-2):** The PSP on PC
   Engines apu2 processor predates the PSP HSTI capabilities introduced in Zen
   microarchitecture. Thus Linux PSP/CCP driver does not expose the HSTI
   attributes and fwupd cannot determine the security state. Also ROM Armor is
   not supported on this processor, chipset SPI write protection is not
   feasible (buggy lock bits prevent access to parts of the SPI flash). Chip
   SPI write protection possible via setup, but this form of protection is not
   checked by fwupd, so this test will never pass.
6. <a id="hsi-issue-6"></a>**IOMMU (HSI-2):** IOMMU is disabled by default on
   this firmware. It has to be explicitly enabled in setup.
7. <a id="hsi-issue-7"></a>**Platform debugging (HSI-2):** The PSP on PC
   Engines apu2 processor predates the PSP HSTI capabilities introduced in Zen
   microarchitecture. Thus Linux PSP/CCP driver does not expose the HSTI
   attributes and fwupd cannot determine the security state.
8. <a id="hsi-issue-8"></a>**SPI replay protection (HSI-3):** The PSP on PC
   Engines apu2 processor predates the PSP HSTI capabilities introduced in Zen
   microarchitecture. Thus Linux PSP/CCP driver does not expose the HSTI
   attributes and fwupd cannot determine the security state. Also, RPMC not
   supported by processor and the SPI chip.
9. <a id="hsi-issue-9"></a>**CET Platform (HSI-3):** Feature not supported by
   the processor present on PC Engines apu2, per CPUID instruction.
10. <a id="hsi-issue-10"></a>**Pre-boot DMA protection (HSI-3):** [Pre-boot
    DMA protection is currently not supported for AMD platforms in Dasharo
    firmware.](https://github.com/Dasharo/dasharo-issues/issues/1903)
11. <a id="hsi-issue-11"></a>**Suspend-to-idle (HSI-3):** Feature not
    supported by the processor present on PC Engines apu2.
12. <a id="hsi-issue-12"></a>**Processor rollback protection (HSI-4):** The
    PSP on PC Engines apu2 processor predates the PSP HSTI capabilities
    introduced in Zen microarchitecture. Thus Linux PSP/CCP driver does not
    expose the HSTI attributes and fwupd cannot determine the security state.
13. <a id="hsi-issue-13"></a>**Encrypted RAM (HSI-4):** The PSP on PC Engines
    apu2 processor predates the PSP HSTI capabilities introduced in Zen
    microarchitecture. Thus Linux PSP/CCP driver does not expose the HSTI
    attributes and fwupd cannot determine the security state. Also, the
    feature not supported by the processor present on PC Engines apu2.
14. <a id="hsi-issue-14"></a>**SMAP (HSI-4):** Feature not supported by the
    processor present on PC Engines apu2, per CPUID instruction.
15. <a id="hsi-issue-15"></a>**Linux kernel lockdown (Runtime):** Kernel
    lockdown is disabled if UEFI Secure Boot is not enabled. Lockdown has to
    be explicitly enabled via kernel command line at boot.
16. <a id="hsi-issue-16"></a>**Linux swap (Runtime):** The swap partitions or
    image files are not encrypted by default on Linux.
17. <a id="hsi-issue-17"></a>**UEFI secure boot (Runtime):** This firmware
    supports legacy BIOS only, thus UEFI Secure Boot cannot be supported.

??? abstract "Full `fwupdmgr security` output"

    ```text
    HSI-1
    ✔ TPM empty PCRs:                Valid
    ✔ TPM v2.0:                      Found
    ✔ UEFI bootservice variables:    Locked
    ✘ SMM locked down:               Unlocked
    ✘ Fused platform:                Unknown
    ✘ Supported CPU:                 Unknown

    HSI-2
    ✔ TPM PCR0 reconstruction:       Valid
    ✘ Platform secure boot:          Unknown
    ✘ SPI write protection:          Unknown
    ✘ IOMMU:                         Not found
    ✘ Platform debugging:            Unknown

    HSI-3
    ✔ Suspend-to-ram:                Disabled
    ✘ SPI replay protection:         Unknown
    ✘ CET Platform:                  Not supported
    ✘ Pre-boot DMA protection:       Invalid
    ✘ Suspend-to-idle:               Disabled

    HSI-4
    ✘ Processor rollback protection: Unknown
    ✘ Encrypted RAM:                 Unknown
    ✘ SMAP:                          Not supported

    Runtime Suffix -!
    ✔ fwupd plugins:                 Untainted
    ✔ Linux kernel:                  Untainted
    ✘ Linux kernel lockdown:         Disabled
    ✘ Linux swap:                    Unencrypted
    ✘ UEFI secure boot:              Disabled
    ```

[pcengines_apu2_v26.09.00.01_mbprov_report.html_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu2_v26.09.00.01_mbprov_report.html
[pcengines_apu2_seabios_v26.09.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu2_seabios_v26.09.00.01.rom.sha256
[pcengines_apu2_seabios_v26.09.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu2_seabios_v26.09.00.01.rom.sha256.sig
[pcengines_apu2_seabios_v26.09.00.01.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu2_seabios_v26.09.00.01.sbom.json
[pcengines_apu2_seabios_v26.09.00.01.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu2_seabios_v26.09.00.01.sbom.json.sha256
[pcengines_apu2_seabios_v26.09.00.01.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu2_seabios_v26.09.00.01.sbom.json.sha256.sig
[pcengines_apu3_seabios_v26.09.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu3_seabios_v26.09.00.01.rom.sha256
[pcengines_apu3_seabios_v26.09.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu3_seabios_v26.09.00.01.rom.sha256.sig
[pcengines_apu3_seabios_v26.09.00.01.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu3_seabios_v26.09.00.01.sbom.json
[pcengines_apu3_seabios_v26.09.00.01.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu3_seabios_v26.09.00.01.sbom.json.sha256
[pcengines_apu3_seabios_v26.09.00.01.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu3_seabios_v26.09.00.01.sbom.json.sha256.sig
[pcengines_apu4_seabios_v26.09.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu4_seabios_v26.09.00.01.rom.sha256
[pcengines_apu4_seabios_v26.09.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu4_seabios_v26.09.00.01.rom.sha256.sig
[pcengines_apu4_seabios_v26.09.00.01.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu4_seabios_v26.09.00.01.sbom.json
[pcengines_apu4_seabios_v26.09.00.01.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu4_seabios_v26.09.00.01.sbom.json.sha256
[pcengines_apu4_seabios_v26.09.00.01.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu4_seabios_v26.09.00.01.sbom.json.sha256.sig
[pcengines_apu6_seabios_v26.09.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu6_seabios_v26.09.00.01.rom.sha256
[pcengines_apu6_seabios_v26.09.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu6_seabios_v26.09.00.01.rom.sha256.sig
[pcengines_apu6_seabios_v26.09.00.01.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu6_seabios_v26.09.00.01.sbom.json
[pcengines_apu6_seabios_v26.09.00.01.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu6_seabios_v26.09.00.01.sbom.json.sha256
[pcengines_apu6_seabios_v26.09.00.01.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v26.09.00.01/pcengines_apu6_seabios_v26.09.00.01.sbom.json.sha256.sig

## v24.08.00.01 - 2025-06-10

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit?usp=sharing).

### Added

- [Rebased with official coreboot repository commit 2ccbcc5 (tag 24.08)](https://doc.coreboot.org/releases/coreboot-24.08-relnotes.html)

### Changed

- [SeaBIOS update to rel-1.16.3.1](https://github.com/pcengines/seabios/compare/rel-1.16.0.1...rel-1.16.3.1)
- [sortbootorder update to v24.08.00.01](https://github.com/pcengines/sortbootorder/compare/v24.05.00.01...v24.08.00.01)

### Known issues

- [apuled driver doesn't work in FreeBSD. Check the GPIOs document for workaround.](https://github.com/pcengines/coreboot/issues/329)
- [Some PCIe cards are not detected on certain OSes and/or in certain mPCIe slots. Check the mPCIe modules document for solution/workaround.](https://github.com/pcengines/apu2-documentation/issues/115)
- [Booting with 2 USB 3.x sticks plugged in apu4 sometimes results in detecting only 1 stick](https://github.com/pcengines/seabios/issues/30)
- [Certain USB 3.x sticks happen to not appear in boot menu](https://github.com/pcengines/seabios/issues/29)
- [Booting Xen 4.8 is unstable](https://github.com/pcengines/apu2-documentation/issues/109)

### Binaries

[sha256][pcengines_apu2_seabios_v24.08.00.01.rom_hash]{.md-button}
[sha256.sig][pcengines_apu2_seabios_v24.08.00.01.rom_sig]{.md-button}

[sha256][pcengines_apu3_seabios_v24.08.00.01.rom_hash]{.md-button}
[sha256.sig][pcengines_apu3_seabios_v24.08.00.01.rom_sig]{.md-button}

[sha256][pcengines_apu4_seabios_v24.08.00.01.rom_hash]{.md-button}
[sha256.sig][pcengines_apu4_seabios_v24.08.00.01.rom_sig]{.md-button}

[sha256][pcengines_apu6_seabios_v24.08.00.01.rom_hash]{.md-button}
[sha256.sig][pcengines_apu6_seabios_v24.08.00.01.rom_sig]{.md-button}

This is a Dasharo Pro Package Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Pro Package newsletter.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/pcengines_apu2/dasharo-release-24.08.00.x-for-pc-engines-signing-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 24.08 revision fadbc031](https://github.com/coreboot/coreboot/tree/24.08)
    + [License](https://github.com/coreboot/coreboot/blob/24.08/COPYING)
- [Dasharo Patchqueue Initiative based on 24.08.00.01 revision d944bc39](https://github.com/Dasharo/dasharo-pq/tree/d944bc39)
    + [License](https://github.com/Dasharo/dasharo-pq/blob/d944bc39/LICENSE)
- [SeaBIOS based on rel-1.16.3.1 revision ac9eb800](https://github.com/pcengines/seabios/tree/ac9eb800)
    + [License](https://github.com/pcengines/seabios/blob/ac9eb800/COPYING)
- [sortbootorder based on v24.08.00.01 revision 6188b4f4](https://github.com/pcengines/sortbootorder/tree/6188b4f4)
    + [License](https://github.com/pcengines/sortbootorder/blob/6188b4f4/LICENSE)
- [iPXE based on 2024.08 revision 301644ab](https://github.com/ipxe/ipxe/tree/301644ab)
    + [License](https://github.com/ipxe/ipxe/blob/301644ab/COPYING.GPLv2)
- [Memtest86+ based on v002 revision 0bd34c22](https://review.coreboot.org/admin/repos/memtest86plus,general)
    + [License](https://review.coreboot.org/admin/repos/memtest86plus,general)
- [AMD AGESA Binary Platform Initialization version MullinsPI 1.0.0.A](https://github.com/coreboot/blobs/tree/a8db7dfe/pi/amd/00730F01/FT3b)
    + [License](https://github.com/coreboot/blobs/tree/a8db7dfe/pi/amd/00730F01/FT3b/license.txt)
- [AMD Platform Security Processor bootloader version D.1.1.4D](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/PSP/PspBootLoader.Bypass.sbin)
    + [License](https://github.com/coreboot/blobs/blob/a8db7dfe/southbridge/amd/avalon/PSP/license.txt)
- [AMD Platform Security Processor firmware public key version v1.0](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/PSP/AmdPubKey.bin)
    + [License](https://github.com/coreboot/blobs/blob/a8db7dfe/southbridge/amd/avalon/PSP/license.txt)
- [AMD System Management Unit firmware version 1433](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/PSP/SmuFirmware.sbin)
    + [License](https://github.com/coreboot/blobs/blob/a8db7dfe/southbridge/amd/avalon/PSP/license.txt)
- [AMD System Management Unit - Software Configuration Settings binary version 1433](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/PSP/SmuScs.bin)
    + [License](https://github.com/coreboot/blobs/blob/a8db7dfe/southbridge/amd/avalon/PSP/license.txt)
- [AMD Hudson xHCI firmware version 1.1.0.0068](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/xhci.bin)
    + [License](https://github.com/coreboot/blobs/blob/a8db7dfe/southbridge/amd/avalon/license.txt)

[pcengines_apu2_seabios_v24.08.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v24.08.00.01/pcengines_apu2_seabios_v24.08.00.01.rom.sha256
[pcengines_apu2_seabios_v24.08.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v24.08.00.01/pcengines_apu2_seabios_v24.08.00.01.rom.sha256.sig
[pcengines_apu3_seabios_v24.08.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v24.08.00.01/pcengines_apu3_seabios_v24.08.00.01.rom.sha256
[pcengines_apu3_seabios_v24.08.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v24.08.00.01/pcengines_apu3_seabios_v24.08.00.01.rom.sha256.sig
[pcengines_apu4_seabios_v24.08.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v24.08.00.01/pcengines_apu4_seabios_v24.08.00.01.rom.sha256
[pcengines_apu4_seabios_v24.08.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v24.08.00.01/pcengines_apu4_seabios_v24.08.00.01.rom.sha256.sig
[pcengines_apu6_seabios_v24.08.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v24.08.00.01/pcengines_apu6_seabios_v24.08.00.01.rom.sha256
[pcengines_apu6_seabios_v24.08.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/seabios/v24.08.00.01/pcengines_apu6_seabios_v24.08.00.01.rom.sha256.sig

## v24.05.00.01 - 2024-06-28

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit?usp=sharing).

### Added

- [apu2, apu3, apu4 and apu6 support added](https://github.com/Dasharo/dasharo-issues/issues/909)
- Rebased with official coreboot repository commit 5a0207e (tag 24.05)
- [coreboot 24.05: security/tpm: support compiling in multiple TPM drivers](https://doc.coreboot.org/releases/coreboot-24.05-relnotes.html#security-tpm-support-compiling-in-multiple-tpm-drivers)
- [coreboot 24.02 and 24.02.01: lib/rtc: Fix off-by-one error in February day count in leap year](https://doc.coreboot.org/releases/coreboot-24.02-relnotes.html#lib-rtc-fix-off-by-one-error-in-february-day-count-in-leap-year)
- coreboot 24.02 and 24.02.01: device: Add support for multiple PCI segment groups
- [coreboot 4.22 & 4.22.01 x86: Support CBFS cache for pre-memory stages and ramstage](https://doc.coreboot.org/releases/coreboot-4.22-relnotes.html#x86-support-cbfs-cache-for-pre-memory-stages-and-ramstage)
- [coreboot 4.21: libpayload/uhci: Re-write UHCI RH driver w/ generic_hub API](https://doc.coreboot.org/releases/coreboot-4.21-relnotes.html#libpayload-uhci-re-write-uhci-rh-driver-w-generic-hub-api)
- [coreboot 4.21: arch/x86: Don’t allow hw floating point operations](https://doc.coreboot.org/releases/coreboot-4.21-relnotes.html#arch-x86-don-t-allow-hw-floating-point-operations)
- [coreboot 4.21: Extracting of TPM logs using cbmem tool](https://doc.coreboot.org/releases/coreboot-4.21-relnotes.html#extracting-of-tpm-logs-using-cbmem-tool)
- [coreboot 4.21: soc/amd: read domain resource window configuration from hardware](https://doc.coreboot.org/releases/coreboot-4.21-relnotes.html#soc-amd-read-domain-resource-window-configuration-from-hardware)
- [coreboot 4.20.1: cpu/x86/smm: Add PCI resource store functionality](https://doc.coreboot.org/releases/coreboot-4.20.1-relnotes.html#cpu-x86-smm-add-pci-resource-store-functionality)
- [coreboot 4.20.1: drivers/usb/acpi: Add USB _DSM method to enable/disable USB LPM per port](https://doc.coreboot.org/releases/coreboot-4.20.1-relnotes.html#drivers-usb-acpi-add-usb-dsm-method-to-enable-disable-usb-lpm-per-port)
- [Code base was moved to Dasharo Patchqueue Initiative](https://github.com/Dasharo/dasharo-pq?tab=readme-ov-file#background)
- [Sign of Life date changed to 19700101 due to making Dasharo Patchqueue Initiative based build reproducible](https://github.com/Dasharo/dasharo-issues/issues/889)
- toolchain updates GCC 13.2.0, CMake 3.27.7
- ACPI 6.4 specification compliance
- sortbootorder update to v24.05.00.01

### Known issues

- [Limited test scope due to infrastructure recovery issues](https://github.com/Dasharo/dasharo-issues/issues/914)
- [apuled driver doesn't work in FreeBSD. Check the  GPIOs document for workaround.](https://github.com/pcengines/coreboot/issues/329)
- [Some PCIe cards are not detected on certain OSes and/or in certain mPCIe slots. Check the  mPCIe modules document for solution/workaround.](https://github.com/pcengines/apu2-documentation/issues/115)
- [Booting with 2 USB 3.x sticks plugged in apu4 sometimes results in detecting only 1 stick](https://github.com/pcengines/seabios/issues/30)
- [Certain USB 3.x sticks happen to not appear in boot menu](https://github.com/pcengines/seabios/issues/29)
- [Booting Xen 4.8 is unstable](https://github.com/pcengines/apu2-documentation/issues/109)

### Binaries

[sha256][pcengines_apu2_seabios_v24.05.00.01.rom_hash]{.md-button}
[sha256.sig][pcengines_apu2_seabios_v24.05.00.01.rom_sig]{.md-button}

[sha256][pcengines_apu3_seabios_v24.05.00.01.rom_hash]{.md-button}
[sha256.sig][pcengines_apu3_seabios_v24.05.00.01.rom_sig]{.md-button}

[sha256][pcengines_apu4_seabios_v24.05.00.01.rom_hash]{.md-button}
[sha256.sig][pcengines_apu4_seabios_v24.05.00.01.rom_sig]{.md-button}

[sha256][pcengines_apu6_seabios_v24.05.00.01.rom_hash]{.md-button}
[sha256.sig][pcengines_apu6_seabios_v24.05.00.01.rom_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/pcengines_apu2/dasharo-release-24.05.00.x-for-pc-engines-signing-key.asc)

### SBOM (Software Bill of Materials)

- [coreboot based on 24.05 revision 5a0207e](https://github.com/coreboot/coreboot/tree/5a0207e)
- [Dasharo Patchqueue Initiative based on 24.05.00.01 revision c86db36f](https://github.com/Dasharo/dasharo-pq/tree/c86db36f)
- [sortbootorder based on v24.05.00.01 revision a7c8b665](https://github.com/pcengines/sortbootorder/tree/a7c8b665)
- [iPXE based on 2024.05 revision e965f179](https://github.com/ipxe/ipxe/tree/e965f179)
- [Memtest86+ based on v002 revision 0bd34c22](https://review.coreboot.org/c/memtest86plus/+/29185)
- [AMD AGESA Binary Platform Initialization based on MullinsPI 1.0.0.A revision a8db7dfe](https://github.com/coreboot/blobs/tree/a8db7dfe/pi/amd/00730F01/FT3b)
- [AMD Platform Security Processor bootloader based on D.1.1.4D revision a8db7dfe](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/PSP/PspBootLoader.Bypass.sbin)
- [AMD Platform Security Processor firmware public key based on v1.0 revision a8db7dfe](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/PSP/AmdPubKey.bin)
- [AMD System Management Unit firmware based on 1433 revision a8db7dfe](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/PSP/SmuFirmware.sbin)
- [AMD System Management Unit - Software Configuration Settings binary based on 1433 revision a8db7dfe](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/PSP/SmuScs.bin)
- [AMD Hudson xHCI firmware based on 1.1.0.0068 revision a8db7dfe](https://github.com/coreboot/blobs/tree/a8db7dfe/southbridge/amd/avalon/xhci.bin)

[pcengines_apu2_seabios_v24.05.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu2_seabios_v24.05.00.01.rom.sha256
[pcengines_apu2_seabios_v24.05.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu2_seabios_v24.05.00.01.rom.sha256.sig
[pcengines_apu3_seabios_v24.05.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu3_seabios_v24.05.00.01.rom.sha256
[pcengines_apu3_seabios_v24.05.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu3_seabios_v24.05.00.01.rom.sha256.sig
[pcengines_apu4_seabios_v24.05.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu4_seabios_v24.05.00.01.rom.sha256
[pcengines_apu4_seabios_v24.05.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu4_seabios_v24.05.00.01.rom.sha256.sig
[pcengines_apu6_seabios_v24.05.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu6_seabios_v24.05.00.01.rom.sha256
[pcengines_apu6_seabios_v24.05.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu6_seabios_v24.05.00.01.rom.sha256.sig
