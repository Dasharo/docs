# Release Notes

Following Release Notes describe status of open-source firmware development for
Protectli VP2410 family.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>
[Subscribe to Protectli VP2410 Dasharo Release Newsletter]
[newsletter]{.md-button .md-button--primary .center}
</center>

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit#gid=975611333).

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

How to verify signatures:

```bash
wget https://github.com/protectli-root/protectli-firmware-updater/raw/main/images/protectli_vp2410_DF_v1.0.15.rom -O protectli_vault_glk_v1.0.15.rom
wget https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.0.15/protectli_vault_glk_v1.0.15.rom.sha256
wget https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.0.15/protectli_vault_glk_v1.0.15.rom.sha256.sig
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/3mdeb-dasharo-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/protectli-dasharo-firewall-release-1.0-key.asc
gpg --list-sigs "3mdeb Master Key" "3mdeb Dasharo Master Key" "Protectli Dasharo Firewall Release 1.0 Signing Key"
sha256sum -c protectli_vault_glk_v1.0.15.rom.sha256
gpg -v --verify protectli_vault_glk_v1.0.15.rom.sha256.sig protectli_vault_glk_v1.0.15.rom.sha256
```

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
[v1.0.15_rom]: https://github.com/protectli-root/protectli-firmware-updater/raw/main/images/protectli_vp2410_DF_v1.0.15.rom
[v1.0.15_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.0.15/protectli_vault_glk_v1.0.15.rom.sha256
[v1.0.15_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_glk/v1.0.15/protectli_vault_glk_v1.0.15.rom.sha256.sig
