# About

This repository contains source code for Dasharo documentation webpage

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
- file where TBD or TODO occurs is displayed (included in nav section of
mkdocs.yml)
- TBD or TODO is visible on website

There should be no TBD or TODO visible on website.

# pre-commit hooks

* [Install pre-commit](https://pre-commit.com/index.html#install)

* Install hooks into repo:

```
pre-commit install
```

* Enjoy automatic checks on each `git commit` action!

* (Optional) Run hooks on all files (for example, when adding new hooks or
  configuring existing ones):

```bash
pre-commit run --all-files
```
