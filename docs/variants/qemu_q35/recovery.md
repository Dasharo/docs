# Recovery

The recovery process of Dasharo (coreboot+UEFI) firmware on QEMU Q35 does not
need any special actions. QEMU Q35 is an emulated platform, not real hardware,
so it doesn't brick itself.

If something goes wrong simply rerun the QEMU command as described in
[Dasharo initial deployment](initial-deployment.md).

To clear all UEFI variables you can run the following:

```bash
dd if=/dev/zero of=build/coreboot.rom bs=256 count=1 conv=notrunc
```
