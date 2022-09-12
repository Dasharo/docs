# Dumping logs

When facing an issue on a unique hardware configuration on the end user side it
may prove useful to submit system logs to Dasharo team for diagnosis and
possibly problem solution. This section describes how to dump various logs from
a running system.

## System information

One may use [Dasharo Tools Suite HCL report](/common-coreboot-docs/dasharo_tools_suite/#dasharo-hcl-report)
or [fwdump-docker image](https://github.com/3mdeb/fwdump-docker) to
gather all the hardware configuration information from a running system. The
usage of the tools should result in an archive containing various logs from the
running system. Submit them via email to [contact@dasharo.com](mailto:contact@dasharo.com)
or use [Dasharo pastebin](https://paste.dasharo.com/).

## coreboot logs

When already migrated to Dasharo, it is possible to retrieve firmware logs from
coreboot on a running system. A utility called `cbmem` can be used for that
purpose. By obtaining the logs Dasharo team will be able to locate any issues
with the firmware. This method requires Secure Boot to be disabled.

Short instruction how to compile and use `cbmem` on Ubuntu 22.04 live CD:

1. Launch Ubuntu 22.04 live CD and choose to `Try Ubuntu`.
2. Right click on the desktop and choose `Open in Terminal`.
3. Install required packages:

    ```bash
    sudo apt-get install -y build-essential libpci-dev
    ```

4. Navigate to tmpfs: `cd /tmp`.
5. Download and extract coreboot source:

    ```bash
    wget https://coreboot.org/releases/coreboot-4.17.tar.xz
    tar xvf coreboot-4.17.tar.xz
    ```

6. Compile cbmem utility:

    ```bash
    cd coreboot-4.17/util/cbmem
    make
    ```

7. Obtain the coreboot logs:

    ```bash
    sudo ./cbmem -1 > coreboot.log
    ```

8. Check if the file `coreboot.log` contains coreboot logs and send them to
   Dasharo team via email or pastebin.

TODO: [make cbmem available with DTS as well](https://github.com/Dasharo/meta-dts/issues/22)
