# About

This repository contains source code for the Dasharo documentation webpage

# Local build

```shell
virtualenv -p $(which python3) venv
source venv/bin/activate
pip install -r requirements.txt
mkdocs build
```

# Broken links checker

```shell
cd utils/blc
docker build -t blc .
docker run --network host blc blc http://0.0.0.0:8000 -r|grep BROKEN
```

# Make sure no TBD or TODO content is displayed

Find all occurrences:

```shell
grep -E "TBD|TODO" docs/**/*.md -r
```

Iterate over all occurrences and check if:
- file, where TBD or TODO occurs, is displayed (included in nav section of
mkdocs.yml)
- TBD or TODO is visible on the website

There should be no TBD or TODO visible on the website.

# pre-commit hooks

- [Install pre-commit](https://pre-commit.com/index.html#install), if you
  followed [local build](#local-build) procedure `pre-commit` should be
  installed

- [Install go](https://go.dev/doc/install)

- Install hooks into repo:

```bash
pre-commit install --hook-type commit-msg
```

- Enjoy automatic checks on each `git commit` action!

- (Optional) Run hooks on all files (for example, when adding new hooks or
  configuring existing ones):

```bash
pre-commit run --all-files
```

## To skip verification

In some cases, it may be needed to skip `pre-commit` tests. To do that, please
use:

```bash
git commit --no-verify
```

# Navigation menu

## Supported hardware

Each subsection of supported hardware should look as follows there should no
more section

```yaml
    - 'Vendor Model':
        - 'Overview': variants/<vendor_model>/overview.md
        - 'Releases': variants/<vendor_model>/releases.md
        - 'Building manual': variants/<vendor_model>/building-manual.md
        - 'Initial deployment': variants/<vendor_model>/initial-deployment.md
        - 'Firmware update': variants/<vendor_model>/firmware-update.md
        - 'Recovery': variants/<vendor_model>/recovery.md
        - 'Hardware Configuration Matrix': variants/<vendor_model>/hardware-matrix.md
        - 'Test Matrix': variants/<vendor_model>/hardware-matrix.md
        - 'Community Test Results (optional)': variants/<vendor_model>/community-test-results.md
        - 'Security and Privacy (optional)': variants/<vendor_model>/security-and-privacy.md
        - 'Other manuals (optional)': variants/<vendor_model>/other-manuals.md
        - 'FAQ': variants/<vendor_model>/hardware-matrix.md
```

- `Vendor` can have multiple meanings, but it can be a vendor who sells the
  platform, OEM or ODM. We tend to follow the naming convention used in
  `coreboot` or other open-source firmware projects. We can consider adjustment
  of the name for SEO reasons, community, or customer demand.
- `Model` in most cases it would include some literal and number, we don't want
  to overload the reader with very precise IDs. As for vendors we try to reuse
  existing open-source firmware conventions, but if needed we can adjust the
  model name.
- 'Overview' presents general information related to Dasharo, history, map of
  subsections, marketing materials, and press release links.
- `Releases` section where all binaries are provided in a standardized way.
- `Building manual` section provides instructions on how to build release and
  debug binaries in a reproducible manner.
- `Firmware update` section explains all methods to update the firmware. If
  additional steps are needed to perform updates between specific versions it,
should also be covered in this section.
- `Recovery` section describes what to do in case of various error signatures
  e.g. platform not booting or hanging in a particular place.
- `Hardware Configuration Matrix` - presents the configuration used in Dasharo
  labs to perform validation as well as a community-contributed hardware
  compatibility reports, which present CPUs, GPUs, memory modules, and other
  components tested by community.
- `Test Matrix` - presents a list of tests that we execute during the release
  process.
- `Community Test Results` - an optional section that presents test results
  contributed by the community.
- `Security and Privacy` - an optional section that provides security-related
  information, like the size of the trusted computing base (via Dasharo
  Openness Score), manuals on how to use verified boot, measured boot, or UEFI
  Secure Boot.
- `Other manuals` - an optional section that provides other manuals, such as:
  how to enable fan control, update EC controller, customize logo etc.
- `FAQ` - frequently asked questions related to a given hardware platform and
  Dasharo support for it.
