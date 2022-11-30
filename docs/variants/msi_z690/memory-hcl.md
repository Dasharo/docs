---
hide:
  - toc
---

# Memory HCL

## Contributing

Feel free to test different modules and report your results via
[email](mailto:contact@dasharo.com) or submit a Pull Request to
[Dasharo documentation repository](https://github.com/Dasharo/docs).

Be sure to include information about the memory:

1. If using Linux use `sudo dmidecode -t memory`.
1. If using Windows attach screenshots from CPU-Z for example.
1. Part Number of the Memory Modules:

    - If you have physical access to the modules, the Part Number is printed on
      a sticker. You may send a photo where the sticker is legible if you can't
      identify it.
    - The Part Number is also usually available as data on the SPD and
      retrievable via Software (see point 2 below), but sometimes it is
      possible than it doesn't match the Part Number on the sticker, or that it
      wasn't programmed onto the SPD at all.

1. Dump of SPD Profiles:

    - If using Linux use `sudo dmidecode -t memory`. Additionally you may
      provide SPD data binaries (example for Ubuntu for all 4 DIMMs):

      ```shell
      sudo apt-get install i2c-tools
      decode-dimms > dimms.log
      cat /sys/bus/i2c/drivers/ee1004/0-0050/eeprom > dimm0_spd.bin
      cat /sys/bus/i2c/drivers/ee1004/0-0051/eeprom > dimm1_spd.bin
      cat /sys/bus/i2c/drivers/ee1004/0-0052/eeprom > dimm2_spd.bin
      cat /sys/bus/i2c/drivers/ee1004/0-0053/eeprom > dimm3_spd.bin
      ```

    - If using Windows attach screenshots from CPU-Z SPD Tab. If multiple
      modules are installed, make sure to open multiple CPU-Z instances and
      have each one cover a different Slot via the Memory Slot Selection drop
      down list.

DDR4 DIMMs include a SPD ROM which can have up to 4 SPD Profiles. Each SPD
Profile contains data for a combination of Speed (MHz), Timings and Voltage
that the module is factory rated to run at. These SPD Profiles can be
considered either JEDEC standard or XMP (Overclocking). Currently, Dasharo only
loads the JEDEC standard profile and ignores the XMP ones.

> Currently memory profile is not selectable via BIOS setup. This feature is
> planned for future releases.

## HCL list

Memory hardware Compatibility List present the DIMM modules tested and verified
to work with Dasharo in 3mdeb laboratory.

Memory Modules are tested in 1, 2 and 4 modules configurations. These follow
the DIMM population procedures as stated in the Board Manual: 1 module in
DIMMA2 Slot (Single Channel), 2 by adding another module in DIMMB2 (Dual
Channel), and 4 by populating all 4 slots. Testing is defined as passing
firmware POST and booting an OS, since what is being tested is that the Intel
FSP (Firmware Support Package) component is initializing the Memory Modules. We
don't stress test them for stability. Each SPD Profile is tested, so each
Memory Module can have from 1 to 4 entries. You may also check out
[Intel memory validation results](https://www.intel.com/content/www/us/en/platform-memory/platform-memory.html)
page and see the results for DDR4 UDIMM testing. Maximum ratings for Alder Lake
S CPUs is also available in the [CPU datasheet](https://edc.intel.com/content/www/us/en/design/ipla/software-development-platforms/client/platforms/alder-lake-desktop/12th-generation-intel-core-processors-datasheet-volume-1-of-2/001/processor-sku-support-matrix/).

Legend:

* Configuration 1/2/4 - means given memory module was tested in 1, 2 and 4
  DIMMs populated configuration, &#10004; means successfully tested, &#10006;
  means platform did not boot with Dasharo, e.g. &#10004;/&#10004;/&#10004;
  means all configurations work, `-` means not tested
* Size: DIMM capacity in GB
* SPD profile: can be one of JEDEC(Standard) / XMP Profile #1 / XMP Profile #2.
  Profile data:
    - Type/speed: for example DDR4-2400 means DDR4 module clocked at max 2400MHz
    for given profile
    - Timings: for example CL17-17-17 means CAS Latency 17, tRCD 17, tRP 17
    (numbers expressed in clock cycles) for given memory profile
    - Voltage: memory voltage in Volts for given memory profile

> NOTE: some XMP profiles may have lower speeds than other ones, but also have
> smaller CAS latency. Also the memory frequency configured in the memory
> controller and reported by DMI/SMBIOS may be slightly lower than advertised
> in the module specifications. This can vary based on the board design, CPU
> and many other factors.

### HCL list - MSI PRO Z690-A DDR4

| DIMM vendor | Part Number | Size | SPD profile | Configuration 1/2/4 |
|:-----------:|:-----------:|:----:|:-----------:|:-------------------:|
| Kingston | [KF436C17BBK4/32][1] |8GB | JEDEC: DDR4-2400 CL17-17-17 1.2V | &#10004;/&#10004;/&#10004; |
| Kingston | [KF436C17BBK4/32][1] |8GB | XMP profile #1: DDR4-3600 CL17-21-21 1.35V | -/-/&#10004; |
| Kingston | [KF436C17BBK4/32][1] |8GB | XMP profile #2: DDR4-3000 CL15-17-17 1.35V | -/-/&#10004; |
| Corsair  | [CMK16GX4M2B3200C16][2] |8GB | XMP 2.0: DDR4-3200 PC4-25600 CL16-18-18-36 1.35 V | -/-/&#10004; |
| Kingston | [KF432C16BB1/16][3] |16GB | JEDEC: DDR4-2400 CL17-17-17 1.2V | -/&#10004;&sup1;/&#10004; |
| PNY      | [8GBF1X08QFHH38-135-K-HXR][4] |8GB | JEDEC: DDR4-2133 CL15-15-15 1.2V | -/&#10004;&sup1;/&#10004; |
| Kingston | [KF436C18BBK2/64][5] |32GB | JEDEC: DDR4-2400 CL17-17-17-39 1.2V | &#10004;/&#10004;/- |
| Kingston | [KHX2666C16/16G][8] |16GB | JEDEC: DDR4-2133 CL16-18-18-39 1.2V | &#10004;/&#10004;/&#10004; |

1) Tested in 2x2 mixed configuration

### HCL list - MSI PRO Z690-A DDR5

| DIMM vendor | Part Number | Size | SPD profile | Configuration 1/2/4 |
|:-----------:|:-----------:|:----:|:-----------:|:-------------------:|
| Kingston    | [KF556C40BB/8][6] |8GB | 5600MT/s 40-40-40 1.25V | &#10004;/&#10004;/&#10004; |
| Crucial     | [CT8G48C40U5.M4A1/8][7] |8GB | 4800MT/s 40-39-39 1.1V | &#10004;/&#10004;/&#10004; |
| ADATA       | [AD5U48008G-S][9] |8GB | 4800MT/s 40-40-40 1.1V | &#10004;/&#10004;/&#10004; |

[1]: https://www.kingston.com/dataSheets/KF436C17BBK4_32.pdf
[2]: https://www.corsair.com/eu/en/Categories/Products/Memory/VENGEANCE-LPX/p/CMK16GX4M2B3200C16
[3]: https://www.kingston.com/dataSheets/KF432C16BB1_16.pdf
[4]: https://www.pny.com/anarchy-x-ddr4-red?sku=MD16GK2D4320016AXR
[5]: https://www.kingston.com/datasheets/KF436C18BBK2_64.pdf
[6]: https://www.kingston.com/memory/gaming/kingston-fury-beast-ddr5-memory
[7]: https://www.crucial.com/memory/ddr5/ct2k16g48c40u5
[8]: https://www.kingston.com/datasheets/HX426C16FRK4_64.pdf
[9]: https://www.adata.com/us/consumer/dram-module-ddr5-4800-u-dimm
