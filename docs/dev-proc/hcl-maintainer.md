# Dasharo HCL Maintainer documentation

This documentaintion aims to describe how to maintain Dasharo Hardware
Compatibility List for CPUs, memory, mainboards and GPU.

## Generating entry

### Dasharo HCL report parsing

For reports uploaded to 3mdeb cloud please use [dedicated
script](https://github.com/Dasharo/dts-hw-conf-gen) readme.

## Extending list

Please always sort table before publishing.

In vim:

- ++shift+v++ - to enter visual mode and mark whole range of entries.
- type `:` and `sort u` to run vim sort function on marked range and leave only
  unique lines.

### Github report

<!--
Current template for adding HCL report over Github issue is way too complex.
Nobody will waste time doing that.
-->

### Github pull request

Go through standard review process for Dasharo documentation.
