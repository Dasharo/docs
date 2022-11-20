
Folloin

## Features

* Hardware features
	* [Write Protect Enable]()
	* OpenSK
		- build from source on hardware that belongs to me
		- `ssh-keygen -t ed25519-sk`
* Dasharo Disposable Chromebook Workload Profile
	* vboot
	* Dasharo System Features
	    - BIOS password
	* UEFI Secure Boot configuration
* Xubuntu Core
  * U2F for most important services
		- Gitlab
	* U2F for disk password
	* systemd-measure
  * [systemd-cryptenroll](https://man7.org/linux/man-pages/man1/systemd-cryptenroll.1.html)
	* Salt for configuration
		- install
			- firefox (consider tor browser)
			- vim
			- libpam-u2f
		- configure
			- firefox to use duckduckgo as default
	* Applications
	  - messangers

## Measured boot values

We are not yet sure how thos should be used correctly since support for
measured boot seem to not be consistent, but at least it is worth to gather
expected values for further development of disposable chromebook.

- https://wiki.tizen.org/Security:IntegrityMeasurement/Using_TPM
- https://openxt.atlassian.net/wiki/spaces/TEST/pages/30408724/TPM+PCRS+Values

## Dasharo System Features

### BIOS Password

We would like to provent simple attacks relying on changing BIOS configuration
(e.g. disabling UEFI Secure Boot).

## OpenSK provisoning

Since our disposable laptop can be left unattended some adversaries can replace
firmware on it. It will require getting through a lot of obstacles or create
fake environment which will pretend original one, but still it is possible.
Because of that our disposable chromebook should not contain any secrets. It is
way easier to keep with you USB token with that contain temporary keys which
can be used to get access to necessary services. For such purpose we use Google
OpenSK.

What we will do in this chapter:
* We will build OpenSK for Nordic nRF52840 Dongle from source
* We will provision USB token

### Requirements

* [Nordic nRF52840 Dongle](https://github.com/google/OpenSK/blob/stable/docs/boards/nrf52840_dongle.md)
* [Software requirements](https://github.com/google/OpenSK/blob/stable/docs/install.md#software-requirements)
	- pkg-config
  - libssl-dev
* Your use needs `dialout` group permission to access `/dev/ttyACM0`


### Token preparation

* Clone OpenSK repository and use `develop` branch to gain access to most
  recent features e.g. support for ed25519-sk

  ```bash
  git clone https://github.com/google/OpenSK.git -b develop
  ```

* Change directory

  ```bash
  cd OpenSK
  ```

* Change `DEFAULT_MIN_PIN_LENGTH` to NIST recommended 6 in `src/ctap/storage.rs`

* Create Python virtual environment

  ```bash
  virtualenv -p $(which python3) --system-site-packages venv
  ```

* Install `nrfutil`

  ```bash
  pip install nrfutil
  ```

* Activate virtual environment

  ```bash
  source venv/bin/activate
  ```

* Export path with `nrfutil`

  ```bash
  export PATH=/home/user/.local/bin:${PATH}
  ```

* Start setup

  ```bash
  ./setup.sh
  ```

* Enter DFU mode by pushing reset button on Nordic nRF52840 Dongle
* Run deploy command

  ```bash
	./deploy.py --board=nrf52840_dongle_dfu --opensk --programmer=nordicdfu --ed25519 --lock-device
  ```

* Correct output should look as follows

  ```bash
  info: Updating rust toolchain to nightly-2020-06-10
  info: syncing channel updates for 'nightly-2020-06-10-x86_64-unknown-linux-gnu'
  info: checking for self-updates
  info: component 'rust-std' for target 'thumbv7em-none-eabi' is up to date
  info: Rust toolchain up-to-date
  info: Building Tock OS for board nrf52840_dongle_dfu
  info: This is the version for the rustup toolchain manager, not the rustc compiler.
  info: The currently active `rustc` version is `rustc 1.45.0-nightly (fe10f1a49 2020-06-02)`
      Finished release [optimized + debuginfo] target(s) in 0.02s
  info: Building OpenSK application
      Finished release [optimized] target(s) in 0.03s
  info: Generating Tock TAB file for application/example ctap2
  info: Generating all-merged HEX file: target/nrf52840_dongle_dfu_merged.hex
  info: Creating DFU package
  info: Please insert the dongle and switch it to DFU mode by keeping the button pressed while inserting...
  info: Press [ENTER] when ready.
  
  info: Flashing device using DFU...
    [####################################]  100%          
  Device programmed.
  ```

