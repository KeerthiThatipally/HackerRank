## convert 12 hr clock into 24 hr clock format

import sys

time = input().strip()
##input sample:07:05:45PM
hh=[]
time=time.lower()
hh=time.split(":")

if "pm" in time:

    hh[2] = hh[2].strip("pm")

    if(int(hh[0]) is not 12):
        add = int(hh[0]) + 12
        hh[0] = add
        ret_time = str(hh[0]) + ":" + hh[1] + ':' + hh[2]

    else:
        ret_time=hh[0] + ":" + hh[1] + ':' + hh[2]
    print(ret_time)
else:
    hh[2] = hh[2].strip("am")
    if(hh[0]=="12"):
        hh[0]="00"
        ret_time = hh[0] + ":" + hh[1] + ':' + hh[2]
        print(ret_time)
    else:
        print(hh[0] + ":" + hh[1] + ':' + hh[2])