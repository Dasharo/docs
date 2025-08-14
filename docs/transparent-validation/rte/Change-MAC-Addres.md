# Changing MAC Addresss on RTE

Connect to RTE via Serial Connection.

While booting, wait for the message: `Hit any key to stop autoboot:`.

Press any key to stop loading U-Boot.

Set the new MAC address, by Overwriting the variable `ethaddres` 
replacing `XX:XX:XX:XX:XX:XX` with desired MAC Address:

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

After RTE boots, verify the MAC address:

```bash
ip link show eth0
```

> Note: If the Serial ID changes, your custom MAC will be lost!

