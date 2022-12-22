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

## v1.0.0 - 2022-12-22

### Added

- description: Support for VP2420 platform
- description: Vboot Verified Boot
  url: https://docs.dasharo.com/common-coreboot-docs/vboot_signing/
- description: TPM Measured Boot
  url: https://docs.dasharo.com/unified-test-documentation/dasharo-security/203-measured-boot/
- description: Vboot recovery notification in UEFI Payload
  url: https://docs.dasharo.com/unified-test-documentation/dasharo-security/201-verified-boot/
- description: UEFI Shell
  url: https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/
- description: UEFI Secure Boot
  url: https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/
- description: BIOS flash protection for Vboot recovery region
  url: https://docs.dasharo.com/unified-test-documentation/dasharo-security/20J-bios-lock-support/
- description: UEFI boot support
- description: Intel i225 controller network boot support
- description: Customized boot menu keys
- description: Customized setup menu keys
- description: Configurable boot order
- description: Configurable boot options

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
sha256sum -c protectli_vault_ehl_v1.0.0.rom.sha256
gpg -v --verify protectli_vault_ehl_v1.0.0.rom.sha256.sig protectli_vault_ehl_v1.0.0.rom.sha256
```

### SBOM (Software Bill of Materials)

- [coreboot based on c492b427 revision c86c9266](https://github.com/Dasharo/coreboot/tree/c86c9266)
- [edk2 based on e461f08 revision 7948a20](https://github.com/Dasharo/edk2/tree/7948a20)
- [iPXE for EFI revision 988d2](https://github.com/ipxe/ipxe/tree/988d2)

[newsletter]: https://newsletter.3mdeb.com/subscription/n2EpSxtqL
[v1.0.0_rom]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom
[v1.0.0_hash]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256
[v1.0.0_sig]: https://3mdeb.com/open-source-firmware/Dasharo/protectli_vault_ehl/v1.0.0/protectli_vp2420_v1.0.0.rom.sha256.sig
