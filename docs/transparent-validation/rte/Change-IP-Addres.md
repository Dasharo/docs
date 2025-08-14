# Changing IP Addres for RTE

Connect to RTE via Serial Connection or SSH.

Check the current IP address of the interface you want to modify:

```bash
ip a
```

> Note the exact interface name for later use.

Navigate to the network configuration files:

```bash
cd /etc/systemd/network
```

Open the file corresponding to desired network interface using nano or vim:

>If there is no file corresponding to the interface create one following naming scheme:
>`10-eth0.network` replacing `eth0` with intraface name

```bash
vim 10-eth0.network
```

The content of the file should look as follows, reaplace `eth0` with name of the interface,
`192.168.X.X` with desired IP Address and set proper gateway:

```bash
[Match]
Name=eth0

[Network]
DHCP=no
Address=192.168.X.X/24
Gateway=192.168.10.1
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

> If the value for `DHCP` in not change to `no` and/or the mac address
> has reserved IP Address the changes may not take effect
