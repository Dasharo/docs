# Boot logo replacement instructions

## Introduction

The logo displayed at boot can be customized according to the client's
preferences. For this, we have created a script that automates the process of
replacing the logo.

## Procedure

Use the [Dasharo Configuration Utility](https://github.com/Dasharo/dcu#usage)
to put custom logo into a Dasharo coreboot image.

```bash
./dcu logo <dasharo_image> -l <logo_file>
```
