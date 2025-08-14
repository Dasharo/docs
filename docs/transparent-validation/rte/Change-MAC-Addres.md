# Changing MAC Addresss on RTE


1. Connect with RTE via serial connection. While using a
   `minicom` there is a need to use the USB-UART converter.

   Open the serial connection by executing the following command:
    
    ```bash
    sudo minicom -D /dev/ttyUSB0 -b 115200 
    ```

1. Reboot RTE.

   While booting, wait for the message: `Hit any key to stop autoboot:`.

   Press any key to stop loading U-Boot.

1. Set the new MAC address, by Overwriting the variable `ethaddres` 
   replacing `XX:XX:XX:XX:XX:XX` with desired MAC Address:

   ```bash
   setenv ethaddr XX:XX:XX:XX:XX:XX
   ```

1. Save changes:

   ```bash
   saveenv
   ```

1. Restart the platform:

   ```bash
   run bootcmd
   ```

1. After RTE boots, verify the MAC address:

   ```bash
   ip link show eth0
   ```

   > Note: If the Serial ID changes, your custom MAC will be lost!

