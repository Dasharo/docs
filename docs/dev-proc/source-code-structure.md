# Source code structure

Every repository forked and maintained by Dasharo Release Team has following
branch structure:

* `master` or `main` - follows upstream project master or main branch
* `dasharo` - contains all code releases for supported platforms, the list of
   supported platforms is in
  [Hardware Compatibility List](../variants/overview.md)
  section
* `<platform>/rel_vX.Y.Z` - release branch for version X.Y.Z
* `<feature>` - tracks development of feature

> `<platform> = <coreboot_mainboard_vendor>_<coreboot_mainboard_model>` if
> platform is supported by coreboot, otherwise we use common sense and available
> information about hardware.

## Remotes

`Dasharo/coreboot` has submodules linked using absolute paths, therefore one
can clone this repository directly.

> Previous guidelines suggested cloning upstream coreboot first and adding
> Dasharo as a separate remote, but this is no longer used **except** when
> building old versions.

Clone the repository and submodules using the following commands:

```bash
git clone git@github.com:Dasharo/coreboot.git
cd coreboot
git submodule update --init --checkout
git remote add upstream https://review.coreboot.org/coreboot.git
```

## Commit message guidelines

### Commit quality

We keep patches for many repositories, but mainly for
[coreboot](https://github.com/Dasharo/coreboot/) and [edk2](https://github.com/Dasharo/edk2).
Even when creating commits in our forks, we should follow the guidelines
of the respective upstream projects, so the future upstream process is easier.

In general, we want ensure that commits getting merged are of a similar quality
as required by upstream projects
([guidelines for coreboot](https://doc.coreboot.org/contributing/gerrit_guidelines.html)).

We want to stress specifically on the following aspects:
* each commit can be built,
* each commit has body message, providing more context, and explaining **why**
the given change was necessary,
* before merging a PR, we squash the changes if necessary, to achieve a similar
granularity as if we would be sending the patch for upstream review.

### Upstream-Status

This is an extra tag in git commit body inspired by how patches are maintained
in the [Yocto Project](https://docs.yoctoproject.org/contributor-guide/recipe-style-guide.html#patch-upstream-status).

The goal is to keep track of which patches should (eventually) be upstreamed,
and which patches are Dasharo-specific.

Currently, following `Upstream-Status` tags are available to choose from:

**`Backport [revision]`**

Patch has been backported from upstream. We should provide unique
identification of the original source of the patch. Possible values for
`revision`:

* `CB:ID` - for coreboot gerrit ID, such as `CB:86758`, translating to:
[CB:86750](https://review.coreboot.org/c/coreboot/+/86750)
* git revision of the upstream project
* link to the mailing message, where the path has been submitted

**`Inappropriate [reason]`**

We believe that patch is not applicable for the upstream project, and provide
some reasining for it. Possible values for `reason`:

* `Dasharo downstream` - patch specific to Dasharo distribution
* other explanation - although we should try to avoid it

**`Pending`**

Patch classified as one for sending upstream, but not yet submitted.

**`Submitted [where]`**

Submitted to upstream. Possible value for `where`:

* `CB:ID` - for coreboot gerrit ID, such as `CB:86758`, translating to:
[CB:86750](https://review.coreboot.org/c/coreboot/+/86750)
* for other cases, link to the review system should be provided

## Tags

Tags for Dasharo releases across repositories in the Dasharo GitHub organization
use the following format: `<platform>_vX.Y.Z`.

> `<platform> = <coreboot_mainboard_vendor>_<coreboot_mainboard_model>` if
> platform is supported by coreboot, otherwise we use common sense and available
> information about hardware.

## New platform support

Support for new platforms is submitted via PRs to the `dasharo` branch. All
mainboards supported by Dasharo live in this branch.

## Force-pushes rules

Force-pushes to `dasharo` and `master` / `main` are forbidden with the
exception of rebasing the `dasharo` branch on new coreboot versions.

## Rebase process

1. Update `master` / `main` branch to the recent coreboot upstream tag
   (and fetch tags as well)

    ```bash
    git checkout main
    git fetch upstream
    git pull upstream `git describe --tags upstream/main --abbrev=0`
    ```

1. Backup the old `dasharo` branch, for example:

    ```bash
    git checkout dasharo
    git checkout -b dasharo-4.21
    git push -u origin dasharo-4.21
    ```

1. Rebase the current `dasharo` branch on the latest tag, for example:

    ```bash
    git checkout -b dasharo-4.22
    git rebase 4.22
    ```

1. Resolve conflicts, build issues and run tests.

1. When issues are resolved and testing is completed, rename the branch to
    `dasharo`:

    ```bash
    git branch -d dasharo
    git branch -M dasharo
    ```

1. Push the new `dasharo` branch:

    !!! info

        Only repository admin can force-push to protected branches. Contact your
        TL to finish this step.

    ```bash
    git push -f origin dasharo
    ```

## Merging guidelines

We want to keep the history linear. The `rebase` merging strategy is desired.
Merge commits in the code repositories are not allowed. The `rebase` strategy
should be the only one available in the GitHub web UI.

> Keeping the git history linear makes it easier to bisect issues and rebase
> commits.

It is, however, **strongly advised not to use GitHub web UI** to perform code
merges. The `signed-off` tends to be dropped (even when using the `rebase`
strategy), which is problematic for some projects (e.g. it makes the coreboot
lint checks fail after merging from the UI).

The procedure of merging is as follows:

1. Review the code in GitHub.
1. Make sure to receive at least one `Approve` in the review process.
1. Make sure that **all** change requests are resolved.
1. Merge the branch using git CLI. In case of merging the `feature` branch into
   `dasharo` branch it may look as follows:

    ```bash
    git fetch dasharo
    git checkout origin/dasharo -b dasharo
    git merge --ff-only origin/<feature>
    git push origin dasharo
    ```

1. This should automatically trigger closing the MR and deleting the merged
   branch on GitHub.

1. Note that the merging may fail if the source (in this case: `feature`) branch
   is not properly rebased on top of the target (in this case: `dasharo`)
   branch. In such a case, one must rebase the source branch first:

    ```bash
    git checkout origin/<feature>
    git checkout -b <feature>
    git rebase origin/dasharo
    git push -f origin <feature>
    ```

> Remember to push the rebased branch _before_ merging it to `dasharo`.
> Otherwise GitHub will not properly detect the merge and won't close the PR
> and delete the source branch. You should also wait for CI to pass without
> errors before merging, in rare cases where a rebase breaks something.

## Hotfixes

For fixes for important issues discovered after release, create a new branch
from the release tag, called `<platform>/rel_vx_y_z`, where the version number
matches the release version. Commit fixes into this branch and when finished,
bump the `z` (patch version) component of the version number.

Fixes from this branch should be merged later back into `dasharo`. Branching
from the previous release tag helps avoid introducing breaking changes that may
have been merged to `dasharo` in the time after the affected release has been
published.
