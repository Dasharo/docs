# Release Notes

Following Release Notes describe status of open-source firmware development for
Protectli VP2420 family.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>
[Subscribe to Protectli VP2420 Dasharo Release Newsletter]
[newsletter]{.md-button .md-button--primary .center}
</center>

Test results for this platform can be found
[here](https://docs.google.com/spreadsheets/d/1wI0qBSLdaluayYsm_lIa9iJ9LnPnCOZ9eNOyrKSc-j4/edit#gid=975611333).

## v1.0.1 - 2023-02-02

### Added

- [TPM 2.0 support over SPI interface](https://docs.dasharo.com/unified-test-documentation/dasharo-security/200-tpm-support/#test-cases-common-documentation)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)

### Changed

- Downgrade edk2 Secure Boot driver to achieve consistent user experience as on the VP46XX v1.0.19 release

### Fixed

- [Dasharo BIOS lock menu is missing](https://github.com/Dasharo/dasharo-issues/issues/291)
- [iPXE entry doesn't occur in setup menu](https://github.com/Dasharo/dasharo-issues/issues/289)
- [Impossibility of pfSense/OPNsense console versions installation](https://github.com/Dasharo/dasharo-issues/issues/289)

### Known issues

- [Popup with information about recovery mode is still displayed after flashing with a valid binary](https://github.com/Dasharo/dasharo-issues/issues/320)
- [pfSense boot time](https://github.com/Dasharo/dasharo-issues/issues/318)
- [Double characters in pfSense initial boot phase](https://github.com/Dasharo/dasharo-issues/issues/319)

### Binaries

[protectli_vp2420_v1.0.1.rom][protectli_vp2420_v1.0.1.rom_file]{.md-button}
[sha256][protectli_vp2420_v1.0.1.rom_hash]{.md-button}
[sha256.sig][protectli_vp2420_v1.0.1.rom_sig]{.md-button}

See how to verify signatures on [this video](https://asciinema.org/a/388861)

### SBOM (Software Bill of Materials)

- [coreboot based on c86c926 revision 54cbbc5b](https://github.com/Dasharo/coreboot/tree/54cbbc5b)
- [edk2 based on 7f90b9cd revision e31b7a71](https://github.com/Dasharo/edk2/tree/e31b7a71)

[newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
[protectli_vp2420_v1.0.1.rom_file]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.1/protectli_vp2420_v1.0.1.rom
[protectli_vp2420_v1.0.1.rom_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.1/protectli_vp2420_v1.0.1.rom.sha256
[protectli_vp2420_v1.0.1.rom_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.1/protectli_vp2420_v1.0.1.rom.sha256.sig

## v1.0.0 - 2022-12-22

### Added

- Support for VP2420 platform
- [Vboot Verified Boot](https://docs.dasharo.com/common-coreboot-docs/vboot_signing/)
- [TPM Measured Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/)
- [Vboot recovery notification in UEFI Payload](https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/)
- [UEFI Shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
- [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [BIOS flash protection for Vboot recovery region](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20J-bios-lock-support/)
- UEFI boot support
- Intel i225 controller network boot support
- Customized boot menu keys
- Customized setup menu keys
- Configurable boot order
- Configurable boot options

### Binaries

[protectli_VP2420_v1.0.0.rom][v1.0.0_rom]{.md-button}
[sha256][v1.0.0_hash]{.md-button}
[sha256.sig][v1.0.0_sig]{.md-button}

How to verify signatures:

```bash
wget https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom
wget https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256
wget https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256.sig
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/3mdeb-dasharo-master-key.asc
gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/customer-keys/protectli/release-keys/protectli-dasharo-firewall-release-1.0-key.asc
gpg --list-sigs "3mdeb Master Key" "3mdeb Dasharo Master Key" "Protectli Dasharo Firewall Release 1.0 Signing Key"
sha256sum -c protectli_vp2420_v1.0.0.rom.sha256
gpg -v --verify protectli_vp2420_v1.0.0.rom.sha256.sig protectli_vp2420_v1.0.0.rom.sha256
```

### SBOM (Software Bill of Materials)

- [coreboot based on c492b427 revision c86c9266](https://github.com/Dasharo/coreboot/tree/c86c9266)
- [edk2 based on e461f08 revision 7948a20](https://github.com/Dasharo/edk2/tree/7948a20)
- [iPXE for EFI revision 988d2](https://github.com/ipxe/ipxe/tree/988d2)

[newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
[v1.0.0_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom
[v1.0.0_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256
[v1.0.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256.sig
