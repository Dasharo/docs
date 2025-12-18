#!/bin/bash

repo=$(mktemp -d)
git clone https://github.com/Dasharo/dts-configs $repo &> /dev/null
python "$(dirname "$(realpath "$0")")"/trustroot-support.py "$repo" --pretty
rm -rf "$repo"
