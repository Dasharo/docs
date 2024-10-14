# Reproducible build verification

[Reproducible builds](https://reproducible-builds.org/) are crucial from both 
security and open-source perspectives because they allow anyone to verify that 
the compiled binary of a software package truly matches the original source 
code. This ensures that no tampering, such as inserting malicious code during 
the build process, has occurred. 

The most obvious and undisputable way of verifying build reproduction is 
comparing `sha256` or `md5` hashes of two given binaries. There are, however, 
corner cases where this is not an ideal approach.

## Romscope

To account for corner cases and to enable a more extensive approach to 
comparing two Dasharo binaries which are supposed to have been build from the 
same source, we have developed 
[romscope](https://github.com/Dasharo/romscope).

As explained in the `README`:

>Consider the scenario: we have a release candidate binary and a final binary.
 Only the version number was changed in the code. We want to prove that changing
 the version number functionally does not influence any other portion of the 
 binary, which ensures that test results for the release candidate are also 
 valid for the final binary.

### Procedure

As an example, let's try to compare a NovaCustom NV4x ADL Dasharo version 1.7.2 
binary obtained from our 
[Releases page](https://docs.dasharo.com/variants/novacustom_nv4x_adl/releases/)
to a binary we will build from source for the same target.

* Obtain the official release binary
* Follow the [Building manual](https://docs.dasharo.com/unified/novacustom/building-manual/#nv4x-12th-gen)
  for NV4x 12th Gen, substituting `1.7.2` for `X.Y.Z` where necessary
* Create a common `romscope-test` directory and enter it
  ```bash
  mkdir romscope-test
  cd romscope-test
  ```
* Place both the downloaded release binary and your build result in the 
  directory, renaming the build result to `nv4x_adl_built.rom`
* Calculate the `sha256` hash of the binaries:
  ```bash
  λ sha256sum *.rom
  00b6338389cc5d020b641629971aac6d4047be6134c6e8d0228140edc42584f6  novacustom_nv4x_adl_v1.7.2.rom
  c8beae48e72adc664a837c990ca89f6b1bb77399cb577e3f7b57206f0a6f0027  nv4x_adl_built.rom
  ```

As you can see, the hashes don't match, indicating a difference between the
binaries. Does that mean the binary you have downloaded is really not the same
as what you have built from source, and maybe even that the code for the 
release binary contains some malicious "hidden features"? That is precisely
what we will find out using the `romscope` utility.

* Clone the `romscope` repository into `romscope-test` and enter it:
  ```bash
  git clone https://github.com/dasharo/romscope
  cd romscope
  ```

For the purpose of reproducible build verification, we will use the `romscope 
compare` command. 

```bash
λ ./romscope compare ../novacustom_nv4x_adl_v1.7.2.rom ../nv4x_adl_built.rom
Extracting file /home/flewinski/workspace/rep-builds-docs/novacustom_nv4x_adl_v1.7.2.rom
Extracting file /home/flewinski/workspace/rep-builds-docs/nv4x_adl_built.rom
Vblock regions/fmap/VBLOCK_A.bin differs.
Vblock regions/fmap/GBB.bin differs.
Files match but signatures differ. Binaries are likely signed using different Vboot keys.
```

