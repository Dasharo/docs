# Hardware configuration matrix

Configuration with a single IBM POWER9 64bit CPU is supported.
Dual CPU setup not supported currently.

Following RAM configurations were tested and are proved to be properly initialized.

```
MCS0, MCA0
   DIMM0: 1Rx4 16GB PC4-2666V-RC2-12-PA0
   DIMM1: not installed
MCS0, MCA1
   DIMM0: 1Rx8 8GB PC4-2666V-RD1-12
   DIMM1: not installed
MCS1, MCA0
   DIMM0: 2Rx4 32GB PC4-2666V-RB2-12-MA0
   DIMM1: not installed
MCS1, MCA1
   DIMM0: 2Rx8 16GB PC4-2666V-RE2-12
   DIMM1: not installed
```

All 3 major DRAM vendors are supported, namely Samsung, Micron and Hynix.
