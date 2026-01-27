# Glossary

After years of providing services and products on firmware
market we recognize that it is poisoned by incorrect and
confusing terminology. In following glossary we would like to
explain most used terms from Dasharo Documentation. We try to
refer to standards, literature and community best practices to
keep content added by us minimalistic.

## Embedded Firmware

We use definition explained in first chapter of
["Embedded Firmware Solutions"](https://link.springer.com/book/10.1007/978-1-4842-0070-4)
book by Jiming Sun, Marc Jones, Stefan Reinauer and Vincent Zimmer.

Firmware is "layer of software between the hardware and the
operating system (OS), with the main purpose to initialize and
abstract enough hardware so that the operating systems and
their drivers can further configure the hardware to its full
functionality."

Rising complexity of hardware initialization and need for its
manageability created need for BMC (Board Management
Controllers), EC (Environmental Controllers) and even more
specialized one like USB Power Delivery firmware. What may
make that firmware also covered by above definition.

## Dasharo Hardware Compatibility List Report

Dasharo HCL Report dumps most important information about platform and backup
SPI NOR flash. Gathered information can be used for future analysis, debugging
and recovery. Optionally scripts upload dump to Dasharo HCL Backup Server, so
Dasharo Team can improve open source firmware product line and support
customers in case of issues.

As temporary solution we use 3mdeb NextCloud as Dasharo HCL Backup Server.

Dasharo HCL Reports are also used during open source firmware port feasibilty
analysis, so if you are interested in Dasharo support for your hardware, feel
free to [reach us](mailto:leads@3mdeb.com).

Please note Dasharo HCL Report may contain sensitive information like serial
numbers. Please do not make this information public. Dasharo Team respect your
privacy.

## Dasharo Blobs Transmission

Unfortunately, some hardware platforms cannot be fully functional without
binary blobs in the firmware. Some binary blobs have no EULA or any other
license discussing redistributability. To avoid issues, Dasharo Blobs
Transmission scripts extract blobs from SPI NOR flash backup and patch Dasharo
open-source firmware distribution before initial deployment.

## Dasharo Openness Score

[Dasharo Openness Score](https://github.com/Dasharo/Openness-Score) is an
utility, which parses the firmware images to calculate the amount of bytes
produced from open-source code. It is able to parse both Dasharo/coreboot
images and proprietary UEFI images. That said, it can be used to compare how
open the Dasharo images are versus the proprietary versions.

Dasharo Openness Score may also refer to the report produced by the Dasharo
Openness Score utility. Such reports are being published in the [platform
directories](https://docs.dasharo.com/variants/overview/) in this repository.
If you are interested in Dasharo Openness Score for you boards, please [reach
us](mailto:leads@3mdeb.com). Example Dasharo Openness Score report can be
found [here](https://github.com/Dasharo/Openness-Score/blob/cab83fe1104c345fd22fb9541c738aca66b392da/examples/msi_ms7d25_v1.1.1_ddr4.rom_openness_score.md)

You can also find an Openness Score comparison table in the
[Supported hardware overview](./variants/overview.md#openness-comparison)
section. It shows the comparison of binary openness between Dasharo and
proprietary firmware.

## Dasharo TrustRoot

Dasharo TrustRoot hardens firmware security by leveraging a hardware-based
Root of Trust.  It ensures platform integrity by verifying firmware authenticity
during the earliest boot stages and refusing to proceed with the boot if
firmware doesn't pass the checks.  **This renders platforms unbootable in an
event of firmware tampering for the sake of not running an unknown and
potentially compromised firmware.**

!!! note

    Making use of Dasharo TrustRoot has serious usability implications which
    should be considered carefully.  For this reason firmware does not enable
    this security mechanism by default requiring a user to explicitly opt-in
    during a firmware update.

    This kind of security hardening cryptographically validates firmware
    against a specific private key managed by the device vendor.  Because the
    private key is not available to device owners, neither adversaries nor the
    device owners themselves can change the firmware to a version that's not
    signed by that private key.

    Another side-effect is that overall firmware layout becomes fixed once and
    for all.

Once Root of Trust has been established by hardware validating the early stages
of firmware, Measured Boot mechanism can be used to build the Chain of Trust
one step at a time.  With Measured Boot the part of firmware initially
validated by hardware measures code and data that it makes use of before
processing or running it.  That extends the trust to the new code, which in turn
does the same to the code and data that it uses, and so on.  The Chain of Trust
built this way relies on a TPM device and can be validated or leveraged to
store secrets, but it's only as good as its root which, in case of Dasharo
TrustRoot, is established in hardware.  More detailed and somewhat more
technical information about Measured Boot is available
[here](https://doc.coreboot.org/security/vboot/measured_boot.html) and
[here](https://docs.dasharo.com/kb/pcr-measurements/).

Secure Boot is another complementary security mechanism that benefits from
Dasharo TrustRoot.  Once firmware as a whole is trusted, Secure Boot can be
leveraged to ensure that only trusted device drivers or operating systems are
loaded by the firmware.  Eventually the control reaches an OS that can further
alter its behaviour to minimize security risks.

!!! warning

    Again, **once enabled, the firmware signing used by Dasharo TrustRoot
    cannot be disabled!**  This is an irreversible process due to changes in
    the device's hardware.  For Intel-based hardware (the only supported as of
    September 2025), the permanent changes happen at the level of a chipset.

    To be specific, field programmable fuses (FPFs) used to store hashes of
    firmware signing keys are one-time programmable.  Initially, they don't
    hold any specific value, but once a properly configured firmware is booted,
    their value is set and cannot be modified ever again (this is called
    "fusing").

    Make sure you fully understand this information before choosing to flash a
    firmware that enforces Dasharo TrustRoot.

## Dasharo TrustRoot fusing

By default, Dasharo TrustRoot-enabled releases are published as binaries that
do not lock the platform down. This means that TrustRoot is active, and
unauthorized updates to the BIOS region will be detected, but the chipset fuses
are not burnt. Unburnt fuses allow for replacing the chipset configuration,
which would disable TrustRoot again.

To perform proper platform lockdown, burn the fuses and permanently enable
Dasharo TrustRoot with no way to disable it again, the platform must be fused.
To perform fusing, follow the [CPU Fusing Guide](guides/cpu-fusing.md).
