# ASRock Rack TURIND8UD-2T/X550 Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
ASRock Rack TURIND8UD-2T/X550

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

{{ subscribe_form("3d024561-472f-4fd3-9cf1-ba070be56862",
"Subscribe to ASRock Rack TURIND8UD-2T/X550 Dasharo (coreboot+LinuxBoot)
Release Newsletter") }}

{{ subscribe_form("17705dae-3106-4f58-9d12-bf048bf57400",
"Subscribe to ASRock Rack TURIND8UD-2T/X550 Dasharo (coreboot+UEFI)
Release Newsletter") }}

</center>

!!! note "Note"

    Before using this firmware, please review the [Dasharo Terms of
    Service](https://www.dasharo.com/pages/terms/) and AMD's [openSIL project
    page](https://github.com/openSIL/openSIL), which describes openSIL's
    current Proof-of-Concept status and AMD's evaluation-only support model.
    Use of this firmware is at the user's own responsibility.

!!! note "Dasharo Pro Package"

    This is a Dasharo Pro Package (DPP) release. The pre-built binaries are
    not publicly available. Access is provided through the
    [BenchRack ASRock TURIND8UD-2T/X550 with Dasharo Pro Package for Servers](https://shop.3mdeb.com/product/benchrack-asrock-turind8ud-2t-x550-with-dasharo-pro-package-for-servers/)
    product in the 3mdeb shop, or by otherwise
    [becoming a Dasharo Pro Package subscriber](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
    As a subscriber you receive access to all firmware updates for the
    duration of your subscription via the Dasharo Pro Package newsletter, and
    gain entry to the Dasharo Premier Support invite-only live chat on the
    Matrix network, enabling direct engagement with the Dasharo Team and
    fellow subscribers for personalized, priority assistance. See the
    [Dasharo Pro Package FAQ](../../osf-trivia-list/dasharo-pro-package.md)
    for more details.

## v0.9.0 - 2026-08-13

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/ASRock/TURIND8UD/UEFI/).

### Added

- Initial support for the ASRock Rack TURIND8UD server board, based on AMD Turin
- [UEFI compatible interface](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30M-uefi-compatible-interface/)
- [Configurable boot order](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/325-custom-boot-order/)
- [Configurable boot options](https://docs.dasharo.com/dasharo-menu-docs/boot-maintenance-mgr/#boot-options)
- [UEFI Secure Boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [USB boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31N-usb-boot/)
- [NVMe boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/312-nvme-support/)
- [Ubuntu LTS booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support/)
- [Windows 11 booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31A-windows-booting/)
- [Serial port console redirection](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31G-ec-and-superio/#sio004001-serial-port-in-firmware)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [SMM BIOS write protection with AMD ROM Armor](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [Firmware Update Mode](https://docs.dasharo.com/guides/firmware-update/#firmware-update-mode)
- [Setup menu password configuration](https://docs.dasharo.com/dasharo-menu-docs/overview/#dasharo-menu-guides)
- [USB stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Network stack disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#networking-options)
- TPM PPI support with UEFI variable backend
- [SBOM generation for AMD PSP blobs](https://doc.coreboot.org/sbom/sbom.html)
- [AMD SME and AMD SEV-SNP support](https://docs.dasharo.com/kb/amd-security-features/#amd-sev-snp)
- Rebased coreboot on 25.12 tag
- Rebased iPXE on last commit of February 2026
- [Option to customize the SMBIOS Serial Number and UUID](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/362-dcu/)
- [TCG OPAL disk password support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/208-opal-disk-password-support/)
- [Boot manager menu disable option](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20P-boot-menu/)
- [Auto boot option creation for pre-installed OSes](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/361-esp-scanning/)
- [Quiet boot/Fast boot options](https://docs.dasharo.com/dasharo-menu-docs/boot-maintenance-mgr/)
- AMD memory context save/restore support
- [SMBIOS 3.8.0 specification support](https://www.dmtf.org/content/dmtf-releases-smbios-38)
- AMD PSP HSTI reporting to reach fwupd HSI2 level and fulfill HSI4 requirements
- AMD CPU temperature reporting via ACPI Thermal Zone

### Known issues

- [Previous power state restoration does not work for powered off state](https://github.com/Dasharo/dasharo-issues/issues/1844)
- [I3C controller initialization fails in Linux](https://github.com/Dasharo/dasharo-issues/issues/1845)
- [Fast Boot does not significantly reduce boot time](https://github.com/Dasharo/dasharo-issues/issues/1841)
- [Firmware flashing and reset to defaults do not give the same measurements](https://github.com/Dasharo/dasharo-issues/issues/1842)

### Binaries

#### Raw Dasharo image

[sha256][asrock_turind8ud_v0.9.0.rom_hash]{.md-button}
[sha256.sig][asrock_turind8ud_v0.9.0.rom_sig]{.md-button}
(asrock_turind8ud_v0.9.0.rom)

#### SBOM CycloneDX

[asrock_turind8ud_v0.9.0.sbom.json][asrock_turind8ud_v0.9.0.sbom.json_file]{.md-button}
[sha256][asrock_turind8ud_v0.9.0.sbom.json_hash]{.md-button}
[sha256.sig][asrock_turind8ud_v0.9.0.sbom.json_sig]{.md-button}

This is a Dasharo Pro Package release. For this platform, access to pre-built
binaries is provided exclusively through the
[Full Build for ASRock Rack TURIND8UD-2T/X550](https://shop.3mdeb.com/product/full-build-asrock-turind8ud-2t-x550-with-dasharo-pro-package-for-servers/),
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
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/refs/heads/master/dasharo/asrock_turind8ud/dasharo-release-0.x-compatible-with-asrock-turind8ud-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.12 revision 114ce55b](https://github.com/Dasharo/coreboot/tree/114ce55b)
- [AMD openSIL based on turin_poc revision 67b35db3](https://github.com/openSIL/openSIL/tree/67b35db3)
    + [License](https://github.com/openSIL/openSIL/blob/genoa_poc/LICENSE/MIT-License.txt)

An [integrated SBOM](https://doc.coreboot.org/sbom/sbom.html) is also
included in the firmware images. It describes a complete set of components
and their versions used to build the firmware images. The published SBOM
artifact is in CycloneDX format and can be viewed by SBOM tools, for example
[sbom-tools](https://github.com/sbom-tool/sbom-tools).

### EU Cyber Resilience Act (CRA)

The [EU Cyber Resilience Act](https://eur-lex.europa.eu/eli/reg/2024/2847/oj)
requires manufacturers to document what their products are made of and how
they handle security issues. This release ships a Software Bill of Materials
(SBOM) that lists every firmware component. We check it against the CRA
requirements with [sbom-tools](https://github.com/sbom-tool/sbom-tools).

!!! success "EU CRA Phase 1 (2026): Compliant"

    *Vulnerability and incident reporting (Article 14): how security issues are reported to us and how we notify the authorities. Applies from 11 September 2026.*

    All mandatory requirements are met. 5 recommendations can still be improved.

    | Area | What it covers | :material-close-circle:{ style="color: #ff5252" title="Failed" } Errors | :material-alert:{ style="color: #ff9100" title="Warning" } Warnings | :material-information:{ style="color: #448aff" title="Info" } Info |
    | --- | --- | :---: | :---: | :---: |
    | **Security Information** | How to report vulnerabilities and get security updates | 0 | 4 | 3 |
    | **Integrity Information** | Checksums that prove each component is unmodified | 0 | 0 | 3 |
    | **Document Metadata** | Who made the firmware and when the SBOM was created | 0 | 1 | 0 |
    | **License Information** | Under which licenses each component is distributed | 0 | 0 | 1 |

    **Errors** are serious gaps. **Warnings** are smaller gaps or
    recommendations; after a phase's deadline, missing items are reported as
    warnings too. **Info** findings are for reference only.

    ??? info "Show all findings"

        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 13(7) / Annex I Part II (1): SBOM freshness** (Document Metadata): SBOM has no creation timestamp; keep the documented component inventory current when components change
        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 13(17): Vulnerability disclosure contact** (Security Information): SBOM should include a security contact or vulnerability disclosure reference
        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 14(2)(a): 24-hour early-warning channel** (Security Information): 24-hour early-warning channel missing — required when an actively-exploited vulnerability is identified
        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 14(2)(b): 72-hour notification channel** (Security Information): 72-hour notification channel missing — required for actively exploited vulnerabilities and severe incidents
        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 14: PSIRT contact for external vulnerability reports** (Security Information): PSIRT URL missing — required to handle external vulnerability reports
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex I Part I (2)(f): Component integrity information (hash)** (Integrity Information): Component 'coreboot' missing cryptographic hash (recommended for integrity)
          *Components: coreboot, AMD openSIL, GCC*
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Art. 13(5): Third-party due diligence (license tracking)** (License Information): 1/87 components (1%) missing license information needed to evidence third-party due diligence
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex I Part II (1): Documented vulnerability information** (Security Information): No vulnerability data or vulnerability assertion found; include vulnerability information or a statement of no known vulnerabilities
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Art. 13(8) / 13(19): Support period disclosure** (Security Information): Consider specifying a support end date for security updates
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Art. 14(7): ENISA single reporting platform** (Security Information): No ENISA single reporting platform identifier — track ENISA publication and add `enisaReportingPlatformId` to the CRA sidecar when available

!!! success "EU CRA Phase 2 (2027): Compliant"

    *All CRA requirements for products sold in the EU, including a complete SBOM, security updates and a support period. Applies from 11 December 2027.*

    All mandatory requirements are met. 7 recommendations can still be improved.

    | Area | What it covers | :material-close-circle:{ style="color: #ff5252" title="Failed" } Errors | :material-alert:{ style="color: #ff9100" title="Warning" } Warnings | :material-information:{ style="color: #448aff" title="Info" } Info |
    | --- | --- | :---: | :---: | :---: |
    | **Security Information** | How to report vulnerabilities and get security updates | 0 | 5 | 4 |
    | **Integrity Information** | Checksums that prove each component is unmodified | 0 | 0 | 3 |
    | **Document Metadata** | Who made the firmware and when the SBOM was created | 0 | 2 | 1 |
    | **License Information** | Under which licenses each component is distributed | 0 | 0 | 1 |

    **Errors** are serious gaps. **Warnings** are smaller gaps or
    recommendations; after a phase's deadline, missing items are reported as
    warnings too. **Info** findings are for reference only.

    ??? info "Show all findings"

        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 13(2): Documented risk assessment** (Document Metadata): No documented risk assessment referenced — add an externalReference of type 'risk-assessment' or supply riskAssessmentUrl in the CRA sidecar
        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 13(7) / Annex I Part II (1): SBOM freshness** (Document Metadata): SBOM has no creation timestamp; keep the documented component inventory current when components change
        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Annex I Part II (5): Coordinated vulnerability disclosure policy** (Security Information): SBOM should reference a coordinated vulnerability disclosure policy (advisories URL or disclosure URL)
        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 13(17): Vulnerability disclosure contact** (Security Information): SBOM should include a security contact or vulnerability disclosure reference
        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 14(2)(a): 24-hour early-warning channel** (Security Information): 24-hour early-warning channel missing — required when an actively-exploited vulnerability is identified
        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 14(2)(b): 72-hour notification channel** (Security Information): 72-hour notification channel missing — required for actively exploited vulnerabilities and severe incidents
        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 14: PSIRT contact for external vulnerability reports** (Security Information): PSIRT URL missing — required to handle external vulnerability reports
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex V: EU Declaration of Conformity reference** (Document Metadata): Missing reference to the EU Declaration of Conformity (attestation or certification external reference) for product class Default
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex I Part I (2)(f): Component integrity information (hash)** (Integrity Information): Component 'coreboot' missing cryptographic hash (recommended for integrity)
          *Components: coreboot, AMD openSIL, GCC*
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Art. 13(5): Third-party due diligence (license tracking)** (License Information): 1/87 components (1%) missing license information needed to evidence third-party due diligence
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex I Part II (1): Documented vulnerability information** (Security Information): No vulnerability data or vulnerability assertion found; include vulnerability information or a statement of no known vulnerabilities
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex II (7): Component lifecycle status** (Security Information): Consider including component lifecycle/end-of-support information
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Art. 13(8) / 13(19): Support period disclosure** (Security Information): Consider specifying a support end date for security updates
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Art. 14(7): ENISA single reporting platform** (Security Information): No ENISA single reporting platform identifier — track ENISA publication and add `enisaReportingPlatformId` to the CRA sidecar when available

### Platform security (fwupd HSI)

!!! warning "HSI:1 (Critical State)"

    Basic protection is in place, but a failure at the next level would still have a critical security impact.

    [fwupd](https://fwupd.org) tested this firmware on real hardware and gave
    it a Host Security ID of **HSI:1**, level 1
    on a scale from 0 (Insecure) to 4 (Secure). Higher is better. To reach a
    level, the platform must pass all of the checks at that level and at all
    of the levels below it.
    [More about HSI](https://fwupd.github.io/libfwupdplugin/hsi.html).

| Level | What it covers | Checks passed | Result |
| --- | --- | :---: | :---: |
| **HSI-1**<br>Critical | The most basic protections, considered essential. A failure here could let an attacker compromise the firmware without physical access. | 6 / 6 | :material-check-circle:{ style="color: #00c853" title="Passed" } |
| **HSI-2**<br>Risky | Protection of the boot process against an attacker with local access. Failures here are theoretical or hard to exploit. | 3 / 5 | :material-close-circle:{ style="color: #ff5252" title="Failed" } |
| **HSI-3**<br>Protected | Out-of-band protection of the firmware, possibly including recovery. | 2 / 5 | :material-close-circle:{ style="color: #ff5252" title="Failed" } |
| **HSI-4**<br>Secure | Encryption and execution protection for the firmware. | 2 / 3 | :material-close-circle:{ style="color: #ff5252" title="Failed" } |
| **Runtime (!)** | Security issues in the operating system that was running during the test, such as an unencrypted swap partition. They add a "!" to the result but never change the level. | 2 / 5 | :material-alert:{ style="color: #ff9100" title="Warning" } |

??? success "HSI-1 Critical: 6 of 6 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **SMM locked down** | System Management Mode, the most privileged CPU mode, is locked down. | Locked |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **BIOS firmware updates** | Firmware updates can be installed through the standard UEFI capsule mechanism. | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Fused platform** | The chipset is in its locked, production configuration. | Locked |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Supported CPU** | fwupd knows how to check the security of this processor. | Valid |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **TPM empty PCRs** | The firmware records every boot stage in the TPM. | Valid |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **TPM v2.0** | A TPM 2.0 security chip is present and usable. | Found |

??? failure "HSI-2 Risky: 3 of 5 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **IOMMU** | Devices are restricted to the memory they are allowed to use (blocks DMA attacks, e.g. via Thunderbolt). | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Platform debugging** | Hardware debugging interfaces are disabled and locked. | Locked |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **TPM PCR0 reconstruction** | The TPM boot measurements match the firmware event log. | Valid |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Platform secure boot** | The processor only runs firmware signed with the platform vendor's key (AMD PSB).<br>**Why it fails:** [issue 1](#hsi-issue-1) | Disabled |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **SPI write protection** | The firmware flash chip is locked against writes from the OS.<br>**Why it fails:** [issue 2](#hsi-issue-2) | Disabled |

??? failure "HSI-3 Protected: 2 of 5 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **CET Platform** | Control-flow Enforcement Technology, which blocks a common class of exploits, is available. | Supported |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Suspend-to-ram** | The system does not use S3 sleep, during which memory is less protected. | Disabled |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **SPI replay protection** | The flash chip rejects replayed writes, so old firmware cannot be written back.<br>**Why it fails:** [issue 3](#hsi-issue-3) | Not supported |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Pre-boot DMA protection** | Devices cannot read or write memory through DMA before the OS has started.<br>**Why it fails:** [issue 4](#hsi-issue-4) | Disabled |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Suspend-to-idle** | The system supports modern standby, which keeps protections active while asleep.<br>**Why it fails:** [issue 5](#hsi-issue-5) | Disabled |

??? failure "HSI-4 Secure: 2 of 3 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Processor rollback protection** | The platform refuses to run older, possibly vulnerable firmware. | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **SMAP** | The kernel is prevented from accidentally accessing user memory. | Enabled |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Encrypted RAM** | RAM contents are encrypted, protecting against cold-boot and bus snooping attacks.<br>**Why it fails:** [issue 6](#hsi-issue-6) | Not supported |

??? warning "Runtime: 2 of 5 checks passed"

    Security issues in the operating system that was running during the test, such as an unencrypted swap partition. They add a "!" to the result but never change the level.

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **fwupd plugins** | fwupd is running without third-party plugins. | Untainted |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Linux kernel** | The Linux kernel has not loaded unsigned or proprietary modules. | Untainted |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **CET OS Support** | The operating system uses Control-flow Enforcement Technology to block a common class of exploits. | Not supported |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Linux kernel lockdown** | The Linux kernel blocks root from modifying the running kernel. | Disabled |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Linux swap** | Swap space is encrypted, so memory contents are not written to disk in the clear. | Unencrypted |

#### Why some checks fail

1. <a id="hsi-issue-1"></a>**Platform secure boot (HSI-2):** [Platform Secure
Boot is currently not implemented in Dasharo firmware.](https://github.com/Dasharo/dasharo-issues/issues/1950)
2. <a id="hsi-issue-2"></a>**SPI write protection (HSI-2):** SPI Write
Protection is not enabled by default in UEFI settings and must be enabled manually.
3. <a id="hsi-issue-3"></a>**SPI replay protection (HSI-3):** SPI Replay
Protection (RPMC) is unsupported by the board's SPI BIOS chip.
4. <a id="hsi-issue-4"></a>**Pre-boot DMA protection (HSI-3):** [Pre-boot DMA
protection is currently not supported for AMD platforms in Dasharo firmware.](https://github.com/Dasharo/dasharo-issues/issues/1903)
5. <a id="hsi-issue-5"></a>**Suspend-to-idle (HSI-3):** Suspend-to-idle isn't
supported on server hardware.
6. <a id="hsi-issue-6"></a>**Encrypted RAM (HSI-4):** [fwupdtool --security does
not correctly detect server RAM encryption](https://github.com/Dasharo/dasharo-issues/issues/1920)

??? abstract "Full `fwupdmgr security` output"

    ```text
    HSI-1
    ✔ SMM locked down:               Locked
    ✔ BIOS firmware updates:         Enabled
    ✔ Fused platform:                Locked
    ✔ Supported CPU:                 Valid
    ✔ TPM empty PCRs:                Valid
    ✔ TPM v2.0:                      Found

    HSI-2
    ✔ IOMMU:                         Enabled
    ✔ Platform debugging:            Locked
    ✔ TPM PCR0 reconstruction:       Valid
    ✘ Platform secure boot:          Disabled
    ✘ SPI write protection:          Disabled

    HSI-3
    ✔ CET Platform:                  Supported
    ✔ Suspend-to-ram:                Disabled
    ✘ SPI replay protection:         Not supported
    ✘ Pre-boot DMA protection:       Disabled
    ✘ Suspend-to-idle:               Disabled

    HSI-4
    ✔ Processor rollback protection: Enabled
    ✔ SMAP:                          Enabled
    ✘ Encrypted RAM:                 Not supported

    Runtime Suffix -!
    ✔ fwupd plugins:                 Untainted
    ✔ Linux kernel:                  Untainted
    ✘ CET OS Support:                Not supported
    ✘ Linux kernel lockdown:         Disabled
    ✘ Linux swap:                    Unencrypted
    ```

[asrock_turind8ud_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_turind8ud/uefi/v0.9.0/asrock_turind8ud_v0.9.0.rom.sha256
[asrock_turind8ud_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_turind8ud/uefi/v0.9.0/asrock_turind8ud_v0.9.0.rom.sha256.sig

[asrock_turind8ud_v0.9.0.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_turind8ud/uefi/v0.9.0/asrock_turind8ud_v0.9.0.sbom.json
[asrock_turind8ud_v0.9.0.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_turind8ud/uefi/v0.9.0/asrock_turind8ud_v0.9.0.sbom.json.sha256
[asrock_turind8ud_v0.9.0.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_turind8ud/uefi/v0.9.0/asrock_turind8ud_v0.9.0.sbom.json.sha256.sig
