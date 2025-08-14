# Changing IP Addresss on PiKVM

Connect to PiKVM via Serial Connection or SSH.

Check the current IP address of the interface you want to modify:

```bash
ip a
```

> Note the exact interface name for later use.

Remount the filesystem in read-write mode:

```bash
sudo mount -o remount,rw /
```

Navigate to the network configuration files:

```bash
cd /etc/systemd/network
```

Open the file corresponding to desired network interface using nano or vim:

```bash
sudo nano wlan0.network
```

Under `[Network]`, update `Address` and `Gateway` to your desired values:

```bash
[Network]
Address=192.168.X.X/24
Gateway=192.168.X.X
```

Save the file and exit the editor.

Restart the systemd-networkd service:

```bash
sudo systemctl restart systemd-networkd
```

Verify the new IP address for your interface:

```bash
ip a
```
