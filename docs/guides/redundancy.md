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
correspondingly to load consecutive stages from.

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

## Further reading

For a more detailed documentation of the implementation, please read the
[upstream coreboot documentation](WIP.com).
