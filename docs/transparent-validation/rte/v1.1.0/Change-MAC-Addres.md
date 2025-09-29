# Changing MAC Address on RTE

1. Connect with RTE via serial connection. While using a `minicom`

   there is a need to use the USB-UART converter.

   Open the serial connection by executing the following command:

    ```bash
    sudo minicom -D /dev/ttyUSB0 -b 115200
    ```

1. Check the current MAC address of the target network interface:

   ```bash
   ip a
   ```

   > Note the exact interface name for later use.

1. Navigate to the network configuration files:

   ```bash
   cd /etc/systemd/network
   ```

1. Open the file for the target interface using nano or vim.

   > If the file does not exist, create one following this scheme:
   > `10-eth0.network`, replacing `eth0` with the interface name

   ```bash
   vim 10-eth0.network
   ```

1. The file content should look as follows. Replace `eth0` with
   the interface name, `xx:xx:xx:xx:xx:xx` with desired IP address

   ```bash
   [Match]
   Name=eth0

   [Network]
   MACAddress=xx:xx:xx:xx:xx:xx
   ```

   Save the file and exit the editor.

1. Restart the systemd-networkd service:

   ```bash
   systemctl restart systemd-networkd
   ```

1. Reboot the platform:

  ```bash
  reboot now
  ```

1. After RTE boots, verify the MAC address:

   ```bash
   ip link show eth0
   ```
