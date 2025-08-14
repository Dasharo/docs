# Changing IP Addres for RTE

1. Connect with RTE via ssh or serial connection.

    While using a `minicom` there is a need to use the USB-UART converter.

   The serial connection can be opened by executing the following command:
    
    ```bash
    sudo minicom -D /dev/ttyUSB0 -b 115200 
    ```

1. Check the current IP address of the target network interface:

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

1. The file content should look as follows. Replace `eth0` with the interface

   name, `192.168.X.X` with desired IP address and set the proper gateway:

   ```bash
   [Match]
   Name=eth0

   [Network]
   DHCP=no
   Address=192.168.X.X/24
   Gateway=192.168.10.1
   ```

   Save the file and exit the editor.

1. Restart the systemd-networkd service:

   ```bash
   systemctl restart systemd-networkd
   ```

1. Verify the new IP address of the interface:

   ```bash
   ip a
   ```
   > Note: If `DHCP` parameter is not set to `no` or the MAC address has a reserved IP,
   > the changes may not be applied.
