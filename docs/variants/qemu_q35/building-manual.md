#Dasharo (UEFI) v0.1.0 for QEMU Q35 - Building Manual

In order to build the `Dasharo (UEFI) OVMF firmware image for QEMU Q35`, please follow the given steps to build the Dasharo firmware image from the EDK2 repository:

1. Clone the official Dasharo EDK2 repository to your local instance with git or downloading the source code from github.

    ```bash
    git clone https://github.com/Dasharo/edk2.git 
    ```
       
2. Once it is done, please follow the below instructions, in order to prepare your environment for the building of the OVMF image.

	
	* Change the directory to Dasharo EDK2 repository locally - 
	
	```bash
	cd Dasharo/edk2
	```
	
	
	
	* Setup the environment variables with the following command - 
	
	```bash
	source edksetup.sh
	```
								       
	* Update the submodules in order get the latest dependencies and avoid any build process errors while building the OVMF image. 
	
	```bash
	git submodules update --init
	```
									       
3. In order to build the UEFI firmware image it can be done in two ways, one way is to give the flags with `-D SMM_REQUIRE` (SMM was actually enabled while building the firmware image, but the flags differ with feature to feature, so please check the OvmfPkgX64.dsc file). And second way is to set the flags in `OvmfPkgX64.dsc` and then build the firmware image. For the purpose of this documentation, I have preferred to set the features in `OvmfPkgX64.dsc` directly.

	Check the following build command:
    
	```bash 
	build -D DEBUG_ON_SERIAL_PORT -D BOOTLOADER=COREBOOT -a IA32 -a X64 -t GCC5 -b DEBUG -p OvmfPkg/OvmfPkgX64.dsc.
	```	
	
	* `DEBUG_ON_SERIAL_PORT` = The following flag must be given for the **DEBUG** build as the output is redirected to the I/O port **0x402** to qemu monitor. We will be able to see the debug messages on the given debug I/O port. (0x402 will be later utilized in the qemu invocation further in this documentation).

4. Once the build is completed, the OVMF firmware image can be found below given path: 

	```bash
	edk2/Build/Ovmf/DEBUG_GCC5/Ovmf.fd
	```
