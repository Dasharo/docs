# Changing MAC Address on PiKVM

1. Connect with PiKVM via serial connection. While using a `minicom`

   there is a need to use the USB-UART converter.

   Open the serial connection by executing the following command:

    ```bash
    sudo minicom -D /dev/ttyUSB0 -b 115200
    ```

1. Check the current MAC address of the network interface:

   ```bash
   ip a
   ```

   > Note the exact interface name for later use.

1. Remount the filesystem in read-write mode:

   ```bash
   sudo rw
   ```

1. Navigate to the network configuration files:

   ```bash
   cd /etc/systemd/network
   ```

1. Open the file corresponding to desired network interface using nano or vim:

   ```bash
   sudo nano wlan0.network
   ```

1. Add following lines to the file. Replace  `xx:xx:xx:xx:xx:xx` with desired
   MAC address:

   ```bash
   [Link]
   MACAddress=xx:xx:xx:xx:xx:xx
   ```

   Save the file and exit the editor.

1. Restart the systemd-networkd service:

   ```bash
   sudo systemctl restart systemd-networkd
   ```

1. Remount the filesystem in read-only mode:

   ```bash
   sudo ro
   ```

1. Reboot the system:

   ```bash
   sudo reboot now
   ```

1. Verify the new MAC address for your interface:

   ```bash
   ip a
   ```
