# About

This repository contains source code for Dasharo documentation webpage

# Local build

```shell
virtualenv -p $(which python3) venv
source venv/bin/activate
pip install mkdocs mkdocs-material
mkdocs build
```

# Broken links checker

```shell
cd utils/blc
docker build -t blc .
docker run --network host blc blc http://0.0.0.0:8000 -r|grep BROKEN
```
