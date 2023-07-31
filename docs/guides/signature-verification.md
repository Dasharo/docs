# Dasharo release signature verification

Dasharo uses digital signatures to guarantee the authenticity and integrity of
certain important assets. This page explains how to verify those signatures.
It is extremely important for your security to understand and apply these
practices.

## Why one should verify the signatures?

Please refer to Qubes OS signature verification page:
[What digital signatures can and cannot prove](https://www.qubes-os.org/security/verifying-signatures/#what-digital-signatures-can-and-cannot-prove).

## Signature verification prcocedure

Each published Dasharo release is signed with a signing key corresponding to
given platform and versions. The key infrastructure is stored in
[3mdeb-secpack](https://github.com/3mdeb/3mdeb-secpack).

For the signature verification we use the
[OpenPGP software like Qubes OS](https://www.qubes-os.org/security/verifying-signatures/#openpgp-software).

To verify the integrity of the binaries published in release notes on this
site, please follow the instructions below:

1. Import necessary keys to your keyring:

    ```bash
    wget https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc \
        -O - | gpg --import -
    ```

    ```bash
    wget https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/3mdeb-dasharo-master-key.asc  \
        -O - | gpg --import -
    ```

    ```bash
    wget <release signing key URL> -O - | gpg --import -
    ```

    - `<release signing key URL>` is provided in the release notes

2. CHeck the signatures on the keys:

    ```bash
    gpg --check-signatures "Dasharo" "3mdeb"
    ```

3. Download the binaries, SHA sums and their signature files

    ```bash
    wget <binary url>
    ```

    ```bash
    wget <binary url>.sha256
    ```

    ```bash
    wget <binary url>.sha256.sig
    ```

4. Verify the signatures and binary integrity:

    ```bash
    gpg -v --verify <binary file>.sha256.sig <binary file>.sha256
    ```

    ```bash
    sha256sum -c <binary file>.sha256
    ```

Example verification of Dasharo release compatible with MSI PRO Z690-A DDR4:

```bash
miczyg@thanatos:/tmp$ gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc
gpg: requesting key from 'https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/keys/master-key/3mdeb-master-key.asc'
gpg: key 4AFD81D97BD37C54: "3mdeb Master Key <contact@3mdeb.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
miczyg@thanatos:/tmp$ gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/3mdeb-dasharo-master-key.asc
gpg: requesting key from 'https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/3mdeb-dasharo-master-key.asc'
gpg: key ABE1D0BC66278008: "3mdeb Dasharo Master Key" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
miczyg@thanatos:/tmp$ gpg --fetch-keys https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-1.x-compatible-with-msi-ms-7d25-signing-key.asc
gpg: requesting key from 'https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-1.x-compatible-with-msi-ms-7d25-signing-key.asc'
gpg: key 5DC481E1F371151E: "Dasharo release 1.x compatible with MSI MS-7D25 signing key" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
miczyg@thanatos:/tmp$ gpg --check-signatures "3mdeb" "Dasharo"
...
pub   rsa4096 2019-02-12 [SC]
      1B5785C2965D84CF85D1652B4AFD81D97BD37C54
uid           [ unknown] 3mdeb Master Key <contact@3mdeb.com>
sig!3        4AFD81D97BD37C54 2019-02-12  3mdeb Master Key <contact@3mdeb.com>
sig!         B2EE71E967AA9E4C 2019-02-12  Piotr Król <piotr.krol@3mdeb.com>

pub   rsa4096 2021-02-03 [SC] [expires: 2026-02-02]
      0D5F6F1DA800329EB7C597A2ABE1D0BC66278008
uid           [ unknown] 3mdeb Dasharo Master Key
sig!3        ABE1D0BC66278008 2021-02-03  3mdeb Dasharo Master Key
sig!         4AFD81D97BD37C54 2021-02-03  3mdeb Master Key <contact@3mdeb.com>
sub   rsa4096 2021-02-03 [E] [expires: 2026-02-02]
sig!         ABE1D0BC66278008 2021-02-03  3mdeb Dasharo Master Key


pub   rsa4096 2022-05-27 [SC] [expires: 2024-07-06]
      89B569C42BB9FCCBC3C9CFDF5DC481E1F371151E
uid           [ unknown] Dasharo release 1.x compatible with MSI MS-7D25 signing key
sig!3        5DC481E1F371151E 2023-07-07  Dasharo release 1.x compatible with MSI MS-7D25 signing key
sig!         ABE1D0BC66278008 2022-05-27  3mdeb Dasharo Master Key
...
gpg: 7 good signatures


miczyg@thanatos:/tmp$ wget https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.0.0/msi_ms7d25_v1.0.0.rom
--2023-07-27 11:09:10--  https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.0.0/msi_ms7d25_v1.0.0.rom
Resolving dl.3mdeb.com (dl.3mdeb.com)... 178.32.205.96
Connecting to dl.3mdeb.com (dl.3mdeb.com)|178.32.205.96|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 33554432 (32M) [application/octet-stream]
Saving to: ‘msi_ms7d25_v1.0.0.rom’

msi_ms7d25_v1.0.0.r 100%[===================>]  32.00M  17.9MB/s    in 1.8s

2023-07-27 11:09:13 (17.9 MB/s) - ‘msi_ms7d25_v1.0.0.rom’ saved [33554432/33554432]

miczyg@thanatos:/tmp$ wget https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.0.0/msi_ms7d25_v1.0.0.rom.sha256
--2023-07-27 11:09:19--  https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.0.0/msi_ms7d25_v1.0.0.rom.sha256
Resolving dl.3mdeb.com (dl.3mdeb.com)... 178.32.205.96
Connecting to dl.3mdeb.com (dl.3mdeb.com)|178.32.205.96|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 88
Saving to: ‘msi_ms7d25_v1.0.0.rom.sha256’

msi_ms7d25_v1.0.0.r 100%[===================>]      88  --.-KB/s    in 0s

2023-07-27 11:09:20 (123 MB/s) - ‘msi_ms7d25_v1.0.0.rom.sha256’ saved [88/88]

miczyg@thanatos:/tmp$ wget https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.0.0/msi_ms7d25_v1.0.0.rom.sha256.sig
--2023-07-27 11:09:22--  https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.0.0/msi_ms7d25_v1.0.0.rom.sha256.sig
Resolving dl.3mdeb.com (dl.3mdeb.com)... 178.32.205.96
Connecting to dl.3mdeb.com (dl.3mdeb.com)|178.32.205.96|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 833 [application/pgp-signature]
Saving to: ‘msi_ms7d25_v1.0.0.rom.sha256.sig’

msi_ms7d25_v1.0.0.r 100%[===================>]     833  --.-KB/s    in 0s

2023-07-27 11:09:22 (21.0 MB/s) - ‘msi_ms7d25_v1.0.0.rom.sha256.sig’ saved [833/833]

miczyg@thanatos:/tmp$ gpg --verify msi_ms7d25_v1.0.0.rom.sha256.sig msi_ms7d25_v1.0.0.rom.sha256
gpg: Signature made Fri 27 May 2022 10:32:18 AM CEST
gpg:                using RSA key 89B569C42BB9FCCBC3C9CFDF5DC481E1F371151E
gpg: Good signature from "Dasharo release 1.x compatible with MSI MS-7D25 signing key" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 89B5 69C4 2BB9 FCCB C3C9  CFDF 5DC4 81E1 F371 151E

miczyg@thanatos:/tmp$ sha256sum -c msi_ms7d25_v1.0.0.rom.sha256
msi_ms7d25_v1.0.0.rom: OK
```
