# Dasharo HCL Maintainer documentation

This documentaintion aims to describe how to maintain Dasharo Hardware
Compatibility List for CPUs, memory, mainboards and GPU.

## Generating entry

### Dasharo HCL report parsing

Use [dts-hw-conf-gen](https://github.com/Dasharo/dts-hw-conf-gen) tool for
automatic HCL report parsing.

Reports can be sourced from:
- 3mdeb Cloud
- DPP download page

## Extending list

The list can be updated via manual or automatic means.

The HCL tables are located in the [Dasharo docs
repository](https://github.com/Dasharo/docs/tree/master/docs/resources/hcl), and
which can be updated via creating a pull request.

Follow [README.md](https://github.com/Dasharo/dts-hw-conf-gen) for more details.

### Automatic table extension

Automatic table extension is currently supported for `memory` reports only. The
script would insert new, unique lines and automatically sort the table.

This feature is available from
[v1.0.0](https://github.com/Dasharo/dts-hw-conf-gen/releases/tag/v1.0.0) of
dts-hw-conf-gen.

### Github report

<!--
Current template for adding HCL report over Github issue is way too complex.
Nobody will waste time doing that.
-->

### Github pull request

Go through standard review process for Dasharo documentation.
