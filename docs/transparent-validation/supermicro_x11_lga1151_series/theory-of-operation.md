# Supermicro X11 LGA1151 Series theory of operation

## Remote power control using ipmitool

To remote control supermicro you can use ipmitool.

```bash
ipmitool -H [bmc_ip] -U [bmc_username] -P [bmc_password] chassis power off
ipmitool -H [bmc_ip] -U [bmc_username] -P [bmc_password] chassis power on
ipmitool -H [bmc_ip] -U [bmc_username] -P [bmc_password] chassis power cycle
ipmitool -H [bmc_ip] -U [bmc_username] -P [bmc_password] chassis power reset
```

## Enabling SOL

This procedure is based on
[this documentation](https://www.fmad.io/blog/supermicro-serial-kvm).

Follow the steps below to set up a serial connection via ssh:

1. Enable SOL/COM2 console in BIOS. To do that in BIOS go to the `Advanced`
   section, then select `Serial Port Console Redirection` and set the
   `SOL/COM2 Console Redirection` option to `Enabled` state.

1. Edit the `/etc/default/grub` on your Linux-based OS file by adding:

    ```text
    linux /vmlinuz ro console=ttyS1,115200n8 earlyprintk=serial,ttyS1,115200n8
    ```

    > NOTE: If your Linux-based OS is QubesOS you should additionally remove the
      `plymouth.ignore-serial-consoles` phase to enable password disk
      authentication via SOL

1. Add the following lines to the `~/.ssh/config` file on your machine:

    ```text
    Host <IP>
    	HostKeyAlgorithms = +ssh-rsa
    	PubkeyAcceptedAlgorithms = +ssh-rsa
    ```

1. Connect with BMC via ssh:

    ```bash
    ssh ADMIN@<IP>
    ```

1. Then run the following command:

    ```bash
    cd system1/sol1
    ```

1. And start the serial console:

    ```bash
    start
    ```

If you want to run the SOL console again, repeat points 4-6.

## Using Supermicro Update Manager (SUM)

[Supermicro Update Manager](https://www.supermicro.com/en/solutions/management-software/supermicro-update-manager)
is a proprietary tool for interacting with Supermicro BMC. It can be used to
change BIOS settings or mount virtual drive through CLI, among other things.

Examples below assume that SUM was downloaded and extracted, and commands are
executed from directory with `sum` executable.

### Mounting floppy image

```bash
./sum -i [bmc_ip] -u [bmc_username] -p [bmc_password] -c MountFloppyImage --file path/to/file.img
```

### Mounting ISO image

Contrary to mounting floppy, for ISO you have to pass URL instead of path to
local file. SUM supports SAMBA, HTTP and, in latest versions, HTTPS.

```bash
./sum -i [bmc_ip] -u [bmc_username] -p [bmc_password] -c MountIsoImage --image_url http://www.example.com/cd.iso
```

### Reading default and current BIOS configuration

To read out default settings:

```bash
./sum -i [bmc_ip] -u [bmc_username] -p [bmc_password] -c GetDefaultBiosCfg --file bios.cfg
```

To get current settings instead, change `GetDefaultBiosCfg` to
`GetCurrentBiosCfg`. In both cases, you can omit `--file bios.cfg` to print the
settings to standard output.

### Writing settings to BIOS

```bash
./sum -i [bmc_ip] -u [bmc_username] -p [bmc_password] -c ChangeBiosCfg --file bios.cfg
```

There are additional switches to this command like `--reboot` and
`--post_complete`, but they require cooperation from the running OS. These
commands result in OS displaying power off (or log out) window, as if power
button was pressed. After 5 minutes or so a hard reboot is initiated. This gives
user a chance to save current work, but for test automation this may be
unnecessary delay.

File passed to this command can be a full configuration saved by one of the
previous commands, or it can be simplified to contain just the settings that are
to be changed, together with their section headers. Any option not listed in
simplified file will not be changed.

For example, to enable TXT you can use file with following content:

```text
[Advanced|Trusted Computing]
TXT Support=01
```
