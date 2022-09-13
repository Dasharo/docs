# Automatic fan control for ASUS KGPE-D16

Starting from KGPE-D16 Dasharo release v0.2.0, coreboot implements automatic
fan control. The feature is realized on the Nuvoton W83795 hardware monitor.

## Testing fan control

In order to check the monitoring values of W83795, one needs to install some
packages:

```shell
apt-get install lm-sensors
```

Linux kernel by default should come with `w83795` module. Load it with the
following command:

```shell
modprobe w83795
```

The `dmesg` should contain the following message after loading the module:

```shell
i2c i2c-1: Found w83795g rev. B at 0x2f
w83795 1-002f: hwmon_device_register() is deprecated.
     Please convert the driver to use hwmon_device_register_with_info().

```

To check the monitoring values execute:

```shell
sensors
```

The output should be similar to the one below:

```shell
k10temp-pci-00cb
Adapter: PCI adapter
temp1:        +36.5°C  (high = +70.0°C)
                       (crit = +106.0°C, hyst = +101.0°C)

w83795g-i2c-1-2f
Adapter: SMBus PIIX4 adapter at 0b20
in0:         910.00 mV (min =  +0.90 V, max =  +1.50 V)
in1:           0.00 V  (min =  +0.90 V, max =  +1.50 V)  ALARM
in2:           1.53 V  (min =  +1.10 V, max =  +1.61 V)
in3:          22.00 mV (min =  +1.10 V, max =  +1.61 V)  ALARM
in4:           1.21 V  (min =  +1.14 V, max =  +1.25 V)
in5:           0.00 V  (min =  +1.14 V, max =  +1.25 V)  ALARM
in6:           1.19 V  (min =  +1.05 V, max =  +1.25 V)
in7:           1.82 V  (min =  +1.70 V, max =  +1.90 V)
in8:           1.21 V  (min =  +1.14 V, max =  +1.25 V)
in9:           1.09 V  (min =  +1.05 V, max =  +1.15 V)
in10:          1.60 V  (min =  +1.50 V, max =  +1.63 V)
in11:        752.00 mV (min =  +0.00 V, max =  +0.01 V)  ALARM
+3.3V:         3.26 V  (min =  +2.96 V, max =  +3.63 V)
3VSB:          3.28 V  (min =  +2.96 V, max =  +3.63 V)
Vbat:          3.16 V  (min =  +2.70 V, max =  +3.63 V)
in15:          1.02 V  (min =  +0.91 V, max =  +1.08 V)
in16:          1.55 V  (min =  +1.50 V, max =  +1.62 V)
fan1:        1157 RPM  (min =  329 RPM)
fan2:           0 RPM  (min =  329 RPM)  ALARM
fan3:           0 RPM  (min =  329 RPM)  ALARM
fan4:           0 RPM  (min =  329 RPM)  ALARM
fan5:           0 RPM  (min =  329 RPM)  ALARM
fan6:           0 RPM  (min =  329 RPM)  ALARM
fan7:           0 RPM  (min =  329 RPM)  ALARM
fan8:           0 RPM  (min =  329 RPM)  ALARM
temp1:        +37.2°C  (high = +70.0°C, hyst = +65.0°C)
                       (crit = +90.0°C, hyst = +80.0°C)  sensor = thermal diode
temp2:        -62.5°C  (high =  +0.0°C, hyst =  +0.0°C)
                       (crit =  +0.0°C, hyst =  +0.0°C)  sensor = thermistor
temp3:        -62.5°C  (high =  +0.0°C, hyst =  +0.0°C)
                       (crit =  +0.0°C, hyst =  +0.0°C)  sensor = thermistor
temp7:        +36.8°C  (high = +70.0°C, hyst = +65.0°C)
                       (crit = +90.0°C, hyst = +80.0°C)  sensor = AMD AMDSI
temp8:         +0.0°C  (high = +70.0°C, hyst = +65.0°C)
                       (crit = +90.0°C, hyst = +80.0°C)  sensor = AMD AMDSI
intrusion0:  ALARM
beep_enable: disabled

fam15h_power-pci-00c4
Adapter: PCI adapter
power1:       49.44 W  (crit = 139.72 W)

k10temp-pci-00c3
Adapter: PCI adapter
temp1:        +36.8°C  (high = +70.0°C)
                       (crit = +106.0°C, hyst = +99.0°C)
```

The CPU temperature is indicated with k10temp and w83795g temp7 inputs and the
CPU fan speed is indicated by fan1.

## Alternative automatic fan control

If you are using a coreboot for KGPE-D16 built from 4.11 branch or earlier
there is also a software option to enable automatic fan control without
modifications in coreboot. In order to configure the fan control, one needs to
install the following package:

```shell
apt-get install fancontrol
```

Now we need to configure the fancontrol application by generating a
`/etc/fancontrol` file containing the relation of temperature inputs to fans.
Be sure that w83795 module is loaded (you may also add the module to be loaded
automatically with `echo w38795 >> /etc/modules`). Execute:

```shell
pwmconfig
```

This application will lead you through the process of identifying the relation
of the fans and temperatures. Simply follow the instructions printed on the
console. At the end do not select save and ext, just configure all PWMs, e.g.:

```shell
Select fan output to configure, or other action:
1) hwmon0/device/pwm1  3) Just quit	      5) Show configuration
2) Change INTERVAL     4) Save and quit
select (1-n): 1
```

Then set up temperature correlation by selecting either `k10temp` or
`hwmon0/device/temp7_input` as temperature source for the fan1 (they should
report identical temperature). When finished, select `Save and quit`. For a
single CPU - single fan configuration it should result in a file like this:

```txt
INTERVAL=10
DEVPATH=hwmon0=devices/pci0000:00/0000:00:14.0/i2c-1/1-002f
DEVNAME=hwmon0=w83795g
FCTEMPS=hwmon0/device/pwm1=hwmon0/device/temp7_input
FCFANS= hwmon0/device/pwm1=hwmon0/device/fan1_input
MINTEMP=hwmon0/device/pwm1=20
MAXTEMP=hwmon0/device/pwm1=80
MINSTART=hwmon0/device/pwm1=150
MINSTOP=hwmon0/device/pwm1=0
```

> NOTE: hwmonX may be different depending on the order of loaded modules, if
> loaded automatically via `etc/modules` it may be hwmon0, if loaded using
> `modprobe` it may be hwmon3 or hwmon4.

Now that the configuration file is ready, time to start the fancontrol service:

```shell
systemctl enable fancontrol
systemctl start fancontrol
systemctl status fancontrol
● fancontrol.service - fan speed regulator
     Loaded: loaded (/lib/systemd/system/fancontrol.service; enabled; vendor pr>
     Active: active (running) since Wed 2021-12-08 11:23:23 CET; 9min ago
       Docs: man:fancontrol(8)
             man:pwmconfig(8)
   Main PID: 1318 (fancontrol)
      Tasks: 2 (limit: 19153)
     Memory: 1.3M
        CPU: 1.340s
     CGroup: /system.slice/fancontrol.service
             ├─1318 /bin/bash /usr/sbin/fancontrol
             └─2228 sleep 10

Dec 08 11:23:24 debian fancontrol[1318]:   Controls hwmon0/device/fan1_input
Dec 08 11:23:24 debian fancontrol[1318]:   MINTEMP=20
Dec 08 11:23:24 debian fancontrol[1318]:   MAXTEMP=80
Dec 08 11:23:24 debian fancontrol[1318]:   MINSTART=150
Dec 08 11:23:24 debian fancontrol[1318]:   MINSTOP=0
Dec 08 11:23:24 debian fancontrol[1318]:   MINPWM=0
Dec 08 11:23:24 debian fancontrol[1318]:   MAXPWM=255
Dec 08 11:23:24 debian fancontrol[1318]:   AVERAGE=1
Dec 08 11:23:24 debian fancontrol[1318]: Enabling PWM on fans...
Dec 08 11:23:24 debian fancontrol[1318]: Starting automatic fan control...
```

It should print the service is running. Now check the fan speed with `sensors`
command from `lm-sensors` package (install it if you haven't done it yet). For
CPU temperature of 40 Celsius degrees the fan1 speed should be a little bit
lower than 3000 RPM. Note it is advised to stop and disable the fancontrol
service when using Dasharo for KGPE-D16 release v0.2.0 or newer:

```shell
systemctl disable fancontrol
systemctl stop fancontrol
```

## Verifying fan speed adaptation

To check if the fan speed adapts to the temperature you may install `stress-ng`:

```shell
apt-get install stress-ng
```

With the following command you may cause a 2 minutes stress on the CPUs and
raise its temperature (it should hit about 70 Celsius degrees with that):

```shell
stress-ng --cpu 16 --io 8 --vm 4 --vm-bytes 4G --timeout 120s --metrics
```

Simultaneously watch the fan speed with `sensors` command. Example for
fancontrol service:

```shell
k10temp-pci-00cb
Adapter: PCI adapter
temp1:        +52.4°C  (high = +70.0°C)

w83795g-i2c-1-2f
Adapter: SMBus PIIX4 adapter at 0b20
in0:           1.09 V  (min =  +0.90 V, max =  +1.50 V)
in1:           0.00 V  (min =  +0.90 V, max =  +1.50 V)  ALARM
in2:           1.53 V  (min =  +1.10 V, max =  +1.61 V)
in3:          22.00 mV (min =  +1.10 V, max =  +1.61 V)  ALARM
in4:           1.21 V  (min =  +1.14 V, max =  +1.25 V)
in5:           0.00 V  (min =  +1.14 V, max =  +1.25 V)  ALARM
in6:           1.20 V  (min =  +1.05 V, max =  +1.25 V)
in7:           1.82 V  (min =  +1.70 V, max =  +1.90 V)
in8:           1.21 V  (min =  +1.14 V, max =  +1.25 V)
in9:           1.09 V  (min =  +1.05 V, max =  +1.15 V)
in10:          1.59 V  (min =  +1.50 V, max =  +1.63 V)
+3.3V:         3.24 V  (min =  +2.96 V, max =  +3.63 V)
3VSB:          3.28 V  (min =  +2.96 V, max =  +3.63 V)
Vbat:          3.06 V  (min =  +2.70 V, max =  +3.63 V)
in15:          1.01 V  (min =  +0.91 V, max =  +1.08 V)
in16:          1.54 V  (min =  +1.50 V, max =  +1.62 V)
fan1:        4299 RPM  (min =  329 RPM)
fan2:           0 RPM  (min =  329 RPM)  ALARM
fan3:           0 RPM  (min =  329 RPM)  ALARM
fan4:           0 RPM  (min =  329 RPM)  ALARM
fan5:           0 RPM  (min =  329 RPM)  ALARM
fan6:           0 RPM  (min =  329 RPM)  ALARM
fan7:           0 RPM  (min =  329 RPM)  ALARM
fan8:           0 RPM  (min =  329 RPM)  ALARM
temp1:        +52.5°C  (high = +70.0°C, hyst = +65.0°C)
                       (crit = +85.0°C, hyst = +80.0°C)  sensor = thermal diode
temp7:        +52.8°C  (high = +70.0°C, hyst = +65.0°C)
                       (crit = +85.0°C, hyst = +80.0°C)  sensor = AMD AMDSI
temp8:         +0.0°C  (high = +70.0°C, hyst = +65.0°C)
                       (crit = +85.0°C, hyst = +80.0°C)  sensor = AMD AMDSI
intrusion0:  ALARM
beep_enable: disabled

fam15h_power-pci-00c4
Adapter: PCI adapter
power1:      141.35 W  (crit = 139.72 W)

k10temp-pci-00c3
Adapter: PCI adapter
temp1:        +52.9°C  (high = +70.0°C)
```

For the software method with fancontrol service the fan speed adapts pretty
quickly, but when using the automatic fan control from Dasharo release the spin
up/down time is longer. coreboot configures the W83795 in Thermal Cruise mode
which automatically probes the CPU temperature via AMD SB TSI interface. The
target temperature is set to 50 Celsius degrees which means the chip will try
to keep the CPU temperature to be around 50 degrees by adapting the fan speed.
Summing it up, the longer the CPU temperature exceeds 50 degrees the faster the
fan will spin by slowly increasing the RPM. When the temperature is below 50
degrees for a long period of time the fan rotates with a speed of around 1000
RPM. The critical temperature is set to 90 Celsius degrees. When this point is
reached the W83795 should spin up to fans to full speed.
