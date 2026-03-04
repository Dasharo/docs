# USB Sniffer usage and preparation

## Requirements

- USB Sniffer
- Computer running Linux (tested on Fedora 42)

## Step 1 — Clone the repository

    ```bash
    git clone https://github.com/ataradov/usb-sniffer.git
    cd usb-sniffer/bin
    ```

## Step 2 — Set udev rules

   Enables device access without root privileges:

    ```bash
    sudo cp 90-usb-sniffer.rules /etc/udev/rules.d/
    sudo udevadm control --reload-rules
    sudo udevadm trigger
    ```

## Step 3 — Connect the sniffer and verify detection

   Connect the sniffer via USB-C to the computer, and verify
   the system recognizes it:

    The board should light up a green and an orange LED

    ```bash
    lsusb
    ```

   Expected output (new, unprogrammed board):

    ```
    Device XXX: ID 04b4:8613 Cypress Semiconductor Corp.
    CY7C68013 EZ-USB FX2
    ```

## Step 4 — Grant execute permission to the binary

    ```bash
    chmod +x usb_sniffer_linux
    ```

## Step 5 — Flash firmware to MCU SRAM

    ```bash
    ./usb_sniffer_linux --mcu-sram usb_sniffer.bin
    ```

   The device will reset and appear as "USB Sniffer".

    Check `lsusb` to confirm.

    Expected output (unprogrammed board):

    ```
    Device XXX: ID 6666:6620 Prototype product Vendor ID
    USB Sniffer
    ```

## Step 6 — Flash firmware to MCU EEPROM

    ```bash
    ./usb_sniffer_linux --mcu-eeprom usb_sniffer.bin
    ```

   After this step **disconnect and reconnect the sniffer**
   (power cycle).

## Step 7 — Flash bitstream to FPGA flash

    ```bash
    ./usb_sniffer_linux --fpga-flash usb_sniffer_impl.jed
    ```

   **Disconnect and reconnect the sniffer** again.

    After reboot, only the green LED should be lit.

## Step 8 — Performance test

    ```bash
    ./usb_sniffer_linux --test
    ```

   **Expected result: 40–50 MB/s**

---

 More information can be found on the
 [USB-Sniffer GitHub page](https://github.com/ataradov/usb-sniffer)
