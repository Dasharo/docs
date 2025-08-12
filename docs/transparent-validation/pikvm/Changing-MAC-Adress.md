# Changing MAC Adresss on PiKVM

Connect to PiKVM via Serial Connection or SSH.

Check the current MAC address of the interface you want to modify:

```bash
ip a
```

> Note the exact interface name for later use.

Remount the filesystem in read-write mode:

```bash
sudo mount -o remount,rw /
```

Open the file `/etc/udev/rules.d/70-persistent-net.rules` with nano or vim:

```bash
sudo nano /etc/udev/rules.d/70-persistent-net.rules
```

Add this line, replacing `eth0` with your interface name and
`XX:XX:XX:XX:XX:XX` with your desired MAC address:

```bash
ACTION=="add", SUBSYSTEM=="net", KERNEL=="eth0", RUN+="/usr/bin/ip link set dev eth0 address XX:XX:XX:XX:XX:XX"
```

Reload udev rules and reboot PiKVM:

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
sudo reboot
```

After reboot, verify the new MAC address for your interface:

```bash
ip link show eth0
```
