# Protectli Dasharo on VP2410 - building manual

To build Dasharo firmware image, follow the steps below:

1. Clone the coreboot repository:

    ```bash
    $ git clone https://github.com/Dasharo/coreboot.git -b protectli_vault_glk/release
    ```

2. Check out the desired version e.g. `v1.0.10`:

    ```bash
    $ cd coreboot
    $ git checkout protectli_vault_glk_v1.0.10
    ```

3. Start build process (note it requires certain blobs to proceed):

    ```bash
    # you will need to put the ZIP with blobs and FSP at this point
    $ ./build.sh vp2410
    ```
