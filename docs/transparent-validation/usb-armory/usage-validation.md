# USB Armory usage and preparation

## Requirements

- USB Armory MK II with empty eMMC
- Computer running Linux (tested on Fedora 42)

## 1. Installing Go

   Check if Go is already installed:

    ```bash
    go version
    ```

   If the command returns version `go1.26.0` or higher, proceed to step 2.
   Otherwise, install Go 1.26.0:

    ```bash
    wget https://go.dev/dl/go1.26.0.linux-amd64.tar.gz
    sudo tar -C /usr/local -xzf go1.26.0.linux-amd64.tar.gz
    ```

   Add Go paths to PATH:

    ```bash
    echo 'export PATH=/usr/local/go/bin:$HOME/go/bin:$PATH' \
      >> ~/.zshrc && source ~/.zshrc
    ```

   Verify the installation:

    ```bash
    go version
    ```

## 2. Installing Tools

### 2.1 Installing armory-boot-usb

    ```bash
    go install \
      github.com/usbarmory/armory-boot/cmd/armory-boot-usb@latest
    ```

   The tool will be installed at `~/go/bin/armory-boot-usb`.

### 2.2 Downloading UMS (USB Mass Storage) Firmware

    ```bash
    cd ~
    wget https://github.com/usbarmory/armory-ums/releases/latest/download/armory-ums.imx
    ```

### 2.3 Downloading the Debian Image for eMMC

    ```bash
    cd ~
    wget https://github.com/usbarmory/usbarmory-debian-base_image/releases/download/20250801/usbarmory-mark-two-emmc-debian_bookworm-base_image-20250801.raw.xz
    xz -d \
      usbarmory-mark-two-emmc-debian_bookworm-base_image-20250801.raw.xz
    ```

## 3. Verifying Serial Download Mode

   After connecting the USB Armory to the computer, both LEDs (white and
   blue) should glow faintly — this indicates the SoC is powered and in
   Serial Download Mode.
   Verify that the SoC has entered Serial Download Mode:

    ```bash
    sudo dmesg | tail -5
    ```

   Expected output:

    ```bash
    usb X-X: New USB device found, idVendor=15a2, idProduct=0080
    usb X-X: Product: SE Blank 6ULL
    usb X-X: Manufacturer: Freescale SemiConductor Inc
    ```

   If you see `SE Blank 6ULL` — the eMMC is empty and the SoC is waiting
   for firmware.

## 4. Loading UMS Firmware

   The UMS firmware is loaded into the device's RAM and exposes the eMMC
   as a USB Mass Storage device on the host computer. After the firmware
   is loaded, the blue LED on the USB Armory should light up brightly.

    ```bash
    sudo ~/go/bin/armory-boot-usb -i ~/armory-ums.imx
    ```

   Expected output:

    ```bash
    found device 15a2:0080 Freescale SemiConductor Inc  SE Blank 6ULL
    parsing /home/user/armory-ums.imx
    loading DCD at 0x00910000 (976 bytes)
    loading imx to 0x8000f400 (1793024 bytes)
    jumping to 0x8000f400
    serial download complete
    ```

## 5. Verifying the Block Device

   Wait 5 seconds, then check which new block device has appeared in the
   system:

    ```bash
    lsblk | grep disk
    ```

   The eMMC should appear as a new device (most commonly `/dev/sda`,
   but it may be `/dev/sdb` or another name if the computer has other
   USB drives connected). Identify it by the size matching the eMMC
   capacity (e.g. 14.6G for a 16GB chip).

   Verify that the device is a valid block device (in the commands below,
   replace `/dev/sda` with the correct device):

    ```bash
    ls -la /dev/sda
    ```

   **CRITICAL: Make sure it is a block device**

    ```bash
    brw-rw---- 1 root disk 8, 0 ... /dev/sda     <- CORRECT (brw-)
    -rw-r--r-- 1 root root ...      /dev/sda     <- ERROR (regular file!)
    ```

   If you see `-rw-` instead of `brw-`, it is a regular file, not a
   device.

## 6. Flashing the Image to eMMC

   Write the downloaded Debian image directly to the USB Armory's eMMC
   (replace `/dev/sda` with the device identified in step 5):

    ```bash
    IMAGE=usbarmory-mark-two-emmc-debian_bookworm-base_image-20250801.raw
    sudo dd if=/home/$USER/$IMAGE \
      of=/dev/sda bs=1M conv=fsync status=progress
    ```

   Expected output (will take a few minutes):

    ```bash
    3670016000 bytes (3.7 GB, 3.4 GiB) copied, ... s, XX MB/s
    3500+0 records in
    3500+0 records out
    ```

## 7. First Boot

   Disconnect the USB Armory, wait 5 seconds, then reconnect it. After
   approximately 30 seconds, once the system has booted, the white LED
   should start blinking (heartbeat), which means the Linux kernel has
   started and the system is active. The blinking frequency reflects
   CPU load.

   Check in `dmesg`:

    ```bash
    sudo dmesg -w
    ```

   Expected output (after ~30 seconds):

    ```bash
    usb X-X: Product: RNDIS/Ethernet Gadget
    usb X-X: Manufacturer: Linux 6.12.40-0 with 2184000.usb
    cdc_ether X-X:1.0 usb0: register 'cdc_ether' at usb-...
    ```

## 8. Network Configuration on the Host

### 8.1 Setting the IP Address

   Check the name of the USB Armory network interface:

    ```bash
    ip addr | grep enp0s20f0u
    ```

   Set the IP address:

    ```bash
    sudo ip addr add 10.0.0.2/24 dev <INTERFACE_NAME>
    ```

### 8.2 SSH Connection

   If you have previously connected to the USB Armory at 10.0.0.1
   (e.g. before re-flashing), SSH may reject the connection due to a
   changed host key. Remove the old key:

    ```bash
    ssh-keygen -R 10.0.0.1
    ```

   Connect to the USB Armory:

    ```bash
    ssh usbarmory@10.0.0.1
    ```

   Default credentials:

   | Field    | Value       |
   |----------|-------------|
   | Login    | `usbarmory` |
   | Password | `usbarmory` |

### 8.3 Sharing Internet Access (NAT)

   Run the following commands on the host computer (not on the USB
   Armory).

   Enable IP packet forwarding in the kernel:

    ```bash
    sudo sysctl -w net.ipv4.ip_forward=1
    ```

   Check which network interface the computer uses to access the
   internet:

    ```bash
    ip route | grep default
    ```

   The output will show the interface name, e.g. `enp0s20f0u1u3` or
   `wlp0s20f3`. Remember this name, it will be needed in the following
   commands as `<INTERNET_IF>`.

   Check the USB Armory interface name (from step 8.1) — it will be
   needed as `<USB_ARMORY_IF>`.

   Configure NAT, replace the source addresses of packets from the USB
   Armory with the address of the internet-facing interface:

    ```bash
    sudo iptables -t nat -A POSTROUTING -s 10.0.0.0/24 \
      -o <INTERNET_IF> -j MASQUERADE
    ```

   Allow packet forwarding from the USB Armory to the internet:

    ```bash
    sudo iptables -A FORWARD \
      -i <USB_ARMORY_IF> -o <INTERNET_IF> -j ACCEPT
    ```

   Allow return packets from the internet to the USB Armory:

    ```bash
    sudo iptables -A FORWARD -i <INTERNET_IF> -o <USB_ARMORY_IF> \
      -m state --state RELATED,ESTABLISHED -j ACCEPT
    ```

   Verify the connection on the USB Armory:

    ```bash
    ping -c 3 8.8.8.8
    ```

## 9. Expanding the Partition to Full eMMC Size

   The default image occupies ~3.5 GB. To use the full eMMC capacity:

    ```bash
    sudo fdisk /dev/mmcblk1 <<EOF
    d
    n
    p
    1
    10240
    w
    EOF
    sudo resize2fs /dev/mmcblk1p1
    ```

   Verification:

    ```bash
    df -h /
    ```

   Expected output (size depends on eMMC capacity):

    ```bash
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/root        15G  541M   14G   4% /
    ```

## 10. System Update

    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

---

   More information can be found on the
   [USB-Armory GitHub page](https://github.com/usbarmory/usbarmory)
