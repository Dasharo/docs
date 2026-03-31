# Introduction to Intel Top Swap A/B Redundancy for coreboot

The problem addressed by this functionality is that when a
platform's firmware crashes during the boot process, the only mode
of recovery is usually taking apart the platform, attaching an
SPI clip and flashing recovery firmware as per our recovery guides
([example](https://docs.dasharo.com/unified/protectli/recovery/)).

With the Top Swap A/B redundancy, there are two firmware slots - **A** and
**B**, of which **A** is a read-only golden copy, and **B** is the update
partition. A firmware update is going to target the **B** slot, and boot from
it. Should the new firmware fail, the platform can be brought back to life by
performing a **CMOS reset**, which will cause the platform to boot from the safe
slot **A** again.

This should significantly reduce the friction of testing the firmware,
especially during development and at early beta stages.

## How It Works

* **Top Swap Control**: The Intel Top Swap feature allows the PCH to take two
physically topmost chunks of the BIOS flash chip, and decide in which order
to map them - effectively allowing to swap the two chunks.

* **A/B Slot Setup**: The top of the firmware is divided into two slots:
`BOOTBLOCK` and `TOPSWAP`, which contain bootblocks "chosen" by the Top
Swap mechanism. They in turn choose `COREBOOT` and `COREBOOT_TS` regions
respectively to load consecutive stages from.

* **Runtime CMOS Control**: The CMOS option `attempt_slot_b` controls the Top
Swap state, also enabling users to manually select the active slot by setting
this value via nvramtool. If the option is set, the platform will attempt
booting slot **B**.

## Updating Firmware with Flashrom

If you wish to update the firmware using Flashrom, you need to follow
these additional steps:

```bash
sudo flashrom -p internal -w coreboot.rom --fmap -i TOPSWAP -i COREBOOT_TS --noverify-all
sudo nvramtool -w attempt_slot_b=Enable
```

This command sequence writes the new firmware image into the appropriate regions
(`TOPSWAP` and `COREBOOT_TS`) and enables the Top Swap feature by setting the
`attempt_slot_b` CMOS option to "Enable". This ensures that after the next
reboot, the system will boot from the newly updated slot.

## Security: Chain of Trust with TrustRoot and CBFS Verification

### Slot Integrity via CBFS Verification

Each redundancy slot is protected by **CBFS Verification**: the bootblock
contains cryptographic hashes of all other CBFS files, and each file's hash
is checked before it is loaded. This ensures that any corruption or tampering
within a slot is detected before the affected code runs, regardless of which
slot is active.

### Dasharo TrustRoot Integration

When TrustRoot is enabled, it extends the root of trust into hardware.
On every boot, the Boot Guard ACM — executed directly by the CPU before any
firmware code runs — cryptographically verifies the **bootblock** of the active
slot. Because the bootblock in turn holds the CBFS hashes, a single hardware
verification anchors the integrity of the entire slot.

The full chain of trust proceeds as follows:

1. **Boot Guard ACM** (hardware) verifies the active slot's bootblock.
2. **Bootblock** uses CBFS Verification to check and load `romstage`.
3. Each subsequent stage verifies the next until the **UEFI payload** is
   reached.
4. **UEFI Secure Boot** takes over to verify OS boot loaders and drivers.

### Interaction with Top Swap

The Top Swap mechanism selects which bootblock the CPU presents to Boot Guard
at reset. Boot Guard verifies whichever bootblock is currently mapped (slot A
or slot B), so both slots must be signed with the same key for the platform to
boot successfully from either. A CMOS reset falls back to slot A, which is the
read-only golden copy — ensuring there is always a known-good, Boot Guard
verified image available for recovery.

!!! note

    The CMOS-backed `attempt_slot_b` bit selects the active slot; physically
    removing or shorting the CMOS battery resets this bit and unconditionally
    restores slot A as the boot target.

## Further reading

For a more detailed documentation of the implementation, please read the
[upstream coreboot documentation](https://doc.coreboot.org/soc/intel/redundancy.html)
(can also be viewed
[here](https://github.com/coreboot/coreboot/blob/main/Documentation/soc/intel/redundancy.md)).
