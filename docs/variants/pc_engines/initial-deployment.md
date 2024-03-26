# Initial deployment

Initial flashing of Dasharo firmware can be done from Linux using flashrom
with the internal programmer.

## Deploy using Dasharo Tools Suite

For simplicity we recommend using [Dasharo Tools
Suite](../../dasharo-tools-suite/documentation.md#dasharo-zero-touch-initial-deployment)
to omit all compilation steps and deploy the Dasharo firmware seamlessly.

## Build flashrom

Please follow generic guide for [flashrom
building](https://www.flashrom.org/dev_guide/building_from_source.html).

Or install it from the OS' package manager (minim supported version is v1.0).

## Reading flash contents

Always prepare a backup of the current firmware image. If you are using DTS,
the backup will be made automatically with [HCL
report](../../dasharo-tools-suite/documentation.md#hcl-report). When deploying
manually, to read from the flash and save it to a file (`dump.rom`), execute
the following command:

```bash
flashrom -p internal -r dump.rom
```

## Flashing Dasharo

To flash Dasharo on the platform, execute the following command - replace
`<variant>` with the APU variant (2, 3, 4 or 6) and `<version>` with the
Dasharo image version, e.g. `v0.9.0` or `v24.02.01.01` or `v4.0.34`.

```bash
flashrom -p internal -w pcengines_apu<variant>_<version>.rom
```

After the operation is successful, reboot the platform.
