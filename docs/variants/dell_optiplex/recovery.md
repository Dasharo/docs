# Recovery

**Please read the [overview page](overview.md) first!**

---

Following documentation describe process of recovering hardware from brick
state with [RTE]() and Dasharo open-source firmware. Following procedure is
supported for following models

<center>

| Vendor | Model |
:-------:|:-----:|
|Dell    | OptiPlex 7010 SFF |
|Dell    | OptiPlex 7010 DT |
|Dell    | OptiPlex 9010 SFF |

</center>

## Step 1: Prepare hardware

1. To prepare hardware please follow
[hardware preparation](../initial-deployment/#hardware-preparation) procedure.
2. Follow instruction in the video to remove heatsink:
  <center>
  <iframe width="640" height="480"
    src="http://www.youtube.com/embed/TiUSTo-XwPo">
  </iframe>
  </center>

## Step 2: Connect SOIC-8 Pomona clip between RTE and target

## Step 2: Connect RTE

<center>
![](../../images/rte-boot.jpg)
</center>

1. Connect J2 Orange Pi Zero system debug output
2. Power the board and confirm it boots
3. **Please note** typical convention of USB-UART converter colors is as follows
    - black - GND
    - red - +5V
    - green - TX
    - white - RX
4. Connect terminal to RTE and read OS version:
    ```shell
    sudo minicom -b 115200 -D /dev/ttyUSB0 -o -C /tmp/minicom.cap
    ```
    * `-b 115200` sets baudrate
    * `-D /dev/ttyUSB0` points to USB-UART converter device, it can be different if
      you already have some devices connected or you use different operating system
    * `-o` skip initialization
    * `-C /tmp/minicom.cap` capture serial terminal output, if you will have
      problems with exercises please post this file
5. Login using following credentials:
    ```shell
    login: root
    password: meta-rte
    ```


