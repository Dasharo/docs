# TPM measured boot

Since the Dasharo release v0.3.0 for KGPE-D16 TPM and measured boot are enabled
by default. The firmware comes with 2 variants for all 3 flash size targets:

- vboot and TPM 1.2 measured boot for 2MB, 8MB and 16MB flash
- vboot and TPM 2.0 measured boot for 2MB, 8MB and 16MB flash

## TPM support

3mdeb office validates the following setups:

1. KGPE-D16 8MB flash with [ASUS TPM-L R2.0](https://www.asus.com/Motherboards-Components/Motherboards/Accessories/TPM-L-R2-0/)
   (Infineon SLB9665 TT2.0).
2. KGPE-D16 16MB flash with ASUS TPM 1.2 Rev 1.02h (Infineon SLB9635 TT1.2).

Both chips are supported by coreboot. For the time being the platforms will be
tested with ASUS modules until OSHW [lpnTPM](https://nlnet.nl/project/lpnTPM/)
with open-source TPM firmware is ready.

## Measured boot behaviour

It is also possible to have builds without vboot:

- TPM 1.2 measured boot only (no vboot) for 2MB, 8MB and 16MB flash
- TPM 2.0 measured boot only (no vboot) for 2MB, 8MB and 16MB flash

These targets are for cases where only the bootblock is intended to be locked
to form Static Root of Trust for Measurement. For details how to lock flash
depending on the firmware variant (with or without vboot) refer to
[SPI hardware write protection](spi-wp.md).

Note the targets without vboot do not need to have any division into read-only
and read-write partitions. Everything can be contained in a single COREBOOT
flashmap region like in a standard coreboot build to have the largest free
space for big payloads like heads.

The variants without vboot have enabled measured boot with an additional option
to initialize the TPM in bootblock in order to send the measurements directly
to TPM in bootblock and other early stages. Otherwise the TPM measurements are
cached in memory and sent to TPM PCRs late in ramstage during TPM setup. The
downside of this approach is that the memory could be corrupted in the meantime
and the measurements could be faked before they are migrated to the TPM.

If you check the boot logs either on serial port on via cbmem utility you
should see:

```bash
coreboot-asus_kgpe-d16_v0.2.0-15-g521dec6dff Wed Dec 15 11:43:34 UTC 2021 bootblock starting (log level: 8)...
CPU INIT detected 00000000
Found TPM SLB9665 TT 2.0 by Infineon
tlcl_send_startup: Startup return code is 0
TPM: Write digests cached in TCPA log to PCR
TPM: Write digest for FMAP: FMAP into PCR 2
tlcl_extend: response is 0
TPM: Write digest for FMAP: COREBOOT CBFS: bootblock into PCR 2
tlcl_extend: response is 0
TPM: Write digest for FMAP: COREBOOT CBFS: cmos.default into PCR 3
tlcl_extend: response is 0
TPM: setup succeeded
CBFS: Found 'fallback/romstage' @0x80 size 0x2d688 in mcache @0x0004962c
FMAP: area COREBOOT found @ 200 (8388096 bytes)
TPM: Extending digest for FMAP: COREBOOT CBFS: fallback/romstage into PCR 2
tlcl_extend: response is 0
TPM: Digest of FMAP: COREBOOT CBFS: fallback/romstage to PCR 2 measured
BS: bootblock times (exec / console): total (unknown) / 62 ms
```

When vboot is enabled and the verstage is being located, the bootblock measures
itself and the verstage, but the measurements are sent to the TPM PCRs not in
bootblock, but in verstage:

```bash
coreboot-asus_kgpe-d16_v0.2.0-15-g521dec6dff Wed Dec 15 11:43:34 UTC 2021 bootblock starting (log level: 8)...
CPU INIT detected 00000000
VBOOT: Loading verstage.
CBFS: Found 'fallback/verstage' @0x8c300 size 0xd848 in mcache @0x0004c8fc
FMAP: area COREBOOT found @ 609000 (2060288 bytes)
TPM: Digest of FMAP: COREBOOT CBFS: fallback/verstage to PCR 2 logged

coreboot-asus_kgpe-d16_v0.2.0-15-g521dec6dff Wed Dec 15 11:43:34 UTC 2021 verstage starting (log level: 8)...
VBNV: CMOS invalid, restoring from flash
FMAP: area RW_NVRAM found @ 80000 (16384 bytes)
spi_init: SPI base fec10000
Manufacturer: ef
SF: Detected ef 4017 with sector size 0x1000, total 0x800000
VBNV: Restore from flash failed
Found TPM SLB9665 TT 2.0 by Infineon
tlcl_send_startup: Startup return code is 0
TPM: Write digests cached in TCPA log to PCR
TPM: Write digest for FMAP: FMAP into PCR 2
tlcl_extend: response is 0
TPM: Write digest for FMAP: COREBOOT CBFS: bootblock into PCR 2
tlcl_extend: response is 0
TPM: Write digest for FMAP: COREBOOT CBFS: cmos.default into PCR 3
tlcl_extend: response is 0
TPM: Write digest for FMAP: COREBOOT CBFS: fallback/verstage into PCR 2
tlcl_extend: response is 0
TPM: Write digest for FMAP: COREBOOT CBFS: cmos_layout.bin into PCR 2
tlcl_extend: response is 0
TPM: setup succeeded
```
