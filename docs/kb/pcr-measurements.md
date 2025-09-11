# PCR measurements performed by Dasharo firmware

## Introduction

As part of measured boot process firmware hashes (measures) various
pieces of code or data and updates PCRs of a TPM device.  This allows a user
(typically, automatically) to attest integrity of the system by verifying PCR
values after a boot or tying decryption of data to expected values.

Usually the firmware is not the only entity which updates PCRs and even if it
is, the number of updates can be large, so it's important to know which values
do get measured to which PCRs and under what conditions (e.g., some
measurements are done in response to user actions).

TPM event log maintained throughout the boot process is meant to track this kind
of information, but due to limitations of its format the log is rarely enough
to understand all of the measurements.  This document is meant to describe when
Dasharo updates PCRs so users would know which PCRs to use for sealing secrets
and when to expect their values to be changed.

Firmware components are described separately because not all components might
be present in a given firmware variant.

## The truth about PCR usage

[TPM 1.2 Specification][TPM12] (section 3.3.3) and
[TPM 2.0 Specification][TPM20] (section 3.3.4) provide information on which
PCRs are expected to be used for what purposes.  The problem is that
instructions seemingly contradict themselves and even if when they don't,
discerning which PCR is to be used for a particular code or data is far from
an easy task.  This results in a disconnect between what's prescribed by those
specification and how things are in practice.

EDK is better at adhering to TCG specifications probably because of interactions
between developers on both sides.  The way coreboot updates PCRs originally came
from Chromebooks and its authors had a different interpretation of PCR
allocations ([see][coreboot-pcrs]).  When EDK is used as a second-stage
firmware after coreboot, you get a mix of both.

[TPM12]: https://trustedcomputinggroup.org/wp-content/uploads/TCG_PCClientImplementation_1-21_1_00.pdf
[TPM20]: https://trustedcomputinggroup.org/wp-content/uploads/TCG_PCClient_PFP_r1p05_v23_pub.pdf
[coreboot-pcrs]: https://doc.coreboot.org/security/vboot/measured_boot.html#platform-configuration-registers

## coreboot measurements

### PCR banks

At the time of writing (September 2025) coreboot supports extending only a
single bank of a PCR despite ability of TPM 2.0 to handle multiple banks.  A PCR
bank, which corresponds to a specific hash function, is fixed at build time:

| TPM version | PCR Bank
| ----------- | --------
| 1.2         | SHA-1 only
| 2.0         | SHA-256 only (default used by Dasharo, but there are other options)

This has an implication for TPM 2.0 case when multiple PCR banks are active and
used by EDK.  This is handled by using dummy hash values (`0100...`) for missing
digests (SHA-1) which do not correspond to actual PCR updates.  Doing this
breaks replaying of TPM log unless fake digests are skipped, but it allows to
comply with TPM event log format.

### PCR measurements

| PCR   | Event type | Condition  | Description
| ---   | ---------- | ---------  | -----------
| PCR-2 | EV_ACTION  | Always     | Stages, constant data, blobs, payload
| PCR-3 | EV_ACTION  | If present | Runtime data

The measurements are done each time a particular part of firmware is read from
ROM, which results in the same data being measured multiple times in some cases.

## EDK measurements

### PCR banks

EDK allows a user to select which TPM banks are active and aligns its
measurements with that.  Practically this means usage of all available PCR banks
by default.

Note that coreboot handles PCR banks differently, see above for more details and
implications.

### PCR measurements

The order of the rows reflects typical order of measurements in the event log
but it's not fixed and depends on TPM version (different drivers do things
differently), user actions (picked a boot option from a menu or not), failure to
boot and other things.

ATM (at the moment) in the table means as of June 2024.  Empty cells match
contents of the last non-empty cell, so that it's easier to read sequences of
measurements.

| PCR      | Event type                       | Condition           | Description
| ---      | ----------                       | ---------           | -----------
| PCR-0    | EV_S_CRTM_VERSION                | Always              | Firmware version (empty string ATM)
| PCR-0    | EV_EFI_PLATFORM_FIRMWARE_BLOB    | Always              | UEFI firmware volume base+size (TPM2 could use v2 of the event, but doesn't ATM), can appear more than once
| PCR-7    | EV_EFI_VARIABLE_DRIVER_CONFIG    | Always for TPM 2.0  | 61dfe48b-ca93-d211-aa0d-00e098032b8c:SecureBoot variable
|          |                                  | These variables set | 61dfe48b-ca93-d211-aa0d-00e098032b8c:PK variable
|          |                                  |                     | 61dfe48b-ca93-d211-aa0d-00e098032b8c:KEK variable
|          |                                  |                     | cbb219d7-3a3d-9645-a3bc-dad00e67656f:db variable
|          |                                  |                     | cbb219d7-3a3d-9645-a3bc-dad00e67656f:dbx variable
| PCR-0    | EV_POST_CODE                     | TPM present         | ACPI tables which are about to be published but not yet finalized for publishing
| PCR-4    | EV_EFI_BOOT_SERVICES_APPLICATION | Boot menu/Setup     | Hash of an EFI application implementing UI
| PCR-1    | 0x00DA0000                       | First boot try      | Dasharo-specific EFI variables (NUL-terminated ASCII name followed by variable's value)
| PCR-1    | EV_EFI_VARIABLE_BOOT             | First boot try      | 61dfe48b-ca93-d211-aa0d-00e098032b8c:BootOrder variable
|          |                                  |                     | 61dfe48b-ca93-d211-aa0d-00e098032b8c:Boot0000... variables
| PCR-4    | EV_EFI_ACTION                    | Any boot try        | "Calling EFI Application from Boot Option"
| PCR-0..7 | EV_SEPARATOR                     | Always              | Separator, the one for PCR-7 can appear earlier
| PCR-1    | EV_EFI_HANDOFF_TABLES            | First boot try      | SMBIOS base+size (could use v2 of the event, but doesn't ATM)
| PCR-4    | EV_EFI_BOOT_SERVICES_APPLICATION | Any boot try        | Hash of an EFI application (bootloader, UEFI shell, etc.)
| PCR-7    | EV_EFI_VARIABLE_AUTHORITY        | Unknown             | Measurements done by shim as an extension of SecureBoot, listed here to show where they appear
| PCR-8..9 | EV_IPL                           | Unknown             | Measurements done by a bootloader (GRUB, shim, etc.), listed here to show where they appear
| PCR-5    | EV_EFI_ACTION                    | OS is booting       | "Exit Boot Services Invocation"
|          |                                  |                     | "Exit Boot Services Returned with Success"

## Other sources of measurements

Applications started by firmware to boot the system continue to measure code
and data they use and also show up in the event log.  You can find more details
in the documentation of respective tools (e.g., for [GRUB2][grub] or
[shim][shim]).

[grub]: https://www.gnu.org/software/grub/manual/grub/html_node/Measured-Boot.html
[shim]: https://github.com/rhboot/shim/blob/master/README.tpm

## Caveats

### First Boot

First boot is somewhat special due to firmware initializing its state.  This
includes SecureBoot-related variables which generate
`EV_EFI_VARIABLE_DRIVER_CONFIG` events.  SecureBoot is considered to be on at
the start, but then it's switched to its default off state.  As a result, event
log on first and subsequent boots will differ even if no configuration is
touched by the user.

### Accuracy

Exact list of measurements depends on the combination of firmware components,
their versions, installed hardware, TPM version, runtime settings and at least
user actions.  This is why this document can only enumerate things which
typically appear in event logs and can't go much further.

#### Repeated entries

Sometimes the same thing is measured multiple times (usually to the same PCR,
digest is the same if that thing is unchanged) or many similar things get
measured in sequence.  Keep this in mind when looking for something in the event
log as it can sometimes appear more than once, including several times in a row.

#### Log entries changing values

Bootloaders or components of operating systems might update SecureBoot
configuration automatically thus changing PCR values.  Similarly, any kind of
software update or even update of configuration can potentially change
behavior and cause an unexpected PCR value.  In such cases PCR values tend to
stabilize after a reboot.

#### Conditional measurements

Some things are measured dynamically when they get used which in turn is
controlled by some setting.  This can result in a single configuration change
affecting event log in multiple places, for example disabling a device can:

- change value of a corresponding option which is measured
- remove an entry with a measurement of device's OptionROM
- remove some of the `BootXXX` variables and update `BootOrder` to reflect that

Another example of a conditional measurement is entering firmware setup or
using boot menu.  Doing that causes a measurement of EFI application
that implements corresponding user interface.
