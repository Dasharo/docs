# Source code structure

Every repository forked and maintained by Dasharo Release Team has following
branch structure:

* `master` or `main` - follows upstream project master or main branch
* `dasharo` - contains all code releases for supported platforms, the list of
   supported platforms is in
  [Hardware Compatibility List](../variants/hardware-compatibility-list.md)
  section
* `<platform>/rel_vX.Y.Z` - release branch for version X.Y.Z
* `<feature>` - tracks development of feature

`<platform> = <coreboot_mainboard_vendor>_<coreboot_mainboard_model>` if
platform is supported by coreboot, otherwise we use common sense and available
information about hardware.

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

## Tags

Dasharo Release tags in git repository use format: `<platform>_vX.Y.Z`

## New platform support

Support for new platforms is submitted via PRs to the `dasharo` branch. All
mainboards supported by Dasharo live in this branch.

## Force-pushes rules

Force-pushes to `dasharo` and `master` / `main` are forbidden with the
following exceptions:

* rebasing the `dasharo` branch on new coreboot versions
* (re-)signing commits (both -S and -s) - shouldn't happen, but if it does
  happen it would be better to have it fixed by original author than the person
  that tries to upstream it some time later.

## Rebasing process

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
    git checkout -b common-base-4.21
    git push -u origin common-base-4.21
    ```

1. Rebase the current `dasharo` branch on the latest tag, for example:

    ```bash
    git checkout dasharo
    git rebase 4.22
    ```

    If there are problems with rebase, you may create a different branch, e.g.
    `common-base-4.22` and work until all issues are resolved, then rename the
    branch back to dasharo

    ```bash
    git checkout -b common-base-4.22
    # resolve issues
    git branch -d dasharo
    git branch -M dasharo
    ```

1. Push the new `dasharo` branch:

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
