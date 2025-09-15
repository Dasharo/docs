# Changing PiKVM IP Address to static

1. Connect with PiKVM via serial connection. While using a `minicom`

   there is a need to use the USB-UART converter.

   Open the serial connection by executing the following command:

    ```bash
    sudo minicom -D /dev/ttyUSB0 -b 115200
    ```

1. Check the current IP address of the interface you want to modify:

   ```bash
   ip a
   ```

   > Note the exact interface name for later use.

1. Remount the filesystem in read-write mode:

   ```bash
   sudo mount -o remount,rw /
   ```

1. Navigate to the network configuration files:

   ```bash
   cd /etc/systemd/network
   ```

1. Open the file corresponding to desired network interface using nano or vim:

   ```bash
   sudo nano wlan0.network
   ```

1. The file content should look as follows. Replace `wlan0` with the interface
   name, `192.168.X.X` with desired IP address and set the proper gateway:

   ```bash
   [Match]
   Name=wlan0
   [Network]
   DHCP=no
   Address=192.168.X.X/24
   Gateway=192.168.X.X
   ```

   Save the file and exit the editor.

   > To return to a DHCP connection, remove the `Address` and `Gateway` variables,
   > set the `DHCP` property to `yes`.

1. Restart the systemd-networkd service:

   ```bash
   sudo systemctl restart systemd-networkd
   ```

1. Verify the new IP address for your interface:

   ```bash
   ip a
   ```
