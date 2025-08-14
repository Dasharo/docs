# Changing MAC Addresss on RTE

Connect to RTE via Serial Connection.

While booting rte wait for `Hit any key to stop autoboot:` popup.
Hit any key to stop loading U-Boot.

Overwrite the variable `ethaddres` replacing `XX:XX:XX:XX:XX:XX` with desired MAC Address:

```bash
setenv ethaddr XX:XX:XX:XX:XX:XX
```

Save changes:

```bash
saveenv
```
Restart the platform:

```bash
run bootcmd
```

After RTE Boots MAC Adress can be veifed my running:

```bash
ip link show eth0
```

> Note: If Serial ID change, you will lost your custom MAC.

