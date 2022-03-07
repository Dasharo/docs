# Booting time measurment with cbmem on Ubuntu OS

## Coldboot time measurment

1. Disconnect DUT from power source.

2. Connect back DUT to power source.

3. Power ON DUT.

4. Get `cbmem`.

5. Use below command to look at boot timestamps:  
`sudo cbmem -T`

6. Read timestamp from last row and second column. Last row may look like this:  
`99     4084321 818      selfboot jump`  
In this example we take `4084321` timestamp
7. To get time in seconds, we need to divide timestamp by 1000000.  
`4084321 / 1000000`

***

## Warmboot time measurment

1. Power ON DUT.

2. Power OFF DUT.

3. Power ON DUT.

4. Get `cbmem`.

5. Use below command to look at boot timestamps:  
`sudo cbmem -T`

6. Read timestamp from last row and second column. Last row may look like this:  
`99     4084321 818      selfboot jump`  
In this example we take `4084321` timestamp
7. To get time in seconds, we need to divide timestamp by 1000000.  
`4084321 / 1000000`

***

## Reboot time measurment

1. Power ON DUT.

2. Reboot DUT, using e.g.
`sudo reboot`

3. Get `cbmem`.

4. Use below command to look at boot timestamps:  
`sudo cbmem -T`

5. Read timestamp from last row and second column. Last row may look like this:  
`99     4084321 818      selfboot jump`  
In this example we take `4084321` timestamp
6. To get time in seconds, we need to divide timestamp by 1000000.  
`4084321 / 1000000`
