# Initial deployment

Initial deployment for Supermicro X11SSH is supported in DTS since version
vTBD. Please check [Dasharo zero-touch initial deployment section](../../dasharo-tools-suite/documentation.md#dasharo-zero-touch-initial-deployment).

## Booting DTS over network

For seamless and storageless deployment one can use BMC virtual floppy
functionality to mount a floppy image containing iPXE. iPXE will allow to boot
DTS over network without much effort. The image file can be downloaded from
[3mdeb FTP server](https://3mdeb.com/open-source-firmware/boot/ipxe.img). If
you wish to build the image, please follow instructions in
[Building iPXE floppy image](#building-ipxe-floppy-image) section.

To boot from the iPXE image, please do the following:

1. Download or build the iPXE image on your host machine.
2. Log in to the BMC dashboard.
3. Upload the floppy image to the BMC in the Virtual Media panel.
4. Enter iKVM control and Power on the server.
5. Enter Boot Menu with F11.
6. Select `UEFI: ATEN Virtual Floppy 3000, Partition 1`.
7. Wait for the embedded menu to show up (it may take up to 30 seconds for the
   UEFI protocols to execute during iPXE initialization - proprietary UEFI
   banzai...).
8. Choose `Dasharo Tools Suite` from the menu:

```txt
------------------------ Dasharo Network Boot Menu ------------------------
Autoboot (DHCP)
Dasharo Tools Suite
OS installation (netboot.xyz official server)
iPXE Shell
```

## Installing Dasharo with DTS

TBD

### Building iPXE floppy image

To create a floppy disk image for Supermicro BMC Virtual Media, you
will need a Linux OS with docker installed. Then follow steps below:

1. Compile iPXE (a sample revision has been taken from top of master branch on
   25.01.2023, iPXE unfortunately stopped tagging the code in December 2020):

    ```bash
    git clone https://github.com/ipxe/ipxe.git
    cd ipxe
    git checkout 4bffe0f0d9d0e1496ae5cfb7579e813277c29b0f
    wget https://raw.githubusercontent.com/Dasharo/dasharo-blobs/46cc16f6d8f0ed9d057fdd20f15bb89ce5b8d212/dasharo/dasharo.ipxe
    sed "s|//#define\s*IMAGE_SCRIPT.*|#define IMAGE_SCRIPT|" src/config/general.h > src/config/general.h.tmp
    mv src/config/general.h.tmp src/config/general.h
    sed "s|.*DOWNLOAD_PROTO_HTTPS|#define DOWNLOAD_PROTO_HTTPS|g" src/config/general.h > src/config/general.h.tmp
    mv src/config/general.h.tmp src/config/general.h
    sed "s|.*IMAGE_EFI|#define IMAGE_EFI|g" src/config/general.h > src/config/general.h.tmp
    mv src/config/general.h.tmp src/config/general.h
    docker run --rm -it -v $PWD:/home/coreboot/ipxe -w /home/coreboot/ipxe \
             coreboot/coreboot-sdk:2022-12-18_3b32af950d /bin/bash
    export CROSS_COMPILE="x86_64-elf-"
    make -C src bin-x86_64-efi-sb/ipxe.efi EMBED=$PWD/dasharo.ipxe BUILD_ID_CMD="echo 0x1234567890" \
        EXTRA_CFLAGS="-Wno-address-of-packed-member  -m64  -fuse-ld=bfd \
        -Wl,--build-id=none -fno-delete-null-pointer-checks -Wlogical-op -march=nocona \
        -malign-data=abi -mcmodel=large -mno-red-zone -fno-pic"
    ```

    This set of commands will embed Dasharo iPXE menu script, enable HTTPS and
    EFI image support and provide custom build ID command to ensure build
    reproducibility.

2. Exit docker container with `exit` command.
3. Create image file: `dd if=/dev/zero of=ipxe.img count=1 bs=1440K`
4. Make FAT filesystem on the image file: `mkfs.fat --mbr=y ipxe.img`
5. Mount the image file: `sudo mount ipxe.img /mnt`
6. Copy the iPXE to the mounted image file:

    ```bash
    sudo mkdir -p /mnt/EFI/BOOT/ && \
        sudo cp src/bin-x86_64-efi-sb/ipxe.efi /mnt/EFI/BOOT/BOOTX64.EFI
    ```

7. Unmount the image file: `sudo umount /mnt`

The resulting `ipxe.img` file is now ready to be attached as Virtual Media on
Supermicro BMC.
