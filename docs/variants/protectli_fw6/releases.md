# Protectli FW6 Dasharo Release Notes

Following Release Notes describe status of Open Source Firmware development
for Protectli FW6.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

{{ subscribe_form("49abc4a2-0807-4720-aef2-b150ef701b30",
"Subscribe to Protectli Dasharo Release Newsletter") }}

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit?usp=sharing).

## v1.0.14 - 2022-05-13

### Added

- Initial support for the Protectli FW6 platform
- SeaBIOS/legacy boot support
- iPXE Network Boot support
- [Protectli boot logo](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/304-custom-logo/)
- Throttling temperature to 75 Celsius degrees

### Known issues

- Samsung memory modules do not work properly on older FW6A/B/C (SKU6LAV20)

### Binaries

[protectli_vault_kbl_v1.0.14.rom][v1.0.14_rom]{.md-button}
[sha256][v1.0.14_hash]{.md-button}
[sha256.sig][v1.0.14_sig]{.md-button}

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](../../guides/signature-verification.md)
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

[v1.0.14_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_kbl/v1.0.14/protectli_vault_kbl_v1.0.14.rom
[v1.0.14_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_kbl/v1.0.14/protectli_vault_kbl_v1.0.14.rom.sha256
[v1.0.14_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_kbl/v1.0.14/protectli_vault_kbl_v1.0.14.rom.sha256.sig

## v1.0.0 .. v1.0.13: Non-public engineering releases
