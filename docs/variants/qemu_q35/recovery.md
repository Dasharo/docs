# Recovery

The recovery process of Dasharo (UEFI) firmware on QEMU Q35 does not need any
special actions. QEMU Q35 is an emulated platform, not real hardware, so it
doesn't brick itself.

If something goes wrong simply rerun the QEMU command:

```bash
qemu-system-x86_64 -machine q35,smm=on \
	-global driver=cfi.pflash01,property=secure,value=on \
	-drive if=pflash,format=raw,unit=0,file=Build/OvmfX64/RELEASE_GCC5/FV/OVMF_CODE.fd,readonly=on \
	-drive if=pflash,format=raw,unit=1,file=Build/OvmfX64/RELEASE_GCC5/FV/OVMF_VARS.fd \
	-debugcon file:debug.log -global isa-debugcon.iobase=0x402 \
	-global ICH9-LPC.disable_s3=1
```

Or build a debug image, gather the logs in `debug.log` file

```bash
qemu-system-x86_64 -machine q35,smm=on \
	-global driver=cfi.pflash01,property=secure,value=on \
	-drive if=pflash,format=raw,unit=0,file=Build/OvmfX64/DEBUG_GCC5/FV/OVMF_CODE.fd,readonly=on \
	-drive if=pflash,format=raw,unit=1,file=Build/OvmfX64/DEBUG_GCC5/FV/OVMF_VARS.fd \
	-debugcon file:debug.log -global isa-debugcon.iobase=0x402 \
	-global ICH9-LPC.disable_s3=1
```

and report an issue with attached log.
