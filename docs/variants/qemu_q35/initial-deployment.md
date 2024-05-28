# Initial Deployment

Initial deployment of Dasharo (coreboot+UEFI) firmware on QEMU Q35 does not need
any special actions. QEMU Q35 is an emulated platform, not real hardware.

Running the Dasharo (coreboot+UEFI) is as simple as invoking a QEMU command:

```bash
qemu-system-x86_64 -machine q35,smm=on \
	-drive if=pflash,format=raw,file=build/coreboot.rom
```

This is the minimal set of parameters that are always required, but you may add
more to e.g. connect additional devices or redirect serial output to a file.
Refer to [QEMU documentation](https://qemu-project.gitlab.io/qemu/system/invocation.html)
for list of possible options.

If you use system without graphical output you may face following issues:

```text
gtk initialization failed
```

In such case add `-nographic` at the end of your command.
