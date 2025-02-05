# Standard Release Process

Following procedure is generic description of release process of firmware for
supported hardware platforms. Precise steps and any difference from standard
process are described in platform specific documentation.

The development process may differ depending on used firmware framework. Select
the applicable tab for your framework below:

## Process steps

=== "Generic"

    1. Checkout new branch `<platform>_rel_vX.Y.Z` from recent commit on `dasharo`
       branch - to understand versioning scheme please read [Versioning](versioning.md)
       section
    2. Merge current platform development branches to `<platform>_rel_vX.Y.Z`
    3. (Optional) Create a release candidate by tagging `<platform>_vX.Y.Z-rcN`
    4. Run platform regression test suite
    5. Fix all required issues and repeat from point 3 until fixed - this doesn't
       mean all tests pass, this mean that approved set passed
    6. If results are accepted merge it to `dasharo` branch
    7. Add tag, which should trigger CI and publish binaries. Tag should be
       annotated and signed. For example:

        ```bash
        git tag -a -s -m "<platform>_vX.Y.Z" <platform>_vX.Y.Z
        ```

=== "Heads"

    Heads development process is a little different and works closer to
    upstream repositories:

    1. Checkout the latest Heads upstream revision
    1. Create release branch for your platform `<platform>_rel_vX.Y.Z`
    1. Inside the `site-local` directory, create file `config` with the
       following contents:

        ```bash
        BRAND_NAME=Dasharo

        ifeq "novacustom-v560tu" "$(BOARD)"

        export CONFIG_COREBOOT_LOCALVERSION="\(coreboot+heads\) v[Enter version number here]"
        export CONFIG_COREBOOT_SMBIOS_PRODUCT_NAME="[Enter SMBIOS product name here]"

        endif
        ```

    1. Download Dasharo bootsplash from [dasharo-blobs](https://github.com/Dasharo/dasharo-blobs/blob/main/dasharo/bootsplash.bmp)
    1. Convert Dasharo bootsplash from BMP to JPEG format:

        ```bash
        magick bootsplash.bmp bootsplash.jpg
        ```
    1. Copy Dasharo logo in JPEG format to `branding/Dasharo/bootsplash.jpg`
    1. Commit your changes and push to Dasharo Heads fork for review

    ### Bugfixes

    When developing patches, submit changes to upstream first:

    1. Checkout latest Heads upstream version
    1. Create branch for your bugfix
    1. Push branch to Dasharo Heads fork
    1. Submit PR to upstream Heads repository for review
    1. Once merged, rebase your release branch onto the merged upstream commit:

        ```bash
        git checkout master
        git pull
        git checkout <platform>_rel_vX.Y.Z
        git rebase master
        ```

        There should be no conflicts, because all changes are in `site-local`
        directory, which is always empty in upstream branches.

    ### Tagging the release

    Once testing is complete, remove `-rcX` suffix from the version number,
    and then tag the release:

    ```bash
    git tag <platform>_vX.Y.Z -s
    git push origin <platform>_vX.Y.Z
    ```

    You may now delete branch `<platform>_rel_vX.Y.Z` on GitHub. Because the
    release is tagged, GitHub garbage collection will not automatically delete
    the commit.
