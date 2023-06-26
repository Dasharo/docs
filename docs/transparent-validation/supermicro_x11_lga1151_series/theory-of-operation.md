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

1. Add the following lines to the `/etc/ssh/ssh_config` file on your machine:

    ```bash
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
