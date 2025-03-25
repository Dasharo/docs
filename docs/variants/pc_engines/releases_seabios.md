# Release Notes

Following Release Notes describe status of Dasharo (coreboot+SeaBIOS) variant
of open-source firmware development for PC Engines apu2/3/4/6 platform.

For details about our release process please read
[Dasharo Standard Release Process](../../dev-proc/standard-release-process.md).

<center>
[Subscribe to Dasharo for PC Engines Release Notification Newsletter]
[newsletter]{.md-button .md-button--primary .center}
</center>

</center>

## v24.05.00.01 - 2024-06-28

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit?usp=sharing).

### Added

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

### Changed

- [Code base was moved to Dasharo Patchqueue Initiative](https://github.com/Dasharo/dasharo-pq?tab=readme-ov-file#background)
- [Sign of Life date changed to 19700101 due to making Dasharo Patchqueue Initiative based build reproducible](https://github.com/Dasharo/dasharo-issues/issues/889)
- toolchain updates GCC 13.2.0, CMake 3.27.7
- ACPI 6.4 specification compliance
- sortbootorder update to v24.05.00.01

### Removed

- [apu1, apu5 and apu7 support removed](https://github.com/Dasharo/dasharo-issues/issues/909)

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

This is a Dasharo Pro/Enterprise Package (formerly Dasharo Pro Package)
Release. To obtain access to the pre-built binaries you will have to [get the
Dasharo Pro/Enterprise Package (formerly Dasharo Pro Package)](../../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Pro/Enterprise Package (formerly Dasharo Pro Package
) newsletter.

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

[newsletter]: https://3mdeb.com/subscribe/pcengines_seabios.html
[pcengines_apu2_seabios_v24.05.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu2_seabios_v24.05.00.01.rom.sha256
[pcengines_apu2_seabios_v24.05.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu2_seabios_v24.05.00.01.rom.sha256.sig
[pcengines_apu3_seabios_v24.05.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu3_seabios_v24.05.00.01.rom.sha256
[pcengines_apu3_seabios_v24.05.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu3_seabios_v24.05.00.01.rom.sha256.sig
[pcengines_apu4_seabios_v24.05.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu4_seabios_v24.05.00.01.rom.sha256
[pcengines_apu4_seabios_v24.05.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu4_seabios_v24.05.00.01.rom.sha256.sig
[pcengines_apu6_seabios_v24.05.00.01.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu6_seabios_v24.05.00.01.rom.sha256
[pcengines_apu6_seabios_v24.05.00.01.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/pcengines_apu2/v24.05.00.01/pcengines_apu6_seabios_v24.05.00.01.rom.sha256.sig
