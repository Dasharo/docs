# About

This repository contains source code for the Dasharo documentation webpage

## Contribution

Please make sure to follow below steps before publishing your changes as a
merge request.

### Local build

```shell
virtualenv -p $(which python3) venv
source venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

By default, it will host a local copy od documentation at:
`http://0.0.0.0:8000/`.

If the following error occurs `OSError: [Errno 98] Address already in use`, try
using a different address by running the command `mkdocs serve -a
localhost:12345` (the number is random).

It is crucial at this point to verify that the pages you have changed
render correctly as HTML in local preview.

### Broken links checker

Currently we are using [lychee](https://github.com/lycheeverse/lychee) a fast,
async, stream-based link checker written in Rust. The automatic check is
triggered on each push to master PR.

You can also run it locally using a docker image:

```bash
$ docker run --init -it --rm -w $(pwd) -v $(pwd):$(pwd) lycheeverse/lychee
    --max-redirects 10 -a 403,429,500,502,503,999 .
```

### Relative links

Please avoid using URL-related links like:

```md
[MSI PRO Z790-P](../../unified/msi/overview)
```

Instead, use relative links within the repository:

```md
[MSI PRO Z790-P](../unified/msi/overview.md)
```

### Make sure no TBD or TODO content is displayed

Find all occurrences:

```shell
grep -E "TBD|TODO" docs/**/*.md -r
```

Iterate over all occurrences and check if:
- file, where TBD or TODO occurs, is displayed (included in nav section of
mkdocs.yml)
- TBD or TODO is visible on the website

There should be no TBD or TODO visible on the website.

### pre-commit hooks

- [Install pre-commit](https://pre-commit.com/index.html#install), if you
  followed [local build](#local-build) procedure `pre-commit` should be
  installed

- [Install go](https://go.dev/doc/install)

- Install hooks into repo:

```shell
pre-commit install
```

- Enjoy automatic checks on each `git commit` action!

- (Optional) Run hooks on all files (for example, when adding new hooks or
  configuring existing ones):

```shell
pre-commit run --all-files
```

#### To skip verification

In some cases, it may be needed to skip `pre-commit` tests. To do that, please
use:

```shell
git commit --no-verify
```

### Embedding videos

Embedding videos with in-line HTML `iframe` tag does not work.
[mkdocs-video](https://github.com/soulless-viewer/mkdocs-video) plugin is used
instead. To embed an video simply type the following in markdown:
`![type:video](https://www.youtube.com/embed/LXb3EKWsInQ)` (example).

## Navigation menu

### Supported hardware

Each subsection of supported hardware should look as follows - there should be
no more sections:

```yaml
    - 'Vendor Model':
        - 'Overview': variants/<vendor_model>/overview.md
        - 'Releases': variants/<vendor_model>/releases.md
        - 'Building manual': variants/<vendor_model>/building-manual.md
        - 'Initial deployment': variants/<vendor_model>/initial-deployment.md
        - 'Firmware update': variants/<vendor_model>/firmware-update.md
        - 'Recovery': variants/<vendor_model>/recovery.md
        - 'Hardware Configuration Matrix': variants/<vendor_model>/hardware-matrix.md
        - 'Test Matrix': variants/<vendor_model>/test-matrix.md
        - 'Security and Privacy (optional)': variants/<vendor_model>/security-and-privacy.md
        - 'Other manuals (optional)': variants/<vendor_model>/other-manuals.md
        - 'FAQ (optional)': variants/<vendor_model>/faq.md
```

- `Vendor` can have multiple meanings, but it can be a vendor who sells the
  platform, OEM or ODM. We tend to follow the naming convention used in
  `coreboot` or other open-source firmware projects. We can consider adjustment
  of the name for SEO reasons, community, or customer demand.
- `Model` in most cases it would include some literal and number, we don't want
  to overload the reader with very precise IDs. As for vendors we try to reuse
  existing open-source firmware conventions, but if needed we can adjust the
  model name.
- `Overview` presents general information related to Dasharo, history, map of
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
