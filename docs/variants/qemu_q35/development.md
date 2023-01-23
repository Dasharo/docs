# Dasharo (UEFI) v0.1.0 for QEMU Q35


1.  Please verify your qemu installation, and then invoke the qemu emulator with the built OVMF firmware image as given below:
    
	```bash 
	qemu-system-x86_64 -drive if=pflash,format=raw,file=Build/OvmfX64/DEBUG_GCC5/FV/OVMF.fd -nographic -debugcon file:debug.log -global isa-debugcon.iobase=0x402 -global ICH9-LPC.disable_s3=1 -net none -machine q35,smm=on
	```
	
	*  The `-drive` parameter indicates that the device is a pflash with the firmware image file pointing out to the built OVMF.fd image.
	
	* `-nographic` indicates to start the qemu emulator without any graphical output. This is useful while testing in the environment like docker.
	
	* `-debugcon file:debug.log -global isa-debugcon.iobase=0x402` default OVMF build writes debug messages to IO port **0x402**. The following qemu command line options save them in the file called debug.log.
	
	* `-global ICH9-LPC.disable_s3=1` SMM is put to use in the S3 suspend and resume infrastructure, and in the UEFI variable driver stack. Similarly, a pflash-backed variable store is a requirement. As SMM was enabled while building the firmware image.
	
	* `-net none` disables the OptionROM execution which will interfere with the firmware image, if not disabled.
	
	* `-machine q35,smm=on` For SMM to work, only Q35 machines are supported hence the machine type.

2. After executing the above qemu command, one should be able to see the UEFI built-in shell and should be able to get to the BIOS selection area.

3. The features which are enabled in the `OvmfPkgX64.dsc` can be verified in the `BIOS menu` and also at the `Device Manager section` and the Dasharo features can be verified at the `Dasharo System Features` section.



## Useful Tips for modifying the changes in .DSC & .FDF


### Following the below guide, one can rebuild the firmware image and run it in the qemu and experiment with the features which are needed.


1.  By making some changes in the `OvmfPkgX64.dsc` file, one can add features like OPAL, SATA security support for QEMU Q35 machine and also for specific platforms. 

	* An example of where the changes can be made in the `OvmfPkgX64.dsc` file is given below. 
	
	> The following changes describe about defining in the **Defines Section** of `OvmfPkgX64.dsc`
	
	```bash
  	# Defines for default states.  These can be changed on the command line.
  	# -D FLAG=VALUE
  	#
  	(...)
  	DEFINE SATA_PASSWORD_ENABLE    = TRUE
  	DEFINE OPAL_PASSWORD_ENABLE    = TRUE
	```
	
	
	* Include the appropriate libraries in the **Libraries Section** of `OvmfPkgX64.dsc`
	
	```bash
	#
	# OPAL_PASSWORD
	#

	!if $(OPAL_PASSWORD_ENABLE) == TRUE
	TcgStorageCoreLib|SecurityPkg/Library/TcgStorageCoreLib/TcgStorageCoreLib.inf
	TcgStorageOpalLib|SecurityPkg/Library/TcgStorageOpalLib/TcgStorageOpalLib.inf
	!endif
	S3BootScriptLib|MdePkg/Library/BaseS3BootScriptLibNull/BaseS3BootScriptLibNull.inf
	#
	#
	```
	
	> Depending upon the feature, proper PCD's must be defined in the `OvmfPkgX64.dsc` file. 
	
	
	* Addition of the components in the **Components Section** of `OvmfPkgX64.dsc` file.
	
	```bash
	### SATA_PASSWORD
	
	!if $(SATA_PASSWORD_ENABLE) == TRUE
	SecurityPkg/HddPassword/HddPasswordPei.inf
	!endif
	#
	#
	```
	
2.  The .FDF file tells about the location of the source file and options to be used for the build process.

	* Below code snippet shows about the location of the `SATA_PASSWORD` .inf file.
	
	```bash
	!if $(SATA_PASSWORD_ENABLE) == TRUE
	INF SecurityPkg/HddPassword/HddPasswordDxe.inf
	!endif
	```
	
	> It is important to include all the necessary source file locations to point out the source libraries in .FDF file
	
	* Below is the snippet of the SATA_PASSWORD support in `Device Manager`.
	
![SATA_PASSWORD](images/q35-dasharo-device-manager.png)
	
	

3.  By default the `Dasharo System Features` are disabled in the **DasharoSystemFeatures.dec** file which describes the configuration of the platform.

	* The flags can be toggled in order to enable the `Dasharo System Features` and view the features in `BIOS Menu => Dasharo System Features` menu.
	
	```bash
	[PcdsFixedAtBuild]
	gDasharoSystemFeaturesTokenSpaceGuid.PcdShowMenu|TRUE|BOOLEAN|0x00000001
	gDasharoSystemFeaturesTokenSpaceGuid.PcdShowSecurityMenu|TRUE|BOOLEAN|0x00000002
	gDasharoSystemFeaturesTokenSpaceGuid.PcdShowIntelMeMenu|TRUE|BOOLEAN|0x00000003
	gDasharoSystemFeaturesTokenSpaceGuid.PcdShowUsbMenu|TRUE|BOOLEAN|0x00000004
	gDasharoSystemFeaturesTokenSpaceGuid.PcdShowNetworkMenu|TRUE|BOOLEAN|0x00000005
	gDasharoSystemFeaturesTokenSpaceGuid.PcdShowChipsetMenu|TRUE|BOOLEAN|0x00000006
	gDasharoSystemFeaturesTokenSpaceGuid.PcdDefaultNetworkBootEnable|FALSE|BOOLEAN|0x00000007
	```

	> In the above PCD definitions, please check the column after PCD definition in order to find the value of **TRUE/FALSE**. 
	>
	> By toggling these flags, one can view the Dasharo System Features.
	
	* The below image shows the Dasharo System Features enabled for the QEMU Q35 machine.
	
![DasharoSystemFeatures](images/q35-dasharo-features.png)

