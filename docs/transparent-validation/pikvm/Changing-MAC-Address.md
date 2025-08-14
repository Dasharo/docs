# Changing MAC Addresss on PiKVM

1. Connect with PiKVM via serial connection. While using a `minicom`
  
   there is a need to use the USB-UART converter.

   Open the serial connection by executing the following command:
    
    ```bash
    sudo minicom -D /dev/ttyUSB0 -b 115200 
    ```

1. Check the current MAC address of the interface you want to modify:

   ```bash
   ip a
   ```

   > Note the exact interface name for later use.

1. Remount the filesystem in read-write mode:

   ```bash
   sudo mount -o remount,rw /
   ```

1. Open the file `/etc/udev/rules.d/70-persistent-net.rules` with nano or vim:

   ```bash
   sudo nano /etc/udev/rules.d/70-persistent-net.rules
   ```
1. Add following line, replacing `eth0` with your interface name
   and `XX:XX:XX:XX:XX:XX` with your desired MAC address:

   ```bash
   ACTION=="add", SUBSYSTEM=="net", KERNEL=="eth0", RUN+="/usr/bin/ip link set dev eth0 address XX:XX:XX:XX:XX:XX"
   ```

1. Reload udev rules and reboot PiKVM:

   ```bash
   sudo udevadm control --reload-rules
   sudo udevadm trigger
   sudo reboot
   ```

1. After reboot, verify the new MAC address for your interface:

   ```bash
   ip link show eth0
   ```
