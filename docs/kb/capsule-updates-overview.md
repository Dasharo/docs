# UEFI Capsule Updates

## Introduction

This document provides information on a firmware update mechanism called UEFI
Update Capsules.

## What are UEFI Update Capsules

UEFI Update Capsules, or simply update capsules or even capsule updates, are a
way of delivering firmware updates for UEFI firmware.  Simultaneously, it's a
format in which corresponding firmware images are being delivered.

As a format, update capsules are essentially a container consisting of a raw
update image(s) along with metadata and optionally drivers necessary to carry
out an update.

## Why use Update Capsules

The distinguishing feature of update capsules is that this method of updates
interacts with the currently running firmware.  This naturally gives it features
which are harder to achieve with other update methods.

### Extra Validation

Thanks to the metadata embedded into update capsules (e.g., firmware kind and
its version), an attempted update to an unsupported firmware image will result
in a failure with no consequences for the device.

Other update methods put responsibility for picking the right firmware release
on the user, resulting in higher probability of making a mistake.

### Embedded Flashing Code

Firmware reads and writes system flash chip as part of its normal operation.
Capsule update mechanism reuses very same code to switch to a different firmware
image.

This way the means for firmware update are always there and require only minimal
extra input to submit the capsule for an update.

### Multiple Firmware Images

A single capsule can contain multiple firmware images each targeting a separate
component (e.g., system firmware and embedded controller (EC) of a laptop)
which can be processed in one go.

This is different from performing such updates via other methods that typically
require use of several firmware update tools in the right order.

### Managing Dependencies

The metadata can even take into account compatibility requirements between
firmware of different components.  For example, if you're trying to update a
system firmware which requires EC version 1.2 but currently running EC firmware
is of version 1.1, the update will no happen, likely avoiding bricking the
device.

### Convenience

When an operating system supports EFI Runtime Services, it can supply a capsule
update to a running firmware which will to be applied after a reboot.

### Migration

Because current firmware is aware that it's being updated, it has a chance to
migrate current settings after a successful update.

### Security

Capsules are cryptographically signed to disallow updates from unauthorized
third-parties.  Applying a capsule also requires the system firmware to be
exposed without any extra protections only for the duration of an update, which
is much shorter compared to other update methods when a whole OS might need to
be boot.

## Further information

A developer-oriented document about how to deal with update capsules in EDK2 is
[here](../kb/edk2-capsule-updates.md).
