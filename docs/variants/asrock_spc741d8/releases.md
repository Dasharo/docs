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

## v0.9.3 - 2026-11-19

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/ASRock/SPC741D8-2L2T-BCM/).

### Added

- Support for early DMA protection
- Enabled boot media write protection
- ME/SPS FWSTS reporting via SMBIOS
- ACM version extraction in SBOM
- [UEFI Capsule Update v1 support with Capsule on Disk](https://docs.dasharo.com/unified-test-documentation/dasharo-stability/capsule-update/)

### Changed

- UEFI Secure Boot enabled by default
- Boot logo customization feature removed due security requirements
- Removed redundant measurement of PEI FV in UEFI Payload that could not be
  proven against event log
- Removed ephemeral Dasharo PK in favor of Windows OEM Devices PK to allow
  updates of KEK via OS
- SBOM now hold the hashes of rebased FSP components as placed in the ROM image
  instead of the split original parts

### Fixed

- [TXT HEAP and SINIT memory ranges not reserved](https://github.com/Dasharo/dasharo-issues/issues/1936)
- [Errors and unexpected messages printed during boot](https://github.com/Dasharo/dasharo-issues/issues/1609)
- BMC IPMI interface not functional
- Race condition in SBOM generation for Intel ACMs during build
- TPM Platform Hierarchy is not closed nor owned by firmware
- [SMM BIOS Write Protection enabled by default](https://github.com/Dasharo/dasharo-issues/issues/1921)
- [SHA-384 PCR 0 does not replay](https://github.com/Dasharo/dasharo-issues/issues/1944)
- [Flash regions are not sector aligned](https://github.com/Dasharo/dasharo-issues/issues/1945)
- [Boot Guard/TXT IBB measurements not logged as EV_S_CRTM_CONTENTS](https://github.com/Dasharo/dasharo-issues/issues/1946)
- [Missing SBOM entry for STM](https://github.com/Dasharo/dasharo-issues/issues/1947)
- Missing microcode update entry in SBOM for concatenated microcode blobs
- [Immediate BSOD trying to boot Windows](https://github.com/Dasharo/dasharo-issues/issues/1598)

### Known issues

- [Intruder switch significantly slows platform down when active](https://github.com/Dasharo/dasharo-issues/issues/1933)
- [USB mass storage devices not detected after warmboot or reboot](https://github.com/Dasharo/dasharo-issues/issues/1935)
- [SINIT ACM does not perform a measurement of an STM](https://github.com/Dasharo/dasharo-issues/issues/1934)
- [Large ME region size](https://github.com/Dasharo/dasharo-issues/issues/1586)
- [STB002.001 encounters unlisted error](https://github.com/Dasharo/dasharo-issues/issues/1013)

### Binaries

[sha256][asrock_spc741d8_v0.9.3_txt.rom_hash]{.md-button}
[sha256.sig][asrock_spc741d8_v0.9.3_txt.rom_sig]{.md-button}
(asrock_spc741d8_v0.9.3_txt.rom)

[asrock_spc741d8_v0.9.3_txt.sbom.json][asrock_spc741d8_v0.9.3_txt.sbom.json_file]{.md-button}
[sha256][asrock_spc741d8_v0.9.3_txt.sbom.json_hash]{.md-button}
[sha256.sig][asrock_spc741d8_v0.9.3_txt.sbom.json_sig]{.md-button}

This is a Dasharo Pro Package release. For this platform, access to pre-built
binaries is provided exclusively through the
[Full Build for ASRock Rack SPC741D8-2L2T/BCM](https://shop.3mdeb.com/product/asrock-spc741d8-2l2t-bcm-dasharo-pro-full-build/),
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
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/refs/heads/master/dasharo/asrock_spc741d8/dasharo-release-0.x-compatible-with-asrock-spc741d8-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.12 revision 7d6c9cdc](https://github.com/Dasharo/coreboot/tree/7d6c9cdc)
- [Dasharo EDKII fork based on edk2-stable202602 revision 0cacb9d1](https://github.com/Dasharo/edk2/tree/0cacb9d1)
- [Dasharo iPXE fork based on 2026.02 revision ad8cbcee](https://github.com/Dasharo/ipxe/tree/ad8cbcee)
    + [License](https://github.com/Dasharo/ipxe/blob/ad8cbcee/COPYING.GPLv2)
- [Intel Firmware Support Package for Eagle Stream version 1.1.1.395](https://github.com/intel/FSP/tree/7cb9638a/EagleStreamFspBinPkg)
    + [License](https://github.com/intel/FSP/tree/7cb9638a/FSP_License.pdf)
- [Intel Server Platform Services version v6.1.4.89.0](https://github.com/Dasharo/dasharo-blobs/blob/fbe0c65c/asrock/spc741d8/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.1](https://github.com/Dasharo/dasharo-blobs/blob/fbe0c65c/asrock/spc741d8/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel microcode version SPR-HBM 0x2c000435 02/03/2026](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20260925/intel-ucode/06-8f-08)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20260925/license)
- [Intel microcode version EMR-SP 0x210002f4 02/03/2026](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20260925/intel-ucode/06-cf-02)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20260925/license)

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

    All mandatory requirements are met. 1 recommendation can still be improved.

    | Area | What it covers | :material-close-circle:{ style="color: #ff5252" title="Failed" } Errors | :material-alert:{ style="color: #ff9100" title="Warning" } Warnings | :material-information:{ style="color: #448aff" title="Info" } Info |
    | --- | --- | :---: | :---: | :---: |
    | **Security Information** | How to report vulnerabilities and get security updates | 0 | 0 | 4 |
    | **Integrity Information** | Checksums that prove each component is unmodified | 0 | 0 | 2 |
    | **Document Metadata** | Who made the firmware and when the SBOM was created | 0 | 1 | 0 |

    **Errors** are serious gaps. **Warnings** are smaller gaps or
    recommendations; after a phase's deadline, missing items are reported as
    warnings too. **Info** findings are for reference only.

    ??? info "Show all findings"

        - :material-alert:{ style="color: #ff9100" title="Warning" }
          **CRA Art. 13(7) / Annex I Part II (1): SBOM freshness** (Document Metadata): SBOM has no creation timestamp; keep the documented component inventory current when components change
        - :material-information:{ style="color: #448aff" title="Info" }
          **CRA Annex I Part I (2)(f): Component integrity information (hash)** (Integrity Information): Component 'coreboot' missing cryptographic hash (recommended for integrity)
          *Components: coreboot, vboot*
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
    | **Integrity Information** | Checksums that prove each component is unmodified | 0 | 0 | 2 |
    | **Document Metadata** | Who made the firmware and when the SBOM was created | 0 | 1 | 1 |

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
          *Components: coreboot, vboot*
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

!!! info "HSI:2 (Risky State)"

    Remaining issues are only exploitable in theory or in a lab.

    [fwupd](https://fwupd.org) tested this firmware on real hardware and gave
    it a Host Security ID of **HSI:2**, level 2
    on a scale from 0 (Insecure) to 4 (Secure). Higher is better. To reach a
    level, the platform must pass all of the checks at that level and at all
    of the levels below it.
    [More about HSI](https://fwupd.github.io/libfwupdplugin/hsi.html).

| Level | What it covers | Checks passed | Result |
| --- | --- | :---: | :---: |
| **HSI-1**<br>Critical | The most basic protections, considered essential. A failure here could let an attacker compromise the firmware without physical access. | 12 / 12 | :material-check-circle:{ style="color: #00c853" title="Passed" } |
| **HSI-2**<br>Risky | Protection of the boot process against an attacker with local access. Failures here are theoretical or hard to exploit. | 4 / 4 | :material-check-circle:{ style="color: #00c853" title="Passed" } |
| **HSI-3**<br>Protected | Out-of-band protection of the firmware, possibly including recovery. | 3 / 4 | :material-close-circle:{ style="color: #ff5252" title="Failed" } |
| **HSI-4**<br>Secure | Encryption and execution protection for the firmware. | 1 / 2 | :material-close-circle:{ style="color: #ff5252" title="Failed" } |
| **Runtime (!)** | Security issues in the operating system that was running during the test, such as an unencrypted swap partition. They add a "!" to the result but never change the level. | 4 / 6 | :material-alert:{ style="color: #ff9100" title="Warning" } |

??? success "HSI-1 Critical: 12 of 12 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **BIOS firmware updates** | Firmware updates can be installed through the standard UEFI capsule mechanism. | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Platform debugging** | Hardware debugging interfaces are disabled and locked. | Disabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **SPI write** | The firmware flash chip is locked against writes from the OS. | Disabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **SPI lock** | The firmware flash chip is locked against writes from the OS. | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **SPI BIOS Descriptor** | The flash layout cannot be changed to unlock protected regions. | Locked |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **SPI BIOS region** | Only trusted firmware code (SMM) can write the flash chip. | Locked |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Supported CPU** | fwupd knows how to check the security of this processor. | Valid |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **TPM empty PCRs** | The firmware records every boot stage in the TPM. | Valid |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **TPM v2.0** | A TPM 2.0 security chip is present and usable. | Found |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **UEFI bootservice variables** | Firmware-internal UEFI variables cannot be changed from the OS. | Locked |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **UEFI platform key** | Secure Boot uses a valid, non-test platform key. | Valid |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **UEFI secure boot** | Only signed bootloaders and operating systems are allowed to start. | Enabled |

??? success "HSI-2 Risky: 4 of 4 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Intel GDS mitigation** |  | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **IOMMU** | Devices are restricted to the memory they are allowed to use (blocks DMA attacks, e.g. via Thunderbolt). | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Platform debugging** | Hardware debugging interfaces are disabled and locked. | Locked |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **TPM PCR0 reconstruction** | The TPM boot measurements match the firmware event log. | Valid |

??? failure "HSI-3 Protected: 3 of 4 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **CET Platform** | Control-flow Enforcement Technology, which blocks a common class of exploits, is available. | Supported |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Pre-boot DMA protection** | Devices cannot read or write memory through DMA before the OS has started. | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Suspend-to-ram** | The system does not use S3 sleep, during which memory is less protected. | Disabled |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Suspend-to-idle** | The system supports modern standby, which keeps protections active while asleep.<br>**Why it fails:** [issue 1](#hsi-issue-1) | Disabled |

??? failure "HSI-4 Secure: 1 of 2 checks passed"

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **SMAP** | The kernel is prevented from accidentally accessing user memory. | Enabled |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Encrypted RAM** | RAM contents are encrypted, protecting against cold-boot and bus snooping attacks.<br>**Why it fails:** [issue 2](#hsi-issue-2) | Disabled |

??? warning "Runtime: 4 of 6 checks passed"

    Security issues in the operating system that was running during the test, such as an unencrypted swap partition. They add a "!" to the result but never change the level.

    | | Check | What it checks | Status |
    | :---: | --- | --- | --- |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **fwupd plugins** | fwupd is running without third-party plugins. | Untainted |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Linux kernel lockdown** | The Linux kernel blocks root from modifying the running kernel. | Enabled |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **Linux kernel** | The Linux kernel has not loaded unsigned or proprietary modules. | Untainted |
    | :material-check-circle:{ style="color: #00c853" title="Passed" } | **UEFI db** | The Secure Boot allow-list is up to date. | Valid |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **CET OS Support** | The operating system uses Control-flow Enforcement Technology to block a common class of exploits.<br>**Why it fails:** [issue 3](#hsi-issue-3) | Not supported |
    | :material-close-circle:{ style="color: #ff5252" title="Failed" } | **Linux swap** | Swap space is encrypted, so memory contents are not written to disk in the clear.<br>**Why it fails:** [issue 4](#hsi-issue-4) | Unencrypted |

#### Why some checks fail

1. <a id="hsi-issue-1"></a>**Suspend-to-idle (HSI-3):** Suspend-to-idle is not
   supported on server platforms.
2. <a id="hsi-issue-2"></a>**Encrypted RAM (HSI-4):** [EagleStream FSP does not
   enable TME.](https://github.com/intel/FSP/issues/133)
3. <a id="hsi-issue-3"></a>**CET OS Support (Runtime):** [CET OS check is not reliable.](https://github.com/fwupd/fwupd/issues/10162)
4. <a id="hsi-issue-4"></a>**Linux swap (Runtime):** The swap partitions or
   image files are not encrypted by default on Linux.

??? abstract "Full `fwupdmgr security` output"

    ```text
    HSI-1
    ✔ BIOS firmware updates:         Enabled
    ✔ Platform debugging:            Disabled
    ✔ SPI write:                     Disabled
    ✔ SPI lock:                      Enabled
    ✔ SPI BIOS Descriptor:           Locked
    ✔ SPI BIOS region:               Locked
    ✔ Supported CPU:                 Valid
    ✔ TPM empty PCRs:                Valid
    ✔ TPM v2.0:                      Found
    ✔ UEFI bootservice variables:    Locked
    ✔ UEFI platform key:             Valid
    ✔ UEFI secure boot:              Enabled

    HSI-2
    ✔ Intel GDS mitigation:          Enabled
    ✔ IOMMU:                         Enabled
    ✔ Platform debugging:            Locked
    ✔ TPM PCR0 reconstruction:       Valid

    HSI-3
    ✔ CET Platform:                  Supported
    ✔ Pre-boot DMA protection:       Enabled
    ✔ Suspend-to-ram:                Disabled
    ✘ Suspend-to-idle:               Disabled

    HSI-4
    ✔ SMAP:                          Enabled
    ✘ Encrypted RAM:                 Disabled

    Runtime Suffix -!
    ✔ fwupd plugins:                 Untainted
    ✔ Linux kernel lockdown:         Enabled
    ✔ Linux kernel:                  Untainted
    ✔ UEFI db:                       Valid
    ✘ CET OS Support:                Not supported
    ✘ Linux swap:                    Unencrypted
    ```

[asrock_spc741d8_v0.9.3.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.3/asrock_spc741d8_v0.9.3.sbom.json
[asrock_spc741d8_v0.9.3.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.3/asrock_spc741d8_v0.9.3.sbom.json.sha256
[asrock_spc741d8_v0.9.3.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.3/asrock_spc741d8_v0.9.3.sbom.json.sha256.sig
[asrock_spc741d8_v0.9.3_txt.cap_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.3/asrock_spc741d8_v0.9.3_txt.cap.sha256
[asrock_spc741d8_v0.9.3_txt.cap_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.3/asrock_spc741d8_v0.9.3_txt.cap.sha256.sig
[asrock_spc741d8_v0.9.3_txt.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.3/asrock_spc741d8_v0.9.3_txt.rom.sha256
[asrock_spc741d8_v0.9.3_txt.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.3/asrock_spc741d8_v0.9.3_txt.rom.sha256.sig
[asrock_spc741d8_v0.9.3_txt.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.3/asrock_spc741d8_v0.9.3_txt.sbom.json
[asrock_spc741d8_v0.9.3_txt.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.3/asrock_spc741d8_v0.9.3_txt.sbom.json.sha256
[asrock_spc741d8_v0.9.3_txt.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.3/asrock_spc741d8_v0.9.3_txt.sbom.json.sha256.sig

## v0.9.1 - 2026-10-15

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
- [SecureBoot can't boot file signed with custom PK](https://github.com/Dasharo/dasharo-issues/issues/1610)

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

[asrock_spc741d8_v0.9.1.sbom.json][asrock_spc741d8_v0.9.1.sbom.json_file]{.md-button}
[sha256][asrock_spc741d8_v0.9.1.sbom.json_hash]{.md-button}
[sha256.sig][asrock_spc741d8_v0.9.1.sbom.json_sig]{.md-button}
[sha256][asrock_spc741d8_v0.9.1_txt.rom_hash]{.md-button}
[sha256.sig][asrock_spc741d8_v0.9.1_txt.rom_sig]{.md-button}
(asrock_spc741d8_v0.9.1_txt.rom)

This is a Dasharo Pro Package release. For this platform, access to pre-built
binaries is provided exclusively through the
[Full Build for ASRock Rack SPC741D8-2L2T/BCM](https://shop.3mdeb.com/product/asrock-spc741d8-2l2t-bcm-dasharo-pro-full-build/),
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

- [Dasharo coreboot fork based on 25.12 revision 1de5aa93](https://github.com/Dasharo/coreboot/tree/1de5aa93)
- [Dasharo EDKII fork based on edk2-stable202502 revision bdb92c0e](https://github.com/Dasharo/edk2/tree/bdb92c0e)
- [Dasharo iPXE fork based on 2025.03 revision ad8cbcee](https://github.com/Dasharo/ipxe/tree/ad8cbcee)
    + [License](https://github.com/Dasharo/ipxe/blob/ad8cbcee/COPYING.GPLv2)
- [Intel Firmware Support Package for Eagle Stream version 0115.D.05](https://github.com/intel/FSP/tree/7cb9638a/EagleStreamFspBinPkg)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Server Platform Services version v6.1.4.89.0](https://github.com/Dasharo/dasharo-blobs/blob/69f6817e/asrock/spc741d8/me.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel Flash Descriptor version v1.0](https://github.com/Dasharo/dasharo-blobs/blob/69f6817e/asrock/spc741d8/descriptor.bin)
    + [License](https://github.com/Dasharo/dasharo-blobs/blob/main/licenses/pv%20intel%20obl%20software%20license%20agreement%2011.2.2017.pdf)
- [Intel microcode version SPR-HBM 0x2c000435 02/03/2026](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20260812/intel-ucode/06-8f-08)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20260812/license)
- [Intel microcode version EMR-SP 0x210002f4 02/03/2026](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20260812/intel-ucode/06-cf-02)
    + [License](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/blob/microcode-20260812/license)

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

[asrock_spc741d8_v0.9.1.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.1/asrock_spc741d8_v0.9.1.sbom.json
[asrock_spc741d8_v0.9.1.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.1/asrock_spc741d8_v0.9.1.sbom.json.sha256
[asrock_spc741d8_v0.9.1.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_spc741d8/uefi/v0.9.1/asrock_spc741d8_v0.9.1.sbom.json.sha256.sig
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
