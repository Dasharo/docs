# FAQ

## How to identify my mainboard model?

```shell
~# dmidecode -t baseboard
# dmidecode 3.0
Getting SMBIOS data from sysfs.
SMBIOS 3.0 present.

Handle 0x0002, DMI type 2, 15 bytes
Base Board Information
	Manufacturer: Supermicro
	Product Name: X11SSH-TF
	Version: 1.01
	Serial Number: WM123S123456
	Asset Tag: To be filled by O.E.M.
	Features:
		Board is a hosting board
		Board is replaceable
	Location In Chassis: To be filled by O.E.M.
	Chassis Handle: 0x0003
	Type: Motherboard
	Contained Object Handles: 0

Handle 0x0026, DMI type 41, 11 bytes
Onboard Device
	Reference Designation: ASPEED Video AST2400
	Type: Video
	Status: Enabled
	Type Instance: 1
	Bus Address: 0000:03:00.0

Handle 0x0027, DMI type 41, 11 bytes
Onboard Device
	Reference Designation: Intel LAN X550-AT2 #1
	Type: Ethernet
	Status: Enabled
	Type Instance: 1
	Bus Address: 0000:04:00.0

Handle 0x0028, DMI type 41, 11 bytes
Onboard Device
	Reference Designation: Intel LAN X550-AT2 #2
	Type: Ethernet
	Status: Enabled
	Type Instance: 2
	Bus Address: 0000:04:00.1

Handle 0x0029, DMI type 41, 11 bytes
Onboard Device
	Reference Designation: Avago SAS 3008
	Type: SAS Controller
	Status: Disabled
	Type Instance: 1
	Bus Address: 0000:ff:00.0
```


