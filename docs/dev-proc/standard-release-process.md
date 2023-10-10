# Standard Release Process

Following procedure is generic description of release process of firmware for
supported hardware platforms. Precise steps and any difference from standard
process are described in platform specific documentation.

Description here is, intentionally, Open Source Firmware framework agnostics
and should be maintained in that way.

## Process steps

1. Checkout new branch `dasharo/<platform>_rel_vX.Y.Z` from recent commit on
   `dasharo/release` - to understand versioning scheme please read
   [Versioning](versioning.md) section
2. Merge current `dasharo/develop` to `dasharo/<platform>_rel_vX.Y.Z`
3. Run platform regression test suite
4. Fix all required issues and repeat point 3 until fixed - this doesn't mean
   all tests pass, this mean that approved set passed
5. If results are accepted merge it to `dasharo/release` branch
6. Add tag, which should trigger CI and publish binaries. Tag should be
   annotated and signed. For example:

    ```bash
    git tag -a -s -m "<platform>_vX.Y.Z" <platform>_vX.Y.Z
    ```

7. Merge release branch to develop
