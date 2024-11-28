# Capsule Update releases

Dasharo releases that support Capsule Updates need to include a number of
additional options in their coreboot configuration file. The options correspond
to the required payload data described in
[Capsule Updates Details - Required Payload Data](./edk2-capsule-updates.md#capsule-information)

## Configuration

The coreboot configuration file can be found in the coreboot repository
in the `configs/` directory under the name of
`config.<coreboot_mainboard_vendor>_<coreboot_mainboard_model>`.

The options that need to be set are:

- `CONFIG_DRIVERS_EFI_MAIN_FW_GUID`
- `CONFIG_DRIVERS_EFI_MAIN_FW_VERSION`
- `CONFIG_DRIVERS_EFI_MAIN_FW_LSV`

### CONFIG_DRIVERS_EFI_MAIN_FW_GUID

The value is a unique identifier of a firmware variant. The exact value is not
important as long as it is the same in all compatible versions of a firmware
variant and different from incompatible ones. When creating a new release
compatible with the previous one, the value should not change. When creating a
new release, for example when adding support to a new platform, the value has
to be set. To get a new UUID for this config options on Linux, use the `uuidgen`
command.

Examples:

- An example UUID generated using `uuidgen` - `CONFIG_DRIVERS_EFI_MAIN_FW_GUID="27ec159a-bfeb-4ddd-a0b1-bc9c664e4216"`

### CONFIG_DRIVERS_EFI_MAIN_FW_VERSION

The value represents the version of the current firmware as a 32bit number.
This option is used to allow for reliable ordering and comparing different
versions of the firmware that might exist and could be used to perform a
Capsule Update.
The `CONFIG_LOCALVERSION` option is a string representation of the version
which does not allow reliable comparisons.
The value consists of 8 hexadecimal digits which are grouped
into four groups of two numbers. Each group represents a single component of
a Dasharo version according to the [Versioning](https://docs.dasharo.com/dev-proc/versioning/)
`CONFIG_DRIVERS_EFI_MAIN_FW_VERSION` has to be updated on new releases to always
match the `CONFIG_LOCALVERSION`.

The value looks like `0xMMmmpprr`, where:

- MM - the MAJOR version
- mm - the MINOR version
- pp - the PATCH version
- rr - optional Release Candidate number

For release versions the Release Candidate number is generally set to `80`
(128 decimal) to make sure the version number is higher than any release
candidate but still leave some headroom for increasing just in case.

Examples:

- Release Candidate v1.5.2-rc3 - `CONFIG_DRIVERS_EFI_MAIN_FW_VERSION="0x01050203"`
- Release v0.9.1 - `CONFIG_DRIVERS_EFI_MAIN_FW_VERSION="0x000901FF"`

### CONFIG_DRIVERS_EFI_MAIN_FW_LSV

The value represents the lowest firmware version, that will be accepted as
a valid one. A Capsule Update to a version lower than
`CONFIG_DRIVERS_EFI_MAIN_FW_LSV` will not be allowed. May be used to forbid
downgrading to versions with severe security vulnerabilities. The value
takes the same format as `CONFIG_DRIVERS_EFI_MAIN_FW_VERSION`

Examples:

- Forbid changing the version to anything below release v0.1.0 - `CONFIG_DRIVERS_EFI_MAIN_FW_LSV="0x000100FF"`
