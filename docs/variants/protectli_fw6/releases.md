# Release Notes

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

See how to verify signatures on [this video](https://asciinema.org/a/388861)

### SBOM (Software Bill of Materials)

- [coreboot based on 87f9fc85 revision e04b0ac8](https://github.com/Dasharo/coreboot/commits/e04b0ac8)
- [seabios based on v1.0.6 revision 03bcdcaf](https://github.com/Dasharo/SeaBIOS/commits/03bcdcaf)
- [ipxe based on 2019.3 stable revision ebf2eaf5](https://github.com/ipxe/ipxe/commits/ebf2eaf5)
- [memtest based on v002 revision dd5b4ff2](https://review.coreboot.org/plugins/gitiles/memtest86plus/+/dd5b4ff2)

[newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
[v1.0.14_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_kbl/v1.0.14/protectli_vault_kbl_v1.0.14.rom
[v1.0.14_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_kbl/v1.0.14/protectli_vault_kbl_v1.0.14.rom.sha256
[v1.0.14_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_kbl/v1.0.14/protectli_vault_kbl_v1.0.14.rom.sha256.sig
