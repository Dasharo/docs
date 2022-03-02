# RTE Update

Following procedure describe how to check current version of operating system
for RTE and how to update it to most recent one.

## Check OS version

* Login using following credentials:
```shell
login: root
password: meta-rte
```

* Obtain OS version
```shell
cat /etc/os-release
```

* The output should look similar to:
```shell
ID="rte"
NAME="RTE (Remote Test Environment Distro)"
VERSION="0.5.3 (rocko)"
VERSION_ID="0.5.3"
PRETTY_NAME="RTE (Remote Test Environment Distro) 0.5.3 (rocko)"
```

* Please check [GitHub](https://github.com/3mdeb/meta-rte/releases) for new releases.

# Flash update to SD card

* To download new SD card image:
```shell
$ wget https://github.com/3mdeb/meta-rte/releases/download/v0.7.1/core-image-minimal-orange-pi-zero-v0.7.1.wic.gz -O v0.7.1.zip
```

* Decompress:
```shell
$ unzip v0.7.1.zip
   creating: v0.7.1/
  extracting: v0.7.1/core-image-minimal-orange-pi-zero-v0.7.1.wic.bmap
  extracting: v0.7.1/core-image-minimal-orange-pi-zero-v0.7.1.wic.gz
```

* `poweroff` system and remove SD card
* To flash SD card you need `bmaptool`, which should be available in your
  distribution as `bmap-tools` package
  ```shell
  $ sudo bmaptool copy --bmap core-image-minimal-orange-pi-zero-v0.7.1.wic.bmap \
  core-image-minimal-orange-pi-zero-v0.7.1.wic.gz /dev/<sdcard>
  ```
