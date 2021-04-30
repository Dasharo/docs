# Dasharo Workstation Releases

TBD: Following notes to not meet quality criteria of Dasharo release notes,
that's why we have to rewrite it

## Release notes

### v0.2

The second release of Dasharo Workstation.

Software BOM:

- coreboot 4.12-1428-g20cf396c96 (with additional commits for custom platform
  config and CI YAML)
- EDK2

Features:

- Dell OptiPlex 7010 and 9010 platforms supported
- Dasharo bootsplash
- UEFI boot support
- USB, SATA, and NVMe boot supported
- Measured boot with TPM 1.2
- ME neutralized with me_cleaner
- Environmental Controller fan control
- Environmental Controller firmware update support (the DELL EC firmware is
  included in the image, the firmware update process is open-source, but the EC
  firmware code is in binary form only and we have no control over what is
  executed on EC)
- Integrated graphics initialization with open-source libgfxinit library for
  both VGA and 2 DP ports
- Discrete graphics support
- Onboard serial port supported
- SATA password
- TCG OPAL password
- configurable boot order
- configurable boot options
- UEFI iPXE for EFI network boot support
- UEFI Secure Boot
- Internal UEFI Shell
- One-time boot feature

### v0.1

The first release of Dasharo Workstation.

Software BOM:

- coreboot 4.12-1428-g20cf396c96 (with additional commits for custom platform
  config and CI YAML)
- SeaBIOS 1.13.0

Features:

- Dell OptiPlex 7010 and 9010 platforms supported
- Dasharo bootsplash
- Legacy boot support
- USB, SATA, and NVMe boot supported
- Measured boot with TPM 1.2
- ME neutralized with me_cleaner
- Environmental Controller fan control
- Environmental Controller firmware update support (the DELL EC firmware is
  included in the image, the firmware update process is open-source, but the EC
  firmware code is in binary form only and we have no control over what is
  executed on EC)
- Integrated graphics initialization with open-source libgfxinit library for
  both VGA and 2 DP ports
- Onboard serial port supported
