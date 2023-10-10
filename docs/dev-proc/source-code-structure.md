# Source code structure

Every repository forked and maintained by Dasharo Release Team has following
branch structure:

* `master` - follows upstream project master branch
* `dasharo/release` - contains all code releases for supported platforms, the
  list of supported platforms is in
  [Hardware Compatibility List](../variants/hardware-compatibility-list.md)
  section
* `dasharo/<platform>_rel_vX.Y.Z` - release branch for version X.Y.Z
* `dasharo/develop` - contains most recent development and is periodically
  synced with tagged releases from the `master` branch.
* `<platform>/<feature>` - tracks development of platform specific feature

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
```

## Tags

Dasharo Release tags in git repository use format: `<platform>_vX.Y.Z`

## New platform support

Branch for new platform should be created from the most recent commit on the
`dasharo/develop` branch. If there is justified need to create support for new
board at arbitrary non-tagged commit developer should mark this commit with
`<platform>_v0.0.0` tag.

## Force-pushes rules

Force-pushes to `dasharo/<platform>_rel_vX.Y.Z`, `dasharo/develop`,
or `<platform>/<feature>` are forbidden with following exceptions:

* rebasing - when some other PR is merged to target branch before our does, or
  when upstream's master introduces the same fixes that our branch would
* squashing - to not produce unnecessary "fix indentation" or "add missing
  braces" commits to the history
* (re-)signing commits (both -S and -s) - shouldn't happen, but if it does
  happen it would be better to have it fixed by original author than the person
  that tries to upstream it some time later.

Force-pushes to  `<platform>/release` branches are unconditionally forbidden.

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
   `develop` branch it may look as follows:

    ```bash
    git fetch dasharo
    git checkout origin/dasharo/develop -b dasharo/develop
    git merge --ff-only origin/<platform>/<feature>
    git push origin dasharo/develop
    ```

1. This should automatically trigger closing the MR and deleting the merged
   branch on GitHub.

1. Note that the merging may fail if the source (in this case: `feature`) branch
   is not properly rebased on top of the target (in this case: `develop`)
   branch. In such a case, one must rebase the source branch first:

   ```bash
   git checkout origin/<platform>/<feature>
   git checkout -b <platform>/<feature>
   git rebase origin/dasharo/develop
   git push -f origin <platform>/<feature>
   ```

> Remember to push the rebased branch _before_ merging it to `dasharo/develop`.
> Otherwise GitHub will not properly detect the merge and won't close the PR
> and delete the source branch.
