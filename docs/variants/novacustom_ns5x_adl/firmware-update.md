# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update. The update process may be different, depending on which
firmware version is currently installed on your device. The currently installed
firmware version can be checked with the following command in a Linux
environment:

```shell
sudo dmidecode -t bios | grep Version
```

Alternatively, it can be checked in the `BIOS Setup Menu`.

## Version v1.0.0

You should update to the [v1.0.0 version](../releases/TBD) first by flashing
externally to overwrite ME region and install Dasharo, then update EC by
following [this procedure](initial-deployment.md).

ME region is provisioned for Boot Guard which must be disabled first. Also
software flashing is not possible due to enabled BIOS Guard.

## Versions newer than v1.0.0

### Update using flashrom

* Boot into
  [Dasharo Tools Suite](../../../common-coreboot-docs/dasharo_tools_suite/#running)

* Flash the `RW_SECTION_A` partition using the following command:

  ```bash
  flashrom -p internal -w [path] --fmap -i RW_SECTION_A
  ```

> This command also preserves UEFI settings and the boot order.
