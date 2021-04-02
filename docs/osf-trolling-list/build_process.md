`[OSFI001]` Build process
-------------------------

# `[OSFI0010]` There is no healthy OSF without reproducible builds

## What are the reproducible builds?

[Reproducible Builds](https://reproducible-builds.org/) and lot of its aspects
is well explained on linked website.

## Why those are in particular important for OSF?

This is because knowing hashes of firmware components we can calculate expected
TPM PCRs values. Knowing good PCR values and being able to predict further
values after firmware update, we gaining following advantages:

* We can easily confirm if firmware is valid by reading TPM PCRs and compare to
  reference integrity measures (RIM), RIM can be calculated by build exactly
  the same version of OSF
* Process of replying measurements provided in TPM Event Log is simpler because
  we can easily obtain software and confirm hashes used during PCR extension
  process was valid and the same as produced by software build process
* Looking for bugs by using bisection is easier since being able to build every
  commit of software in reproducible manner give us confidence that there would
  be no change in behavior between 2 consecutive builds
* Consistent behavior for given hash can be confirmed by test results tied to
  given hash in that way users looking at test results may expect exactly the
  same behavior for firmware binaries with the same hash
* Long term maintenance should be easier if firmware build would be
  reproducible over long time, because often happen some firmware land in
  industrial applications e.g. robots, trains, smart city infrastructure, if
  bug will be detected after long time it is important to have tools and be
  able to confirm the same binary can be generated in future. If we know given
  toolchain reproduce binary bit by bit we are sure it also reproduces
  software/firmware behavior. In that light making small incremental
  improvement using toolchain that give reproducible results give us higher
  chance that we will not introduce uncontrolled change in behavior and code
  change will be reflected by compilation process without affecting previous
  software behavior.

# [OSFI0011] Docker containers as build systems "considered harmful"

Docker containers for couple last years become default method for providing
reproducible runtime environment for software as well those started to be very
useful for developers to transfer exact configuration for building given
software stack. We wrote about usefulness of Docker containers in embedded
software development environment on 
[3mdeb blog](https://blog.3mdeb.com/2018/2018-09-27-optimize-performance-in-docker/).

After long time of using Docker containers for embedded software development
and build environments we noticed problems for long time maintenance and
reproducibility.

## coreboot-sdk problems

Example can be `coreboot-sdk` used for building [coreboot project](https://coreboot.org).

Good summary of the problem was provided by [Thrilleratplay in guix-docker repo](https://github.com/Thrilleratplay/guix-docker#the-problem):

> Currently, the coreboot build environment, `coreboot-sdk`, uses a Debian docker
> base image.  To install additional required packages, `apt-get update` must be
> run.  The resulting docker image is hosted in docker hub repository to be
> retrieved at any time in the future.  However, at any time in the future,
> building the same docker file will generate a different image based on the
> latest packages used in apt-get.  Overtime, as packages are updated due to bug,
> security or feature improvements, the provenance of the docker image in the
> docker hub repository becomes increasingly difficult, if not impossible to
> audit and reproduce.

Some more elaborate notes related to `coreboot-sdk`

1. There is no meaningful versioning of SDK
   [[1]](https://hub.docker.com/r/coreboot/coreboot-sdk/tags) - at some point
   there was versioning 1.32-53, now switched to git SHA. Both seem to have no
   meaning and were released at arbitrary points in time. Result is that it is
   hard to find which version of SDK works with version of coreboot tree.
2. Validation of coreboot-sdk is not sufficient - for example recently python
   fixes were merged [[2]](https://review.coreboot.org/c/coreboot/+/45265), somehow this change passed all QA checks, but SeaBIOS
   use python (not python2 or python3) and all builds using this version of SDK
   that compile SeaBIOS fail.
3. coreboot-sdk is based on moving target Debian sid, it is close to impossible
   to build the same Docker images at 2 different points in time.
4. coreboot-sdk enforce given version of ACPI spec - this may not always be
   good thing to use most recent compiler and update code accordingly, since it
   can easily break OSes.

### Why we care?

1. Whenever we deliver code or service to community or customer we provide
   build environment which, for the sake of quality user support, should be
   stable.
2. CI pipelines rely on those containers. Replacing docker image in CI pipeline
   whenever something change defeat the purpose of having automation and
   increase maintenance cost significantly and increase maintenance cost
   significantly

## Requirements for OSF dev and build process

Open Source Firmware development and build environment SHOULD have:
* meaningful release process, we describe our approach to OSF-related release
  processes [here](#TBD)
* meaningful validation process, at least basic build system and dev env
  capabilities should be tested
* meaningful revisions with clear explanation of what software stack can be build
  with what version of dev and build system, description should include
  side-spec compliance e.g. ACPI, SMBIOS, UEFI etc.
* reproducible process that works across systems and in long run
* signature, so anyone can identify where build and dev env coming from and if
  it is trustworthy

## Ideas for solving above issues

1. Docker images are not reproducible - this is known fact and if we are
   extremely serious about stability, security and quality we should stop using
   not reproducible build environment. Of course there is some work making
   Docker images reproducible, but it opens Pandora's box
   [[3]](https://elinux.org/images/6/62/Building-Container-Images-with-OpenEmbedded-and-the-Yocto-Project-Scott-Murray-Konsulko-Group-1.pdf)
   of Yocto or Buildroot. Other paths could be Nix or Guix, which is currently
   pursued in community [OSFW #guix-buildstack channel](http://osfw.slack.com/)
   - this is private channel, feel free to ping anyone from 3mdeb Team to join.
2. coreboot toolchain is build by its own build system, which would be hard to
   couple with Dockerfile or something else.
3. Docker images can be signed using `docker trust` commands as described
   [here](https://docs.docker.com/engine/security/trust/#signing-images-with-docker-content-trust).

I'm not tracking all activity in community, so some claims may be plain
wrong. Please let me know what I miss when I'm wrong.
