# Standard Release Process

Following procedure is generic description of release process of firmware for
supported hardware platforms. Precise steps and any difference from standard
process are described in platform specific documentation.

Description here is, intentionally, open-source firmware framework agnostic and
should be maintained in that way.

## Process steps

1. Checkout new branch `<platform>_rel_vX.Y.Z-rcN` from recent commit on
   `dasharo` - to understand versioning scheme please read
   [Versioning](versioning.md) section
2. Merge current platform development/bugfix branches to
   `<platform>_rel_vX.Y.Z-rcN`.
3. Merge `<platform>_rel_vX.Y.Z-rcN` branch it to `dasharo` branch
4. Change the CONFIG_LOCALVERSION in coreboot configs appropriately and create
   a release candidate by tagging `<platform>_vX.Y.Z-rcN`
5. Run platform regression test suite.
6. If all required tests passed, go to 8.
7. Fix all required issues and repeat from point 1 until fixed.
8. Change the CONFIG_LOCALVERSION in coreboot configs appropriately and add a
   tag, which should trigger CI and publish binaries. Tag should be annotated,
   signed and placed on the `dasharo` branch. For example:

    ```bash
    git tag -a -s -m "<platform>_vX.Y.Z" <platform>_vX.Y.Z
    ```
