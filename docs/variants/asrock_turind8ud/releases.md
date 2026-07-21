# ASRock Rack TURIND8UD-2T/X550 Dasharo Release Notes

Following Release Notes describe status of open-source firmware development for
ASRock Rack TURIND8UD-2T/X550

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>

{{ subscribe_form("3d024561-472f-4fd3-9cf1-ba070be56862",
"Subscribe to ASRock Rack TURIND8UD-2T/X550 Dasharo Release Newsletter") }}

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

## v0.9.0 - 2026-07-21

Test results for this release can be found
[here](https://github.com/Dasharo/osfv-results/blob/main/boards/ASRock/TURIND8UD/).

### Added

- Initial support for the ASRock Rack TURIND8UD-2T/X550 platform
- [LinuxBoot payload support](https://www.linuxboot.org/)
- [Support for discrete TPM](https://docs.dasharo.com/unified-test-documentation/dasharo-security/200-tpm-support/)
- [NVMe boot support](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/312-nvme-support/)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [Ubuntu LTS booting](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/308-debian-stable-and-ubuntu-lts-support/)
- [Serial port console redirection](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/31G-ec-and-superio/#sio004001-serial-port-in-firmware)
- [SMM BIOS write protection](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [SBOM generation for AMD PSP blobs](https://doc.coreboot.org/sbom/sbom.html)
- LinuxBoot console on COM1, BMC VGA and BMC SOL
- AMD SME and AMD SEV-SNP support
- Rebased coreboot on 25.12 tag
- AMD memory context save/restore support
- SMBIOS 3.8.0 specification support
- AMD PSP HSTI reporting
- AMD CPU temperature reporting via ACPI Thermal Zone

### Known issues

- [I3C controller initialization fails in Linux](https://github.com/Dasharo/dasharo-issues/issues/1845)

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
for this platform; additional purchase options (Enterprise Build and Barebones
Build) are expected in the next 3-6 months.

With the Full Build, you receive firmware updates for the duration of your
subscription via the Dasharo Pro Package newsletter, and gain entry to the
Dasharo Premier Support invite-only live chat on the Matrix network, enabling
direct engagement with the Dasharo Team and fellow subscribers for
personalized, priority assistance.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/refs/heads/master/dasharo/asrock_turind8ud/dasharo-release-0.x-compatible-with-asrock-turind8ud-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo coreboot fork based on 25.12 revision 9e3f8181](https://github.com/Dasharo/coreboot/tree/9e3f8181)
- [Linux kernel based on v6.19 revision v6.19](https://github.com/torvalds/linux/tree/v6.19)
    + [License](https://github.com/torvalds/linux/blob/master/LICENSES/preferred/GPL-2.0)
- [AMD openSIL based on turin_poc revision 67b35db3](https://github.com/openSIL/openSIL/tree/67b35db3)
    + [License](https://github.com/openSIL/openSIL/blob/genoa_poc/LICENSE/MIT-License.txt)

An [integrated SBOM](https://doc.coreboot.org/sbom/sbom.html) is also
included in the firmware images. It describes a complete set of components
and their versions used to build the firmware images. The published SBOM
artifact is in CycloneDX format and can be viewed by SBOM tools, for example
[sbom-tools](https://github.com/sbom-tool/sbom-tools).

[asrock_turind8ud_v0.9.0.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_turind8ud/linuxboot/v0.9.0/asrock_turind8ud_v0.9.0.rom.sha256
[asrock_turind8ud_v0.9.0.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_turind8ud/linuxboot/v0.9.0/asrock_turind8ud_v0.9.0.rom.sha256.sig

[asrock_turind8ud_v0.9.0.sbom.json_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_turind8ud/linuxboot/v0.9.0/asrock_turind8ud_v0.9.0.sbom.json
[asrock_turind8ud_v0.9.0.sbom.json_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_turind8ud/linuxboot/v0.9.0/asrock_turind8ud_v0.9.0.sbom.json.sha256
[asrock_turind8ud_v0.9.0.sbom.json_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/asrock_turind8ud/linuxboot/v0.9.0/asrock_turind8ud_v0.9.0.sbom.json.sha256.sig
