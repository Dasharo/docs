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

2. Check the signatures on the keys:

    ```bash
    gpg --check-signatures "Dasharo" "3mdeb"
    ```

3. Optionally set the trust level on the imported keys (if you have not done
   so yet), for example `Dasharo Master Key`:

    ```bash
    gpg --edit-key 0D5F6F1DA800329EB7C597A2ABE1D0BC66278008
    gpg (GnuPG) 2.4.3; Copyright (C) 2023 g10 Code GmbH
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.


    pub  rsa4096/ABE1D0BC66278008
        created: 2021-02-03  expires: 2026-02-02  usage: SC
        trust: undefined     validity: undefined
    sub  rsa4096/EF3E219237E312A8
        created: 2021-02-03  expires: 2026-02-02  usage: E
    [  undef ] (1). 3mdeb Dasharo Master Key

    gpg> trust
    pub  rsa4096/ABE1D0BC66278008
        created: 2021-02-03  expires: 2026-02-02  usage: SC
        trust: undefined     validity: undefined
    sub  rsa4096/EF3E219237E312A8
        created: 2021-02-03  expires: 2026-02-02  usage: E
    [  undef ] (1). 3mdeb Dasharo Master Key

    Please decide how far you trust this user to correctly verify other users' keys
    (by looking at passports, checking fingerprints from different sources, etc.)

        1 = I don't know or won't say
        2 = I do NOT trust
        3 = I trust marginally
        4 = I trust fully
        5 = I trust ultimately
        m = back to the main menu

    Your decision? 5
    Do you really want to set this key to ultimate trust? (y/N) y

    pub  rsa4096/ABE1D0BC66278008
        created: 2021-02-03  expires: 2026-02-02  usage: SC
        trust: ultimate      validity: undefined
    sub  rsa4096/EF3E219237E312A8
        created: 2021-02-03  expires: 2026-02-02  usage: E
    [  undef ] (1). 3mdeb Dasharo Master Key
    Please note that the shown key validity is not necessarily correct
    unless you restart the program.
    ```

    Setting the trust level of master key to ultimate will imply the full trust
    of the release signing keys. With full trust in the release signing keys,
    the warning:

    ```bash
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.
    ```

    will not appear (full trust or stronger). Set the trust level based on how
    you trust the keys (if you have validated them properly, obtained from
    legitimate source, etc.). After exiting the gpg program and editing the key
    again the trust level will be updated:

    ```bash
    gpg --edit-key 0D5F6F1DA800329EB7C597A2ABE1D0BC66278008
    gpg (GnuPG) 2.4.3; Copyright (C) 2023 g10 Code GmbH
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.


    gpg: checking the trustdb
    gpg: marginals needed: 3  completes needed: 1  trust model: pgp
    gpg: depth: 0  valid:   4  signed:  10  trust: 0-, 0q, 0n, 0m, 0f, 4u
    gpg: depth: 1  valid:  10  signed:   0  trust: 10-, 0q, 0n, 0m, 0f, 0u
    gpg: next trustdb check due at 2024-03-24
    pub  rsa4096/ABE1D0BC66278008
        created: 2021-02-03  expires: 2026-02-02  usage: SC
        trust: ultimate      validity: ultimate
    sub  rsa4096/EF3E219237E312A8
        created: 2021-02-03  expires: 2026-02-02  usage: E
    [ultimate] (1). 3mdeb Dasharo Master Key
    ```

4. Download the binaries, SHA sums and their signature files

    ```bash
    export BIN_URL=https://3mdeb.com/open-source-firmware/Dasharo/...
    ```

    ```bash
    wget ${BIN_URL} ${BIN_URL}.sha256 ${BIN_URL}.sha256.sig
    ```

5. Verify the signatures and binary integrity:

    ```bash
    gpg -v --verify `basename $BIN_URL`.sha256.sig `basename $BIN_URL`.sha256
    ```

    ```bash
    sha256sum -c `basename $BIN_URL`.sha256
    ```

Example verification of Dasharo release compatible with MSI PRO Z690-A DDR4:

```bash
miczyg@3M08:~ $ export BIN_URL=https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr4.rom
miczyg@3M08:~ $ wget ${BIN_URL} ${BIN_URL}.sha256 ${BIN_URL}.sha256.sig
--2023-08-02 10:44:13--  https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr4.rom
Resolving 3mdeb.com (3mdeb.com)... 2001:41d0:301:5::26, 178.32.205.96
Connecting to 3mdeb.com (3mdeb.com)|2001:41d0:301:5::26|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr4.rom [following]
--2023-08-02 10:44:14--  https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr4.rom
Resolving dl.3mdeb.com (dl.3mdeb.com)... 178.32.205.96
Connecting to dl.3mdeb.com (dl.3mdeb.com)|178.32.205.96|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 33554432 (32M) [application/octet-stream]
Saving to: ‘msi_ms7d25_v1.1.1_ddr4.rom’

msi_ms7d25_v1.1.1_d 100%[===================>]  32.00M  24.4MB/s    in 1.3s

2023-08-02 10:44:15 (24.4 MB/s) - ‘msi_ms7d25_v1.1.1_ddr4.rom’ saved [33554432/33554432]

--2023-08-02 10:44:15--  https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr4.rom.sha256
Connecting to 3mdeb.com (3mdeb.com)|2001:41d0:301:5::26|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr4.rom.sha256 [following]
--2023-08-02 10:44:16--  https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr4.rom.sha256
Connecting to dl.3mdeb.com (dl.3mdeb.com)|178.32.205.96|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 93
Saving to: ‘msi_ms7d25_v1.1.1_ddr4.rom.sha256’

msi_ms7d25_v1.1.1_d 100%[===================>]      93  --.-KB/s    in 0s

2023-08-02 10:44:16 (49.8 MB/s) - ‘msi_ms7d25_v1.1.1_ddr4.rom.sha256’ saved [93/93]

--2023-08-02 10:44:16--  https://3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr4.rom.sha256.sig
Connecting to 3mdeb.com (3mdeb.com)|2001:41d0:301:5::26|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr4.rom.sha256.sig [following]
--2023-08-02 10:44:16--  https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/v1.1.1/msi_ms7d25_v1.1.1_ddr4.rom.sha256.sig
Connecting to dl.3mdeb.com (dl.3mdeb.com)|178.32.205.96|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 833 [application/pgp-signature]
Saving to: ‘msi_ms7d25_v1.1.1_ddr4.rom.sha256.sig’

msi_ms7d25_v1.1.1_d 100%[===================>]     833  --.-KB/s    in 0s

2023-08-02 10:44:17 (11.5 MB/s) - ‘msi_ms7d25_v1.1.1_ddr4.rom.sha256.sig’ saved [833/833]

gpg -v --verify `basename $BIN_URL`.sha256.sig `basename $BIN_URL`.sha256
FINISHED --2023-08-02 10:44:17--
Total wall clock time: 3.3s
Downloaded: 3 files, 32M in 1.3s (24.4 MB/s)
gpg: enabled compatibility flags:
gpg: Signature made Thu 23 Feb 2023 12:21:55 AM CET
gpg:                using RSA key 89B569C42BB9FCCBC3C9CFDF5DC481E1F371151E
gpg: using pgp trust model
gpg: Good signature from "Dasharo release 1.x compatible with MSI MS-7D25 signing key" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 89B5 69C4 2BB9 FCCB C3C9  CFDF 5DC4 81E1 F371 151E
gpg: binary signature, digest algorithm SHA256, key algorithm rsa4096

miczyg@3M08:~ $sha256sum -c `basename $BIN_URL`.sha256
msi_ms7d25_v1.1.1_ddr4.rom: OK
```
