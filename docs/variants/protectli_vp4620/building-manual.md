# Protectli Dasharo on VP4620 - building manual

To build Dasharo firmware image, follow the steps below:

1. Clone the coreboot repository:

    ```bash
    $ git clone https://github.com/Dasharo/coreboot.git -b protectli_vault_cml/release
    ```

2. Start build process (note it requires certain blobs to proceed):

    ```bash
    $ cd coreboot
    # you will need to put the ZIP with blobs at this point
    $ ./build.sh vp4620
    ```
